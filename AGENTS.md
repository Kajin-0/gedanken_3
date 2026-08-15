# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active research branch:** `experiment-13-observable-resource-unification`  
**Current repository frontier:** **Experiment 13 unified flagship Rev. 4 — science frozen; Physical Review Applied production PDF QA-passed; human metadata required**

## Recovery order

Read these first, in order:

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV4_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/REV4_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
4. `experiments/13-observable-resource-unification/PAPER_REV4_RENDERED_HOSTILE_REVIEW_2026-08-15.md`
5. `experiments/13-observable-resource-unification/PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`
6. `experiments/13-observable-resource-unification/PAPER_REV4_REFERENCE_QA_2026-08-15.md`
7. `experiments/13-observable-resource-unification/PAPER_REV4_FINAL_HOSTILE_CLAIM_REFERENCE_REVIEW_2026-08-15.md`
8. `experiments/13-observable-resource-unification/HGCDTE_STABLE_RANK_PRODUCTION_QA_2026-08-15.md`
9. `experiments/13-observable-resource-unification/HGCDTE_PT_SYMMETRY_STABLE_RANK_EXPLANATION_2026-08-15.md`

Older Experiment-13 notes are derivation history. If they conflict with the recovery order above, the newer files control.

## Strategic state

The unified manuscript has passed:

```text
scientific-unity review;
multiple hostile manuscript reviews;
production-resolution HgCdTe decomposition QA;
model-symmetry audit;
extreme novelty/significance review;
reference-network audit;
claim/reference freeze review;
REVTeX production compile;
all-page rendered visual QA;
rendered hostile manuscript review.
```

```text
FLAGSHIP-FIRST STRATEGY:   ACTIVE
TARGET:                    Physical Review Applied Regular Article
SCIENTIFIC CONTENT:        FROZEN
PRODUCTION PDF:            QA-PASSED
NEW THEORY BY DEFAULT:     STOP
SUBMISSION BLOCKER:        HUMAN METADATA ONLY
```

The Experiment-01 Applied Optics, Experiment-09 PRA, and Experiment-12 PRB manuscripts remain mature frozen fallback packages. Preserve them. Do not simultaneously submit materially overlapping standalone and flagship manuscripts.

## Controlling production identity

```text
GitHub Actions run:   31900965632
head commit:          f41bdc6a4e580bfadd8155903f4127b2b63655ca
artifact ID:          9251078733
artifact digest:      1b4375f9953707ddf1e6b35bf55f91377370274d230298429398096f1b42e01a
PDF SHA-256:          84c86c30019a0517246493ad4b9aacd60ac54051164b27ca7dfedac2fdba800f
built TeX SHA-256:    c1459c18e4bf5d20f09a9a956c23b565c76bd0a913fe9636adc2ca7fe1e2b8f9
pages:                7
undefined refs/cites: none
overfull boxes:       none
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

Use selected direct cross-chemical-potential conductivity and the basis-invariant exact-energy-shell capacity. Do not silently substitute arbitrary total conductivity or a pairwise velocity maximum.

The theorem bounds equilibrium one-body endpoint population. It is not a universal dark-current, generation-rate, finite-bandwidth-noise, or `D*` theorem.

## Unified connector

For a physically declared admissible domain,

```math
\boxed{
\mathcal S_{X|D}\tau_{X|D}=1.
}
```

This is organizing algebra, not a generic novelty claim.

Important physical realizations:

```text
Experiment 09:   S=N_eff=1/sum_j w_j^2
Experiment 12:   S_th,B^act=1/tau_cap^act
uniform tasks:   S=d/r_st
readout stage:   channel-specific positive effects and null sectors
```

The dispersive thermal decomposition is

```math
\tau_{cap}^{act}=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
```

```math
\tau_{obs}^{act}=\eta_F\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
```

## Production HgCdTe result

```text
n_ref                         = 1.005140525e17 cm^-3
v_B^cap                       = 1.01764e6 m/s
eta_F                         = 0.306836598
tau_cap^act                   = 0.572622972
tau_obs^act                   = 0.175701685
bound/reference               ~= 0.118
bound/active                  ~= 0.176
```

```math
0.306836598\times0.572622972=0.175701685.
```

Selected active exact-shell blocks have `S_a^act=1` to floating-point precision in the **BIA-neglecting second-order Kane validation model**. The fixed-k `PT`/quaternionic explanation is model-specific. Real zincblende HgCdTe has BIA; do not generalize the exact equality without a BIA-inclusive calculation.

## Recycling observability result

A terminal has positive observability effect

```math
G_i(\omega)=M^\dagger|i><i|M.
```

A positive activity/lineage sector null to one channel cannot contribute cross-noise with another channel.

Under independent conservative one-final-sink Poisson lineages, ideal final-sink counting can therefore have zero interterminal cross-spectrum despite internal recycling and mean crosstalk.

For an internally created/recombined pair,

```math
Q_i^{rec}=0
```

while finite-transit Shockley-Ramo motion can have finite-frequency support and lift the endpoint channel null. A nonzero ensemble cross-spectrum is allowed, not guaranteed.

## Novelty boundary

Do not claim generic matrix, stable-rank, task-information, bright/dark-state, Shockley-Ramo, GR-noise, Poisson-output, photon-recycling, or optical-sum-rule theory as new.

The candidate contribution is the detector-specific cross-closure, shell decomposition/material diagnosis, and conservative-recycling readout boundary. No direct prior-art collision was found in the completed targeted audits. Historical priority remains unproven.

## Production infrastructure

```text
experiments/13-observable-resource-unification/typeset/rev4_unified_prapplied.tex
experiments/13-observable-resource-unification/typeset/rev4_unified.bib
experiments/13-observable-resource-unification/typeset/rev4_figures.tex
experiments/13-observable-resource-unification/typeset/build_rev4.py
.github/workflows/rev4-flagship-pdf.yml
```

Do not replace the theorem-label/environment slicing in `build_rev4.py` with a broad multiline regex. A broad regex previously swallowed preceding manuscript content in an intermediate built copy; the scientific source remained intact and the regression was caught during visual QA.

## Next work

Do **not** reopen theory by default.

The only known submission blockers are:

```text
author name
institutional affiliation
corresponding email
acknowledgments / funding statement
```

When those are supplied:

```text
make metadata-only edits;
rebuild through CI;
record new hashes;
inspect every rendered page;
submit if the metadata-only package remains clean.
```

Reopen science only for a concrete mathematical defect, numerical inconsistency, direct prior-art collision, explicit referee/editor request, or specific journal requirement.
