# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **FIRST HARD DERIVATION CLOSED / MASSIVE-DIRAC MATCHED-ABSORPTANCE LEVER SURVIVES / CROSS-CLASS PARABOLIC COMPARATOR CONDITIONAL / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET**

## Research question

Can one derive, from first principles, the electronic-structure conditions that a passive LWIR photon-detector absorber must satisfy to operate near 300 K with HgCdTe-class or near-HgCdTe-class sensitivity **without sacrificing useful temporal response**?

The objective remains a finite-gap **band-structure admissibility theorem or no-go result**, not a materials leaderboard and not a new scalar figure of merit.

## Fixed target

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
```

```math
E_g=0.1239841984\ \mathrm{eV},
\qquad
k_BT=0.0258519998\ \mathrm{eV},
```

```math
\boxed{E_g/(k_BT)\approx4.796.}
```

## Controlling new derivation

Read first:

`MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`

The model is an intrinsic isotropic 3-D massive Dirac absorber

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad
\Delta=E_g/2,
```

with `N_D` equivalent Dirac species.

### Exact thermal density

At intrinsic `mu=0`,

```math
\boxed{
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3
F_2(\delta),
}
```

```math
F_2(\delta)
=\int_0^\infty
\frac{x^2dx}
{\exp(\sqrt{x^2+\delta^2})+1},
\qquad
\delta=\Delta/(k_BT).
```

Hence

```math
\boxed{n_e\propto N_Dv^{-3}.}
```

At 10 um / 300 K,

```math
\delta=2.39796146,
\qquad
F_2=0.7887622040.
```

For `N_D=1`, `v=1e6 m/s`,

```math
n_e=4.8421\times10^{15}\ \mathrm{cm^{-3}}.
```

### Parabolic finite-gap warning

Using the band-edge mass

```math
m_D=\Delta/v^2
```

in the ordinary nondegenerate parabolic density gives

```math
\boxed{
n_e^{Dirac}/n_e^{par}\approx1.8644
}
```

at the actual 10-um / 300-K target. The finite-gap nonparabolic correction is therefore already large enough that the exact dispersion must be retained.

## Exact interband optical scaling

The clean-limit interband conductivity is

```math
\boxed{
\sigma_1(\omega)
=
\frac{N_De^2\omega}{12\pi\hbar v}
\left(1+\frac{2\Delta^2}{\hbar^2\omega^2}\right)
\sqrt{1-\frac{4\Delta^2}{\hbar^2\omega^2}}
\tanh\left(\frac{\hbar\omega}{4k_BT}\right)
}
```

above the gap.

Therefore, at fixed `E_g,T` and normalized photon energy,

```math
\boxed{\alpha\propto N_Dv^{-1}.}
```

This inverse-velocity optical-conductivity scaling is established 3-D Dirac physics and is not itself a novelty claim.

## Headline first result — matched absorptance

For ideal single-pass absorptance

```math
A=1-e^{-\alpha d},
```

matching a fixed optical depth requires

```math
\boxed{d\propto v/N_D.}
```

The equilibrium electron column per detector area is

```math
\Sigma_e=n_ed.
```

Combining the exact thermal density and absorption gives

```math
\boxed{
\Sigma_e\propto v^{-2},
\qquad
\Sigma_e\text{ is independent of }N_D.
}
```

Thus, **inside the ideal massive-Dirac family, the low-DOS advantage is not exactly canceled by reduced absorption.** A larger `v` reduces the thermal carrier column at fixed absorptance.

A second result corrects the founding heuristic: equivalent valley/species degeneracy is not a thermal-column lever after absorptance is matched, because its linear increase in carrier density is canceled by the corresponding linear increase in absorption.

## Temporal check

For a photon with

```math
r=\hbar\omega/E_g>1,
```

the excited quasiparticle speed is

```math
u_\omega=v\sqrt{1-r^{-2}}.
```

Since

```math
d\propto v,
\qquad
u_\omega\propto v,
```

```math
\boxed{\tau_{ball}=d/u_\omega\propto v^0.}
```

So the simplest absorptance-versus-ballistic-transit tradeoff does **not** erase the `v^-2` thermal-column advantage.

This is not yet a full detector-bandwidth theorem.

## Numerical witness

At

```text
r = 1.2,
n_b = 3.5,
N_D = 1,
A = 0.90,
```

```text
v (m/s)       n_e (cm^-3)      alpha (cm^-1)    d_90 (um)    Sigma_e (cm^-2)    tau_ball (ps)
5.0e5         3.874e16          2090.5            11.015       4.267e13            39.85
1.0e6         4.842e15          1045.2            22.029       1.067e13            39.85
2.0e6         6.053e14           522.6            44.059       2.667e12            39.85
```

Doubling `v` gives exactly the predicted

```text
8x lower volume carrier density;
2x larger thickness;
4x lower carrier column;
unchanged ballistic crossing time.
```

## Important model correction — generic parabolic comparator is underconstrained

A generic parabolic model with independently adjustable

```text
m_e,
m_h,
p_cv or v_cv
```

cannot support a fundamental comparison because DOS and oscillator strength can be tuned independently by assumption.

If the parabolic bands are instead required to be the low-`k` limit of a self-consistent two-band `k.p` Hamiltonian, their effective mass and optical matrix element are linked by the same velocity `v`; that parabolic model is simply the edge approximation to the massive-Dirac model.

Therefore the intended cross-class comparison is currently

```text
CONDITIONAL:
    a fair parabolic comparator requires multiband k.p / oscillator-strength / sum-rule constraints.
```

## Prior-art status

The 3-D Dirac optical-conductivity ingredients are established, including inverse velocity scaling. A focused search has not yet found a direct statement of the combined

```math
\Sigma_e=n_ed\propto v^{-2}
```

matched-absorptance result together with equivalent-species cancellation and ballistic-transit invariance.

This is **not sufficient to establish novelty**. Broader semiconductor `k.p`, oscillator-strength, infrared-detector, and Dirac-material audits remain mandatory.

## What has actually been established

```text
DERIVED:
    exact finite-gap massive-Dirac carrier density;

DERIVED:
    exact clean-limit interband optical conductivity for the toy model;

DERIVED:
    matched absorptance thermal column Sigma_e ~ v^-2;

DERIVED:
    equivalent Dirac-species degeneracy cancels from Sigma_e;

DERIVED:
    ideal ballistic transit time is independent of v;

NUMERICAL VALIDATION:
    exact 10-um / 300-K witness follows the scaling.
```

## What is not established

```text
massive Dirac global optimality;
real-material tunability or upper range of v;
HgCdTe-relative advantage;
Auger generation scaling;
SRH behavior;
full electrical bandwidth;
detector D* improvement;
novelty.
```

## Single next question

> Once full multiband `k.p` and oscillator-strength constraints are imposed at fixed finite `E_g`, is the Dirac velocity `v` genuinely a free material-design lever, or is there a microscopic upper bound/tradeoff that limits the `Sigma_e ~ v^-2` gain?

**Do not add Auger until this question is resolved or cleanly bounded.**

## Read next

1. `MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`
2. `FOUNDING_GEDANKEN_2026-08-14.md`
3. `PRIOR_BRANCH_BOUNDARY_2026-08-14.md`
4. `PROGRESS_LOG.md`
5. Experiment 08 novelty stop before invoking zero/small-gap Kane asymptotics.
