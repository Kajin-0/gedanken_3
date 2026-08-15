# Experiment 13 Rev. 5 — Physical Review Applied production QA

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Target:** Physical Review Applied — Regular Article  
**Disposition:** **REPRODUCIBLE BUILD PASS / ALL-PAGE VISUAL QA PASS / SCIENTIFIC DELTA AUDITABLE AGAINST REV. 4**

## 1. Why Rev. 5 exists

An extreme adversarial review of the title-complete Rev. 4 manuscript found no fatal defect in the central optical population theorem, but identified three technical corrections and one major editorial vulnerability worth repairing before submission:

```text
Tr(G)/lambda_max(G) was described too loosely as stable rank;
the PT-isotropy statement required the single-parent-doublet qualification;
the stochastic model behind the two-pixel occupancy spectrum needed explicit reaction rates and PSD convention;
the paper risked making the definitional S tau = 1 identity look like the unifying theorem.
```

Rev. 5 repairs those issues and reframes the conceptual thesis around stage-specific non-transferability.

## 2. Reproducible source architecture

Rev. 5 is not maintained as an unrelated hand-edited duplicate of Rev. 4.

The CI path is:

```text
1. reconstruct the frozen Rev. 4 production source with build_rev4.py;
2. concatenate rev5_from_rev4.patch.part1..part3;
3. apply the recorded unified patch to the Rev. 4 source;
4. load rev5_figures.tex;
5. compile with REVTeX 4.2 / prapplied;
6. render every page and run automated QA.
```

This makes the Rev. 4 -> Rev. 5 scientific and editorial delta mechanically inspectable.

## 3. Controlling production identity

```text
GitHub Actions run ID: 31903046137
head commit:           8ac77c06accd02e56c43910b903ff53bb07a72dd
artifact ID:           9251615353
artifact digest:       sha256:64046cfd6972a9fbc810ab4a67ef61b27b9cd16249b7c666ecd75fabd5c5f843
```

Production hashes:

```text
rev5_prapplied.tex
9f45c235d3e2852fe04bf77a2adf519213e7af76ef8c9a7e26194a2cb10c72e7

rev5_prapplied.pdf
ce0fd199bb43652edf598ce7fa516e093e41fdc7a664d336092b8161ea7fa1c9

rev4_unified.bib
029d1029c487c99e277a24dc95ad536d10a41742992c89916a1991d423f39d3d

rev5_figures.tex
19c7b0f83ddadc9ff7000144ea09e257bb9d130fd898a519f88707bf54cbcf6d

patch part 1
d1d21f31aa647b3e0eb64d3d2ff61b80ac6be4bdca947f347c6d6b283499f3e0

patch part 2
cb4b0dce9f27b666fb1791782489c42766461c9f5bd9bfeb15edb50a73489685

patch part 3
bf320aabcfe838257633da897ab269b531a4bc66e1a2dda7b357d6a2afa5635c
```

## 4. Automated QA

```text
pages:                  8
page size:              US Letter
PDF version:            1.5
undefined references:   none
undefined citations:    none
overfull boxes:          none
```

One underfull paragraph warning remains:

```text
Underfull hbox, badness 2426, conclusion area.
```

Direct inspection shows no visible defect there.

REVTeX also emits the pre-existing class-level `nameref` warning and a stuck-float warning near the HgCdTe table. Every expected table and figure is present and correctly placed in the rendered manuscript, so these warnings are nonblocking.

## 5. Visual QA history

The first CI Rev. 5 artifact compiled successfully but direct visual inspection found one defect that automated QA could not detect: the standalone `1.000` label in Fig. 4 collided with the summary text.

That figure was repaired by moving the within-shell value into the summary block.

The repaired artifact was rebuilt from scratch through CI.

Render regression against the first Rev. 5 artifact:

```text
pages 1-4: identical
page 5:    changed, as expected from Fig. 4 repair
page 6:    changed by float/text reflow from the Fig. 4 height change
pages 7-8: identical
```

Pages 5 and 6 were then inspected directly at full rendered resolution.

## 6. All-page visual disposition

Direct inspection of all eight controlling pages found:

```text
no clipped text;
no equation overflow;
no figure overflow;
no table clipping;
no broken glyphs;
no black boxes;
no unresolved references;
no overlapping labels after the Fig. 4 repair;
no missing floats;
no accidental blank manuscript page.
```

Page 8 contains only the final bibliography entries and normal trailing white space.

## 7. Principal Rev. 5 scientific/editorial changes visible in the artifact

```text
new title: Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability;
S tau = 1 explicitly demoted to a definitional fixed-map normalization;
generic positive-effect quantity renamed r_eff(G)=Tr(G)/lambda_max(G)=srank(sqrt(G));
d>1 stated for the orthogonal-task bound;
certification explicitly conditional on domain/capacity/response attribution;
full bound/reference factorization promoted;
HgCdTe support fraction 0.66897 added to close the ~0.1175 full ratio;
PT isotropy restricted to single-parent-doublet sectors in the validation;
immigration-death-exchange process and two-sided angular-frequency PSD specified;
positive-sector channel-null proof made explicit;
Poisson final-sink marking/displacement proof made explicit;
stage-specific non-transferability promoted as the conceptual thesis.
```

## 8. Current production status

The Rev. 5 production PDF itself passes the render gate.

The remaining scientific gate is the dedicated hostile review of the actual Rev. 5 manuscript. If that review finds no new substantive defect, Rev. 5 should supersede Rev. 4 as the flagship submission text while Rev. 4 remains a reproducible historical checkpoint.
