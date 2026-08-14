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
4. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
10. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

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
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

with equivalent-species cancellation and ideal ballistic crossing time `v^0`.

# Closed result B — microscopic velocity resource

For a lattice/Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

hence conditionally

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

At 10 um / 300 K, the scalar toy model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct threshold above `10 kBT`.

Do not treat this as a universal edge-mass rule; finite-momentum electron-hole symmetry is the actual requirement.

# Closed result E — thresholded direct-Auger rate

On the interior branch,

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If `|V_eff|^2 ~ (K-K_th)^nu`, then

```math
\boxed{\Gamma_{II}\propto(K-K_{th})^{2+\nu}.}
```

Detailed balance gives

```math
\boxed{
G_A^{vol}\propto T^{3+\nu}e^{-(E_g/2+K_{th})/(k_BT)}.
}
```

For the minimal statically screened Coulomb model at matched absorptance,

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

Weak-screening and intrinsic-Debye large-`v` asymptotics tend toward `v^-4`.

# Closed result F — external optical-boundary floor

Matching useful scene absorptance alone is insufficient. Match the complete external mode-resolved optical boundary:

```math
\boxed{\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}}
```

for all external optical channels relevant to active-carrier exchange.

For reciprocal passive structures, this fixes external thermal emission and external background absorption through modal Kirchhoff/detailed balance.

At thermal equilibrium,

```math
\boxed{\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.}
```

Internal radiative recombination is not invariant under photon recycling; use irreversible external optical traffic in the low-frequency/coarse-grained carrier-number problem.

For the ideal hemispherical step absorber at 10 um / 300 K,

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

# Closed result G — direct-Auger-to-optical admissibility ratio

Define

```math
\boxed{
\Xi_A^{ext}
=\frac{G_A^{gen}+R_A^{rec}}
{\Phi_{abs}^{ext}+\Phi_{em}^{ext}}.
}
```

At equilibrium,

```math
\boxed{\Xi_A^{ext}=G_A/\Phi_0.}
```

The direct-channel admissibility target is

```math
\boxed{\Xi_A^{ext}\le1.}
```

The radiative boundary floor carries `e^-Eg/kBT`, whereas direct Auger carries `e^{-(Eg/2+K_th)/kBT}`. Therefore

```math
\boxed{
\Xi_A^{ext}\propto_{exp}
\exp[-(K_{th}-E_g/2)/(k_BT)].
}
```

The activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

At the `K_th=10 kBT` witness, the direct-Auger/radiative exponential factor is `4.99e-4` before high-`v` algebraic suppression and unresolved interaction prefactors.

Within the positive-curvature scalar-asymmetry model,

```math
\boxed{K_{th}\ge\sqrt3\,E_g/2>E_g/2.}
```

so that controlled family is on the favorable side of activation parity, but this does not guarantee `Xi_A^ext <= 1` without prefactor control.

## Novelty discipline

Established ingredients include radiative detailed balance, spectral/angular and modal Kirchhoff reciprocity, photon recycling, radiative dark-current formulas, HgCdTe photon transport, direct-gap Auger thresholds/activation, threshold powers, Kane overlap zeros, and quasi-relativistic HgCdTe-QW Auger suppression.

Do not claim novelty for any individual ingredient.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC JOINT ADMISSIBILITY SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

## Active frontier — extra-band Auger escape

Do not rank materials and do not draft a paper yet.

The symmetric two-band protection is the most fragile remaining assumption. Real narrow-gap systems can contain heavy-hole or remote bands that enable Auger channels absent from the two-band model.

### Single next question

> Add a minimal heavy-hole-like third band to the high-`v` symmetric active pair. Under exact energy and crystal-momentum conservation, determine whether an extra-band direct Auger channel is necessarily open, conditionally open, or closable. Derive the minimum band offset/mass/velocity separation condition required to keep its threshold high enough for a radiative-floor-limited regime.

Start with kinematics. Add Coulomb matrix elements only after the support and threshold are known. Do not insert empirical Auger lifetimes.
