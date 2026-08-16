# Repository Recovery Guide — gedanken_3

**Date:** 2026-08-15  
**Active branch:** `experiment-13-observable-resource-unification`  
**Repository frontier:** **Experiment 13 Rev. 8 — Physical Review Applied flagship; homogeneous full-BIA robustness, 8-page production QA, and hostile review passed**

## Recovery order

1. `agent.md`
2. `experiments/13-observable-resource-unification/00_ACTIVE_FRONTIER_REV8_FLAGSHIP_2026-08-15.md`
3. `experiments/13-observable-resource-unification/PAPER_REV8_BIA_ROBUST_HOSTILE_REVIEW_2026-08-15.md`
4. `experiments/13-observable-resource-unification/REV8_PRAPPLIED_PRODUCTION_QA_2026-08-15.md`
5. `experiments/13-observable-resource-unification/HGCDTE_FULL_HOMOGENEOUS_BIA_ROBUSTNESS_2026-08-15.md`
6. `experiments/13-observable-resource-unification/PRAPPLIED_SUBMISSION_PREFLIGHT_REV8_2026-08-15.md`
7. `experiments/13-observable-resource-unification/CURRENT_STATE.md`

Rev. 7 and earlier are historical checkpoints. Rev. 8 controls whenever states conflict.

## Controlling production identity

```text
Actions run:          31916728949
source commit:        813fd8a2fc3011ef6e3ba63a0567cb3eee30297b
artifact ID:          9255118533
artifact digest:      a5d7aac0a5f3a68783a3510c9c2e8632af3e5b4e34f326e3012dd1aa6316bfcd
PDF SHA-256:          309655aec80a7778428beedad4c95b53b27b8ebae24143310b1f4fdc1c6faf87
TeX SHA-256:          08efd63da8e5558a07bbc5a4bc9be8667811bf2314705c69f257e30b9b565973
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
hostile review:       PASS
```

## Scientific core

The central optical population theorem, thermodynamic uniform-capacity/liminf formalism, and full tightness hierarchy are unchanged from Rev. 7.

Production HgCdTe baseline:

```text
support fraction       = 0.66897
eta_F                  = 0.30684
tau_cap^act            = 0.57262
tau_bound^act          = 0.17570
full bound/reference   ~= 0.1175
v_B^cap                = 1.01764e6 m/s
```

## New Rev. 8 material robustness

A separate homogeneous effective eight-band BIA stress model includes `B8v+`, `B8v-`, and complete `C_k` bulk couplings.

```text
BIA off:
capacity 1.01764e6 m/s
full ratio 0.11747
20072 sampled active dimension-2 blocks
S_a=1

homogeneous BIA:
capacity 1.02203e6 m/s
full ratio 0.11651
40452 sampled active dimension-1 blocks
S_a=1
```

Relative change:

```text
capacity ~= +0.43%
full ratio ~= -0.82%
within-shell factor unchanged at 1
```

The BIA result passes hard basis/symmetry/velocity QA, multi-seed continuous-capacity search, independent-grid checks, and exact-shell cluster-tolerance sweeps.

The structural reason for unity changes: BIA-off blocks are PT doublets with equal singular values; generic BIA-split sampled active parents are one-dimensional, so a nonzero block has rank = stable rank = 1.

Model limits are explicit: homogeneous effective eight-band BIA, not atomistic/interface complete; exceptional multidimensional exact degeneracies are not excluded.

## Reproducible production

```text
build_rev4.py
-> Rev4-to-Rev5 patches
-> build_rev6.py
-> build_rev7.py
-> build_rev8.py
-> finalize_rev8.py
-> REVTeX/BibTeX
-> automated QA + 180-dpi page renders
```

Workflow:
`.github/workflows/rev8-flagship-pdf.yml`

## Publication architecture — mandatory

```text
Experiment 13 Rev. 8:     SOLE PRIMARY ACTIVE SUBMISSION MANUSCRIPT
Experiment 12 manuscript: FROZEN FALLBACK / DEVELOPMENT PROVENANCE
Experiment 01 manuscript: FROZEN FALLBACK
Experiment 09 manuscript: FROZEN FALLBACK
concurrent overlapping submission: DO NOT DO
```

Any change to the supersession policy requires a fresh overlap audit before submission.

## Stop rule

Do not create Rev. 9 or new theory by default. Reopen only for a concrete external criticism, counterexample, numerical inconsistency, or direct prior-art collision.

## Remaining work

Use `PRAPPLIED_SUBMISSION_PREFLIGHT_REV8_2026-08-15.md`.

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

After metadata insertion, rebuild through Rev. 8 CI, record final hashes, inspect every page, and verify submitted source reproduces submitted PDF.
