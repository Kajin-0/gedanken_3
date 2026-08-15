# Experiment 13 Rev. 7 — Physical Review Applied production QA

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **REPRODUCIBLE BUILD PASS / AUTOMATED QA PASS / ALL 8 PAGES VISUALLY INSPECTED / NO PRODUCTION BLOCKER IDENTIFIED**

## 1. Controlling production identity

```text
GitHub Actions run ID: 31912951827
head commit:           f464dc966e0223f6b8c3ff1e51f82f948c8e950c
artifact ID:           9254179157
artifact digest:       sha256:29072be047b7a8174404ba02f32de1615c45c06daebcd5627b9f5cda54339d56
```

Production hashes:

```text
rev7_prapplied.tex
806ebffeb398a892550c62b9bcb7bcfa0c85c75a9c349add6f0ad628103ac5d6

rev7_prapplied.pdf
e40627dfb12f122cafb013415a475efffabda02befbff757ebd80b2da993da50

rev4_unified.bib
029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d

rev7_figures.tex
e60d35acc894ca5317d4ca5b8dce1b7b8869cfa62ca0cb6475181cfb5728d0c6

build_rev7.py
c76134decf039e03e97da44488fda669aa15ddb9b5bfc5ce7f37b27aedb48415
```

## 2. Reproducible build chain

CI performs:

```text
1. build_rev4.py -> frozen Rev. 4 built source;
2. recorded Rev. 4 -> Rev. 5 patch sequence;
3. build_rev6.py -> audited Rev. 6 source + figures;
4. build_rev7.py -> bounded final re-review corrections;
5. REVTeX/BibTeX compile;
6. automated warning/hash/page QA;
7. 180-dpi render of every page;
8. artifact upload.
```

`build_rev7.py` contains hard gates requiring:

```text
thermodynamic liminf qualifier;
reference-domain support-coverage qualifier;
carrier-cutoff convergence statement;
"numerically converged" HgCdTe wording;
tau_bound^act terminology;
Rev. 7 figure source.
```

It rejects:

```text
unknown-arrival transient construction;
production-resolution HgCdTe wording;
tau_obs^act;
Fermi/Kubo terminology.
```

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

Remaining nonblocking warning:

```text
one nameref package warning about the definition of \label
```

No visible reference or hyperlink defect was found.

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
no accidental blank manuscript page;
no bibliography regression.
```

Specific Rev. 7 checks:

```text
thermodynamic liminf equation is visible and clean;
full hierarchy remains legible after the new support-coverage qualifier;
carrier-cutoff convergence sentence fits without crowding;
Fig. 1 small labels are enlarged without collision;
Fig. 3 top annotation is enlarged and shortened;
Fig. 4 labels/values are enlarged without clipping;
recycling/Ramo section remains intact;
references remain complete on page 8.
```

## 5. Rev. 6 -> Rev. 7 scientific scope

Rev. 7 does **not** change:

```text
cross-mu conductivity definition;
pointwise Fermi inequality;
Kubo-Greenwood normalization;
exact-shell capacity definition;
main finite-system population inequality;
full tightness factorization;
HgCdTe production numerical values;
support-rank threshold or sweep;
PT single-parent-doublet qualification;
immigration-death-exchange spectrum;
Poisson final-sink cancellation;
Shockley-Ramo zero-DC / finite-frequency-support result.
```

The only mathematical addition is the explicit liminf form of the thermodynamic statement when ordinary intensive thermodynamic limits are not assumed.

## 6. Production disposition

```text
LATEX COMPILE:               PASS
BIBLIOGRAPHY:                PASS
UNDEFINED REFS/CITES:        NONE
OVERFULL/UNDERFULL BOXES:    NONE
PAGE COUNT:                  8
ALL-PAGE VISUAL QA:          PASS
REV7 FIGURE SOURCE:          CONFIRMED
PRODUCTION BLOCKER:          NONE IDENTIFIED
```

Rev. 7 is the controlling technical manuscript. Do not create Rev. 8 for defensive polish by default.
