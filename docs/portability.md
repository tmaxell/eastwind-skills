# Portability: Claude ↔ ChatGPT

> **RU, кратко.** Скиллы должны работать и в Claude, и в ChatGPT. Цена этого —
> отказ от Claude-специфичных возможностей: полей фронтматтера вроде
> `allowed-tools`, переменных `${CLAUDE_SKILL_DIR}`, упоминаний конкретных
> инструментов ("используй Read"). Пиши инструкции в терминах действий, а не
> инструментов. Для ChatGPT скилл собирается в один файл скриптом `bundle.py`.

## What differs between the platforms

| | Claude | ChatGPT |
| :-- | :-- | :-- |
| Skill format | Folder with `SKILL.md`, loaded automatically by `description` | No native equivalent |
| Delivery | `~/.claude/skills/`, `.zip` upload, or a plugin | Project instructions, custom GPT instructions, project knowledge |
| On-demand file reads | Yes — the model can open `references/` itself | Only if the files are attached as knowledge; otherwise it sees one blob of text |
| Invocation | Auto-triggered or `/skill-name` | Always active inside the project |

The consequence: a skill cannot assume it will be able to read a file later. It
must still make sense when every reference has been flattened into one document
that is always in context.

## Rules

**1. Portable frontmatter only.**
`name`, `description`, and optionally `license` and `metadata`. Anything else is
Claude Code-specific and is rejected by claude.ai uploads and the Skills API.

**2. No tool names.**
Write "read `references/x.md`", not "use the Read tool to open". Write "produce a
.docx", not "call the docx skill". Tools differ per platform; actions do not.

**3. No environment variables or absolute paths.**
`${CLAUDE_SKILL_DIR}`, `${CLAUDE_PLUGIN_ROOT}`, `/Users/...` — all forbidden.
Relative paths from the skill folder only.

**4. No scripts as a hard dependency.**
A skill may ship a helper script in `assets/`, but the procedure must be
completable without running it. ChatGPT projects have no shell.

**5. References must read standalone.**
Each `references/*.md` opens with one line saying what it is. When `bundle.py`
inlines them into a single file, that line becomes the section's context.

**6. State the trigger inside the body too.**
Claude decides from `description` whether to load the skill; in ChatGPT the text
is always present, so the body must say when it applies and when it does not —
otherwise the skill fires on unrelated requests.

**7. No conversation-state assumptions.**
Do not write "as established earlier". Each run starts cold.

## Building for ChatGPT

```bash
python3 scripts/bundle.py eastwind-brand
```

Produces:

- `dist/eastwind-brand.md` — frontmatter rendered as a header, body, and every
  linked `references/*.md` inlined as an appendix. This is what goes into Project
  instructions or a custom GPT.
- `dist/eastwind-brand.zip` — the folder as-is, for uploading to claude.ai.

Binary assets are not inlined. If a skill depends on them, `bundle.py` lists them
at the end of the `.md` so whoever sets up the project knows what to attach to the
project knowledge.

## Known limits

- ChatGPT project instructions have a length cap. A skill whose flattened bundle
  runs long has to move detail into attached knowledge files instead — check the
  size that `bundle.py` reports.
- Multiple skills in one ChatGPT project compete for attention. Prefer one project
  per skill, or one project per role with two or three closely related skills.
- Auto-triggering by `description` has no ChatGPT equivalent. Whoever sets up the
  project decides the scope; the skill body has to defend its own boundaries.
