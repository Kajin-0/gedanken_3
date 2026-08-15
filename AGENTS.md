# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active research branch:** `experiment-13-observable-resource-unification`  
**Current repository frontier:** **Experiment 13 Rev. 6 — Physical Review Applied flagship; final hostile technical review and production QA passed**

## Recovery order

Read these first:

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV6_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_REV6_RESPONSE_TO_REREVIEW_2026-08-15.md`
6. `experiments/13-observable-resource-unification/CURRENT_STATE.md`
7. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_2026-08-15.md` — guidance only; its Rev. 4 production identifiers are stale

Rev. 4 and Rev. 5 are preserved development checkpoints. Rev. 6 controls whenever states conflict.

## Controlling production identity

```text
GitHub Actions run:   31905440563
head commit:          1fcd627f194223dbf277cbf9d51b87501b1fcdb6
artifact ID:          9252213152
artifact digest:      38709b3e6f5e6b236812a70b78880c195a4e86d718a62e9b5d1e2bb63e6f7a7b
PDF SHA-256:          fa3c40b73ae8c75b8317e5522ebf50fb5fbf77c099aeeef52cf378a4febcf2e6
TeX SHA-256:          2a4bed7a70098e1e641a59d64d16adfe549fc35d775868e2a6b4ec7b03fa3d74
figure SHA-256:       07ee725da6522c7060c27644852a78977468ba02dd85ba0497e66f820f67b816
builder SHA-256:      fafa390867f6cfe665f2b79647d58837c525c155f6c6f65d277b27d2d9243859
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
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

At finite normalization volume this is exact. Its macroscopic density interpretation requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

The bounded-domain second-order HgCdTe validation supplies that uniform bound within its stated model because its finite-dimensional velocity matrix has a volume-independent operator bound on the compact momentum domain.

## Stage-specific thesis

```text
H_task -> H_exc -> H_int -> H_term
```

Capacity, selectivity, internal correlation, and terminal observability are properties of their own physical stage maps. Do not transfer them between stages without the intervening dynamics.

## Full bound hierarchy

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

`eta_F` is the Fermi-statistical factor; Kubo-Greenwood is exact spectral bookkeeping.

Optical bound tightness is `tau_bound^act`; reserve `observability` for the terminal/readout null-space problem.

## HgCdTe production state

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

Experiment 13 inherits the principal Experiment-12 theorem and HgCdTe validation. Therefore:

```text
Experiment 13 Rev. 6:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

Experiment-12 hold notice:

`experiments/12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`

Any change to this policy requires a fresh publication-overlap audit before submission.

## Reproducible production

```text
build_rev4.py
-> Rev4 built source
-> recorded Rev4->Rev5 patch sequence
-> build_rev6.py
-> rev6_prapplied.tex + rev6_figures.tex
-> REVTeX/BibTeX
-> automated QA + 180-dpi page renders
```

Workflow:
`.github/workflows/rev6-flagship-pdf.yml`

## Final disposition

```text
central theorem:                    PASS
thermodynamic condition:            RESTORED / PASS
HgCdTe uniform-capacity link:       PASS
numerical method disclosure:        PASS
support-rank threshold/stability:   PASS
observability terminology:          FIXED
Fermi/Kubo attribution:             FIXED
publication overlap:                RESOLVED IF SUPERSESSION POLICY MAINTAINED
task/coherence breadth:             MODERATE EDITORIAL RISK ONLY
production PDF:                     PASS
new scientific revision required:   NO
```

## Remaining work

Do not create Rev. 7 or new theory by default.

Human/submission inputs:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
submission-history declaration;
final Data Availability / archival citation decision;
optional ORCID/referee recommendations/exclusions.
```

Before actual submission, update the old Rev. 4 preflight/cover-letter wording to the Rev. 6 title and terminology, insert human-owned declarations, then rebuild and visually inspect the metadata-complete PDF.
