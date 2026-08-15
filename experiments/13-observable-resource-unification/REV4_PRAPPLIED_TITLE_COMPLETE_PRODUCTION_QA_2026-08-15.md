# Experiment 13 — Rev. 4 title-complete Physical Review Applied production QA

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **TITLE-COMPLETE PRODUCTION PDF PASS / SCIENTIFIC PAGES UNCHANGED / FINAL BIBLIOGRAPHY PAGE VISUAL QA PASS / HUMAN METADATA STILL REQUIRED**

## 1. Why this rebuild was required

After the initial seven-page production package passed full visual QA, a current Physical Review Applied submission preflight identified one remaining non-human production issue: several legacy BibTeX entries lacked article titles.

Physical Review Applied requires article titles in the published reference list and strongly encourages complete titled references at submission. The bibliography was therefore completed before freezing the submission identity.

The added metadata does not alter scientific prose, equations, figures, tables, numerical values, or claims.

## 2. Controlling title-complete production identity

```text
GitHub Actions run ID: 31901326001
head commit:           7b2f8fe1a9e92ba8ea778828c2682c5a374a1abb
artifact ID:           9251170031
artifact name:         experiment13-rev4-production
artifact SHA-256:      11d4bf5bd6262d6a19c6b1f0bdbdb7a7d16644981b9bd597c199e7a23ddbf32e
```

Production hashes:

```text
built TeX SHA-256:
c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9

PDF SHA-256:
d2e65ab9b0953e1f987c8c2c2b47e4d8558ac72989b84325590b3a0a67086ee8

BibTeX SHA-256:
029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d

figure-source SHA-256:
c577b1b09eaad28367b0a1318783feb95397b6d85b9ecf885200ed1d817c4f54
```

The built TeX and figure hashes are unchanged from the preceding QA-passed package. Only bibliography metadata changed.

## 3. Bibliography completion

Titles were added for the previously incomplete entries:

```text
Piotrowski and Gawron (1997)
Callen and Welton (1951)
Watanabe and Oshikawa (2020)
Gusynin and Sharapov (2006)
Gusynin, Sharapov, and Carbotte (2007)
Novik et al. (2005)
Laurenti et al. (1990)
Mirasol (1963)
Harrison and Lemoine (1981)
```

The Mao–Mendez-Valderrama–Chowdhury 2025 DOI was also added explicitly, and the Harrison–Lemoine page range was completed.

The added titles were checked against publisher/primary bibliographic records where available. The Laurenti title was cross-checked against the DOI-linked bibliographic record.

## 4. Automated QA

```text
pages:                  7
page size:              US Letter
PDF version:            1.5
undefined references:   none
undefined citations:    none
overfull boxes:          none
```

One pre-existing underfull paragraph warning remains visually harmless.

REVTeX emits the same pre-existing float-placement and `nameref` warnings as the prior package. All expected floats are visibly present and correctly placed.

## 5. Render regression comparison

The title-complete PDF was rendered at the same 150-dpi production QA setting and compared to the previously all-page-inspected PDF.

Rendered-page SHA-256 comparison:

```text
pages 1-6: byte-for-byte identical PNG renders
page 7:    changed, as expected from added bibliography titles
```

Therefore the complete theorem, figures, HgCdTe table, observability section, discussion, conclusion, and the start of the references retain the prior visual QA exactly.

## 6. Page-7 visual QA — PASS

The changed bibliography page was inspected directly.

Checks:

```text
all remaining references present;
added titles readable;
no reference collision between columns;
no broken diacritics;
no broken math in M/G/infinity or Hg/Mn formulas;
no clipped DOI-driven metadata;
no overflow into margins;
no accidental eighth page;
normal trailing white space only.
```

The page passes.

## 7. Scientific integrity

The scientific source hash is unchanged. No theorem, assumption, numerical value, figure, table, claim, or scientific sentence changed in this rebuild.

The previously completed rendered hostile review remains applicable to pages 1-6 exactly. Page 7 contains bibliography only and has now received separate visual QA.

## 8. Final production state

```text
SCIENTIFIC CONTENT:            FROZEN
REFERENCE TITLES:              COMPLETE FOR CURRENT BIBLIOGRAPHY
REVTeX COMPILE:                PASS
UNDEFINED REFS/CITATIONS:      NONE
OVERFULL BOXES:                NONE
PAGE COUNT:                    7
ALL SCIENTIFIC PAGES:          PRIOR QA PRESERVED BIT-FOR-BIT AT RENDER LEVEL
CHANGED BIBLIOGRAPHY PAGE:     VISUAL QA PASS
TITLE-COMPLETE PDF:            FROZEN PENDING HUMAN METADATA
```

## 9. Remaining blockers

Only human/submission metadata remain:

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding statement
submission-history / joint-submission declaration
final Data Availability Statement / archival citation decision
optional ORCID and referee suggestions/exclusions
```

Do not reopen scientific content by default. After metadata insertion, run one metadata-only rebuild/hash/all-page QA before actual submission.
