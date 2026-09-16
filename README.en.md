# Eastwind Skills

Portable skills for Eastwind. A skill is a folder with a `SKILL.md` file holding
instructions for an AI assistant: how to carry out one specific work task the way
the company does it.

Skills are written to run in Codex and ChatGPT as well as Claude (Claude Code,
Cowork, claude.ai). See [docs/portability.md](docs/portability.md).

Русская версия: [README.md](README.md)

## Catalog

| Skill | What it does | Status |
| :---- | :----------- | :----- |
| [eastwind-brand](skills/eastwind-brand/) | Design artifacts to the Eastwind identity | ✅ ready |
| [eastwind-brand-review](skills/eastwind-brand-review/) | Audit finished artifacts against the brand guideline | ✅ ready |
| [eastwind-documents](skills/eastwind-documents/) | Produce the company's standard documents | 🚧 scaffold |

Each skill ships its own `README.md` card — purpose, trigger conditions, expected
inputs, expected outputs.

## Repository layout

```
eastwind-skills/
├── .agents/skills/         Codex auto-discovery entry points
├── skills/                 one folder per skill
│   └── <skill-name>/
│       ├── SKILL.md        instructions for the model (the main file)
│       ├── README.md       card for humans
│       ├── references/     details the model reads on demand
│       └── assets/         templates, images, fonts
├── shared/                 material used by more than one skill
│   └── brand/              the brand knowledge base, logo files, check_brand.py
├── docs/                   authoring and portability conventions
├── scripts/                validation and bundling
└── dist/                   built bundles (not committed)
```

A skill cannot reference anything outside its own folder — the folder is copied on
install. Shared material therefore lives in `shared/`, and a skill's `references/`
and `assets/` hold symlinks into it, so one edit reaches every skill that uses it.
That is how `eastwind-brand` and `eastwind-brand-review` are paired: different
procedures, one knowledge base.

## Usage

### Codex and ChatGPT Desktop

Codex scans `.agents/skills/` from the current directory up to the repository
root. This repository includes symlinks for every skill, so opening the repo in
Codex is enough. Codex normally detects new and changed skills automatically;
restart it if an update does not appear.

Invoke a skill explicitly with `$eastwind-brand` in Codex CLI or the IDE (or
open `/skills`), or select it with `@` in ChatGPT Desktop. Codex can also choose
a skill implicitly when the request matches its `description`.

To make a skill available across all repositories, install it in the user scope:

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/skills/eastwind-brand" ~/.agents/skills/eastwind-brand
```

Current discovery and invocation rules: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills).

### Claude Code / Cowork

Skills load from `~/.claude/skills/`. A symlink beats a copy — edits in the repo
apply immediately:

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)/skills/eastwind-brand" ~/.claude/skills/eastwind-brand
```

Then either invoke it by name — `/eastwind-brand` — or let the assistant load it
on its own when a request matches the skill's `description`.

### claude.ai

```bash
python3 scripts/bundle.py eastwind-brand
```

Upload the resulting `dist/eastwind-brand.zip` under Skills in claude.ai
settings.

### ChatGPT Projects and custom GPTs

Where filesystem skills are unavailable, the same script writes
`dist/eastwind-brand.md` — a single self-contained file with every `references/`
document inlined. Paste its contents into Project instructions or a custom GPT's
instructions. Add files from `assets/` to project knowledge when needed.

## Development

```bash
python3 scripts/validate.py          # check every skill
python3 scripts/validate.py eastwind-brand
python3 scripts/bundle.py --all      # build every bundle
```

Authoring rules: [docs/authoring.md](docs/authoring.md).
Change process: [CONTRIBUTING.md](CONTRIBUTING.md).
