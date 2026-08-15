# Current State — Experiment 12

**Date:** 2026-08-14  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **THEOREM-LEVEL INTERNAL QA PASS / REV6 SCIENCE FROZEN / PRB REVTeX RENDER PASS / COVER LETTER + SUBMISSION METADATA DRAFTED / PRB FIRST TARGET / JAP FALLBACK / NOVELTY NOT ESTABLISHED / NO MORE THEORY BY DEFAULT**

## Read first

1. `MANUSCRIPT_REV6_2026-08-14.md`
2. `MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
3. `PRB_RENDER_QA_2026-08-14.md`
4. `PRB_COVER_LETTER_DRAFT_2026-08-14.md`
5. `PRB_SUBMISSION_METADATA_2026-08-14.md`
6. `JOURNAL_FIT_AND_SUBMISSION_PLAN_2026-08-14.md`
7. `ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`
8. `NOVELTY_AUDIT_ADDENDUM_TRK_CONDUCTIVITY_PARTICLE_COUNT_2026-08-14.md`
9. `PROGRESS_LOG.md`

Older Rev0–Rev5 manuscripts preserve the derivation/correction history. Rev6 is scientifically controlling.

---

# Controlling theorem

For exact independent-quasiparticle states with `E_v < mu < E_c`, define the direct cross-chemical-potential conductivity

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{[f(E_v)-f(E_c)]|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
```

The exact pointwise Fermi inequality is

```math
\boxed{
\frac{2[f(E_v)-f(E_c)]}
{e^{E_{cv}/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v).
}
```

For any positive-frequency window `B`, use exact energy-shell projectors to define selected optical blocks `A_{epsilon_c,B}`, `B_{epsilon_v,B}` and the basis-invariant capacity

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

Define thermal optical-support populations

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

`n_B^act` is a support-dimension population, not an oscillator-strength-weighted participation ratio. In 2-D, replace volume by sample area and bulk conductivity by sheet conductivity.

---

# Main consequence / validation

```math
K_T(E)=E/[e^{E/(2k_BT)}-1]\to2k_BT
```

as `E -> 0`. Finite **integrated** low-energy direct spectral weight therefore carries a finite thermal population cost at fixed `v_B^{cap}`. A vanishing-bandwidth peak can evade this because its integrated spectral weight can vanish.

Validation summary:

```text
Equal-mass mirror-symmetric parabolic model:
    active-subspace theorem exact for any selected direct window;
    total-population theorem exact for full relevant direct spectrum.

2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac,
10 um / 300 K:              0.794684
```

Unequal parabolic masses, nondegenerate global limit:

```math
n_{bound}/n_{exact}
=[4m_em_h/(m_e+m_h)^2]^{3/4}\le1.
```

---

# Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Do not automatically extend to bound excitons, neutral collective states, phonon-assisted transitions, interacting many-body spectral functions, or arbitrary passive photonic path enhancement.

Localized states do not break the state-count theorem but block automatic inference to DC dark current.

Do not claim universal dark-current, thermal-generation-rate, `D*`, or finite-bandwidth-noise bounds. The proposed `G_th >= n_th/tau_response` theorem was explicitly rejected by a depleted-photodiode counterexample.

---

# Novelty status

Adjacent audited theory includes phase-space filling, Kubo-Greenwood, ordinary/generalized `f`/TRK sums, restricted and quantum-geometric optical sums, graphene optical sum rules, classic IR `alpha/G_th`, Yablonovitch-Kane low-carrier laser engineering, and Bethkenhagen et al. conductivity-to-ionization TRK particle counting.

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

---

# PRB production state

First target:

```text
Physical Review B — Regular Article
```

Fallback:

```text
Journal of Applied Physics — Article
```

A PRB-oriented REVTeX 4.2 rendering of frozen Rev6 has passed production QA.

Final local artifact hashes:

```text
experiment12_prb_rev6.tex
ecd9e09621c6fc3e87e9e6293f51ae4499b68a9e9ca878662a076e5d21700ced

experiment12_prb_rev6.pdf
b705d0868c3f2349a1821b5856f09792e8b2e0599d98efe38745c4e353229896
```

Render disposition:

```text
REVTeX 4.2 COMPILE: PASS
US-LETTER MEDIA BOX: PASS
PAGES: 6
OVERFULL BOXES: NONE
UNDEFINED REFERENCES/CITATIONS: NONE
STUCK FLOATS: NONE
PDF PREFLIGHT: PASS
PAGE-LEVEL VISUAL QA: PASS
CLIPPING/OVERLAP/BROKEN GLYPHS: NONE
```

Details: `PRB_RENDER_QA_2026-08-14.md`.

Current cover-letter template: `PRB_COVER_LETTER_DRAFT_2026-08-14.md`.

Current submission checklist / Data Availability options: `PRB_SUBMISSION_METADATA_2026-08-14.md`.

---

# Remaining blockers are author-owned / production-only

Before actual submission, complete:

```text
[ ] exact author name(s) and order
[ ] affiliation(s)
[ ] corresponding-author email
[ ] funding statement
[ ] conflict/disclosure statement
[ ] authorship approval
[ ] simultaneous-submission confirmation
[ ] prior Physical Review submission history
[ ] joint-submission status
[ ] referee suggestions/exclusions if desired
[ ] final Data Availability Statement
[ ] decision whether to archive validation scripts with persistent DOI
```

After these are supplied, insert them into the REVTeX source, recompile, and repeat rendered-PDF QA.

---

# ACTIVE NEXT ACTION — SUBMISSION PRODUCTION ONLY

```text
NO MORE THEORY BY DEFAULT.
```

Next work is to finalize author-owned metadata and Data Availability, then produce the exact submission PDF/source and cover letter. Add new science only if an external referee identifies a blocking scientific defect.