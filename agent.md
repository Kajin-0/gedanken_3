# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 6 — Physical Review Applied flagship; final hostile technical review + 8-page production QA pass; human submission inputs remain**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV6_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV6_RESPONSE_TO_REREVIEW_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md`
6. `experiments/13-observable-resource-unification/CURRENT_STATE.md`

Rev. 4 and Rev. 5 are historical checkpoints. Rev. 6 controls.

## Controlling production identity

```text
Actions run:          31905440563
head commit:          1fcd627f194223dbf277cbf9d51b87501b1fcdb6
artifact ID:          9252213152
artifact digest:      38709b3e6f5e6b236812a70b78880c195a4e86d718a62e9b5d1e2bb63e6f7a7b
PDF SHA-256:          fa3c40b73ae8c75b8317e5522ebf50fb5fbf77c099aeeef52cf378a4febcf2e6
TeX SHA-256:          2a4bed7a70098e1e641a59d64d16adfe549fc35d775868e2a6b4ec7b03fa3d74
pages:                8
undefined refs/cites: none
overfull/underfull:   none
visual QA:            PASS
hostile review:       PASS
```

## Central theorem

```math
\boxed{
 n_e+n_h
 \ge n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
 \ge
 \frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
 \int_{\mathcal B}
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
```

At finite normalization volume this is exact. A macroscopic density floor requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

The bounded-domain second-order HgCdTe validation satisfies this within its stated model because the finite-dimensional velocity matrix has a volume-independent operator bound on the compact momentum domain.

## Full tightness hierarchy

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

`eta_F` is the **Fermi-statistical factor**. Kubo-Greenwood is exact spectral bookkeeping and does not introduce additional inequality/slack.

Optical bound tightness is `tau_bound^act`; reserve `observability` for terminal/readout null spaces.

## HgCdTe broad-window closure

```text
support fraction       = 0.66897
eta_F                  = 0.30684
tau_cap^act            = 0.57262
tau_bound^act          = 0.17570
full bound/reference   ~= 0.1175
v_B^cap                = 1.01764e6 m/s
production quadrature  = 160 x 10 x 16
support check          = 200 x 12 x 20
rank threshold         = 1e-6 m/s
rank audit             = 1e-9 through 1e4 m/s, stable to printed precision
```

## Publication architecture — mandatory

```text
Experiment 13 Rev. 6:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

Experiment-12 hold:
`experiments/12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`

If this supersession policy is changed, publication overlap must be re-audited before any submission.

## Remaining work

Do not create Rev. 7 or reopen theory by default.

The Rev. 6 submission preflight is complete in `PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md`. Human inputs still required:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
conflicts/disclosures as applicable;
truthful submission-history declaration;
final Data Availability / persistent-archive decision;
optional ORCID/referee recommendations/exclusions.
```

After inserting those human-owned fields, rebuild through CI, record the final hashes, and visually inspect every page before submission.
