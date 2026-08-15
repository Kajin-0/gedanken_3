# Current State — Experiment 12: Oscillator-Strength / Thermal-State-Count Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **GLOBAL THERMAL–OPTICAL SPECTRAL-WEIGHT INEQUALITY DERIVED FOR INDEPENDENT-QUASIPARTICLE INTERBAND ABSORBERS / DISPERSIVE MULTIBAND STATE-REUSE LOOPHOLE CLOSED / DIRAC VALIDATIONS STRONG / MANY-BODY EXCITON ESCAPE IDENTIFIED / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

## Read first

1. `THERMAL_OPTICAL_SUM_INEQUALITY_STEP_2026-08-14.md`
2. `DISPERSIVE_MULTIBAND_GENERALIZATION_STEP_2026-08-14.md`
3. `OSCILLATOR_STRENGTH_STATE_COUNT_THEOREM_STEP_2026-08-14.md`
4. `FOUNDING_GEDANKEN_2026-08-14.md`
5. `PROGRESS_LOG.md`

---

# Research question

Can a direct interband charge absorber carry a fixed amount of low-energy optical spectral weight while its equilibrium thermal free-carrier population tends to zero, if the microscopic interband velocity-strength resource remains finite?

The current answer is **no** for the independent-quasiparticle class defined below.

---

# Controlling theorem — global cutoff-free form

Let exact single-particle eigenstates below the chemical potential be `v` and above it be `c`:

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

For one optical/current polarization, assume the crossing-transition velocity matrix satisfies the row/column strength bounds

```math
\sum_v|v_{cv}|^2\le v_*^2
\quad\forall c,
```

```math
\sum_c|v_{cv}|^2\le v_*^2
\quad\forall v.
```

A sufficient condition is a finite relevant velocity-operator norm `||v_i|| <= v_*`.

Exact Fermi algebra plus AM-GM gives, for every crossing transition,

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
}
```

Using Kubo-Greenwood and the row/column velocity budget gives

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

For an intrinsic neutral absorber,

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

This is the current core Experiment-12 inequality.

The thermal kernel is

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
```

It approaches `2 kBT` at low energy and falls as `E exp[-E/(2kBT)]` at high energy.

---

# Earlier flat-manifold and cutoff results are corollaries

For two exactly resonant manifolds separated by `E_gamma`, the tight result is

```math
\boxed{
N_{th}
\ge
\frac{S_{abs}}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

For partial interband spectral weight

```math
W(E_\Omega)
=\int_0^{E_\Omega/\hbar}
\sigma_1^{inter}(\omega)d\omega,
```

the global theorem implies

```math
\boxed{
n_e+n_h
\ge
\frac{2E_\Omega}{\pi e^2v_*^2}
\frac{W(E_\Omega)}
{e^{E_\Omega/(2k_BT)}-1}.
}
```

Intrinsic form is half this total excitation bound.

A useful spectroscopic corollary is

```math
\boxed{
n_{th}
\ge
\sup_{E_\Omega>0}
\left[
\frac{E_\Omega W(E_\Omega)}
{\pi e^2v_*^2[e^{E_\Omega/(2k_BT)}-1]}
\right].
}
```

---

# Low-energy implication

At fixed low-energy intrinsic interband spectral weight,

```math
K_T(E)\to2k_BT.
```

Therefore lowering the transition energy toward zero cannot make the thermal-population lower bound vanish while `v_*` and the required optical spectral weight remain fixed.

This is the dispersion-independent version of the high-velocity tradeoff that first appeared in Experiment 10.

---

# Validation

Reproducible script:

`numerics/thermal_optical_sum_dirac_validation.py`

## 2-D neutral massless Dirac / graphene

Exact:

```math
n_e
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2.
```

Experiment-12 bound:

```math
n_e^{bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2.
```

Thus

```math
\boxed{n_e^{bound}/n_e^{exact}=1/2.}
```

## 3-D massless Dirac

```math
\boxed{(n_e+n_h)_{bound}/(n_e+n_h)_{exact}=2/3.}
```

## 3-D massive Dirac at 10 um / 300 K

For

```math
\Delta/k_BT=2.39796146,
```

exact finite-T conductivity inserted into the global theorem gives

```math
\boxed{
(n_e+n_h)_{bound}/(n_e+n_h)_{exact}=0.794684.
}
```

The ratio increases toward unity as `Delta/kBT` grows:

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

This is a strong nontrivial check: the theorem recovers most of the actual finite-gap Dirac thermal population without using its DOS in the derivation.

---

# Static disorder / broadening boundary

Static disorder is allowed in principle if one uses exact single-particle eigenstates: the proof does not require Bloch momentum or translational invariance.

Do not apply the theorem naively to phenomenologically Lorentzian-broadened clean transitions and reinterpret high-energy tails as genuine low-energy transitions. Interaction-generated lifetime broadening lies outside the present independent-particle theorem class.

---

# Many-body escape — explicit boundary

Bound excitons and other neutral collective optical states can carry strong low-energy optical spectral weight while the free electron-hole continuum remains at a larger energy.

Thus Experiment 12 is **not** a theorem for all photodetectors.

Current valid class:

```math
\boxed{
\text{independent-quasiparticle direct interband charge absorbers}
}
```

or systems reducible to that description over the relevant thermal/optical window.

For a photodetector interpretation, the thermally occupied states counted by the inequality must also be electrically active enough to affect collection or carrier-number fluctuations. The theorem itself presently bounds thermal population, not dark current or D*.

---

# Novelty status

Focused audits have checked:

```text
Kubo-Greenwood finite-T conductivity;
standard/generalized optical f-sum rules;
restricted/partial optical sums;
quantum-geometric optical conductivity bounds;
finite-T QFI/susceptibility integrals;
graphene finite-T optical conductivity and sum rules;
classical infrared alpha/G_th material criteria.
```

No direct prior source has yet been identified with the Experiment-12 thermal kernel and carrier-population inequality.

This is not a priority claim.

```text
NOVELTY NOT ESTABLISHED.
```

---

# Active next action

1. Audit localized-state / electrical-activity escape routes.
2. Decide whether a detector-level noise statement can be added without assuming an arbitrary mobility or lifetime.
3. Continue dedicated novelty search around the exact global kernel.
4. Do not draft a manuscript until those tests survive.
