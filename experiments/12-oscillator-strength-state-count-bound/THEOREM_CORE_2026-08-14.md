# Experiment 12 — Theorem Core After Hostile Review

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **CORE MATHEMATICAL RESULT SURVIVES / WINDOWED FORM CONTROLLING / DETECTOR INTERPRETATION IS NECESSARY-CONDITION ONLY / NOVELTY NOT ESTABLISHED**

## 1. The theorem class

Consider an equilibrium **independent-quasiparticle** system with exact one-body eigenstates and chemical potential `mu`.

For detector interpretation the intended class is a direct interband charge absorber with `mu` in a gap (or at a measure-zero gap node), but the algebra only needs a split into exact states

```math
E_v<\mu<E_c.
```

For each crossing transition,

```math
E_{cv}=E_c-E_v>0,
```

```math
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
```

```math
D_{cv}=f(E_v)-f(E_c)>0.
```

Choose one physical current/velocity polarization `i` and write

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

All spin, valley, orbital, disorder, and finite-volume multiplicities are included explicitly in the state labels.

---

## 2. Cross-`mu` optical conductivity

The conductivity entering the theorem is **not arbitrary interband conductivity**.

Define

```math
\boxed{\sigma_1^{cross}(\omega)}
```

as the positive-frequency Kubo-Greenwood contribution only from transitions whose initial exact one-particle state is below `mu` and final exact state is above `mu`:

```math
\boxed{
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
}
```

For an ordinary intrinsic gapped direct-gap semiconductor near its absorption edge, this is the relevant band-to-band contribution.

Transitions entirely below `mu`, entirely above `mu`, phonon-assisted processes, and neutral many-body excitations are not included in this definition.

---

## 3. Exact pointwise Fermi lemma

For every crossing transition,

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le
p_c+h_v.
}
```

### Proof

Let

```math
a=e^{-(E_c-\mu)/(k_BT)},
\qquad
b=e^{-(\mu-E_v)/(k_BT)}.
```

Then

```math
ab=e^{-E_{cv}/(k_BT)}\equiv z,
```

and

```math
D_{cv}=\frac{1-z}{(1+a)(1+b)},
```

```math
p_c+h_v=\frac{a+b+2z}{(1+a)(1+b)}.
```

At fixed `z`,

```math
a+b\ge2\sqrt z
```

by AM-GM. Substitution gives the result.

Equality holds iff

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
```

Thus the least thermally populated realization of a transition of energy `E_cv` places its two states symmetrically about the chemical potential.

---

## 4. Arbitrary useful spectral window

Let `B` be **any measurable set of positive angular frequencies**. It may be contiguous or disjoint.

Define the selected transition graph

```math
\mathcal T_B
=\left\{
(c,v):\frac{E_{cv}}{\hbar}\in B
\right\}.
```

For each upper state define its selected row velocity strength

```math
R_c(B)
=\sum_{v:(c,v)\in\mathcal T_B}|v_{cv}|^2,
```

and for each lower state

```math
C_v(B)
=\sum_{c:(c,v)\in\mathcal T_B}|v_{cv}|^2.
```

Define the thermally weighted velocity-strength density

```math
\boxed{
\mathcal R_B(T)
=\frac1V
\left[
\sum_cp_cR_c(B)
+
\sum_vh_vC_v(B)
\right].
}
```

This quantity contains no maximum-velocity approximation.

---

# THEOREM 1 — thermal optical velocity-strength inequality

Define the thermal optical kernel

```math
\boxed{
K_T(E)
=\frac{E}{e^{E/(2k_BT)}-1}.
}
```

Then for every spectral window `B`,

```math
\boxed{
\mathcal R_B(T)
\ge
\frac{2}{\pi e^2}
\int_B
K_T(\hbar\omega)
\sigma_1^{cross}(\omega)
\,d\omega.
}
```

### Proof

Multiply the pointwise Fermi lemma by `|v_cv|^2` and sum only over `T_B`:

