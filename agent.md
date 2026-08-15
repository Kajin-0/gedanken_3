# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All active research is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated audit.

# ACTIVE — Experiment 12

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV3_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV3_NOTATION_ERRATUM_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/THEOREM_CORE_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/BASIS_INVARIANT_VELOCITY_RESOURCE_CORRECTION_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV1_ADVERSARIAL_REVIEW_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/NOVELTY_AUDIT_ADDENDUM_LOW_CARRIER_OPTICS_2026-08-14.md`
9. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

## Controlling theorem

For independent quasiparticles and direct transitions crossing the chemical potential, the exact Fermi lemma is

```math
\frac{2[f(E_v)-f(E_c)]}{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
```

For any useful positive-frequency window `B`, let `u_B` be the **Latin-u** basis-invariant optical-velocity resource defined within exact degenerate energy eigenspaces.

Then

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2 u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

Intrinsic neutral form:

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2 u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega.
}
```

The low-energy kernel tends to `2 kBT`, so finite integrated low-energy direct spectral weight has a finite thermal quasiparticle population cost at fixed `u_B`.

## Tightness checks

```text
3-D equal-mass parabolic direct bands: exact saturation at all T
2-D neutral massless Dirac:            bound/exact = 0.5000
3-D massless Dirac:                    bound/exact = 0.6667
3-D massive Dirac, 10 um / 300 K:      bound/exact = 0.794684
```

For unequal parabolic masses in the nondegenerate limit,

```math
n_bound/n_exact
=
[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

## Scope

Valid class: independent-quasiparticle direct cross-`mu` charge absorbers.

Do not extend the theorem automatically to bound excitons, indirect/phonon-assisted transitions, interacting many-body spectral functions, or arbitrary photonic path enhancement.

Do not infer a universal dark-current, generation-rate, D*, or finite-bandwidth-noise floor from the population inequality.

## Manuscript status

`MANUSCRIPT_REV3_2026-08-14.md` is the current manuscript.

It has one mechanical notation regression only: four occurrences render Greek `nu_B` where the intended and defined resource is Latin `u_B`. The exact locations and correction are recorded in:

`MANUSCRIPT_REV3_NOTATION_ERRATUM_2026-08-14.md`

Treat Rev3 + that erratum as the archival manuscript state until the next rendered revision folds in the four substitutions.

```text
NOVELTY NOT ESTABLISHED.
REV3 IS READY FOR ANOTHER INDEPENDENT EXTERNAL-STYLE REVIEW.
```

## Next action

Do not add new physics by default. Fold the notation erratum into the next typeset/journal-facing version, verify bibliography/journal fit, and run another hostile manuscript review.

## Closed previous branches

- Experiment 10: `experiment-10-room-temperature-lwir-admissibility` — closed by default as novelty/manuscript path.
- Experiment 11: `experiment-11-weighting-capacitance-duality` — closed by default; retained result reduces to Maxwell-relaxation / reciprocal-sensitivity theory.
