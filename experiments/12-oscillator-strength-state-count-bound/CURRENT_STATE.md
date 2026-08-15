# Current State — Experiment 12: Oscillator-Strength / Thermal-State-Count Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **WINDOWED CROSS-mu THERMAL–OPTICAL INEQUALITY SURVIVED HOSTILE REVIEW / DISPERSIVE MULTIBAND STATE REUSE CLOSED / DIRAC VALIDATIONS STRONG / MANY-BODY AND DARK-CURRENT SCOPE LIMITS EXPLICIT / DIRECT PRIOR-ART COLLISION NOT FOUND / MANUSCRIPT VIABILITY UNDER REVIEW**

## Read first

1. `THEOREM_CORE_2026-08-14.md`
2. `HOSTILE_THEOREM_REVIEW_2026-08-14.md`
3. `NOVELTY_AUDIT_2026-08-14.md`
4. `NOVELTY_AUDIT_ADDENDUM_LOW_CARRIER_OPTICS_2026-08-14.md`
5. `THERMAL_OPTICAL_SUM_INEQUALITY_STEP_2026-08-14.md` — historical derivation; some legacy `inter` notation is superseded by `cross`
6. `THERMAL_OCCUPATION_FLUCTUATION_COROLLARY_STEP_2026-08-14.md`
7. `MICROSCOPIC_VELOCITY_RESOURCE_COROLLARY_2026-08-14.md`
8. `FAILED_RESPONSE_TIME_TO_GENERATION_BOUND_2026-08-14.md`
9. `PROGRESS_LOG.md`

---

# Research question

For an equilibrium independent-quasiparticle **direct charge absorber**, can a material retain fixed low-energy optical spectral weight while the thermal upper-state electron / lower-state hole population tends to zero, if the available optical velocity strength per participating state remains finite?

The current answer is **no**, in the precise resource-conditioned sense below.

---

# Controlling notation

Use exact one-particle states split by the chemical potential:

```math
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0.
```

Define

```math
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
\qquad
D_{cv}=f(E_v)-f(E_c).
```

Use

```math
\boxed{\sigma_1^{cross}(\omega)}
```

for the positive-frequency conductivity contributed only by **direct one-particle transitions from below `mu` to above `mu`**.

Do not use generic `sigma_inter` in theorem claims; finite-temperature same-side transitions are outside the strong half-gap proof.

---

# Pointwise Fermi lemma

