# eastwind-brand

Оформление артефактов по айдентике Eastwind. Парный скилл —
[eastwind-brand-review](../eastwind-brand-review/) — проверяет уже готовое.

Источник правил: `DesignDocs/Brand Guidelines_L.pdf` (v1, MVP 1, 2024, 76 с.),
`Цвета фирм стиля EW.pdf`, `Инструкция по типографике.pdf`, открытые материалы
брендбука. Токены и палитры вынуты из векторных заливок самого гайдлайна, поэтому
значения точные, а не срисованные на глаз.

## Русский

**Что делает.** Собирает или переоформляет визуальный артефакт: презентацию,
одностраничник, отчёт, схему, баннер, картинку для соцсетей, веб-страницу,
вёрстку документа. Назначает цвета по ролям, ставит типографику, кладёт на сетку
8, размещает логотип, выбирает графический стиль.

**Когда срабатывает.** «Оформи», «свёрстай», «сделай в нашем стиле»,
«переоформи под бренд», «нужна дека для клиента».

**Когда не нужен.** Проверка готового — `eastwind-brand-review`. Написание
текста. Сборка договоров, актов и КП по шаблонам — `eastwind-documents`.

**Что нужно на входе.** Формат и размеры, аудитория (клиент / партнёр /
внутренний), язык, новая работа или переоформление, доступен ли фирменный шрифт
TT Firs Neue (он коммерческий и в открытых материалах его нет — без лицензии
используется Raleway).

**Что на выходе.** Артефакт плюс короткая записка: какие токены назначены на
какие роли, что отклонилось от гайдлайна и почему, какие вопросы гайдлайн не
закрывает.

**Что внутри.** `references/` — токены (цвета, шрифты, сетка), правила логотипа,
графика и фотостиль, плейбуки по типам артефактов, чеклист и реестр
противоречий в исходных материалах. `assets/logo/` — открытый набор логотипов в
SVG и PNG. Референсы общие с ревью-скиллом и лежат в `shared/brand/`.

**Запуск.** Claude: `/eastwind-brand` или само подхватится.
ChatGPT: `python3 scripts/bundle.py eastwind-brand` → `dist/eastwind-brand.md`.

## English

**What it does.** Designs or restyles a visual artifact — deck, one-pager,
report, diagram, banner, social image, web page, document layout — to the
Eastwind identity: color roles, typography, the 8-px grid, logo placement,
graphic style.

**Triggers on.** "Style this", "lay this out", "make it look like ours", "a
client-ready deck".

**Not for.** Auditing a finished artifact (`eastwind-brand-review`), writing the
copy, or assembling contracts and proposals from templates
(`eastwind-documents`).

**Inputs.** Format and dimensions, audience, language, new work or restyle, and
whether TT Firs Neue is licensed in the environment — without it the artifact
uses Raleway.

**Outputs.** The artifact plus a handover note: tokens assigned per role, any
deviation with its reason, and the questions the guideline leaves open.

**Run it.** Claude: `/eastwind-brand`, or let it auto-trigger.
ChatGPT: `python3 scripts/bundle.py eastwind-brand` → `dist/eastwind-brand.md`.
