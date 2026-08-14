# Phonon-Edge Exponent and Isotope-Sign Correction

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** GENERAL EDGE ASYMPTOTICS / PREVIOUS DISPERSIONLESS SIGN REVERSAL RESTRICTED

## 1. Why the previous `sqrt(Delta)` model is not generic

The previous one-phonon toy model used

```math
F(\Delta)\propto\sqrt{\Delta}\,\Theta(\Delta),
```

which is the 3-D electron density-of-states factor for a **dispersionless single-energy phonon**.

The actual 2024 HgCdTe calculation uses Fermi's golden rule and integrates over optical-phonon wavevector `q`, with energy conservation enforced inside the `q` integral. The HgTe-like and CdTe-like optical branches span finite energy intervals.

Therefore the actual threshold exponent depends on the coupling-weighted phonon spectral density near the relevant branch edge.

## 2. General branch-edge convolution

Let

```math
u=\hbar\omega_{edge}-\hbar\omega\ge0
```

measure the phonon energy deficit below the relevant upper edge.

Define the coupling-weighted phonon spectral density near that edge by

```math
J_{ph}(u)\propto u^\eta,
\qquad \eta>-1.
```

For a 3-D parabolic conduction band,

```math
\rho_e(E)\propto E^{1/2}.
```

Let

```math
\Delta=\hbar\omega_{edge}-(E_g-E_2)
```

be the excess phonon-edge energy above the conduction-to-defect separation. Energy conservation gives

```math
E+u=\Delta.
```

Then the edge capture phase space has asymptotic form

```math
F(\Delta)
\propto
\int_0^\Delta
E^{1/2}(\Delta-E)^\eta dE.
```

Using the beta integral,

```math
\boxed{
F(\Delta)
\propto
B\left(\frac32,\eta+1\right)
\Delta^{\eta+3/2}.
}
```

Thus define

```math
\boxed{\beta=\eta+\frac32.}
```

The dispersionless `sqrt(Delta)` model is not a member of this continuous-edge family; it corresponds to a delta-function phonon spectrum.

## 3. Representative edge cases

### Smooth 3-D quadratic phonon extremum with nonsingular coupling

For a quadratic extremum at `q=0`, the ordinary 3-D phonon density of states scales as

```math
J_{ph}(u)\sim u^{1/2},
```

so

```math
\boxed{\beta=2.}
```

### Quadratic edge with a Fröhlich-like polar coupling singularity

A 3-D polar-optical matrix element has the familiar small-`q` weighting `|M(q)|^2 ~ 1/q^2`. Combined with the `q^2 dq` state measure, the weighted radial measure is approximately `dq`. For quadratic edge dispersion `u~q^2`, this gives

```math
J_{ph}(u)\sim u^{-1/2},
```

and hence

```math
\boxed{\beta=1.}
```

This is a conditional asymptotic argument. The actual HgCdTe exponent also depends on the continuum-to-localized-state overlap and the detailed optical-phonon dispersion used in the capture calculation.

The important point is that a dispersive phonon branch can change the threshold exponent from `1/2` to order unity or larger.

## 4. General isotope sensitivity for edge exponent beta

Use the reduced model

```math
C\propto
\omega^p(N_\omega+1)
\Delta^\beta e^{-\Delta/(kT)}.
```

Here `p` parameterizes the smooth explicit frequency dependence of the quantized coupling prefactor. For the simple polar/relative-coordinate model used previously, `p~1`.

Define

```math
\alpha=-\frac{d\ln\omega}{d\ln M}>0,
\qquad
x=\frac{\hbar\omega}{kT}.
```

Holding the electronic transition energy fixed,

```math
\frac{d\Delta}{d\ln M}=-\alpha\hbar\omega.
```

Then

```math
\boxed{
S_C
=\alpha\left[
-p+x(N_\omega+1)
-\beta\frac{\hbar\omega}{\Delta}
\right].
}
```

The sign crossing occurs at

```math
\boxed{
\Delta_\times
=\frac{\beta\hbar\omega}
{x(N_\omega+1)-p},
}
```

provided the denominator is positive.

## 5. Consequence at 77 K for the HgCdTe one-phonon window

