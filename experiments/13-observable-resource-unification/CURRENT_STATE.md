# Current State — Experiment 13: Stage-Specific Spectral Geometry of Photodetection

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 7 CONTROLS / FINAL ADVERSARIAL TECHNICAL LOOP CLOSED / 8-PAGE PRODUCTION QA PASS / REV7 SUBMISSION PREFLIGHT COMPLETE / HUMAN INPUTS REMAIN**

## Read first

1. `00_ACTIVE_FRONTIER_REV7_FLAGSHIP_2026-08-15.md`
2. `PAPER_REV7_RESPONSE_TO_REREVIEW_2026-08-15.md`
3. `REV7_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md` — review that motivated the bounded Rev. 7 polish
5. `PRAPPLIED_SUBMISSION_PREFLIGHT_REV7_2026-08-15.md`

Rev. 7 supersedes Rev. 6 for submission. Earlier revisions are reproducible history.

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

## Central theorem — unchanged

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

Exact finite-system statement. Macroscopic density interpretation requires

```math
\bar v_{\mathcal B}^{cap}=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

Rev. 7 adds the fully explicit nonconvergent fallback

```math
\boxed{
\liminf_{j\to\infty}n_{\mathcal B,V_j}^{act}
\ge
\frac{\liminf_{j\to\infty}\mathcal L_{\mathcal B,V_j}}
{(\bar v_{\mathcal B}^{cap})^2}.
}
```

If the relevant intensive population and response have ordinary thermodynamic limits, the simpler density inequality follows.

The bounded-domain HgCdTe model satisfies the uniform-capacity hypothesis within the model because the finite-dimensional velocity matrix is bounded on the compact momentum domain by a volume-independent microscopic operator norm.

## Full tightness hierarchy — unchanged

```math
\boxed{
\frac{n_{bound}}{n_{ref}}
=
\frac{n_{\mathcal B}^{act}}{n_{ref}}
\eta_F
\sum_a w_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

Rev. 7 clarification:

```text
n_B^act / n_ref is reference-domain dependent.
```

It changes if the declared reference population changes; unlike `eta_F`, `c_a`, and `S_a^act`, it is not determined by the selected optical map alone.

`eta_F` is the Fermi-statistical factor. Kubo-Greenwood is exact spectral bookkeeping. Optical bound tightness is `tau_bound^act`; reserve `observability` for terminal/readout null spaces.

## HgCdTe production state — numerical values unchanged

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

The abstract now says `numerically converged second-order eight-band HgCdTe calculation`, not `production-resolution`, to distinguish numerical convergence from full physical realism. Explicit BIA remains omitted; the exact shell-isotropy claim remains limited accordingly.

## Publication architecture — mandatory

```text
Experiment 13 Rev. 7:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 PRB paper:  FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

Experiment-12 hold:
`../12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`

The overlap issue becomes potentially blocking only if this supersession policy is changed.

## Final review disposition

```text
central theorem:                       PASS / UNCHANGED
thermodynamic liminf precision:        FIXED
support-coverage reference dependence: FIXED
carrier-cutoff convergence statement:  RESTORED
HgCdTe numerical closure:              PASS
support-rank threshold/stability:      PASS
PT single-parent qualification:        PASS
recycling Markov spectrum:             PASS
final-sink Poisson cancellation:       PASS
Shockley-Ramo result:                   PASS
publication overlap:                   RESOLVED UNDER SUPERSESSION POLICY
generic task subsection:               EDITORIAL COMPRESSION TARGET ONLY
figure readability:                    IMPROVED
production PDF:                        PASS
new scientific revision required:      NO
```

## Stop rule

Do not create Rev. 8 or reopen theory for defensive polish by default.

A BIA-inclusive stress test is scientifically interesting but explicitly nonblocking under the present claim set.

Reopen science only for a concrete mathematical counterexample, numerical inconsistency, direct prior-art collision, or explicit editor/referee request.

## Submission layer

`PRAPPLIED_SUBMISSION_PREFLIGHT_REV7_2026-08-15.md` contains the current title, production identity, approximately 100-word suitability statement, Rev. 7 cover-letter draft, supersession guidance, Data Availability/archive guidance, source package, closed-science list, and human completion checklist.

## Remaining work

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

After those are supplied, make metadata-only edits on top of Rev. 7, rebuild through CI, record final hashes, visually inspect every page, and verify that the submitted source compiles to the submitted PDF.
