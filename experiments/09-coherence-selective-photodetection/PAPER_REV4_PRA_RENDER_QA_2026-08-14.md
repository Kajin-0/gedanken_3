# Experiment 09 — Rev. 4 PRA render QA

**Date:** 2026-08-14  
**Target:** Physical Review A — Regular Article  
**Manuscript:** `PAPER_DRAFT_REV4_PRA_2026-08-14.md`  
**Status:** LOCAL REVTEX RENDER PASSES SCIENTIFIC/PRODUCTION QA / AUTHOR METADATA AND FINAL SUBMISSION PACKAGE STILL OPEN

## Render basis

The Rev. 4 journal-facing text was typeset locally with installed `revtex4-2` using a PRA two-column reprint layout:

```latex
\documentclass[aps,pra,reprint,amsmath,amssymb,longbibliography,floatfix]{revtex4-2}
```

The rendered package uses the three figures generated reproducibly by

```text
numerics/paper_rev3_figures.py
```

The author and affiliation fields remain explicit placeholders and were not fabricated.

## Final local artifacts

```text
exp09_rev4_pra.tex
exp09_rev4_pra.pdf
```

Final PDF state:

```text
7 pages
letter size
not encrypted
opens successfully
REVTeX two-column layout
all 3 figures present
all 8 bibliography entries present
```

SHA-256 of the final rendered PDF:

```text
275fe4e23a4d52b59f121e602e6f844249b98f9ff912c01297e2a4c1ebbe8d11
```

SHA-256 of the local LaTeX source:

```text
0fd4d98ca19043b5826422e988fee3a39cb8641883d2c7b973899ad106214451
```

## Cross-reference and citation repair

The first automated `latexmk` pass stopped because the local environment lacks the `bibtex` executable and REVTeX emits an auxiliary notes bibliography even though the manuscript itself uses an explicit `thebibliography` environment.

This was an environment/build-tool issue, not a manuscript citation defect.

The manuscript was then compiled directly with repeated `pdflatex` passes. The final `.aux` contains all equation/figure/table labels and all eight `\bibcite` records.

Final checks:

```text
unresolved citations: 0
unresolved equation references: 0
unresolved figure references: 0
unresolved table references: 0
literal ?? markers in extracted PDF text: 0
```

## Figure QA

### Fig. 1 — detector mechanism and two clocks

The first visual render exposed overlapping dephasing/recycling labels and crowded gate text. The figure-generation script was revised twice.

Final figure clearly separates:

```text
photon-created bright state;
bright counted sector;
fast extraction kappa_N;
local dark event;
dark manifold;
local dephasing gamma_N;
slow return r_- ~ lambda_N/N;
efficiency-selected gate condition;
accepted local-dark integral.
```

Final disposition: **PASS**.

### Fig. 2 — exact finite-N scaling verification

Exact finite-`N` curves are shown for representative rate sectors with asymptotic slope guides. The curves reproduce the intended scaling classes and remain legible in the two-column manuscript.

Final disposition: **PASS**.

### Fig. 3 — scalable-efficiency ceiling

The first render had an annotation collision. The final version separates the balanced-line formula from the vertical boundary and clearly labels the `alpha<beta`, `alpha=beta`, and `alpha>beta` sectors.

Final disposition: **PASS**.

## Page-level visual QA

The final 7-page PDF was rendered to PNG at 180 dpi and inspected as a full contact sheet plus full-size checks of the figure pages.

Observed:

```text
no clipped equations;
no equation overflow;
no figure overlap;
no broken glyphs;
no black squares;
no truncated captions;
no unresolved references;
no reference-page clipping;
no malformed two-column breaks.
```

The final reference page is balanced across both columns after cross-references are resolved.

## Remaining LaTeX warning

REVTeX reports one deferred-float warning during `\clearpage` processing. All three floats are present in the final PDF; Fig. 3 is correctly placed on page 6.

A test that converted Fig. 3 into a two-column float removed the warning but increased the manuscript from 7 to 8 pages without improving readability. The rendered seven-page result is therefore retained.

This is treated as a benign layout warning rather than a scientific or visible production defect.

## PDF preflight

The PDF skill preflight reports:

```text
Pages: 7
Encrypted: False
Openable (PyMuPDF): True
Likely scanned: False
XFA present: False
```

## Scientific claim regression

The final render does not revive the failed Rev. 0/Rev. 1 claims.

Specifically:

```text
static 1/N projection presented as novelty: NO
end-to-end photon QE claimed: NO
universal kT ln(C) gated penalty claimed: NO
new generic decoherence phase transition claimed: NO
new coherent collective detector architecture claimed: NO
same-mode background rejection claimed: NO
```

The active theorem remains the bounded-resource scalable internal-efficiency ceiling plus its supporting accepted-event scaling laws.

## Current production disposition

```text
REV. 4 SCIENTIFIC TEXT: PASS CURRENT INTERNAL AUDIT
PRA REVTEX COMPILE: PASS
CITATIONS/CROSS-REFERENCES: PASS
FIGURE CALLOUT ORDER: PASS
FIGURE VISUAL QA: PASS
PAGE-LEVEL VISUAL QA: PASS
PDF PREFLIGHT: PASS
AUTHOR NAME/AFFILIATION: OPEN
FINAL AUTHOR DECLARATIONS: OPEN
FINAL CITATION-NETWORK NOVELTY CONFIDENCE: NOT ESTABLISHED
```

The next useful step is one final adversarial review of the **rendered PDF itself**, followed by author metadata and actual submission preparation if no new scientific defect appears.
