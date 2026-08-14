# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch the live target and exact blob SHA. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not merely more branches or calculations.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Recovery order

1. `AGENTS.md`
2. `agent.md`
3. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
4. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`
7. founding/history files as needed.
8. Experiment-08 novelty stop before zero/small-gap Kane limits.

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

The target is a finite-gap band-structure admissibility theorem/bound, not a material ranking or scalar FOM.

---

# Closed result A — matched massive-Dirac absorptance

For the intrinsic 3-D massive-Dirac model,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1}.
```

Matched ideal single-pass absorptance requires

```math
d\propto v/N_D,
```

therefore

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time is

```math
\boxed{\tau_{ball}\propto v^0.}
```

At the actual 10-um / 300-K target, exact finite-gap Dirac carrier density is `1.8644x` the edge-parabolic estimate. Do not use the simple parabolic density expression for quantitative closure.

---

# Closed result B — Kane velocity freedom and microscopic resource

Using

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

```math
\boxed{\Sigma_e\propto E_P^{-1}.}
```

The following do **not** furnish a useful material-independent upper bound on large `v`:

```text
multiband effective-mass identity;
global optical f-sum over a fixed detector-relevant energy interval;
low-energy Kramers-Kronig dielectric loading;
fixed remote-band separation in energy.
```

The key negative result from the optical sum is

```math
\int_{\omega_1}^{\omega_2}\sigma_1(\omega)d\omega\propto v^{-1}
```

for fixed photon-energy endpoints: increasing `v` consumes less low-energy spectral weight.

For a microscopic lattice/Wannier Hamiltonian

```math
H(\mathbf k)=\sum_RH_Re^{i\mathbf k\cdot R},
```

the velocity operator satisfies

```math
\boxed{
\|\hat v_i\|
\le
\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop}.
}
```

Therefore, conditionally on this ultraviolet hopping-range resource,

```math
\boxed{v\le V_{hop}.}
```

Combining with matched absorptance gives the first explicit resource-conditioned detector inequality

```math
\boxed{
\Sigma_e\ge C(T,E_g,A,r,n_b)/V_{hop}^2.
}
```

No chemistry-independent numerical upper bound on `v` has been established.

---

# Novelty discipline

Established ingredients include Kane `k.p`, `E_P`, HgCdTe Kane velocity, effective-mass sums, optical f-sum rules, 3-D Dirac optical conductivity, Wannier/tight-binding Hamiltonians, `alpha/G_th`, `alpha sqrt(tau)`, generic Auger engineering, and Experiment-08 zero-gap statistics.

Do not claim novelty for the operator-norm velocity inequality itself.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

## Active frontier — Auger kinematics

The high-`v` lever has survived the obvious absorption/DOS, ballistic-time, effective-mass, optical-sum, and remote-band-energy cancellation attacks.

The next unavoidable intrinsic mechanism is Auger recombination/generation.

### Single next question

> For the same finite-gap massive-Dirac/Kane family, what Auger channels are kinematically allowed under exact energy and crystal-momentum conservation, how do their thresholds/phase space scale with `v`, `E_g`, and minimal asymmetry/remote-band parameters, and does the matched-absorptance `Sigma_e ~ v^-2` advantage survive?

### Method constraint

Do **not** begin with an empirical Auger coefficient `C_A` or lifetime. Start with exact kinematics for the simplest Coulomb process. Add matrix elements/rates only after the allowed phase space is understood.

Do not rank candidate compounds or draft a paper yet.
