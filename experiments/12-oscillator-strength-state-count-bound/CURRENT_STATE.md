# Current State — Experiment 12: Oscillator-Strength / Thermal-State-Count Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **EXACT RESONANT TWO-MANIFOLD STATE-COUNT BOUND DERIVED / OBSERVABLE KUBO FORM DERIVED / LOW-ENERGY PLATEAU DERIVED / NOVELTY NOT ESTABLISHED / GENERALIZATION IN PROGRESS**

## Read first

1. `OSCILLATOR_STRENGTH_STATE_COUNT_THEOREM_STEP_2026-08-14.md`
2. `FOUNDING_GEDANKEN_2026-08-14.md`
3. `PROGRESS_LOG.md`

## Founding question

Can an intrinsic interband absorber carry a fixed amount of useful optical oscillator strength while its equilibrium thermal carrier population tends to zero, if the physical interband velocity operator has a finite norm?

## Minimal exact model

Two resonant manifolds:

```text
valence dimension N_v, energy E_v;
conduction dimension N_c, energy E_c;
E_gamma = E_c-E_v > 0.
```

Intrinsic neutrality:

```math
N_cp_e=N_vp_h=N_{th}.
```

For polarization `i`,

```math
M=P_c\hat v_iP_v,
\qquad
\|\hat v_i\|\le v_{max}.
```

Define absorptive interband velocity spectral weight

```math
S_{abs}
=\sum_{cv}(f_v-f_c)|v_{cv}|^2.
```

## Exact theorem

Singular-value/rank control plus exact Fermi neutrality gives

```math
\boxed{
N_{th}
\ge
\frac{S_{abs}}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

The bound is tight in the two-manifold model. Equality requires equal manifold dimensions, midpoint chemical potential, full optical rank, and every nonzero singular value equal to `v_max`.

## Kubo observable form

For the exactly resonant manifolds,

```math
W_\sigma
=\int_0^\infty\sigma_1(\omega)d\omega
=\frac{\pi e^2}{VE_\gamma}S_{abs}.
```

Therefore

```math
\boxed{
n_{th}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma}{e^{E_\gamma/(2k_BT)}-1}.
}
```

Sheet form:

```math
\boxed{
\Sigma_{th}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma^{sheet}}{e^{E_\gamma/(2k_BT)}-1}.
}
```

## Low-transition-energy result

At fixed integrated intrinsic optical spectral weight,

```math
\boxed{
\lim_{E_\gamma\to0}
n_{th,min}
=
\frac{2k_BT}{\pi e^2v_{max}^2}W_\sigma.
}
```

Thus the lower bound does not vanish as the transition energy tends to zero.

## Conditional single-pass absorptance corollary

For background index `n_b` and optical depth `tau=alpha d`,

```math
\boxed{
\Sigma_{th}
\ge
\frac{n_b\epsilon_0cE_\gamma}
{\pi e^2v_{max}^2}
\frac{\int\tau(\omega)d\omega}
{e^{E_\gamma/(2k_BT)}-1}.
}
```

If `A>=A0` over narrow bandwidth `Delta_omega`,

```math
\boxed{
\Sigma_{th}
\ge
\frac{n_b\epsilon_0cE_\gamma}
{\pi e^2v_{max}^2}
\frac{[-\ln(1-A_0)]\Delta\omega}
{e^{E_\gamma/(2k_BT)}-1}.
}
```

This is a single-pass/material-dominant corollary, not a universal photonic bound.

## 10-um / 300-K witness

For

```text
n_b = 3.5
A0 = 0.90
Delta_omega/omega0 = 0.10
```

```text
v_max (m/s)    Sigma_min (cm^-2)
5.0e5            3.96998e12
1.0e6            9.92495e11
1.07e6           8.66883e11
2.0e6            2.48124e11
3.0e6            1.10277e11
```

Reproduce with:

`numerics/state_count_bound_witness.py`

## Prior-art status

Focused searches found the adjacent established ingredients:

```text
Kubo-Greenwood optical conductivity;
optical f-sum/restricted sum rules;
quantum-metric interband conductivity;
classic alpha/G_th infrared detector material FOMs;
modern multiband/superlattice oscillator-strength + dark-current calculations.
```

No direct collision with the specific thermal-state-count / velocity-matrix-rank inequality was found in the focused screen.

```text
NOVELTY NOT ESTABLISHED.
```

## Active next action

Attempt energy-resolved generalization to dispersive bands. Determine whether optical transitions can reuse electronic states across frequency bins in a way that defeats the two-manifold rank bound.

Do not write a manuscript and do not claim a universal semiconductor bound until this escape route and many-body collective oscillator strength are audited.
