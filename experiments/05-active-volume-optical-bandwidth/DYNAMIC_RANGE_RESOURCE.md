# Experiment 05 — the missing resource is dynamic range / throughput

**Date:** 2026-08-13  
**Status:** REFINEMENT / VOLUME-BANDWIDTH HYPOTHESIS REJECTED GENERALLY / VOLUME-DYNAMIC-RANGE SCALING DERIVED / NOVELTY NOT ESTABLISHED

## 1. Context

`LOSSLESS_TRANSFORMER_COUNTEREXAMPLE.md` shows that passivity and causality alone do not force the optical acceptance bandwidth to collapse as active semiconductor volume shrinks when arbitrary lossless impedance transformation is treated as a free resource.

The price is increasing local optical field and absorbed power density.

This step asks what detector resource is therefore naturally lost as `V -> 0`.

## 2. Continuous field-limited model

For a uniform linear absorber,

```math
P_{abs}
=\frac{\omega\epsilon_0\chi''}{2}V\langle |E|^2\rangle.
```

Let the required external absorptance be `eta`, so `P_abs=eta P_in`.

If the material remains acceptably linear only up to internal field `E_lin`, then

```math
\boxed{
P_{in,max}
=\frac{\omega\epsilon_0\chi''E_{lin}^2}{2\eta}V.
}
```

Thus the maximum linear optical input scales directly with active volume.

Assume independent bulk dark-generation events occur at density `g_d`, giving

```math
G_d=g_dV.
```

For one collected carrier per dark event and signal quantum efficiency `eta`,

```math
\boxed{
NEP_d^2
=\frac{2(\hbar\omega)^2g_d}{\eta^2}V.
}
```

Eliminating volume gives

```math
\boxed{
\frac{P_{in,max}}{NEP_d^2}
=
\frac{\omega\epsilon_0\chi''E_{lin}^2\eta}
{4(\hbar\omega)^2g_d}.
}
```

Within this model, active-volume reduction improves small-signal dark-limited NEP as `sqrt(V)` but decreases maximum linear input power as `V`.

A one-Hz amplitude dynamic-range scale therefore behaves as

```math
\boxed{P_{in,max}/NEP_d\propto\sqrt V.}
```

Smaller active volume is better for weak-signal sensitivity but worse for bright-signal headroom.

## 3. Microscopic absorber-count interpretation

Let the active volume contain `N` statistically similar absorbing centers, with

```math
N\propto V.
```

Let each center have:

- dark-event rate `d`;
- maximum useful absorption/reset/cycling rate `r_max`.

An ideal passive concentrator may increase the external optical coupling to the available centers, but it cannot make one center process arbitrarily many independent absorptions per unit time without saturation/reset physics.

Then

```math
G_{dark}=Nd,
```

and

```math
\Phi_{max}=Nr_{max}.
```

Hence

```math
\boxed{
\frac{\Phi_{max}}{G_{dark}}=\frac{r_{max}}{d},
}
```

independent of `N` and therefore of active volume.

The dark-shot-noise-limited minimum detectable signal-rate scale is

```math
\Phi_{min}\sim\sqrt{2G_{dark}}\propto\sqrt N,
```

whereas

```math
\Phi_{max}\propto N.
```

Therefore

```math
\boxed{
\frac{\Phi_{max}}{\Phi_{min}}\propto\sqrt N\propto\sqrt V.
}
```

The microscopic counting picture and the continuous internal-field picture give the same qualitative tradeoff.

## 4. Parallelization does not evade the active-volume accounting

Split total active volume `V` among many smaller detector elements and combine their outputs ideally.

If each element has the same per-volume dark generation and per-volume saturation capacity, then:

```text
total dark generation -> proportional to total V
total maximum throughput -> proportional to total V
```

Parallelization can change readout architecture and spatial information but does not improve the intrinsic throughput/dark-event ratio without changing the microscopic rates.

## 5. Optical/radiative floor

The `sqrt(V)` NEP improvement applies only to the bulk dark-generation component.

If the accepted optical modes and absorptance are held fixed while `V` shrinks, then background-photon noise and radiative detailed-balance terms need not shrink with `V`. Schematically,

```math
NEP_{tot}^2(V)=A V+B_{opt}+B_{read}+\cdots.
```

Once `AV << B_opt+B_read`, further volume reduction no longer materially improves NEP but still reduces `P_in,max`.

Thus an aggressively concentrated detector eventually becomes optical/background/readout limited before the formal bulk-dark noise reaches zero.

This is ordinary background/radiative-limited detector physics, not a novelty claim.

## 6. Current disposition

```text
universal active-volume / optical-bandwidth invariant:
    REJECTED

active-volume / local-field or throughput tradeoff:
    DERIVED in simple extensive models

unbounded small-signal sensitivity improvement from V -> 0:
    NO once volume-independent optical/radiative/readout floors are included

publication novelty:
    NOT ESTABLISHED
```

## 7. Next strong-comparator question

The remaining question is whether this volume-throughput tradeoff contains any detector-specific content beyond ordinary saturation and shot-noise scaling.

Before extending it, audit literature on antenna/meta-lens/resonant infrared detectors for explicit sensitivity-versus-saturation/dynamic-range discussions. If the scaling is already standard or follows immediately from established detector saturation models, close Experiment 05 rather than forcing a paper.