# Eastwind Skills

Репозиторий переносимых скиллов Eastwind. Скилл — это папка с файлом `SKILL.md`,
в котором лежат инструкции для ИИ-ассистента: как выполнять конкретную рабочую
задачу по правилам компании.

Скиллы написаны так, чтобы работать и в Claude (Claude Code, Cowork, claude.ai),
и в ChatGPT. См. [docs/portability.md](docs/portability.md).

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

### ChatGPT

Тот же скрипт кладёт рядом `dist/eastwind-brand.md` — одиночный самодостаточный
файл, в котором все `references/` уже вклеены в текст. Его содержимое идёт в
инструкции проекта (Project instructions) или в описание кастомного GPT.
Файлы из `assets/` при необходимости прикладываются в knowledge проекта.

## Разработка

```bash
python3 scripts/validate.py          # проверить все скиллы
python3 scripts/validate.py eastwind-brand
python3 scripts/bundle.py --all      # собрать все бандлы
```

Правила написания скиллов — [docs/authoring.md](docs/authoring.md).
Процесс внесения изменений — [CONTRIBUTING.md](CONTRIBUTING.md).
