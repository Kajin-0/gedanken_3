# Bandgap–Isotope Differential Equivalence and Its Multibranch No-Go

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT SINGLE-BRANCH EQUIVALENCE / MULTIBRANCH NON-IDENTIFIABILITY DERIVED / NOT A NOVELTY CLAIM

## 1. HgCdTe electron energy-selection law is now fixed by the primary theory

The 2024 narrow-gap HgCdTe calculation considers electron capture from the conduction band to the singly charged mercury-vacancy acceptor level `A2^-1`, with the defect level approximately `E2=20 meV` above the valence-band edge.

For electron capture, the energy transferred to the optical phonon is the conduction-band-to-defect energy plus the electron kinetic energy. Equivalently,

```math
K=\hbar\omega_{LO}-(E_g-E_2),
```

where `K>=0` is the selected conduction-electron kinetic energy.

The paper explicitly gives the example `E_g=38 meV`: the conduction-band-to-defect separation is `18 meV`, so a `20 meV` optical phonon allows electrons with kinetic energy up to `2 meV`.

Thus define the electron detuning

```math
\boxed{
\Delta_j=\hbar\omega_j-E_g+E_2
}
```

for each optical-phonon branch `j`.

## 2. Exact single-branch bandgap equivalence

Suppose one phonon branch dominates and write

```math
C_n=P(E_g,E_2,\omega,T)F(\Delta,T),
\qquad
\Delta=\hbar\omega-E_g+E_2.
```

If only the energy-selection part is considered, then

```math
\delta\Delta=\delta(\hbar\omega)-\delta E_g+\delta E_2.
```

Therefore an isotope-induced phonon shift `delta(hbar omega)` with electronic energies fixed is exactly equivalent in `F` to a bandgap shift

```math
\boxed{
\delta E_{g,eq}=-\delta(\hbar\omega).
}
```

For natural Hg -> 204Hg in an ideal HgTe-like `143 cm^-1` mode,

```text
delta(hbar omega) ~= -0.0577 meV
```

and hence

```math
\boxed{
\delta E_{g,eq}\simeq+0.0577\ \text{meV}.
}
```

This equivalence concerns only the detuning coordinate. It does not include isotope dependence of the quantized coupling prefactor, Bose factor, electronic levels or spectral broadening.

## 3. Differential single-branch closure

Define

```math
G_\Delta=\frac{\partial\ln F}{\partial\Delta}.
```

Then

```math
\frac{\partial\ln C_n}{\partial E_g}
=\frac{\partial\ln P}{\partial E_g}-G_\Delta.
```

For elemental mass `M`,

```math
S_M\equiv\frac{d\ln C_n}{d\ln M}
=S_{P,M}+G_\Delta\frac{d\Delta}{d\ln M}.
```

Eliminating the unknown threshold derivative gives

```math
\boxed{
S_M-S_{P,M}
=-\frac{d\Delta}{d\ln M}
\left[
\frac{\partial\ln C_n}{\partial E_g}
-\frac{\partial\ln P}{\partial E_g}
\right].
}
```

Thus a branch-resolved theoretical `C_n(E_g,T)` curve contains the first-order kinetic isotope response once the smooth prefactor derivative is known.

## 4. Equivalent composition shift

For composition `x`, without assuming any specific empirical bandgap convention,

```math
\frac{\partial\Delta}{\partial x}
=\hbar\frac{\partial\omega}{\partial x}
-\frac{\partial E_g}{\partial x}
+\frac{\partial E_2}{\partial x}.
```

An isotope perturbation has a local detuning-equivalent composition shift

```math
\boxed{
\delta x_{eq}
=\frac{\delta\Delta_{iso}}
{\partial\Delta/\partial x}.
}
```

If the composition dependence of the phonon and vacancy level is neglected compared with the bandgap slope,

```math
\delta x_{eq}\simeq
-\frac{\delta\Delta_{iso}}{\partial E_g/\partial x}.
```

Using the Hansen empirical gap formula only as an illustrative mapping near `x~0.188` at low temperature gives `dE_g/dx~1.71 eV`; the Hg-only `-0.0577 meV` phonon shift then corresponds to `delta x_eq~+3.4e-5`.

