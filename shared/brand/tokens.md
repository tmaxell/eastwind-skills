# Eastwind design tokens

Colors, type, and spacing, extracted from `Brand Guidelines_L.pdf` (v1, MVP 1,
2024, 76 pp.), `Цвета фирм стиля EW.pdf`, `Инструкция по типографике.pdf`, and the
logo SVG sources. Hex values below were read out of the vector fills of the
guideline itself, so they are exact. Conflicts between sources are recorded in
[known-issues.md](known-issues.md) — read it before treating any value here as
final.

## Color

### Core three

| Role | Name | Hex | RGB | CMYK |
| :--- | :--- | :-- | :-- | :--- |
| Dark / logo wordmark | EW Dark blue | `#201E3B` | 32 30 59 | 100 97 42 58 |
| Light surface | EW Light Gray | `#F1F5F9` | 241 245 249 | — |
| Accent | EW Blue | `#382DDD` | 56 45 221 | 100 75 0 0 |

Any of the three may be text or background, but **default to the light theme**:
white or brand light gray as the background. The accent may only be EW Blue, or —
in special cases where blue is impossible — one of the six decorative colors.

**The 60/30/10 proportion is a rule, not a suggestion:**

- 60% white or brand light gray background
- 30% dark text or graphics
- 10% accent, to draw attention

### Brand scale

Twelve steps. Main is 70. Buttons, borders, and text in UI all take the same
step — that is the intended way to use the scale.

| Step | Hex | Notes |
| :--- | :-- | :---- |
| 5 | `#ECF1FF` | extra step, desaturated, for surfaces and states |
| 10 | `#DCE5FF` | |
| 20 | `#C0CFFF` | |
| 30 | `#9AAEFF` | |
| 40 | `#7282FF` | |
| 50 | `#5257FF` | |
| 60 | `#3B33F8` | |
| **70** | **`#382DDD`** | **main — the accent** |
| 80 | `#2922B1` | |
| 90 | `#27248B` | |
| 95 | `#181551` | extra step |
| 100 | `#201E3B` | **logo wordmark color — never use for text or content** |

New intermediate steps of the main color may be added for contrast.

### Neutral scale

Ten steps, main is 90. Carries most of the surface area: backgrounds, body text,
rules, table lines.

| Step | Hex | Typical role |
| :--- | :-- | :----------- |
| 10 | `#F8FAFC` | page background |
| 20 | `#F1F5F9` | brand light gray, panel background |
| 30 | `#E2E8F0` | dividers, table fills |
| 40 | `#CBD5E1` | borders |
| 50 | `#94A3B8` | disabled, muted |
| 60 | `#64748B` | secondary text |
| 70 | `#475569` | |
| 80 | `#334155` | |
| **90** | **`#1E293B`** | **main — body text and headings** |
| 100 | `#0F172A` | maximum contrast text |

For black-and-white print and for decks filled in by managers, the cold gray may
be swapped for a neutral gray.

### Decorative colors

For corporate illustration, infographics, dashboards, stickers, deck artwork, and
conference identity. One of them — usually Teal — may act as the accent when blue
is impossible.

| Hue | Main | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100 |
| :-- | :--- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :-- |
| Red | 60 | `#FBE9EA` | `#F8D5D7` | `#F1ABAF` | `#EB8187` | `#E4575F` | `#DD2D38` | `#B71E27` | `#89161D` | `#5C0F13` | `#2E070A` |
| Magenta | 70 | `#FBE9FA` | `#F8D5F5` | `#F1ABEA` | `#EB81E0` | `#E457D6` | `#DD2DCB` | `#B71EA8` | `#89167E` | `#5C0F54` | `#2E072A` |
| Purple | 60 | `#F1E9FB` | `#E4D5F8` | `#CAABF1` | `#AF81EB` | `#9557E4` | `#7A2DDD` | `#611EB7` | `#491689` | `#310F5C` | `#18072E` |
| Blue | 60 | `#E9F1FB` | `#D5E5F8` | `#ABCBF1` | `#81B2EB` | `#5798E4` | `#2D7EDD` | `#1E64B7` | `#164B89` | `#0F325C` | `#07192E` |
| Teal | 70 | `#E9FBFA` | `#D5F8F6` | `#ABF1ED` | `#81EBE4` | `#57E4DB` | `#2DDDD2` | `#1EB7AE` | `#168982` | `#0F5C57` | `#072E2B` |
| Green | 70 | `#EBFBE9` | `#D8F8D5` | `#B1F1AB` | `#89EB81` | `#62E457` | `#3BDD2D` | `#2AB71E` | `#1F8916` | `#155C0F` | `#0A2E07` |

Rules:

- Do not tie a decorative color to a product of the company.
- Do not mix them with brand blue in UI or advertising.
- In UI they appear only in very specific components — tag chips, visited links.

### System colors

