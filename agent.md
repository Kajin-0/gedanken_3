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

Rev11 remains the last fully typeset and QA-passed manuscript. A final independent regression audit has now been completed and found no central theorem defect or HgCdTe numerical inconsistency. It identified one concrete pre-submission literature-completeness amendment: cite and distinguish Mao, Mendez-Valderrama, and Chowdhury, Phys. Rev. B 112, 075116 (2025), on projected low-energy optical sum rules.

A candidate literature patch is committed, but it is **not yet a new QA-passed revision**. Do not call it Rev12 or submission-ready until the exact Rev11 source is reconstructed, the patch is applied, and compile/hash/all-page QA is complete.

## Recovery order

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/REV11_FINAL_ADVERSARIAL_REGRESSION_AUDIT_2026-08-15.md`
3. `experiments/12-oscillator-strength-state-count-bound/typeset/rev11_literature_completeness_candidate.patch`
4. `experiments/12-oscillator-strength-state-count-bound/PRB_REV11_MINOR_REVISION_QA_2026-08-15.md`
5. `experiments/12-oscillator-strength-state-count-bound/REV10_MINOR_REREVIEW_RESPONSE_2026-08-15.md`
6. `experiments/12-oscillator-strength-state-count-bound/typeset/rev10_to_rev11_minor_revision.patch`
7. `experiments/12-oscillator-strength-state-count-bound/numerics/parameter_sensitivity_audit.py`
8. `experiments/12-oscillator-strength-state-count-bound/PRB_REV10_REFEREE_REPAIR_QA_2026-08-15.md`
9. `experiments/12-oscillator-strength-state-count-bound/REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`
10. `experiments/12-oscillator-strength-state-count-bound/numerics/supremum_active_support_audit.py`
11. `experiments/12-oscillator-strength-state-count-bound/typeset/rev9_exposition_to_rev10_referee_repaired.patch`
12. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`

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

Eq. (29) and its proof remain unchanged through Rev11 and survived the final regression audit.

## Repairs that must not be lost

- Eq. (49) is an ordinary supremum, not an essential supremum.
- The isolated-Gamma correction is inapplicable because `mu` is 11.477 meV above the nominal Gamma6 edge and the selected cross-mu set begins only at finite `k`.
- For the translationally invariant bulk model,

```math
P_\epsilon v_xQ_{\epsilon,B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,B},
```

so the complete-shell operator norm is the maximum finite-k block norm and becomes the ordinary bulk `k` supremum.
- The exact theorem uses exact support rank. `1e-6 m/s` is only the numerical Table-II diagnostic threshold.

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

Production quadrature is `160 x 10 x 16`; `200 x 12 x 20` is a support check. The reduced one-at-a-time `+/-5%` parameter diagnostic spans `0.1098 ... 0.1293` and is not an uncertainty interval.

## Final regression-audit result

The following all passed independent re-derivation/regression checking:

```text
pointwise Fermi lemma;
Kubo-Greenwood prefactor and thermal-kernel conversion;
projected-shell singular-value/rank step;
active-population <= total-population step;
fixed-window thermodynamic hypothesis;
moving-window low-energy quantifiers;
Rev11 complete-shell -> k-block ordinary-supremum specialization;
HgCdTe cross-mu versus conventional population interpretation;
forbidden downstream dark-current/D*/noise inferences.
```

The HgCdTe ordinary supremum is a numerical global-optimization result, not an interval-certified mathematical maximum. This is acceptable at the manuscript's stated numerical-validation claim level. If a referee demands stronger certification, multi-seed replication or deterministic/interval bracketing is the next numerical check.

## Literature amendment

Rev11 already cites Onishi-Fu (PRX 14, 011052 (2024)). The final audit additionally identified:

```text
D. Mao, J. F. Mendez-Valderrama, D. Chowdhury,
Phys. Rev. B 112, 075116 (2025),
DOI 10.1103/xmz7-jgl6.
```

Their projected low-energy/inverse-frequency optical sum and finite-temperature geometry/QFI discussion are methodologically close enough that omission is avoidable referee risk. They do not state Eq. (29): the target quantity, kernel, many-body scope, and per-shell state-count construction differ.

Candidate patch:

`typeset/rev11_literature_completeness_candidate.patch`

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

Reconstruct exact Rev11 TeX, apply the literature-completeness candidate patch, compile and run the same QA, then record the amended TeX/PDF hashes and bibliography count. If that passes, stop defensive rewriting absent a new concrete mathematical defect, numerical inconsistency, direct prior-art collision, or specific journal requirement.
