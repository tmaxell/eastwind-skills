#!/usr/bin/env python3
"""Extract the colors and fonts actually used in a file and diff them against the
Eastwind tokens.

Deterministic half of a brand review: catches off-palette values and near-misses
that the eye does not. Judgement — hierarchy, composition, whether the layout has
air — is not its job.

    python3 check_brand.py <file> [<file> ...]
    python3 check_brand.py --tolerance 12 deck.pptx

Handles .pptx .docx .xlsx (OOXML), .pdf, .svg, .html/.htm/.css.
Needs only the standard library. tokens.json must sit next to this script or one
directory up.

Optional and never required: the review procedure works without it.
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys
import zipfile

HEX_RE = re.compile(r"#([0-9A-Fa-f]{6})\b|#([0-9A-Fa-f]{3})\b")
RGB_FN_RE = re.compile(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)")
OOXML_HEX_RE = re.compile(r'(?:val|fill|color|srgbClr[^>]*val)="([0-9A-Fa-f]{6})"')
OOXML_FONT_RE = re.compile(r'(?:typeface|w:ascii|w:hAnsi|w:cs)="([^"]{1,64})"')
PDF_RGB_RE = re.compile(
    r"(?<![\d.])([01](?:\.\d+)?)\s+([01](?:\.\d+)?)\s+([01](?:\.\d+)?)\s+(?:rg|scn)\b"
)
# Matches both `font-family: X, Y` and the `font: 400 16px/1.5 X, Y` shorthand.
CSS_FONT_RE = re.compile(r"font(?:-family)?\s*:\s*([^;}\"']+)", re.I)
SVG_FONT_RE = re.compile(r'font-family="([^"]+)"')
# Strips the `400 16px/1.5 ` head of a shorthand so only the family survives.
SHORTHAND_HEAD_RE = re.compile(r"^[\d.]+\s+[\d.]+[a-z%]*(?:\s*/\s*[\d.]+[a-z%]*)?\s+", re.I)
CSS_KEYWORDS = {
    "normal", "bold", "bolder", "lighter", "italic", "oblique", "small-caps",
    "inherit", "initial", "unset", "revert", "serif", "sans-serif", "monospace",
    "cursive", "fantasy", "system-ui", "ui-sans-serif", "ui-serif", "ui-monospace",
    "-apple-system", "blinkmacsystemfont", "caption", "icon", "menu", "status-bar",
}

# Colors that carry no brand meaning and would only add noise.
IGNORED = {"#FFFFFF", "#000000"}

APPROVED_FONTS = {
    "tt firs neue", "tt firs neue variable", "raleway", "arial", "noto",
}


def load_tokens(script_dir: pathlib.Path) -> dict:
    for candidate in (script_dir / "tokens.json", script_dir.parent / "tokens.json"):
        if candidate.exists():
            return json.loads(candidate.read_text(encoding="utf-8"))
    sys.exit("tokens.json not found next to this script or one directory up")


def palette(tokens: dict) -> dict[str, str]:
    """hex -> human name, e.g. '#382DDD' -> 'brand 70'."""
    out: dict[str, str] = {}
    for family, data in tokens["scales"].items():
        for step, hx in data["steps"].items():
            out.setdefault(hx.upper(), f"{family} {step}")
    for hue, data in tokens["decorative"].items():
        for step, hx in data["steps"].items():
            out.setdefault(hx.upper(), f"{hue} {step}")
    for state, data in tokens["system"].items():
        for step, hx in data["steps"].items():
            out.setdefault(hx.upper(), f"system {state} {step}")
    return out


def norm_hex(value: str) -> str:
    value = value.lstrip("#").upper()
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    return "#" + value


def rgb(hx: str) -> tuple[int, int, int]:
    hx = hx.lstrip("#")
    return tuple(int(hx[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def distance(a: str, b: str) -> float:
    """Rough perceptual distance. Good enough to separate drift from a new color."""
    r1, g1, b1 = rgb(a)
    r2, g2, b2 = rgb(b)
    rm = (r1 + r2) / 2
    return (
        (2 + rm / 256) * (r1 - r2) ** 2
        + 4 * (g1 - g2) ** 2
        + (2 + (255 - rm) / 256) * (b1 - b2) ** 2
    ) ** 0.5


CONTENT_PART_RE = re.compile(
    r"^(word/(document|header\d*|footer\d*)\.xml"
    r"|ppt/slides/slide\d+\.xml"
    r"|xl/worksheets/sheet\d+\.xml)$"
)


def from_ooxml(path: pathlib.Path):
    colors: collections.Counter = collections.Counter()
    used: collections.Counter = collections.Counter()
    declared: collections.Counter = collections.Counter()
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.endswith(".xml"):
                continue
            # Office theme defaults and the font table are declarations, not
            # authored choices — counting them buries the real findings.
            if "/theme/" in name or name.endswith(("fontTable.xml", "settings.xml")):
                continue
            text = z.read(name).decode("utf-8", "ignore")
            for hx in OOXML_HEX_RE.findall(text):
                colors[norm_hex(hx)] += 1
            if name.endswith("word/styles.xml"):
                # docDefaults sets the face for every run that does not override
                # it, so it is the document's actual font, not a latent style.
                defaults = re.search(r"<w:docDefaults>.*?</w:docDefaults>", text, re.S)
                if defaults:
                    for f in OOXML_FONT_RE.findall(defaults.group(0)):
                        used[f.strip()] += 1
                    text = text.replace(defaults.group(0), "")
                bucket = declared
            else:
                bucket = used if CONTENT_PART_RE.match(name) else declared
            for f in OOXML_FONT_RE.findall(text):
                bucket[f.strip()] += 1
    for f in used:
        declared.pop(f, None)
    return colors, used, declared


def from_pdf(path: pathlib.Path):
    colors: collections.Counter = collections.Counter()
    fonts: collections.Counter = collections.Counter()
    try:
        import pypdf
    except ImportError:
        print("  note: pypdf is not installed, PDF colors were not read", file=sys.stderr)
        return colors, fonts, collections.Counter()

    def forms(obj, depth=0, seen=None):
        seen = seen if seen is not None else set()
        try:
            yield obj.get_data()
        except Exception:
            pass
        res = obj.get("/Resources")
        if res and depth < 6:
            xobjects = res.get("/XObject")
            if xobjects:
                for key in xobjects:
                    inner = xobjects[key].get_object()
                    if id(inner) in seen:
                        continue
                    seen.add(id(inner))
                    if inner.get("/Subtype") == "/Form":
                        yield from forms(inner, depth + 1, seen)

    reader = pypdf.PdfReader(str(path))
    for page in reader.pages:
        blob = page.get_contents().get_data()
        resources = page.get("/Resources") or {}
        xobjects = resources.get("/XObject")
        if xobjects:
            for key in xobjects:
                for chunk in forms(xobjects[key].get_object()):
                    blob += chunk
        text = blob.decode("latin-1", "ignore")
        for m in PDF_RGB_RE.finditer(text):
            channels = tuple(round(float(m.group(i)) * 255) for i in (1, 2, 3))
            colors["#%02X%02X%02X" % channels] += 1
        for font in (resources.get("/Font") or {}).values():
            base = font.get_object().get("/BaseFont")
            if base:
                fonts[re.sub(r"^/[A-Z]{6}\+", "", str(base)).lstrip("/")] += 1
    return colors, fonts, collections.Counter()


def from_text(path: pathlib.Path):
    colors: collections.Counter = collections.Counter()
    fonts: collections.Counter = collections.Counter()
    text = path.read_text(encoding="utf-8", errors="ignore")
    for six, three in HEX_RE.findall(text):
        colors[norm_hex(six or three)] += 1
    for r_, g_, b_ in RGB_FN_RE.findall(text):
        colors["#%02X%02X%02X" % (int(r_), int(g_), int(b_))] += 1
    for stack in CSS_FONT_RE.findall(text) + SVG_FONT_RE.findall(text):
        stack = SHORTHAND_HEAD_RE.sub("", stack.strip())
        for part in stack.split(","):
            part = part.strip().strip("\"'")
            if not part or part.startswith("var(") or "/" in part:
                continue
            if part.lower() in CSS_KEYWORDS or any(ch.isdigit() for ch in part):
                continue
            fonts[part] += 1
    return colors, fonts, collections.Counter()


def read_file(path: pathlib.Path):
    suffix = path.suffix.lower()
    if suffix in (".pptx", ".docx", ".xlsx", ".potx", ".dotx"):
        return from_ooxml(path)
    if suffix == ".pdf":
        return from_pdf(path)
    if suffix in (".svg", ".html", ".htm", ".css", ".md", ".txt", ".json"):
        return from_text(path)
    sys.exit(f"unsupported file type: {path.name}")


def report(path: pathlib.Path, tokens: dict, tolerance: float) -> int:
    colors, fonts, declared = read_file(path)
    known = palette(tokens)
    findings = 0

    print(f"\n{path.name}")
    print(f"  {sum(colors.values())} color uses, {len(colors)} distinct")

    exact, drift, unknown = [], [], []
    for hx, count in colors.most_common():
        if hx in IGNORED:
            continue
        if hx in known:
            exact.append((hx, known[hx], count))
            continue
        nearest = min(known, key=lambda k: distance(hx, k))
        if distance(hx, nearest) <= tolerance:
            drift.append((hx, nearest, known[nearest], count))
        else:
            unknown.append((hx, nearest, known[nearest], count))

    if drift:
        print(f"  DRIFT — near a token but not equal to it ({len(drift)}):")
        for hx, near, name, count in drift:
            print(f"    {hx} ×{count:<4} -> should be {near} ({name})")
            findings += 1
    if unknown:
        print(f"  OFF-PALETTE ({len(unknown)}):")
        for hx, near, name, count in unknown:
            print(f"    {hx} ×{count:<4} nearest token {near} ({name}), d={distance(hx, near):.0f}")
            findings += 1
    if exact:
        preview = ", ".join(f"{h} {n}" for h, n, _ in exact[:8])
        print(f"  on palette ({len(exact)}): {preview}{' …' if len(exact) > 8 else ''}")

    off_brand = lambda names: sorted(
        {n for n in names if not any(a in n.lower() for a in APPROVED_FONTS)}
    )

    if fonts:
        offenders = off_brand(fonts)
        approved = sorted(set(fonts) - set(offenders))
        if approved:
            print(f"  fonts in content, on brand: {', '.join(approved)}")
        if offenders:
            print(f"  FONTS OFF BRAND, in content: {', '.join(offenders)}")
            findings += len(offenders)

    latent = off_brand(declared)
    if latent:
        print(
            f"  note — declared in styles but not used in the content: "
            f"{', '.join(latent)}. Harmless until someone applies the style."
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+")
    parser.add_argument(
        "--tolerance",
        type=float,
        default=40.0,
        help="distance below which an off-palette color is reported as drift "
        "from the nearest token rather than as a new color (default 40)",
    )
    args = parser.parse_args()

    tokens = load_tokens(pathlib.Path(__file__).resolve().parent)
    total = 0
    for name in args.files:
        path = pathlib.Path(name)
        if not path.exists():
            print(f"missing: {name}", file=sys.stderr)
            total += 1
            continue
        total += report(path, tokens, args.tolerance)

    print(f"\n{total} finding(s). Colors and fonts only — composition, hierarchy, "
          "logo handling, and imagery still need a human or a model to look.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
