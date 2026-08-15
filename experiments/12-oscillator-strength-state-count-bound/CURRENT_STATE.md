# Current State — Experiment 12

**Date:** 2026-08-14  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **THEOREM-LEVEL INTERNAL QA PASS / ACTIVE-SUBSPACE REFINEMENT COMPLETE / REV6 SCIENTIFIC TEXT FROZEN / PRB SELECTED AS FIRST TARGET / JAP FALLBACK / NO DIRECT PRIOR-ART COLLISION FOUND / NOVELTY NOT ESTABLISHED / NO MORE THEORY BY DEFAULT**

## Read first

1. `MANUSCRIPT_REV6_2026-08-14.md`
2. `MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
3. `JOURNAL_FIT_AND_SUBMISSION_PLAN_2026-08-14.md`
4. `ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`
5. `MANUSCRIPT_REV4_EXTERNAL_STYLE_REVIEW_2026-08-14.md`
6. `NOVELTY_AUDIT_ADDENDUM_TRK_CONDUCTIVITY_PARTICLE_COUNT_2026-08-14.md`
7. `NOVELTY_AUDIT_2026-08-14.md`
8. `PROGRESS_LOG.md`

Older manuscript revisions preserve the derivation/correction history. Rev6 is scientifically controlling.

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

For an arbitrary positive-frequency window `B`, use exact energy-shell projectors to define selected optical blocks `A_{epsilon_c,B}`, `B_{epsilon_v,B}` and

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

Define the basis-invariant thermal optical-support populations

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

# Main physical consequence

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}
\to2k_BT
```

as `E -> 0`.

Thus finite **integrated** low-energy direct cross-`mu` optical spectral weight carries a finite thermal population cost at fixed `v_B^{cap}`. A peak-only line whose useful bandwidth vanishes can have vanishing integrated spectral weight and is not forced to a finite population floor.

---

# Equality / validation

```text
Ideal equal-mass mirror-symmetric parabolic model:
    active-subspace theorem saturates for any selected direct window;
    total-population theorem saturates for the full relevant direct spectrum.

2-D neutral massless Dirac: 0.5000
3-D massless Dirac:         0.6667
3-D massive Dirac,
10 um / 300 K:              0.794684
```

For unequal parabolic masses in the nondegenerate global limit,

```math
\boxed{
n_{bound}/n_{exact}
=[4m_em_h/(m_e+m_h)^2]^{3/4}\le1.
}
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

No direct source was identified with the exact combination

```text
cross-mu direct conductivity
+ E/[exp(E/2kBT)-1] thermal kernel
+ per-shell optical-velocity capacity
-> minimum thermal optical-support population
-> minimum total thermal electron-hole population.
```

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

---

# Manuscript and journal state

Current scientific submission-candidate text:

`MANUSCRIPT_REV6_2026-08-14.md`

Final internal hostile QA:

`MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`

Journal plan:

```text
FIRST TARGET: Physical Review B — Regular Article
FALLBACK: Journal of Applied Physics — Article
LESS CLEAN FIT: Physical Review Applied
```

Rationale is recorded in:

`JOURNAL_FIT_AND_SUBMISSION_PLAN_2026-08-14.md`

PRB is the preferred first target because the manuscript is fundamentally a general semiconductor/condensed-matter optical-response theorem. The photodetector motivation should remain, but the manuscript should not be weakened into an HgCdTe-only or device-performance claim.

---

# ACTIVE NEXT ACTION — PRB PRODUCTION, NOT MORE THEORY

```text
1. convert Rev6 into PRB-compatible LaTeX;
2. perform PRB-specific reference/style audit;
3. compile and visually inspect the PDF;
4. run an independent review of the rendered manuscript;
5. prepare cover-letter/submission metadata only after rendered QA passes.
```

Add new physics only if a referee identifies a blocking scientific gap.
