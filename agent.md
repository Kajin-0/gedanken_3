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
2. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

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

and equivalent Dirac-species degeneracy cancels from `Sigma_e`. Ideal ballistic crossing time is `v^0`.

## 2. Microscopic velocity resource

A lattice/Wannier Hamiltonian gives

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

## 3. Symmetric-Dirac direct Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
```

normal-momentum phononless `eeh` and `hhe` Auger channels have empty exact support in the symmetric two-band model.

The exact off-shell mismatch is

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
\mathcal A_m=2|\beta|,
\qquad
\beta=D\Delta/(\hbar^2v^2),
```

the exact reduced-model threshold is in `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`.

Weak-asymmetry law:

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to place the direct threshold above `10 kBT`.

Do not treat this as a universal edge-mass criterion; finite-momentum dispersion symmetry is what matters.

## 5. Near-threshold direct Auger rate

For a fixed hot electron, the six-dimensional constrained final-state phase space gives

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{\Gamma_{II}\propto(K-K_{th})^{2+\nu}.}
```

The phase-space exponent `2` is robust; the full-rate exponent is not universal because Kane/multiband overlap factors can vanish at threshold.

Detailed balance gives the thermal event-rate structure

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

At the `K_th=10 kBT` witness:

```text
lifetime activation = 4.54e-5
equilibrium event activation = 4.13e-6
```

## 6. Conditional Coulomb-v scaling

Before interaction momentum dependence,

```math
G_A^{area}\propto|V_{th}|^2v^{-8}
```

at matched absorptance.

For the minimal static screened Coulomb interaction

```math
V(Q)=\frac{e^2}{\epsilon_0\epsilon_r(Q^2+\kappa^2)}S_{cv},
```

with `Q_th ~ v^-1`,

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

Weak screening and intrinsic-Debye large-`v` asymptotics tend toward

```math
G_A^{area}\propto v^{-4}e^{-K_{th}/k_BT}
```

apart from the common intrinsic gap activation and interaction resources.

Thus high `v` provides an algebraic rate advantage while small finite-`k` asymmetry provides an exponential threshold advantage.

---

# Prior-art boundary

Established territory includes direct-gap Auger activation thresholds, Beattie-Landsberg thermal factors, anisotropy/warping corrections, Kane threshold-overlap zeros, quadratic/cubic impact-ionization threshold powers, and quasi-relativistic HgCdTe-QW Auger suppression.

Do not claim novelty for any individual ingredient.

Current disposition:

```text
POSSIBLE DETECTOR-SPECIFIC JOINT ADMISSIBILITY SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

---

# DO NOT DO

Do not rank candidate compounds. Do not replace the microscopic problem with an empirical Auger coefficient. Do not draft a paper yet.

# NEXT ACTION

Derive the **unavoidable radiative/background generation event floor under matched external absorptance and optical environment**.

Then compare it to the thresholded direct-Auger event rate and ask whether the branch can support a derived condition of the form

```math
G_A\le G_{rad}+G_{bg}.
```

The objective is to replace the provisional `Xi_nr` bookkeeping quantity with a detector-level admissibility inequality whose radiative side is fixed by optical boundary conditions and whose Auger side is expressed through `v`, finite-momentum asymmetry, and explicit interaction resources.
