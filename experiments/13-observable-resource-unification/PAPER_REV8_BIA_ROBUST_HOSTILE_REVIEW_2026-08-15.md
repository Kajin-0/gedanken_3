# Extreme hostile review — Experiment 13 Rev. 8 BIA-robust manuscript

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Controlling artifact:** Actions run `31916728949`, PDF SHA-256 `309655aec80a7778428beedad4c95b53b27b8ebae24143310b1f4fdc1c6faf87`  
**Disposition:** **CENTRAL THEORY UNCHANGED / BIA ROBUSTNESS ADDITION PASSES / NO REV. 9 SCIENTIFIC REVISION TRIGGERED**

## Overall verdict

Rev. 8 is stronger than Rev. 7 for a Physical Review Applied submission because it closes the manuscript's clearest remaining material-physics question with a directly relevant robustness calculation rather than another caveat.

The new result is not that BIA is negligibly weak. The homogeneous BIA model strongly changes the fixed-k exact-shell degeneracy structure, yet the within-shell selectivity factor remains exactly unity for the sampled active blocks because those parent shells become one-dimensional. The final population-bound ratio changes by less than one percent after the full hierarchy is recomputed.

This is a useful negative/structural result and directly supports the paper's spectral-geometry interpretation.

## 1. Central population theorem — PASS / UNCHANGED

Rev. 8 does not alter the cross-mu Fermi inequality, Kubo-Greenwood convention, exact-shell capacity definition, finite-system population inequality, thermodynamic uniform-capacity condition, or liminf refinement.

No new theorem-level issue is introduced.

## 2. Full tightness hierarchy — PASS / UNCHANGED

The controlling factorization remains

```math
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

Rev. 8 tests the previously least constrained material factor rather than changing the decomposition.

The production BIA-off values remain the baseline shown in Table I and Fig. 4. The BIA calculation is explicitly identified as a separate homogeneous stress test and is not silently substituted for the production values.

## 3. BIA exact-shell logic — PASS

For the BIA-neglecting production model, each thermally relevant selected parent exact shell is a fixed-k PT doublet and the selected velocity block has equal nonzero singular values.

For the homogeneous BIA stress model, the sampled active fixed-k parent shells become one-dimensional. For any nonzero active block with a one-dimensional parent there is exactly one nonzero singular value, so

```math
rank(M_a)=r_{st,a}=1
```

and

```math
\boxed{\mathcal S_a^{act}=1.}
```

This conclusion does not depend on the magnitude of the BIA coefficients once the parent shell is genuinely one-dimensional.

The manuscript correctly avoids claiming that arbitrary multidimensional crystalline or accidental degeneracies must have unity selectivity.

## 4. Full homogeneous BIA implementation — HARD QA PASS

The side calculation does not rely on an ad hoc matrix perturbation. Its implementation was gated by:

```text
parent Gamma6-Gamma8 Kane P-block reproduction;
parent Gamma6-Gamma7 Kane P-block reproduction;
Hermiticity;
spinful time-reversal symmetry;
T-odd velocity transformation;
zero BIA Hamiltonian at Gamma;
analytic-vs-finite-difference dH/dkx comparison;
reduction of the Gamma8 C term to the previously symmetry-validated C-only implementation.
```

The parent P-block mismatches are at approximately `6e-17` and `1e-17`; the Hamiltonian/time-reversal/velocity symmetry residuals are zero to numerical representation; and the analytic derivative differs from finite differences by approximately `3.6e-10 eV nm`.

I find no implementation-level reason to reject the BIA result.

## 5. BIA parameter scope — DISCIPLINED

The manuscript now states the actual interpolated effective parameters used at the present composition:

```text
B8v+ = -0.2026 eV nm^2
B8v- = +0.00706 eV nm^2
C_k  = -0.00654 eV nm
```

and cites their HgTe/CdTe effective-parameter source.

It does not present these as an ab-initio determination for the alloy. The result is described as a homogeneous effective eight-band stress test, not a complete atomistic or interface inversion-asymmetry model.

Parameter uncertainty is not propagated. That is a remaining model-scope limitation, but not a correctness defect because the quantitative statement is explicitly a robustness stress test rather than a calibrated prediction of every real-HgCdTe BIA correction.

## 6. Numerical BIA hierarchy — PASS

The refined same-pipeline comparison gives approximately:

```text
BIA off:
continuous capacity      = 1.01764e6 m/s
full bound/reference     = 0.11747
active exact blocks      = 20072 dimension-2
S_a                      = 1 for every sampled active block

