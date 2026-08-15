# Experiment 12 — Extreme Adversarial Review of MANUSCRIPT_REV0

**Date:** 2026-08-14  
**Reviewer posture:** hostile condensed-matter / semiconductor-optics referee  
**Disposition:** **MAJOR REVISION — CORE THEOREM SURVIVES / ONE BLOCKING RESOURCE-DEFINITION DEFECT / MANUSCRIPT ARGUMENT IS VIABLE AFTER CORRECTION**

## Executive verdict

The manuscript contains a real and compact finite-temperature inequality. I do **not** find an algebraic counterexample to the pointwise Fermi lemma or to the subsequent Kubo summation. The parabolic equality family and Dirac checks are strong and make the result considerably more credible than an abstract norm estimate.

However, Rev0 is not submission-ready. The most important defect is that the headline resource

```math
v_{*,B}^2
=\max[\sup_cR_c(B),\sup_vC_v(B)]
```

is defined using individual eigenvectors and can change under a unitary rotation within an exactly degenerate eigenspace. The inequality remains true in any chosen basis, but the paper should not present a basis-dependent quantity as a uniquely defined material resource.

This is fixable by replacing the headline resource with a basis-invariant spectral norm of a frequency-filtered cross-`mu` velocity block. The old row/column maximum may remain as a sharper basis-resolved computational quantity only when the eigenbasis is fixed by nondegeneracy or an additional commuting symmetry.

The remaining objections are framing/citation issues rather than theorem failures.

---

# 1. BLOCKING — basis dependence of the per-state velocity resource

## Problem

Inside an exactly degenerate upper or lower eigenspace, the individual states may be unitarily rotated without changing the Hamiltonian. The row norms

```math
R_c(B)=\sum_v|v_{cv}|^2
```

and column norms can redistribute under that rotation.

Consequently

```math
\max_cR_c(B)
```

need not be invariant under the choice of basis within a degenerate manifold.

A referee can therefore object that the supposedly microscopic resource `v_{*,B}` is not itself a well-defined observable/property of the Hamiltonian.

## Correct invariant resource

Define the frequency-filtered cross-`mu` velocity operator

```math
\boxed{
\hat V_B
=
\sum_{\substack{E_v<\mu<E_c\\E_{cv}/\hbar\in B}}
|c\rangle\langle c|\hat v_i|v\rangle\langle v|.
}
```

Equivalently, in the exact energy eigenbasis its matrix is

```math
(V_B)_{cv}
=1_B(E_{cv}/\hbar)v_{cv}.
```

Because the frequency mask depends only on exact eigenvalues, rotations within degenerate energy eigenspaces transform `V_B` by left/right unitary matrices. Its singular values and spectral norm are therefore invariant.

Define

```math
\boxed{
u_B=\|\hat V_B\|_{op}.}
```

Every selected row and every selected column has Euclidean norm at most `u_B`, because

```math
R_c(B)
=\|\langle c|V_B\|^2
\le\|V_B\|_{op}^2,
```

and similarly for columns.

