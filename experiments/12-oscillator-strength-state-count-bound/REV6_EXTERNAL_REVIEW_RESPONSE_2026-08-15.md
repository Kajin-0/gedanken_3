# Experiment 12 — Response to external adversarial review of PRB Rev6

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **CENTRAL THEOREM RETAINED / REV7 REQUIRED / REALISTIC KANE CAPACITY VALIDATION ADDED**

## Review disposition

The supplied external review finds no algebraic defect that destroys the central theorem. The revision therefore does **not** alter the Fermi lemma, Kubo conversion, support-rank inequality, Dirac checks, unequal-mass parabolic check, or 10-um numerical arithmetic.

The three highest-priority requested changes are accepted:

1. promote thermodynamic-limit boundedness of the shell optical capacity to an explicit theorem hypothesis;
2. add van Roosbroeck-Shockley and fluctuation-dissipation context;
3. demonstrate that the optical-capacity resource is finite and quantitatively meaningful in a realistic multiband narrow-gap semiconductor Hamiltonian.

The remaining interpretation/wording items are also accepted: exact-`mu` endpoints, support-rank brittleness, practical separation of `sigma_1^cross`, ideal-model qualification of global parabolic saturation, and internal/AR interpretation of the 90% single-pass example.

---

# 1. Thermodynamic-limit hypothesis

The finite-volume theorem is exact without an additional assumption.

For a thermodynamic sequence `V_j -> infinity` and fixed useful spectral window `B`, a nonzero macroscopic density floor requires a **uniform** capacity bound

```math
\boxed{
\bar v_B^{cap}
\equiv
\limsup_{j\to\infty}v_{B,V_j}^{cap}<\infty.
}
```

Then the thermodynamic-limit density inequality uses `\bar v_B^{cap}` in the denominator.

This will be promoted from interpretive prose to a formal hypothesis in Rev7.

---

# 2. Realistic multiband Kane capacity — exact result

Use the published first-order `8 x 8` Kane Hamiltonian for bulk HgCdTe written by Malcolm and Nicol, Phys. Rev. B 92, 035118 (2015), with

```math
H_K(\mathbf k)
=\hbar v_K M(\mathbf k)
+H_{edge}(E_g,\Delta).
```

For x-polarized light,

```math
\hat v_x
=\frac{1}{\hbar}\frac{\partial H_K}{\partial k_x}
=v_K M_x.
```

In the basis used in that paper, `M_x` decomposes into two independent weighted-star blocks. The squared edge weights of either block are

```math
\frac34+\frac14+\frac12=\frac32.
```

Therefore the nonzero eigenvalues are

```math
\pm\sqrt{\frac32}
```

(twofold), and the remaining four eigenvalues are zero. Hence

```math
\boxed{
\|\hat v_x\|_{op}
=\sqrt{\frac32}\,v_K.
}
```

Projector contraction immediately gives, for **every** selected optical window,

```math
\boxed{
v_B^{cap}
\le \sqrt{\frac32}\,v_K.
}
```

This ceiling is independent of system volume, wave vector, `E_g`, and the split-off energy `\Delta` inside the first-order Kane model. It therefore automatically supplies the uniform thermodynamic bound requested by the referee.

Using the standard Kane energy

```math
E_P=\frac{2m_0P^2}{\hbar^2},
\qquad
v_K^2=\frac{E_P}{3m_0},
```

the same result is

```math
\boxed{
v_B^{cap}\le\frac{P}{\hbar}
=\sqrt{\frac{E_P}{2m_0}}.
}
```

For the accepted HgCdTe value `E_P ~= 18.8 eV`,

```text
v_K = 1.050e6 m/s
v_B^cap <= 1.286e6 m/s.
```

Using the experimentally extracted universal Kane velocity

```text
v_K = (1.07 +/- 0.05)e6 m/s
```

gives the central capacity scale

```text
v_B^cap <= 1.31e6 m/s
```

(with approximately +/-0.06e6 m/s propagated from the quoted velocity uncertainty).

This is the key response to the reviewer's largest conceptual objection: in a standard, experimentally validated multiband narrow-gap Hamiltonian, the capacity is not arbitrary and cannot grow with sample volume.

### Relation to higher-order HgCdTe models

The exact `sqrt(3/2) v_K` result is for the first-order `8 x 8` Kane Hamiltonian. Second-order `8 x 8 k.p` calculations are established for quantitative HgTe/HgCdTe infrared absorption; they introduce finite `k`-dependent velocity corrections. For any finite detector-relevant energy window the corresponding selected momentum region is finite, so finite second-order coefficients still give a finite capacity, but the numerical ceiling is no longer exactly `sqrt(3/2) v_K`.

