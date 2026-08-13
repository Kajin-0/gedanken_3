# Current State — Experiment 03: When is photon recycling visible in terminal noise?

**Date:** 2026-08-13
**Status:** ACTIVE / MAJOR DEVICE-CLASS BOUNDARY ESTABLISHED / NOVELTY NOT ESTABLISHED

## Revised central question

HgCdTe photon recycling can move an excitation from one pixel to another by radiative recombination followed by photon reabsorption.

The original question was whether this exchange must appear as spontaneous inter-pixel electrical noise correlation.

The answer is now more precise:

```text
NO — visibility depends qualitatively on what the terminal readout measures.
```

The same internal exchange can produce a strong carrier-population cross-spectrum in an occupancy-sensitive photoconductor and **zero** cross-spectrum in an ideal endpoint-counting photodiode.

This is now the central device-physics result of Experiment 03.

## Prior-art boundaries already established

Do not claim the following as new:

- HgCdTe photon recycling / optical crosstalk;
- sign-changing equilibrium cross-spectra from conservative exchange;
- general fluctuation-response / network inference;
- passive crosstalk correlation in SPAD arrays;
- Poisson departure processes from independent linear routing networks;
- Shockley-Ramo coupling of carrier motion to junction terminal current.

Relevant adjacent prior art is documented in the experiment files.

## Internal carrier exchange: exact two-pixel result

For two identical carrier reservoirs with mean `m`, local non-transfer relaxation `gamma`, and conservative exchange rate `k`,

```math
M=\begin{pmatrix}
\gamma+k&-k\\
-k&\gamma+k
\end{pmatrix}.
```

Common and difference relaxation rates are

```math
\lambda_+=\gamma,
\qquad
\lambda_-=\gamma+2k.
```

The stationary equal-time covariance is

```math
P=mI,
```

so distinct pixels have zero equal-time covariance despite dynamical coupling.

The internal carrier cross-spectrum is

```math
\boxed{
S_{x,12}(\omega)=
m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].}
```

It is positive at low frequency, negative at high frequency, and crosses zero at

```math
\boxed{\omega_x=\sqrt{\gamma(\gamma+2k)}.}
```

Time-domain cross covariance:

```math
\boxed{
C_{12}(t)=\frac{m}{2}
[e^{-\gamma|t|}-e^{-(\gamma+2k)|t|}].}
```

Thus `C12(0)=0` but `C12(t)>0` for nonzero lag.

The qualitative exchange-noise structure is old in other physical systems.

## Deterministic / occupancy-noise closure

Localized steady generation in pixel 1 gives the internal neighboring/self response

```math
\boxed{c_{dc}=\frac{k}{\gamma+k}.}
```

For the **internal population observable**,

```math
\frac{S_{x,12}(0)}{S_{x,11}(0)}=+c_{dc},
```

and

```math
\frac{S_{x,12}(\infty)}{S_{x,11}(\infty)}=-c_{dc}.
```

The full normalized spectrum is

```math
\boxed{
\frac{S_{x,12}(\omega)}{S_{x,11}(\omega)}
=c_{dc}
\frac{\omega_x^2-\omega^2}
{\omega_x^2+\omega^2},
}
```

with

```math
\omega_x^2=\gamma^2\frac{1+c_{dc}}{1-c_{dc}}.
```

If a terminal readout is proportional to carrier occupancy, this is a no-free-shape prediction once `gamma` and `c_dc` are independently measured.

## N-pixel exchange graph

For symmetric exchange graph Laplacian `L`,

```math
M=\gamma I+L.
```

The equilibrium carrier cross-spectral matrix is

```math
\boxed{
S_x(\omega)=2mM(M^2+\omega^2I)^{-1}.}
```

Low frequency:

```math
S_x(0)=2mM^{-1},
```

which contains the same Green-function matrix as the steady deterministic response.

High frequency:

```math
S_x(\omega)=\frac{2m}{\omega^2}M
-\frac{2m}{\omega^4}M^3+O(\omega^{-6}).
```

A direct exchange edge gives

```math
S_{x,ij}\sim-2mk_{ij}/\omega^2.
```

No direct edge means the `1/omega^2` term vanishes.

For continuous local diffusion across physical separation `d`, the high-frequency Green function is suppressed approximately as

```math
\omega^{-1/2}\exp[-d\sqrt{\omega/(2D)}],
```

