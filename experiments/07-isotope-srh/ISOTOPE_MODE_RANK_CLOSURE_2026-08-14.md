# Isotope-Mode Rank Closure

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT CHAIN-RULE CLOSURE / GENERAL ISOTOPE-COEFFICIENT IDEAS HAVE PRIOR ART / HGCDTE APPLICATION RETAINED AS THEORY TOOL

## 1. General theorem

Let a scalar detector or recombination observable `R` depend on elemental isotope masses `M_a`, `a=1...s`, only through `m` isotope-dependent phonon coordinates `omega_j(M)`, plus variables that are isotope-independent:

```math
R=R(\omega_1,\ldots,\omega_m;z).
```

Define elemental logarithmic isotope sensitivities

```math
S_a=\frac{\partial\ln R}{\partial\ln M_a}
```

and mode sensitivities

```math
K_j=\frac{\partial\ln R}{\partial\ln\omega_j}.
```

Define the mass-participation matrix

```math
A_{aj}=\frac{\partial\ln\omega_j}{\partial\ln M_a}.
```

By the chain rule,

```math
\boxed{\mathbf S=A\mathbf K.}
```

Therefore the elemental isotope-response vector lies in the column space of `A`:

```math
\boxed{\mathbf S\in\operatorname{Col}(A).}
```

If `s>rank(A)`, every vector `v` in the left nullspace of `A` gives an exact closure

```math
\boxed{\mathbf v^T\mathbf S=0.}
```

The number of independent closures is at least

```math
s-\operatorname{rank}(A).
```

This result does not depend on the detailed functional form of `R`. Thresholds, nonlinear phonon phase space, finite-temperature Bose factors, serial SRH steps, and parallel capture paths are all allowed, provided all isotope dependence enters through the stated mode coordinates.

## 2. Why arbitrary SRH networks do not break the closure

The previous control theorem showed that a sequential/parallel SRH cycle has isotope sensitivity

```math
S_R=\sum_\ell W_\ell S_\ell,
\qquad W_\ell\ge0,\quad\sum_\ell W_\ell=1,
```

where `ell` labels microscopic channels.

If every microscopic channel sensitivity has the form

```math
\mathbf S_\ell=A\mathbf K_\ell,
```

then

```math
\mathbf S_R
=\sum_\ell W_\ell A\mathbf K_\ell
=A\left(\sum_\ell W_\ell\mathbf K_\ell\right).
```

Thus the complete SRH cycle remains in `Col(A)`.

An isotope-insensitive bypass has `S=0`, which is already in this column space and only reduces the magnitude of the response.

## 3. Ideal HgCdTe two-mode closure

Use three elemental mass axes

```text
Hg, Cd, Te
```

and two ideal relative optical coordinates

```text
H = HgTe-like
C = CdTe-like.
```

For a diatomic relative coordinate with isotope-independent force constant,

```math
\omega_H\propto\mu_{HgTe}^{-1/2},
\qquad
\omega_C\propto\mu_{CdTe}^{-1/2}.
```

The mass-participation matrix is

```math
A=
-\frac12
\begin{pmatrix}
M_{Te}/(M_{Hg}+M_{Te}) & 0\\
0 & M_{Te}/(M_{Cd}+M_{Te})\\
M_{Hg}/(M_{Hg}+M_{Te}) & M_{Cd}/(M_{Cd}+M_{Te})
\end{pmatrix}.
```

The first column is the HgTe-like mode; the second is the CdTe-like mode.

Solving the one-dimensional left nullspace gives

```math
\boxed{
S_{Te}
=\frac{M_{Hg}}{M_{Te}}S_{Hg}
+\frac{M_{Cd}}{M_{Te}}S_{Cd}.
}
```

Using standard natural atomic weights

```text
M_Hg = 200.59
M_Cd = 112.414
M_Te = 127.60
```

gives

```math
\boxed{
S_{Te}\approx1.5720\,S_{Hg}+0.8810\,S_{Cd}.
}
```

This is stronger than the earlier single-mode ratios:

```text
HgTe-only: S_Hg/S_Te = M_Te/M_Hg ~ 0.636
CdTe-only: S_Cd/S_Te = M_Te/M_Cd ~ 1.135
```

