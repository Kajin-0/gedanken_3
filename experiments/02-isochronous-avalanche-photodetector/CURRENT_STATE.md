# Experiment 02 — Isochronous Avalanche Photodetector

**Date:** 2026-08-13
**Status:** PROVISIONAL / SURVIVED FIRST PRIOR-ART SCREEN / NOVELTY NOT ESTABLISHED

## Question

Can random photon-absorption-position jitter in an APD/SPAD be reduced by deliberately compensating optical propagation delay against internal carrier transit delay to the avalanche region?

Plainly: a photon absorbed later optically can have a shorter carrier trip. Can those delays be made to cancel?

## Core condition

For random absorption coordinate `X`, define the conditional mean timestamp

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

Then

```math
Var(T)=Var[m(X)]+E[Var(T|X)].
```

The absorption-position contribution vanishes exactly if

```math
\boxed{m(X)=constant.}
```

For one coordinate `x`:

```math
\boxed{d[t_o+t_c+t_e+\mu_a]/dx=0.}
```

This removes only position-dependent deterministic delay. Avalanche stochasticity, diffusion, electronics jitter, and other conditional fluctuations remain.

## Status

Known literature already covers absorption-position jitter, carrier transport, waveguide SPADs, and optical/electrical velocity matching. Targeted searches have not yet found this specific optical-delay/internal-carrier-delay compensation in an APD/SPAD. That is not proof of novelty.

Do not write a paper or claim priority yet.