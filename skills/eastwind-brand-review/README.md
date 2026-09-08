# eastwind-brand-review

Проверка готовых артефактов на соответствие брендбуку Eastwind. Парный скилл —
[eastwind-brand](../eastwind-brand/) — оформляет новое.

## Русский

**Что делает.** Аудит готового артефакта: цвета против палитры, гарнитуры и
начертания, сетка 8, обращение с логотипом, графика и фотостиль. На выходе —
отчёт с приоритетами, а не переделанный файл.

**Когда срабатывает.** «Проверь по брендбуку», «это в нашем стиле?», «отревьюй
деку перед отправкой», проверка шаблона перед запуском в оборот.

**Когда не нужен.** Создание и переоформление — `eastwind-brand`.

**Что нужно на входе.** Файл или скриншоты, тип артефакта (от него зависит,
какая гарнитура правильная: Arial в приказе — норма, Arial в деке — нарушение),
аудитория.

**Что на выходе.** Находки по уровням `blocker` / `major` / `minor`, каждая с
ссылкой на правило и с указанием, каким должно быть значение. Плюс что сделано
хорошо и открытые вопросы, которые гайдлайн не закрывает.

**Детерминированная часть.** `assets/check_brand.py` вытаскивает реально
использованные цвета и шрифты из `.pptx`, `.docx`, `.xlsx`, `.pdf`, `.svg`,
`.html`, `.css` и сравнивает с токенами. Отделяет точные совпадения от дрейфа
(значение в одном-двух символах от токена — это опечатка, а не решение) и от
по-настоящему чужих цветов; шрифты, реально применённые в контенте, — от просто
объявленных в стилях. Скрипт необязателен: в ChatGPT его не будет, процедура
работает и на глаз.

```bash
python3 assets/check_brand.py "КП_template_april 2026_en.docx"
```

**Запуск.** Claude: `/eastwind-brand-review` или само подхватится.
ChatGPT: `python3 scripts/bundle.py eastwind-brand-review`.

## English

**What it does.** Audits a finished artifact against the brand guideline — color
against the palette, typefaces and weights, the 8-px grid, logo handling, graphic
and photographic style — and reports findings by severity. It produces a report,
not a corrected file.

**Triggers on.** "Check this against the brand book", "is this on brand?",
"review the deck before I send it", reviewing a template before circulation.

**Not for.** Creating or restyling an artifact — that is `eastwind-brand`.

**Inputs.** The file or screenshots, the artifact type (it decides which typeface
is correct), the audience.

**Outputs.** Findings graded `blocker` / `major` / `minor`, each citing a rule and
naming the correct value, plus what works and the questions the guideline leaves
open.

**Deterministic half.** `assets/check_brand.py` extracts the colors and fonts
actually present in a file and diffs them against the tokens. Optional — the
procedure works without it.

**Run it.** Claude: `/eastwind-brand-review`, or let it auto-trigger.
ChatGPT: `python3 scripts/bundle.py eastwind-brand-review`.
