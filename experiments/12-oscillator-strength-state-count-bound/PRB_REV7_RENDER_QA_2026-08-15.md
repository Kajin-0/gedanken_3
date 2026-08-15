# Experiment 12 — PRB Rev7 render QA

**Date:** 2026-08-15  
**Target:** Physical Review B — Regular Article  
**Scientific disposition:** **MAJOR EXTERNAL REVIEW ADDRESSED / REV7 COMPILE PASS / SEVEN-PAGE VISUAL QA PASS**

## 1. Why Rev7 exists

Rev7 responds to the supplied extreme adversarial review of the PRB Rev6 manuscript. The review found the central theorem mathematically sound but identified three principal remaining vulnerabilities:

```text
uniform thermodynamic boundedness of v_B^cap not formalized;
physical restrictiveness of v_B^cap not demonstrated in a realistic material Hamiltonian;
van Roosbroeck-Shockley / fluctuation-dissipation positioning absent.
```

The central Fermi inequality, Kubo normalization, rank/operator-norm step, parabolic/Dirac validation values, and 10-um numerical arithmetic are unchanged.

The detailed response is in:

`REV6_EXTERNAL_REVIEW_RESPONSE_2026-08-15.md`

The realistic-capacity reproducibility script is:

`numerics/kane_8band_capacity.py`

---

## 2. Rev7 production artifacts

Local files:

```text
experiment12_prb_rev7.tex
experiment12_prb_rev7.pdf
```

SHA-256:

```text
experiment12_prb_rev7.tex
ec5f46f0256b320861fabdd3ad5e61832c1f20c03ea95216979207fe92dc488d

experiment12_prb_rev7.pdf
e481354dc25a0526dbe0b4eb636a0ca733aae8678f3a12b7a2d0a349d25c0740

kane_8band_capacity.py
cc71c406cba56314a9caca14f26f9ebb38235bf00c1e403b9f3db5eeae1b29a7
```

The GitHub connector used in this session can write UTF-8 repository text but does not accept a local-file reference for the generated TeX/PDF artifact. Therefore the exact source hash is recorded here and the scientific changes are preserved separately in `MANUSCRIPT_REV7_CHANGESET_2026-08-15.md`.

---

## 3. Principal scientific revisions

### 3.1 Formal thermodynamic-limit condition

For a finite-system sequence `V_j -> infinity`, Rev7 promotes to a formal hypothesis

```math
\bar v_B^{cap}
=\limsup_{j\to\infty}v_{B,V_j}^{cap}<\infty.
```

The finite-volume theorem remains exact without this assumption. The nonzero macroscopic density-floor interpretation requires it.

### 3.2 Realistic 8x8 HgCdTe Kane capacity

For the standard first-order 8x8 Kane Hamiltonian used for bulk HgCdTe optical calculations,

```math
\hat v_x=(1/\hbar)\partial H_K/\partial k_x=v_K M_x.
```

The two nontrivial weighted-star blocks of `M_x` each have squared coupling sum

```math
3/4+1/4+1/2=3/2.
```

Thus

```math
\boxed{\|\hat v_x\|_{op}=\sqrt{3/2}\,v_K}
```

and projector contraction yields, for every selected window,

```math
\boxed{v_B^{cap}\le\sqrt{3/2}\,v_K.}
```

This capacity ceiling is independent of sample volume in the first-order model and therefore satisfies the thermodynamic uniform-boundedness condition automatically.

Using the experimentally extracted HgCdTe Kane velocity `v_K=(1.07 +/- 0.05)e6 m/s` gives a central capacity scale about `1.31e6 m/s`. Using `E_P ~= 18.8 eV` gives approximately `1.286e6 m/s`.

The exact `sqrt(3/2)` coefficient is explicitly restricted to the first-order 8x8 Kane Hamiltonian. Second-order 8x8 k.p treatments introduce finite k-dependent corrections and are cited as the quantitative full-model boundary.

### 3.3 Equilibrium-relations positioning

