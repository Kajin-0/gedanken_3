# Experiment 13 Rev. 8 — Physical Review Applied production QA

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **FINAL REPRODUCIBLE BUILD PASS / 8 PAGES / AUTOMATED QA PASS / ALL-PAGE VISUAL QA PASS**

## Controlling production identity

```text
GitHub Actions run:   31916728949
source commit:        813fd8a2fc3011ef6e3ba63a0567cb3eee30297b
artifact ID:          9255118533
artifact digest:      a5d7aac0a5f3a68783a3510c9c2e8632af3e5b4e34f326e3012dd1aa6316bfcd
PDF SHA-256:          309655aec80a7778428beedad4c95b53b27b8ebae24143310b1f4fdc1c6faf87
TeX SHA-256:          08efd63da8e5558a07bbc5a4bc9be8667811bf2314705c69f257e30b9b565973
base BibTeX SHA-256:  029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d
Rev8 BibTeX SHA-256:  0f1b177bae87a55386506cf1438292411159610f86e5b75818a5c9af0d362fc7
figure SHA-256:       fc7e06f02a617e6b462ca57d51b36cff2c1cb34e890882eef2c378377cb06e8f
build_rev8.py:        7a443d100a0e14e77a2aaf413441099d8a3bbe02b4e21c8e2cb5990c46232ec5
finalize_rev8.py:     22446d79b75062ab56c6b4f26d269e9a4b4e4585cde2ac5ced04224e78f91c47
```

## Build chain

CI reconstructs the manuscript deterministically:

```text
build_rev4.py
-> recorded Rev4-to-Rev5 patch sequence
-> build_rev6.py
-> build_rev7.py
-> build_rev8.py
-> finalize_rev8.py
-> REVTeX/BibTeX compile
-> automated QA
-> 180-dpi page renders
-> artifact upload
```

The finalizer performs only claim-precision/self-containment edits to the Rev. 8 BIA paragraph:

```text
labels 26.6 meV as an adjacent-pair separation diagnostic;
states the interpolated BIA parameters in math-safe nm units.
```

## Automated QA

```text
pages:                  8
page size:              US Letter
PDF version:            1.5
undefined references:   none
undefined citations:    none
overfull boxes:          none
underfull boxes:         none
invalid math-mode glyph warnings: none
```

Remaining nonblocking warnings:

```text
nameref package warning about the label definition;
REVTeX class-level stuck-float warnings near the HgCdTe table/figure region.
```

Every expected figure and table is visibly present in the rendered artifact.

## Visual QA history

The first Rev. 8 scientific build expanded to nine pages, with the ninth page containing only the last references. It was rejected as a production regression.

The generic uniform-task subsection was then compressed while retaining its effective-rank relation and worst-orthogonal-task bound. The BIA paragraph was tightened. The resulting manuscript returned to eight pages.

A subsequent claim-precision pass changed the 26.6-meV wording from an unqualified selected-support splitting to an adjacent-pair separation diagnostic. A self-containment pass added the interpolated BIA parameters. The first parameter formatting used Angstrom notation inside math mode and generated invalid accent-command warnings; the final build instead uses eV nm^2 / eV nm and is warning-clean on that issue.

## All-page visual disposition

All eight controlling 180-dpi renders were inspected.

Checks passed:

```text
no clipped text;
no equation overflow;
no figure overlap;
no table clipping;
no broken glyphs;
no black boxes;
no unresolved-reference marks;
no missing figures;
no missing table;
no accidental blank page;
no mostly empty trailing bibliography page.
```

The new BIA paragraph occupies the upper-left portion of page 6 and remains legible. Figure 4 remains within column width and its caption clearly distinguishes the BIA-neglecting production baseline from the separate homogeneous BIA stress test.

## Scientific delta relative to Rev. 7

Rev. 8 does not change the central theorem, baseline HgCdTe production values, tightness factorization, or recycling/Ramo result.

It adds one substantive material-robustness result:

```text
homogeneous B8v+ / B8v- / C_k eight-band BIA stress model;
20072 active dimension-2 baseline blocks -> 40452 active dimension-1 BIA blocks;
S_a^act = 1 for every sampled active block in both cases;
continuous capacity 1.01764e6 -> 1.02203e6 m/s;
full bound/reference 0.11747 -> 0.11651;
relative full-ratio change about -0.82%;
independent-grid, multi-seed-capacity, and cluster-tolerance robustness checks pass.
```

The manuscript explicitly limits this result to a homogeneous effective eight-band stress model and does not claim atomistic/interface BIA completeness.

## Final production disposition

```text
LATEX COMPILE:                    PASS
BIBLIOGRAPHY:                     PASS
UNDEFINED REFS/CITES:             NONE
OVERFULL/UNDERFULL BOXES:         NONE
PAGE COUNT:                       8
ALL-PAGE VISUAL QA:               PASS
BIA PARAMETER SELF-CONTAINMENT:   PASS
BIA DIAGNOSTIC CLAIM PRECISION:   PASS
PRODUCTION BLOCKER:               NONE IDENTIFIED
```

Rev. 8 may be promoted to the active submission frontier if the focused scientific/editorial hostile review also passes.