Not used in design. UI states and warnings only, plus utility marks in working
documentation. Four steps each: 10, 20, 50, 60.

| State | 10 | 20 | **50 (main)** | 60 |
| :---- | :- | :- | :------------ | :- |
| Success | `#DEF2E6` | `#7FDCA4` | `#05C168` | `#11845A` |
| Error / Warning | `#FFF6E4` | `#FFE39B` | `#FDBD1A` | `#FFA800` |
| Danger | `#FFEFF0` | `#FFBEC2` | `#FF5A65` | `#DC2B2B` |

### Gradients

For infographics and for marking extreme values; usable in illustration alongside
primitive and generative graphics; dark gradients for exhibition and conference
materials.

- Never tint photos with a gradient.
- Never put a gradient in type.
- Never blend more than two colors in a linear gradient. Mesh backgrounds are the
  one exception.
- Steps 30–60 give bright gradients that read on both light and dark grounds.
  Blend darker or lighter steps for more contrast or more subtlety. A one-step
  blend within a single hue gives volume and depth.

Explicitly recommended pairs — treat this as the safe list:

| Light | Dark |
| :---- | :--- |
| Red 20 + Magenta 20 | Red 80 + Magenta 70 |
| Magenta 20 + Blue 20 | Magenta 70 + Blue 70 |
| Blue 30 + Purple 30 | Blue 70 + Purple 80 |
| Blue 40 + Teal 30 | Blue 70 + Teal 70 |
| Teal 30 + Green 30 | Teal 70 + Green 70 |

The guideline also states a general rule: never blend colors more than two steps
apart on the color wheel. It does not print the wheel order, and the recommended
pairs are not all adjacent, so do not infer an order — use the list above.

The Figma token library contains no gradients.

## Typography

### The four typefaces

| Typeface | Use | Availability |
| :------- | :-- | :----------- |
| **TT Firs Neue Variable** | Primary brand face: web, print, advertising. No emotional or period coloring. | Commercial licence. Not shipped with the open brand materials. |
| **Raleway** | Substitute when the brand face cannot be used. | Google Fonts, SIL Open Font License. Full Cyrillic including Ё. Variable axis wght 100–900 plus 18 static faces. |
| **Arial** | Administrative and records documents — letters, orders, banking-details forms. | System. |
| **Noto** | Languages TT Firs Neue does not cover (Chinese, Arabic, and so on). | Google Fonts. |

- Avoid italics.
- Avoid combining typefaces in one medium — they do not complement each other.

### Weights

TT Firs Neue Variable:

| Weight | Use |
| :----- | :-- |
| Thin, Light, Extra Light | With thin linear graphics — greeting text on cards, VIP gifts. Check against the printer's minimum stroke width before printing. |
| Regular | Body text |
| Normal | UI elements — button labels, input fields |
| Medium, Demi Bold | H1–H5 in UI |
| Demi Bold, Bold | Presentation headings |
| Extra Bold, Black, Extra Black | Display. Attention grabbers, large figures. At large sizes the fill may be removed and only the outline kept; enlarged phrases or figures may themselves form surfaces or masks holding an image. |

Raleway:

| Weight | Use |
| :----- | :-- |
| Regular | Body text |
| Medium | UI elements |
| Bold | H1–H5 in UI |
| Bold, Extra Bold | Presentation headings |
| Extra Bold, Black | Display |

Recommended maximum for a heading is 600 (Demi Bold). Avoid headings that are
heavier than that.

### Setting

- **No ALL CAPS** in UI headings, advertising, or presentations. The only
  exception is abbreviations, which may be set in caps.
- Hierarchy: each heading is roughly twice the size of the body text or of the
  level below it.
- Line height 130–160% for web and print.
- Paragraph spacing in body text ≈ the font size.
- Build contrast with color and weight. Outlines and coloring individual words
  are allowed for emphasis.
- The brand face has a distinctive character — experimenting with individual
  glyphs or words in corporate design is encouraged.

## Grid and spacing

The grid module is **8**. The logo is built on it.

- Divide the space into 2, 4, 8, 16, 32, or 64 columns or rows. Both vertical
  rhythm (columns) and horizontal rhythm (rows) apply.
- Three grid structures: no margins and no gutters; margins without gutters;
  margins and gutters. They may be mixed between the horizontal and vertical
  rhythm.
- Columns and rows are always equal to each other.
- Align text to the margins, not to canvas dividers.
- The base unit scales by ×2: 2, 4, 8, 16, 32, 64.

Spacing steps, where the grid cannot be used, everything still obeys the interval
rhythm — multiples 1×, 2×, 3×, 4×, 6×, 8×, 10×, 12×:

```
8   16   24   32   48   64   80   96
```

Aspect ratios for images and graphic frames: **16:9, 4:3, 3:2, 2:1, 1:1**. Always
measure the width against the columns; the height follows from it. Both landscape
and portrait orientations are allowed.
