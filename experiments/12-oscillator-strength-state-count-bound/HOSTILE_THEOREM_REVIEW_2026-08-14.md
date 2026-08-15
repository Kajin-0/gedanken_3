# Experiment 12 — Hostile Theorem Review

**Date:** 2026-08-14  
**Role:** adversarial referee / theorem audit  
**Disposition:** **MAJOR REVISION — CORE INEQUALITY SURVIVES / TWO FORMULATION DEFECTS REQUIRE CORRECTION / DETECTOR CLAIM MUST REMAIN NECESSARY-CONDITION ONLY**

## 1. Claim under review

The branch currently argues that low-energy direct interband optical spectral weight in an equilibrium independent-quasiparticle absorber requires a nonzero population of thermally excited upper-state electrons and lower-state holes.

The strongest current formula was written as

```math
n_e+n_h
\ge
\frac{2}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
```

This review attacks the theorem rather than attempting to defend the project.

---

# 2. Objection: `sigma_inter` is too broad and can make the theorem false as stated

At finite temperature, an optical spectrum can contain transitions entirely below `mu` or entirely above `mu`. The proof counts only transitions

```math
E_v<\mu<E_c.
```

Therefore the conductivity entering the theorem cannot be generic `sigma_inter`.

It must be the positive-frequency **cross-chemical-potential direct-transition conductivity**

```math
\boxed{\sigma_1^{cross}(\omega)}.
```

That is the Kubo contribution from transitions whose initial one-particle state lies below `mu` and final state lies above `mu`.

### Disposition

```text
OBJECTION VALID.
```

Required correction: replace loose `inter` notation by `cross` in theorem statements. Ordinary semiconductor near-gap interband absorption is a principal physical realization, but the mathematical theorem is about cross-`mu` transitions.

---

# 3. Objection: a global finite velocity norm need not exist in a continuum

A continuum Schrödinger velocity operator is unbounded at arbitrarily high energy. Therefore an all-frequency theorem divided by one finite global `v_*` is not generally useful.

### Resolution — arbitrary spectral-window theorem

Let `B` be any measurable set of positive optical frequencies. Define the selected transition set

```math
\mathcal T_B
=\{(c,v):E_v<\mu<E_c,\ (E_c-E_v)/\hbar\in B\}.
```

For each upper state define the selected row strength

```math
R_c(B)
=\sum_{v:(c,v)\in\mathcal T_B}|v_{cv}|^2,
```

and for each lower state the selected column strength

```math
C_v(B)
=\sum_{c:(c,v)\in\mathcal T_B}|v_{cv}|^2.
```

Define

```math
\boxed{
v_{*,B}^2
=\max\left[
\sup_cR_c(B),
\sup_vC_v(B)
\right].
}
```

This is a finite **spectral-window oscillator-strength resource** whenever the selected matrix block has finite row/column norms. No globally bounded continuum velocity is required.

The exact pointwise Fermi inequality then gives

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

For an intrinsic neutral absorber,

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

The previous all-frequency form is recovered only when a finite `v_{*,(0,infinity)}` exists.

### Disposition

```text
OBJECTION VALID; THEOREM STRENGTHENED BY REFORMULATION.
```

---

# 4. Stronger exact hierarchy — remove `v_*` from the first inequality

The proof actually contains a stronger quantity than the population bound.

Define the thermally weighted selected velocity-strength density

```math
\mathcal R_B
=\frac1V
\left[
\sum_c p_cR_c(B)
+
\sum_v h_vC_v(B)
\right].
```

The pointwise Fermi inequality gives **without any maximum-velocity assumption**

```math
\boxed{
\mathcal R_B
\ge
\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

Then simply

```math
\mathcal R_B
\le
v_{*,B}^2(n_e+n_h),
```

which yields the carrier-population corollary.

The theorem should therefore be presented as the hierarchy

```math
\boxed{
\frac{2}{\pi e^2}
\int_BK_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega
\le
\mathcal R_B
\le
v_{*,B}^2(n_e+n_h),
}
```

where

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
```

This is conceptually stronger and makes clear that `v_*` is a second-stage microscopic resource, not part of the fundamental Fermi/Kubo inequality.

---

# 5. Objection: `v_*` is arbitrary