Rev7 explicitly distinguishes:

```text
van Roosbroeck-Shockley:
    absorption -> radiative generation/recombination;

fluctuation-dissipation/KMS neighborhood:
    dissipative response <-> equilibrium observable fluctuations;

Experiment 12:
    cross-mu direct spectral weight
    + finite per-shell optical capacity
    -> minimum one-body thermal support population.
```

No radiative lifetime, recombination coefficient, or readout-noise spectrum is inferred by the theorem.

### 3.4 Other referee corrections

Rev7 also:

```text
adds an E=mu limiting prescription;
qualifies support-rank population as a discontinuous exact support-dimension construct;
states that applying the theorem to measured sigma_1 requires sigma_1 ~ sigma_1^cross or a decomposition;
qualifies full-spectrum parabolic saturation as an ideal effective two-band optical-model statement;
makes the low-energy consequence explicitly conditional on integrated spectral weight + uniformly bounded capacity;
clarifies the 90% 10-um witness as internal absorptance of admitted power / ideal AR or index matching;
adds a Kane-capacity anchored illustrative 10-um lower column of about 5.33e11 cm^-2.
```

---

## 4. Compile QA

Rev7 was compiled with three consecutive `pdflatex` passes.

Final log scan:

```text
OVERFULL BOXES: NONE
UNDEFINED REFERENCES: NONE
UNDEFINED CITATIONS: NONE
LATEX/PACKAGE WARNINGS: NONE
STUCK/DEFERRED FLOAT WARNINGS: NONE
```

PDF preflight:

```text
Pages: 7
Page size: 612 x 792 pt (US letter)
Encrypted: no
File size: 305985 bytes
```

---

## 5. Page-level visual QA

All seven pages were rendered at 180 dpi and inspected.

```text
PAGE 1: PASS
  revised title, abstract, theorem statement, and equilibrium-context introduction clean.

PAGE 2: PASS
  cross-mu transition definitions, E=mu prescription, Fermi lemma, and Kubo setup clean.

PAGE 3: PASS
  capacity definition, formal thermodynamic limsup condition, support-rank definitions,
  and central theorem clean.

PAGE 4: PASS
  conditional low-energy result, parabolic qualification, Dirac checks, and Table I clean.

PAGE 5: PASS
  new HgCdTe 8x8 Kane-capacity derivation, VRS/FDT comparison, and established-theory sections clean.

PAGE 6: PASS
  scope refinements, conclusion, measured-conductivity qualification, internal-absorptance
  Appendix-A setup, and Kane-anchored column statement clean.

PAGE 7: PASS
  Table II, occupation-fluctuation appendix, and complete 16-reference bibliography clean.
```

Global visual checks:

```text
CLIPPED TEXT: NONE
OVERLAPS: NONE
BROKEN GLYPHS: NONE
MISSING EQUATIONS: NONE
MISSING TABLES: NONE
FLOAT/BIBLIOGRAPHY COLLISION: NONE
```

---

## 6. Rev6-to-Rev7 render comparison

The PDF comparison reports:

```text
Rev6 pages: 6
Rev7 pages: 7
changed pages: 7
```

The changes are expected because the revision modifies the title/abstract and inserts a substantive Kane validation plus equilibrium-positioning section. No unexpected isolated layout artifact was observed in the page-by-page inspection.

---

## 7. Disposition

```text
CENTRAL THEOREM: PASS / UNCHANGED
EXTERNAL MAJOR-REVISION ISSUES: ADDRESSED
REALISTIC MULTIBAND CAPACITY EXAMPLE: ADDED
THERMODYNAMIC LIMIT: FORMALIZED
VRS/FDT POSITIONING: ADDED
REV7 COMPILE: PASS
REV7 VISUAL QA: PASS
PRB SIGNIFICANCE READINESS: MATERIALLY IMPROVED
NOVELTY/PRIORITY: STILL NOT ESTABLISHED
```

The next scientific action should be another hostile review of **Rev7 itself**, not further theorem expansion by default.