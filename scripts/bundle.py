#!/usr/bin/env python3
"""Bundle a skill for platforms that are not Claude Code.

Produces two artifacts in dist/:

  <skill>.md   single self-contained file with every referenced .md inlined,
               for ChatGPT project instructions or a custom GPT
  <skill>.zip  the folder as-is, for uploading to claude.ai Skills

    python3 scripts/bundle.py eastwind-brand
    python3 scripts/bundle.py --all
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)#]+?)\)")
TEXT_SUFFIXES = {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}
SKIP_NAMES = {".DS_Store", ".gitkeep"}

# ChatGPT project instructions have a practical ceiling; warn before it bites.
SIZE_WARN_CHARS = 30_000


def split_frontmatter(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :]).lstrip("\n")
    return "", text


def frontmatter_value(raw: str, key: str) -> str:
    for line in raw.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return ""


def collect_local_links(text: str) -> list[str]:
    out: list[str] = []
    for _, target in LINK_RE.findall(text):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target not in out:
            out.append(target)
    return out


def build_markdown(skill_dir: Path) -> str:
    name = skill_dir.name
    raw_fm, body = split_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    description = frontmatter_value(raw_fm, "description")

    parts: list[str] = []
    parts.append(f"# Skill: {name}\n")
    if description:
        parts.append(
            "**When this applies.** " + description + "\n\n"
            "Follow the instructions below whenever the request matches. When it does "
            "not, ignore this document entirely.\n"
        )
    parts.append("---\n")
    parts.append(body.rstrip() + "\n")

    # Inline every local .md the body links to, then anything else in references/.
    inlined: set[Path] = set()
    queue = [
        (skill_dir / t).resolve()
        for t in collect_local_links(body)
        if (skill_dir / t).resolve().suffix == ".md"
    ]
    refs = skill_dir / "references"
    if refs.is_dir():
        queue += sorted(p.resolve() for p in refs.glob("*.md"))

    appendix: list[str] = []
    while queue:
        path = queue.pop(0)
        if path in inlined or not path.exists() or not path.is_file():
            continue
        inlined.add(path)
        rel = path.relative_to(skill_dir)
        content = path.read_text(encoding="utf-8")
        _, content_body = split_frontmatter(content)
        appendix.append(f"\n---\n\n## Appendix: {rel.as_posix()}\n\n{content_body.rstrip()}\n")
        for t in collect_local_links(content_body):
            nxt = (path.parent / t).resolve()
            if nxt.suffix == ".md" and nxt not in inlined:
                queue.append(nxt)

    if appendix:
        parts.append(
            "\n---\n\n"
            "# Appendices\n\n"
            "The documents the instructions above refer to are reproduced below. "
            "Read the relevant appendix instead of trying to open the file.\n"
        )
        parts.extend(appendix)

    binaries = [
        p for p in sorted(skill_dir.rglob("*"))
        if p.is_file()
        and p.suffix.lower() not in TEXT_SUFFIXES
        and p.name not in SKIP_NAMES
    ]
    if binaries:
        listing = "\n".join(f"- `{p.relative_to(skill_dir).as_posix()}`" for p in binaries)
        parts.append(
            "\n---\n\n"
            "# Files to attach\n\n"
            "These files could not be inlined. Attach them to the project knowledge "
            "if the task needs them:\n\n" + listing + "\n"
        )

    return "\n".join(parts)


def build_zip(skill_dir: Path, out: Path) -> None:
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if not path.is_file() or path.name in SKIP_NAMES:
                continue
            zf.write(path, Path(skill_dir.name) / path.relative_to(skill_dir))


def bundle(skill_dir: Path) -> None:
    DIST_DIR.mkdir(exist_ok=True)
    name = skill_dir.name

    md = build_markdown(skill_dir)
    md_path = DIST_DIR / f"{name}.md"
    md_path.write_text(md, encoding="utf-8")

    zip_path = DIST_DIR / f"{name}.zip"
    build_zip(skill_dir, zip_path)

    print(f"{name}")
    print(f"  {md_path.relative_to(ROOT)}   {len(md):,} chars")
    print(f"  {zip_path.relative_to(ROOT)}  {zip_path.stat().st_size:,} bytes")
    if len(md) > SIZE_WARN_CHARS:
        print(
            f"  warn: {len(md):,} chars may exceed a ChatGPT project instructions "
            "limit; move detail into attached knowledge files"
        )


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2

    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))
    if args != ["--all"]:
        by_name = {d.name: d for d in dirs}
        missing = [a for a in args if a not in by_name]
        if missing:
            print(f"unknown skill(s): {', '.join(missing)}", file=sys.stderr)
            return 2
        dirs = [by_name[a] for a in args]

    for d in dirs:
        if not (d / "SKILL.md").exists():
            print(f"skipping {d.name}: no SKILL.md", file=sys.stderr)
            continue
        bundle(d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
