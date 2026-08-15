# Experiment 12 — PRB Rev8 render QA

**Date:** 2026-08-15  
**Target:** Physical Review B — Regular Article  
**Disposition:** **REVTeX COMPILE PASS / EIGHT-PAGE VISUAL QA PASS / PDF PREFLIGHT PASS**

## Artifacts

```text
experiment12_prb_rev8.tex
SHA-256 18424af7052262b2974a94a5ed6f85495951674fdcc0333624f3426f635df3a9

experiment12_prb_rev8.pdf
SHA-256 36e3fa7c01053bd5ec20f235cbb3f4f99c5297c3d44f11845440f77dff1da402
```

## Compile state

The final Rev8 source was compiled with three consecutive `pdflatex` passes.

Final log:

```text
OVERFULL BOXES: NONE
UNDEFINED REFERENCES: NONE
UNDEFINED CITATIONS: NONE
STUCK/DEFERRED FLOAT WARNINGS: NONE
LATEX/PACKAGE WARNINGS: NONE
```

The new realistic-material validation initially produced a REVTeX float-placement warning. Both compact validation tables were converted to two-column `table*` floats, after which the final compile is warning-free.

Ordinary underfull-line diagnostics in narrow bibliography/prose lines are not layout failures.

## PDF preflight

```text
Pages: 8
Page size: US letter, 612 x 792 pt
Encrypted: no
Openable with PyMuPDF: yes
Likely scanned: no
XFA: no
```

## Visual QA

All eight pages were rendered at 180 dpi using the PDF skill renderer and inspected.

```text
PAGE 1: PASS — title, abstract, new Rev8 significance sentence, opening text.
PAGE 2: PASS — Fermi/Kubo definitions and theorem setup.
PAGE 3: PASS — shell-capacity theorem and new double-uniformity low-energy formulation.
PAGE 4: PASS — equality and Dirac validation.
PAGE 5: PASS — Table I, first-order Kane capacity, start of second-order HgCdTe validation.
PAGE 6: PASS — HgCdTe headline bound/exact result and theory-positioning sections.
PAGE 7: PASS — Table II, scope, conclusion, shifted Appendix-A window and conservative Kane-bound wording.
PAGE 8: PASS — recalculated Table III, fluctuation appendix, complete bibliography.
```

Global checks:

```text
CLIPPED TEXT: NONE
OVERLAPS: NONE
BROKEN GLYPHS: NONE
MISSING EQUATIONS: NONE
MISSING TABLES: NONE
FLOAT/BIBLIOGRAPHY COLLISIONS: NONE
```

## Rev7 → Rev8 comparison

A render comparison was generated with the PDF compare workflow. Page count increases from 7 to 8 because the second-order HgCdTe bound/exact validation is a substantive new section. No unrelated visual regression was identified.

## Scientific regression gate

The central finite-volume inequality is unchanged.

Rev8 adds only:

```text
a rigorous moving-window double-uniformity statement;
precision fixes requested by the Rev7 re-review;
a second-order eight-band HgCdTe-like bound/exact validation;
recomputed Appendix-A values after moving above the exact edge.
```

Claim boundaries remain unchanged.

## Disposition

```text
REV8 COMPILE: PASS
REV8 PDF PREFLIGHT: PASS
REV8 PAGE-LEVEL VISUAL QA: PASS
CENTRAL THEOREM REGRESSION: NONE FOUND
NEXT ACTION: INDEPENDENT EXTREME ADVERSARIAL REVIEW OF REV8
```