# AGENTS.md — Research Objective, Recovery, and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `experiment-12-oscillator-strength-state-count-bound`

Before material writes, fetch live targets and exact blob SHAs. Preserve failed, corrected, conditional, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Primary objective

Generate analytical/theoretical photodetector research from simple Gedanken experiments. The target is a defensible theorem, bound, invariant, counterexample, scaling law, or escape condition—not a materials list or a new scalar FOM.

## Hard global scope — ANALYTICAL / THEORETICAL ONLY

Allowed work: first-principles derivations, exact toy models, analytical bounds/no-go theorems, asymptotics, numerical thought experiments, analytical comparisons, and prior-art audits.

Do not make fabrication, measurement, instrumentation, sample procurement, or laboratory optimization the next step.

## Research protocol

```text
premise
-> minimal model
-> first nontrivial result
-> immediate primary-literature audit
-> kill if established
-> deepen only if something survives
-> theorem/bound/invariant/counterexample
-> quantitative witness
-> adversarial audit
-> manuscript only if novelty survives sufficiently to justify a draft
-> hostile manuscript review
-> typeset only after claim scope remains stable.
```

Do not add phenomenology merely to rescue a weak novelty case.

---

# Experiment 12 — REV6 SCIENCE FROZEN / PRB RENDER PASS / SUBMISSION PRODUCTION

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Recovery order:

1. `experiments/12-oscillator-strength-state-count-bound/CURRENT_STATE.md`
2. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_2026-08-14.md`
3. `experiments/12-oscillator-strength-state-count-bound/PRB_RENDER_QA_2026-08-14.md`
4. `experiments/12-oscillator-strength-state-count-bound/MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
5. `experiments/12-oscillator-strength-state-count-bound/PRB_COVER_LETTER_DRAFT_2026-08-14.md`
6. `experiments/12-oscillator-strength-state-count-bound/PRB_SUBMISSION_METADATA_2026-08-14.md`
7. `experiments/12-oscillator-strength-state-count-bound/JOURNAL_FIT_AND_SUBMISSION_PLAN_2026-08-14.md`
8. `experiments/12-oscillator-strength-state-count-bound/PROGRESS_LOG.md`

Older manuscript revisions preserve the development/correction history. Rev6 is controlling.

## Controlling theorem

For exact independent-quasiparticle states below and above `mu`, the pointwise Fermi inequality is

```math
\boxed{
\frac{2[f(E_v)-f(E_c)]}
{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
}
```

For any useful positive-frequency window `B`, use exact energy-shell projectors to define selected velocity blocks and

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

Define the thermally occupied optical-support populations

```math
n_{e,B}^{act}
=V^{-1}\sum_{\epsilon_c>\mu}f(\epsilon_c)
\operatorname{rank}A_{\epsilon_c,B},
```

```math
n_{h,B}^{act}
=V^{-1}\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]
\operatorname{rank}B_{\epsilon_v,B}.
```

Then

```math
\boxed{
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

For intrinsic neutrality,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
}
```

The thermal kernel tends to `2 kBT`, so finite **integrated** low-energy direct spectral weight carries a finite equilibrium thermal quasiparticle support-population cost at fixed `v_B^{cap}`.

`n_B^act` is a support-dimension count. In 2-D, use sample area and sheet conductivity.

## Equality / validation

```text
equal-mass mirror-symmetric parabolic model:
    active theorem exact for any selected direct window;
    total theorem exact for the full relevant direct spectrum.

2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac,
10 um / 300 K:              0.794684
```

For unequal parabolic masses in the nondegenerate global limit,

```math
n_bound/n_exact
=[4m_em_h/(m_e+m_h)^2]^{3/4}.
```

## Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to bound excitons/neutral collective states, phonon-assisted indirect absorption, interaction-generated many-body spectral functions, or unconstrained passive photonic path enhancement.

Localized states do not invalidate the state-count theorem but block automatic conversion to DC dark current.

Do not claim universal dark-current, thermal-generation-rate, `D*`, or finite-bandwidth-noise limits. The attempted `G_th >= n_th/tau_response` theorem was rejected by a depleted-photodiode counterexample.

## Novelty status

Audited adjacency includes phase-space filling, Kubo-Greenwood, ordinary/generalized `f` and TRK sums, restricted and quantum-geometric optical sums, graphene optical sum rules, classic IR `alpha/G_th`, Yablonovitch-Kane low-carrier laser engineering, and Bethkenhagen et al. conductivity-to-ionization particle counting.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

## Manuscript / journal / render state

```text
CURRENT SCIENTIFIC TEXT: MANUSCRIPT_REV6_2026-08-14.md
FINAL INTERNAL HOSTILE QA: PASS
FIRST TARGET: Physical Review B — Regular Article
FALLBACK: Journal of Applied Physics — Article
```

PRB REVTeX 4.2 production render has passed:

```text
6 pages
US letter
no overfull boxes
no undefined references/citations
no stuck floats
PDF preflight pass
all six pages visually inspected
no clipping, overlap, broken glyphs, or missing tables/equations
```

The local QA-passed `.tex` and `.pdf` SHA-256 hashes are recorded in `PRB_RENDER_QA_2026-08-14.md`.

A conservative PRB cover-letter draft and submission-metadata/Data Availability checklist are committed.

# ACTIVE NEXT ACTION — AUTHOR METADATA / FINAL SUBMISSION PACKAGE

```text
NO MORE THEORY BY DEFAULT.
```

The current blockers are author-owned:

```text
author names/order;
affiliations;
corresponding email;
funding;
conflicts/disclosures;
authorship approval;
simultaneous-submission confirmation;
prior Physical Review submission history;
joint-submission status;
final Data Availability/archive decision;
optional referee recommendations/exclusions.
```

Once those are supplied, insert them into the PRB REVTeX source, recompile, rerender, inspect the exact final PDF, and prepare the submission package.

Add new theory only if an external/referee-style review identifies a blocking scientific gap.

---

# Closed previous branches

## Experiment 10

`experiment-10-room-temperature-lwir-admissibility`

```text
CLOSED BY DEFAULT AS NOVELTY / MANUSCRIPT PATH.
```

## Experiment 11

`experiment-11-weighting-capacitance-duality`

```text
CLOSED BY DEFAULT AS NOVELTY / MANUSCRIPT PATH.
```

Candidate-audit files from the Experiment-10/11 lineage document rejected premises; consult them before reopening old ideas.
