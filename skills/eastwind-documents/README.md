# eastwind-documents

**Статус: каркас.** `SKILL.md` содержит структуру и вопросы к автору, но не сами
шаблоны документов.

## Русский

**Что делает.** Готовит типовые документы компании из короткого брифа:
коммерческие предложения, ТЗ и SOW, акты, NDA, служебные записки.

**Когда срабатывает.** «Сделай КП», «нужен акт», «подготовь приложение к
договору», «оформи на бланке».

**Когда не нужен.** Продуктовые спецификации, инженерная документация,
маркетинговые тексты.

**Что нужно на входе.** Тип документа, контрагент, предмет и объём, сроки, суммы,
подписанты.

**Что на выходе.** Документ по шаблону плюс явный список незаполненных полей и
сделанных допущений. Юридические формулировки не переписываются — цитируются.

**Запуск.** Codex: `$eastwind-documents` или автоподбор по `description`;
ChatGPT Desktop: выбор через `@`; Claude: `/eastwind-documents`. Для
ChatGPT Projects и кастомных GPT: `python3 scripts/bundle.py eastwind-documents`.

## English

**What it does.** Produces the company's standard documents from a short brief —
commercial proposals, SOWs, acts of acceptance, NDAs, internal memos.

**Triggers on.** "Draft an offer", "I need an act", "prepare a contract annex",
"put it on letterhead".

**Not for.** Product specs, engineering documentation, marketing copy.

**Inputs.** Document type, counterparty, scope, dates, amounts, signatories.

**Outputs.** The document from its template, plus an explicit list of unfilled
placeholders and assumptions made. Fixed legal wording is quoted, never
paraphrased.

**Run it.** Codex: `$eastwind-documents` or implicit matching; ChatGPT Desktop:
select it with `@`; Claude: `/eastwind-documents`. For ChatGPT Projects and
custom GPTs: `python3 scripts/bundle.py eastwind-documents`.
