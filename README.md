# Eastwind Skills

Репозиторий переносимых скиллов Eastwind. Скилл — это папка с файлом `SKILL.md`,
в котором лежат инструкции для ИИ-ассистента: как выполнять конкретную рабочую
задачу по правилам компании.

Скиллы написаны так, чтобы работать в Codex и ChatGPT, а также в Claude
(Claude Code, Cowork, claude.ai). См. [docs/portability.md](docs/portability.md).

English version: [README.en.md](README.en.md)

## Каталог скиллов

| Скилл | Что делает | Статус |
| :---- | :--------- | :----- |
| [eastwind-brand](skills/eastwind-brand/) | Оформление артефактов по айдентике Eastwind | ✅ готов |
| [eastwind-brand-review](skills/eastwind-brand-review/) | Аудит готовых артефактов на соответствие брендбуку | ✅ готов |
| [eastwind-documents](skills/eastwind-documents/) | Подготовка типовых документов компании | 🚧 каркас |

У каждого скилла есть своя карточка `README.md` — назначение, когда срабатывает,
что нужно на входе, что получается на выходе.

## Структура репозитория

```
eastwind-skills/
├── .agents/skills/         точки входа для автоподхвата в Codex
├── skills/                 скиллы, по папке на каждый
│   └── <skill-name>/
│       ├── SKILL.md        инструкция для модели (главный файл)
│       ├── README.md       карточка для человека
│       ├── references/     детали, которые модель читает по необходимости
│       └── assets/         шаблоны, изображения, шрифты
├── shared/                 материалы, общие для нескольких скиллов
│   └── brand/              база знаний по бренду + логотипы + check_brand.py
├── docs/                   конвенции написания и совместимости
├── scripts/                валидация и сборка
└── dist/                   собранные бандлы (не коммитится)
```

Скилл не может ссылаться наружу своей папки: при установке она копируется.
Поэтому общие материалы лежат в `shared/`, а в `references/` и `assets/` скилла
на них ведут симлинки — правка в одном месте расходится по всем скиллам. Так
устроена пара `eastwind-brand` и `eastwind-brand-review`: процедуры у них разные,
а база знаний по бренду одна.

## Как пользоваться

### Codex и ChatGPT Desktop

Codex ищет проектные скиллы в `.agents/skills/` от текущей папки до корня
репозитория. В этом репозитории уже лежат симлинки на все скиллы, поэтому
достаточно открыть репозиторий в Codex. Новый или изменённый скилл обычно
подхватывается автоматически; если он не появился, перезапустите Codex.

Скилл можно вызвать явно: в Codex CLI и IDE наберите `$eastwind-brand` (или
откройте `/skills`), а в ChatGPT Desktop выберите его через `@`. Без явного
вызова Codex может подобрать скилл сам, когда запрос совпадает с его
`description`.

Чтобы использовать скиллы во всех репозиториях, установите их в личную папку:

```bash
mkdir -p ~/.agents/skills
ln -s "$(pwd)/skills/eastwind-brand" ~/.agents/skills/eastwind-brand
```

Актуальные правила обнаружения и вызова: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills).

### Claude Code / Cowork

Скиллы подхватываются из `~/.claude/skills/`. Симлинк удобнее копии — правки в
репозитории применяются сразу:

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)/skills/eastwind-brand" ~/.claude/skills/eastwind-brand
```

Дальше либо вызов по имени — `/eastwind-brand`, либо ассистент подхватит скилл
сам, когда задача совпадёт с его `description`.

### claude.ai

```bash
python3 scripts/bundle.py eastwind-brand
```

Готовый `dist/eastwind-brand.zip` загружается в разделе Skills в настройках
claude.ai.

### ChatGPT Projects и кастомные GPT

Когда файловые скиллы недоступны, тот же скрипт кладёт рядом
`dist/eastwind-brand.md` — одиночный самодостаточный файл, в котором все
`references/` уже вклеены в текст. Его содержимое идёт в инструкции проекта
(Project instructions) или в описание кастомного GPT. Файлы из `assets/` при
необходимости прикладываются в knowledge проекта.

## Разработка

```bash
python3 scripts/validate.py          # проверить все скиллы
python3 scripts/validate.py eastwind-brand
python3 scripts/bundle.py --all      # собрать все бандлы
```

Правила написания скиллов — [docs/authoring.md](docs/authoring.md).
Процесс внесения изменений — [CONTRIBUTING.md](CONTRIBUTING.md).