homogeneous B+/B-/C_k BIA:
continuous capacity      = 1.02203e6 m/s
full bound/reference     = 0.11651
active exact blocks      = 40452 dimension-1
S_a                      = 1 for every sampled active block
```

Thus

```text
capacity change          ~= +0.43%
full-ratio change        ~= -0.82%
within-shell factor      = unchanged at 1.
```

The arithmetic and interpretation are internally consistent.

## 7. Robustness tests — PASS

The full-BIA ordinary capacity supremum is multi-seed stable to approximately `1.4e-8` fractional spread at the controlling chemical potential.

Independent hierarchy grids keep the full-ratio shift at approximately one percent or smaller.

Sweeping the exact-shell clustering tolerance from `1e-9` to `1e-5 eV` leaves all sampled active BIA blocks one-dimensional, with

```text
selectivity_min = 1
selectivity_max = 1
nonunit-selectivity population fraction = 0.
```

This substantially weakens the possible objections that the BIA result is optimizer luck, coarse quadrature, or numerical near-degeneracy clustering.

## 8. 26.6-meV diagnostic — CLAIM PRECISION FIXED

The maximum `26.6 meV` quantity is not used in the theorem or hierarchy. It is an adjacent-pair separation diagnostic over selected-support k points and is used only to show that the applied inversion-breaking perturbation is not numerically infinitesimal.

Rev. 8 now labels it that way rather than calling it an unqualified spin splitting. This removes a potential band-tracking objection.

## 9. Uniform-task compression — PASS

To preserve the eight-page manuscript after adding the BIA result, the uniform-task subsection was compressed.

The retained content is the useful content:

```math
r_{eff}(G)=\frac{\operatorname{Tr}G}{\lambda_{max}(G)},
```

```math
\mathcal S_{mix}=d/r_{eff},
\qquad
\tau_{mix}=r_{eff}/d,
```

and the worst-orthogonal-task bound.

No result used by the coherent specialization or later sections was removed. The compression improves the paper's editorial balance because this was already the most detachable generic subsection.

## 10. Abstract / significance — PASS

The abstract remains dense but contribution-ranked. The new BIA sentence is justified because it directly answers the most obvious realism objection to the HgCdTe material example.

It does not displace the central theorem or tightness hierarchy from the abstract's first positions.

## 11. Recycling / readout section — NO REGRESSION

The BIA revision does not touch the immigration-death-exchange spectrum, channel-null proof, final-sink Poisson cancellation, or finite-transit Shockley-Ramo result.

No downstream regression was found.

## 12. Publication-overlap architecture — STILL RESOLVED

Experiment 13 remains the sole active submission manuscript. Experiment 12 is frozen fallback/development provenance.

The BIA addition makes the flagship even more distinct scientifically, but it does not authorize concurrent submission of the overlapping Experiment-12 manuscript.

## 13. Rendered presentation — PASS

The first Rev. 8 build expanded to nine pages and was rejected. Compression restored the paper to eight pages.

The final artifact has:

```text
8 pages;
no undefined references/citations;
no overfull or underfull boxes;
no invalid math-mode glyph warnings;
no visible clipping;
no figure/table overlap;
no missing floats;
no mostly empty trailing bibliography page.
```

The BIA paragraph is dense but legible. Figure 4 remains readable and distinguishes the production baseline from the separate BIA stress result.

## 14. Strongest surviving referee attacks

The remaining attacks are now limited and nonfatal:

### A. Effective BIA parameter uncertainty

The BIA stress uses one published effective parameter set with alloy interpolation and does not propagate parameter uncertainty.

This could be requested in review, but the manuscript does not claim a precision BIA correction for real devices. It claims robustness of the hierarchy within a specified homogeneous model.

### B. Interface / atomistic BIA

Not included and explicitly excluded from the claim.

### C. Exceptional multidimensional degeneracies

The exact one-dimensional-shell argument does not cover every possible high-symmetry/accidental multidimensional exact shell. The manuscript explicitly says so.

### D. Overall breadth

The article remains broad, but the generic task material has now been compressed and the added BIA calculation increases applied-material coherence rather than breadth.

None of these is sufficient to trigger a further scientific revision before submission.

## Referee-style disposition

A severe but fair post-Rev. 8 report would now be approximately:

> The added inversion-asymmetry calculation strengthens the HgCdTe validation. The authors do not merely perturb the previously degenerate model: they verify the homogeneous BIA implementation against the Kane basis and relevant symmetries, reoptimize the capacity, and repeat the shell-resolved hierarchy. The result that generic BIA-split active shells remain at unit within-shell selectivity because they are one-dimensional is both conceptually useful and numerically supported. The final bound/reference ratio changes by less than one percent in the stated model. The remaining limitations are primarily model scope rather than internal inconsistency. I do not identify another technical revision necessary before peer review.

## Final disposition

```text
CENTRAL THEOREM:                     PASS / UNCHANGED
THERMODYNAMIC FORMALISM:             PASS / UNCHANGED
FULL TIGHTNESS HIERARCHY:            PASS / UNCHANGED
BASELINE HgCdTe VALIDATION:          PASS / UNCHANGED
HOMOGENEOUS FULL-BIA IMPLEMENTATION: PASS
BIA EXACT-SHELL RESULT:              PASS
BIA CONTINUOUS CAPACITY:             PASS
BIA GRID/SEED/CLUSTER ROBUSTNESS:    PASS
BIA CLAIM SCOPE:                     PASS
TASK-SECTION COMPRESSION:            PASS
RECYCLING/RAMO SECTION:              PASS / UNCHANGED
PUBLICATION OVERLAP:                 RESOLVED UNDER SUPERSESSION POLICY
RENDERED PDF:                        PASS
REV. 9 REQUIRED:                     NO
```

Rev. 8 should supersede Rev. 7 as the flagship submission manuscript. Further scientific revision should require a concrete external criticism, counterexample, or numerical inconsistency rather than additional defensive polish.
