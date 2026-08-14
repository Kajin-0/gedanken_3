# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

Experiment 10 is analytical/theoretical only. Preserve negative/corrected/conditional paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE FRONTIER — Experiment 10

Branch:

```text
experiment-10-room-temperature-lwir-admissibility
```

No manuscript is justified yet.

## Read in this order

1. `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`
2. `experiments/10-room-temperature-lwir-admissibility/THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

Fixed target:

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g=0.1239841984\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.796.
```

---

# Controlling closed results

## Matched absorptance

```math
\boxed{\Sigma_e=n_ed\propto v^{-2}}
```

for the finite-gap massive-Dirac family at matched ideal absorptance, with equivalent-species cancellation and ideal ballistic crossing time `v^0`.

## Microscopic velocity resource

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally `v<=V_hop` and `Sigma_e>=C/V_hop^2`.

## Two-band direct-Auger protection

Exact particle-hole-symmetric massive-Dirac dispersion closes normal-momentum phononless `eeh`/`hhe` channels. Exact mismatch:

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

## Scalar asymmetry reopening

For `E_±=Dk^2±sqrt(Delta^2+(hbar v k)^2)`, weak asymmetry gives

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, `A_m <= ~0.0848` places the toy-model direct threshold above `10 kBT`.

## Thresholded two-band rate

```math
\Phi_{3body}\propto(K-K_{th})^2
```

for pure interior-threshold phase space, while matrix-element zeros can add powers. Detailed balance gives

```math
G_A^{vol}\propto T^{3+\nu}e^{-(E_g/2+K_{th})/(k_BT)}.
```

Minimal screened Coulomb at matched absorptance tends toward `G_A^area ~ v^-4` in the weak-screening/intrinsic-Debye large-`v` limit.

## External optical floor

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

At equilibrium, `Xi_A^ext=G_A/Phi_0`. The activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

For the ideal 10-um / 300-K hemispherical step absorber,

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

---

# NEW closed result — heavy-hole third-band escape

Model spectator hole branch

```math
E_{hh}(k)=\Delta+\delta_{hh}+\frac{\hbar^2k^2}{2M_{hh}}.
```

Define

```math
\boxed{
\rho=\frac{M_{hh}v^2}{\Delta}=\frac{M_{hh}}{m_D},
\qquad
\eta=\frac{\delta_{hh}}{\Delta}.
}
```

For inverse CCCH

```text
e_0 -> e_1 + e_2 + h_hh,
```

the exact fixed-total-momentum final-energy minimum is collinear with equal final-electron momenta. Parameterized by common dimensionless group velocity `u`,

```math
x=\frac{u}{\sqrt{1-u^2}},
\qquad
z=\rho u,
```

```math
q=\frac{2u}{\sqrt{1-u^2}}+\rho u,
```

```math
\mathcal F
=\frac{2}{\sqrt{1-u^2}}+1+\eta+\frac{\rho u^2}{2}.
```

For mismatch `D(q)=F(q)-sqrt(1+q^2)`, derive

```math
\boxed{D'(q)<0}
```

and

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

This is the first direct conflict with the high-`v` thermodynamic lever because `rho~v^2` while `Sigma_e~v^-2`.

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

Near the opening boundary `rho_c=2(1+eta)`,

```math
\boxed{
K_{th}^{hh}/\Delta\sim3/(\rho-\rho_c).
}
```

For a very heavy band,

```math
\boxed{K_{th}^{hh}\to E_g+\delta_{hh}.}
```

For a flat touching band, `K_th^hh -> Eg`.

Rigorous lower bound:

```math
\boxed{K_{th}^{hh}\ge E_g+\delta_{hh}.}
```

Thus for `delta_hh>=0` the open heavy-hole channel remains on the favorable side of radiative activation parity, but in the flat touching limit the exponent-only Auger/radiative advantage degrades to

```math
\boxed{e^{-E_g/(2k_BT)}=0.0909}
```

at 10 um / 300 K.

Broad heavy-hole CCCH/Auger-1 physics is established prior art. Novelty of the compact closure theorem or joint framework is not established.

---

# DO NOT DO

Do not claim two-band Auger closure for bulk HgCdTe. Do not rank compounds. Do not insert empirical Auger-1 lifetime coefficients. Do not draft a manuscript yet.

# NEXT ACTION

The third-band support problem is closed. Derive the **near-threshold open-heavy-hole CCCH phase-space and algebraic `v`/`M_hh` scaling**, keeping the heavy-hole spinor/Coulomb/exchange overlap explicit.

Question:

> Once `M_hh v^2 > 2(Delta+delta_hh)`, can the large spectator-band DOS still be made sub-radiative (`Xi_hh^ext <= 1`) by threshold, offset, velocity, and explicit overlap resources, or does the heavy-hole prefactor destroy the proposed room-temperature admissibility region?
