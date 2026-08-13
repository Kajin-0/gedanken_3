# GR-limited HgCdTe timing-information result

**Date:** 2026-08-13
**Status:** DEVICE-PHYSICS EXTENSION / NOVELTY UNESTABLISHED

## Core model

Use the small-signal carrier-balance equation

```math
\dot{\delta N}=-\delta N/\tau+\eta\Phi(t)+\xi_{GR}(t).
```

For a first-order photoconductor, the optical carrier signal and intrinsic generation-recombination (GR) fluctuations share the same lifetime pole. With equilibrium carrier-number variance represented by `N0`, use

```math
|\delta N_{sig}(\omega)|^2
=\frac{\eta^2\tau^2|P(\omega)|^2}{1+\omega^2\tau^2},
```

and the standard single-time-constant GR spectrum

```math
S_{N,GR}(\omega)=\frac{2N_0\tau}{1+\omega^2\tau^2}.
```

Therefore the GR-limited whitened information spectrum is

```math
\boxed{
\mathcal I_{GR}(\omega)
=\frac{|\delta N_{sig}|^2}{S_{N,GR}}
=\frac{\eta^2\tau}{2N_0}|P(\omega)|^2.
}
```

The lifetime pole cancels exactly.

## Consequence for unknown-arrival timing

After normalization, the matched-filter timing covariance is

```math
\boxed{
R_{GR}(\Delta)
=\frac{\int |P(\omega)|^2e^{i\omega\Delta}d\omega}
{\int |P(\omega)|^2d\omega},
}
```

which is independent of raw carrier lifetime `tau`.

Thus, in the ideal GR-noise-limited photoconductor, the detector can have a slow measured decay while the optimally whitened timing-search geometry is controlled by the optical event rather than by the lifetime pole.

Lifetime still changes the total available information through the prefactor `tau/N0`; the cancellation concerns normalized timing geometry, not eventual SNR.

## Add Johnson/readout white noise

Let the measured current-noise PSD be approximated over the transient-information band by

```math
S_i(\omega)
=\frac{S_{GR,0}}{1+\omega^2\tau^2}+S_W,
```

where `S_W` combines approximately white Johnson and readout/amplifier contributions.

The detector-dependent factor in the whitened information spectrum becomes a Lorentzian with

```math
\boxed{
\tau_I=\frac{\tau}{\sqrt{1+\lambda_{GR}}},
\qquad
\lambda_{GR}=\frac{S_{GR,0}}{S_W}.
}
```

Therefore

```text
lambda_GR = 1  -> tau_I/tau = 0.707
lambda_GR = 3  -> tau_I/tau = 0.500
lambda_GR = 9  -> tau_I/tau = 0.316
```

This gives a directly measurable criterion: if the low-frequency GR PSD is comparable to or larger than the white floor, the timing-information width should differ substantially from the raw detector lifetime.

## Finite optical pulse

For a unit-area exponential optical pulse with time constant `tau_p`, the whitened timing covariance is

```math
R(\Delta)=
\frac{\tau_p e^{-|\Delta|/\tau_p}
-\tau_I e^{-|\Delta|/\tau_I}}
{\tau_p-\tau_I}.
```

Its local curvature is

```math
\boxed{R''(0)=-\frac{1}{\tau_p\tau_I}.}
```

Thus the local timing scale is the geometric mean

```math
\boxed{\tau_{local}=\sqrt{\tau_p\tau_I}.}
```

This makes the separation explicit:

```text
raw detector decay: tau
noise-adjusted detector information time: tau_I
optical event time: tau_p
local timing-search scale: sqrt(tau_p tau_I)
```

## 1/f noise

A realistic HgCdTe spectrum can also contain `1/f` noise and extra Lorentzians from traps or shunts. In that case the exact information spectrum is

```math
\mathcal I(\omega)
=\frac{|S_{sig}(\omega)|^2}
{S_{GR}(\omega)+S_W+S_{1/f}(\omega)+\cdots}.
```

No single `tau_I` is then exact. The full measured PSD should be used directly. Low-frequency excess noise is down-weighted by whitening and can reduce total SNR without necessarily broadening the timing statistic in proportion to the raw detector response.

## Experimental test

Measure on the same HgCdTe photoconductor:

1. small-signal frequency response -> `tau`;
2. dark noise PSD -> fit GR Lorentzian, white floor, and `1/f` term;
3. transient response to a known optical pulse;
4. construct the optimal whitening/matched filter from the measured PSD;
5. scan it in arrival time and measure the normalized correlation width.

Compare the observed scan covariance with the prediction from the measured noise decomposition. The strongest test is a bias/temperature/background sweep that changes `S_GR,0/S_W` while independently tracking `tau`.

## Prior-art status

Classical photoconductor theory already links response time, responsivity, GR noise, background, and material parameters. HgCdTe measurements also show combinations of `1/f`, GR Lorentzians, shunt noise, and lifetime-dependent response. Optimum-filter literature already treats arbitrary stationary noise spectra. The specific detector-facing timing-search consequence above has not yet been established as novel.

**Do not claim novelty or priority.**