#!/usr/bin/env python3
"""Validate Eastwind skills.

Checks the things that break silently: frontmatter shape, portability rules,
size limits, broken relative links.

    python3 scripts/validate.py              # every skill
    python3 scripts/validate.py eastwind-brand
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

MAX_BODY_LINES = 500
MAX_DESCRIPTION = 1024
MAX_NAME = 64

PORTABLE_KEYS = {"name", "description", "license", "compatibility", "metadata"}
CLAUDE_ONLY_KEYS = {
    "allowed-tools",
    "disallowed-tools",
    "arguments",
    "argument-hint",
    "disable-model-invocation",
    "user-invocable-only",
    "model",
    "paths",
}
BANNED_IN_BODY = [
    (r"\$\{CLAUDE_[A-Z_]+\}", "Claude-specific path variable"),
    (r"\$\{CLAUDE_PLUGIN_ROOT\}", "Claude-specific path variable"),
    (r"(?<![\w/])/(Users|home)/", "absolute filesystem path"),
    (r"\.\./\.\./", "path escaping the skill folder"),
]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+?)\)")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, skill: str, msg: str) -> None:
        self.errors.append(f"{skill}: {msg}")

    def warn(self, skill: str, msg: str) -> None:
        self.warnings.append(f"{skill}: {msg}")


def split_frontmatter(text: str) -> tuple[str | None, str, int]:
    """Return (frontmatter, body, body_start_line). Frontmatter is None if absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text, 1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :]), i + 2
    return None, text, 1


def parse_frontmatter(raw: str) -> dict[str, str]:
    """Minimal YAML: top-level `key: value` pairs. Nested blocks map to ''."""
    out: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1] in (" ", "\t"):  # nested value, we only need top-level keys
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        out[key.strip()] = value.strip().strip("\"'")
    return out


def check_links(skill_dir: Path, source: Path, text: str, rep: Report, name: str) -> None:
    for target in LINK_RE.findall(text):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (source.parent / target).resolve()
        if not resolved.exists():
            rep.error(name, f"{source.name}: broken link -> {target}")


def validate(skill_dir: Path, rep: Report) -> None:
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        rep.error(name, "SKILL.md is missing")
        return
    if not (skill_dir / "README.md").exists():
        rep.warn(name, "README.md card is missing")

    text = skill_md.read_text(encoding="utf-8")
    fm_raw, body, _ = split_frontmatter(text)

    if fm_raw is None:
        rep.error(name, "SKILL.md has no YAML frontmatter starting on line 1")
        return

    fm = parse_frontmatter(fm_raw)

    fm_name = fm.get("name", "")
    if not fm_name:
        rep.error(name, "frontmatter has no `name`")
    elif fm_name != name:
        rep.error(name, f"frontmatter name `{fm_name}` != folder name `{name}`")
    if fm_name and not NAME_RE.match(fm_name):
        rep.error(name, f"name `{fm_name}` is not kebab-case")
    if len(fm_name) > MAX_NAME:
        rep.error(name, f"name is {len(fm_name)} chars, max {MAX_NAME}")
    if fm_name and not fm_name.startswith("eastwind-"):
        rep.warn(name, "name has no `eastwind-` prefix; collisions are likely")

    desc = fm.get("description", "")
    if not desc:
        rep.error(name, "frontmatter has no `description`")
    else:
        if len(desc) > MAX_DESCRIPTION:
            rep.error(name, f"description is {len(desc)} chars, max {MAX_DESCRIPTION}")
        if len(desc) < 60:
            rep.warn(name, "description is very short; auto-triggering will be unreliable")
        if "use when" not in desc.lower():
            rep.warn(name, "description does not say when to use the skill")

    for key in fm:
        if key in CLAUDE_ONLY_KEYS:
            rep.error(name, f"frontmatter key `{key}` is Claude Code-only; breaks portability")
        elif key not in PORTABLE_KEYS:
            rep.warn(name, f"unrecognised frontmatter key `{key}`")

    body_lines = len(body.splitlines())
    if body_lines > MAX_BODY_LINES:
        rep.error(name, f"body is {body_lines} lines, max {MAX_BODY_LINES}; move detail to references/")
    elif body_lines > MAX_BODY_LINES * 0.8:
        rep.warn(name, f"body is {body_lines} lines, approaching the {MAX_BODY_LINES} limit")

    for pattern, why in BANNED_IN_BODY:
        if re.search(pattern, body):
            rep.error(name, f"body contains {why} (/{pattern}/)")

    check_links(skill_dir, skill_md, body, rep, name)

    refs = skill_dir / "references"
    if refs.is_dir():
        for ref in sorted(refs.glob("*.md")):
            ref_text = ref.read_text(encoding="utf-8")
            check_links(skill_dir, ref, ref_text, rep, name)
            for pattern, why in BANNED_IN_BODY:
                if re.search(pattern, ref_text):
                    rep.error(name, f"references/{ref.name} contains {why}")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"no skills/ directory at {SKILLS_DIR}", file=sys.stderr)
        return 2

    wanted = sys.argv[1:]
    dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))
    if wanted:
        by_name = {d.name: d for d in dirs}
        missing = [w for w in wanted if w not in by_name]
        if missing:
            print(f"unknown skill(s): {', '.join(missing)}", file=sys.stderr)
            return 2
        dirs = [by_name[w] for w in wanted]

    rep = Report()
    for d in dirs:
        validate(d, rep)

    for w in rep.warnings:
        print(f"warn   {w}")
    for e in rep.errors:
        print(f"ERROR  {e}")

    checked = ", ".join(d.name for d in dirs) or "nothing"
    print(f"\nchecked {len(dirs)} skill(s): {checked}")
    print(f"{len(rep.errors)} error(s), {len(rep.warnings)} warning(s)")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
