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
4. `experiments/10-room-temperature-lwir-admissibility/THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
10. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
11. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

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
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

for the finite-gap massive-Dirac family at matched ideal absorptance. Equivalent-species degeneracy cancels from the carrier column; ideal ballistic crossing time is `v^0`.

# Closed result B — microscopic velocity resource

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

hence conditionally `v<=V_hop` and `Sigma_e>=C/V_hop^2`.

# Closed result C — symmetric two-band direct-Auger no-go

Exact particle-hole-symmetric finite-gap massive-Dirac dispersion closes normal-momentum phononless `eeh` and `hhe` channels.

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels.

# Closed result D — scalar asymmetry reopening

For `E_±=Dk^2±sqrt(Delta^2+(hbar v k)^2)`, weak asymmetry gives

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar toy model requires approximately `A_m<=0.0848` to put the direct threshold above `10 kBT`.

# Closed result E — thresholded two-band rate

Pure interior-threshold phase space:

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If `|V_eff|^2~(K-K_th)^nu`, then `Gamma_II~(K-K_th)^(2+nu)`.

Detailed balance:

```math
G_A^{vol}\propto T^{3+\nu}e^{-(E_g/2+K_{th})/(k_BT)}.
```

Minimal screened-Coulomb matched-area large-`v` scaling tends toward `v^-4` in weak screening/intrinsic-Debye asymptotics.

# Closed result F — external optical boundary

Match the complete external mode-resolved absorptance, not useful front-side absorptance alone. At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant under photon recycling.

Define

```math
\boxed{
\Xi_A^{ext}
=\frac{G_A^{gen}+R_A^{rec}}
{\Phi_{abs}^{ext}+\Phi_{em}^{ext}}.
}
```

At equilibrium `Xi_A^ext=G_A/Phi_0`. The direct-Auger/radiative activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

For the ideal 10-um / 300-K hemispherical step absorber,

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

---

# Closed result G — minimal heavy-hole third-band escape

Controlling file: `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`.

Add

```math
E_{hh}(k)=\Delta+\delta_{hh}+\frac{\hbar^2k^2}{2M_{hh}}.
```

Define

```math
\rho=M_{hh}v^2/\Delta=M_{hh}/m_D,
\qquad
\eta=\delta_{hh}/\Delta.
```

For inverse CCCH `e_0 -> e_1 + e_2 + h_hh`, the exact fixed-total-momentum final-energy minimum is collinear with equal final-electron momenta.

The mismatch is strictly decreasing with total momentum and has

```math
\boxed{D(\infty)=1+\eta-\rho/2.}
```

Therefore

```math
\boxed{
M_{hh}v^2<2(\Delta+\delta_{hh})
\Rightarrow\text{CCCH closed},
}
```

```math
\boxed{
M_{hh}v^2=2(\Delta+\delta_{hh})
\Rightarrow\text{asymptotically marginal},
}
```

```math
\boxed{
M_{hh}v^2>2(\Delta+\delta_{hh})
\Rightarrow\text{one unique finite threshold}.
}
```

This is the first direct conflict found with the high-`v` thermodynamic lever:

```text
Sigma_e ~ v^-2 favors large v;
rho ~ v^2 at fixed spectator band pushes CCCH toward reopening.
```

Exact closure requires

```math
\boxed{
v\le\sqrt{2(\Delta+\delta_{hh})/M_{hh}}.}
```

For a touching spectator band at 10 um,

```math
M_{hh}^{max}=E_g/v^2.
```

At `v=1e6 m/s`, `M_hh^max=0.02181 m0`; at `1.07e6 m/s`, `0.01905 m0`.

Near the boundary `rho_c=2(1+eta)`,

```math
\boxed{K_{th}^{hh}/\Delta\sim3/(\rho-\rho_c).}
```

For a very heavy spectator band,

```math
\boxed{K_{th}^{hh}\to E_g+\delta_{hh}.}
```

For a flat touching band, `K_th^hh -> Eg`.

Rigorous lower bound:

```math
\boxed{K_{th}^{hh}\ge E_g+\delta_{hh}.}
```

Thus for `delta_hh>=0` the open heavy-hole channel remains on the favorable side of radiative activation parity, but in the flat touching limit the exponent-only direct-Auger/radiative factor is only

```math
\boxed{e^{-E_g/(2k_BT)}=0.0909}
```

at 10 um / 300 K. A heavy spectator band therefore erases most of the stronger symmetry-derived exponential margin even though it does not reverse activation parity.

Broad heavy-hole CCCH/Auger-1 physics and flat-heavy-hole Kane structure are established prior art. Novelty of the compact closure theorem or combined framework is not established.

## Novelty discipline

Established ingredients include radiative detailed balance, modal Kirchhoff reciprocity, photon recycling, direct-gap Auger thresholds/activation, heavy-hole CCCH/Auger-1 in HgCdTe, flat heavy-hole Kane bands, threshold powers, Kane overlap zeros, and quasi-relativistic HgCdTe-QW Auger suppression.

Do not claim novelty for any individual ingredient.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC JOINT ADMISSIBILITY SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

## Active frontier — open heavy-hole rate

Do not rank materials and do not draft a paper yet.

The minimal third-band support problem is closed.

### Single next question

> Once `M_hh v^2 > 2(Delta+delta_hh)`, derive the near-threshold CCCH phase-space exponent and the algebraic dependence of the matched-area event rate on `v`, `M_hh`, and offset while keeping the heavy-hole spinor/Coulomb/exchange overlap explicit. Can an explicit regime still satisfy `Xi_hh^ext <= 1`, or does the spectator-band DOS destroy the room-temperature admissibility region?

Do not insert empirical Auger-1 lifetimes before deriving this scaling.
