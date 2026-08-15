# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch initialization

Created `experiment-10-room-temperature-lwir-admissibility` to derive a finite-gap band-structure admissibility theorem/bound rather than rank materials.

Immediate novelty exclusions: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## 2026-08-14 — matched massive-Dirac absorptance

Derived

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

hence

```math
\boxed{\Sigma_e=C/v^2}
```

with equivalent-species cancellation and ideal ballistic crossing time `v^0`.

At 10 um / 300 K the exact finite-gap Dirac density is `1.8644x` the edge-parabolic estimate.

Controlling file: `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`.

---

## 2026-08-14 — Kane velocity resource

Generic low-energy effective-mass sums, fixed-window optical f-sums, and remote-band energy separation did not give a universal upper `v`.

A Wannier Hamiltonian gives

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally `v<=V_hop` and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

Controlling file: `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`.

---

## 2026-08-14 — exact symmetric two-band Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
```

strict subadditivity closes normal-momentum phononless `eeh` and `hhe` Auger exactly.

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. Large `v` and electron-hole symmetry are separate resources.

Broad Dirac/symmetric Auger suppression is prior art.

Controlling file: `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`.

---

## 2026-08-14 — particle-hole-asymmetry reopening

For

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

derived an exact finite-energy reopening boundary and the weak-asymmetry law

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the scalar model needs about `A_m<=0.0848` for `K_th>=10kBT`.

Broad threshold enhancement by symmetric quasi-relativistic dispersion is established prior art. Novelty of the cube-root reduced-model law is unestablished.

Controlling file: `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`.

---

## 2026-08-14 — thresholded two-band direct-Auger rate

For a fixed hot electron on the interior threshold branch,

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If the microscopic squared matrix element adds a threshold zero of order `nu`,

```math
\Gamma_{II}\propto(K-K_{th})^{2+\nu}.
```

Detailed balance gives

```math
G_A^{vol}\propto T^{3+\nu}e^{-(E_g/2+K_{th})/(k_BT)}.
```

For the minimal weakly screened Coulomb model at matched absorptance, the direct-area rate tends toward `v^-4` at large `v`.

Controlling file: `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`.

---

## 2026-08-14 — external radiative boundary floor

Corrected the founding optical match: useful front-side absorptance is insufficient. The complete external mode-resolved absorptance must be matched.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant because of photon recycling; irreversible external optical traffic is the correct coarse-grained denominator.

Defined

```math
\Xi_A^{ext}
=\frac{G_A^{gen}+R_A^{rec}}
{\Phi_{abs}^{ext}+\Phi_{em}^{ext}},
```

so at equilibrium `Xi_A^ext=G_A/Phi_0`.

At 10 um / 300 K for an ideal hemispherical step absorber:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

The Auger/radiative activation-parity line is

```math
\boxed{K_{th}=E_g/2.}
```

Controlling file: `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`.

---

## 2026-08-14 — minimal heavy-hole third-band escape

Added

```math
E_{hh}(k)=\Delta+\delta_{hh}+\hbar^2k^2/(2M_{hh}).
```

With

```math
\rho=M_{hh}v^2/\Delta,
\qquad
\eta=\delta_{hh}/\Delta,
```

proved the exact CCCH classification

```math
\boxed{
\rho\le2(1+\eta)
\Longleftrightarrow
\text{no finite-energy normal-momentum CCCH support}.
}
```

Equivalently,

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

This was the first direct conflict with the high-`v` thermodynamic lever.

Near the opening boundary, `K_th/Delta~3/(rho-rho_c)`; for a flat heavy hole, `K_th->Eg+delta_hh`.

Controlling file: `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`.

---

## 2026-08-14 — open heavy-hole phase space and joint exact-closure bound

Controlling file: `HEAVY_HOLE_AUGER_RATE_AND_JOINT_BOUND_STEP_2026-08-14.md`.

Reproducible calculation: `numerics/heavy_hole_rate_and_joint_bound.py`.

### Threshold Hessian

For the open CCCH channel, the six-dimensional constrained threshold Hessian has

```math
\boxed{
\det H
=
a_\parallel\left(a_\parallel+\frac{2}{\rho}\right)
\left[
a_\perp\left(a_\perp+\frac{2}{\rho}\right)
\right]^2,
}
```

where

```math
a_\parallel=(1-u^2)^{3/2},
\qquad
a_\perp=\sqrt{1-u^2}.
```

With threshold-envelope factor

```math
\gamma
=1-u_{th}/[q_{th}/\sqrt{1+q_{th}^2}],
```

the pure fixed-hot threshold shell is

```math
\boxed{
\Phi_{hh}^{(q)}
\propto
\frac{\gamma^2}{\sqrt{\det H}}
(K-K_{th}^{hh})^2.
}
```

### Negative result — no heavy-hole-DOS catastrophe

For `rho->infinity`,

```math
\det H\to1,
\qquad
\gamma\to1.
```

Therefore the normalized threshold phase-space coefficient stays finite. A flat heavy-hole band collapses the activation threshold but does **not** force a universal `M_hh^(3/2)` divergence in the local threshold event rate.

### Near-closure suppression

Let `delta rho=rho-rho_c>0`. Derived

```math
K_{th}^{hh}/\Delta\sim3/(\delta\rho),
```

and

```math
\boxed{
\frac{\gamma^2}{\sqrt{\det H}}
\sim
\frac{\sqrt3\rho_c^{3/2}}{64}(\delta\rho)^{3/2}.
}
```

Thus the rate near exact closure is suppressed both exponentially and algebraically.

### Conditional open-channel v scaling

In the weak-screening matched-area limit,

```math
G_{hh}^{area}
\propto
\mathcal P_{hh}(\rho,\eta)
v^{-4}
\exp[-(\Delta+K_{th}^{hh})/(k_BT)]
```

up to dielectric, spinor, exchange, screening, and thermal-power factors. The heavy-hole band does not automatically cancel the high-`v` algebraic lever.

### Stronger exact-closure result

Combining

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

Combining with the microscopic lattice resource gives

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

This is the current strongest Experiment-10 theorem candidate.

At the standard 10-um/300-K witness with a touching spectator band:

```text
M_hh/m0     v_c (m/s)      minimum Sigma_e for exact closure (cm^-2)
0.50        2.088e5         2.446e14
0.20        3.302e5         9.783e13
0.10        4.670e5         4.892e13
0.05        6.604e5         2.446e13
0.02        1.044e6         9.783e12
```

A `0.5 m0` touching spectator forces a carrier-column floor roughly 23x above the earlier `v=1e6 m/s` matched-absorptance witness if exact CCCH closure is demanded.

### Prior-art status

Established: heavy-hole Auger-1 in HgCdTe; threshold/effective-mass dependence; Kane overlap zeros; anisotropy/warping prefactors; multiband Auger engineering; detector `alpha/G_th` and `alpha sqrt(tau)` metrics.

A focused search did not locate the exact composed carrier-column inequality above. This does **not** establish novelty.

---

## Active frontier

Do not add another mechanism yet.

Perform a dedicated adversarial prior-art audit of the **joint theorem structure**:

```text
complete external optical boundary
+ matched-absorptance finite-gap carrier scaling
+ microscopic velocity resource
+ finite-k electron-hole symmetry
+ spectator-band CCCH closure
-> lower bound on matched thermal carrier column / admissible band-structure region.
```

If the synthesis survives, compress Experiment 10 into theorem/corollary form and then attack only the minimum extra channels required to invalidate it. If it does not survive, close the branch rather than accumulating more phenomenology.