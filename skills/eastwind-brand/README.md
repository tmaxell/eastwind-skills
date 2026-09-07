# eastwind-brand

**Статус: каркас.** `SKILL.md` содержит структуру и вопросы к автору, но не сам
брендбук.

## Русский

**Что делает.** Оформляет артефакты по брендбуку Eastwind: презентации,
одностраничники, отчёты, схемы, веб-страницы. Проверяет готовый артефакт на
соответствие бренду.

**Когда срабатывает.** Просьбы «оформи», «сделай в нашем стиле», «проверь по
брендбуку», «свёрстанная презентация для клиента».

**Когда не нужен.** Написание текста и содержания — это не сюда. Текстовые
шаблоны документов — `eastwind-documents`.

**Что нужно на входе.** Формат артефакта, аудитория (клиент / внутренний /
партнёр), исходник, если это переоформление.

**Что на выходе.** Оформленный артефакт плюс перечень мест, где брендбук не даёт
однозначного ответа.

**Запуск.** Claude: `/eastwind-brand` или само подхватится.
ChatGPT: `python3 scripts/bundle.py eastwind-brand` → `dist/eastwind-brand.md`.

## English

**What it does.** Designs artifacts to the Eastwind brand book — decks,
one-pagers, reports, diagrams, web pages — and brand-checks existing ones.

**Triggers on.** "Style this", "make it look like ours", "check it against the
brand book", "a client-ready deck".

**Not for.** Writing the content itself. Document text templates live in
`eastwind-documents`.

**Inputs.** Artifact format, audience (customer / internal / partner), the source
file when restyling.

**Outputs.** The styled artifact, plus a list of cases the brand book does not
settle.

**Run it.** Claude: `/eastwind-brand`, or let it auto-trigger.
ChatGPT: `python3 scripts/bundle.py eastwind-brand` → `dist/eastwind-brand.md`.
