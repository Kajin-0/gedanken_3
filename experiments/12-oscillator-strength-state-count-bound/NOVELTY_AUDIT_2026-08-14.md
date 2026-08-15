# Experiment 12 — Focused Novelty Audit

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** **NO DIRECT COLLISION FOUND IN FOCUSED AUDIT / SUBSTANTIAL CONCEPTUAL ADJACENCY / PRIORITY NOT ESTABLISHED**

## 1. Candidate claim being audited

The current core result for independent-quasiparticle direct-interband charge absorbers is

```math
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega,
}
```

where `sigma_1^cross` is the positive-frequency direct optical conductivity from lower single-particle states below `mu` to upper states above `mu`, and `v_*` is a finite row/column velocity-strength resource.

For an intrinsic neutral absorber,

```math
n_e=n_h=n_{th},
```

so

```math
\boxed{
n_{th}
\ge
\frac{1}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

The question is not whether Kubo, Pauli blocking, or optical sum rules are known. They are. The audit asks whether the **specific finite-temperature inverse bound from useful interband spectral weight to thermally excited charge population** is already established or trivially equivalent to a standard theorem.

---

## 2. Search families

Focused searches covered combinations of:

```text
finite-temperature optical conductivity + carrier density + bound/inequality;
interband spectral weight + thermal carrier density;
Pauli blocking + carrier density + optical sum;
phase-space filling + oscillator strength + carrier concentration;
generalized f-sum + finite temperature;
quantum metric / inverse-frequency optical sum;
quantum Fisher information + dynamical susceptibility;
graphene finite-temperature interband/Drude spectral-weight transfer;
infrared detector alpha/G_th material figures of merit.
```

The audit also checked literature outside infrared detectors because the theorem could plausibly exist as a general linear-response inequality.

---

## 3. Comparator A — classic infrared detector `alpha/G_th`

### Primary comparator

J. Piotrowski and W. Gawron, **“Ultimate performance of infrared photodetectors and figure of merit of detector material,”** *Infrared Physics & Technology* **38**, 63–68 (1997), DOI `10.1016/S1350-4495(96)00030-8`.

This work states that ultimate detector performance is controlled by the ratio

```math
\alpha/G_{th}
```

and uses it to compare IR detector materials.

### Relation to Experiment 12

The conceptual motivation is very close:

```text
strong useful absorption is desirable;
thermal electronic activity is undesirable.
```

But the mathematical object is different.

Piotrowski/Gawron take

```text
absorption coefficient alpha
and
thermal generation rate G_th
```

as material quantities arising from the chosen semiconductor/recombination model.

Experiment 12 instead derives, before choosing a DOS or recombination law,

```text
required direct-interband optical spectral weight
-> minimum equilibrium thermally excited quasiparticle population
```

conditional only on a finite microscopic velocity-strength resource.

The theorem does **not** replace `alpha/G_th`; it supplies a new necessary population constraint that can exist upstream of a rate model.

### Collision verdict

```text
ADJACENT, NOT IDENTICAL.
```

---

## 4. Comparator B — semiconductor phase-space filling / Pauli blocking

### Representative primary papers

- D. Huang, J.-I. Chyi, and H. Morkoc, **“Carrier effects on the excitonic absorption in GaAs quantum-well structures: Phase-space filling,”** *Phys. Rev. B* **42**, 5147 (1990).
- N. H. Kwong, G. Rupper, and R. Binder, **“Self-consistent T-matrix theory of semiconductor light-absorption and luminescence,”** *Phys. Rev. B* **79**, 155205 (2009), DOI `10.1103/PhysRevB.79.155205`.
- Modern pump-probe/semiconductor-Bloch literature continues to use occupation factors of the form `f_v-f_c` to calculate bleaching versus carrier distribution.

### Relation to Experiment 12

Phase-space filling establishes the **forward map**

```text
specified carrier occupations/density
-> reduced optical absorption / oscillator strength.
```

Experiment 12 inverts this logic under a microscopic matrix-strength constraint:

```text
specified surviving equilibrium interband spectral weight
+ finite v_*
-> lower bound on total thermal occupation.
```

The inversion is nontrivial only because a state can couple to many others; the row/column velocity-strength budget closes that state-reuse loophole.

No searched phase-space-filling paper was found to state the global thermally weighted inverse inequality.

### Collision verdict

```text
STRONG CONCEPTUAL ADJACENCY; NO DIRECT THEOREM COLLISION LOCATED.
```

This is probably the most likely reviewer route for arguing that the result is “obvious Pauli blocking.”

---

## 5. Comparator C — graphene finite-temperature interband optical weight

Graphene and Dirac-material optical-conductivity literature explicitly treats finite-temperature/interband Pauli blocking and spectral-weight redistribution between interband absorption and intraband/Drude response.

This is important because Experiment 12 is exactly testable there.

For neutral 2-D massless Dirac quasiparticles, the theorem gives

```math
n_e^{bound}/n_e^{exact}=1/2.
```

For a 3-D massless Dirac cone the ratio is `2/3`, and for the 10-um / 300-K finite-gap massive-Dirac witness it is `0.794684`.

Thus known Dirac optical formulas **validate** the inequality but do not appear to state it as a general population bound.

### Collision verdict

```text
MODEL-SPECIFIC CONTENT KNOWN; GENERAL INEQUALITY NOT LOCATED.
```

A manuscript must cite the finite-temperature Dirac optical literature prominently and present these cases as checks, not discoveries.

---

## 6. Comparator D — conventional and generalized `f`-sum rules

### Primary comparator

H. Watanabe and M. Oshikawa, **“Generalized f-sum rules and Kohn formulas on nonlinear conductivities,”** *Phys. Rev. B* **102**, 165137 (2020), DOI `10.1103/PhysRevB.102.165137`.

The conventional and generalized `f`-sum rules are exact conductivity constraints valid broadly, including finite-temperature stationary states.

### Difference

The conventional sum constrains conductivity spectral weight using quantities such as total charge density, kinetic energy, or derivatives of the Hamiltonian.

Experiment 12 instead uses

```math
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}
```

and bounds the density of **thermally excited upper-state electrons and lower-state holes**, not the density of all electrons.

The Experiment-12 result also requires the finite crossing-transition velocity-strength resource `v_*`; it is not a consequence of a universal bare-mass full spectral sum.

### Collision verdict

```text
DISTINCT OBSERVABLE AND THERMAL KERNEL.
```

---

## 7. Comparator E — quantum-geometric optical sums

### Primary comparator

L. F. Cardenas-Castillo et al., **“Detecting the spread of valence-band Wannier functions by optical sum rules,”** *Phys. Rev. B* **110**, 075203 (2024), DOI `10.1103/PhysRevB.110.075203`.

This work relates frequency-integrated optical response to the gauge-invariant spread / quantum metric of valence-band Wannier functions, including 2-D absorbance and 3-D dielectric response.

### Difference

Those sum rules use optical frequency moments chosen to recover quantum geometry/Wannier spread.

Experiment 12 instead has a finite-temperature Fermi kernel and targets thermally excited quasiparticle population.

### Collision verdict

```text
DIFFERENT SUM-RULE TARGET AND KERNEL.
```

---

## 8. Comparator F — QFI / fluctuation–dissipation response integrals

Finite-temperature quantum-Fisher-information and generalized covariance literature relates dynamic susceptibilities to fluctuation measures using thermal response kernels, commonly involving `tanh(beta hbar omega/2)` or related KMS factors.

Representative literature includes the linear-response/QFI work of Shitara and Ueda and subsequent dynamic-susceptibility entanglement witnesses.

The kernels and bounded quantities found in the focused audit are not equivalent to

```math
\frac{\hbar\omega}{e^{\hbar\omega/(2k_BT)}-1}
```

multiplying the direct interband charge conductivity to bound thermally excited quasiparticle density.

### Collision verdict

```text
NO DIRECT KERNEL/OBSERVABLE COLLISION LOCATED.
```

---

## 9. Comparator G — detailed-balance / van Roosbroeck–Shockley relations

Detailed balance relates equilibrium radiative recombination to absorption and the thermal photon field. This is established and was already treated as prior art in Experiment 10.

It does not provide the same statement:

```text
optical spectral weight
-> minimum thermally excited electronic state population
conditional on electronic velocity strength.
```

Its thermal Bose factor refers to photons; the Bose-like half-transition factor in the two-manifold Experiment-12 theorem arises instead from optimizing two Fermi occupations on opposite sides of `mu`.

### Collision verdict

```text
DISTINCT.
```

---

## 10. Novelty risk that remains

The absence of a direct search hit is not enough to establish novelty.

The theorem is mathematically compact:

```text
exact Fermi inequality
+
Kubo-Greenwood
+
row/column velocity-strength bound.
```

A hostile reviewer could reasonably argue that it is an unstated but straightforward corollary of standard Pauli blocking.

Therefore the novelty case cannot rest on algebraic difficulty.

The stronger scientific case would be:

```text
1. a general inverse optical-to-thermal-population constraint was not previously formulated;
2. it eliminates DOS-model dependence;
3. it survives arbitrary dispersive multiband state reuse and static disorder;
4. it is quantitatively tight in nontrivial Dirac examples;
5. it identifies v_* as the explicit microscopic resource required to evade low-energy thermal population.
```

Whether that rises to a publishable theorem is still open.

---

## 11. Scope limitations that must appear in any claim

The current result is **not** universal across all photodetectors.

Explicit exclusions:

```text
bound excitons and neutral collective optical excitations;
phonon-assisted/indirect absorption unless separately generalized;
strong interaction-generated spectral functions beyond an independent-quasiparticle representation;
arbitrary passive photonic path enhancement when converting material conductivity to external absorptance;
dark-current/noise claims without a collection/recombination kinetic assumption.
```

Static single-particle disorder is not an exclusion if exact eigenstates are used.

The optical conductivity in the theorem should be denoted `sigma_1^cross`: direct transitions from states below `mu` to states above `mu`. Do not silently include thermally activated transitions entirely within the lower or upper state sets.

---

## 12. Current novelty disposition

```text
DIRECT PRIOR-ART COLLISION: NOT FOUND IN FOCUSED AUDIT.
CONCEPTUAL ADJACENCY: HIGH.
MATHEMATICAL NOVELTY: PROBABLY MODEST.
PHYSICAL / DETECTOR-SPECIFIC NOVELTY: PLAUSIBLE BUT UNPROVEN.
MANUSCRIPT: NOT YET JUSTIFIED.
```

The next step should be a hostile theorem review and a determination of whether the result remains scientifically useful after every scope limitation is stated explicitly.
