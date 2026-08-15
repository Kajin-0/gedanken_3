# Current State — Experiment 13: Stage-Specific Spectral Geometry of Photodetection

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 6 CONTROLS / FINAL HOSTILE TECHNICAL REVIEW PASS / 8-PAGE PRODUCTION QA PASS / REV6 SUBMISSION PREFLIGHT COMPLETE / HUMAN INPUTS REMAIN**

## Read first

1. `00_ACTIVE_FRONTIER_REV6_FLAGSHIP_2026-08-15.md`
2. `PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
3. `REV6_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `PAPER_REV6_RESPONSE_TO_REREVIEW_2026-08-15.md`
5. `PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md`

Rev. 6 supersedes Rev. 5 for submission. Rev. 4 and Rev. 5 are preserved as reproducible history.

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

Finite-system exact statement. Macroscopic density floor requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

The bounded-domain HgCdTe model satisfies this within the model because the finite-dimensional velocity matrix is bounded on the compact momentum domain by a volume-independent microscopic operator norm.

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

`eta_F` is the **Fermi-statistical factor**; Kubo-Greenwood is exact spectral bookkeeping. The optical tightness quantity is `tau_bound^act`; reserve `observability` for the terminal/readout stage.

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
rank audit             = 1e-9 through 1e4 m/s, support fraction stable to printed precision
```

## Publication architecture

```text
Experiment 13 Rev. 6:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 PRB paper:  FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

Experiment-12 hold:
`../12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`

## Final review disposition

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

## Submission layer

`PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md` now contains:

```text
current Rev. 6 title and production identity;
100-word suitability justification;
updated Rev. 6 cover-letter draft;
publication-overlap/supersession guidance;
Data Availability/archive guidance;
current APS source-package instructions;
human completion checklist.
```

## Remaining work

Do not create Rev. 7 by default.

Human/submission inputs still required:

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
conflicts/disclosures as applicable;
truthful submission-history declaration;
final Data Availability / persistent-archive decision;
optional ORCID and referee recommendations/exclusions.
```

After those are supplied, make metadata-only edits, rebuild through CI, record final hashes, visually inspect every page, and verify that the submitted source compiles to the submitted PDF.
