# Contributing

> **RU, кратко.** Новый скилл: скопируй каркас, заполни `SKILL.md` и карточку,
> прогони `validate.py`, добавь строку в каталог обоих README, закоммить.
> Правка чужого скилла — через ветку и обсуждение с владельцем скилла
> (`metadata.owner`). Обязательное условие приёмки — скилл проверен на реальной
> задаче в Claude и в ChatGPT.

## Adding a skill

```bash
cp -r skills/eastwind-documents skills/eastwind-<name>
rm -rf skills/eastwind-<name>/references/* skills/eastwind-<name>/templates/*
```

Then:

1. Write `SKILL.md` following [docs/authoring.md](docs/authoring.md). Set `name`
   to the folder name and `metadata.owner` to yourself.
2. Write the `README.md` card — RU section, then EN.
3. `python3 scripts/validate.py eastwind-<name>`
4. Add a row to the catalog table in `README.md` **and** `README.en.md`.
5. Test on one real task in Claude and one in ChatGPT
   (`python3 scripts/bundle.py eastwind-<name>`).
6. Commit.

## Changing an existing skill

Skills are shared company-wide, so a change to someone's skill changes their
colleagues' output. Work on a branch, and get the owner named in
`metadata.owner` to look at it before merging.

```bash
git switch -c skill/<name>-<what-changed>
# edit
python3 scripts/validate.py
git commit -am "eastwind-<name>: <what changed and why>"
git switch main && git merge --no-ff skill/<name>-<what-changed>
```

Bump `metadata.updated` on any change to `SKILL.md` or `references/`.

## Review checklist

Correctness of the content is the author's business. A reviewer checks the parts
that break silently:

- [ ] `description` is specific enough to fire on the right requests, and narrow
      enough not to fire on the neighbouring skill's requests
- [ ] Nothing Claude-specific slipped in (see [docs/portability.md](docs/portability.md))
- [ ] Facts that could go stale — prices, names, legal wording — live in
      `references/`, not in the body, and are attributed to a source
- [ ] The skill states what to do when required input is missing, instead of
      inventing it
- [ ] Output language rule is present
- [ ] `validate.py` passes

## Retiring a skill

Delete the folder, remove the catalog rows, commit with a note saying what
replaces it. Tell everyone who symlinked it — a stale symlink in
`~/.claude/skills/` silently loads nothing.

## Remote

The repository is local. To publish it privately:

```bash
git remote add origin git@github.com:<org>/eastwind-skills.git
git push -u origin main
```

Keep it private: skills carry brand assets, document templates, and commercial
wording.