```math
2\sum_{(c,v)\in\mathcal T_B}
\frac{D_{cv}|v_{cv}|^2}
{e^{E_{cv}/(2k_BT)}-1}
\le
\sum_cp_cR_c(B)
+
\sum_vh_vC_v(B).
```

The Kubo formula converts the left side directly into the stated optical integral.

No flat bands, Bloch momentum, equal degeneracies, one-to-one optical transitions, or frequency-bin state counting are required.

This is the most assumption-light surviving Experiment-12 result.

---

## 5. Windowed microscopic velocity resource

Define

```math
\boxed{
v_{*,B}^2
=\max\left[
\sup_cR_c(B),
\sup_vC_v(B)
\right].
}
```

Then

```math
\mathcal R_B(T)
\le
v_{*,B}^2
\left(n_e+n_h\right),
```

where

```math
n_e=\frac1V\sum_cp_c,
\qquad
n_h=\frac1V\sum_vh_v.
```

Combining with Theorem 1 gives the carrier-population result.

---

# THEOREM 2 — windowed thermal carrier-population bound

For any positive-frequency window `B`,

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

For an intrinsic charge-neutral absorber,

```math
n_e=n_h\equiv n_{th},
```

so

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

This is the preferred detector-material form.

A global all-frequency formula is a special case **only if** the corresponding global row/column velocity resource is finite. The windowed theorem is the controlling statement because it remains meaningful for continuum systems with unbounded high-energy velocity.

---

## 6. Microscopic meaning of `v_{*,B}`

The resource is not an arbitrary fitting parameter.

Completeness gives

```math
R_c(B)
\le
\langle c|\hat v_i^2|c\rangle,
```

```math
C_v(B)
\le
\langle v|\hat v_i^2|v\rangle.
```

Thus one may upper-bound `v_{*,B}` by the largest relevant one-body velocity second moment.

In an orthonormal bounded Wannier/tight-binding representation,

```math
\boxed{
v_{*,B}
\le
V_i^{hop}
=\frac1\hbar\sum_R|R_i|\|H_R\|.
}
```

There is no claim of a universal chemistry-independent numerical `v_*`.

---

## 7. Low-energy consequence

For

```math
E\ll k_BT,
```

```math
K_T(E)=2k_BT-E/2+O(E^2/k_BT).
```

Therefore, for a useful spectral window whose transition energies are all driven toward zero while its integrated cross-`mu` conductivity and `v_{*,B}` remain finite,

```math
\boxed{
n_e+n_h
\gtrsim
\frac{4k_BT}{\pi e^2v_{*,B}^2}
\int_B\sigma_1^{cross}(\omega)d\omega.
}
```

Intrinsic form:

```math
\boxed{
n_{th}
\gtrsim
\frac{2k_BT}{\pi e^2v_{*,B}^2}
\int_B\sigma_1^{cross}(\omega)d\omega.
}
```

Thus lowering the useful direct-interband transition energy alone cannot make the thermal quasiparticle population vanish at fixed optical spectral weight and fixed microscopic velocity-strength resource.

---

## 8. Partial-cutoff corollary

For a contiguous window

```math
B=(0,E_\Omega/\hbar],
```

`K_T(E)` decreases monotonically with `E`, so

```math
\boxed{
n_e+n_h
\ge
\frac{2E_\Omega}{\pi e^2v_{*,B}^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1},
}
```

where

```math
W(E_\Omega)
=\int_0^{E_\Omega/\hbar}\sigma_1^{cross}(\omega)d\omega.
```

This is weaker than the kernel-integrated window theorem but easier to evaluate from cumulative spectral weight.

---

## 9. Equality structure

The population bound is tight only if all relevant inequalities saturate simultaneously.

Required conditions include:

```text
1. Every optically weighted transition is symmetric about mu.
2. Every thermally occupied selected upper/lower state saturates the same row/column ceiling v_{*,B}^2.
3. Those states spend no velocity strength outside the selected optical graph if the common ceiling is to be saturated.
4. No extra thermally occupied states exist outside the selected graph.
```

