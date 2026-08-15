# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All research is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not claim novelty or priority without a dedicated audit.

## Continuity discipline

Important work must not exist only in chat or untracked local artifacts. Commit significant reasoning milestones, manuscript revisions, numerical audits, QA results, and changes of scientific disposition on the active branch. Keep this file and the experiment `CURRENT_STATE.md` synchronized with the controlling manuscript state. Preserve prior revisions and audits rather than silently replacing them.

# ACTIVE — Experiment 12 / Rev10 referee-repaired PRB manuscript

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/numerics/supremum_active_support_audit.py`
5. `experiments/12-oscillator-strength-state-count-bound/typeset/rev9_exposition_to_rev10_referee_repaired.patch`
6. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`
7. `experiments/12-oscillator-strength-state-count-bound/REV9_EXPOSITION_REVISION_QA_2026-08-15.md`
8. `experiments/12-oscillator-strength-state-count-bound/INDEPENDENT_NOVELTY_SIGNIFICANCE_ASSESSMENT_2026-08-15.md`
9. `experiments/12-oscillator-strength-state-count-bound/numerics/kane_8band_tightness.py`
10. `experiments/12-oscillator-strength-state-count-bound/HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`

## Controlling theorem

```math
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

Eq. (29) and its proof are unchanged in Rev10.

## Rev10 repair that must not be lost

A Rev9 adversarial rereview correctly found a formal mismatch: Eqs. (21)–(22) use an ordinary finite-system shell supremum, while the HgCdTe Eq. (49) had been written with `ess sup` in k.

Rev10 repairs Eq. (49) to the ordinary supremum over the bounded k domain. Do **not** revert to `ess sup` unless a separate density theorem is actually proved.

The rereview's proposed isolated-Gamma correction to about 11.0% is rejected for the actual numerical state: `mu` lies 11.477 meV above the nominal Gamma6 edge, so Gamma6 and Gamma8 are all below `mu` at k=0. There is no selected cross-mu Gamma8-to-Gamma6 block at Gamma.

Continuous ordinary-supremum audit:

```text
v_B^cap ~= 1.01764e6 m/s
maximum begins near |k| ~= 0.05535 nm^-1
```

Broad HgCdTe result:

```text
n_ref                      = 1.005141e17 cm^-3
precise bound/reference    ~= 0.1175
headline rounded value     = 0.118 / 11.8%
lower bound                ~= 1.18e16 cm^-3
n_B^act/n_ref              ~= 0.669
n_bound/n_B^act            ~= 0.176
pairwise ordinary sup      ~= 0.87165e6 m/s
pairwise substitution bias ~= +36.3%
```

Eq. (48) now uses the energy image `E_B={hbar omega: omega in B}`. Production quadrature is explicitly `160 x 10 x 16`; `200 x 12 x 20` is an additional support check.

## Rev10 production identity

Exact Rev10 TeX is reconstructed from the archived Rev9 exposition source plus

`typeset/rev9_exposition_to_rev10_referee_repaired.patch`.

```text
Rev10 TeX SHA-256 454a2ff8aba637d2e4c66ef5747899e85894996a020c633296cf950044c79b3d
Rev10 PDF SHA-256 31ec4dd408552318f21de3e6bc7366e1b87badd7721a21575250c73adbb59a54
13 pages / US letter / REVTeX PRB / compile clean / all-page visual QA pass
```

## Scope / novelty

No universal dark-current, `D*`, generation-rate, or finite-bandwidth-noise theorem. Excitons, indirect transitions, interacting many-body spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN TARGETED SEARCH
NOVELTY: PLAUSIBLE
HISTORICAL PRIORITY: NOT ESTABLISHED
```

## Current action

Treat Rev10 as the controlling submission candidate. Next perform a focused adversarial rereview of the repaired ordinary-supremum implementation, active-support decomposition, Eq. (48) unit-domain correction, and possible regression introduced by the surgical edits. Do not reopen unrelated theory by default.