In the windowed formulation `v_{*,B}` is defined directly from the selected velocity-matrix block. It can also be upper-bounded without assuming a universal speed.

Completeness gives

```math
R_c(B)
\le
\sum_n|\langle c|\hat v_i|n\rangle|^2
=\langle c|\hat v_i^2|c\rangle,
```

and similarly for lower states.

Thus a convenient sufficient microscopic ceiling is the largest relevant one-body velocity second moment.

For a bounded orthonormal Wannier/tight-binding Hamiltonian, Experiment 10 further gives

```math
v_{*,B}\le V_i^{hop}
=\frac1\hbar\sum_R|R_i|\|H_R\|.
```

### Disposition

```text
OBJECTION DOES NOT KILL THE THEOREM.
```

The manuscript must not call `v_*` universal or chemistry-independent.

---

# 6. Objection: the result is only Pauli blocking written backwards

This is the strongest novelty objection.

The pointwise inequality is indeed elementary Fermi algebra. Semiconductor phase-space-filling literature has long calculated

```text
carrier occupation -> bleaching of an optical transition.
```

The nontrivial extra step in Experiment 12 is that arbitrary multiband state reuse cannot evade the inverse bound because each upper/lower state has a finite total selected velocity-matrix strength. Kubo then converts this into a spectral integral over a measurable response.

Thus the mathematical ingredients are established, but the composed statement is

```text
surviving cross-mu optical spectral weight
+ finite per-state velocity-strength budget
-> minimum thermal excitation population.
```

### Disposition

```text
NOVELTY RISK HIGH; NO DIRECT COLLISION YET FOUND.
```

A paper cannot sell algebraic sophistication. It must sell the general inverse constraint, DOS-independence, multiband/state-reuse robustness, and quantitative tightness.

---

# 7. Objection: ordinary TRK/f-sum should already imply the result

The ordinary full `f`-sum constrains total optical spectral weight using all-electron/kinetic quantities. It does not by itself bound the population of thermally excited upper-state electrons and lower-state holes with the Experiment-12 kernel.

Moreover, generic multiband effective-mass/oscillator identities contain signed remote-band contributions and do not provide a positive universal numerical ceiling on the selected low-energy cross-`mu` velocity block.

### Disposition

```text
NO DIRECT REDUCTION TO THE STANDARD f-SUM IDENTIFIED.
```

The manuscript must compare explicitly against standard/generalized `f`-sum rules rather than merely asserting difference.

---

# 8. Objection: dimensions / Kubo normalization

