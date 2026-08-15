# Active Frontier — Experiment 13 Rev. 7 Flagship

**Date:** 2026-08-15  
**Branch:** `experiment-13-observable-resource-unification`  
**Scope:** analytical/theoretical only  
**Target:** Physical Review Applied — Regular Article  
**Status:** **REV. 7 CONTROLS / FINAL ADVERSARIAL TECHNICAL LOOP CLOSED / 8-PAGE PRODUCTION QA PASS / HUMAN SUBMISSION INPUTS REMAIN**

## Read first

1. `PAPER_REV7_RESPONSE_TO_REREVIEW_2026-08-15.md`
2. `REV7_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
3. `PAPER_REV6_FINAL_HOSTILE_REVIEW_2026-08-15.md`
4. `PRAPPLIED_SUBMISSION_PREFLIGHT_REV6_2026-08-15.md` — submission guidance; update production identifiers to Rev. 7 during metadata insertion
5. `CURRENT_STATE.md`

Rev. 6 and earlier are historical checkpoints. Rev. 7 controls whenever states conflict.

## Controlling production identity

```text
GitHub Actions run:   31912951827
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

## Why Rev. 7 exists

The Rev. 6 adversarial re-review found the technical loop essentially closed but requested three final bounded corrections:

```text
1. thermodynamic convergence/liminf precision;
2. explicit reference dependence of support coverage;
3. restoration of the carrier-cutoff convergence statement for n_ref.
```

Rev. 7 closes all three.

It also performs two low-risk editorial cleanups:

```text
"production-resolution" -> "numerically converged";
remove dangling unknown-arrival transient sentence;
enlarge only the smallest Fig. 1/3/4 annotations.
```

No central scientific result changes.

## Central finite-system theorem — unchanged

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
\bar v_{\mathcal B}^{cap}
=\limsup_{j\to\infty}v_{\mathcal B,V_j}^{cap}<\infty.
```

If ordinary thermodynamic limits of the relevant intensive population and response exist, the same density inequality follows using `bar v_B^cap`. Without those convergence assumptions Rev. 7 now states

```math
\boxed{
\liminf_{j\to\infty}n_{\mathcal B,V_j}^{act}
\ge
\frac{\liminf_{j\to\infty}\mathcal L_{\mathcal B,V_j}}
{(\bar v_{\mathcal B}^{cap})^2}.
}
```

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

Important Rev. 7 qualification:

```text
n_B^act / n_ref is reference-domain dependent.
```

The remaining factors are properties of the selected optical/statistical construction, but support coverage changes if the declared broader reference population changes.

## HgCdTe production closure — unchanged numerically

```text
n_ref                    = 1.0051405e17 cm^-3
n_B^act                  = 6.7241114e16 cm^-3
n_B^act / n_ref          = 0.66897
eta_F                    = 0.30684
tau_cap^act              = 0.57262
tau_bound^act            = 0.17570
v_B^cap                  = 1.01764e6 m/s
bound/reference          ~= 0.1175
```

Newly restored convergence statement:

```text
raising the carrier cutoff from 1.5 to 2.0 nm^-1
changes the cross-mu reference population by < 1%.
```

## Publication architecture — mandatory

```text
Experiment 13 Rev. 7:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

Experiment-12 hold remains:
`../12-oscillator-strength-state-count-bound/00_SUBMISSION_HOLD_EXPERIMENT13_SUPERSESSION_2026-08-15.md`

## Optional BIA calculation

A BIA-inclusive HgCdTe stress test would be scientifically interesting because it would quantify how close the real zincblende system remains to the exact within-shell factor of unity.

It is **not required before submission** under the present claim set. Do not reopen this calculation by default.

## Stop rule

```text
new defensive theory revision: STOP
Rev. 8 by default:            DO NOT CREATE
```

Reopen science only for:

```text
a new mathematical counterexample;
a numerical inconsistency;
a direct prior-art collision;
an explicit editor/referee request.
```

## Human submission inputs still required

```text
author name;
affiliation;
corresponding email;
acknowledgments/funding;
submission-history declaration;
final Data Availability / archive decision;
optional ORCID/referee recommendations/exclusions.
```

After metadata insertion, rebuild through Rev. 7 CI, record new hashes, and visually inspect all pages again.
