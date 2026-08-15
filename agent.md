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
2. `experiments/10-room-temperature-lwir-admissibility/HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`
3. `experiments/10-room-temperature-lwir-admissibility/THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`
4. `experiments/10-room-temperature-lwir-admissibility/RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`
5. `experiments/10-room-temperature-lwir-admissibility/AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
6. `experiments/10-room-temperature-lwir-admissibility/AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
7. `experiments/10-room-temperature-lwir-admissibility/AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
8. `experiments/10-room-temperature-lwir-admissibility/KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
9. `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
10. `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`

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

# Controlling results

## Matched absorptance

```math
\boxed{\Sigma_e=C/v^2.}
```

At the standard witness (`A=0.90`, `r=1.2`, `n_b=3.5`),

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

## Lattice velocity resource

```math
\boxed{v\le V_{hop}}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

## Symmetric two-band Auger

Exact finite-gap massive-Dirac `eeh/hhe` direct Auger is kinematically closed. Scalar particle-hole asymmetry reopens it with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

Interior threshold phase space scales as `(K-K_th)^2`; microscopic overlap zeros may add powers.

## External optical floor

Match the complete external mode-resolved optical boundary, not useful front-side absorptance alone.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Use external irreversible optical traffic, not bulk radiative recombination, as the coarse-grained radiative denominator because photon recycling breaks the latter invariance.

At 10 um / 300 K for the ideal hemispherical step absorber:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Direct-Auger/radiative activation parity occurs at

```math
K_{th}=E_g/2.
```

## Heavy-hole third-band escape

For

```math
E_{hh}(k)=\Delta+\delta_{hh}+\hbar^2k^2/(2M_{hh}),
```

exact finite-energy CCCH closure is equivalent to

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

If open, the threshold is unique. Near the closure boundary,

```math
K_{th}^{hh}/\Delta\sim3/(\rho-\rho_c).
```

For a flat heavy hole,

```math
K_{th}^{hh}\to E_g+\delta_{hh}.
```

## Heavy-hole threshold phase space

The constrained six-dimensional Hessian gives

```math
\det H
=
a_\parallel(a_\parallel+2/\rho)
[a_\perp(a_\perp+2/\rho)]^2.
```

The threshold shell is

```math
\Phi_{hh}^{(q)}
\propto
\frac{\gamma^2}{\sqrt{\det H}}
(K-K_{th}^{hh})^2.
```

Flat-heavy-hole limit:

```math
\det H\to1,
\qquad\gamma\to1.
```

Therefore there is no universal independent `M_hh^(3/2)` divergence in the local threshold event rate. The heavy band mainly collapses the activation threshold.

Near exact closure, with `delta rho=rho-rho_c`,

```math
\boxed{
\frac{\gamma^2}{\sqrt{\det H}}
\sim
\frac{\sqrt3\rho_c^{3/2}}{64}(\delta\rho)^{3/2},
}
```

while `K_th~3Delta/delta rho`.

Conditional weak-screening matched-area scaling remains approximately

```math
G_{hh}^{area}\sim
\mathcal P_{hh}(\rho,\eta)v^{-4}
\exp[-(\Delta+K_{th}^{hh})/(k_BT)]
```

before unresolved dielectric/spinor/exchange factors.

---

# Strongest current theorem candidate

Combining matched absorptance

```math
\Sigma_e=C/v^2
```

with exact CCCH closure

```math
v^2\le2(\Delta+\delta_{hh})/M_{hh}
```

gives

```math
\boxed{
\Sigma_e
\ge
C\frac{M_{hh}}{2(\Delta+\delta_{hh})}.
}
```

Combining with the lattice resource gives

```math
\boxed{
\Sigma_e
\ge
\max\!\left[
C/V_{hop}^2,
C M_{hh}/(2(\Delta+\delta_{hh}))
\right].
}
```

For a touching `0.5 m0` spectator at the standard 10-um/300-K witness, exact CCCH closure restricts `v<=2.088e5 m/s` and forces

```math
\Sigma_e\ge2.446\times10^{14}\ \mathrm{cm^{-2}}.
```

That is about 23x the earlier `v=1e6 m/s` matched-column witness.

---

# Novelty boundary

Established and not novelty:

```text
alpha/G_th and alpha sqrt(tau) detector figures of merit;
classical direct-gap Auger thresholds and effective-mass dependence;
HgCdTe CCCH/Auger-1 with heavy holes;
Kane overlap zeros;
anisotropy/warping pre-exponential corrections;
Dirac/symmetric Auger suppression;
HgCdTe-QW multiband Auger engineering;
radiative detailed balance and photon recycling.
```

A focused search has not established prior art for the composed exact-closure carrier-column inequality. This is **not** a novelty claim.

---

# DO NOT DO

Do not rank compounds. Do not add another phenomenological recombination mechanism. Do not insert empirical Auger coefficients. Do not draft a paper before the joint theorem receives a dedicated novelty audit.

# NEXT ACTION

Perform an adversarial primary-literature audit specifically against the composed structure

```text
complete external optical boundary
+ matched absorptance
+ high-v thermal carrier-column law
+ microscopic velocity resource
+ finite-k electron-hole symmetry
+ spectator-band CCCH closure
-> lower bound on matched carrier column / admissible band-structure region.
```

If this survives, rewrite Experiment 10 in theorem/corollary form and identify the minimum additional channel needed to invalidate it. If prior art already contains the same synthesis, close or reframe Experiment 10 rather than adding complexity.