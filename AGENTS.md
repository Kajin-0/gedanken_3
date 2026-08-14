# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch the live target and exact blob SHA. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary research objective

Generate genuinely new **analytical/theoretical photodetector research** from simple Gedanken experiments.

The intended progression is

```text
simple physical question
-> minimal first-principles model
-> first nontrivial consequence
-> strongest comparator / closest prior art
-> kill early if already known or dominated
-> deepen only if it survives
-> theorem / bound / invariant / counterexample / scaling law
-> quantitative thought-experiment witness
-> adversarial novelty/correctness audit
-> manuscript architecture only when justified.
```

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work includes first-principles derivations, exact toy models, bounds/no-go theorems, asymptotics, numerical thought experiments supporting theory, analytical comparison with established architectures, and prior-art audits.

Do not make fabrication, sample procurement, measurement, instrumentation, or laboratory optimization the next step.

## Recovery order

1. Read this file.
2. Read `agent.md`.
3. Read `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`.
4. Read `experiments/10-room-temperature-lwir-admissibility/MATCHED_DIRAC_ABSORPTION_DOS_STEP_2026-08-14.md`.
5. Read `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`.
6. Read the founding and prior-branch-boundary files only as needed for history.
7. Before invoking zero/small-gap Kane limits, read Experiment 08's novelty stop on branch `experiment-08-zero-gap-kane-statistics`.

Do not infer chronology from `main`; later experiments live on divergent branches.

## Active frontier — Experiment 10

Target:

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

> What electronic structure must a passive LWIR interband absorber possess to approach HgCdTe-class room-temperature detector quality without sacrificing useful temporal response?

The target is a **finite-gap band-structure admissibility theorem, no-go theorem, invariant, or escape condition**, not a materials ranking and not a new scalar figure of merit.

## First hard derivation — CLOSED

Use the intrinsic isotropic 3-D massive-Dirac model

```math
H=\hbar v\tau_x\boldsymbol\sigma\cdot\mathbf k+\Delta\tau_z,
\qquad
\Delta=E_g/2.
```

With `N_D` equivalent Dirac species, exact finite-gap statistics give

```math
\boxed{
n_e
=\frac{N_D}{\pi^2}
\left(\frac{k_BT}{\hbar v}\right)^3F_2(\Delta/k_BT)
}
```

so

```math
n_e\propto N_Dv^{-3}.
```

The clean-limit interband optical conductivity gives

```math
\alpha\propto N_Dv^{-1}
```

at fixed `E_g,T` and normalized photon energy.

For matched single-pass absorptance,

```math
d\propto v/N_D.
```

Therefore the equilibrium electron column per detector area obeys

```math
\boxed{
\Sigma_e=n_ed\propto v^{-2},
\qquad
\Sigma_e\text{ independent of }N_D.
}
```

This is the controlling first result:

```text
within the ideal massive-Dirac family,
low DOS is NOT exactly canceled by reduced absorption.
```

Equivalent species/valley degeneracy cancels from the matched-absorptance thermal carrier column in this restricted model.

For photocarrier group velocity

```math
u_\omega=v\sqrt{1-r^{-2}},
\qquad
r=\hbar\omega/E_g,
```

and `d~v`, the ideal ballistic crossing time is

```math
\boxed{\tau_ball\propto v^0.}
```

Thus the simplest absorption-versus-ballistic-speed tradeoff does not erase the `v^-2` advantage.

## Important finite-gap correction

At the actual 10-um / 300-K target, the exact massive-Dirac carrier density is

```math
\boxed{n_e^{Dirac}/n_e^{edge-parabolic}\approx1.8644.}
```

Do not revert to the simple edge-parabolic density formula for quantitative work at this target.

## Comparator correction

The originally proposed generic parabolic-vs-Dirac comparison is not yet fundamental.

A generic parabolic model with independent

```text
m_e,
m_h,
p_cv or v_cv
```

is underconstrained. If made self-consistent through a two-band `k.p` Hamiltonian, the parabolic edge model is just the low-`k` expansion of the same massive-Dirac model.

Therefore the cross-class comparison is currently

```text
CONDITIONAL:
    full multiband k.p / oscillator-strength / sum-rule constraints are required.
```

## Numerical witness

For

```text
r=1.2,
n_b=3.5,
N_D=1,
A=0.90,
```

changing

```text
v: 1e6 -> 2e6 m/s
```

gives

```text
8x lower bulk thermal carrier density;
2x thicker absorber;
4x lower thermal carrier column;
unchanged ideal ballistic crossing time (~39.85 ps in the chosen witness).
```

## Novelty status

Established territory includes:

```text
3-D Dirac optical conductivity and inverse-v scaling;
Kane optical physics;
alpha/G_th and alpha*sqrt(tau) material figures of merit;
generic low-ni arguments;
radiative detailed balance;
generic Auger suppression by band engineering;
Experiment-08 zero-gap Kane statistics.
```

A focused search did not find a direct statement of the complete matched-absorptance

```math
\Sigma_e\propto v^{-2}
```

result together with equivalent-species cancellation and ballistic-transit invariance.

Disposition:

```text
POSSIBLE USEFUL SYNTHESIS / NOVELTY NOT ESTABLISHED.
```

Do not promote it further without a broader audit.

## Single next question

> Once full multiband `k.p` and oscillator-strength constraints are imposed at fixed finite `E_g`, is `v` genuinely a free material-design lever, or is there a microscopic upper bound/tradeoff that limits the `Sigma_e ~ v^-2` gain?

**Do not add Auger until this question is resolved or cleanly bounded.**
