# Experiment 12 — Final adversarial QA of MANUSCRIPT_REV6

**Date:** 2026-08-14  
**Reviewer posture:** final hostile internal referee  
**Disposition:** **THEOREM-LEVEL PASS / SUBMISSION-CANDIDATE TEXT / NOVELTY NOT ESTABLISHED**

## 1. Executive disposition

Rev6 resolves the remaining manuscript defects without adding new physics.

The optical-resource notation is now unambiguous:

```math
v_B^{cap}
```

throughout the defining equations and theorem statements. The previous Latin-`u` / Greek-`nu` transcription problem is eliminated rather than patched.

The active-subspace refinement is mathematically valid and corrects the overbroad finite-window equality statement that existed in Rev3. No counterexample was found to the controlling hierarchy

```math
\boxed{
n_e+n_h
\ge
n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega .
}
```

The theory phase should now stop by default.

---

## 2. Pointwise Fermi inequality — PASS

For each transition with `E_v < mu < E_c`,

```math
\frac{2[f(E_v)-f(E_c)]}
{e^{(E_c-E_v)/(2k_BT)}-1}
\le
f(E_c)+1-f(E_v)
```

follows from AM-GM at fixed transition energy.

Equality condition:

```math
E_c-mu=mu-E_v.
```

No algebraic defect found.

---

## 3. Kubo-Greenwood conversion — PASS

The angular-frequency convention

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta(\omega-E_{cv}/\hbar)
```

has the correct dimensional normalization for the theorem. The chosen thermal kernel cancels the `1/E_cv` factor exactly as required.

No missing `hbar` or factor-of-two defect was found.

---

## 4. Basis invariance — PASS

The selected shell coupling operators

```math
A_{epsilon_c,B}=P_{epsilon_c}v_iQ^-_{epsilon_c,B},
```

```math
B_{epsilon_v,B}=Q^+_{epsilon_v,B}v_iP_{epsilon_v}
```

are defined with complete exact energy eigenspace projectors.

The capacity

```math
(v_B^{cap})^2
=max[
 sup_{epsilon_c}||A||_op^2,
 sup_{epsilon_v}||B||_op^2]
```

is invariant under arbitrary unitary basis changes inside exact degeneracies and does not mix distinct-energy equilibrium eigenstates.

---

## 5. Active-subspace trace-rank theorem — PASS

For every selected block,

```math
Tr(XX^dagger)<=||X||_op^2 rank(X).
```

The finite-volume support ranks therefore give

```math
R_B(T)
<=
(v_B^{cap})^2
[n_{e,B}^{act}+n_{h,B}^{act}].
```

The active populations are basis invariant and satisfy

```math
n_{e,B}^{act}<=n_e,
n_{h,B}^{act}<=n_h.
```

The manuscript explicitly identifies `n^act` as a support-dimension count rather than a continuously weighted participation ratio.

---

## 6. Finite-window equality — PASS

The ideal equal-mass mirror-symmetric parabolic one-to-one model exactly saturates the **active-subspace** theorem for arbitrary selected direct-transition window `B`.

The total-population theorem is correctly stated to saturate only when the full relevant direct spectrum is selected.

This fixes the only substantive scientific presentation error found in the Rev3 external-style pass.

---

## 7. Dimensional normalization — PASS

Rev6 now explicitly states:

```text
3-D: V is volume and sigma is bulk conductivity;
2-D: V is replaced by sample area and sigma by sheet conductivity.
```

The graphene validation is therefore dimensionally explicit rather than implicit.

---

## 8. Validation family — PASS

Retained checks:

```text
2-D neutral massless Dirac: global total-population bound/exact = 0.5000
3-D massless Dirac:                                      = 0.6667
3-D massive Dirac, Delta/kBT=2.398:                     = 0.794684
3-D equal-mass parabolic global model:                  = 1.0000
```

For unequal parabolic masses in the nondegenerate global limit,

```math
\frac{n_{bound}}{n_{exact}}
=\left[
\frac{4m_em_h}{(m_e+m_h)^2}
\right]^{3/4}
<=1.
```

No regression was introduced by the active-subspace refinement because these quoted ratios concern the global total-population corollary.

---

## 9. Low-energy interpretation — PASS

With

```math
K_T(E)=E/[e^{E/(2k_BT)}-1],
```

```math
K_T(E)->2k_BT
```

as `E->0`.

The manuscript correctly phrases the consequence in terms of **integrated** spectral weight. It does not claim that an arbitrarily narrow high-peak line carries a finite population floor.

---

## 10. Scope discipline — PASS

Rev6 does not claim a universal lower bound on:

```text
dark current;
thermal generation rate;
D*;
finite-bandwidth noise.
```

It explicitly excludes or qualifies:

```text
neutral excitons / collective optical states;
phonon-assisted indirect transitions;
interaction-generated many-body spectral functions;
localized-state transport implications;
unconstrained photonic enhancement.
```

The previously rejected conversion

```math
G_th >= n_th/tau_response
```

is not revived.

---

## 11. Bibliography QA

Primary publisher records were checked for the core references used to position the theorem:

```text
Piotrowski & Gawron 1997 — metadata and alpha/G detector-material criterion confirmed;
Huang, Chyi & Morkoc 1990 — phase-space-filling paper confirmed;
Kwong, Rupper & Binder 2009 — finite-density/T semiconductor optical theory confirmed;
Watanabe & Oshikawa 2020 — generalized f-sum/Kohn paper confirmed;
Cardenas-Castillo et al. 2024 — quantum-geometric optical-sum paper confirmed;
Gusynin & Sharapov 2006 — graphene optical-conductivity paper confirmed;
Gusynin, Sharapov & Carbotte 2007 — graphene optical sum-rule paper confirmed;
Tabert, Carbotte & Nicol 2016 — 3-D Dirac/Weyl optical/transport paper and erratum confirmed;
Tabert & Carbotte 2016 — gapped-semimetal optical-conductivity paper confirmed.
```

The Yablonovitch–Kane 1986 citation remains consistent with DOI/title/author metadata used in the branch and is retained as the classic low-carrier band-engineering comparator.

No citation was found to contradict the manuscript's conservative related-work statements.

---

## 12. Final novelty audit

Adjacent theory includes:

```text
phase-space filling;
TRK/f-sum conductivity particle counts;
generalized optical sum rules;
quantum-geometric optical sums;
low-carrier semiconductor-laser band engineering;
classic IR alpha/G_th criteria.
```

Bethkenhagen et al., Phys. Rev. Research 2, 023260 (2020), provides an important additional comparator: dynamic conductivity is used with the TRK sum rule to infer ionization/free-electron count in warm dense matter.

That establishes that the broad idea

```text
conductivity spectral weight -> particle count
```

is not new.

No direct source was identified with the Experiment-12 combination

```text
cross-mu direct conductivity;
thermal kernel E/[exp(E/2kBT)-1];
per-energy-shell optical-velocity capacity;
minimum thermal optical-support population;
minimum total thermal electron-hole excitation population.
```

Disposition:

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

No `first`, `novel`, or priority wording is authorized.

---

# Final gate

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

## Recommendation

Treat

`MANUSCRIPT_REV6_2026-08-14.md`

as the current submission-candidate scientific text.

Do not add further theory by default. The next work should be journal selection, journal-specific bibliography/style audit, typesetting, and an independent review of the rendered manuscript.