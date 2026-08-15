# Experiment 13 Rev. 6 — Physical Review Applied production QA

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **REPRODUCIBLE BUILD PASS / AUTOMATED QA PASS / ALL 8 PAGES VISUALLY INSPECTED / NO PRODUCTION BLOCKER IDENTIFIED**

## 1. Controlling production identity

```text
GitHub Actions run ID: 31905264642
head commit:           18920f64b49212f98173276ddad4e8be681fd667
artifact ID:           9252170376
artifact digest:       sha256:8b5645325d82d9ea6a302dd9ed33954f92f8f6f59281b53744db4843708c38f6
```

Production hashes:

```text
rev6_prapplied.tex
f80bcd5204d8fd014b06e85a3c76f5c3227eff46e002291942bd690e01b8d71a

rev6_prapplied.pdf
d9387b64d2ce4ba2b1a7383fa2092a5afe4e34af651df1e2450f9bdee1450fd7

rev4_unified.bib
029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d

rev6_figures.tex
07ee725da6522c7060c27644852a78977468ba02dd85ba0497e66f820f67b816

build_rev6.py
2caa9b9b4c76567af08ef161fd25699908b2709637a65efa715a5a419d22edd5
```

## 2. Reproducible build chain

CI performs:

```text
1. build_rev4.py -> frozen Rev. 4 built source;
2. apply recorded Rev. 4 -> Rev. 5 patch sequence;
3. build_rev6.py -> Rev. 6 source + Rev. 6 native vector figures;
4. REVTeX/BibTeX compile;
5. automated warning/hash/page QA;
6. 180-dpi render of every page;
7. artifact upload.
```

`build_rev6.py` contains hard regression gates requiring:

```text
thermodynamic uniform-capacity condition;
tau_bound^act terminology;
Fermi-statistical factor wording;
rank threshold 1e-6 m/s;
160-node production radial quadrature;
200 x 12 x 20 support check;
0.583 nm^-1 selected-transition extent;
rev6_figures.tex actually loaded by the manuscript.
```

It also rejects obsolete `tau_obs^act`, `Fermi/Kubo`, and old shell-observable tokens.

## 3. Automated QA

```text
pages:                  8
page size:              US Letter
PDF version:            1.5
undefined references:   none
undefined citations:    none
overfull boxes:          none
underfull boxes:         none
```

Remaining nonblocking REVTeX warnings:

```text
one nameref package warning;
class-level stuck-float warnings near the HgCdTe/table/readout regions.
```

Every expected float is visibly present and correctly placed in the controlling artifact.

## 4. All-page visual QA

All eight 180-dpi CI renders were inspected directly.

Checks passed:

```text
no clipped text;
no equation overflow;
no figure overlap;
no table clipping;
no broken glyphs;
no black boxes;
no missing figures;
no missing table;
no unresolved-reference marks;
no accidental blank manuscript page.
```

The thermodynamic-limit equation is visibly present in the theorem section on page 2.

The revised Fig. 2 visibly uses `Kubo map + Fermi bound` and labels the lower step as the Fermi inequality.

The full hierarchy uses `Fermi factor` rather than `Fermi/Kubo`.

The HgCdTe table and expanded reproducibility paragraph fit on page 5 without column overflow or increasing the manuscript beyond eight pages.

The recycling/Ramo section remains intact and legible.

## 5. Rev. 5 -> Rev. 6 visual scope

The manuscript remains eight pages. All pages change at least slightly because the restored thermodynamic equation changes equation numbering and downstream flow.

A direct render comparison found no new clipping or collision. The largest layout changes are expected around:

```text
page 2: restored thermodynamic condition;
page 3: renumbering + Fermi terminology;
page 5: expanded HgCdTe methods and renamed tightness quantity;
downstream pages: equation/float reflow only.
```

## 6. Scientific-scope regression checks

The Rev. 6 repair does **not** alter:

```text
cross-mu conductivity definition;
pointwise Fermi inequality;
Kubo-Greenwood normalization;
exact-shell capacity definition;
main finite-system population inequality;
shell-resolved capacity/selectivity decomposition;
production HgCdTe numerical values;
PT single-parent-doublet qualification;
immigration-death-exchange cross-spectrum;
Poisson final-sink cancellation;
Shockley-Ramo zero-DC / finite-frequency-support result.
```

The restored thermodynamic statement limits the macroscopic interpretation; it does not modify the finite-system inequality.

## 7. Production disposition

```text
LATEX COMPILE:               PASS
BIBLIOGRAPHY:                PASS
UNDEFINED REFS/CITES:        NONE
OVERFULL/UNDERFULL BOXES:    NONE
PAGE COUNT:                  8
ALL-PAGE VISUAL QA:          PASS
REV6 FIGURE SOURCE:          CONFIRMED
PRODUCTION BLOCKER:          NONE IDENTIFIED
```

Proceed to a focused scientific/editorial hostile review of Rev. 6 before promoting it to the repository-wide active frontier.
