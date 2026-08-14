# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Recovery order

1. `AGENTS.md`
2. `agent.md`
3. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
4. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

Do not infer chronology from `main`; later experiments live on divergent branches.

## Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.123984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

Research question:

> What electronic structure must a passive LWIR interband absorber possess to approach HgCdTe-class room-temperature intrinsic detector quality without sacrificing useful temporal response?

---

# Closed result A — matched absorptance

For the intrinsic finite-gap massive-Dirac family,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

so

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time is `v^0`.

# Closed result B — microscopic velocity resource

A lattice/Wannier Hamiltonian gives conditionally

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

hence

```math
\boxed{v\le V_{hop}}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

No chemistry-independent numerical upper `v` has been established.

# Closed result C — exact symmetric-Dirac Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

normal-momentum phononless `eeh` and `hhe` Auger channels have empty exact kinematic support in the symmetric two-band model.

The exact mismatch is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/Eg`, `v` cancels. High `v` and particle-hole symmetry are distinct favorable resources.

# Closed result D — scalar particle-hole-asymmetry reopening

For

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

define

```math
\beta=D\Delta/(\hbar^2v^2)
```

and

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

The exact reduced-model reopening boundary is

```math
\boxed{
\beta_c(q_0)
=
\min_{0\le x\le q_0/2}
\frac{2s(x)+s(q_0-2x)-s(q_0)}
{2(q_0-x)^2},
\qquad s(q)=\sqrt{1+q^2}.
}
```

For weak asymmetry,

```math
\boxed{
\beta_c\sim4/q_{th}^3,
\qquad
q_{th}\sim(4/|\beta|)^{1/3},
}
```

and

```math
\boxed{
K_{th}\sim E_g\mathcal A_m^{-1/3}.
}
```

At the fixed 10-um / 300-K target, exact inversion gives approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to place the direct-channel threshold above `10 k_BT` in this scalar-asymmetry toy model.

Do not treat that as a universal edge-mass criterion. The actual physical requirement is small finite-momentum electron-hole dispersion asymmetry across the Auger-active window.

Reproducible calculation:

`experiments/10-room-temperature-lwir-admissibility/numerics/auger_asymmetry_threshold.py`

## Novelty discipline

Broad Dirac/symmetric-dispersion Auger suppression and enhanced Auger thresholds near quasi-relativistic HgCdTe-QW regimes are established prior art. Mandatory adjacent work includes Alymov et al. PRB 2018 and ACS Photonics 2020, Aleshkin et al. JPCM 2019, Morozov et al. ACS Photonics 2021, and classical threshold/anisotropy literature.

The cube-root asymmetry law is retained as a reduced-model derivation only; novelty is not established.

Real bulk HgCdTe is not the exact two-band model. Heavy-hole/remote bands, phonons, disorder, linewidth, and many-body effects can reopen channels.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

## Active frontier — thresholded Auger phase-space scaling

Do not rank materials and do not jump to a phenomenological Auger coefficient.

Retain the exact reopening threshold and introduce only the minimum screened-Coulomb structure necessary to determine the leading near-threshold rate/phase-space scaling.

Question:

> Can the thresholded Auger scaling be combined with `Sigma_e ~ v^-2` into a detector-level room-temperature admissibility inequality whose dominant dependence is fixed by electronic structure before model-dependent interaction prefactors enter?

Separate universal threshold exponents from model-dependent Coulomb magnitude and screening.