so a long-range direct radiative jump and local diffusion have different ideal high-frequency structure. This is a candidate mechanism discriminator, not established novelty.

## Photon-recycling factorization

In the fast-photon limit, let `Gamma_r` be the small-signal radiative recombination event rate per pair and `p_ij` the probability that an emitted photon from pixel `i` is reabsorbed in pixel `j`.

Then

```math
\boxed{k_{ij}=\Gamma_r p_{ij}.}
```

A radiative origin therefore predicts

```math
\boxed{k_{ij}/p_{ij}=\Gamma_r}
```

across the spatial coupling matrix if one source population is adequate.

This could be compared against an independently calculated optical transfer kernel. Carrier diffusion has no reason to follow the same optical kernel.

## CRITICAL NEW RESULT — ideal extraction current can erase the exchange noise

See `EXTRACTION_CURRENT_CANCELLATION.md`.

Split local loss into measured extraction `Gamma_e` plus other loss `Gamma_o`:

```math
\gamma=\Gamma_e+\Gamma_o.
```

Let the ideal terminal observable count final extraction events. In event-rate units,

```math
j_e=\Gamma_e x+\zeta_e,
```

where `zeta_e` is extraction shot noise.

The same extraction event also removes the carrier from the internal state, so the state/output noises are correlated. Carrying that correlation through exactly gives

```math
\boxed{
S_{j_e}(\omega)=\Gamma_e m I.
}
```

Therefore

```math
\boxed{S_{j_e,12}(\omega)=0}
```

at every frequency, even though `S_x,12(omega)` is sign-changing and nonzero.

This cancellation is not merely Gaussian. With independent Poisson generation and independent one-particle routing, each excitation receives one random final sink and delay. Poisson marking/thinning/displacement makes the final sink streams independent Poisson processes.

### Counterintuitive consequence

```text
nonzero mean optical crosstalk
DOES NOT imply
nonzero passive extraction-current cross-noise.
```

An excitation can be routed from source pixel A to final collection in pixel B, changing the mean point-spread/crosstalk, while the two final count streams remain independent Poisson thinnings.

## Why SPAD arrays behave differently

SPAD crosstalk is branching rather than conservative routing: the avalanche in pixel A is already recorded, and avalanche luminescence can trigger an **additional** recorded avalanche in pixel B. One primary event can therefore create multiple measured outputs, so inter-pixel timing correlations appear naturally.

This does not contradict the conservative-routing cancellation.

## Device-class boundary

### Photoconductor / occupancy-sensitive readout

Under fixed bias,

```math
\delta I_i\approx g_{I,i}x_i.
```

Internal exchange noise is visible at the terminal, subject to filtering and additive readout noise.

### Ideal endpoint-counting photodiode

Final extraction streams can be exactly independent Poisson; internal exchange noise is invisible.

### Real junction photodiode

A real current can contain Shockley-Ramo induced current during carrier motion, finite transit/diffusion response, capacitance/charge storage, and other distributed transport effects. It is therefore not generally equivalent to endpoint counting.

A real HgCdTe photodiode requires an explicit transport/Ramo readout model before a passive cross-noise prediction is valid.

## Numerical validation

An exact Gillespie simulation with

```text
gamma = 1
gamma_e = 0.6
gamma_o = 0.4
k = 1.5
m ~ 2 carriers per pixel
```

reproduced the internal population limits

```text
low-f S12/S11  ~ +0.57   (theory +0.60)
high-f S12/S11 ~ -0.60   (theory -0.60)
```

while simultaneously counted extraction streams remained consistent with zero cross-spectrum in every tested band.

See `numerics/extraction_current_cancellation_gillespie.py`.

## Current novelty status

```text
exchange-noise mathematics: old
Poisson-output cancellation mathematics: old
SPAD passive crosstalk correlations: old
HgCdTe deterministic photon recycling: old

readout-observable boundary for HgCdTe photon-recycling noise:
    useful / novelty not established
```

Do not build a manuscript yet.

## Next question

Derive the most general simple readout criterion using a Poisson-lineage / shot-noise description:

> Under what terminal impulse response does one recycled excitation contribute to more than one pixel waveform, making the photon-recycling cross-spectrum observable?

Then specialize that criterion to:

1. a voltage-biased HgCdTe photoconductor;
2. an ideal endpoint-counting photodiode;
3. a finite-transit Shockley-Ramo photodiode;
4. a branching/gain device such as a SPAD/e-APD.

This is the correct next step before any further novelty claim.