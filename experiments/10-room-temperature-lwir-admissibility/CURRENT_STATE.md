# Current State — Experiment 10: Room-Temperature LWIR Material Admissibility

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** ACTIVE PREMISE / FIRST-PRINCIPLES DERIVATION NOT YET CLOSED / NOVELTY NOT ESTABLISHED / NO MANUSCRIPT YET

## Research question

Can one derive, from first principles, the electronic-structure conditions that a passive LWIR photon-detector absorber must satisfy to operate near 300 K with HgCdTe-class or near-HgCdTe-class sensitivity **without sacrificing useful temporal response**?

The objective is not initially to nominate a known material. The target is a **band-structure admissibility theorem or no-go result**.

## Founding Gedanken experiment

Compare two idealized interband photon detectors:

- `H`: a reference HgCdTe detector;
- `X`: an unknown semiconductor whose electronic dispersion may be chosen subject to physical consistency.

Impose, at minimum,

```math
T=300\ \mathrm{K},
\qquad
\lambda_c=10\ \mu\mathrm{m},
```

with the same detector area, optical environment, accepted etendue, and external absorptance spectrum unless a later step explicitly relaxes one of these constraints.

At `lambda_c = 10 um`,

```math
E_g=\frac{hc}{\lambda_c}\approx 0.12398\ \mathrm{eV}.
```

At 300 K,

```math
k_B T\approx 25.85\ \mathrm{meV},
\qquad
\frac{E_g}{k_B T}\approx 4.80.
```

Thus the central thermal problem is already present before defects are introduced: an LWIR interband gap at room temperature is only a few `k_B T`.

## Initial model hierarchy

Start with the cleanest intrinsic model and add complexity only when forced:

1. passive reciprocal absorber;
2. direct interband detection;
3. no extrinsic SRH centers initially;
4. exact Fermi-Dirac carrier statistics where needed;
5. radiative generation/recombination constrained by optical absorption and detailed balance;
6. intrinsic Auger processes added only after the absorption/carrier-statistics relation is understood;
7. explicit temporal-bandwidth or response-time requirement so the optimum cannot become arbitrarily slow.

## First heuristic — not yet a theorem

For a conventional nondegenerate 3-D parabolic semiconductor,

```math
n_i=\sqrt{N_cN_v}\,e^{-E_g/(2k_BT)},
```

with

```math
N_c\propto g_c(m_e^*T)^{3/2},
\qquad
N_v\propto g_v(m_h^*T)^{3/2}.
```

Therefore, at fixed `E_g` and `T`,

```math
n_i\propto
(g_cg_v)^{1/2}
(m_e^*m_h^*)^{3/4}
T^{3/2}
e^{-E_g/(2k_BT)}.
```

This suggests low DOS masses and low valley degeneracy as favorable. It does **not** establish that these can be reduced independently of optical absorption, matrix elements, Auger phase space, or response time.

Do not extrapolate this parabolic expression toward `E_g -> 0`. Experiment 08 already established the noncommuting-limit failure of that shortcut for Kane systems.

## Candidate finite-gap comparison class

A primary comparator is the isotropic massive-Dirac/Kane form

```math
E_\pm(k)=\pm\sqrt{(E_g/2)^2+(\hbar vk)^2}.
```

Near the band edge,

```math
m_D=\frac{E_g}{2v^2}.
```

The working hypothesis is that large band velocity `v` may simultaneously reduce thermodynamic DOS while retaining strong interband velocity matrix elements and altering Auger phase space.

**This is a hypothesis, not a result and not a claim that the massive-Dirac class is optimal.**

## Detector-quality constraint

Do not optimize scalar `D*` in isolation. Any admissibility result must include a finite temporal requirement, for example

```math
f_{3\mathrm{dB}}\ge f_0
```

or an equivalent task-specific response constraint.

A provisional dimensionless excess-generation quantity is

```math
\Xi_{nr}
=\frac{\Gamma_{nonrad}}
{\Gamma_{rad}+\Gamma_{background}}.
```

The intuitive target `Xi_nr <= 1` means nonradiative internal generation is no larger than the unavoidable radiative/background contribution. This definition is **provisional** until the exact measurement/noise normalization is derived.

## Novelty boundary already known

The following are not available as novelty claims:

- generic `alpha/G_th` detector-material figures of merit;
- generic `alpha sqrt(tau)` detector-material comparison;
- the statement that small intrinsic carrier density is beneficial;
- general radiative detailed-balance limits;
- generic Auger suppression by band-structure engineering;
- the zero-gap Kane carrier-statistics correction from Experiment 08.

The possible surviving contribution must be deeper, for example:

- a general finite-gap band-structure admissibility inequality;
- a no-go theorem for a specified dispersion class;
- an escape condition identifying a dispersion class that can satisfy absorption, thermal-generation, Auger, and bandwidth requirements simultaneously;
- an invariant showing that an apparently favorable DOS/absorption trade cannot actually improve detector SNR under matched optical constraints.

## Immediate next derivation

Use two idealized 3-D two-band absorbers with the same

```text
E_g,
T,
external absorptance target,
optical environment,
and response-time target.
```

Compare:

1. a conventional parabolic two-band dispersion;
2. a finite-gap massive-Dirac dispersion.

Before adding Auger, derive exactly enough of the Fermi-Dirac carrier density and interband absorption to answer one question:

> At fixed finite gap and matched optical absorptance, can the massive-Dirac class reduce the equilibrium carrier population relative to a parabolic absorber, or does optical coupling impose a compensating invariant/tradeoff?

Stop at the first nontrivial consequence. Do not jump directly to a generalized material survey.

## Read next

1. `FOUNDING_GEDANKEN_2026-08-14.md`
2. `PRIOR_BRANCH_BOUNDARY_2026-08-14.md`
3. `PROGRESS_LOG.md`
4. Experiment 08 novelty stop on branch `experiment-08-zero-gap-kane-statistics` before using Kane small-gap asymptotics.

