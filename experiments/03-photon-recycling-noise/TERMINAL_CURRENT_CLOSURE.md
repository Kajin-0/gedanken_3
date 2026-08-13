# Terminal-current closure

**Date:** 2026-08-13
**Status:** EXACT SMALL-SIGNAL PHOTOCONDUCTOR MAPPING / NOVELTY UNDER AUDIT

## Voltage-biased photoconductor

For a uniform rectangular photoconductor of electrical length `ell`, voltage `V`, and excess pair number `x`,

```math
\boxed{\delta I=g_Ix,\qquad g_I=\frac{q(\mu_e+\mu_h)V}{\ell^2}.}
```

Equivalently,

```math
g_I=q(1/t_{tr,e}+1/t_{tr,h}).
```

Thus

```math
\boxed{S_{I,ij}=g_{I,i}g_{I,j}S_{x,ij}.}
```

This is the low-injection, uniform-field approximation. Contacts, sweepout, nonuniform fields and spatial weighting require a distributed model.

## Independent electrical noise

Let `y_i=g_{I,i}x_i+n_i` with independent Johnson/readout noises. For `i!=j`,

```math
\boxed{S_{y,ij}=g_{I,i}g_{I,j}S_{x,ij}.}
```

Independent additive noise does not bias the cross-spectrum, although it increases estimator variance and auto-spectra.

For identical per-pixel electronics `y_i(omega)=H(omega)x_i+n_i`,

```math
S_{y,12}=|H|^2S_{x,12}.
```

An identical RC/TIA response therefore does not move the intrinsic zero crossing or change the sign pattern. Unequal known channel responses can be de-embedded through `H_1H_2^*`.

## Exact normalized two-pixel spectrum

For identical pixels define

```math
c=c_{dc}=\frac{k}{\gamma+k}.
```

The two relaxation rates are `a=gamma` and `b=gamma+2k`, hence

```math
\frac{b}{a}=\frac{1+c}{1-c},
\qquad
\omega_x^2=ab=\gamma^2\frac{1+c}{1-c}.
```

The intrinsic spectra satisfy

```math
\boxed{
\frac{S_{12}(\omega)}{S_{11}(\omega)}
=c\frac{\omega_x^2-\omega^2}{\omega_x^2+\omega^2}.}
```

Thus

```text
omega -> 0:        S12/S11 -> +c
omega = omega_x:   S12 = 0
omega -> infinity: S12/S11 -> -c
```

If `c` is measured independently by steady localized illumination and `gamma` by common-mode relaxation, the entire normalized intrinsic cross-spectrum is predicted with no free shape parameter.

## Deterministic frequency-domain crosstalk

For harmonic generation applied only to pixel 1,

```math
\boxed{\frac{x_2}{x_1}=\frac{k}{\gamma+k+i\omega}.}
```

At zero frequency this is `c_dc`.

The same birth/death/exchange model obeys

```math
\boxed{S_x(\omega)=2m\,\mathrm{Re}[(M+i\omega I)^{-1}].}
```

This is a fluctuation-response identity of the model, not a new general theorem.

## Minimal falsification protocol

1. Uniformly modulate both pixels and measure common-mode rate `gamma`.
2. Illuminate pixel 1 only at low frequency and measure deterministic `c_dc`.
3. Record simultaneous unforced pixel signals.
4. Estimate and de-embed the complex cross-spectrum.
5. Test

```math
\boxed{
\frac{S_{12}}{S_{11}}
=c_{dc}\frac{\gamma^2(1+c_{dc})/(1-c_{dc})-\omega^2}
{\gamma^2(1+c_{dc})/(1-c_{dc})+\omega^2}.}
```

Failure means the two-state conservative-exchange model is incomplete. It does not alone identify the omitted mechanism.

## Prior-art boundary

Cross-correlation noise metrology is old. SPAD arrays already use dark-event correlations to measure optical/electrical crosstalk, and HgCdTe deterministic optical/diffusive crosstalk is well studied. Possible novelty is only the analog linear-HgCdTe closure and any mechanism-specific spectral consequence.