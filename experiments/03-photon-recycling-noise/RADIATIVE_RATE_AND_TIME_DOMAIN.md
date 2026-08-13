# Time-domain interpretation and radiative-rate factorization

**Date:** 2026-08-13
**Status:** EXACT IN MINIMAL MODEL / DETECTOR-SPECIFIC INTERPRETATION

For identical pixels,

```math
\boxed{C_{12}(t)=\frac{m}{2}[e^{-\gamma|t|}-e^{-(\gamma+2k)|t|}].}
```

Hence `C12(0)=0`, but `C12(t)>0` for every nonzero lag, and

```math
\boxed{C_{12}(t)=mk\,t+O(t^2)\quad(t\to0^+).}
```

The initial short-lag slope contains the exchange rate. The corresponding cross spectrum is positive at low frequency and negative at high frequency. The fast negative component encodes the microscopic transfer event (`-1` pair in the emitter, `+1` in the receiver); the slower population following produces positive lagged correlation. Their integrated spectral areas cancel, leaving zero equal-time covariance.

This qualitative exchange-noise structure is prior art in other physical systems.

## Photon-recycling rate factorization

Let `Gamma_r` be the small-signal radiative recombination event rate per carrier pair. For an emitted photon define probabilities `p_self`, `p_ij`, and `p_loss` for self-reabsorption, reabsorption in another active pixel, and loss from the modeled active-pixel set, with

```math
p_{self}+p_{loss}+\sum_{j\ne i}p_{ij}=1.
```

If photon flight/reabsorption is fast compared with carrier relaxation, inter-pixel recycling is an effective carrier-pair jump:

```math
\boxed{k_{ij}=\Gamma_r p_{ij}.}
```

Self-reabsorption has no net effect on the coarse pixel carrier number. Radiative escape contributes to local loss. In the minimal model,

```math
\boxed{\gamma=\Gamma_{nr}+\Gamma_{ext}+\Gamma_r p_{loss}.}
```

Therefore a photon-recycling origin imposes a spatial factorization closure:

```math
\boxed{k_{ij}/p_{ij}=\Gamma_r}
```

for all pixel pairs described by one source population.

The inferred exchange kernel `k_ij` can thus be compared with an independently modeled emission-spectrum-weighted optical transfer kernel `p_ij`. Carrier diffusion has no reason to reproduce that optical kernel.

If `p_ij` and `p_loss` are independently known, then in principle

```math
\Gamma_r=k_{ij}/p_{ij}
```

and

```math
\Gamma_{nr}+\Gamma_{ext}=\gamma-\Gamma_r p_{loss}.
```

This is a candidate detector application, not yet a novelty claim. Real HgCdTe devices may require a distributed carrier/photon model rather than one scalar radiative rate.