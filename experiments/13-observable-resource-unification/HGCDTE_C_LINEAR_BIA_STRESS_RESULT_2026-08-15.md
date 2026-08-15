# HgCdTe C-linear BIA stress result

**Date:** 2026-08-15  
**Scope:** theoretical/numerical stress test; C_k-linear Gamma8 BIA only  
**Status:** **REFINED AUDIT PASS / EXACT-SHELL PREDICTION CONFIRMED / BIA EFFECT MIGRATES TO CAPACITY, SUPPORT, AND FERMI FACTORS / NO REV. 8 TRIGGER**

## 1. Question

Rev. 7 validates the full population-tightness hierarchy in a second-order eight-band HgCdTe model that neglects explicit zincblende bulk inversion asymmetry (BIA). In that model every thermally important active fixed-k parent shell is a PT doublet and

```math
\mathcal S_a^{act}=1.
```

The natural robustness question is whether realistic inversion breaking makes the within-shell factor appreciably less than one.

The preceding analytical note

`HGCDTE_BIA_EXACT_SHELL_SELECTIVITY_ANALYSIS_2026-08-15.md`

shows that this intuition is generally wrong for the theorem's exact-shell decomposition. Generic BIA splitting makes the active fixed-k parent shell one-dimensional, and any nonzero one-dimensional parent block has active selectivity exactly one.

This numerical stress test checks that mechanism in the HgCdTe model.

---

# 2. BIA perturbation used

The calculation adds only the standard k-linear Gamma8 zincblende BIA invariant weighted by `C_k`.

In the J=3/2 Gamma8 block,

```math
H_C
=
\frac{2C_k}{\sqrt3}
\left[
\{J_x,J_y^2-J_z^2\}k_x
+
\{J_y,J_z^2-J_x^2\}k_y
+
\{J_z,J_x^2-J_y^2\}k_z
\right],
```

where the braces denote Hermitian symmetrization.

The HgTe/CdTe endpoint values used by Li et al., Phys. Rev. B 95, 035308 (2017), are

```text
HgTe: C_k = -0.0746 eV A
CdTe: C_k = -0.0234 eV A
```

with linear alloy interpolation. For the present composition

```text
x_Cd = 0.179727548444
```

this gives

```text
C_k = -0.0653979495 eV A.
```

The analytic x-velocity includes the derivative of this BIA term.

**Important scope limitation:** the quadratic `B+`/`B-` BIA couplings are omitted. This is therefore a **C-linear BIA stress test**, not a complete zincblende BIA calculation.

---

# 3. Numerical setup

Refined hierarchy quadrature:

```text
carrier integral: 120 x 10 x 16, |k| <= 2.0 nm^-1
optical audit:    120 x 10 x 16, |k| <= 1.0 nm^-1
selected window:  Eg <= DeltaE <= 0.5 eV
energy clustering tolerance: 1e-7 eV
active rank threshold: 1e-6 m/s
```

For both BIA-off and C-linear-BIA-on models, the global selected projected-block capacity is independently searched as a continuous ordinary supremum with seeded differential evolution.

The refined workflow is

`.github/workflows/hgcdte-bia-c-linear-refined.yml`.

Controlling run:

```text
GitHub Actions run: 31915284219
source commit:      7f75832a74f575a6cb49abf6823b485391ef009a
artifact ID:        9254738471
artifact digest:    af36deaa0bb33a5f4af557bd957c5690b2ef79bd7cc81de8beb579be3f987079
```

A separate 80 x 8 x 12 versus 50 x 6 x 8 audit gave the same qualitative result and similar percent shifts.

---

# 4. Baseline validation

The refined BIA-off calculation gives

```text
mu                         = 0.1354615106 eV
n_ref                      = 1.005246445e17 cm^-3
n_active                   = 6.713386175e16 cm^-3
support fraction           = 0.667834859
eta_F                      = 0.307116485
sampled capacity           = 1.014653706e6 m/s
continuous capacity        = 1.017639607e6 m/s
tau_cap (continuous)       = 0.572727662
tau_bound (continuous)     = 0.175894107
full bound/reference       = 0.117468216
```

The independently searched BIA-off continuous capacity

```text
1.017639607e6 m/s
```

agrees essentially exactly with the existing Experiment-12/13 production value

```text
1.01764e6 m/s.
```

This is a strong cross-check that the refined audit is using the same physical capacity convention.

All active baseline blocks are dimension two:

```text
block_count_by_dim = {2: 20072}
```

and

```text
selectivity_min = 1
selectivity_max = 1
mean inverse selectivity = 1.
```

---

# 5. C-linear BIA result

With the C-linear BIA invariant enabled:

```text
mu                         = 0.1358654445 eV
n_ref                      = 1.017300651e17 cm^-3
n_active                   = 6.776778963e16 cm^-3
support fraction           = 0.666153016
eta_F                      = 0.303719522
sampled capacity           = 1.017141991e6 m/s
continuous capacity        = 1.019062337e6 m/s
tau_cap (continuous)       = 0.571456892
tau_bound (continuous)     = 0.173562614
full bound/reference       = 0.115619259
```

