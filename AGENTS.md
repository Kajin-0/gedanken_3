# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-10-room-temperature-lwir-admissibility`

Before material writes, fetch the live target and exact blob SHA. Preserve failed, corrected, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary research objective — DO NOT LOSE THIS

The purpose of this repository is to generate **genuinely new analytical/theoretical photodetector research from simple Gedanken experiments**.

The goal is not to maximize the number of experiments. A Gedanken experiment is the seed. If one line survives adversarial checking and develops into a technically defensible research paper, the objective has been met for that line.

Use the progression

```text
simple physical question
-> minimal first-principles model
-> first nontrivial consequence
-> strongest comparator / closest prior art
-> kill early if already known or dominated
-> deepen only if it survives
-> theorem / bound / invariant / counterexample / scaling law
-> quantitative thought-experiment witness where useful
-> adversarial novelty and correctness audit
-> manuscript architecture only when justified
-> hostile referee review and revision.
```

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Active research is restricted to first-principles derivations, exact toy models, analytical bounds/no-go theorems, counterexamples, asymptotics, numerical thought experiments supporting theory, analytical comparisons with established architectures, prior-art audits, and theoretical manuscript development.

Do not make fabrication, sample procurement, measurement pilots, instrumentation, annealing, device processing, or laboratory optimization the next research step.

## Recovery order

1. Read this file.
2. Read `agent.md`.
3. Read `experiments/10-room-temperature-lwir-admissibility/CURRENT_STATE.md`.
4. Read `experiments/10-room-temperature-lwir-admissibility/FOUNDING_GEDANKEN_2026-08-14.md`.
5. Read `experiments/10-room-temperature-lwir-admissibility/PRIOR_BRANCH_BOUNDARY_2026-08-14.md`.
6. Read `experiments/10-room-temperature-lwir-admissibility/PROGRESS_LOG.md`.
7. Before using Kane small-gap limits, read the Experiment-08 novelty stop on branch `experiment-08-zero-gap-kane-statistics`.

Do not infer chronology from `main` alone; later experiments live on divergent branches.

## Important lineage boundary

Experiment 09 remains a separate paper line on branch

```text
experiment-09-coherence-selective-photodetection
```

and was the parent of this branch. Do not rewrite or silently absorb its theorem into Experiment 10.

Experiment 08 is also directly relevant because it already closed the zero-gap Kane carrier-statistics novelty path. Experiment 10 must not rediscover that work under a room-temperature label.

## Active frontier — Experiment 10

Founding question:

> What electronic dispersion and matrix-element structure must an LWIR absorber possess to operate near 300 K with HgCdTe-class or near-HgCdTe-class intrinsic detector quality while retaining useful temporal response?

Start with

```math
T=300\ \mathrm K,
\qquad
\lambda_c=10\ \mu\mathrm m,
\qquad
E_g\approx0.12398\ \mathrm{eV},
\qquad
E_g/(k_BT)\approx4.80.
```

The target is **not** a materials ranking and **not** a new scalar figure of merit. The target is a finite-gap **band-structure admissibility theorem, no-go theorem, invariant, or escape condition**.

Initially compare two matched passive interband absorbers:

```text
A. conventional parabolic two-band dispersion;
B. finite-gap massive-Dirac/Kane dispersion.
```

Match cutoff, temperature, area, optical etendue, optical environment, external absorptance target, and a finite response-time/bandwidth requirement.

The first hard question is:

> At fixed finite gap and matched useful absorptance, can the massive-Dirac class reduce equilibrium carrier population relative to a parabolic absorber without an exact compensating optical cost?

Derive the first nontrivial consequence before adding Auger.

## Novelty-first discipline specific to Experiment 10

Do not claim novelty for:

- `alpha/G_th` or `alpha sqrt(tau)` material figures of merit;
- low intrinsic carrier density as a generic design principle;
- radiative detailed balance;
- generic Auger suppression by band engineering;
- T2SL or quantum-well Auger engineering in general;
- Experiment-08 zero-gap Kane statistics.

The branch survives only if it yields something more primitive and constraining, e.g. a joint relation derived from the electronic structure itself rather than treating absorption and thermal generation as independent phenomenological inputs.

## Manuscript gate

Do not begin a paper merely because the premise is attractive. Manuscript architecture becomes justified only after the branch has:

- a sharply stated theorem/bound/invariant or equally strong analytical result;
- an exact claim boundary;
- a serious closest-prior-art audit;
- at least one quantitative witness when useful;
- a clear explanation of why the result is not reducible to established `alpha/G`, detailed-balance, Kane-statistics, or Auger-engineering theory.
