---
name: eastwind-brand
description: Design a new artifact in Eastwind's visual identity — presentation, one-pager, report, diagram, banner, social image, or web page — or restyle an existing one to it. Applies the brand palette, typography, 8-px grid, logo rules, and graphic style from the Eastwind brand guideline. Use when the user asks to design, lay out, style, or make something look like Eastwind. Do not use to audit a finished artifact for compliance — that is eastwind-brand-review — and do not use to write the copy or to draft standard business documents.
metadata:
  owner: TODO
  source: DesignDocs/Brand Guidelines_L.pdf (v1, MVP 1, 2024) and the open brand materials
  updated: 2026-09-08
---

# Eastwind brand design

Produce artifacts that a colleague would recognise as Eastwind's without being
told. The brand is quiet: a light ground, a lot of air, precise geometry, one
strong accent. Getting it right is mostly a matter of restraint — the failure
mode is not ugliness, it is a layout that could belong to any company.

## When this applies

A request to design, lay out, style, restyle, or "make it look like ours" for any
visual artifact: deck, one-pager, report, diagram, poster, banner, social image,
email header, web page, or document layout.

It does not apply to auditing something already finished, to writing the words, or
to assembling a contract, act, or proposal from a template.

## Before you start

1. Read [references/tokens.md](references/tokens.md). Never pick a color, size,
   or spacing value that is not in it.
2. Read [references/artifact-types.md](references/artifact-types.md) and find the
   section for the format you are producing. It says which typeface applies —
   which differs between a deck, an official Word document, and a proposal.
3. Read [references/known-issues.md](references/known-issues.md). Several rules in
   the source guideline contradict each other; that file records which reading was
   adopted and which questions are still open. Do not resolve them differently on
   your own.
4. Read [references/logo.md](references/logo.md) whenever the logo appears, and
   [references/layout-and-graphics.md](references/layout-and-graphics.md) whenever
   the artifact contains imagery, illustration, or a graphic style decision.

Establish these before designing. If any is missing, ask rather than assume:

- **Format and dimensions** — deck 16:9, A4 portrait, banner size, screen width.
- **Audience** — customer, partner, or internal. Customer-facing work has no
  latitude for improvisation.
- **Language** of the artifact.
- **Whether this is new work or a restyle.** For a restyle, the existing file
  matters more than any brief: keep its structure and change only what the brand
  requires.
- **Whether the brand typeface is available.** TT Firs Neue is commercial and is
  not part of the open materials; without a licensed environment the artifact uses
  Raleway.

## Steps

1. **Pick the artifact type** and load its section from
   `references/artifact-types.md`. Use the existing template or reference
   implementation named there instead of starting from nothing.

2. **Assign color roles before choosing any color.** Decide what is background,
   what is text, what is the single accent, and what is a secondary surface. Then
   fill those roles from the tokens:
   - background — white, Neutral 10, or Neutral 20;
   - text — Neutral 90, or Neutral 100 for maximum contrast;
   - accent — Brand 70;
   - borders and dividers — Neutral 30 or 40.
   Hold the 60/30/10 proportion. If the accent is covering much more than a tenth
   of the surface, it has stopped being an accent.

3. **Set the type.** One typeface for the whole artifact. Body Regular, UI
   elements Medium, headings Medium to Demi Bold, display Extra Bold and above.
   Heading roughly twice the body size. Line height 130–160%. Paragraph spacing
   about equal to the font size. No italics. No ALL CAPS headings.

4. **Lay out on the 8 grid.** Every gap, margin, and gutter comes from
   8/16/24/32/48/64/80/96. Columns and rows equal. Text aligned to the margins.
   Images and graphic frames in 16:9, 4:3, 3:2, 2:1, or 1:1.

5. **Place the logo** per `references/logo.md`: the right variant for the ground,
   clear space of at least X, at least 24 px tall, the compressed mark in small
   square placements.

6. **Add graphics, if any,** in one of the three sanctioned styles — illustrative
   with a metaphor, primitives, or generative — and keep to geometric, abstract
   forms. Arrows, lines, schemes, and diagrams are the house vocabulary.

7. **Self-check against [references/checklist.md](references/checklist.md)** and
   fix what it catches before handing anything over. Report anything you could not
   fix rather than quietly leaving it.

## Rules

These hold for the whole task, not just the step where they appear.

- **Never invent a value.** Colors, weights, and spacing come from the tokens. If
  a case is not covered, say so and propose the nearest covered pattern.
- **Light theme.** The guideline forbids the dark theme for graphics and
  photography. Dark grounds are for the dark logo variant and for conference
  materials, not as a default.
- **`#201E3B` is the logo wordmark color.** Do not set text or content in it. Body
  text is Neutral 90.
- **One accent.** Brand 70. A decorative color may take the accent role only when
  blue is genuinely impossible, and then it does not appear alongside brand blue.
- **Decorative colors are never tied to a product** of the company.
- **Do not put text or graphics over a photograph.** If material must sit on one,
  the logo goes on a plate.
- **Do not modify the logo** in any way listed under "Never" in
  `references/logo.md`.
- **Never embed or redistribute TT Firs Neue.** It is licensed commercially.
- When the request conflicts with the guideline, follow the guideline and say
  what you changed and why. When the user insists after that, comply and record
  the deviation in the handover note.

## Output

Deliver the artifact in the format asked for, plus a short handover note
containing:

- which artifact type and template were used;
- the tokens assigned to each role, by name and hex;
- any deviation from the guideline, with the reason;
- open questions the guideline does not settle — listed, not guessed.

Where the artifact is code — a web page, an HTML export, an SVG diagram — declare
the palette as named custom properties (`--brand-70`, `--neutral-90`) rather than
as bare hex values scattered through the file, so the next person can see the
roles.

**Language:** produce the artifact in the language of the request; default to
Russian when it is unclear. These instructions are in English; the deliverable
need not be.

## Failure patterns

Seen in the company's own materials, so these are not hypothetical:

- **A hex one character off a token.** `#382CDD` instead of Brand 70 `#382DDD`
  appears ten times in the current proposal template. Copy values from the tokens
  file; do not retype them.
- **Inheriting an Office theme.** A Word or PowerPoint file carries default
  accent colors that have nothing to do with the brand. Set colors explicitly.
- **Treating an existing company file as a color reference.** Some are on brand,
  some have drifted. `references/known-issues.md` says which is which.
- **Filling the page.** The archetype is the sage: air is a brand attribute, not
  wasted space.
- **Decoration for its own sake.** Ornament with no meaning is explicitly
  forbidden; so are cyberpunk, steampunk, Matrix, neon and glow effects.
- **Designing only the primary state.** Decide what the artifact looks like in
  black-and-white print and at small sizes before calling it done.
