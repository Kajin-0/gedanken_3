# Experiment 12 — Global Thermal–Optical Spectral-Weight Inequality

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **GLOBAL CUTOFF-FREE INEQUALITY DERIVED / FLAT-MANIFOLD AND PARTIAL-CUTOFF RESULTS BECOME COROLLARIES / DIRAC VALIDATIONS STRONG / NOVELTY NOT ESTABLISHED**

## 1. Motivation

The dispersive multiband step established a partial spectral-weight inequality below an arbitrary transition-energy cutoff `E_Omega`. The cutoff is useful experimentally but is not fundamental.

The pointwise Fermi inequality can instead be inverted transition by transition before any spectral binning. This produces a stronger cutoff-free thermal optical sum.

---

## 2. Assumptions and definitions

Consider an independent single-particle Hamiltonian at thermal equilibrium with chemical potential `mu`.

Split its exact one-particle eigenstates into

```text
lower states v: E_v < mu;
upper states c: E_c > mu.
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

and

```math
D_{cv}=f(E_v)-f(E_c)>0.
```

For one optical/current polarization `i`, define

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

Assume a finite inter-subspace velocity-strength resource `v_*` such that

```math
\sum_v|v_{cv}|^2\le v_*^2
\quad\text{for every upper state }c,
```

and

```math
\sum_c|v_{cv}|^2\le v_*^2
\quad\text{for every lower state }v.
```

A sufficient condition is a finite operator norm of the relevant physical/projected velocity operator,

```math
\|\hat v_i\|\le v_*.
```

Define thermal excitation densities relative to the zero-temperature filling:

```math
n_e=\frac1V\sum_c p_c,
\qquad
n_h=\frac1V\sum_v h_v.
```

No intrinsic-neutrality assumption is required until the final specialization.

---

## 3. Exact pointwise Fermi inequality

Write

```math
a=e^{-\beta(E_c-\mu)},
\qquad
b=e^{-\beta(\mu-E_v)},
```

so

```math
ab=e^{-\beta E_{cv}}.
```

Direct algebra gives

```math
p_c+h_v
=\frac{a+b+2ab}{(1+a)(1+b)},
```

and

```math
D_{cv}
=\frac{1-ab}{(1+a)(1+b)}.
```

At fixed transition energy, AM-GM gives

```math
a+b\ge2\sqrt{ab}.
```

Therefore

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le
p_c+h_v.
}
```

Equality holds exactly when

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
```

Thus an optically active transition with a large population difference cannot be placed arbitrarily close to the chemical potential without paying thermal upper-state or lower-state-hole occupation.

---

## 4. Sum over arbitrary dispersive multiband states

Multiply the pointwise inequality by `|v_cv|^2` and sum over all crossing transitions:

```math
2\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}
{e^{E_{cv}/(2k_BT)}-1}
\le
\sum_{cv}(p_c+h_v)|v_{cv}|^2.
```

Use the row and column velocity-strength bounds:

```math
\sum_{cv}p_c|v_{cv}|^2
\le
v_*^2\sum_cp_c,
```

```math
\sum_{cv}h_v|v_{cv}|^2
\le
v_*^2\sum_vh_v.
```

Hence

```math
\boxed{
\frac{2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}
{e^{E_{cv}/(2k_BT)}-1}
\le
v_*^2(n_e+n_h).
}
```

This step does not assume flat bands, equal degeneracies, one-to-one transitions, or frequency-bin additivity. Reusing a state in many optical transitions spends the same finite row/column velocity-strength budget.

---

## 5. Kubo-Greenwood conversion

For clean independent-particle interband absorption, the Kubo-Greenwood spectral measure obeys, for any nonnegative transition-energy weight `F(E)`,

```math
\int_0^\infty
F(\hbar\omega)\,
\sigma_1^{inter}(\omega)d\omega
=
\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
F(E_{cv}).
```

Choose

```math
F_T(E)
=\frac{E}{e^{E/(2k_BT)}-1}.
```

Then

```math
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega
=
\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}
{e^{E_{cv}/(2k_BT)}-1}.
```

Combining with the state-count inequality gives the central cutoff-free result:

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
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
\frac{1}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

This is the current controlling Experiment-12 theorem.

---

## 6. Interpretation of the thermal kernel

Define

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
```