The original equal-dimensional flat two-manifold model is an exact equality construction.

---

## 10. Nontrivial validation

The generalized inequality has been checked against exact finite-temperature Dirac responses.

```text
2-D neutral massless Dirac / graphene:
    population bound / exact = 1/2

3-D massless Dirac:
    population bound / exact = 2/3

3-D massive Dirac at the Experiment-10 target
Delta/kBT = 2.39796146:
    population bound / exact = 0.794684
```

For the finite-gap 3-D Dirac family the ratio approaches unity as `Delta/kBT` increases.

Reproducible calculation:

`numerics/thermal_optical_sum_dirac_validation.py`

---

## 11. Corrected 10-um / 300-K single-pass illustration

This is an **illustration**, not the theorem.

Take:

```text
T = 300 K
10-um absorption edge
background index n_b = 3.5
single-pass absorptance A >= 0.90
useful angular-frequency interval B = [omega_g, 1.1 omega_g]
```

With weak-loss

```math
\alpha\simeq\sigma_1^{cross}/(n_b\epsilon_0c)
```

and optical depth `tau=alpha d`, `A>=0.90` requires

```math
\tau\ge -\ln(0.1).
```

Using the exact thermal-kernel integral over the window gives approximate minimum intrinsic electron columns

```text
v_{*,B} (m/s)      Sigma_e,min (cm^-2)
5.0e5                 3.6598e12
1.0e6                 9.1495e11
1.07e6                7.9915e11
2.0e6                 2.2874e11
3.0e6                 1.0166e11
```

The previous constant-kernel 10%-band approximation was high by `7.81%` for this above-edge interval and is superseded.

Reproduce with:

`numerics/state_count_bound_witness.py`

External resonant/path-enhanced photonic structures require separate optical resources and are not bounded by this single-pass illustration.

---

## 12. Scope and counterexamples

The theorem survives arbitrary dispersive multiband state reuse and static single-particle disorder when exact eigenstates and the physical current operator are used.

It does **not** automatically cover:

```text
bound excitons or neutral collective optical excitations;
phonon-assisted / indirect absorption;
interaction-generated many-body spectral broadening;
optical weight that does not correspond to cross-mu charge-state transitions;
arbitrary external photonic enhancement when translating material conductivity to absorptance.
```

A bound exciton is an explicit free-carrier escape: neutral low-energy oscillator strength can lie below the free pair continuum and photocurrent requires a separate dissociation step.

Localized one-particle states do not break the population theorem, but they do break any automatic inference from population to dc dark current.

---

## 13. What the theorem does NOT claim

Do not claim:

```text
universal dark-current lower bound;
universal D* limit;
universal thermal generation-rate lower bound;
universal finite-bandwidth noise floor;
universal numerical maximum electronic velocity;
validity for every photodetector architecture.
```

A proposed universal conversion

```math
G_{th}\ge n_{th}/\tau_{response}
```

has already been rejected by the depleted-photodiode counterexample.

---

## 14. Novelty status

Focused audit finds strong adjacency to:

```text
semiconductor phase-space filling / Pauli blocking;
Kubo-Greenwood conductivity;
standard and generalized f-sum rules;
graphene interband/Drude spectral-weight transfer;
quantum-geometric optical sum rules;
classic infrared alpha/G_th material figures of merit.
```

No direct source has yet been found that states the windowed inverse inequality

```text
cross-mu optical spectral weight
+ finite per-state velocity-strength budget
-> minimum equilibrium thermal electron-hole excitation population.
```

The mathematics is compact enough that priority risk remains high.

```text
NOVELTY NOT ESTABLISHED.
NO MANUSCRIPT CLAIM YET.
```

The next decision should be based on whether this corrected theorem remains scientifically substantial after a final focused literature audit and an independent proof check.
