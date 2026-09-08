# Known conflicts and open questions

Places where the source materials disagree with each other or leave a rule
undefined. Each entry says what was adopted and why. Nothing here is invented:
where the sources give no answer, the entry says so instead of supplying one.

Everything below was found in the files under `DesignDocs/`. Nobody at Eastwind
has confirmed these readings yet — treat the "adopted" column as a working
default, and raise the flagged ones with the brand owner.

## 1. `#201E3B` — core color or logo-only?

The color page calls EW Dark blue one of the three core colors and says any of
the three may serve as text or background. The palette page, two pages later,
labels the same value Brand 100 and says: *"Цвет 100 — цвет текста в логотипе — не
используйте его для текста и контента!"*

Practice settles it. In `Eastwind_Сorporate Overview_2026.pdf` and
`Преимущества MP.pdf`, body text is Neutral 90 `#1E293B` and `#201E3B` appears
only in the logo.

**Adopted:** body text is Neutral 90 or 100. `#201E3B` is reserved for the logo
wordmark and for dark surfaces. **Needs confirmation.**

## 2. EW Light Gray printed as "000"

In the 76-page `Brand Guidelines_L.pdf`, the HEX field under EW Light Gray reads
`000`. In the earlier `Brand_Guidelines_26_11_2024.pdf` the same field reads
`F1F5F9`, and the logo SVG files use `#F1F5F9` for the light field.

**Adopted:** `#F1F5F9`. The newer file has a typo.

## 3. The commercial proposal template is off-palette

`КП_template_april 2026_en.docx` uses:

| Value | Occurrences | Verdict |
| :---- | :---------- | :------ |
| `#382CDD` | 10 | One character off Brand 70 `#382DDD`. Drift, not a color. |
| `#140731` | 28 | Not in the palette. |
| `#7D7D7D` | 56 | Not in the palette; nearest is Neutral 50–60. |
| `#FAFAFA` | 52 | Not in the palette; nearest is Neutral 10 `#F8FAFC`. |
| `#3C1594`, `#6B37E2` | 3 | Not in the palette. |
| `#E4575F` | 1 | Red 50. Valid. |

Its Office theme accents (`5FD8FE`, `FFB624`, `23DEB2`, `8455F5`, `F55555`,
`4DE733`) are entirely off-palette.

**Adopted:** the template is a structural reference, not a color reference. When
producing a proposal, map its colors onto the tokens. **The template itself needs
a brand pass.**

## 4. `#21203A` in the order blank

`Бланк приказ без реквизитов EW 2024.docx` contains `#21203A`, one step off
`#201E3B`. Minor drift in an otherwise Arial-and-black document.

**Adopted:** treat as drift; use `#201E3B` if that color is needed at all.

## 5. The color wheel order is not printed

The gradient rules forbid blending colors "more than two steps apart on the color
wheel", but no wheel order is given. The recommended pairs include
Magenta + Blue, which is not adjacent under the obvious reading
(Red–Magenta–Purple–Brand–Blue–Teal–Green).

**Adopted:** use only the explicitly recommended pairs listed in
[tokens.md](tokens.md). Do not infer an order. **Needs the wheel from the brand
owner.**

## 6. No Pantone or RAL equivalents

The core color table has Pantone and RAL columns, and every cell reads `0`. There
are no print spot-color equivalents defined for the brand.

**Adopted:** for spot-color print, escalate rather than choose a Pantone.

## 7. TT Firs Neue is not available

The primary face is commercial and is not shipped with the open brand materials.
Only Raleway is present, under the SIL Open Font License, with full Cyrillic
coverage including Ё and a variable weight axis of 100–900.

**Adopted:** any artifact produced outside a licensed design environment uses
Raleway. Never embed or redistribute TT Firs Neue.

## 8. Business card measurements are not specified

Section 07 shows card layouts but prints no dimensions, margins, or type sizes.

**Adopted:** any reconstruction is approximate and must be checked before print.

## 9. Brand voice vs. visual scope

The guideline's introduction defines the archetype, tone of voice, and key
messages. Only the parts that drive visual decisions were carried into
[layout-and-graphics.md](layout-and-graphics.md). The copy rules — no mentoring
tone, no exclamation marks, no caps lock, no emoji, avoiding the letter "ё" —
belong to a writing skill, not to these.