because the ternary closure remains valid when both mode families contribute simultaneously with arbitrary strengths.

## 4. Unknown threshold functions cancel

Write an arbitrary capture rate as

```math
C=C_H(\omega_H)+C_C(\omega_C)+C_0,
```

where each phonon channel may have arbitrary nonlinear dependence on its frequency and `C_0` is isotope-insensitive.

Define

```math
K_H=\frac{\partial\ln C}{\partial\ln\omega_H},
\qquad
K_C=\frac{\partial\ln C}{\partial\ln\omega_C}.
```

Then

```math
S_{Hg}=A_{Hg,H}K_H,
```

```math
S_{Cd}=A_{Cd,C}K_C,
```

and

```math
S_{Te}=A_{Te,H}K_H+A_{Te,C}K_C.
```

Eliminating `K_H,K_C` yields the ternary closure exactly.

No knowledge of

- capture spectral broadening,
- proximity to one-phonon threshold,
- electron distribution,
- HgTe/CdTe branch fractions,
- or isotope-insensitive bypass strength

is required.

## 5. Closure residual as an additional-physics coordinate

Define

```math
\boxed{
\mathcal E
=S_{Te}
-\frac{M_{Hg}}{M_{Te}}S_{Hg}
-\frac{M_{Cd}}{M_{Te}}S_{Cd}.
}
```

In the ideal two-mode mass-only model,

```math
\boxed{\mathcal E=0.}
```

A nonzero residual means at least one assumption has failed. Possible extra isotope-dependent coordinates include:

1. isotope-dependent electronic band-edge or defect-level renormalization not reducible to the two chosen optical frequencies;
2. other acoustic or local defect modes;
3. mass-dependent mode eigenvectors/mixing beyond the ideal diatomic approximation;
4. isotope-disorder broadening or phonon-lifetime changes, which depend on isotope variance rather than only mean elemental mass;
5. anharmonic force-constant changes or structural isotope effects;
6. isotope-dependent defect thermodynamics/population.

Thus `mathcal E` is not a generic measure of 'nonphononic physics'; it specifically measures physics outside the chosen two-coordinate isotope model.

## 6. Extension to arbitrary mode sets

For `s` isotope axes and `m` phonon or other isotope-dependent coordinates, collect their mass derivatives in `A`.

Then:

```math
\boxed{
\operatorname{dim}(\text{independent isotope closures})
=s-\operatorname{rank}(A).
}
```

Adding a genuinely independent isotope-sensitive coordinate increases `rank(A)` and removes a closure.

This gives a compact model-selection principle: the dimension of the elemental isotope-response space cannot exceed the number of independent isotope-sensitive microscopic coordinates in the model.

## 7. Important caveat: isotope enrichment changes more than mean mass

The theorem applies to derivatives with respect to smooth elemental mass parameters, or to isotope substitutions that are adequately represented by shifts of the selected mean mode frequencies.

Real isotope purification can also change the mass-variance disorder parameter and therefore phonon linewidth/lifetime. Mass variance is an additional isotope coordinate not determined by the mean mass alone. If this contribution matters, it must be added as another column of `A`, and the simple three-axis/two-mode closure need not hold.

The same is true for zero-point electronic renormalization involving phonons outside the two selected mode families.

## 8. Prior-art boundary

Partial isotope coefficients and isotope-coefficient sum rules are established in multicomponent superconductors and other electron-phonon systems. The linear-algebra theorem above is a generic chain-rule statement.

Therefore do **not** claim the generic rank theorem itself as new.

The retained value for Experiment 07 is HgCdTe-specific: it provides a stringent analytical closure for any model claiming that mercury-vacancy SRH isotope dependence is controlled solely by HgTe-like and CdTe-like optical coordinates.

The closure is especially useful because the 2024 HgCdTe SRH calculation explicitly includes both HgTe-like and CdTe-like optical phonons in the one-phonon capture problem.

## 9. Next theoretical question

Combine this isotope-mode closure with the HgCdTe electron energy-selection condition

```math
K=\hbar\omega_{LO}-(E_g-E_2)
```

and derive an exact isotope-bandgap/composition differential equivalence.

Then determine whether the existing calculated `C_n(E_g,T)` curves already imply the isotope coefficient to first order, modulo only smooth prefactor derivatives.
