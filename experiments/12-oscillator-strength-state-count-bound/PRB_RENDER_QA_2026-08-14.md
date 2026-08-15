# Experiment 12 — PRB Rev6 render QA

**Date:** 2026-08-14  
**Scientific source:** `MANUSCRIPT_REV6_2026-08-14.md`  
**Target:** Physical Review B — Regular Article  
**Production state:** **REVTeX 4.2 COMPILE PASS / SIX-PAGE RENDER PASS / VISUAL QA PASS**

## 1. Production source

A PRB-oriented REVTeX 4.2 source was generated from frozen Rev6 without changing the scientific theorem or claim scope.

Local production filenames:

```text
experiment12_prb_rev6.tex
experiment12_prb_rev6.pdf
```

Exact SHA-256 hashes for the QA-passed local artifacts:

```text
experiment12_prb_rev6.tex
ecd9e09621c6fc3e87e9e6293f51ae4499b68a9e9ca878662a076e5d21700ced

experiment12_prb_rev6.pdf
b705d0868c3f2349a1821b5856f09792e8b2e0599d98efe38745c4e353229896
```

Source length:

```text
485 lines
27071 bytes
```

## 2. REVTeX configuration

The QA-passed source uses

```latex
\documentclass[aps,prb,reprint,amsmath,amssymb,longbibliography,floatfix,letterpaper]{revtex4-2}
```

with

```latex
\pdfpagewidth=\paperwidth
\pdfpageheight=\paperheight
```

to ensure the PDF driver respects REVTeX's US-letter page dimensions in the local TeX environment.

Additional packages are limited to

```text
bm
booktabs
placeins
```

No custom geometry, typography, or journal-mimicking layout code is used.

The local installation reports REVTeX 4.2f.

## 3. Bibliography handling

The local environment has `pdflatex` and REVTeX but lacks a `bibtex` executable. For reproducible QA, the 11 references were embedded in a standard `thebibliography` environment rather than changing or omitting citations.

This is a production workaround only; the reference content remains the Rev6 bibliography plus the Bethkenhagen TRK comparator already approved in the novelty audit.

## 4. Layout corrections made during rendering

The following were purely typesetting corrections and did not change scientific content.

### 4.1 Overfull occupation-definition line

The compact line defining `p_c`, `h_v`, and `D_cv` produced a small overfull box. It was split into a two-line `align` environment.

### 4.2 Central theorem

An initial `widetext` rendering of the main hierarchy produced the standard REVTeX horizontal rules and excessive page whitespace.

The same theorem was reformatted as an in-column boxed `aligned` equation:

```math
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega.
```

No factor, symbol, inequality direction, or definition changed.

### 4.3 Appendix table

The single-pass column table was changed to a `table*` so it spans both columns cleanly rather than remaining as a deferred single-column float.

A `\FloatBarrier` was placed immediately before the bibliography. This ensures Table II appears before the references rather than interrupting the bibliography on the final page.

### 4.4 Page size

The final PDF is true US letter:

```text
612 x 792 pt
```

rather than the local pdfTeX driver's default A4 media box.

## 5. Compile QA

The final source was compiled with three consecutive `pdflatex` passes.

Final log checks:

```text
OVERFULL BOXES: NONE
UNDEFINED REFERENCES: NONE
UNDEFINED CITATIONS: NONE
STUCK/DEFERRED FLOAT WARNINGS: NONE
OTHER LATEX WARNINGS: NONE
```

Only ordinary underfull-line diagnostics remain in several narrow two-column prose/reference lines; these do not indicate clipping or overflow.

## 6. PDF preflight

Final PDF:

```text
Pages: 6
Page size: 612 x 792 pt (US letter)
Encrypted: no
Openable with PyMuPDF: yes
Likely scanned: no
Forms/XFA: none
```

## 7. Page-level visual QA

All six pages were rendered to PNG at 180 dpi and inspected.

```text
PAGE 1: PASS
    title, anonymous author line, abstract, abstract theorem, and two-column opening all clean.

PAGE 2: PASS
    Fermi lemma, Kubo definition, theorem hierarchy setup, and shell-capacity equations clean.

PAGE 3: PASS
    active-subspace definitions, central boxed hierarchy, intrinsic corollary, low-energy result, and parabolic validation clean.
    The prior `widetext` whitespace/rule issue is eliminated.

PAGE 4: PASS
    Table I, Dirac validation, and prior-art comparison sections clean.

PAGE 5: PASS
    scope boundaries, conclusion, Appendix A/B prose and equations clean.

PAGE 6: PASS
    Table II appears before the complete bibliography; no float interrupts the reference sequence.
```

Global render checks:

```text
CLIPPED TEXT: NONE
OVERLAPS: NONE
BROKEN GLYPHS: NONE
BLACK SQUARES: NONE
MISSING EQUATIONS: NONE
MISSING TABLES: NONE
REFERENCE INTERRUPTION BY FLOATS: NONE
```

## 8. Scientific regression gate

The PRB rendering did **not** alter the frozen Rev6 science.

Controlling claims remain:

```text
independent-quasiparticle direct cross-mu absorbers only;
thermal optical-support population bound;
no universal dark-current / G_th / D* / finite-bandwidth-noise claim;
neutral excitons, indirect absorption, many-body spectral functions, and unconstrained photonic enhancement remain outside scope;
novelty and priority remain unestablished.
```

## 9. Disposition

```text
REV6 SCIENTIFIC CONTENT: FROZEN
REVTeX COMPILE: PASS
PDF PREFLIGHT: PASS
PAGE-LEVEL VISUAL QA: PASS
PRB PRODUCTION CHECKPOINT: PASS
```

Next work should be submission production only:

```text
1. final PRB-specific bibliography/metadata check;
2. author/affiliation/funding/disclosure placeholders;
3. cover letter;
4. independent review of the exact rendered PDF;
5. submission only after author-owned metadata is supplied.
```

Do not add new theory by default.