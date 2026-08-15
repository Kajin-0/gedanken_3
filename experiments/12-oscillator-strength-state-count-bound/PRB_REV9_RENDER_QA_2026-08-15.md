# Experiment 12 — PRB Rev9 render QA

**Date:** 2026-08-15  
**Target:** Physical Review B — Regular Article  
**Disposition:** **COMPILE PASS / PDF PREFLIGHT PASS / NINE-PAGE VISUAL QA PASS**

## Artifacts

```text
experiment12_prb_rev9.tex
SHA-256 da4d929d77d817e48c6661d61ffcdcaac82a8503b9594a8dafcca27e838c0f7b

experiment12_prb_rev9.pdf
SHA-256 849e0653b6007c35a92967e812ab584ede70914714c2315bf849839701232e0b
```

## Compile

Three consecutive `pdflatex` passes.

Final log:

```text
OVERFULL BOXES: NONE
UNDEFINED REFERENCES: NONE
UNDEFINED CITATIONS: NONE
LATEX WARNINGS: NONE
PACKAGE WARNINGS: NONE
STUCK/OVERSIZE FLOATS: NONE
```

## PDF preflight

```text
Pages: 9
Page size: US letter, 612 x 792 pt
Encrypted: no
Openable with PyMuPDF: yes
Likely scanned: no
XFA: none
```

## Visual QA

All nine pages were rendered at 180 dpi and inspected.

```text
PAGE 1: PASS — title/abstract/opening clean
PAGE 2: PASS — Fermi/Kubo derivation clean
PAGE 3: PASS — capacity theorem and low-energy quantifiers clean
PAGE 4: PASS — equality/Dirac validation clean
PAGE 5: PASS — first-order Kane section and revised cross-mu/reference distinction clean
PAGE 6: PASS — reproducibility equations, SVD capacity prescription, diagnostics and literature transition clean
PAGE 7: PASS — four-column HgCdTe table and scope/conclusion clean
PAGE 8: PASS — conclusion and appendices clean
PAGE 9: PASS — Table III and complete bibliography clean
```

Global checks:

```text
CLIPPING: NONE
OVERLAPS: NONE
BROKEN GLYPHS: NONE
MISSING EQUATIONS: NONE
MISSING TABLES: NONE
FLOAT/BIBLIOGRAPHY COLLISION: NONE
```

A Rev8-to-Rev9 render comparison was also generated; page-count growth from 8 to 9 pages is attributable to the new numerical-reproducibility derivation and diagnostics rather than unrelated layout changes.

## Scientific regression gate

The central theorem and previously reported realistic HgCdTe ratios are unchanged. Rev9 changes only corollary domain, numerical-method transparency, terminology, and diagnostics requested by the supplied review.

```text
REV9 RENDER: PASS
NEXT ACTION: HOSTILE REVIEW OF REV9
```