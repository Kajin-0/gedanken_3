# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch initialization

Created `experiment-10-room-temperature-lwir-admissibility` to derive a finite-gap band-structure admissibility theorem/bound rather than rank materials.

Immediate novelty exclusions: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## 2026-08-14 — matched massive-Dirac absorptance

Controlling file: `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`.

Derived

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

At 10 um / 300 K, exact finite-gap Dirac density is `1.8644x` the edge-parabolic estimate.

---

## 2026-08-14 — Kane velocity freedom and microscopic resource

Controlling file: `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`.

Low-energy effective-mass sums, fixed-window optical f-sum, and fixed remote-band energy did **not** give a universal upper `v`.

For a Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally `v <= V_hop` and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

Negative-path lesson: a useful high-`v` ceiling requires an ultraviolet material resource, not generic low-energy sum rules.

---

## 2026-08-14 — exact symmetric two-band Auger closure

Controlling file: `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`.

For `epsilon=sqrt(Delta^2+(hbar v k)^2)`, strict subadditivity closes normal-momentum phononless `eeh` and `hhe` channels exactly.

Exact mismatch:

```math
\boxed{\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.}
```

At fixed `E/Eg`, `v` cancels. Large `v` and dispersion symmetry are separate resources.

Broad Dirac/symmetric Auger suppression is established prior art.

---

## 2026-08-14 — scalar asymmetry reopening

Controlling file: `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`.

For `E_±=Dk^2±sqrt(Delta^2+(hbar v k)^2)`, define normalized inverse-mass asymmetry `A_m=2|D Delta/(hbar^2 v^2)|`.

Weak-asymmetry threshold:

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At 10 um / 300 K, the exact scalar model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct threshold above `10 kBT`.

The edge-mass interpretation is not universal; finite-k symmetry is the physical quantity.

---

## 2026-08-14 — near-threshold two-band direct-Auger rate

Controlling file: `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`.

Pure interior-threshold phase space gives

```math
\boxed{\Phi_{3body}\propto(K-K_{th})^2.}
```

If the threshold matrix element contributes `|V_eff|^2 ~ (K-K_th)^nu`, then

```math
\Gamma_{II}\propto(K-K_{th})^{2+\nu}.
```

Detailed balance gives

```math
G_A^{vol}\propto T^{3+\nu}e^{-(E_g/2+K_{th})/(k_BT)}.
```

For minimal static screened Coulomb and matched absorptance, weak-screening/intrinsic-Debye large-`v` scaling tends toward

```math
G_A^{area}\sim v^{-4}e^{-K_{th}/k_BT}
```

apart from the common intrinsic gap factor and interaction remainder.

Correction retained: exponent `2` belongs to phase space, not universally to the full rate; Kane overlap zeros can add powers.

---

## 2026-08-14 — external radiative boundary and event-traffic admissibility

Controlling file: `RADIATIVE_BOUNDARY_ADMISSIBILITY_STEP_2026-08-14.md`.

Correction: matching useful front-side absorptance alone does not fix thermal emission. The complete external mode-resolved absorptance must be matched.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant under photon recycling. Use irreversible external optical traffic.

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

Ideal 10-um / 300-K hemispherical step absorber:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Direct-Auger/radiative activation ratio:

```math
\boxed{
\Xi_A^{ext}\propto_{exp}
\exp[-(K_{th}-E_g/2)/(k_BT)].
}
```

Activation parity occurs at `K_th=E_g/2`.

---

## 2026-08-14 — minimal third-band / heavy-hole Auger escape

Controlling file:

`THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`

Reproducible calculation:

`numerics/third_band_heavy_hole_threshold.py`

### Model

Retain the active massive-Dirac conduction/light-hole pair and add

```math
E_{hh}(k)
=\Delta+\delta_{hh}
+\frac{\hbar^2k^2}{2M_{hh}}.
```

Define

