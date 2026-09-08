# Artifact types

Per-format rules. Everything here is grounded either in the brand guideline or in
the real Eastwind files shipped in the design materials — the source is named in
each section. Where practice and the guideline disagree, see
[known-issues.md](known-issues.md).

Common to every type: light theme, the 60/30/10 proportion, the 8-px grid, no ALL
CAPS headings, no italics, one typeface per medium.

## Presentation / deck

Source: guideline sections 04–05; layout examples throughout the guideline.

- Format 16:9. The guideline's own ratio list also allows 4:3.
- Type: TT Firs Neue Variable where licensed, otherwise Raleway. Headings Demi
  Bold or Bold (Raleway: Bold / Extra Bold), body Regular, UI-like elements
  Medium. Heading weight above 600 is discouraged.
- Heading ≈ 2× the body size. Line height 130–160%.
- Background white or Neutral 10/20. Body text Neutral 90. Accent Brand 70 on
  roughly a tenth of the surface.
- Decorative colors are allowed in deck infographics and illustration, but never
  mixed with brand blue in the same UI-like element.
- The guideline calls out decks "filled in by managers" as a case where the cold
  gray may be replaced with a neutral gray.

## PDF one-pager / marketing collateral

Reference implementations in the materials: `Eastwind_Сorporate Overview_2026.pdf`
and `Преимущества MP.pdf`. Both are A4 portrait, 595 × 842 pt, and both are
consistent with the palette. Their measured usage is the model to copy:

- Body text and headings: Neutral 90 `#1E293B`.
- Accent: Brand 60 `#3B33F8` and Brand 70 `#382DDD`, used sparingly.
- Surfaces: white, Neutral 10 `#F8FAFC`, Neutral 20 `#F1F5F9`, Neutral 30
  `#E2E8F0`, Neutral 40 `#CBD5E1` for rules and borders.
- `#201E3B` appears only in the logo.
- Small amounts of Red 10/50 for accenting figures.

These files carry no embedded fonts — they are exported as vector and raster from
a design tool, which is the expected route for this type.

## Word documents

Two distinct cases; do not confuse them.

**Administrative and records documents** — outgoing letters, orders, banking
details, and similar. Templates ship in the materials under `Бланк EW/`:
`Бланк без реквизитов`, `Бланк банковские реквизиты`, `Бланк исходящего письма`,
`Бланк приказ`, and an English outgoing-letter blank.

- Typeface: **Arial**, per the guideline's own rule that Arial is the face for
  records documents. All shipped blanks use Arial in the body.
- Start from the existing blank rather than styling a blank page — the letterhead
  image, margins, and footer are already in place.
- Text black or Neutral; the blanks use `000000` and `7F7F7F` for secondary text.
- Do not introduce brand blue as body text in these documents.

**Commercial documents** — the proposal template `КП_template_april 2026_en.docx`.

- Typeface: **Raleway** (Regular / Medium / SemiBold), because TT Firs Neue is not
  installable in a generic Word environment and Raleway is the sanctioned
  substitute. The template's own theme font is Arial.
- The template's color set has drifted off-palette. Correct it to the tokens
  rather than copying it — see [known-issues.md](known-issues.md).

## Social media and avatars

Source: guideline section 02.

- Use the compressed mark, not the horizontal logo, for Notion, Slack, Jira,
  Discord, LinkedIn, and social profiles.
- Pick the corner radius to match the platform: `r 0`, `r 8`, or `r full`.
- Light version is the `#F1F5F9` field with the `#382DDD` mark; dark version is
  the `#201E3B` field.

## Email

- Signature logo: `Logo EW light for e-mail.png`.
- The materials include seasonal email banners (`Новогодний сет 2025`) as
  precedent for banner proportions and treatment.

## Business cards and stationery

Source: guideline section 07. The card carries name, role, phone, email, and
`eastwind.ru/en`, set against the logo pattern, with the positioning line
"Автоматизируем маркетинг, строим ML-инфраструктуру, монетизируем клиентские
данные" / "Automate marketing, build ML infrastructure, protect and monetize
customer data" on the reverse. The guideline shows the layouts but does not print
measurements — treat any reconstruction as approximate and check with the brand
owner before print.

## Conference and event materials

Dark gradients are allowed here, and only here, per the gradient rules. The
guideline shows generative code-based graphics for annual conference materials.
