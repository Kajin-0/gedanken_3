# Experiment 02 — Isochronous Avalanche Photodetector

**Date:** 2026-08-13
**Status:** PROVISIONAL / NARROWED AFTER TWPD PRIOR-ART CHECK / NOVELTY NOT ESTABLISHED

## Device-engineer question

In an APD/SPAD, photons are absorbed at random depths. A photon absorbed farther from the avalanche region has a longer internal carrier trip and therefore a later mean trigger time. Can the optical structure deliberately make that photon arrive earlier optically, so optical delay and carrier-depth delay cancel?

Plainly:

> Can we make a thick, efficient absorber behave as though every photon were absorbed at the same timing depth?

## Core condition

For random absorption coordinate `X`, define the conditional mean timestamp

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

Then

```math
\boxed{Var(T)=Var[m(X)]+E[Var(T|X)].}
```

The absorption-position contribution vanishes exactly if

```math
\boxed{m(X)=constant.}
```

For one smooth coordinate,

```math
\boxed{d[t_o+t_c+t_e+\mu_a]/dx=0.}
```

This removes only the position-dependent conditional mean delay. Avalanche stochasticity, carrier diffusion/scattering, optical dispersion, and electronics jitter remain.

## Important narrowing after prior-art stress test

Longitudinal optical-position delay in an ordinary traveling-wave detector is **not** the new target. If a detector is read out at the far end,

```math
t(x)=x/v_g+L_c(x)/v_c+(L-x)/v_e+\bar t_a(x),
```

and therefore

```math
1/v_g+(1/v_c)dL_c/dx-1/v_e+d\bar t_a/dx=0
```

is the general longitudinal isochronous condition.

When `v_e=v_g` and internal carrier delay is position independent, optical and electrical propagation already cancel. This is essentially classical traveling-wave velocity matching.

**Therefore Experiment 02 is now specifically about transverse absorption-depth jitter:** use optical path engineering to correlate optical propagation time with physical absorption depth and cancel the internal carrier-to-avalanche transit delay. Standard optical/microwave velocity matching does not by itself remove this transverse depth term.

## Simplest depth-mapping condition

If the mean optical absorption depth follows optical propagation coordinate `x` as `z_bar(x)`, with avalanche region at depth `d`,

```math
t(x)=x/v_g+[d-z_bar(x)]/v_c.
```

Ignoring electrical and avalanche-mean gradients, exact mean-depth compensation requires

```math
\boxed{dz_bar/dx=v_c/v_g.}
```

Equivalently, the optical mode should move through the absorber depth very slowly as it propagates. Over optical length

```math
L=d v_g/v_c,
```

the mode center traverses the full absorber depth while optical delay accumulates by exactly `d/v_c`.

## Current prior-art status

Known literature covers:

- absorption/generation-position timing jitter in APDs/SPADs;
- waveguide/nanophotonic absorption engineering;
- lateral Ge/Si multiplication structures;
- traveling-wave optical/electrical velocity matching;
- tapered-electrode traveling-wave photodetectors with position-varying carrier transit for power/bandwidth optimization.

A 2001 variable-electrode TW-MSM patent is structurally close because its carrier transit time changes along optical propagation, but its taper follows optical-power decay and does not appear to target cancellation of optical arrival delay against carrier-to-avalanche delay.

Targeted searches have not yet found an APD/SPAD that deliberately maps transverse absorption depth onto optical propagation time to make the conditional mean trigger time independent of absorption depth. This absence is not proof of novelty.

## Immediate next questions

1. derive the irreducible drift-diffusion floor after perfect mean-depth compensation;
2. quantify residual jitter from finite transverse optical-mode thickness;
3. determine whether an adiabatically depth-shifted absorbing mode can be fabricated over the required optical length;
4. include avalanche-build-up and electrical-readout floors;
5. continue journal and patent searching before any manuscript work.

## Hard rule

Do not draft a paper or claim priority yet. Kill the experiment if the depth-compensation concept is found in prior art or if realistic optical-mode thickness/diffusion leaves no material timing improvement.