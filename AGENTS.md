# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Recovery order

1. `AGENTS.md`
2. `agent.md`
3. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
4. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

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

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

therefore

```math
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

with equivalent-species cancellation in the matched carrier column and ideal ballistic crossing time `v^0`.

# Closed result B — microscopic velocity resource

For a lattice/Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally

```math
\boxed{v\le V_{hop}}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

# Closed result C — symmetric direct-Auger no-go

For exact particle-hole-symmetric finite-gap massive-Dirac dispersion, normal-momentum phononless `eeh` and `hhe` Auger channels are kinematically closed.

The exact mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. Large `v` and dispersion symmetry are distinct resources.

# Closed result D — scalar asymmetry reopening

For

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

with

```math
\mathcal A_m=2|D\Delta/(\hbar^2v^2)|,
```

the weak-asymmetry threshold obeys

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct threshold above `10 kBT`.

Do not treat this as a universal edge-mass rule; finite-momentum electron-hole symmetry is the actual requirement.

# Closed result E — thresholded direct-Auger phase space and thermal factor

For a fixed hot electron on the interior reopening branch, the six-dimensional constrained final-state phase space gives

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If the squared threshold matrix element vanishes as

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{\Gamma_{II}\propto(K-K_{th})^{2+\nu}.}
```

The phase-space exponent is robust; the full-rate exponent is not universal because Kane/multiband overlap zeros can add powers.

Detailed balance gives

```math
\boxed{
G_A^{vol}
\propto
T^{3+\nu}
\exp[-(E_g/2+K_{th})/(k_BT)].
}
```

For `nu=0`, the low-T parabolic-edge limit recovers the classical direct-gap lifetime form

```math
\tau_A^{-1}\propto T^{3/2}e^{-K_{th}/k_BT}.
```

At `K_th=10kBT`, the lifetime activation is `4.54e-5` and the intrinsic equilibrium event activation is `4.13e-6`.

# Closed result F — conditional screened-Coulomb v scaling

Before Coulomb momentum dependence,

```math
G_A^{area}\propto|V_{th}|^2v^{-8}
```

at matched absorptance.

For

```math
V(Q)=\frac{e^2}{\epsilon_0\epsilon_r(Q^2+\kappa^2)}S_{cv},
\qquad
Q_{th}\propto v^{-1},
```

obtain

```math
\boxed{
G_A^{area}
\propto
\frac{|S_{cv}|^2}{\epsilon_r^2}
\frac{v^{-4}}{(\mathcal Q_{th}^2+s_\kappa^2)^2}
\left(\frac{k_BT}{\Delta}\right)^{3+\nu}
\exp[-(\Delta+K_{th})/(k_BT)].
}
```

Weak screening and the intrinsic-Debye large-`v` limit approach `v^-4`; fixed physical screening length can strengthen the suppression toward `v^-8`.

Thus the first combined direct-rate structure has

```text
large v -> algebraic suppression;
small finite-k asymmetry -> exponential threshold suppression.
```

## Novelty discipline

Established ingredients include direct-gap Auger thresholds/activation, Beattie-Landsberg thermal factors, anisotropy/warping corrections, Kane overlap zeros, quadratic/cubic impact-ionization threshold laws, and quasi-relativistic HgCdTe-QW Auger suppression.

Do not claim novelty for any individual Auger ingredient or exponent.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC JOINT ADMISSIBILITY SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

Real bulk HgCdTe is not the exact two-band toy model. Heavy-hole/remote bands, phonons, disorder, linewidth, Umklapp, and many-body effects can reopen or add channels.

## Active frontier — radiative floor versus Auger

Do not rank materials and do not draft a paper yet.

The direct Auger channel is now factored as far as useful without a complete multiband wave-function model.

Next derive the unavoidable radiative/background generation event floor for the already matched external absorptance, optical environment, and etendue. Then compare it to the thresholded Auger event rate.

Target question:

> Can one derive an admissibility inequality of the form `G_A <= G_rad + G_bg` whose radiative side is fixed by optical boundary conditions and whose nonradiative side depends explicitly on `v`, finite-momentum asymmetry, dielectric/screening resources, and matrix-element remainder terms?

This is the natural point to replace the provisional `Xi_nr` bookkeeping quantity with a derived detector-level condition.
