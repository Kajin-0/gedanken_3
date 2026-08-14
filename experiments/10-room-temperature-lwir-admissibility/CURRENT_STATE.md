# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **MATCHED-ABSORPTANCE HIGH-v LEVER SURVIVES / MICROSCOPIC VELOCITY RESOURCE BOUND DERIVED / SYMMETRIC-DIRAC AUGER CLOSURE DERIVED / FINITE-ASYMMETRY THRESHOLD DERIVED / NEAR-THRESHOLD DIRECT-AUGER RATE FACTORIZED / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

## Research objective

Derive from first principles the electronic-structure conditions a passive LWIR interband absorber must satisfy to approach HgCdTe-class intrinsic detector quality near 300 K without sacrificing useful temporal response.

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

## Read first

1. `AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`
2. `AUGER_ASYMMETRY_REOPENING_STEP_2026-08-14.md`
3. `AUGER_KINEMATIC_CLOSURE_STEP_2026-08-14.md`
4. `KANE_VELOCITY_RESOURCE_BOUND_STEP_2026-08-14.md`
5. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
6. `PROGRESS_LOG.md`

---

# Result A — matched-absorptance thermodynamic lever

For the intrinsic isotropic finite-gap massive-Dirac family,

```math
n_e\propto N_Dv^{-3},
\qquad
\alpha\propto N_Dv^{-1},
\qquad
d\propto v/N_D,
```

so

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

Ideal ballistic crossing time is `v^0`. At 10 um / 300 K the exact finite-gap carrier density is `1.8644x` the edge-parabolic estimate.

---

# Result B — microscopic velocity resource

A Wannier/tight-binding Hamiltonian gives

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

and therefore

```math
\boxed{\Sigma_e\ge C/V_{hop}^2.}
```

No chemistry-independent numerical upper `v` follows from the low-energy effective-mass sum, optical f-sum, or remote-band energy separation alone.

---

# Result C — exact symmetric-Dirac Auger closure

For

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\qquad\Delta=E_g/2>0,
```

normal-momentum phononless `eeh` and `hhe` Auger channels have empty exact kinematic support in the particle-hole-symmetric two-band model.

The minimum off-shell mismatch is

```math
\boxed{
\Delta_A(E)=\sqrt{E^2+2E_g^2}-E.
}
```

At fixed `E/Eg`, `v` cancels. High `v` and electron-hole symmetry are distinct favorable resources.

---

# Result D — scalar particle-hole-asymmetry reopening

Use

```math
E_\pm(k)=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

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

The exact reduced-model reopening boundary is

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

At 10 um / 300 K, the exact scalar-asymmetry model requires approximately

```math
\boxed{\mathcal A_m\lesssim0.0848}
```

to put the direct-channel threshold above `10 k_BT`.

This is not a universal edge-mass rule; the physical requirement is finite-momentum electron-hole symmetry over the Auger-active window.

---

# Result E — near-threshold direct Auger phase space and thermal factor

Controlling file:

`AUGER_NEAR_THRESHOLD_RATE_STEP_2026-08-14.md`

Reproducible check:

`numerics/auger_near_threshold_phase_space.py`

After crystal-momentum conservation, a fixed hot electron has six local relative final-state coordinates. On the interior reopening branch, the constrained final-energy Hessian is positive definite and the channel opens linearly with hot-electron excess energy.

Therefore the purely kinematic energy-shell measure is

```math
\boxed{
\Phi_{3body}(K)\propto(K-K_{th})^2\Theta(K-K_{th}).
}
```

If the squared microscopic matrix element is finite at threshold (`nu=0`),

```math
\boxed{
\Gamma_{II}(K)\propto(K-K_{th})^2.
}
```

