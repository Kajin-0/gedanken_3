# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All research in this repo is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE — Experiment 12

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV4_EXTERNAL_STYLE_REVIEW_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_ADDENDUM_TRK_CONDUCTIVITY_PARTICLE_COUNT_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

Older manuscript revisions preserve the development path. Rev6 is controlling.

## Controlling theorem

For independent quasiparticles and direct transitions crossing `mu`,

```math
\frac{2[f(E_v)-f(E_c)]}
{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
```

For any useful positive-frequency window `B`, define exact shell coupling blocks `A_{epsilon_c,B}`, `B_{epsilon_v,B}` and

```math
(v_B^{cap})^2
=\max[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2].
```

Define active thermal support populations

```math
n_{e,B}^{act}
=V^{-1}\sum_{\epsilon_c>\mu}f(\epsilon_c)
\operatorname{rank}A_{\epsilon_c,B},
```

```math
n_{h,B}^{act}
=V^{-1}\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]
\operatorname{rank}B_{\epsilon_v,B}.
```

Then

```math
\boxed{
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

For intrinsic neutrality,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

The low-energy kernel tends to `2 kBT`, so finite integrated low-energy direct spectral weight carries a finite thermal quasiparticle state-count cost at fixed `v_B^{cap}`.

`n_B^act` is a support-dimension count, not an oscillator-strength-weighted participation ratio.

## Equality / validation

```text
equal-mass parabolic model:
  active theorem saturates for any selected direct window;
  total theorem saturates for the full direct spectrum.

2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac,
10 um / 300 K:              0.794684
```

For unequal parabolic masses in the nondegenerate global limit,

```math
n_bound/n_exact
=[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

## Scope

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not extend automatically to:

```text
bound excitons / neutral collective states;
phonon-assisted indirect transitions;
interaction-generated many-body spectral functions;
unconstrained photonic path enhancement.
```

Do not infer universal dark current, thermal generation, `D*`, or finite-bandwidth noise from the state-count theorem.

## Novelty

The audit now includes phase-space filling, `f`/TRK sum rules, quantum-geometric optical sums, classic IR `alpha/G_th`, Yablonovitch-Kane low-carrier laser engineering, and Bethkenhagen et al. conductivity-to-ionization TRK counting.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first` or priority wording is authorized.

## Current manuscript state

```text
MANUSCRIPT_REV6_2026-08-14.md
```

Final internal hostile QA: theorem-level PASS.

```text
NO MORE THEORY BY DEFAULT.
```

## Next action

Select journal, audit journal-specific scope/reference style, typeset Rev6, then independently review the rendered manuscript. Add new physics only if a referee identifies a blocking gap.

## Closed previous branches

- Experiment 10: `experiment-10-room-temperature-lwir-admissibility` — closed by default as novelty/manuscript path.
- Experiment 11: `experiment-11-weighting-capacitance-duality` — closed by default; retained result reduces to Maxwell-relaxation / reciprocal-sensitivity theory.
