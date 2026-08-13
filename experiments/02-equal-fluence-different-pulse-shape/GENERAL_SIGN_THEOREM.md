# General split-pulse sign theorem

**Date:** 2026-08-13
**Status:** EXACT GENERALIZATION / PHYSICALLY USEFUL / NOVELTY NOT ESTABLISHED

Let excess carrier density decay autonomously according to

```math
\frac{dn}{dt}=-R(n),
\qquad R(n)>0\quad(n>0).
```

Define the density-dependent effective lifetime

```math
\boxed{\tau_{eff}(n)=\frac{n}{R(n)}}.
```

The time-integrated carrier response accumulated while density falls from `n_a` to `n_b` is

```math
H(n_a)-H(n_b),
```

where

```math
H(n)=\int_0^n\frac{u}{R(u)}du
```

and therefore

```math
\boxed{H'(n)=\tau_{eff}(n).}
```

Now inject two equal impulsive carrier densities `q`, separated by `Delta`. Let `r(Delta)` be the residual density immediately before the second pulse. Since the system is dissipative,

```text
r'(Delta)<0.
```

The total integrated carrier response is

```math
A_2(\Delta)=H(q)-H(r)+H(r+q).
```

Differentiate:

```math
\frac{dA_2}{d\Delta}
=
[\tau_{eff}(r+q)-\tau_{eff}(r)]\,r'(\Delta).
```

Hence:

```math
\boxed{
\operatorname{sign}\left(\frac{dA_2}{d\Delta}\right)
=-\operatorname{sign}
[\tau_{eff}(r+q)-\tau_{eff}(r)].
}
```

Consequences:

- If `tau_eff(n)` decreases with carrier density, increasing pulse separation increases integrated response.
- If `tau_eff(n)` is constant, pulse separation does not matter.
- If `tau_eff(n)` increases with carrier density, increasing pulse separation decreases integrated response.

Equivalently, if the per-carrier recombination rate `R(n)/n` increases with density, temporal concentration reduces the integrated response.

For

```math
R(n)=a n+b n^2+c n^3,
\qquad a>0,\;b,c\ge0,
```

```math
R(n)/n=a+bn+cn^2
```

is nondecreasing, so the integrated response is nondecreasing with pulse separation and strictly increasing if `b>0` or `c>0` over the visited density range.

This contains the cubic Auger result as one special case.

## Mechanism interpretation

The sign of the two-pulse integrated-current correlation directly reports whether the effective carrier lifetime rises or falls with injection density in this lumped autonomous model.

This suggests a simple qualitative diagnostic:

```text
response increases with pulse separation
    -> lifetime falls with density
    -> superlinear recombination such as bimolecular/Auger is consistent

flat response
    -> locally linear recombination is consistent

response decreases with pulse separation
    -> lifetime rises with density
    -> trap saturation / another sublinear-loss mechanism is plausible
```

This sign diagnostic is not unique in realistic devices: extraction, diffusion, heating, field redistribution, contact effects, mobility changes, and non-autonomous trap populations can alter it.

## Prior-art boundary

Excitation-correlation spectroscopy already uses two delayed pulses and time-integrated photocurrent/photoluminescence to diagnose nonlinear recombination. Rojas-Gatjens et al., J. Phys. Chem. C (2023), DOI 10.1021/acs.jpcc.3c04755, explicitly model negative nonlinear photocurrent from bimolecular and Auger recombination using the same `gamma n + Bn^2` and `gamma n + An^3` rate equations.

Therefore the two-pulse diagnostic principle is established. The compact general sign identity above is useful for organizing the physics but is not presently a research-novelty claim.