More generally, if

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{
\Gamma_{II}(K)\propto(K-K_{th})^{2+\nu}.
}
```

This distinction is mandatory: Kane-model literature contains threshold overlap zeros that change the pre-exponential power. Thus the exponent `2` is a phase-space result, not a universal full-rate exponent.

## Thermal activation

Detailed balance through the inverse impact-ionization process gives, for the smooth-matrix case,

```math
\boxed{
G_A^{vol}
\propto
T^3
\exp\!\left[-\frac{E_g/2+K_{th}}{k_BT}\right].
}
```

With a threshold matrix-element zero of order `nu`,

```math
\boxed{
G_A^{vol}
\propto
T^{3+\nu}
\exp\!\left[-\frac{E_g/2+K_{th}}{k_BT}\right].
}
```

In the low-T parabolic-edge limit, division by `n_i` recovers the classical direct-gap lifetime structure

```math
\tau_A^{-1}\propto
T^{3/2+\nu}e^{-K_{th}/k_BT}.
```

The activation exponent is robust; the polynomial power is interaction/spinor dependent.

At the `A_m ~= 0.08476` witness,

```math
K_{th}=10k_BT,
```

so

```math
\boxed{e^{-K_{th}/k_BT}=4.54\times10^{-5}}
```

and

```math
\boxed{
\exp[-(E_g/2+K_{th})/(k_BT)]
=4.13\times10^{-6}.
}
```

---

# Result F — conditional Coulomb-v scaling at matched absorptance

Before inserting the momentum dependence of the interaction, the four-particle golden-rule measure gives

```math
G_A^{vol}\propto |V_{th}|^2v^{-9}
```

at fixed `beta`, `E_g`, `T/E_g`, and normalized threshold geometry. Because matched absorptance requires `d ~ v`,

```math
G_A^{area}\propto |V_{th}|^2v^{-8}.
```

This is not yet the physical Coulomb scaling.

For the minimal statically screened interaction

```math
V(Q)
=\frac{e^2}{\epsilon_0\epsilon_r(Q^2+\kappa^2)}S_{cv},
```

with threshold transfer

```math
Q_{th}=\frac{\Delta}{\hbar v}\mathcal Q_{th},
```

define

```math
s_\kappa=\hbar v\kappa/\Delta.
```

Then the matched-area direct-channel scaling becomes

```math
\boxed{
G_A^{area}
\propto
\frac{|S_{cv}|^2}{\epsilon_r^2}
\frac{v^{-4}}
{(\mathcal Q_{th}^2+s_\kappa^2)^2}
\left(\frac{k_BT}{\Delta}\right)^{3+\nu}
\exp[-(\Delta+K_{th})/(k_BT)].
}
```

Thus:

```text
weak screening at threshold transfer:
    G_A^area ~ v^-4;

fixed physical screening length at sufficiently large v:
    G_A^area ~ v^-8;

intrinsic Debye screening:
    s_kappa^2 ~ v^-1, so the large-v asymptote tends toward v^-4.
```

Within this minimal screened-Coulomb model, the smaller physical momentum transfer weakens but does not cancel the high-`v` Auger advantage.

---

# First joint rate-level structure

For weak screening and a smooth threshold matrix element, the reduced-model dependence is schematically

```math
\boxed{
G_A^{area}
\sim
\mathcal I_A
v^{-4}
\exp\!\left[-\frac{K_{th}(\mathcal A_m)}{k_BT}\right]
\exp[-E_g/(2k_BT)],
}
```

where `mathcal I_A` contains dielectric response, threshold spinor overlap, exchange, species counting, and finite-width corrections.

Using the weak-asymmetry threshold,

```math
K_{th}\sim E_g\mathcal A_m^{-1/3},
```

so the two band-structure coordinates enter differently:

```text
large v:
    algebraic suppression of direct Auger events;

small finite-k particle-hole asymmetry:
    exponential threshold suppression.
```

This is the first Experiment-10 formula in which both favorable resources enter the same direct nonradiative event rate.

---

# Prior-art boundary

Established territory includes threshold-activated direct-gap Auger lifetimes, Beattie-Landsberg thermal activation, anisotropy/warping corrections to pre-exponential powers, Kane overlap zeros at threshold, quadratic/cubic impact-ionization threshold laws, and HgCdTe-QW Auger suppression near quasi-relativistic symmetry.

Mandatory comparators include Combescot & Combescot PRB 37, 8781 (1988); Gelmont Phys. Lett. A 66, 323-324 (1978); Afanasiev, Greshnov & Zegrya on direct-gap impact-ionization threshold powers; Alymov et al. PRB 2018 / ACS Photonics 2020; Morozov et al. ACS Photonics 2021.

```text
NOVELTY NOT ESTABLISHED.
```

The possible surviving contribution is the detector-specific joint admissibility synthesis, not any individual threshold or Auger ingredient.

---

# What remains unresolved

```text
microscopic spinor/exchange exponent nu for the desired massive-Dirac material class;
dynamic screening rather than static screening;
heavy-hole/remote-band Auger channels;
phonon-, disorder-, and Umklapp-assisted Auger;
exact radiative/background event floor at matched absorptance;
full detector SNR/D* implication;
novelty of the combined framework.
```

# NEXT ACTION

The direct Auger channel is now factored as far as possible without choosing a complete multiband wave-function model.

Next derive the unavoidable radiative/background generation floor under the already imposed matched external absorptance and optical environment, then compare it to the thresholded direct-Auger event rate.

Target question:

> Can one express a detector-level admissibility condition `G_A <= G_rad + G_bg` in terms of `v`, finite-momentum asymmetry, dielectric/screening resources, and the fixed optical boundary, thereby replacing the provisional `Xi_nr` bookkeeping idea with a derived inequality?

Do not rank real materials yet.
