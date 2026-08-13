# Experiment 05 — active volume versus optical bandwidth

**Date:** 2026-08-13  
**Status:** PROVISIONAL / SINGLE-RESONANCE RESULT DERIVED / GENERAL PASSIVITY BOUND NOT YET ESTABLISHED / NOVELTY NOT ESTABLISHED

## Question

Antenna-, lens-, waveguide-, and resonant-cavity-coupled photodetectors can collect substantial optical power into an electrically small absorber, reducing bulk dark generation. Can the active semiconductor volume be driven arbitrarily toward zero while preserving both high absorptance and a fixed nonzero optical spectral bandwidth?

The device idea is old. The open question here is whether established optical power-bandwidth/sum-rule bounds imply a detector-side lower bound on bulk dark-generation noise for a prescribed optical acceptance band.

## Minimal one-resonance model

Use one temporal coupled mode

```math
\dot a=(i\omega_0-\gamma_e-\gamma_i)a+\sqrt{2\gamma_e}\,s_+.
```

The absorptance is

```math
A(\omega)=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

At critical coupling,

```math
\gamma_e=\gamma_i=\gamma,
```

so

```math
A(\omega_0)=1
```

and

```math
\boxed{\Delta\omega_{FWHM}=4\gamma_i.}
```

## First detector-specific scaling assumption

For a small bulk absorber occupying volume `V` in a fixed normalized optical mode, assume

```math
\gamma_i=\kappa V.
```

This is a local reduced-order assumption, **not** a universal optical theorem.

Then

```math
\boxed{\Delta\omega_{FWHM}=4\kappa V.}
```

Assume bulk thermal dark-generation events occur at rate density `g_d`, so

```math
G_d=g_dV,
```

and one collected electron per dark event gives

```math
S_I=2q^2g_dV
```

for the one-sided shot-noise current PSD.

At unity peak absorptance and unit collection efficiency,

```math
R_{pk}=q/(\hbar\omega_0).
```

Therefore

```math
\boxed{NEP_{pk}^2=2(\hbar\omega_0)^2g_dV.}
```

Eliminating `V`,

```math
\boxed{
\frac{NEP_{pk}^2}{\Delta\omega_{FWHM}}
=\frac{(\hbar\omega_0)^2g_d}{2\kappa}.
}
```

Within this model, reducing active volume by `100x` improves on-resonance shot-noise-limited NEP by `10x`, but narrows the optical FWHM by `100x`.

Peak absorptance therefore hides the spectral cost.

## General threshold form for the critical mode

For required absorptance `A>=eta` over a centered band,

```math
\boxed{
\Delta\omega_\eta
=4\gamma_i\sqrt{\frac{1-\eta}{\eta}}.
}
```

Hence

```math
\boxed{
\frac{NEP_{pk}^2}{\Delta\omega_\eta}
=\frac{(\hbar\omega_0)^2g_d}{2\kappa}
\sqrt{\frac{\eta}{1-\eta}}.
}
```

Demanding absorptance closer to unity over a finite band requires proportionally more internal optical loss and therefore more active volume in this family.

## Many-resonance escape attempt

If several non-overlapping critically coupled modes have the same local coefficient `kappa`,

```math
\Delta\omega_j=4\kappa V_j.
```

Therefore

```math
\boxed{
\sum_j\Delta\omega_j=4\kappa\sum_jV_j.
}
```

Tiling a broad band with many narrow resonances does not evade the total active-volume requirement in this reduced-order model.

This is the same qualitative structure expected from established frequency-integrated optical-response and power-bandwidth bounds; it is not a novelty claim.

## Strong-comparator warning

A lossless external lens, taper, or waveguide can change the field distribution while the semiconductor volume changes. Thus `gamma_i=kappa V` with fixed `kappa` is not universal.

Do **not** claim a universal detector invariant from the equations above.

The next hard step is to start from established geometry-independent per-volume absorption bounds / spectral sum rules and determine whether they can be written for an active semiconductor embedded in arbitrary passive lossless collection optics. If arbitrary lossless optics invalidate any bound that depends only on active semiconductor volume, Experiment 05 should stop.

## Prior-art boundary

Known and not new:

- resonant-cavity-enhanced photodetectors using thinner absorbers to reduce dark current;
- antenna/metasurface-coupled detectors reducing active volume while preserving optical collection;
- narrow spectral response of resonant-cavity detectors;
- geometry-independent per-volume optical absorption limits;
- frequency-integrated and power-bandwidth bounds for passive optical response.

The possible contribution, if any, is only a detector-facing bound linking required optical acceptance to minimum bulk dark-generation noise. Novelty is not established.