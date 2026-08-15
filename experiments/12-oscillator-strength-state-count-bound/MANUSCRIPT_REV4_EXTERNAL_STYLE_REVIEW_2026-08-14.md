# Experiment 12 — External-style adversarial review of MANUSCRIPT_REV4

**Date:** 2026-08-14  
**Reviewer posture:** independent hostile referee  
**Disposition:** **PASS WITH MINOR REVISION / ACTIVE-SUBSPACE REFINEMENT IS VALID / NOVELTY REMAINS THE DOMINANT RISK**

## 1. Executive verdict

Rev4 materially improves the manuscript. The new optically active subspace hierarchy fixes the overbroad finite-window equality statement in Rev3 and strengthens the theorem rather than merely narrowing it.

I find no counterexample to the revised hierarchy

```math
\frac{2}{\pi e^2u_B^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega
\le
n_{e,B}^{act}+n_{h,B}^{act}
\le n_e+n_h.
```

The pointwise Fermi lemma, Kubo normalization, shell decomposition, operator-norm resource, trace-rank step, and finite-window parabolic saturation are mutually consistent.

Two minor corrections are required before archival freeze:

```text
1. Eqs. (17) and (23) still render Greek \nu_B where the intended resource is Latin u_B.
2. The 2-D Dirac/graphene validation must state explicitly that the normalization measure V is replaced by area and sigma_1 by sheet conductivity.
```

A third clarification is recommended:

```text
The rank-defined active population is a support-dimension count. Algebraic rank is intentionally binary with respect to nonzero coupling; it is not a continuously weighted participation ratio.
```

This is an interpretation issue, not a correctness defect.

---

## 2. Pointwise Fermi lemma — PASS

For each crossing transition,

```math
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v
```

follows directly from AM-GM at fixed `ab=exp(-beta E_cv)`.

Equality remains exactly

```math
E_c-mu=mu-E_v.
```

No missing factor of two or sign defect was found.

---

## 3. Kubo-Greenwood normalization — PASS

Using angular frequency,

```math
sigma_1^{cross}(omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta(omega-E_{cv}/hbar)
```

has the correct dimensions and converts the thermally weighted transition sum into Eq. (14) without an extra factor of `hbar`.

---

## 4. Active-subspace refinement — PASS

For each upper energy shell,

```math
A=P_{epsilon_c}v_iQ^-_{epsilon_c,B},
```

and analogously for each lower shell.

The shell contribution to `R_B` is proportional to

```math
Tr(AA^dagger).
```

The singular-value identity

```math
Tr(AA^dagger)=sum_j s_j^2
```

and the bound

```math
Tr(AA^dagger)
<= ||A||_op^2 rank(A)
```

are exact. Since all states in one exact degenerate shell have the same Fermi occupation, defining

```math
n_{e,B}^{act}
=V^{-1}sum_{epsilon_c}f(epsilon_c)rank(A_{epsilon_c,B})
```

and the analogous hole quantity is basis invariant.

Therefore

```math
R_B
<=u_B^2(n_{e,B}^{act}+n_{h,B}^{act})
```

is correct.

The inequalities

```math
n_{e,B}^{act}<=n_e,
qquad
n_{h,B}^{act}<=n_h
```

also follow because each selected rank is no larger than the dimension of its parent energy eigenspace.

```text
PASS.
```

---

## 5. Finite-window equality correction — PASS

The Rev3 statement that equal-mass parabolic bands saturate the **total-population** bound for arbitrary `B` was too broad.

Rev4 correctly distinguishes two statements.

### Active population

For the ideal equal-mass, mirror-symmetric parabolic model with one-to-one matrix element `v_0`, every selected transition saturates the Fermi lemma and every selected coupling block has all nonzero singular values equal to `v_0`.

Therefore the active-subspace theorem saturates for any selected frequency window.

### Total population

The total-population theorem saturates only when the selected window contains all thermally populated direct-transition states. A partial window leaves thermal states outside the selected graph and makes the total inequality strict.

This is the correct resolution.

---

## 6. Algebraic rank interpretation — CLARIFY, DO NOT CHANGE

The active population uses algebraic rank. Consequently, an arbitrarily weak but nonzero singular channel counts as one active one-body degree of freedom.

This is mathematically appropriate for a theorem about the support dimension of the selected coupling operator, but it should not be described as a continuously weighted optical participation number.

A stable-rank or Frobenius-weighted quantity could be introduced, but doing so would mostly repackage `R_B` and is not required for the present theorem. Do not inflate the paper with a second participation metric unless a referee specifically asks for it.

Recommended sentence:

