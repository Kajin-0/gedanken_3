# Experiment 13 — Rev. 4 Physical Review Applied production QA

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **PRODUCTION PDF PASS / ALL-PAGE VISUAL QA PASS / SCIENTIFIC CONTENT UNCHANGED / HUMAN METADATA STILL REQUIRED**

## 1. Controlling production identity

The controlling production build is the latest successful GitHub Actions run after all figure, bibliography, font, float-safe prose, and builder-safety repairs:

```text
GitHub Actions run ID: 31900965632
head commit:           f41bdc6a4e580bfadd8155903f4127b2b63655ca
artifact ID:           9251078733
artifact name:         experiment13-rev4-production
artifact SHA-256:      1b4375f9953707ddf1e6b35bf55f91377370274d230298429398096f1b42e01a
```

The production package was independently downloaded and inspected page by page.

## 2. Production hashes

```text
built TeX SHA-256:
c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9

PDF SHA-256:
84c86c30019a0517246493ad4b9aacd60ac54051164b27ca7dfedac2fdba800f

BibTeX SHA-256:
c46f4e951139b772faeaa695147d3ad38b60c7a9f1a0690dba58d86de759e4df

figure-source SHA-256:
c577b1b09eaad28367b0a1318783feb95397b6d85b9ecf885200ed1d817c4f54
```

## 3. PDF properties

```text
pages:       7
page size:   612 x 792 pt / US Letter
PDF version: 1.5
journal:     Physical Review Applied REVTeX option
layout:      two-column
figures:     five native vector TikZ figures
```

## 4. Automated QA

The controlling build reports:

```text
undefined references: none
undefined citations:  none
overfull boxes:        none
```

One underfull paragraph warning remains:

```text
Underfull \hbox (badness 2351) at source lines 317--319
```

It produces no visible layout defect.

REVTeX also emits repeated `float is stuck` warnings and a `nameref` label-hook warning. These are **nonblocking in this package** because every expected figure and table is visibly present, correctly numbered, and entirely inside the intended page/column geometry in the rendered PDF. No float is missing or clipped.

## 5. All-page visual QA

Every page of the controlling PDF was rendered to PNG and inspected directly.

### Page 1 — PASS

- title and abstract clean;
- two-column body aligned;
- no clipping or overlap;
- author, affiliation, and email placeholders are visible and intentionally unresolved.

### Page 2 — PASS

- Fig. 1 staged-map diagram readable;
- complete Section II derivation present;
- Fermi endpoint inequality, selected conductivity, exact-shell capacity, and central theorem all present;
- Eq. (16) fits cleanly in one column as a two-line boxed theorem;
- no equation or text clipping.

### Page 3 — PASS

- Fig. 2 theorem-flow diagram readable;
- endpoint-lifted reciprocity section complete;
- Eq. (21) is explicitly identified as a normalized spectral-capacity identity rather than new matrix theory;
- task/coherence specialization begins without layout defects.

### Page 4 — PASS

- Fig. 3 selectivity/certification diagram has no label collision;
- coherent bright-state result and dispersive decomposition are readable;
- HgCdTe production section begins cleanly;
- float-safe prose now reads naturally into Table I;
- Table I is entirely inside the right column.

### Page 5 — PASS

- Fig. 4 HgCdTe decomposition is fully inside the left column;
- `0.5726 x 0.3068 = 0.1757` hierarchy is legible;
- BIA/PT qualification is intact;
- terminal-observability derivation is readable;
- no overlap between figure, equations, or adjacent column.

### Page 6 — PASS

- Fig. 5 final-sink versus finite-transit Ramo schematic is readable;
- Discussion and Conclusion are complete;
- acknowledgments placeholder is visibly separated from references;
- reference block begins cleanly.

### Page 7 — PASS

- remaining references render cleanly;
- no broken diacritics or math symbols;
- large trailing white space is ordinary bibliography pagination, not missing content.

## 6. Production regressions caught and repaired

The production process exposed several defects before this pass. They are preserved here because they should not be rediscovered or silently reintroduced:

1. T1 encoding was required for the Dąbrowski bibliography entries.
2. Scalable Latin Modern fonts were required because microtype rejected bitmap T1 fonts.
3. A bibliography title containing `3-\mu m` required math-safe micrometer encoding.
4. The first theorem-flow/selectivity/recycling figures were too compressed at APS column width and were simplified.
5. A `widetext` treatment of the central theorem introduced undesirable REVTeX grid rules and was rejected.
6. An intermediate theorem-builder regex accidentally consumed preceding manuscript content. The authoritative scientific source was never damaged. The builder now locates the unique theorem label and replaces only its nearest enclosing equation environment, with invariants that assert the staged-map equation and central derivation remain present.
7. The HgCdTe decomposition figure initially extended into the neighboring column and is now explicitly constrained to `0.94\columnwidth`.
8. The HgCdTe table produced an awkward visual prose join. The production builder now uses an explicit table-reference sentence and a float-independent post-table transition.

## 7. Scientific-content integrity

The production edits do **not** alter:

```text
- the central population theorem;
- its assumptions or scope;
- the selectivity/certification reciprocity;
- the task/coherence specializations;
- the dispersive decomposition;
- any HgCdTe numerical value;
- the BIA/PT caveat;
- the endpoint-Poisson result;
- the finite-transit Shockley-Ramo result;
- the bibliography's scientific content.
```

The only prose change is the float-safe HgCdTe table transition, which is semantically identical to the scientific source.

## 8. Submission blockers

The manuscript is **not yet submission-ready** because the source intentionally still contains human metadata placeholders:

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding statement
```

These are the remaining blockers. They are administrative, not scientific or production defects.

## 9. Freeze decision

```text
SCIENTIFIC DERIVATION:       PASS / FROZEN
NUMERICAL VALUES:            PASS / FROZEN
REFERENCE COMPLETENESS:      PASS AT CURRENT AUDIT LEVEL
REVTeX COMPILE:              PASS
UNDEFINED REFS/CITATIONS:    NONE
OVERFULL BOXES:              NONE
ALL-PAGE VISUAL QA:          PASS
PRODUCTION PDF:              FROZEN PENDING HUMAN METADATA
```

Do not reopen theory or numerical work by default. A new scientific revision requires a concrete theorem defect, numerical inconsistency, direct prior-art collision, referee/editor request, or a specific journal requirement.
