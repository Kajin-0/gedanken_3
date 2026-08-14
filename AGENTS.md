# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch the live target and exact blob SHA. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Recovery order

1. `AGENTS.md`
2. `agent.md`
3. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
4. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`
8. founding/history files as needed.

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

The continuum low-energy constraints tested do not give a universal upper `v`. A lattice/Wannier Hamiltonian gives conditionally

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

# Closed result C — exact ideal Auger kinematic no-go

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

strict subadditivity implies

```math
\varepsilon(\mathbf p+\mathbf q)
<\varepsilon(\mathbf p)+\varepsilon(\mathbf q).
```

Therefore the normal-momentum phononless `eeh` impact-ionization/Auger channel and its `hhe` mirror cannot satisfy exact energy and momentum conservation in the particle-hole-symmetric two-band model.

The exact minimum mismatch at hot quasiparticle energy `E` is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/E_g`, `v` cancels.

Interpretation:

```text
large v -> lower matched-absorptance thermal population;
particle-hole-symmetric relativistic dispersion -> ideal Auger closure.
```

These are distinct design resources.

The massless limit is only marginal/collinear rather than strictly closed.

## Novelty discipline

Broad Dirac/symmetric-dispersion Auger suppression is established prior art. Mandatory comparators include Alymov et al. PRB 97, 205411 (2018), Alymov et al. ACS Photonics 7, 98–104 (2020), But et al. Nature Photonics 13, 783–787 (2019), and Combescot & Combescot PRB 37, 8781 (1988).

Real bulk HgCdTe is not the exact symmetric two-band model. Do not claim zero bulk-HgCdTe Auger recombination.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

## Active frontier — symmetry-breaking reopening

Do not calculate an empirical Auger rate yet.

Add the smallest controlled particle-hole asymmetry, preferably

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

and derive the exact boundary at which Auger kinematic support first reopens over the finite thermally relevant energy window.

The objective is a dimensionless admissibility condition on asymmetry relative to `E_g`, `v`, and the hot-carrier energy window.

Only after that boundary is known should Coulomb matrix elements and finite rates be introduced.
