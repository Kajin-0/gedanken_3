# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 6 — Physical Review Applied flagship; final hostile technical review + 8-page production QA pass; human submission inputs remain**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV6_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV6_RESPONSE_TO_REREVIEW_2026-08-15.md`
5. `experiments/13-observable-resource-unification/CURRENT_STATE.md`
6. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md` — submission guidance; Rev. 4 identifiers inside are historical

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

## Rev. 6 corrections

The Rev. 5 re-review found no theorem-breaking error but identified formal/reproducibility issues. Rev. 6 fixes them:

```text
restores the thermodynamic uniform-capacity condition;
explicitly connects the bounded-domain HgCdTe model to that condition;
restores key HgCdTe parameters, k cutoff, quadrature, support grid, clustering tolerance, and continuous capacity-search details;
states support-rank threshold s > 1e-6 m/s and its 1e-9 to 1e4 m/s stability sweep;
renames optical tau_obs^act -> tau_bound^act so observability is terminal/readout terminology only;
renames the 0.3068 loss the Fermi-statistical factor and states Kubo-Greenwood adds no inequality/slack.
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

Finite-system exact statement. Macroscopic density floor requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

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

HgCdTe broad-window closure:

```text
support fraction   = 0.66897
eta_F              = 0.30684
tau_cap^act        = 0.57262
tau_bound^act      = 0.17570
full ratio         ~= 0.1175
v_B^cap            = 1.01764e6 m/s
```

## Publication architecture — mandatory

The unified flagship substantially inherits Experiment 12's theorem and HgCdTe validation. Therefore:

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

Human/submission inputs:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
submission-history declaration;
final Data Availability / archive decision;
optional ORCID/referee recommendations/exclusions.
```

Before submission, update the old Rev. 4 preflight/cover-letter wording to the Rev. 6 title and terminology, insert human-owned declarations, rebuild through CI, record hashes, and visually inspect all pages.
