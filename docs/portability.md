# Portability: Codex / ChatGPT / Claude

> **RU, кратко.** Codex и ChatGPT Desktop нативно поддерживают файловые
> скиллы. Claude использует тот же базовый формат, но иначе их устанавливает.
> Для ChatGPT Projects и кастомных GPT репозиторий собирает плоскую версию
> скриптом `bundle.py`. Портативность требует инструкций в терминах действий,
> а не имён конкретных инструментов.

## What differs between the platforms

| | Codex / ChatGPT Desktop | Claude | ChatGPT Projects / custom GPTs |
| :-- | :-- | :-- | :-- |
| Skill format | Folder with `SKILL.md` | Folder with `SKILL.md` | Flattened instructions plus knowledge files |
| Delivery | Repo `.agents/skills/`, user `~/.agents/skills/`, or a plugin | `~/.claude/skills/`, `.zip`, or a plugin | Project or GPT instructions and knowledge |
| On-demand file reads | Yes | Yes | Only for attached knowledge files |
| Invocation | Explicit `$skill-name` or implicit match; `@` in ChatGPT Desktop | Explicit `/skill-name` or implicit match | Always active inside the configured project/GPT |

The consequence: a portable skill cannot assume every target can browse its
folder. It must still make sense after its references have been flattened or
attached as project knowledge.

Codex discovers repository skills by scanning `.agents/skills/` from the current
working directory to the repository root. It discovers personal skills in
`~/.agents/skills/`. Codex follows symlinked skill folders and normally detects
changes automatically; restart it if an update does not appear. See
[OpenAI's current skill documentation](https://learn.chatgpt.com/docs/build-skills).

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
A skill may ship a helper script, but the procedure must remain completable on
surfaces without a shell, including ChatGPT Projects and custom GPTs.

**5. References must read standalone.**
Each `references/*.md` opens with one line saying what it is. When `bundle.py`
inlines them into a single file, that line becomes the section's context.

**6. State the trigger inside the body too.**
Codex and Claude use `description` for discovery. In a flattened ChatGPT Project
bundle the text is always present, so the body must also say when it applies and
when it does not; otherwise the skill can affect unrelated requests.

**7. No conversation-state assumptions.**
Do not write "as established earlier". Each run starts cold.

## Building for ChatGPT Projects and custom GPTs

```bash
python3 scripts/bundle.py eastwind-brand
```

Produces:

- `dist/eastwind-brand.md` — frontmatter rendered as a header, body, and every
  linked `references/*.md` inlined as an appendix. This is what goes into Project
  instructions or a custom GPT.
- `dist/eastwind-brand.zip` — the portable folder, for hosts that accept skill
  uploads such as claude.ai.

Binary assets are not inlined. If a skill depends on them, `bundle.py` lists them
at the end of the `.md` so whoever sets up the project knows what to attach to the
project knowledge.

When the flattened file runs long — as it does for the brand skills, whose
references are the brand book itself — `bundle.py` also writes a split build:

```
dist/<skill>/instructions.md      paste into the project instructions
dist/<skill>/knowledge/*.md       attach to the project knowledge
```

The instructions in the split build tell the model the references are attached
files rather than files it can open, which is the difference that matters.

## Known limits

- ChatGPT project instructions have a length cap. A skill whose flattened bundle
  runs long has to move detail into attached knowledge files instead — check the
  size that `bundle.py` reports.
- Multiple skills in one ChatGPT project compete for attention. Prefer one project
  per skill, or one project per role with two or three closely related skills.
- ChatGPT Projects and custom GPTs do not auto-trigger a flattened bundle from
  its `description`. Whoever configures the project decides the scope, so the
  skill body still has to defend its own boundaries.