Rev7 will state this distinction explicitly rather than overclaiming the first-order number as an exact full-band HgCdTe constant.

---

# 3. Numerical detector-scale consequence using the Kane capacity

Rev6 Appendix A has the internal-single-pass 10-um/300-K witness

```text
v_B^cap = 1.0e6 m/s -> Sigma_e >= 9.1495e11 cm^-2
```

and the bound scales exactly as `(v_B^cap)^(-2)`.

Inserting the experimentally anchored first-order Kane capacity

```text
v_B^cap <= 1.3105e6 m/s
```

gives the conservative central-value consequence

```math
\boxed{
\Sigma_e\gtrsim 5.33\times10^{11}\ \mathrm{cm^{-2}}
}
```

for the same illustrative optical requirement.

This does **not** claim that bulk HgCdTe exactly realizes the idealized Appendix-A absorptance model. It shows that the resource values in the table are in the range of an actual narrow-gap multiband Hamiltonian rather than being arbitrary velocity choices.

The Appendix-A 90% absorptance will also be relabeled as internal absorptance of admitted power, equivalently ideal antireflection/index-matched coupling.

Reproducibility script:

`numerics/kane_8band_capacity.py`

---

# 4. Detailed-balance and fluctuation-dissipation positioning

Rev7 will add a dedicated equilibrium-relations subsection.

### van Roosbroeck-Shockley

The van Roosbroeck-Shockley relation uses detailed balance to infer radiative electron-hole recombination/emission from optical absorption.

Its logical object is

```text
absorption spectrum -> radiative generation/recombination rate.
```

Experiment 12 instead establishes

```text
surviving direct cross-mu conductivity
+ finite per-shell velocity capacity
-> minimum equilibrium one-body thermal population.
```

No recombination coefficient or radiative lifetime is inferred. The two results are complementary, not competing.

### Fluctuation-dissipation / KMS neighborhood

Callen-Welton/Kubo fluctuation-dissipation relations connect dissipative linear response to equilibrium fluctuations of the conjugate observable/current.

The Experiment-12 theorem instead uses a statewise Fermi occupation inequality and a finite optical-coupling capacity to constrain the population of the one-body states supporting the response. It is therefore not an FDT identity, even though both are equilibrium response constraints.

This distinction will be made explicit because the unusual thermal kernel naturally invites comparison to detailed-balance/FDT relations.

---

# 5. Remaining referee corrections accepted for Rev7

## Exact states at `E = mu`

For notation, the theorem will assume no selected positive-frequency transition endpoint lies exactly at `mu`. If such states occur, their contribution is defined by the continuous `mu -> mu +/- 0` limiting prescription. This has no effect on the gapped examples and only measure-zero effect at the ideal Dirac node.

## Support-rank interpretation

`n_B^act` will be described explicitly as an exact support-dimension construct. Because matrix rank is discontinuous when a singular value crosses zero, it should not be interpreted as a robust experimentally inferred number of "participating carriers." The total-population corollary does not depend on making that interpretation.

## Experimental use of `sigma_1^cross`

Rev7 will state that direct application to measured conductivity requires either

```text
sigma_1 ~= sigma_1^cross
```

inside the selected window or a microscopic/spectral decomposition that isolates the direct cross-`mu` contribution.

## Parabolic saturation

Global all-spectrum saturation will be stated only as an exact property of the stated ideal effective two-band optical model. No ultraviolet-complete real-semiconductor claim will be made. Finite-window active-subspace saturation remains the stronger physically local statement.

## Low-energy wording

The low-energy conclusion will be written only in the precise conditional form

```text
transition energy -> low
+ finite integrated direct cross-mu spectral weight
+ uniformly bounded per-shell optical capacity
-> nonvanishing active thermal population floor.
```

---

# 6. Revision disposition

```text
CENTRAL THEOREM: RETAIN
ALGEBRA: NO CHANGE
KUBO NORMALIZATION: NO CHANGE
DIRAC/PARABOLIC NUMERICS: NO CHANGE
THERMODYNAMIC HYPOTHESIS: STRENGTHEN
PHYSICAL CAPACITY RESOURCE: REALISTIC KANE VALIDATION ADDED
LITERATURE POSITIONING: VRS + FDT ADDED
APPENDIX OPTICAL BOUNDARY: CLARIFY INTERNAL/AR ASSUMPTION
TITLE/ABSTRACT: MAKE CAPACITY CONDITIONALITY EXPLICIT
```

The supplied review is therefore treated as a **productive major revision**, not a reason to abandon Experiment 12.