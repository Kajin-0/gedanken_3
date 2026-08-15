# Agent recovery entrypoint

Read `AGENTS.md` first, then this file. Do not infer chronology from `main` alone.

## Hard scope

All research is analytical/theoretical only. Preserve failed, corrected, conditional, and negative paths. Do not claim novelty or priority without a dedicated audit.

## Continuity discipline

Important work must not exist only in chat or untracked local artifacts. Commit significant reasoning milestones, manuscript revisions, numerical audits, QA results, and changes of scientific disposition on the active branch. Keep this file and the experiment `CURRENT_STATE.md` synchronized with the controlling manuscript state. Preserve prior revisions and audits rather than silently replacing them.

# ACTIVE — Experiment 12 / Rev11 PRB submission candidate

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/PRB_REV11_MINOR_REVISION_QA_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/REV10_MINOR_REREVIEW_RESPONSE_2026-08-15.md`
4. `experiments/12-oscillator-strength-state-count-bound/typeset/rev10_to_rev11_minor_revision.patch`
5. `experiments/12-oscillator-strength-state-count-bound/numerics/parameter_sensitivity_audit.py`
6. `experiments/12-oscillator-strength-state-count-bound/PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
7. `experiments/12-oscillator-strength-state-count-bound/REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
8. `experiments/12-oscillator-strength-state-count-bound/numerics/supremum_active_support_audit.py`
9. `experiments/12-oscillator-strength-state-count-bound/typeset/rev9_exposition_to_rev10_referee_repaired.patch`
10. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`

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

Eq. (29) and its proof remain unchanged through Rev11.

## Rev10 repair that must not be lost

Eqs. (21)–(22) use an ordinary finite-system shell supremum. Rev10 repaired the HgCdTe Eq. (49) from `ess sup` to the ordinary supremum. Do **not** revert to `ess sup` unless a separate density theorem is actually proved.

The isolated-Gamma 11.0% correction is not applicable: `mu` lies 11.477 meV above the nominal Gamma6 edge, so Gamma6 and Gamma8 are all below `mu` at `k=0`; there is no selected cross-mu Gamma8-to-Gamma6 block at Gamma.

## Rev11 clarification that must not be lost

For the translationally invariant bulk model, the complete exact-energy shell decomposes into independent momentum blocks because `v_x` conserves crystal momentum:

```math
P_\epsilon v_xQ_{\epsilon,B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,B}.
```

Hence the complete-shell operator norm is the maximum of the finite-k block norms and becomes the ordinary k supremum in the bulk limit. This directly justifies Eq. (49) as the bulk specialization of Eq. (21).

## Controlling HgCdTe result

```text
n_ref                      = 1.005141e17 cm^-3
v_B^cap ordinary sup       ~= 1.01764e6 m/s
precise bound/reference    ~= 0.1175
headline rounded value     = 0.118 / 11.8%
lower bound                ~= 1.18e16 cm^-3
n_B^act/n_ref              ~= 0.669
n_bound/n_B^act            ~= 0.176
pairwise ordinary sup      ~= 0.87165e6 m/s
pairwise substitution bias ~= +36.3%
selected k onset           ~= 0.05535 nm^-1
selected k max             ~= 0.583 nm^-1
```

Production quadrature: `160 x 10 x 16`; `200 x 12 x 20` is an additional support check.

Active-support diagnostic rank threshold:

```text
1e-6 m/s
```

A reduced-grid sweep from `1e-9` to `1e4 m/s` leaves `n_B^act/n_ref` unchanged to printed precision. This threshold is numerical bookkeeping for Table II only; the central lower bound does not depend on it.

Lightweight one-at-a-time `+/-5%` sensitivity of `EP, Delta, F, gamma1, gamma2, gamma3` on a reduced common grid gives a broad diagnostic ratio range `0.1098 ... 0.1293`, confirming only the order-`10^-1` robustness of the representative model result. Do not present this as experimental uncertainty.

## Literature positioning added in Rev11

Onishi and Fu, Phys. Rev. X 14, 011052 (2024), is now cited and distinguished. Their work relates generalized optical weight, topology/quantum geometry, and topological-gap bounds, including infrared applications. Experiment 12 instead uses a finite-temperature cross-mu thermal kernel and per-shell velocity capacity to bound equilibrium thermal quasiparticle population. Neighboring literature, no identified collision.

## Rev11 production identity

Exact Rev11 source is reconstructed by applying, in order:

1. `typeset/rev9_exposition_to_rev10_referee_repaired.patch`
2. `typeset/rev10_to_rev11_minor_revision.patch`

to the archived Rev9 exposition source.

```text
Rev11 TeX SHA-256 a75b75d6016d335746751b7c75a01d49deea7c4796c2eff30a7dd99c1f73cd68
Rev11 PDF SHA-256 ed5a558ac561cb67f0e918de96f4774c493cacd54fd6f3bea01e597890a7df5d
13 pages / US letter / REVTeX PRB / compile clean / all-page visual QA pass
19 references
```

## Scope / novelty

No universal dark-current, `D*`, generation-rate, or finite-bandwidth-noise theorem. Excitons, indirect transitions, interacting many-body spectral functions, and unconstrained photonic enhancement remain outside scope.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN TARGETED SEARCH
NOVELTY: PLAUSIBLE
HISTORICAL PRIORITY: NOT ESTABLISHED
```

## Current action

Treat Rev11 as the controlling submission candidate. A final adversarial regression check is reasonable, but stop defensive rewriting unless it exposes a concrete mathematical defect, numerical inconsistency, direct prior-art collision, or a specific journal-facing requirement. The latest rereview's remaining risk is ordinary publication significance/editorial judgment rather than an elementary theorem defect.
