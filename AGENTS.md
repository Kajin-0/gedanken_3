# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 6 — Physical Review Applied flagship; final hostile technical review and 8-page production QA passed**

## Recovery order

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV6_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_REV6_RESPONSE_TO_REREVIEW_2026-08-15.md`
6. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md`
7. `experiments/13-observable-resource-unification/CURRENT_STATE.md`

Rev. 4 and Rev. 5 are historical development checkpoints. Rev. 6 controls whenever states conflict.

## Controlling production identity

```text
Actions run:          31905440563
head commit:          1fcd627f194223dbf277cbf9d51b87501b1fcdb6
artifact ID:          9252213152
artifact digest:      38709b3e6f5e6b236812a70b78880c195a4e86d718a62e9b5d1e2bb63e6f7a7b
PDF SHA-256:          fa3c40b73ae8c75b8317e5522ebf50fb5fbf77c099aeeef52cf378a4febcf2e6
TeX SHA-256:          2a4bed7a70098e1e641a59d64d16adfe549fc35d775868e2a6b4ec7b03fa3d74
figure SHA-256:       07ee725da6522c7060c27644852a78977468ba02dd85ba0497e66f820f67b816
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
hostile review:       PASS
```

## Scientific state

Central theorem:

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

Macroscopic density interpretation requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

Full tightness hierarchy:

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

`eta_F` is the Fermi-statistical factor. Kubo-Greenwood is exact spectral bookkeeping. Optical bound tightness is `tau_bound^act`; `observability` is reserved for terminal/readout null spaces.

HgCdTe broad-window closure:

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

Any change to the supersession policy requires a fresh overlap audit before submission.

## Reproducible production

```text
build_rev4.py
-> recorded Rev4-to-Rev5 patches
-> build_rev6.py
-> rev6_prapplied.tex + rev6_figures.tex
-> REVTeX/BibTeX
-> automated QA + 180-dpi page renders
```

Workflow:
`.github/workflows/rev6-flagship-pdf.yml`

## Remaining work

Do not create Rev. 7 or new theory by default.

The manuscript-specific APS submission layer is now current in:
`experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md`.

Human-owned fields still required:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
conflicts/disclosures as applicable;
truthful submission-history declaration;
final Data Availability / persistent archive decision;
optional ORCID/referee recommendations/exclusions.
```

After metadata insertion, rebuild through CI, record final hashes, inspect every page, and verify that the submitted source compiles to the submitted PDF.
