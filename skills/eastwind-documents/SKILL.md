---
name: eastwind-documents
description: Produce Eastwind's standard business documents from a short brief — commercial proposals, statements of work, acts of acceptance, NDAs, and internal memos. Use when the user asks for a company document, contract annex, offer, or letterhead deliverable. Do not use for product specifications, engineering docs, or marketing copy.
metadata:
  owner: TODO
  status: draft
  updated: 2026-09-08
---

# Eastwind standard documents

> **DRAFT SCAFFOLD.** The sections below are the intended shape of this skill.
> Fill each one and delete this note. Authoring rules live in `docs/authoring.md`
> at the repository root.

## Purpose

TODO — one paragraph. What makes a document "the company's" rather than a generic
one: structure, required sections, legal boilerplate, tone, approvals.

## Document types

TODO — table of the types this skill covers, each pointing at its template and its
reference:

| Type | Template | Rules |
| :--- | :------- | :---- |
| TODO | `templates/…` | `references/…` |

## Before you start

TODO:

- Identify which document type is being asked for. If the request matches none of
  the types above, say so instead of improvising a format.
- Read the matching reference and open the matching template.
- Collect the required inputs — counterparty, scope, dates, amounts, signatories.
  List what is missing and ask for it; never invent a legal or commercial term.

## Steps

TODO — numbered, imperative.

## Rules

TODO — the standing constraints. Candidates:

- Never alter fixed legal wording; quote it verbatim from the reference.
- Never fill a required field with a plausible guess — leave a visible placeholder
  and list it as an open item.
- Flag anything that commits the company beyond the stated brief.

## Output

TODO — file format, structure, naming convention, and what to hand back alongside
the document (list of placeholders, list of assumptions).

**Language:** produce the document in the language of the user's request; default
to Russian when it is unclear. Fixed legal wording is reproduced in its original
language regardless.

## Open questions for the author

- Which document types are actually standard, and which are one-offs?
- Where do the current templates live, and who owns them?
- Which clauses are fixed by legal and must never be paraphrased?
- Is the output a `.docx` on letterhead, a PDF, or both?
- What is the approval path before a document goes to a counterparty?