> The active population counts the support dimension of the selected optical coupling blocks; it is not an oscillator-strength-weighted participation ratio.

---

## 7. 2-D normalization — MINOR REVISION REQUIRED

The main derivation uses a finite volume `V` and bulk conductivity. The graphene validation then quotes a two-dimensional carrier density and sheet conductivity.

The adaptation is straightforward, but it should be stated explicitly:

```text
In d dimensions, V denotes the normalization measure. For the 2-D validation, replace V by sample area and sigma_1 by sheet conductivity; the algebra and inequality are unchanged.
```

Without this sentence, a careful referee can object that the dimensional convention changes silently.

---

## 8. Continuum / thermodynamic-limit language — PASS WITH ONE SENTENCE

The energy-shell ranks and projectors are cleanest in finite volume. The thermodynamic limit can then be taken after the inequalities are established.

Rev4 begins in finite volume, so the construction is defensible. A sentence immediately after the active-population definitions stating that all ranks are finite-volume ranks before the thermodynamic limit would improve readability.

This is not a mathematical defect.

---

## 9. Dirac and parabolic validation — PASS

The global total-population validation family remains internally consistent:

```text
2-D massless Dirac: 1/2
3-D massless Dirac: 2/3
3-D massive Dirac at Delta/kBT=2.398: 0.794684
equal-mass 3-D parabolic: 1
```

The unequal-mass nondegenerate ratio

```math
[4m_em_h/(m_e+m_h)^2]^{3/4}
```

has the correct symmetry under `m_e <-> m_h`, is bounded by unity, and reaches equality only at equal masses.

---

## 10. Scope discipline — PASS

Rev4 correctly refuses to claim:

```text
universal dark-current floor;
universal generation-rate floor;
universal D* bound;
universal finite-bandwidth noise floor;
coverage of neutral excitons or indirect absorption;
unconstrained external-absorptance bound in arbitrary photonic structures.
```

This scope should remain frozen.

---

## 11. Prior-art / novelty review — HIGH RISK, NO DIRECT COLLISION FOUND

The strongest rejection argument remains that the ingredients are elementary:

```text
Fermi occupations / Pauli blocking;
Kubo-Greenwood;
operator norm and rank inequalities.
```

The paper is viable only if the **composed inverse windowed theorem** is not already standard.

Adjacent established results include:

1. phase-space filling: carrier density -> reduced optical oscillator strength;
2. ordinary/generalized f-sum rules: conductivity moments -> total charge/kinetic quantities;
3. quantum-geometric optical sums: response moments -> Wannier spread / metric;
4. classic infrared alpha/G_th material criteria;
5. semiconductor-laser low-carrier band engineering;
6. warm-dense-matter use of the TRK conductivity sum to infer ionization/free-electron count.

The warm-dense-plasma comparator is especially worth recording:

```text
Phys. Rev. Research 2, 023260 (2020)
```

uses the Thomas-Reiche-Kuhn sum rule to infer ionization degree from optical conductivity. This is not the same theorem: it uses a conventional total-electron sum rule rather than a cross-mu thermal kernel and does not derive a minimum thermal electron-hole excitation population from surviving low-energy interband weight.

Focused searches still did not reveal the exact kernel

```math
E/[exp(E/2kBT)-1]
```

combined with a per-shell optical-resource/state-count inequality.

```text
DIRECT COLLISION: NOT FOUND.
PRIORITY: NOT ESTABLISHED.
NOVELTY RISK: HIGH.
```

---

## 12. Overall disposition

```text
POINTWISE FERMI ALGEBRA: PASS
KUBO NORMALIZATION: PASS
BASIS INVARIANCE: PASS
ACTIVE-SUBSPACE TRACE-RANK THEOREM: PASS
FINITE-WINDOW EQUALITY LOGIC: PASS
PARABOLIC VALIDATION: PASS
DIRAC VALIDATION: PASS
DETECTOR CLAIM SCOPE: PASS
LATIN-u NOTATION: MINOR FIX REQUIRED
2-D NORMALIZATION: MINOR FIX REQUIRED
DIRECT PRIOR-ART COLLISION: NOT FOUND
NOVELTY: NOT ESTABLISHED / HIGH RISK
```

## Recommendation

Issue one clean revision that:

```text
1. replaces the remaining Greek-nu tokens by Latin u_B;
2. adds the 2-D normalization sentence;
3. clarifies that active population is a support-dimension count;
4. leaves every scientific claim otherwise unchanged.
```

After those corrections, further theory development is not justified by the present referee record. The next stage should be bibliography verification, journal-fit selection, and typesetting—not additional mechanisms.