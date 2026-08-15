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
4. `experiments/12-oscillator-strength-state-count-bound/JOURNAL_FIT_AND_SUBMISSION_PLAN_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_ADDENDUM_TRK_CONDUCTIVITY_PARTICLE_COUNT_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

Older revisions preserve the development history. Rev6 is controlling.

## Controlling result

For any useful direct cross-`mu` optical window `B`, define the basis-invariant shell optical-velocity capacity `v_B^cap` and optically active thermal support populations `n_{e,B}^act`, `n_{h,B}^act` from exact energy-shell coupling blocks.

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

Intrinsic neutral form:

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

The thermal kernel tends to `2 kBT` at low energy. The theorem constrains integrated spectral weight, not a vanishing-bandwidth peak.

## Equality / checks

```text
equal-mass parabolic model:
  active theorem exact for any selected direct window;
  total theorem exact for full direct spectrum.

2-D massless Dirac: 0.5000
3-D massless Dirac: 0.6667
3-D massive Dirac, 10 um / 300 K: 0.794684
```

## Scope

Valid only as stated for independent-quasiparticle direct cross-`mu` charge absorbers. Do not convert automatically to dark current, generation rate, `D*`, finite-bandwidth noise, excitonic/collective absorption, indirect absorption, many-body spectral functions, or arbitrary photonic enhancement.

## Novelty

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No priority wording is authorized.

## Manuscript / journal state

```text
CURRENT SCIENTIFIC TEXT: MANUSCRIPT_REV6_2026-08-14.md
FIRST TARGET: Physical Review B — Regular Article
FALLBACK: Journal of Applied Physics — Article
```

Final internal hostile QA: PASS at theorem level.

# ACTIVE NEXT ACTION

```text
NO MORE THEORY BY DEFAULT.
```

Convert Rev6 to PRB-compatible LaTeX, perform PRB-specific reference/style QA, compile and visually inspect the PDF, then review the rendered manuscript independently.

## Closed previous branches

- Experiment 10: `experiment-10-room-temperature-lwir-admissibility` — closed by default as novelty/manuscript path.
- Experiment 11: `experiment-11-weighting-capacitance-duality` — closed by default; retained result reduces to Maxwell-relaxation / reciprocal-sensitivity theory.
