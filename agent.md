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
2. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

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

# CONTROLLING RESULTS

## 1. Matched absorptance

For the exact finite-gap massive-Dirac family,

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

## 2. Microscopic velocity resource

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

## 3. Symmetric two-band direct-Auger protection

For exact particle-hole-symmetric finite-gap massive-Dirac dispersion, normal-momentum phononless `eeh` and `hhe` Auger channels are kinematically closed.

The exact mismatch is

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. High `v` and electron-hole symmetry are distinct resources.

## 4. Scalar asymmetry reopening

For

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

with

```math
\mathcal A_m=2|D\Delta/(\hbar^2v^2)|,
```

the weak-asymmetry law is

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar toy model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct threshold above `10 kBT`.

Do not interpret this as a universal edge-mass rule; finite-momentum dispersion symmetry is the actual requirement.

## 5. Thresholded direct-Auger rate

The interior-threshold kinematic phase space gives

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

Weak-screening/intrinsic-Debye large-`v` behavior tends toward `v^-4`.

## 6. Complete external optical boundary — CLOSED

Matching useful scene absorptance alone is insufficient. The theorem-grade comparison must match the complete mode-resolved external optical boundary:

```math
\boxed{
\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}
}
```

for every external optical channel relevant to active-carrier exchange.

Then modal Kirchhoff reciprocity fixes

```math
\Phi_{em}^{ext}(T_d)
=\int d\mu\,\mathcal A_\mu n_B(\omega_\mu,T_d)\Gamma_\mu,
```

and the external background absorption is fixed by the same `A_mu` and environment.

At thermal equilibrium,

```math
\boxed{\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.}
```

Internal radiative recombination is **not** the invariant denominator because photon recycling allows

```math
\Phi_{em}^{ext}=p_{esc}R_{rad}^{int}.
```

Use external irreversible optical traffic in the low-frequency/coarse-grained carrier-number problem.

## 7. Derived admissibility ratio

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

The direct-channel admissibility criterion is

```math
\boxed{\Xi_A^{ext}\le1.}
```

For an ideal step absorber over one hemisphere at 10 um / 300 K,

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

## 8. Activation parity

The radiative boundary floor scales exponentially as `e^-Eg/kBT`; direct Auger scales as `e^{-(Eg/2+K_th)/kBT}`.

Therefore

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

At the previous `K_th=10 kBT` witness, the direct-Auger/radiative exponential factor is

```math
\boxed{4.99\times10^{-4}.}
```

Within the positive-curvature scalar-asymmetry family,

```math
\boxed{K_{th}\ge\sqrt3\,E_g/2>E_g/2.}
```

so this controlled family lies on the favorable side of activation parity, although unresolved prefactors still determine whether `Xi_A^ext <= 1`.

---

# Prior-art boundary

Established territory includes radiative detailed balance, photovoltaic/luminescence reciprocity, modal Kirchhoff laws, radiative dark-current formulas, photon recycling, HgCdTe photon transport, direct-gap Auger activation, threshold powers, Kane overlap zeros, and quasi-relativistic HgCdTe-QW Auger suppression.

No individual ingredient is a novelty claim.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC JOINT ADMISSIBILITY SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

---

# DO NOT DO

Do not rank compounds. Do not replace multiband kinematics with an empirical Auger lifetime. Do not draft a paper yet.

# NEXT ACTION

The two-band direct-Auger problem and external radiative-boundary floor are now closed at the controlled-model level.

Proceed to the minimal **third-band/heavy-hole escape channel**:

> Add a heavy-hole-like reservoir to the high-`v` symmetric active pair and derive exact three-band Auger kinematics. Determine whether an extra-band direct channel remains open and derive the minimum band offset/mass/velocity condition required to preserve a radiative-floor-limited regime.

Start with kinematics only. Add matrix elements only after support/threshold is known.
