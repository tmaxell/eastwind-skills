---
name: eastwind-brand-review
description: Audit a finished artifact against the Eastwind brand guideline and report violations by severity. Checks colors against the palette, typefaces and weights, the 8-px grid, logo handling, graphic and photographic style. Use when the user asks to check, review, audit, or validate a deck, document, PDF, image, or page for brand compliance, or asks whether something is on brand. Do not use to create or restyle an artifact — that is eastwind-brand.
metadata:
  owner: TODO
  source: DesignDocs/Brand Guidelines_L.pdf (v1, MVP 1, 2024) and the open brand materials
  updated: 2026-09-08
---

# Eastwind brand review

Judge an artifact that already exists. The output is a report, not a redesign:
what is wrong, how badly, and what it should have been.

Be adversarial. The point of a separate review is that it does not defend earlier
decisions. Do not soften a finding because the artifact is otherwise good, and do
not pad the list with preferences that no rule supports — every finding cites a
rule.

## When this applies

A request to check, review, audit, validate, or brand-check a finished artifact:
deck, PDF, Word document, image, diagram, page, or a batch of them. Also applies
to "is this on brand?" and to reviewing a template before it goes into circulation.

It does not apply to producing or fixing the artifact. If the user wants it
corrected after the review, that is a separate pass with `eastwind-brand`.

## Before you start

1. Read [references/checklist.md](references/checklist.md). It is the scoring
   frame and the severity model.
2. Read [references/tokens.md](references/tokens.md) for the values to check
   against.
3. Read [references/known-issues.md](references/known-issues.md) **before
   reporting anything**. Several apparent violations are unresolved contradictions
   in the source guideline. Reporting one as a violation is a false positive.
4. Read [references/logo.md](references/logo.md) and
   [references/layout-and-graphics.md](references/layout-and-graphics.md) when the
   artifact contains the logo or imagery.

Establish before judging:

- **What the artifact is** — the type determines which typeface is correct. Arial
  in an official letter is right; Arial in a deck is wrong.
- **Who it is for.** Internal working documents get the same rules but a softer
  severity call on polish items.
- **Whether the brand typeface was available** to whoever made it. Raleway instead
  of TT Firs Neue is compliance, not a violation.

## Steps

1. **Extract the measurable facts first.** If the environment allows running a
   script, `assets/check_brand.py` reads the colors and fonts actually present in
   a .pptx, .docx, .xlsx, .pdf, .svg, .html, or .css file and diffs them against
   the tokens:

   ```
   python3 assets/check_brand.py <file>
   ```

   It separates exact matches, drift (a value close to a token — almost always a
   typo, not a decision), and genuinely off-palette values, and it distinguishes
   fonts used in the content from fonts merely declared in styles.

   The script is optional. Where it cannot run, read the values off the artifact
   by eye and say in the report that the color audit was visual rather than
   measured.

2. **Judge what the script cannot.** Composition, hierarchy, whether the layout
   has air, whether the graphic style is one of the three sanctioned ones, logo
   treatment, photographic style, the 60/30/10 proportion. This is the part that
   needs looking.

3. **Walk the checklist** section by section: color, typography, grid and space,
   logo, graphics and photography. Do not skip a section because nothing jumped
   out; absence of a finding is itself a result.

4. **Assign severity** to each finding — blocker, major, or minor — per the
   checklist's definitions. Severity is about consequence, not about how obvious
   the mistake is.

5. **Sort and cut.** Order by severity. If the list runs past roughly ten items,
   report the top ten and say how many more of each severity remain. A flat list
   of forty findings does not get fixed.

## Rules

- **Every finding cites a rule and names the correction.** "The blue looks off" is
  not a finding. "`#382CDD` is not in the palette; Brand 70 is `#382DDD`" is.
- **Distinguish drift from a decision.** A value one or two characters from a
  token is a typo to correct, not a new color to argue about. Say which token it
  should have been.
- **Do not report the unresolved.** If `references/known-issues.md` records a
  contradiction, list it under open questions, not under violations.
- **Do not invent rules.** The guideline is silent on plenty — business card
  measurements, Pantone equivalents, the color wheel order. Silence is not a
  violation; say the rule does not exist.
- **Do not fix.** Describe the correction; leave the editing to a separate pass.
- **Do not grade on a curve.** A blocker in an internal deck is still a blocker.

## Output

```
## Brand review: <artifact>

Type: <artifact type> · Checked: <colors, typography, grid, logo, imagery>
Method: <measured with the script | visual>

### Findings

[blocker] <where> — <what is wrong> — <what it should be>
[major]   <where> — <what is wrong> — <what it should be>
[minor]   <where> — <what is wrong> — <what it should be>

<n> blocker, <n> major, <n> minor. <k> further minor findings not listed.

### What works

<two or three lines, specific>

### Open questions

<rules the guideline does not settle, or cases where sources conflict>
```

**Language:** write the report in the language of the request; default to Russian
when it is unclear.

## Failure patterns

- **Reporting the palette conflict as a violation.** `#201E3B` used for the logo
  is correct; `#201E3B` used for body text is the violation. The two are one page
  apart in the guideline and easy to confuse.
- **Flagging Raleway.** It is the sanctioned substitute, not a deviation.
- **Flagging fonts that are only declared.** A style sheet mentioning Calibri
  proves nothing about what the document uses.
- **Counting white and black as off-palette.** They are not palette entries and
  not violations.
- **Reporting everything at the same severity,** which leaves the reader to
  prioritise and therefore to ignore.
- **Auditing a template as if it were an artifact.** A template's defects
  propagate; raise its severity, do not lower it.
