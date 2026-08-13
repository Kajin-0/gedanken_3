# Paper A — Optica Render QA

**Date:** 2026-08-13  
**Target:** Applied Optics  
**Status:** LOCAL LATEX RENDER PASSES PAGE-LEVEL QA / AUTHOR METADATA AND FINAL BACK-MATTER DECLARATIONS STILL OPEN

## Production basis

The journal-facing Rev. 3 text was rendered as one standard LaTeX source, consistent with current Optica guidance to use standard LaTeX where possible and to keep the submission in one `.tex` file.

The local source uses a simple portable article layout rather than trying to reproduce Optica's production typography exactly. Current Optica guidance states that the templates are a guide and visual styling is optional; content is formatted consistently in production.

## Local render

Rendered source artifact:

```text
paper_a_applied_optics.tex
```

Rendered PDF artifact:

```text
paper_a_applied_optics.pdf
```

Final pre-submission render after citation corrections:

```text
11 pages
letter size
not encrypted
no JavaScript/forms
PDF opens and renders successfully
```

## Compile regression found and fixed

The first local TeX pass imported both `newtxmath` and `amssymb`, which collided on the symbol definition `\Bbbk` in the installed TeX distribution.

Resolution:

```text
remove redundant amssymb import;
retain amsmath + newtxmath.
```

This was a package-level production issue only. No manuscript mathematics changed.

## Page-level visual QA

The final PDF was rendered to PNG pages using the repository PDF QA workflow and visually inspected.

Checked explicitly:

- page 1 — title, author placeholders, abstract, opening text;
- figure pages for all three figures;
- back-matter page;
- final two reference pages after citation corrections.

Observed:

```text
no clipped text;
no equation overflow;
no figure overlap;
no broken glyphs;
no black squares;
no truncated captions;
no reference clipping.
```

## Style corrections made after first render

Two presentational corrections were made after visually inspecting the first PDF:

1. changed the title block from centered default LaTeX styling to a left-aligned title block;
2. changed the figure-caption label from `Figure` to `Fig.`.

The final render contains both changes.

## Figures

The three figures are generated reproducibly by

```text
numerics/paper_a_submission_figures.py
```

and referenced with stable names:

```text
paper_a_fig1_evidence.png
paper_a_fig2_covariance.png
paper_a_fig3_feasibility.png
```

Figure 3 remains intentionally one-sided:

```math
P_{FA,s}\le0.0336428,
\qquad
P_{FA,f}\ge0.0624701.
```

It does not visually represent either bound as an exact probability.

## Citation correction incorporated into final render

The final local LaTeX/PDF corrects two citation-metadata errors found during the primary-source audit:

- Croce et al. 2004 author order/list;
- Milstein et al. 2008 author list.

See `PAPER_A_REFERENCE_AUDIT_2026-08-13.md`.

## Back matter still requiring author confirmation

The rendered PDF intentionally contains placeholders for:

```text
author name(s);
affiliation(s);
corresponding-author email;
Funding statement;
Disclosures statement.
```

These must not be fabricated. Current Optica submission guidance also requires a Data Availability statement and a cover letter; both are represented in the current package, but the author-specific declarations must be confirmed before actual submission.

## Data Availability

Current rendered wording points to the public research repository and the experiment directory containing the analytical derivations and reproduction scripts.

Before submission, decide whether the final wording should cite a specific archived release/DOI rather than a mutable GitHub branch. A versioned archive would be preferable for a final publication record but is not required for this internal render checkpoint.

## Final render disposition

```text
LATEX COMPILE: PASS
PDF PREFLIGHT: PASS
PAGE-LEVEL VISUAL QA: PASS
FIGURE CALLOUT ORDER: PASS
FIGURE-BOUND SEMANTICS: PASS
REFERENCE PAGE LAYOUT: PASS
AUTHOR METADATA: OPEN
FUNDING: OPEN
DISCLOSURES: OPEN
FINAL DATA-ARCHIVE VERSIONING: OPEN
```

No reason was found to reopen the Paper-A theorem or the Step-13–49 mathematical branch.
