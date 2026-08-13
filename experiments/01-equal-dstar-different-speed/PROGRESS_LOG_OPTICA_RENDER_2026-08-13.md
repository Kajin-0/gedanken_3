# Progress Log Addendum — Optica Render Phase

**Date:** 2026-08-13  
**Status:** RENDERED-MANUSCRIPT PHASE COMPLETE / THEORY UNCHANGED

This addendum continues `PROGRESS_LOG.md` without replacing its detailed Step-01–49 correction history.

## 1. Submission architecture completed

The Applied Optics-oriented manuscript architecture from PR #2 was treated as frozen science rather than an invitation to reopen the theorem.

Current journal-facing title:

> **Task-dependent photodetector ordering under unknown arrival time**

The Rev. 3 text retains the exact claim boundary

```math
P_D^{scan}\ge P_{D,true}
```

and therefore concerns a **sufficient batch guarantee time** rather than exact full-scan detection time.

No numerical `T_G(L)` crossover curve was introduced.

## 2. Real LaTeX render produced

A standard single-file LaTeX manuscript was built from the frozen journal-facing text and the three existing reproducible figures.

Final local artifacts:

```text
paper_a_applied_optics.tex
paper_a_applied_optics.pdf
```

Final PDF state:

```text
11 pages
letter size
opens successfully
no encryption
no forms or JavaScript
```

The rendered manuscript was inspected visually at the title page, every figure page, back matter, and final reference pages.

Observed:

```text
no clipped text
no equation overflow
no figure overlap
no broken glyphs
no black squares
no truncated captions
no reference clipping
```

## 3. Compile failure found and fixed

The first TeX pass exposed a package collision:

```text
newtxmath + redundant amssymb -> \Bbbk redefinition conflict
```

Resolution:

```text
remove redundant amssymb;
retain amsmath + newtxmath.
```

This was a typesetting issue only. No equation or scientific claim changed.

## 4. Page-level style corrections

The first rendered PDF led to two visual corrections:

- title block changed to left alignment;
- figure caption label changed from `Figure` to `Fig.`.

The final PDF was recompiled and re-rendered after those changes.

## 5. Citation audit found two real bibliography errors

### Croce et al. 2004

The older Markdown bibliography had the wrong author order/list after the first two authors.

Correct APS list:

```text
R. P. Croce
Th. Demma
M. Longo
S. Marano
V. Matta
V. Pierro
I. M. Pinto
```

The rendered source now uses the corrected list/title/DOI.

### Milstein et al. 2008

The older Markdown bibliography incorrectly listed `S. M. Oh`, `D. A. Kashdan`, etc.

Correct Applied Optics authors:

```text
Adam B. Milstein
Leaf A. Jiang
Jane X. Luu
Eric L. Hines
Kenneth I. Schultz
```

The rendered source now uses the correct Applied Optics metadata.

These corrections are documented in

`PAPER_A_REFERENCE_AUDIT_2026-08-13.md`.

They do not change the prior-art or novelty disposition.

## 6. Cover letter drafted

Created:

`PAPER_A_APPLIED_OPTICS_COVER_LETTER.md`.

The draft describes the detector/task result and continuum Rice/Slepian witness without claiming:

- universal slow-detector preference;
- exact full-scan reversal;
- a new search-penalty principle;
- novelty or priority.

Author/contact/conflict/not-under-consideration placeholders remain intentionally unresolved until the author confirms them.

## 7. Render QA checkpoint

Created:

`PAPER_A_OPTICA_RENDER_QA_2026-08-13.md`.

Current production disposition:

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

## 8. Remaining work is author-owned submission metadata

The obvious remaining blockers before a real journal submission are now:

1. author name(s), affiliation(s), corresponding-author email;
2. Funding statement;
3. Disclosures/conflict statement;
4. decision on a versioned repository archive/DOI for Data Availability;
5. final cover-letter confirmations;
6. one independent review of the actual rendered PDF.

These are not reasons to reopen the Step-13–49 mathematical branch.

## Hard stop remains

**DO NOT CREATE STEP 50 BY DEFAULT.**

No new mathematical branch was opened during typesetting, citation correction, or cover-letter preparation.