Then

```text
E << kBT:  K_T(E) -> 2 kBT;
E >> kBT:  K_T(E) ~ E exp[-E/(2kBT)].
```

Thus low-energy interband optical spectral weight is expensive in equilibrium thermal carriers, while high-energy optical spectral weight is exponentially discounted.

The Bose-like denominator is not introduced as a bosonic occupation. It follows from optimizing two Fermi occupations on opposite sides of the chemical potential.

At fixed nonzero low-energy optical spectral weight, lowering the optical transition energy toward zero cannot drive the thermal-population lower bound to zero.

---

## 7. Partial-cutoff theorem is a corollary

`K_T(E)` is monotonically decreasing for `E>0`.

Therefore for all transitions satisfying

```math
E_{cv}\le E_\Omega,
```

```math
K_T(E_{cv})\ge K_T(E_\Omega).
```

Keeping only those positive contributions gives

```math
\boxed{
n_e+n_h
\ge
\frac{2E_\Omega}{\pi e^2v_*^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1},
}
```

where

```math
W(E_\Omega)
=\int_0^{E_\Omega/\hbar}
\sigma_1^{inter}(\omega)d\omega.
```

Thus `DISPERSIVE_MULTIBAND_GENERALIZATION_STEP_2026-08-14.md` is a weaker directly measurable corollary of the global thermal sum.

One may also optimize the cutoff corollary spectroscopically:

```math
\boxed{
n_{th}
\ge
\sup_{E_\Omega>0}
\left[
\frac{E_\Omega W(E_\Omega)}
{\pi e^2v_*^2[e^{E_\Omega/(2k_BT)}-1]}
\right]
}
```

for the intrinsic case.

---

## 8. Relation to ordinary optical sum rules

The conventional full `f`-sum constrains total conductivity spectral weight by the density of all charged particles or by kinetic-energy/band-curvature quantities.

The present inequality instead uses a **thermal kernel** and bounds the density of thermally excited upper-state electrons plus lower-state holes.

Key distinctions:

```text
ordinary f-sum:
    all-electron / ground-state spectral-weight constraint;

Experiment-12 thermal optical sum:
    low-energy interband weight is penalized according to finite-T Fermi occupation;
    the counted population is thermal particle-hole excitation density;
    a finite interband velocity-strength resource v_* is explicit.
```

The theorem should not be called a universal replacement for the f-sum rule.

---

## 9. Validation A — neutral 2-D massless Dirac cone / graphene

For neutral 2-D massless Dirac quasiparticles with velocity `v_F`, the exact finite-temperature interband sheet conductivity is

```math
\sigma_{sheet}^{inter}(\omega)
=\frac{e^2}{4\hbar}
\tanh\left(\frac{\hbar\omega}{4k_BT}\right).
```

The velocity-operator norm is

```math
v_*=v_F.
```

The exact thermal electron areal density, including fourfold spin/valley degeneracy, is

```math
n_e
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2.
```

The intrinsic Experiment-12 bound evaluates analytically using

```math
\frac{\tanh u}{e^{2u}-1}
=\frac{1}{e^{2u}+1}
```

to

```math
\boxed{
n_e^{bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2.
}
```

Therefore

```math
\boxed{
\frac{n_e^{bound}}{n_e^{exact}}=\frac12.
}
```

The inequality is nontrivial on a gapless dispersive continuum and does not rely on the flat-manifold construction.

---

## 10. Validation B — 3-D massless Dirac cone

For an isotropic 3-D massless Dirac cone with the standard interband conductivity and the same velocity norm `v`, direct evaluation gives

```math
\boxed{
\frac{(n_e+n_h)_{bound}}
{(n_e+n_h)_{exact}}
=\frac23.
}
```

Thus dimensional dispersive state reuse does not make the theorem parametrically loose.

---

## 11. Validation C — 3-D finite-gap massive Dirac at the Experiment-10 target

