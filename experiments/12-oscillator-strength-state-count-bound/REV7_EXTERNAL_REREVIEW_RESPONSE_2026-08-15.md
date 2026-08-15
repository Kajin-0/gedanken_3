# Experiment 12 — Response to extreme adversarial re-review of Rev7

**Date:** 2026-08-15  
**Disposition:** **MODERATE-REVISION ITEMS ADDRESSED / FULL SECOND-ORDER HgCdTe TIGHTNESS TEST ADDED / CENTRAL THEOREM UNCHANGED / REV8 PREPARED**

## Review disposition

The Rev7 re-review again found no mathematical error invalidating the central population hierarchy. It reduced the manuscript recommendation from major revision to moderate revision / close to submission quality.

The remaining requested work was:

```text
1. formal double uniformity for a low-energy sequence of moving windows;
2. distinguish a first-order Kane upper bound from the actual selected-window capacity;
3. restrict higher-order k.p capacity claims to a bounded momentum domain of validity;
4. preferably perform a full second-order HgCdTe bound/exact comparison;
5. move the Appendix-A absorptance window above the exact mathematical edge.
```

All five are addressed in Rev8.

---

## 1. Moving-window double-uniformity — FIXED

Rev7 had the fixed-window thermodynamic assumption

```math
\limsup_{V\to\infty}v_{B,V}^{cap}<\infty.
```

The low-energy consequence, however, also moves the window `B_m` toward zero transition energy. Rev8 now states the required joint condition explicitly:

```math
\boxed{
v_*
=\sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]
<\infty.
}
```

With

```math
E_m=\sup_{\omega\in B_m}\hbar\omega\to0,
```

and

```math
W_m=\int_{B_m}\sigma_1^{cross}(\omega)d\omega\to W_0>0,
```

uniform convergence of the thermal kernel on the shrinking window gives

```math
\boxed{
\liminf_{m\to\infty}
(n_{e,B_m}^{act}+n_{h,B_m}^{act})
\ge
\frac{4k_BT}{\pi e^2v_*^2}W_0>0.
}
```

This removes the quantifier ambiguity completely.

---

## 2. First-order HgCdTe capacity language — FIXED

Rev8 no longer describes `1.31e6 m/s` as the selected HgCdTe capacity.

The first-order Kane result is stated only as

```math
v_B^{cap}\le\sqrt{3/2}\,v_K
```

and therefore as a **microscopic upper bound** that can be inserted into the denominator to obtain a conservative population lower bound.

The actual selected capacity is calculated separately in the second-order model.

---

## 3. Higher-order k.p bounded-domain qualification — FIXED

Rev8 now states explicitly that the second-order velocity operator is finite only on a selected spectral window **within a bounded momentum domain where the k.p expansion is being used**.

No claim is made that a quadratic continuum k.p Hamiltonian has a globally bounded velocity as `|k| -> infinity`.

---

## 4. Full second-order HgCdTe bound/exact comparison — COMPLETED

Controlling calculation:

`HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`

Reproducibility script:

`numerics/kane_8band_tightness.py`

Model:

```text
bulk constant-parameter limit of the second-order 8-band model of
E. G. Novik et al., Phys. Rev. B 72, 035321 (2005).
```

Representative target:

```text
T  = 300 K
Eg = 0.123984198 eV (10 um)
x  = 0.179727548 using the Laurenti Eg(x,T) convention
```

Remote parameters are linearly interpolated between the Novik HgTe/CdTe endpoint values as a representative modeling choice.

Charge-neutral result:

```text
mu - Ec = +11.477 meV
conventional electron density = 5.050214e16 cm^-3
conventional hole density     = 5.050214e16 cm^-3
cross-mu exact theorem population = 1.005141e17 cm^-3
```

The theorem population is within about `0.5%` of the conventional electron-plus-hole total in this state.

Windowed result:

| window | v_B^cap (m/s) | n_bound (cm^-3) | bound/exact |
|---|---:|---:|---:|
| Eg .. 1.5 Eg | 1.016823e6 | 3.221119e15 | 0.032046 |
| Eg .. 2 Eg | 1.017273e6 | 7.530675e15 | 0.074922 |
| Eg .. 3 Eg | 1.015473e6 | 1.115475e16 | 0.110977 |
| Eg .. 0.5 eV | 1.015611e6 | 1.186163e16 | **0.118010** |

Thus a broad low-energy validation window recovers about

```math
\boxed{11.8\%}
```

of the exact cross-mu thermal population.

This is looser than the symmetric parabolic and Dirac validations, as expected from the heavy-hole/multiband asymmetry, but it is order `10^-1` rather than numerically negligible.

The `0.5 eV` upper endpoint is a model-validation window, not a proposed detector bandwidth.

Convergence checks show the reported ratio is stable to radial/angular resolution and bounded-k-domain changes at the level needed for the manuscript.

---

## 5. Appendix-A exact-edge absorptance — FIXED

The internal absorptance illustration now uses

```math
B=[1.02\omega_g,1.10\omega_g]
```

rather than starting at the exact mathematical edge.

The recalculated intrinsic electron-column bounds are

```text
v_B^cap = 5.0e5  m/s -> 2.88e12 cm^-2
v_B^cap = 1.0e6  m/s -> 7.20e11 cm^-2
v_B^cap = 1.07e6 m/s -> 6.29e11 cm^-2
v_B^cap = 2.0e6  m/s -> 1.80e11 cm^-2
v_B^cap = 3.0e6  m/s -> 8.00e10 cm^-2
```

Using the first-order Kane **upper bound** `v_B^cap <= 1.31e6 m/s` gives the conservative illustrative lower column

```text
Sigma_e >= 4.19e11 cm^-2.
```

The illustration remains explicitly internal-absorptance / ideal entrance-coupling only.

---

## Scientific disposition after Rev8

```text
CENTRAL FINITE-VOLUME THEOREM: UNCHANGED
THERMODYNAMIC FIXED-WINDOW HYPOTHESIS: RETAINED
MOVING-WINDOW DOUBLE UNIFORMITY: FORMALIZED
FIRST-ORDER KANE CAPACITY: UPPER-BOUND LANGUAGE FIXED
SECOND-ORDER KANE CAPACITY: DIRECTLY EVALUATED ON BOUNDED DOMAIN
FULL HgCdTe-LIKE BOUND/EXACT TEST: COMPLETE
APPENDIX EDGE SPECIFICATION: FIXED
NOVELTY: NOT ESTABLISHED
```

The correct next action is another independent hostile review of Rev8. Do not add further theory by default unless that review identifies a blocking defect.