Because different HgCdTe gap parameterizations differ materially in the extreme narrow-gap regime, the energy-domain equivalence `delta E_g,eq` is the preferred statement.

## 5. Critical multibranch no-go

The 2024 HgCdTe theory includes both HgTe-like and CdTe-like optical phonons. Therefore write generally

```math
C_n=P\,F(\Delta_H,\Delta_C),
```

with

```math
\Delta_H=\hbar\omega_H-E_g+E_2,
\qquad
\Delta_C=\hbar\omega_C-E_g+E_2.
```

Define

```math
G_H=\frac{\partial\ln F}{\partial\Delta_H},
\qquad
G_C=\frac{\partial\ln F}{\partial\Delta_C}.
```

A bandgap shift moves both coordinates equally:

```math
\frac{\partial\Delta_H}{\partial E_g}
=\frac{\partial\Delta_C}{\partial E_g}=-1.
```

Hence

```math
\boxed{
\frac{\partial\ln C_n}{\partial E_g}
-\frac{\partial\ln P}{\partial E_g}
=-(G_H+G_C).
}
```

But an Hg isotope perturbation predominantly shifts the HgTe-like coordinate,

```math
S_{Hg}^{kin}
=G_H\frac{d\Delta_H}{d\ln M_{Hg}},
```

whereas Cd isotope substitution predominantly shifts the CdTe-like coordinate.

Therefore the total ordinary bandgap/composition slope gives only the **sum** `G_H+G_C`; it does not determine `G_H` and `G_C` separately.

This produces the no-go:

```math
\boxed{
\text{A total }C_n(E_g,T)\text{ curve cannot, by itself, predict an elemental isotope coefficient when multiple independent phonon branches contribute.}
}
```

A unique isotope prediction requires at least one of:

1. one phonon branch dominates;
2. branch-resolved theoretical capture contributions are available;
3. additional independent derivatives/closures separate `G_H` and `G_C`.

## 6. Relation to the isotope-mode rank closure

The previous `ISOTOPE_MODE_RANK_CLOSURE_2026-08-14.md` supplies the complementary information.

In the ideal two-mode mass-only model, the three elemental isotope sensitivities obey

```math
S_{Te}
=\frac{M_{Hg}}{M_{Te}}S_{Hg}
+\frac{M_{Cd}}{M_{Te}}S_{Cd}.
```

This is independent of `G_H,G_C`, but it also does not determine their absolute values.

Thus:

```text
bandgap derivative -> one sum of branch responses
isotope rank closure -> one relation among elemental responses
```

Neither alone reconstructs the full branch-resolved response. Together with one branch-resolved quantity, however, the model closes.

## 7. Physical interpretation

Composition tuning and isotope tuning are not generally interchangeable controls.

- `E_g` moves the electronic separation seen by **every** phonon branch.
- Hg isotope mass primarily shifts Hg-dominated vibrations.
- Cd isotope mass primarily shifts Cd-dominated vibrations.
- Te isotope mass shifts both families.

Thus isotope mass explores directions in microscopic parameter space that ordinary composition or temperature tuning cannot reproduce exactly.

This is why the existence of a steep `C_n(x)` curve is insufficient by itself to imply a large Hg isotope coefficient.

## 8. Prior-art boundary

The chain-rule equivalence and multivariable non-identifiability are generic mathematics. Do not claim them as new.

The HgCdTe-specific content is that the primary 2024 theory fixes the relevant electron energy-selection coordinate to

```math
K=\hbar\omega_{LO}-(E_g-E_2)
```

while simultaneously allowing both HgTe-like and CdTe-like optical branches. This makes the multibranch no-go directly applicable to the proposed isotope extension.

## 9. Next theoretical question

Determine whether the two branch contributions in the published HgCdTe capture model can be separated analytically from the Fermi-golden-rule kernel.

If they cannot be separated without reproducing the full existing numerical calculation, then Experiment 07 is likely only a straightforward isotope perturbation of established theory rather than a distinct theoretical advance.
