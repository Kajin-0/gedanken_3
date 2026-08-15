# Experiment 12 — Manuscript Viability Review

**Date:** 2026-08-14  
**Disposition:** **PROVISIONAL PASS — SHORT THEORETICAL MANUSCRIPT JUSTIFIED / PRIORITY CLAIM NOT ESTABLISHED / CLAIM SCOPE MUST REMAIN NARROW**

## 1. Decision question

After hostile review, scope reduction, multiple exact/model validations, and a focused novelty audit, is the surviving result sufficiently general, nontrivial, and physically meaningful to justify a manuscript draft?

Current answer:

```text
YES — provisionally.
```

This is a decision to **draft and attack a paper**, not a claim that the theorem is certainly new or publishable.

---

## 2. Surviving core result

For any selected positive-frequency window `B`, direct one-particle transitions crossing the equilibrium chemical potential obey

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

For an intrinsic neutral direct interband absorber,

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2v_{*,B}^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

The result follows from:

```text
exact Fermi occupation inequality;
Kubo-Greenwood optical spectral measure;
finite per-state selected velocity-matrix strength.
```

No assumed DOS, effective mass, Dirac dispersion, or recombination model is required.

---

## 3. Why the result is manuscript-worthy enough to test

### 3.1 It generalized instead of collapsing

The founding two-flat-manifold result survived removal of:

```text
flat dispersion;
equal conduction/valence degeneracy;
one-to-one transition counting;
frequency-bin additivity;
Bloch momentum / translational invariance;
Dirac-specific kinematics.
```

The state-reuse loophole closes through the finite row/column velocity-strength budget.

### 3.2 It has exact equality families

The theorem is not merely a loose dimensional estimate.

Exact saturation occurs for:

```text
equal flat resonant manifolds;
3-D mirror-symmetric parabolic direct bands with m_e=m_h and constant one-to-one matrix element.
```

### 3.3 It is quantitatively nontrivial away from equality

Known exact models give:

```text
2-D neutral massless Dirac / graphene:  0.5000 of exact thermal population
3-D massless Dirac:                     0.6667
3-D massive Dirac, 10 um / 300 K:       0.794684
```

For unequal parabolic masses at the same 10-um / 300-K gap:

```text
m_h/m_e = 2:    0.9161
m_h/m_e = 5:    0.6455
m_h/m_e = 10:   0.4379
```

Thus the theorem remains substantial in realistic asymmetric systems and approaches equality as electron-hole optical/thermal structure becomes symmetric.

### 3.4 It yields a genuine low-energy conclusion

Because

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}\to2k_BT,
```

fixed low-energy direct cross-`mu` optical spectral weight cannot coexist with vanishing thermal quasiparticle population at fixed microscopic velocity-strength resource simply by lowering the transition energy.

This conclusion is DOS-model independent inside the stated quasiparticle class.

---

## 4. What is already known and therefore cannot be sold as novelty

Do not claim novelty for:

```text
Pauli blocking / phase-space filling;
Kubo-Greenwood conductivity;
ordinary/generalized optical f-sum rules;
light/symmetric bands reducing semiconductor-laser carrier requirements;
Dirac finite-T optical conductivity;
quantum-geometric control of oscillator strength;
classic infrared alpha/G_th material criteria.
```

The candidate contribution is only the **inverse finite-temperature spectral-weight inequality** and its resource-conditioned population interpretation.

---

## 5. Main novelty risk

The proof is short.

A skeptical referee can say:

> This is just Pauli blocking plus a trivial bound on the optical matrix elements.

That criticism is not mathematically wrong about the ingredients.

The paper must therefore demonstrate value through:

```text
generality of the inverse statement;
explicit arbitrary-window formulation;
robustness to multiband state reuse and static disorder;
tight equality conditions;
nontrivial Dirac and parabolic validations;
clear distinction from f-sums and alpha/G_th;
use as a necessary material admissibility condition rather than a new empirical FOM.
```

If the manuscript cannot make that case concisely, the branch should be closed rather than inflated.

---

## 6. Scope that must appear in title/abstract/conclusion

The theorem concerns

```text
thermal quasiparticle population
versus
intrinsic direct cross-mu optical spectral weight.
```

It is **not** presently a theorem for:

```text
dark current;
thermal generation rate;
D*;
finite-bandwidth detector noise;
bound-exciton / collective absorbers;
phonon-assisted indirect absorbers;
arbitrary cavity-enhanced external absorptance.
```

Localized one-particle states still obey the population theorem but may contribute weakly to dc current.

---

## 7. Suggested manuscript framing

### Preferred title family

```text
Thermal population cost of interband optical spectral weight
```

or

```text
A finite-temperature spectral-weight bound for direct interband absorbers
```

Avoid titles containing:

```text
ultimate detector limit;
dark-current limit;
fundamental D* bound;
universal photodetector theorem.
```

### Central message

A finite amount of low-energy cross-Fermi optical spectral weight requires either:

```text
finite equilibrium electron-hole excitation population,
```

or

```text
large microscopic velocity-matrix strength per participating state.
```

That resource tradeoff is independent of a chosen DOS model.

---

## 8. Suggested paper structure

```text
I. Motivation: absorption versus thermal quasiparticle population
II. Pointwise Fermi lemma
III. Arbitrary-window spectral-weight theorem
IV. Microscopic velocity resource and equality conditions
V. Exact / quantitative validations
    A. parabolic direct bands
    B. 2-D and 3-D Dirac bands
VI. Relation to phase-space filling, f-sums, and infrared detector FOMs
VII. Scope: disorder, localization, excitons, photonics
VIII. Conclusion
```

The main text should stay short. Fluctuation corollary, all-transition fallback, and detailed derivations can go to appendices/supplement.

---

## 9. Venue realism

If the novelty audit continues to survive, plausible targets are a short theoretical paper in a venue such as:

```text
Physical Review B — only if condensed-matter generality and novelty are convincing;
Journal of Applied Physics — strong fit for a rigorous semiconductor/IR detector theorem;
APL Photonics / Journal of Photonics for Energy — if detector/material interpretation is emphasized.
```

Do not choose a venue until the first complete draft has survived an adversarial manuscript review.

---

## 10. Final viability disposition

```text
THEOREM RIGOR: PASS AFTER CORRECTIONS
MODEL-INDEPENDENCE WITHIN CLASS: PASS
QUANTITATIVE TIGHTNESS: PASS
DIRECT PRIOR-ART COLLISION: NOT FOUND
CONCEPTUAL PRIOR ART: STRONG
DETECTOR SIGNIFICANCE: NECESSARY-CONDITION LEVEL, NOT FULL PERFORMANCE LIMIT
MANUSCRIPT DRAFT: JUSTIFIED
PRIORITY / NOVELTY CLAIM: NOT YET ESTABLISHED
```

## Next action

Write a compact Rev0 manuscript around `THEOREM_CORE_2026-08-14.md`, with no dark-current overclaim. Then subject the draft itself to an extreme adversarial review before deciding whether the project has reached the paper-level objective.
