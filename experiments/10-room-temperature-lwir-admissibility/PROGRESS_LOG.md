# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch initialization

Created branch

```text
experiment-10-room-temperature-lwir-admissibility
```

with the objective of deriving a finite-gap band-structure admissibility theorem/bound rather than ranking known materials.

Novelty hazards excluded at founding: generic `alpha/G_th`, `alpha sqrt(tau)`, low-`n_i` arguments, radiative detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## 2026-08-14 — matched massive-Dirac absorptance

Controlling file:

`MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`

Derived

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
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

Ideal ballistic crossing time is `v^0`.

At 10 um / 300 K, exact finite-gap Dirac carrier density is `1.8644x` the edge-parabolic estimate.

Disposition:

```text
MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — Kane velocity freedom and microscopic resource bound

Controlling file:

`KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`

Using

```math
E_P=2m_0P^2/\hbar^2,
\qquad
v^2=E_P/(3m_0),
```

obtained

```math
\Sigma_e\propto E_P^{-1}.
```

Generic upper-bound attempts based on the multiband effective-mass identity, global optical f-sum over a fixed detector energy window, and fixed remote-band energy did **not** provide a material-independent upper `v`.

For a Wannier Hamiltonian,

```math
\boxed{
\|\hat v_i\|
\le\frac1\hbar\sum_R|R_i|\|H_R\|
\equiv V_i^{hop},
}
```

so conditionally

```math
v\le V_{hop}
```

and

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

Disposition:

```text
MICROSCOPIC-RESOURCE-CONDITIONED DETECTOR INEQUALITY DERIVED.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — exact symmetric-Dirac Auger kinematic closure

Controlling file:

`AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
```

strict subadditivity gives empty exact normal-momentum phononless `eeh` / `hhe` Auger support in the particle-hole-symmetric two-band model.

The exact off-shell mismatch is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/Eg`, `v` cancels. Therefore high `v` and particle-hole symmetry are distinct design resources.

Broad Dirac/symmetric-dispersion Auger suppression is established prior art.

---

## 2026-08-14 — scalar particle-hole-asymmetry reopening law

Controlling file:

`AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`

Reproducible calculation:

`numerics/auger_asymmetry_threshold.py`

Add

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

with

```math
\beta=D\Delta/(\hbar^2v^2),
```

and

```math
\boxed{
\mathcal A_m
=\frac{|m_e^{-1}-m_h^{-1}|}
{m_e^{-1}+m_h^{-1}}
=2|\beta|.
}
```

The exact reopening boundary is

```math
\boxed{
\beta_c(q_0)
=
\min_{0\le x\le q_0/2}
\frac{2s(x)+s(q_0-2x)-s(q_0)}
{2(q_0-x)^2},
\qquad s(q)=\sqrt{1+q^2}.
}
```

For weak asymmetry,

```math
\boxed{
\beta_c\sim4/q_{th}^3,
\qquad
K_{th}\sim E_g\mathcal A_m^{-1/3}.
}
```

At 10 um / 300 K, exact inversion gives approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to place the direct threshold above `10 kBT` in the scalar-asymmetry model.

The edge-mass interpretation is model-specific; the physical requirement is finite-momentum electron-hole symmetry over the Auger-active window.

Broad threshold enhancement near quasi-relativistic HgCdTe-QW regimes is established prior art; novelty of the cube-root reduced-model law is not established.

---

## 2026-08-14 — near-threshold direct Auger phase space and thermal scaling

Controlling file:

`AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`

Reproducible check:

`numerics/auger_near_threshold_phase_space.py`

### Fixed-hot-electron phase space

After momentum conservation, the final state has six local relative coordinates. On the interior threshold branch, numerical Hessian checks confirm a positive-definite constrained minimum and a linear opening of available energy above threshold.

Hence the pure energy-shell measure obeys

```math
\boxed{
\Phi_{3body}(K)\propto(K-K_{th})^2.
}
```

For a smooth nonzero threshold matrix element,

```math
\Gamma_{II}\propto(K-K_{th})^2.
```

However, if

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{
\Gamma_{II}\propto(K-K_{th})^{2+\nu}.
}
```

