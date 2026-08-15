# Experiment 12 — PRB Rev9 exposition-revised typeset QA

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **TYPESET / RENDER QA PASS**

## Production basis

The production manuscript is the exposition-revised Rev9 text in

`MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`,

checked against the exact QA-passed nine-page Rev9 PDF supplied by the user. The revision preserves the Rev9 scientific content while adding explanatory scaffolding.

## Production source

Journal format:

```text
REVTeX 4-2
APS / PRB / reprint
US letter
two-column body
standard journal font sizing and margins
```

The exact final TeX source is archived in the repository as

`typeset/experiment12_prb_rev9_exposition_revised.tex.gz.b64`.

Recover it with

```bash
base64 -d experiment12_prb_rev9_exposition_revised.tex.gz.b64 | gunzip > experiment12_prb_rev9_exposition_revised.tex
```

Exact final hashes:

```text
TeX SHA-256  400a5a724765df3c9103a38e59c0647e86e62edbb255cb76c8730aede6949b87
PDF SHA-256  83aadc1f82a1fd5e453cb16dc7e2836f985e6af20a85a28011d85f1077d7ff2a
```

## Page count

```text
Original Rev9:              9 pages
Exposition-revised typeset: 12 pages
```

The increase is the natural consequence of the added explanatory prose. Font size, journal margins, equation sizing, and column geometry were not compressed to force the manuscript back to nine pages.

## Compile QA

Three `pdflatex` passes completed successfully.

```text
critical LaTeX/package/class warnings: none
overfull boxes:                      none
undefined references/citations:      none
stuck/unplaced floats:               none
```

Only ordinary underfull-box notices associated with narrow two-column composition remain; these are not clipping or overflow defects.

## Structural retention

Verified in the final PDF:

```text
main numbered equations: (1) through (50)
appendix equations:       (A1), (B1)
validation tables:        I, II, III
references:               18
sections:                 I–VIII + Appendices A/B
paper title:              retained
```

The Rev9 intrinsic-gap qualification, thermodynamic uniform-capacity condition, moving-window double-uniformity condition, projected-block SVD capacity, HgCdTe numerical diagnostics, scope limitations, and detector-performance nonclaims remain present.

## Visual QA

All 12 rendered pages were visually inspected after the final compile.

Pass criteria:

```text
no clipping
no text/equation overlap
no broken glyphs
no missing equations or tables
no bibliography collision
balanced two-column composition
standard PRB title/abstract treatment retained
```

Tables I, II, and III remain full-width, matching the visual treatment in Rev9. Table III required an explicit one-column-grid / two-column-grid transition rather than a normal floating `table*`; this keeps Table III on the final page with the bibliography, reproducing the useful final-page behavior of Rev9 without an otherwise blank trailing page or non-PRB separator artifacts.

Equation (49) was line-broken without introducing any new multiplication symbol or changing its mathematical content.

## Final disposition

```text
SCIENTIFIC CONTENT RETENTION: PASS
PRB/REVTEX TYPESETTING:       PASS
COMPILE QA:                    PASS
PDF PREFLIGHT:                 PASS
12-PAGE VISUAL INSPECTION:     PASS
READY FOR READER/REFEREE USE:  YES
```
