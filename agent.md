# Agent Handoff — Gedanken 3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 7 — Physical Review Applied flagship; final adversarial technical loop closed; 8-page production QA pass; human submission inputs remain**

## Read first

1. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV7_FLAGSHIP_2026-08-15.md`
2. `experiments/13-observable-resource-unification/PAPER_REV7_RESPONSE_TO_REREVIEW_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV7_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
5. `experiments/13-observable-resource-unification/CURRENT_STATE.md`
6. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md` — submission-layer guidance; update identifiers to Rev. 7 during metadata insertion

Rev. 6 and earlier are historical checkpoints. Rev. 7 controls.

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

This is exact at finite normalization volume.

Macroscopic density interpretation requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

Rev. 7 adds the precise nonconvergent fallback

```math
\liminf_{j\to\infty}n_{\mathcal B,V_j}^{act}
\ge
\frac{\liminf_{j\to\infty}\mathcal L_{\mathcal B,V_j}}
{(\bar v_{\mathcal B}^{cap})^2}.
```

If ordinary thermodynamic limits of the relevant intensive quantities exist, the simpler density theorem follows.

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

Important Rev. 7 qualification:

```text
support coverage = n_B^act / n_ref is reference-domain dependent.
```

`eta_F` is the Fermi-statistical factor. Kubo-Greenwood is exact bookkeeping. `tau_bound^act` is optical bound tightness; reserve `observability` for the terminal map.

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
carrier-cutoff check   = 1.5 -> 2.0 nm^-1 changes n_ref by <1%
```

Abstract now says `numerically converged second-order eight-band HgCdTe calculation`; do not revert to `production-resolution`.

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

If this supersession policy changes, publication overlap must be re-audited before any submission.

## Stop rule

Do not create Rev. 8 or reopen theory by default.

The final Rev. 6 re-review found no new theorem, normalization, degeneracy, HgCdTe, recycling, Poisson, or Shockley-Ramo defect. Rev. 7 closed its three remaining bounded technical suggestions.

A BIA-inclusive HgCdTe stress test is optional scientific follow-up, not a pre-submission requirement under the current claim set.

## Remaining work

Human/submission inputs:

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

After inserting those human-owned fields, update the submission preflight production identity to Rev. 7, rebuild through Rev. 7 CI, record final hashes, and visually inspect every page before submission.
