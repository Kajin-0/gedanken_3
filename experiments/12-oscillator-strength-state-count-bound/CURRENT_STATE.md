# Current State — Experiment 12

**Date:** 2026-08-14  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Scope:** analytical/theoretical only

**Status:** **THEOREM SURVIVES / ACTIVE-SUBSPACE REFINEMENT COMPLETE / REV6 SUBMISSION-CANDIDATE SCIENTIFIC TEXT / FINAL HOSTILE QA PASS / NO DIRECT PRIOR-ART COLLISION FOUND / NOVELTY NOT ESTABLISHED / NO MORE THEORY BY DEFAULT**

## Read first

1. `MANUSCRIPT_REV6_2026-08-14.md`
2. `MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`
3. `ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`
4. `MANUSCRIPT_REV4_EXTERNAL_STYLE_REVIEW_2026-08-14.md`
5. `NOVELTY_AUDIT_ADDENDUM_TRK_CONDUCTIVITY_PARTICLE_COUNT_2026-08-14.md`
6. `NOVELTY_AUDIT_2026-08-14.md`
7. `NOVELTY_AUDIT_ADDENDUM_LOW_CARRIER_OPTICS_2026-08-14.md`
8. `PROGRESS_LOG.md`

Older Rev0–Rev5 files preserve the development and correction history. Rev3's notation erratum is historical only; Rev6 eliminates that ambiguity by using a new resource symbol.

---

# Controlling theorem

Consider equilibrium independent quasiparticles with exact states `E_v < mu < E_c`. Define the direct cross-chemical-potential conductivity

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

For an arbitrary positive-frequency window `B`, define the basis-invariant selected shell coupling blocks and the optical-velocity capacity

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

Define the basis-invariant optically active thermal populations from the support ranks of those blocks:

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

Then the strongest surviving theorem is

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

For an intrinsic neutral absorber, `n_e=n_h=n_th`,

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

`n_B^act` is a **support-dimension population**, not an oscillator-strength-weighted participation ratio.

In 2-D, replace volume by sample area and bulk conductivity by sheet conductivity.

---

# Low-energy consequence

With

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1},
```

```math
K_T(E)\to2k_BT
```

as `E -> 0`.

Therefore finite **integrated** low-energy direct cross-`mu` spectral weight has a finite equilibrium thermal population cost at fixed `v_B^{cap}`:

```math
n_{e,B}^{act}+n_{h,B}^{act}
\gtrsim
\frac{4k_BT}{\pi e^2(v_B^{cap})^2}
\int_B\sigma_1^{cross}(\omega)d\omega.
```

A peak-only line with useful bandwidth tending to zero is not forced to a finite population floor because its integrated spectral weight can vanish.

---

# Equality / validation

## Equal-mass parabolic model

For ideal mirror-symmetric 3-D parabolic direct bands with constant one-to-one optical matrix element:

```text
active-subspace theorem: exact saturation for any selected direct-transition window and all T;

total-population theorem: exact saturation only when the full relevant direct spectrum is selected.
```

For unequal masses in the nondegenerate global limit,

```math
\boxed{
\frac{n_{bound}}{n_{exact}}
=\left[
\frac{4m_em_h}{(m_e+m_h)^2}
\right]^{3/4}
\le1.
}
```

At `E_g/kBT = 4.7959`, total-population ratios are approximately:

```text
m_h/m_e = 2   -> 0.9161
m_h/m_e = 5   -> 0.6455
m_h/m_e = 10  -> 0.4379
m_h/m_e = 1   -> 1 exactly
```

## Dirac checks

```text
2-D neutral massless Dirac / graphene: 0.5000
3-D massless Dirac:                    0.6667
3-D massive Dirac, 10 um / 300 K:      0.794684
```

---

# Scope boundary

Valid class:

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

The theorem survives arbitrary dispersive multiband state reuse, unequal degeneracy, and static one-particle disorder when exact eigenstates are used.

It does not automatically cover:

```text
bound excitons / neutral collective optical states;
phonon-assisted / indirect transitions;
interaction-generated many-body spectral functions;
unconstrained external photonic path enhancement.
```

Localized states do not invalidate the population theorem but block automatic inference to DC dark current.

Do not claim a universal lower bound on:

```text
dark current;
thermal generation rate;
D*;
finite-bandwidth noise.
```

The attempted universal conversion `G_th >= n_th/tau_response` was rejected by the depleted-photodiode counterexample.

---

# Novelty / prior-art disposition

Audited adjacency includes:

```text
Kubo-Greenwood;
semiconductor phase-space filling;
ordinary/generalized f-sums;
restricted optical sums;
quantum-geometric optical sums;
graphene optical sum rules;
classic IR alpha/G_th detector criteria;
Yablonovitch-Kane low-carrier laser band engineering;
TRK conductivity-to-ionization particle counting in warm dense matter.
```

Bethkenhagen et al., *Phys. Rev. Research* 2, 023260 (2020), confirms that the broad concept `conductivity spectral weight -> particle count` is established through the TRK sum rule. It does not state the Experiment-12 cross-`mu` thermally weighted state-count inequality.

Focused searches did not identify a source with the combination

```text
cross-mu direct optical conductivity
+ thermal kernel E/[exp(E/2kBT)-1]
+ per-shell optical-velocity capacity
-> minimum thermal optical-support population
-> minimum total thermal electron-hole population.
```

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH BECAUSE THE PROOF IS ELEMENTARY
```

No `first`, `novel`, or priority language is authorized without a stronger external priority check.

---

# Manuscript state

Current scientific submission-candidate text:

`MANUSCRIPT_REV6_2026-08-14.md`

Final hostile QA:

`MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md`

Final QA disposition:

```text
FERMI ALGEBRA: PASS
KUBO NORMALIZATION: PASS
BASIS INVARIANCE: PASS
TRACE-RANK ACTIVE-SUBSPACE REFINEMENT: PASS
FINITE-WINDOW EQUALITY: PASS
2-D NORMALIZATION: PASS
PARABOLIC VALIDATION: PASS
DIRAC VALIDATION: PASS
LOW-ENERGY INTERPRETATION: PASS
CLAIM SCOPE: PASS
BIBLIOGRAPHY CORE: PASS
DIRECT PRIOR-ART COLLISION: NOT FOUND
NOVELTY: NOT ESTABLISHED
```

Rev6 uses `v_B^{cap}` throughout and supersedes the Rev3–Rev5 `u/nu` notation history.

---

# Next action — NO MORE THEORY BY DEFAULT

Do not add mechanisms or extend the theorem unless an external/referee-style review identifies a blocking scientific gap.

Next work should be:

```text
1. select the most appropriate journal;
2. perform journal-specific scope and reference-style audit;
3. typeset Rev6;
4. independently review the rendered manuscript;
5. prepare submission materials only after the rendered QA passes.
```