Therefore the basis-invariant population theorem is

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
```

The intrinsic form is half the total-excitation bound.

## Cost of the correction

Since

```math
u_B^2
\ge
\max[\max_cR_c(B),\max_vC_v(B)],
```

the invariant theorem can be weaker than the basis-resolved version.

This is acceptable. A physically invariant theorem is more important than an artificially sharp basis-dependent prefactor.

The exact flat-manifold and parabolic equality examples still saturate the invariant form because their filtered transition operators have all relevant singular values equal to the same optical velocity.

### Verdict

```text
BLOCKING IN REV0.
STRAIGHTFORWARDLY REPAIRABLE.
```

---

# 2. Theorem 1 is stronger conceptually than Theorem 2 and should lead the paper

The manuscript correctly derives the parameter-free hierarchy first half

```math
\mathcal R_B(T)
\ge
\frac{2}{\pi e^2}
\int_BK_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega.
```

This should be emphasized more strongly.

The `u_B`-conditioned carrier-density theorem is a corollary. Presenting the hierarchy in this order has two advantages:

```text
1. the exact response/statistics inequality is not accused of containing an ad hoc velocity constant;
2. the role of u_B is clearly an explicit microscopic resource needed to convert optical strength into a state-count bound.
```

### Verdict

```text
MAJOR PRESENTATION REVISION.
```

---

# 3. The novelty case is not “new physics ingredients”

Every individual ingredient is old:

```text
Fermi-Dirac occupations;
Pauli blocking;
Kubo-Greenwood;
operator/matrix norm bounds;
light/symmetric bands as favorable optical-device design;
infrared alpha/G_th reasoning.
```

If the paper implies otherwise it will be rejected immediately.

The defensible novelty case, if any, is narrower:

```text
an inverse finite-temperature inequality from surviving cross-mu optical spectral weight to equilibrium thermal quasiparticle excitation population;
valid for arbitrary dispersive multiband state reuse;
without choosing a DOS model;
with explicit equality conditions and a microscopic per-state optical-strength resource.
```

The introduction and conclusion should say this explicitly.

### Verdict

```text
HIGH NOVELTY RISK, BUT NOT A DIRECT COLLISION.
```

---

# 4. The 10-um detector illustration is too prominent in the current main text

The theorem is much broader than LWIR detectors, while the detector interpretation is deliberately only a necessary material condition.

A full section and table of single-pass 10-um numbers risks making the paper look like an underdeveloped detector-performance manuscript, inviting objections about:

```text
cavities/path enhancement;
refractive-index assumptions;
collection;
dark-current kinetics;
actual HgCdTe comparison.
```

The numerical example is useful but should be compressed to one paragraph or moved to an appendix/supplement.

The core paper should stand even if every detector-specific number is removed.

### Verdict

```text
MAJOR FRAMING REVISION.
```

---

# 5. Massive-Dirac reference is incomplete

Rev0 cites Tabert, Carbotte, and Nicol, PRB 93, 085426 (2016), for three-dimensional Dirac/Weyl optical response. The finite-gap/gapped-semimetal validation should also cite the directly relevant work

```text
C. J. Tabert and J. P. Carbotte,
"Optical conductivity of Weyl semimetals and signatures of the gapped semimetal phase transition,"
Phys. Rev. B 93, 085442 (2016).
```

The manuscript's numerical calculation is independent and reproducible, but the adjacent exact optical-response literature must be cited accurately.

### Verdict

```text
REQUIRED CITATION CORRECTION.
```

---

# 6. Kubo normalization check

The angular-frequency form

```math
\sigma_1(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta(\omega-E_{cv}/\hbar)
```

is dimensionally consistent.

Starting from an energy-delta representation with an explicit `hbar` prefactor and converting

```math
\delta(E_{cv}-\hbar\omega)
=\hbar^{-1}\delta(\omega-E_{cv}/\hbar)
```

produces the displayed expression.

### Verdict

```text
PASS.
```

---

# 7. Pointwise Fermi lemma check

For

```math
a=e^{-\beta(E_c-\mu)},
\quad
b=e^{-\beta(\mu-E_v)},
\quad
z=ab=e^{-\beta E_{cv}},
```

one has

```math
D=(1-z)/[(1+a)(1+b)],
```

and

```math
p_c+h_v=(a+b+2z)/[(1+a)(1+b)].
```

The claimed inequality is equivalent to

```math
a+b\ge2\sqrt{ab},
```

so the proof and equality condition are exact.

### Verdict

```text
PASS.
```

---

# 8. State reuse / multiband check

The global sum does not double-count thermal population incorrectly. A state that couples to many optical partners contributes its thermal occupation once to `n_e` or `n_h`, while all of its optical edges consume the finite row/column matrix-strength budget.

The random-matrix falsification script provides a useful bookkeeping test but should not be presented as mathematical evidence in the main manuscript. The analytic proof is sufficient.

### Verdict

```text
PASS.
```

---

# 9. Parabolic equality family is a major strength

For mirror-symmetric parabolic bands with equal masses and constant vertical matrix element, every direct transition is symmetric about `mu`. Thus the pointwise Fermi inequality saturates at every `k`, and the filtered transition-operator norm equals the one-to-one matrix element.

The exact all-temperature equality is convincing and materially strengthens the paper.

For unequal masses, the nondegenerate tightness ratio

```math
[4m_em_h/(m_e+m_h)^2]^{3/4}
```

is symmetric under mass exchange and correctly bounded by unity.

### Verdict

```text
PASS; KEEP IN MAIN TEXT.
```

---

# 10. Dirac validations are valuable but should not dominate

The graphene and three-dimensional Dirac checks demonstrate that the result is not a parabolic-band artifact. The finite-gap 10-um/300-K ratio `0.794684` is especially useful.

But the paper does not need a long parameter sweep. One compact table plus an appendix calculation is enough.

### Verdict

```text
PASS; COMPRESS.
```

---

# 11. Static disorder claim is acceptable if phrased precisely

The proof does not require Bloch momentum. Exact eigenstates of a static one-body disordered Hamiltonian can be used.

However, this statement must not be conflated with interaction-generated lifetime broadening or an arbitrary phenomenological Lorentzian convolution.

### Verdict

```text
PASS WITH EXISTING SCOPE LANGUAGE.
```

---

# 12. Excitons are a genuine escape and must stay in the abstract/conclusion

A neutral bound exciton can carry large low-energy optical weight while free-charge excitation remains costly. This is a real counterexample to universality over all photodetectors.

Rev0 appropriately states this limitation. Do not bury it in supplementary material.

### Verdict

```text
PASS; ESSENTIAL SCOPE LIMIT.
```

---

# 13. Dark-current / D* restraint is correct

Rev0 does not claim a universal generation-rate, dark-current, or `D*` bound. That restraint is scientifically necessary.

The failed shortcut

```math
G_th>=n_th/tau_response
```

should remain out of the paper except perhaps as one sentence explaining why the result is a population theorem.

### Verdict

```text
PASS.
```

---

# 14. Literature audit after Rev0

A further focused search after drafting still finds strong adjacency but no direct collision:

```text
semiconductor phase-space filling gives the forward carrier-density -> bleaching problem;
standard/generalized f-sums constrain all-electron/kinetic spectral moments;
quantum-geometric sums use different moments and target Wannier spread;
classic alpha/G_th compares absorption to thermal generation after a material model is supplied;
Yablonovitch-Kane low-mass laser engineering establishes the favorable symmetry intuition.
```

No searched source states the corrected arbitrary-window inverse thermal-population inequality with the half-transition-energy kernel.

This remains an absence-of-collision result, not proof of priority.

---

# 15. Recommended Rev1 structure

The next manuscript should be shorter and sharper:

```text
I. Introduction
II. Pointwise Fermi lemma
III. Arbitrary-window theorem hierarchy
    A. parameter-free thermal velocity-strength inequality
    B. basis-invariant operator-norm population corollary
IV. Equality and tightness
    A. equal-mass parabolic exact equality
    B. Dirac checks
V. Relation to phase-space filling / sum rules / detector FOMs
VI. Scope and escape routes
VII. Conclusion
Appendix: detector illustration and secondary corollaries
```

---

# Final referee disposition

```text
POINTWISE LEMMA: PASS
KUBO NORMALIZATION: PASS
MULTIBAND GENERALIZATION: PASS
PARABOLIC EQUALITY: PASS
DIRAC VALIDATION: PASS
BASIS-INVARIANT RESOURCE: FAIL IN REV0, FIX AVAILABLE
NOVELTY: PLAUSIBLE, HIGH-RISK
DETECTOR OVERCLAIM: CONTROLLED
REV0: MAJOR REVISION
REV1 AFTER RESOURCE FIX: WORTH RE-REVIEWING
```