For angular frequency, the clean independent-particle positive-frequency cross conductivity is

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}\hbar\right).
```

Therefore

```math
\int_B
K_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega
=
\frac{\pi e^2}{V}
\sum_{(c,v)\in\mathcal T_B}
\frac{D_{cv}|v_{cv}|^2}
{e^{E_{cv}/(2k_BT)}-1}.
```

No missing factor of `hbar` is present when the delta function is written in angular-frequency form.

### Disposition

```text
PASS.
```

Older flat-manifold formulas written with `delta(E-hbar omega)` should be normalized consistently if reused.

---

# 9. Objection: static disorder invalidates band language

The proof does not require Bloch momentum. It can be formulated using exact eigenstates of an arbitrary static one-body Hamiltonian. Static disorder therefore changes the transition graph and matrix elements but does not invalidate the inequality.

### Disposition

```text
PASS, WITH TERMINOLOGY CORRECTION.
```

Use `lower/upper exact eigenstates` in the theorem. `Valence/conduction` is a semiconductor specialization.

---

# 10. Objection: excitons provide an immediate counterexample

Correct.

A bound neutral exciton can carry large low-energy oscillator strength while the free electron-hole continuum remains at a higher energy. The useful photocurrent then depends on a separate dissociation process.

### Disposition

```text
OBJECTION VALID AS A SCOPE LIMIT, NOT A COUNTEREXAMPLE TO THE STATED INDEPENDENT-PARTICLE THEOREM.
```

The theorem class must be stated explicitly as

```text
independent-quasiparticle direct cross-mu charge absorbers,
```

or systems reducible to that description over the relevant optical/thermal window.

---

# 11. Objection: localized states can absorb but produce negligible dark current

Correct.

Static localization does not evade the thermal **population** inequality, but it can strongly reduce transport/collection. Quantum-dot and localized-state detectors show that optical occupation and terminal dark current are not interchangeable.

### Disposition

```text
DETECTOR CLAIM MUST BE NARROWED.
```

Experiment 12 is a necessary material-state-count condition, not a universal dark-current or `D*` theorem.

Do not infer a current floor without an independent electrical-activity/kinetic hypothesis.

---

# 12. Objection: finite response time should convert population into generation noise

A proposed universal conversion

```math
G_{th}\ge n_{th}/\tau_{response}
```

is false.

A depleted photovoltaic detector can have a long intrinsic recombination lifetime and low thermal generation while field-driven collection is fast. Response time and equilibrium recombination residence time are not universally identical.

### Disposition

```text
REJECTED COROLLARY.
```

This failure is already documented in `FAILED_RESPONSE_TIME_TO_GENERATION_BOUND_2026-08-14.md`.

---

# 13. Objection: photonic resonators invalidate an absorptance bound

They invalidate a universal conversion from external absorptance to intrinsic material sheet conductivity unless photonic resources are constrained.

They do **not** invalidate the intrinsic conductivity theorem itself.

### Disposition

```text
PASS FOR MATERIAL CONDUCTIVITY THEOREM; EXTERNAL-ABSORPTANCE COROLLARY CONDITIONAL.
```

Do not headline the old single-pass absorbance-number witness.

---

# 14. Objection: phenomenological broadening can move high-energy oscillator strength into the thermal window

A static disordered one-body Hamiltonian is safe if exact eigenstates are used. A phenomenological Lorentzian applied to clean transitions is not the same thing: interaction-generated lifetime broadening belongs to a many-body spectral-function problem and is outside the proof.

### Disposition

```text
SCOPE LIMIT REQUIRED.
```

---

# 15. Equality / tightness

The carrier-population bound is saturated only under restrictive conditions:

```text
for every optically weighted transition, upper/lower energies are symmetric about mu;
thermally occupied states carry no unused selected velocity strength;
selected row/column strengths saturate the common ceiling v_{*,B}^2;
there are no extra thermally populated states outside the selected optical graph.
```

The original equal flat-manifold construction realizes this structure exactly.

Nontrivial dispersive checks show the bound is not vacuous:

```text
2-D neutral massless Dirac:  0.5 of exact thermal population
3-D massless Dirac:          0.6667
3-D massive Dirac,
10 um / 300 K:               0.794684
```

This quantitative tightness is a major part of the scientific case.

---

# 16. 10-um single-pass witness needs correction

The earlier witness used a nominal `10%` bandwidth but treated the thermal kernel as constant at the 10-um threshold energy.

For a detector whose cutoff is 10 um, a physically natural frequency interval is

```math
\omega\in[\omega_g,1.1\omega_g],
```

not a symmetric interval extending below the band edge.

The exact window theorem should be integrated over this interval. Relative to the constant-kernel approximation, the exact integral is smaller by about `7.81%` at 300 K.

For `n_b=3.5`, `A>=0.90`, and the 10%-above-edge single-pass interval, the corrected approximate electron-column lower bounds are

```text
v_* (m/s)       Sigma_e,min (cm^-2)
5.0e5             3.6598e12
1.0e6             9.1495e11
1.07e6            7.9915e11
2.0e6             2.2874e11
3.0e6             1.0166e11
```

This witness remains conditional on material-dominant single-pass absorption and should be secondary to the intrinsic spectral theorem.

---

# 17. Referee verdict

```text
MATHEMATICAL CORE: PASS AFTER FORMULATION CORRECTIONS.
GLOBAL-v_* FORM: TOO STRONG / SOMETIMES TRIVIAL; REPLACE BY WINDOWED RESOURCE.
CROSS-mu NOTATION: MUST CORRECT.
DIRAC CHECKS: STRONG.
DARK-CURRENT CLAIM: NOT PROVEN; DO NOT MAKE IT.
EXCITON ESCAPE: REAL AND MUST BE EXPLICIT.
NOVELTY: PLAUSIBLE BUT HIGH-RISK.
MANUSCRIPT READINESS: NOT YET; ONE MORE theorem-compression + literature pass required.
```

The correct next step is to rewrite the branch around the spectral-window hierarchy, then reassess whether the surviving theorem is substantial enough for a short theoretical manuscript.