This distinction is required by Kane-model prior art: threshold overlap zeros can change the pre-exponential power. The phase-space exponent `2` is robust; the full-rate exponent is not universal without a microscopic spinor model.

### Thermal activation

Detailed balance through inverse impact ionization gives

```math
\boxed{
G_A^{vol}
\propto
T^{3+\nu}
\exp\!\left[-\frac{E_g/2+K_{th}}{k_BT}\right]
}
```

near threshold.

For `nu=0`, low-T division by the parabolic-edge `n_i` reproduces the classical Beattie-Landsberg structure

```math
\tau_A^{-1}\propto T^{3/2}e^{-K_{th}/k_BT}.
```

This was used as a cross-check only; exact finite-gap Dirac statistics remain required for quantitative Experiment-10 carrier densities.

At the `A_m ~= 0.08476` witness,

```text
K_th/kBT = 10
exp(-K_th/kBT) = 4.54e-5
exp[-(Eg/2+K_th)/kBT] = 4.13e-6
```

### High-v scaling at matched absorptance

Before interaction momentum dependence,

```math
G_A^{vol}\propto|V_{th}|^2v^{-9},
```

and because `d~v`,

```math
G_A^{area}\propto|V_{th}|^2v^{-8}.
```

For the minimal screened Coulomb interaction

```math
V(Q)
=\frac{e^2}{\epsilon_0\epsilon_r(Q^2+\kappa^2)}S_{cv},
```

with

```math
Q_{th}=\frac{\Delta}{\hbar v}\mathcal Q_{th},
```

obtained

```math
\boxed{
G_A^{area}
\propto
\frac{|S_{cv}|^2}{\epsilon_r^2}
\frac{v^{-4}}
{(\mathcal Q_{th}^2+s_\kappa^2)^2}
\left(\frac{k_BT}{\Delta}\right)^{3+\nu}
\exp[-(\Delta+K_{th})/(k_BT)],
}
```

where

```math
s_\kappa=\hbar v\kappa/\Delta.
```

Weak screening at the threshold transfer gives `G_A^area ~ v^-4`; fixed physical screening length can strengthen this toward `v^-8`. For intrinsic Debye screening, `s_kappa^2 ~ v^-1`, so the large-`v` asymptote tends toward `v^-4`.

### First joint rate-level structure

In the weak-screening, smooth-matrix limit,

```math
\boxed{
G_A^{area}
\sim
\mathcal I_A
v^{-4}
\exp[-K_{th}(\mathcal A_m)/(k_BT)]
\exp[-E_g/(2k_BT)].
}
```

With

```math
K_{th}\sim E_g\mathcal A_m^{-1/3},
```

large `v` provides algebraic direct-Auger suppression while small finite-`k` asymmetry provides exponential suppression.

This is the first formula in the branch where both favorable band-structure coordinates enter the same nonradiative event rate.

Disposition:

```text
RATE FACTORIZATION DERIVED IN CONTROLLED MODEL.
FULL INTERACTION PREFactor NOT UNIVERSAL.
NOVELTY NOT ESTABLISHED.
```

### Prior-art notes

Cross-checked against:

```text
Combescot & Combescot, PRB 37, 8781 (1988): classical activated direct-gap lifetime and anisotropy-dependent prefactors;
Gelmont, Phys. Lett. A 66, 323-324 (1978): Kane overlap zero at threshold changes pre-exponential behavior;
Afanasiev, Greshnov & Zegrya: quadratic/cubic threshold impact-ionization contributions in multiband direct-gap semiconductors;
Alymov / Morozov HgCdTe-QW work: symmetry-controlled Auger suppression.
```

No individual threshold or rate exponent is available as a novelty claim.

---

## Active frontier

The direct Auger channel is now factored as far as useful without choosing a complete multiband wave-function model.

Next derive the **radiative/background generation floor under matched external absorptance and optical environment**, then compare it to the thresholded Auger rate.

Target:

```math
G_A\le G_{rad}+G_{bg}
```

with the right-hand side fixed by optical boundary conditions wherever detailed balance permits.

This is the natural point to replace the provisional `Xi_nr` bookkeeping idea with a derived detector-level admissibility inequality.
