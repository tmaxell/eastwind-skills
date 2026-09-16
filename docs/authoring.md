# Authoring skills

> **RU, кратко.** Один скилл = одна задача. `SKILL.md` пишется на английском,
> коротко (до 500 строк), детали выносятся в `references/`. Выходные документы
> скилл готовит на языке запроса, по умолчанию — русский. Во фронтматтере
> только `name` и `description` (плюс необязательные `license`, `metadata`).
> `description` — самое важное поле: по нему модель решает, включать ли скилл.

## One skill, one job

A skill covers a task a person would name in one phrase: "design a deck to brand",
"draft a standard contract annex". If a skill needs the word "and" to describe
what it does, it is probably two skills.

Skills do not call each other. Overlap is resolved by making `description` fields
disjoint, not by cross-references.

## File layout

```
skills/<skill-name>/
├── SKILL.md        required
├── README.md       required in this repository — the human-facing card
├── agents/         optional — Codex UI metadata and invocation policy
├── references/     optional — .md files the model reads on demand
└── assets/         optional — templates, fonts, images, example files
```

Repository-scoped Codex discovery uses `.agents/skills/`. This repository keeps
the canonical sources under `skills/` for cross-platform packaging and exposes
them to Codex through relative symlinks in `.agents/skills/`. Global Codex skills
belong in `~/.agents/skills/`.

`<skill-name>` is kebab-case, prefixed with `eastwind-`. The prefix matters:
skills install into a flat `~/.claude/skills/` namespace shared with personal and
third-party skills, and a folder called `brand` would collide.

## Sharing material between skills

A skill folder is copied when it is installed, so `../shared/x.md` does not
survive the trip. Material used by more than one skill lives in `shared/<topic>/`
at the repository root, and each skill links to the individual files it needs:

```bash
ln -sfn ../../../shared/brand/tokens.md skills/eastwind-brand/references/tokens.md
```

Link files, never directories — a symlinked directory is not traversed reliably
when the bundle is built. Both `validate.py` and `bundle.py` follow file symlinks
and treat the target as if it lived inside the skill.

Splitting one job into two skills is worth it when the verbs differ — designing
and auditing have different inputs, outputs, and dispositions — and the shared
folder is what makes the split cheap. Splitting by topic rather than by verb
usually is not: that is what `references/` is for.

## Frontmatter

```yaml
---
name: eastwind-brand
description: Apply the Eastwind brand book to decks, documents, and visual artifacts. Use when the user asks to design, restyle, or review a deck, one-pager, report, or any customer-facing visual for brand compliance.
---
```

| Field | Required | Notes |
| :---- | :------- | :---- |
| `name` | yes | Must equal the folder name. Kebab-case, ≤64 chars. |
| `description` | yes | ≤1024 chars. Third person, present tense. |
| `license` | no | Only if the skill leaves the company. |
| `metadata` | no | Free-form key/value, e.g. `owner`, `updated`. |

Do **not** use `allowed-tools`, `arguments`, `disable-model-invocation`,
`user-invocable-only`, or `model`. They are Claude Code-specific and break
portability — see [portability.md](portability.md). Codex-specific UI metadata,
invocation policy, and dependencies belong in optional `agents/openai.yaml`, not
in `SKILL.md` frontmatter.

### Writing the description

The description is the only text the model sees before deciding whether to load
the skill. Specificity beats length. State two things:

1. **What** the skill produces.
2. **When** to use it — the concrete phrasings and artifacts that should trigger it.

Add a negative clause when a neighbouring skill could be confused with this one:
"…do not use for internal engineering documentation."

Bad: `Helps with documents.`
Good: `Produces Eastwind's standard commercial documents — NDAs, statements of work, act of acceptance, commercial proposals — from a short brief. Use when the user asks for a contract, annex, SOW, or offer on company letterhead. Do not use for product specs or engineering docs.`

## Writing the body

The body is a procedure, not an essay. Structure that works:

1. **Purpose** — one paragraph on what "done" looks like.
2. **Before you start** — which `references/` to read, what to ask the user for
   if it is missing.
3. **Steps** — numbered, imperative.
4. **Rules and constraints** — what must never happen.
5. **Output format** — exact structure of the deliverable.

Rules that must hold for the whole task are written as standing rules, not as one
step among many: the assistant reads `SKILL.md` once and keeps it in context, so a
constraint buried in step 3 stops being salient by step 9.

Keep `SKILL.md` under 500 lines. Beyond that, split detail out into
`references/*.md` and point at it from the body:

```markdown
Read [references/color-and-type.md](references/color-and-type.md) before choosing
any color or typeface.
```

This is progressive disclosure: the body stays cheap to load, the detail arrives
only when the task needs it.

## Language

- `SKILL.md` and `references/` — **English**. Instruction-following is more
  reliable, and the files stay usable by non-Russian-speaking colleagues.
- Fixed wording that must appear verbatim in a deliverable — legal clauses,
  approved product names, boilerplate — stays in its original language inside
  `references/` or `assets/`, quoted as-is.
- Deliverables — the language of the user's request; Russian when unclear. Say so
  explicitly in the body, otherwise the model tends to answer in the language of
  its instructions.
- `README.md` of a skill — Russian section first, English section after.

## Assets and paths

Reference files with relative paths from the skill folder: `references/x.md`,
`assets/template.docx`. Never use absolute paths, `../`, or environment variables
such as `${CLAUDE_SKILL_DIR}` — the folder is copied around, and `../` does not
survive the trip.

## Checklist before commit

- [ ] `python3 scripts/validate.py <skill-name>` passes
- [ ] `description` names both the output and the trigger
- [ ] Body ≤500 lines, detail pushed to `references/`
- [ ] No Claude-specific frontmatter fields, tool names, or path variables
- [ ] Output language rule stated explicitly
- [ ] `README.md` card updated (RU + EN)
- [ ] Skill listed in the catalog table of both root READMEs
- [ ] Tested on one real task in Claude, and on one in ChatGPT via `bundle.py`
