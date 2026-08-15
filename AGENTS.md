# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 7 — Physical Review Applied flagship; final adversarial technical loop closed and 8-page production QA passed**

## Recovery order

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV7_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV7_RESPONSE_TO_REREVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/REV7_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
6. `experiments/13-observable-resource-unification/CURRENT_STATE.md`
7. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md` — submission guidance; production identifiers must be advanced to Rev. 7 during final metadata insertion

Rev. 6 and earlier are historical development checkpoints. Rev. 7 controls whenever states conflict.

## Controlling production identity

```text
Actions run:          31912951827
head commit:          f464dc966e0223f6b8c3ff1e51f82f948c8e950c
artifact ID:          9254179157
artifact digest:      29072be047b7a8174404ba02f32de1615c45c06daebcd5627b9f5cda54339d56
PDF SHA-256:          e40627dfb12f122cafb013415a475efffabda02befbff757ebd80b2da993da50
TeX SHA-256:          806ebffeb398a892550c62b9bcb7bcfa0c85c75a9c349add6f0ad628103ac5d6
figure SHA-256:       e60d35acc894ca5317d4ca5b8dce1b7b8869cfa62ca0cb6475181cfb5728d0c6
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
```

## Scientific state

Central finite-system theorem:

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

Rev. 7 formal fallback when ordinary intensive thermodynamic limits are not assumed:

```math
\liminf_{j\to\infty}n_{\mathcal B,V_j}^{act}
\ge
\frac{\liminf_{j\to\infty}\mathcal L_{\mathcal B,V_j}}
{(\bar v_{\mathcal B}^{cap})^2}.
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

Rev. 7 explicitly states that `n_B^act/n_ref` is reference-domain dependent. `eta_F` is the Fermi-statistical factor; Kubo-Greenwood is exact spectral bookkeeping. Optical bound tightness is `tau_bound^act`; `observability` is reserved for terminal/readout null spaces.

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
carrier-cutoff check   = 1.5 -> 2.0 nm^-1 changes n_ref by <1%
```

The abstract uses `numerically converged` for the HgCdTe calculation. Explicit BIA remains omitted, so do not generalize the exact shell-isotropy result beyond the stated BIA-neglecting single-parent-doublet validation.

## Publication architecture — mandatory

```text
Experiment 13 Rev. 7:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
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
-> build_rev7.py
-> rev7_prapplied.tex + rev7_figures.tex
-> REVTeX/BibTeX
-> automated QA + 180-dpi page renders
```

Workflow:
`.github/workflows/rev7-flagship-pdf.yml`

## Why Rev. 7 exists

The final Rev. 6 hostile re-review found the central manuscript technically sound and requested only:

```text
thermodynamic convergence/liminf precision;
reference-domain qualification of support coverage;
carrier-cutoff convergence statement for n_ref.
```

Rev. 7 closes those points, removes the dangling unknown-arrival sentence, changes `production-resolution` to `numerically converged`, and enlarges only the smallest figure annotations.

No production numerical value or central theorem changed.

## Stop rule

Do not create Rev. 8 or new theory by default.

A BIA-inclusive stress test is optional scientific follow-up, not a submission prerequisite under the current claim set.

Reopen science only for a concrete mathematical counterexample, numerical inconsistency, direct prior-art collision, or explicit editor/referee request.

## Remaining work

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

After metadata insertion, update the submission preflight identifiers to Rev. 7, rebuild through Rev. 7 CI, record final hashes, inspect every page, and verify that the submitted source compiles to the submitted PDF.
