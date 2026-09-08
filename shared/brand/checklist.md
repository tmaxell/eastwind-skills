# Brand compliance checklist

One list, used twice: as the self-check at the end of designing an artifact, and
as the scoring frame when reviewing one. Every item traces to a rule in
[tokens.md](tokens.md), [logo.md](logo.md), or
[layout-and-graphics.md](layout-and-graphics.md).

## Severity

| Level | Meaning | Examples |
| :---- | :------ | :------- |
| **blocker** | The artifact misrepresents the brand. Do not send it out. | Logo distorted, recolored, or rotated; a color outside the palette in a primary role; dark theme in a light-theme artifact; ALL CAPS headings; text set in Brand 100 |
| **major** | A rule is broken in a way a colleague would notice. Fix before sending. | Off-grid spacing; heading heavier than 600; italics; more than two colors in a gradient; decorative color mixed with brand blue; wrong typeface for the document class |
| **minor** | Polish. Fix when convenient. | Line height outside 130–160%; heading-to-body ratio far from 2×; an accent occupying noticeably more or less than 10%; inconsistent corner radii |

Report at most the top items by severity. A flat list of forty complaints gets
ignored; ten sorted ones get fixed.

## Color

- [ ] Every color appears in the token tables — core three, Brand, Neutral,
      decorative, or system. Off-palette values are a blocker in a primary role
      and a major elsewhere.
- [ ] Near-misses caught: a hex one or two characters away from a token is
      drift, not a new color. Name the token it should have been.
- [ ] Proportion approximately 60/30/10: light background, dark text, accent.
- [ ] The accent is Brand 70, or a decorative color only where blue is
      impossible.
- [ ] Brand 100 `#201E3B` is not used for text or content — only the logo, or a
      dark surface.
- [ ] Body text is Neutral 90 or 100.
- [ ] Decorative colors are not mixed with brand blue in UI or advertising, and
      are not tied to a specific product.
- [ ] System colors appear only in UI states, never as design colors.
- [ ] Gradients: at most two colors, from the recommended pair list, not on
      photos, not in type.

## Typography

- [ ] One typeface in the artifact. TT Firs Neue where licensed; Raleway as the
      substitute; Arial for administrative and records documents; Noto for
      scripts TT Firs Neue does not cover.
- [ ] No italics.
- [ ] No ALL CAPS headings. Abbreviations are the only exception.
- [ ] Heading weight ≤ 600.
- [ ] Weights match their roles — body Regular, UI Medium/Normal, headings
      Medium–Demi Bold, display Extra Bold and above.
- [ ] Heading ≈ 2× the body or the level below.
- [ ] Line height 130–160%.
- [ ] Paragraph spacing ≈ font size.

## Grid and space

- [ ] Spacing values come from the 8 scale: 8, 16, 24, 32, 48, 64, 80, 96.
- [ ] Columns and rows are equal to each other.
- [ ] Text aligns to the margins, not to canvas dividers.
- [ ] Image and graphic frames use 16:9, 4:3, 3:2, 2:1, or 1:1.
- [ ] The layout has air. Density that reads as "overloaded" is a major.

## Logo

- [ ] The right variant for the ground — light, dark, or monochrome.
- [ ] Not distorted, rotated, shadowed, rearranged, recolored, boxed, or set
      lowercase; the mark keeps its size relative to the wordmark; the wordmark
      never appears alone.
- [ ] Clear space of at least X on every side.
- [ ] At least 24 px tall.
- [ ] The compressed mark, not the horizontal logo, in small square placements.

## Graphics and photography

- [ ] Light theme.
- [ ] Geometric and abstract forms; arrows, lines, schemes, diagrams; no concrete
      objects.
- [ ] One of the three graphic styles, applied consistently.
- [ ] No cyberpunk, steampunk, Matrix, neon or glow, or meaningless ornament.
- [ ] Photos: light tones, soft shadows, natural and unstaged, eye level, clean
      frame, no filters, white balance on white.
- [ ] No text or graphics over a photo; if unavoidable, the logo sits on a plate.
- [ ] Photos are not tinted in brand colors or gradients.
- [ ] The compositional center is not cropped.

## Reporting format

For each finding:

```
[severity] Where — what is wrong — what it should be
```

For example:

```
[blocker] Slide 4, heading — #382CDD is not in the palette — Brand 70 #382DDD
[major]   Slide 7 — 20 px gap between cards — off the 8 scale, use 16 or 24
```

End with what works, briefly, and with the open questions: anything the guideline
does not settle, listed rather than guessed.
