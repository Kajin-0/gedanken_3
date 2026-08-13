# HgCdTe timing-information experiment

**Date:** 2026-08-13
**Status:** FALSIFIABLE EXPERIMENT DESIGN / NO NOVELTY CLAIM

## Question

Does the timing width of an optimally whitened transient from a HgCdTe photoconductor equal the raw photoconductive lifetime, or is it shortened because GR noise carries the same lifetime pole as the signal?

## Direct prediction

Fit the device noise over the transient band as

```math
S_n(f)=\frac{S_{GR,0}}{1+(f/f_tau)^2}+S_W+S_{1/f}(f)+...,
```

where

```math
f_tau=1/(2 pi tau).
```

If `1/f` is negligible over the main transient-information band, define

```math
lambda = S_GR,0/S_W.
```

Then

```math
\boxed{tau_I=tau/sqrt(1+lambda)}
```

and

```math
\boxed{f_I=f_tau sqrt(1+lambda)}.
```

The GR/white equality frequency is

```math
f_x=f_tau sqrt(lambda-1), lambda>1,
```

so for strong GR noise the information bandwidth is physically set near the frequency where the lifetime-shaped GR spectrum falls into the non-common-path white floor.

## Model-independent analysis

The experiment does not actually require a GR/white fit. Measure a transient waveform `s(t)` and dark-noise PSD `S_n(f)` on the same device and operating point. Compute

```math
I(f)=|S(f)|^2/S_n(f).
```

Then obtain

```math
rho_inf^2 = integral I(f) df,
```

and the normalized timing covariance

```math
R(Delta)=
[integral I(f) exp(i 2 pi f Delta) df]
/ [integral I(f) df].
```

A local timing bandwidth can be defined from the second spectral moment,

```math
B_t^2 =
[integral (2 pi f)^2 I(f) df]
/ [integral I(f) df],
```

with local timing scale

```math
tau_local = 1/B_t.
```

Compare these quantities with the ordinary decay time `tau` or `f_3dB`.

## Strong experimental control

Do not rely only on comparisons between different devices. On one detector:

1. measure the baseline pulse response and noise PSD;
2. add a calibrated downstream white-noise contribution without changing the detector;
3. repeat the optimal-whitening/timing analysis.

Increasing downstream white noise raises `S_W`, lowers `lambda`, and predicts

```math
tau_I -> tau.
```

Reducing downstream noise or increasing the GR fraction predicts

```math
tau_I < tau.
```

This is a causal test of noise placement rather than a correlation across devices.

## Additional sweeps

Useful independent controls:

- temperature: changes lifetime, resistance, and GR population;
- optical background: changes carrier generation and GR noise;
- bias: changes responsivity, sweepout, and excess noise;
- readout configuration: changes the downstream floor without changing material lifetime.

## Concrete published scale

A 2025 MWIR HgCdTe photoconductor study reports approximately `tau = 1.15 us` at 77 K, measured with a 10 ns optical pulse, together with separate noise spectra containing both 1/f and GR components. Its reported 1/f knee is about 1 kHz at 77 K, far below `1/(2 pi tau) ≈ 138 kHz`.

For that lifetime, illustrative ratios give:

```text
S_GR,0/S_W   tau_I
0            1.150 us
1            0.813 us
3            0.575 us
9            0.364 us
99           0.115 us
```

The PSD ratios are not taken from that paper and must not be attributed to it.

## Falsification conditions

The simple GR/white model fails if any of the following occurs materially in the information band:

- multiple recombination/trap Lorentzians;
- significant sweepout or transit-time poles;
- nonstationary or signal-dependent noise;
- strong 1/f noise extending into the timing band;
- electronics bandwidth/aliasing not included in `S_n(f)`;
- nonlinear response.

The model-independent `|S|^2/S_n` construction remains usable under stationary linear conditions even when the two-component fit fails.

## Publication status

The general optimum-filter mathematics is established prior art. A future publication would require an experimentally demonstrated detector-specific consequence that is not already reported, not merely this derivation.