For an HgTe-like optical scale

```text
hbar omega ~ 17.73 meV
T = 77 K
kT ~ 6.64 meV
x ~ 2.67
N ~ 0.074
```

and `p=1`,

```math
x(N+1)-1\simeq1.87.
```

Therefore

```math
\boxed{
\Delta_\times\simeq9.48\,\beta\ \text{meV}.
}
```

Representative cases:

```text
beta = 1/2  -> Delta_x ~ 4.74 meV
beta = 1    -> Delta_x ~ 9.48 meV
beta = 2    -> Delta_x ~ 18.96 meV
```

The 2024 HgCdTe paper states that for the relevant `E_g=35-38 meV` examples the participating electron kinetic-energy window is at most about `5 meV` and can be only `2 meV` near `E_g=38 meV`.

Hence, conditional on

```math
\beta\ge1
```

and the reduced prefactor exponent `p~1`, the entire relevant `0<Delta<=5 meV` window lies below the sign crossing:

```math
\boxed{S_C<0.}
```

Thus increasing the isotope mass lowers the one-phonon electron-capture coefficient throughout this narrow-gap window.

The earlier possible 77-K sign reversal inside the 0-5 meV window was a consequence of the dispersionless `beta=1/2` model and is not robust once a continuous dispersive phonon edge is admitted.

## 6. Finite natural-Hg -> 204Hg scale

Using the Hg-only frequency change for an ideal HgTe-like `143 cm^-1` mode,

```text
omega_heavy/omega_nat ~ 0.996745
hbar omega shift ~ -0.0577 meV
```

and the sharp reduced model, representative heavy/natural ratios at 77 K are:

```text
                   beta=1/2   beta=1   beta=2
Delta=0.10 meV       0.654      0.426    0.180
Delta=0.20 meV       0.849      0.716    0.509
Delta=0.50 meV       0.946      0.890    0.787
Delta=1.00 meV       0.977      0.948    0.893
Delta=2.00 meV       0.991      0.977    0.949
Delta=5.00 meV       1.000      0.994    0.983
```

These values deliberately omit spectral broadening and are not quantitative predictions for HgCdTe. They show how strongly the assumed branch-edge exponent controls the near-threshold isotope response.

## 7. Relation to broadening theorem

The earlier Gaussian regularization theorem for a generic onset

```math
F_0(\Delta)\sim\Delta^\beta\Theta(\Delta)
```

already gives

```math
\left.
\frac{\partial\ln F_\sigma}{\partial\Delta}
\right|_{\Delta=0}
=
\frac{\sqrt2\,\Gamma[(\beta+2)/2]}
{\Gamma[(\beta+1)/2]}
\frac1\sigma.
```

Thus the edge-exponent correction and finite-broadening correction fit into one hierarchy:

```text
phonon dispersion/coupling -> determines beta
finite linewidth/disorder  -> replaces threshold divergence by ~1/sigma
isotope shift              -> probes deltaDelta/sigma
```

## 8. What is established and what remains open

Established:

- `sqrt(Delta)` is not a universal one-phonon threshold law when phonon dispersion is retained;
- the joint electron/phonon phase space gives `beta=eta+3/2`;
- the isotope sign crossing moves linearly with `beta`;
- for `beta>=1`, the reduced model has no 77-K sign reversal inside the 0-5 meV electron window relevant to the 2024 HgCdTe calculation.

Open:

- the exact coupling-weighted edge exponent `eta` of the HgTe-like and CdTe-like branches in the full HgCdTe Fermi-golden-rule calculation;
- how the continuum/localized wavefunction overlap behaves at the relevant phonon-edge wavevector;
- finite phonon linewidth and alloy-disorder regularization;
- isotope-induced electronic-level renormalization.

## 9. Next theoretical gate

Determine whether the full 2024 polar-optical matrix element fixes the edge exponent analytically. If it does, replace the conditional `beta>=1` result with the exact HgCdTe branch-edge exponent.

If doing so merely reproduces a standard Fröhlich edge law without a new detector consequence, treat Experiment 07 as approaching a novelty stop rather than extending it indefinitely.
