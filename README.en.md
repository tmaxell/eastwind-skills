# Eastwind Skills

Portable skills for Eastwind. A skill is a folder with a `SKILL.md` file holding
instructions for an AI assistant: how to carry out one specific work task the way
the company does it.

Skills are written to run both in Claude (Claude Code, Cowork, claude.ai) and in
ChatGPT. See [docs/portability.md](docs/portability.md).

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

### ChatGPT

The same script also writes `dist/eastwind-brand.md` — a single self-contained
file with every `references/` document inlined. Paste its contents into Project
instructions or into a custom GPT's instructions. Add files from `assets/` to the
project knowledge when the skill needs them.

## Development

```bash
python3 scripts/validate.py          # check every skill
python3 scripts/validate.py eastwind-brand
python3 scripts/bundle.py --all      # build every bundle
```

Authoring rules: [docs/authoring.md](docs/authoring.md).
Change process: [CONTRIBUTING.md](CONTRIBUTING.md).