Use the Experiment-10 finite-gap massive-Dirac dispersion

```math
\varepsilon(k)
=\sqrt{\Delta^2+(\hbar vk)^2},
```

with

```text
T = 300 K
lambda_g = 10 um
Delta/kBT = 2.39796146.
```

The exact thermal electron density is

```math
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3
F_2(\Delta/k_BT),
```

with

```text
F_2 = 0.788762205.
```

Insert the exact finite-T massive-Dirac interband conductivity into the global thermal optical sum. Numerical quadrature gives

```math
\boxed{
\frac{(n_e+n_h)_{bound}}
{(n_e+n_h)_{exact}}
=0.794684.
}
```

Thus the generalized theorem recovers about `79.5%` of the exact thermal population at the fixed 10-um / 300-K witness without using the Dirac density of states in the derivation.

For the same model the bound/exact ratio evolves approximately as

```text
Delta/kBT       bound/exact
0                0.6667
0.5              0.6863
1.0              0.7191
2.398            0.7947
4.0              0.8454
8.0              0.9045
16.0             0.9459
```

The approach toward unity at large gap is consistent with the equality condition: thermally and optically relevant electron/hole states become increasingly concentrated near symmetric band edges around the chemical potential.

---

## 12. Static disorder and line broadening

The theorem is naturally stated for exact eigenstates of a static single-particle Hamiltonian. Static disorder does not by itself invalidate the proof: it changes the eigenstates, transition energies, and matrix elements, but the exact Kubo spectral measure remains a sum over those eigenstates and the row/column velocity budget still applies.

A phenomenological Lorentzian broadening of clean transitions should **not** be inserted into the measured spectrum and then interpreted as exact low-energy transition weight without care. Lifetime broadening generated by genuine interactions is outside the independent-particle theorem class and belongs to the many-body boundary.

Thus the global exact-eigenstate integral is preferable to a sharp experimental cutoff when disorder broadening is important.

---

## 13. Many-body boundary

The theorem does not extend automatically to neutral collective optical excitations.

A bound exciton is the canonical counterexample:

```text
its optical energy can lie below the free electron-hole continuum;
it can carry strong oscillator strength;
it is electrically neutral until a separate dissociation process creates free charge.
```

Therefore a many-body excitonic absorber can carry low-energy optical spectral weight without obeying the present lower bound on **free quasiparticle** density.

The correct theorem class is consequently

```math
\boxed{
\text{independent-quasiparticle direct interband charge absorbers}
}
```

or systems that can be reduced to such a quasiparticle description over the relevant optical and thermal energy window.

For a photodetector interpretation, the thermally occupied upper/lower states counted by the bound must also be electrically active enough to participate in collection or number fluctuations. The inequality itself is first a thermal-population versus intrinsic-optical-spectral-weight statement, not yet a universal dark-current theorem.

---

## 14. Focused novelty audit after the global theorem

Primary/adjacent literature checked includes:

```text
Kubo-Greenwood formulations of finite-temperature optical conductivity;
standard and generalized optical f-sum rules;
graphene finite-temperature optical conductivity and optical sum rules;
quantum-geometric/inverse-frequency optical sums;
finite-temperature quantum-Fisher-information response integrals;
classical infrared alpha/G_th material figures of merit.
```

The established response/QFI kernels found in this audit differ from

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
```

No direct prior source was identified in the focused search that bounds thermally excited electron/hole population by this thermally weighted interband optical conductivity together with a velocity-strength ceiling.

This remains an absence-of-collision result, not a priority claim.

```text
NOVELTY NOT ESTABLISHED.
```

---

## 15. Next hostile questions

Before any manuscript decision:

1. Audit localized-state / electrical-activity loopholes. Strong intrinsic absorption can involve states that are poor dark-current carriers.
2. Determine whether a useful detector-level statement can be made by adding a minimal collection/activity condition without collapsing back to the old `alpha/G_th` figure of merit.
3. Perform a dedicated prior-art audit centered on the exact thermal kernel and carrier-population inequality, including mathematical-response literature outside photodetectors.
4. If these survive, only then derive a concise theorem statement and manuscript outline.