Every active exact fixed-k block is now one-dimensional:

```text
block_count_by_dim = {1: 40292}
```

and nevertheless

```text
selectivity_min = 1
selectivity_max = 1
mean inverse selectivity = 1
nonunit-selectivity population fraction = 0.
```

Thus the numerical calculation confirms the exact-shell lemma:

```math
\boxed{
\text{BIA-split one-dimensional active shell}
\Longrightarrow
\mathcal S_a^{act}=1.
}
```

The within-shell factor is unchanged to numerical precision even though the degeneracy structure has completely changed.

---

# 6. The BIA perturbation is not infinitesimal on the selected support

Restricting the splitting diagnostic to k points that actually contain selected cross-mu transitions in the broad optical window gives

```text
selected k range, BIA off:
0.05856 to 0.58433 nm^-1

selected k range, C-BIA on:
0.05856 to 0.59714 nm^-1
```

For C-BIA on:

```text
maximum adjacent old-doublet splitting on selected support
= 0.0108657 eV
= 10.87 meV

k-space-weighted selected-support splitting
= 0.0064322 eV
= 6.43 meV.
```

The baseline splitting is at floating-point zero (~1e-15 eV).

Therefore the persistence of `S_a=1` is not explained by an imperceptibly weak perturbation. The exact parent-shell dimensionality changes from two to one throughout the sampled active support.

---

# 7. Where the C-linear BIA effect goes

Relative C-BIA-on versus BIA-off changes in the refined continuous-capacity calculation are

```text
n_ref                    +1.1991%
n_active                 +0.9443%
support fraction         -0.2518%
eta_F                    -1.1061%
continuous capacity      +0.1398%
tau_cap                  -0.2219%
tau_bound                -1.3255%
full bound/reference     -1.5740%
mean inverse selectivity ~0 change
```

Thus the C-linear BIA correction moves the hierarchy primarily through

```text
Fermi-statistical weighting;
reference/active support redistribution;
global and shell capacity changes;
transition-window membership.
```

It does **not** produce a within-exact-shell singular-concentration penalty in this audit.

---

# 8. Main scientific conclusion

The naive expectation

```text
BIA breaks PT -> doublet singular values become unequal -> 1/S_a drops
```

is not the correct exact-shell logic.

The calculation instead realizes

```text
BIA breaks fixed-k PT degeneracy
-> exact parent shell becomes one-dimensional
-> one nonzero singular value
-> rank = stable rank = 1
-> S_a^act = 1 exactly.
```

Therefore substantial BIA spin splitting can coexist with **zero within-exact-shell selectivity penalty**.

This is a useful negative result and a structural robustness result for the Experiment-13 factorization.

---

# 9. What is and is not established

Established:

```text
1. The exact-shell decomposition predicts S_a=1 for generic active one-dimensional BIA-split shells.
2. A physically parameterized C_k-linear HgCdTe BIA perturbation realizes that shell splitting numerically.
3. Every sampled active C-BIA shell is one-dimensional and has S_a=1.
4. The continuous global capacity changes only about +0.14% in this C-linear test.
5. The full bound/reference ratio changes about -1.57% on the refined audit.
6. Selected-support same-k splitting reaches ~10.9 meV, so the result is not a vanishing-perturbation artifact.
```

Not established:

```text
1. A complete HgCdTe BIA result including quadratic B+/B- terms.
2. A universal statement excluding exceptional multidimensional crystalline or accidental degeneracies.
3. A claim that all real-device corrections from BIA are below 2%.
4. A replacement for a full zincblende eight-band validation if an editor specifically requests one.
```

---

# 10. Manuscript disposition

**Do not create Rev. 8 from this result by default.**

Rev. 7 is already correct because it restricts the PT-isotropy explanation to the BIA-neglecting validation and does not assert universal real-HgCdTe isotropy.

This new result shows that the existing caveat is conservative: breaking inversion does not automatically create a within-shell penalty under the theorem's exact-shell definition.

Adding a C-only result to the manuscript could instead invite a request for the omitted quadratic BIA terms. Keep this as a documented robustness result unless

```text
an editor/referee asks explicitly for BIA;
a full B+/B-/C implementation is completed and independently checked;
or the full calculation produces a quantitatively important change worth publishing.
```

The sole active submission manuscript remains Experiment 13 Rev. 7.

---

# 11. Next research step

The highest-value remaining extension is a **full B+/B-/C zincblende BIA audit**, but it is nonblocking.

Before coding it, reproduce the complete Appendix-B eight-band BIA matrix in the exact basis convention of the current Kane implementation and cross-check:

```text
Hermiticity;
time-reversal symmetry;
vanishing BIA energy correction at Gamma;
C-only reduction against the present validated implementation;
HgTe/CdTe endpoint interpolation conventions;
velocity derivative including all BIA terms.
```

Only then repeat the continuous-capacity and exact-shell audit.