```math
\rho=M_{hh}v^2/\Delta=M_{hh}/m_D,
\qquad
\eta=\delta_{hh}/\Delta.
```

Analyze inverse CCCH impact ionization

```text
e_0 -> e_1 + e_2 + h_hh.
```

### Exact fixed-momentum minimum

Strict convexity gives a collinear minimum with equal final-electron momenta. Parameterizing by common group velocity `u`,

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

For mismatch `D(q)=F(q)-sqrt(1+q^2)`, the envelope theorem gives

```math
\boxed{D'(q)<0.}
```

Also

```math
D(0)=2+\eta,
```

and

```math
\boxed{D(\infty)=1+\eta-\rho/2.}
```

### Exact opening theorem

Therefore

```math
\boxed{
\rho<2(1+\eta)\Rightarrow\text{closed at all finite energies},
}
```

```math
\boxed{
\rho=2(1+\eta)\Rightarrow\text{asymptotically marginal},
}
```

```math
\boxed{
\rho>2(1+\eta)\Rightarrow\text{one unique finite threshold}.
}
```

Equivalently,

```math
\boxed{
M_{hh}v^2\le2(\Delta+\delta_{hh})
}
```

is the exact finite-energy CCCH closure condition in this minimal model.

### First direct high-v conflict

Earlier, `Sigma_e ~ v^-2` favored large `v`. Here

```math
\rho=M_{hh}v^2/\Delta\propto v^2
```

for fixed spectator band. Thus increasing `v` pushes the heavy-hole channel toward reopening.

This is the first mechanism found in Experiment 10 that directly conflicts with the high-`v` thermodynamic lever.

Closure requires

```math
\boxed{
v\le\sqrt{2(\Delta+\delta_{hh})/M_{hh}}.}
```

For a touching spectator band at 10 um,

```math
M_{hh}^{max}=E_g/v^2.
```

At `v=1e6 m/s`, this is only `0.02181 m0`; at `1.07e6 m/s`, `0.01905 m0`.

### Threshold asymptotics

Near the opening boundary `rho_c=2(1+eta)`,

```math
\boxed{
q_{th}\sim3/(\rho-\rho_c),
\qquad
K_{th}^{hh}/\Delta\sim3/(\rho-\rho_c).
}
```

For a very heavy spectator band,

```math
\boxed{K_{th}^{hh}\to E_g+\delta_{hh}.}
```

For a flat touching heavy-hole band,

```math
\boxed{K_{th}^{hh}\to E_g.}
```

This recovers the standard low-threshold CCCH/Auger-1 direction.

### Radiative comparison

Rigorous bound:

```math
\boxed{K_{th}^{hh}\ge E_g+\delta_{hh}.}
```

Thus for `delta_hh>=0` the open heavy-hole channel remains thermally steeper than the external radiative floor, but in the flat touching-band limit the exponent-only ratio degrades to

```math
\boxed{e^{-E_g/(2k_BT)}=0.0909}
```

at 10 um / 300 K. This erases most of the stronger two-band symmetry margin.

### Prior-art disposition

Heavy-hole CCCH / Auger-1 in bulk HgCdTe, the flat heavy-hole branch in simplified Kane physics, and multiband Auger engineering are established. The compact closure theorem is retained as a reduced-model derivation only.

```text
NOVELTY NOT ESTABLISHED.
```

---

## Active frontier

The minimal third-band support problem is closed.

Next derive the **near-threshold heavy-hole CCCH phase-space and algebraic `v` / `M_hh` scaling** while keeping the multiband Coulomb/spinor overlap explicit.

Question:

> Once `M_hh v^2 > 2(Delta+delta_hh)`, does the heavy spectator-band DOS inevitably overwhelm the fixed external radiative floor, or is there still an explicit prefactor/offset regime with `Xi_hh^ext <= 1`?

Do not insert empirical Auger-1 lifetimes and do not rank materials yet.
