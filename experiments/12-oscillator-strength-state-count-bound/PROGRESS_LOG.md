# Progress Log — Experiment 12: Oscillator-Strength / Thermal-State-Count Bound

## 2026-08-14 — branch opened provisionally

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Question: can fixed low-energy direct-interband optical spectral weight coexist with arbitrarily small equilibrium thermal quasiparticle population when the microscopic interband velocity resource remains finite?

Opened only after many preceding candidate premises were rejected against established detector/statistical/optical theory.

---

## 2026-08-14 — exact two-manifold theorem

For flat conduction/valence manifolds separated by `E_gamma`, exact Fermi occupations and the singular-value/rank optical-strength budget gave

```math
\boxed{
N_{th}
\ge
\frac{S_{abs}}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

Kubo-Greenwood converted this to

```math
\boxed{
n_{th}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma}{e^{E_\gamma/(2k_BT)}-1}.
}
```

At fixed integrated spectral weight,

```math
n_{th,min}
\to
\frac{2k_BT}{\pi e^2v_{max}^2}W_\sigma
```

as `E_gamma -> 0`.

```text
FIRST EXACT RESULT SURVIVED.
NOVELTY NOT ESTABLISHED.
```

---

## 2026-08-14 — arbitrary dispersive multiband generalization

State reuse across different transitions did not break the premise.

For every transition with `E_v < mu < E_c`,

```math
\boxed{
\frac{2D_{cv}}{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v.
}
```

This closed the main frequency-bin double-counting loophole when combined with finite row/column velocity strength.

---

## 2026-08-14 — thermal optical spectral-weight inequality

Kubo-Greenwood produced the thermal kernel

```math
K_T(E)=E/[e^{E/(2k_BT)}-1].
```

For a finite velocity-strength resource the population is bounded by the thermally weighted cross-`mu` optical conductivity.

The low-energy kernel tends to `2 kBT`, so the carrier-population floor does not vanish merely because the direct transition energy tends to zero at fixed optical spectral weight and fixed velocity resource.

---

## 2026-08-14 — independent validation

Reproducible Dirac calculations were added.

```text
2-D neutral massless Dirac / graphene: bound/exact = 1/2
3-D massless Dirac:                    bound/exact = 2/3
```

For the 3-D massive-Dirac family:

```text
Delta/kBT       bound/exact
0                0.6667
0.5              0.6863
1.0              0.7191
2.39796146       0.794684
4.0              0.8454
8.0              0.9045
16.0             0.9459
```

At the 10-um / 300-K witness, the theorem recovers about `79.5%` of the exact thermal population without using the Dirac density of states in the proof.

---

## 2026-08-14 — many-body boundary

Bound excitons were identified as a genuine free-quasiparticle escape:

```text
neutral low-energy excitonic oscillator strength can lie below the free e-h continuum;
photocurrent then requires a separate dissociation process.
```

The theorem class was explicitly restricted to

```text
independent-quasiparticle direct cross-mu charge absorbers.
```

Static one-particle disorder does not automatically break the proof if exact eigenstates are used. Interaction-generated many-body spectral functions lie outside scope.

---

## 2026-08-14 — detector-level overclaim rejected

An attempted conversion

```math
G_{th}\gtrsim n_{th}/\tau_{response}
```

was rejected. A depleted photodiode can have long recombination lifetime but fast field-driven collection/transit.

Therefore the thermal-population theorem is not a universal dark-current, thermal-generation, `D*`, or bandwidth theorem.

---

## 2026-08-14 — basis-invariant shell resource

A hostile review found that a raw row/column maximum could depend on basis choice inside an exact degenerate eigenspace.

The resource was reformulated with exact energy-shell projectors and projected velocity-operator norms. This fixed the basis-invariance defect without mixing distinct-energy equilibrium states.

---

## 2026-08-14 — parabolic equality family

For ideal 3-D parabolic direct bands with constant one-to-one optical matrix element, equal electron and hole masses produce mirror symmetry about the intrinsic chemical potential.

For the global direct spectrum the population theorem is exactly saturated at all temperatures.

For unequal masses in the nondegenerate global limit,

```math
\boxed{
\frac{n_{bound}}{n_{exact}}
=\left[
\frac{4m_em_h}{(m_e+m_h)^2}
\right]^{3/4}.
}
```

This showed the theorem is not a Dirac-specific artifact.

---

## 2026-08-14 — manuscript Rev0–Rev3 and notation failure

A short theory manuscript was drafted and subjected to hostile review.

The major mathematical-presentation defect in Rev0 was the basis dependence of the optical resource. Rev1 fixed it. Rev2/Rev3 tightened scope around integrated spectral weight and moved the LWIR example to an appendix.

A recurring LaTeX escape regression rendered Greek `nu_B` in several places where Latin `u_B` was intended. Rev3 was preserved with an explicit notation erratum rather than silently rewritten.

No theorem coefficient changed in that erratum.

---

## 2026-08-14 — finite-window equality correction and active-subspace theorem

An independent external-style reread found that the statement

```text
equal-mass parabolic bands saturate the total-population bound for arbitrary B
```

was too broad. For a partial spectral window, thermally populated states outside the selected optical graph make the total-population inequality strict.

This led to a stronger result rather than a mere wording patch.

For each exact upper/lower energy shell define selected optical blocks `A` and `B`, their support ranks, and

```math
n_{e,B}^{act}
=V^{-1}\sum_{\epsilon_c>\mu}f(\epsilon_c)\operatorname{rank}A_{\epsilon_c,B},
```

```math
n_{h,B}^{act}
=V^{-1}\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]\operatorname{rank}B_{\epsilon_v,B}.
```

Using

```math
Tr(XX^\dagger)\le\|X\|_{op}^2\operatorname{rank}X
```

gave the basis-invariant active-subspace hierarchy.

For the ideal equal-mass one-to-one parabolic model:

```text
active-subspace theorem: exact saturation for any selected window;
total-population theorem: exact saturation only for the full relevant direct spectrum.
```

Controlling derivation:

`ACTIVE_SUBSPACE_REFINEMENT_2026-08-14.md`

---

## 2026-08-14 — Rev4 external-style review

`MANUSCRIPT_REV4_EXTERNAL_STYLE_REVIEW_2026-08-14.md` found:

```text
POINTWISE FERMI ALGEBRA: PASS
KUBO NORMALIZATION: PASS
BASIS INVARIANCE: PASS
ACTIVE-SUBSPACE TRACE-RANK THEOREM: PASS
FINITE-WINDOW EQUALITY LOGIC: PASS
PARABOLIC VALIDATION: PASS
DIRAC VALIDATION: PASS
DETECTOR CLAIM SCOPE: PASS
```

Minor issues:

```text
resource notation regression;
2-D normalization needed to be explicit;
active population needed to be described as a support-dimension count.
```

No new theory was required.

---

## 2026-08-14 — final novelty comparator

Bethkenhagen et al., *Physical Review Research* **2**, 023260 (2020), was added as an important adjacent precedent: dynamic conductivity plus the Thomas-Reiche-Kuhn sum rule is used to infer plasma ionization/free-electron count.

Thus the broad idea

```text
conductivity spectral weight -> particle count
```

is established and is not a novelty claim for Experiment 12.

No direct source was identified with the Experiment-12 combination

```text
cross-mu direct conductivity
+ E/[exp(E/2kBT)-1] thermal kernel
+ per-shell optical-velocity capacity
-> minimum thermal optical-support population.
```

```text
DIRECT COLLISION: NOT FOUND
PRIORITY: NOT ESTABLISHED
NOVELTY: NOT ESTABLISHED
NOVELTY RISK: HIGH
```

---

## 2026-08-14 — Rev6 submission-candidate text

To eliminate the recurring `u/nu` transcription ambiguity permanently, Rev6 changed the resource notation to

```math
v_B^{cap}.
```

The controlling hierarchy is

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

Rev6 also states explicitly that 2-D uses area and sheet conductivity, and that `n_B^act` is a support-dimension population rather than an oscillator-strength-weighted participation ratio.

File:

`MANUSCRIPT_REV6_2026-08-14.md`

---

## 2026-08-14 — final hostile QA

`MANUSCRIPT_REV6_FINAL_QA_2026-08-14.md` records:

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

## Final disposition

```text
THEOREM-LEVEL SCIENCE: PASS FROM INTERNAL ADVERSARIAL QA
CURRENT MANUSCRIPT: REV6
NOVELTY: NOT ESTABLISHED
NO MORE THEORY BY DEFAULT
```

Next work is journal selection, journal-specific citation/style audit, typesetting, and independent review of the rendered manuscript. Do not add mechanisms merely to make the paper larger.