For every crossing transition,

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
}
```

Equality occurs only for a transition symmetric about `mu`.

---

# Controlling theorem hierarchy — arbitrary spectral window

Let `B` be any measurable set of positive angular frequencies. Define selected row/column velocity strengths

```math
R_c(B)=\sum_{v:(c,v)\in B}|v_{cv}|^2,
```

```math
C_v(B)=\sum_{c:(c,v)\in B}|v_{cv}|^2.
```

Define the thermally weighted velocity-strength density

```math
\boxed{
\mathcal R_B
=V^{-1}\left[
\sum_cp_cR_c(B)+\sum_vh_vC_v(B)
\right].
}
```

Then the exact first inequality is

```math
\boxed{
\mathcal R_B
\ge
\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

This statement contains no global maximum-velocity assumption.

Now define the selected per-state velocity-strength resource

```math
\boxed{
v_{*,B}^2
=\max[\sup_cR_c(B),\sup_vC_v(B)].
}
```

Since

```math
\mathcal R_B\le v_{*,B}^2(n_e+n_h),
```

obtain

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

For an intrinsic neutral absorber,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

This **windowed form** is controlling. The older all-frequency formula is a corollary only when a finite global row/column resource exists.

---

# Microscopic resource

`v_{*,B}` is not a universal speed or a fit parameter.

Completeness gives

```math
R_c(B)\le\langle c|\hat v_i^2|c\rangle,
```

```math
C_v(B)\le\langle v|\hat v_i^2|v\rangle.
```

In a bounded orthonormal Wannier/tight-binding representation,

```math
v_{*,B}\le
V_i^{hop}
=\hbar^{-1}\sum_R|R_i|\|H_R\|.
```

No universal numerical `v_*` is claimed.

---

# Low-energy implication

The thermal kernel

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}
```

satisfies

```math
K_T(E)\to2k_BT
```

as `E->0`.

Therefore fixed low-energy cross-`mu` optical spectral weight cannot coexist with vanishing thermal quasiparticle population at fixed `v_{*,B}` merely by lowering the transition energy.

---

# Validation

Reproduce with:

`numerics/thermal_optical_sum_dirac_validation.py`

```text
2-D neutral massless Dirac / graphene: bound/exact = 1/2
3-D massless Dirac:                    bound/exact = 2/3
3-D massive Dirac at 10 um / 300 K:    bound/exact = 0.794684
```

For the finite-gap 3-D Dirac family the ratio approaches unity as `Delta/kBT` increases.

Random finite-dimensional stress test:

`numerics/random_matrix_theorem_stress_test.py`

The script checks arbitrary asymmetric spectra, dense complex transition matrices, and random spectral windows against both the strong cross-`mu` theorem and the weaker all-transition fallback.

---

# Corrected 10-um single-pass illustration

The old constant-kernel 10%-band witness is superseded.

For

```text
T = 300 K
10-um edge
n_b = 3.5
A >= 0.90
B = [omega_g, 1.1 omega_g]
```

exact kernel integration gives

```text
v_{*,B} (m/s)      Sigma_e,min (cm^-2)
5.0e5                 3.6598e12
1.0e6                 9.1495e11
1.07e6                7.9915e11
2.0e6                 2.2874e11
3.0e6                 1.0166e11
```

This remains only a material-dominant single-pass illustration. Arbitrary photonic path enhancement introduces separate resources.

Reproduce with:

`numerics/state_count_bound_witness.py`

---

# Supporting corollaries / negative results

## Occupation variance

For independent grand-canonical Fermi occupations,

```math
\mathcal V_{1b}
\ge
\frac{1}{\pi e^2v_*^2}
\int
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{\sinh[\hbar\omega/(2k_BT)]}d\omega.
```

This is **not** a universal finite-bandwidth detector-noise bound.

## All-transition fallback

If cross-`mu` optical weight cannot be decomposed, a weaker all-transition theorem exists with kernel

```math
E/[e^{E/(k_BT)}-1].
```

See `ALL_TRANSITION_FALLBACK_COROLLARY_2026-08-14.md`.

## Failed generation-rate shortcut

Do not claim

```math
G_{th}\ge n_{th}/\tau_{response}
```

for arbitrary detectors. Depleted photovoltaic collection is a counterexample.

---

# Scope boundary

Current valid theorem class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

The mathematical population theorem survives arbitrary dispersive multiband state reuse and static one-body disorder when exact eigenstates and the physical current operator are used.

It does not automatically cover:

```text
bound excitons / neutral collective optical excitations;
phonon-assisted / indirect absorption;
interaction-generated many-body spectral broadening;
external absorptance produced mainly by unconstrained passive photonic enhancement.
```

Localized one-particle states do not break the population inequality but can decouple population from dc dark current.

Therefore Experiment 12 is currently a **necessary material-state-count condition**, not a universal dark-current, D*, or noise theorem.

---

# Novelty status

Focused audit has found strong adjacency to:

```text
semiconductor phase-space filling / Pauli blocking;
Kubo-Greenwood;
ordinary/generalized f-sum rules;
graphene interband/Drude spectral-weight transfer;
quantum-geometric optical sums;
classic infrared alpha/G_th criteria;
Yablonovitch-Kane / Adams low-carrier-density band engineering for semiconductor lasers.
```

No direct source has yet been identified with the corrected windowed inverse inequality.

```text
DIRECT COLLISION: NOT FOUND IN FOCUSED AUDIT.
CONCEPTUAL ADJACENCY: HIGH.
MATHEMATICAL NOVELTY: MODEST.
PHYSICAL / DETECTOR-SPECIFIC NOVELTY: PLAUSIBLE, UNPROVEN.
```

---

# Active next action

Perform the manuscript-viability decision on the **corrected theorem only**.

Question:

> After all scope limits are stated, is the inverse cross-mu optical-spectral-weight / thermal-population inequality sufficiently general, nontrivial, and distinct from phase-space filling and optical sum rules to justify a short theoretical manuscript?

Do not broaden the claim to dark current to make it look stronger.
