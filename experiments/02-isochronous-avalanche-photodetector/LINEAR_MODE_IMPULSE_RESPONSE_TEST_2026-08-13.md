# Linear-mode impulse-response test of transverse depth isochrony

**Date:** 2026-08-13  
**Status:** EXACT MEASUREMENT EQUIVALENCE / VALIDATION PLATFORM ONLY / NOT A NOVELTY CLAIM

## 1. Why leave Geiger mode for the first test

The depth-compensation physics is a statement about the distribution of detector response times. It does not require one-by-one photon timestamping.

Let the normalized intrinsic current impulse response for absorption coordinate `X=x` be

```math
h(t|x),
\qquad
\int h(t|x)dt=1.
```

Define its conditional mean and variance

```math
\mu(x)=\int t h(t|x)dt,
```

```math
s^2(x)=\int [t-\mu(x)]^2h(t|x)dt.
```

For detected-photon weighting `p(x)`, the normalized ensemble response to an optical delta pulse is

```math
H(t)=\int p(x)h(t|x)dx.
```

Then exactly

```math
\boxed{
Var_H(t)=Var_X[\mu(X)]+E_X[s^2(X)].
}
```

This is the same law-of-total-variance decomposition used for single-event timestamps.

Therefore a device that flattens `mu(x)` narrows the normalized analog impulse response by removing the same between-position mean-delay term.

## 2. Gain/charge weighting correction

If the integrated charge or avalanche gain depends on position, write the unnormalized conditional response as

```math
I(t|x)=Q(x)h(t|x).
```

The normalized measured response is then weighted by

```math
\tilde p(x)=\frac{p(x)Q(x)}{\int p(x')Q(x')dx'}.
```

All timing moments must use `tilde p`, not the optical absorption distribution alone.

Thus position-dependent collection efficiency or gain cannot be silently ignored. A low/moderate-gain linear-mode test with weak position dependence is preferable for the first demonstration.

## 3. Common source/instrument broadening cancels in variance differences

Let the optical source pulse and common measurement chain have normalized kernels with temporal variances `sigma_src^2` and `sigma_inst^2`. For convolution of finite-moment kernels,

```math
\boxed{
\sigma_{meas}^2
=\sigma_{src}^2+\sigma_{det}^2+\sigma_{inst}^2.
}
```

If forward and reverse measurements use the same source and instrument,

```math
\boxed{
\sigma_{meas,r}^2-\sigma_{meas,f}^2
=\sigma_{det,r}^2-\sigma_{det,f}^2.
}
```

This makes the **difference of squared impulse-response widths** a strong differential observable. Common laser pulse width and common instrument response do not have to be individually much smaller than the detector width, provided they remain stable and the convolution model is valid.

## 4. Current N=3 predictions

For the present three-step surrogate, exact forward match remains about

```text
8.37 ps RMS
```

under the historical stochastic assumptions.

For near-end traveling-wave readout:

```text
ve/vg=1.0 -> reverse ~12.06 ps RMS;  reverse^2-forward^2 ~75.5 ps^2
ve/vg=1.5 -> reverse ~13.62 ps RMS;  difference ~115.6 ps^2
ve/vg=2.0 -> reverse ~14.73 ps RMS;  difference ~147.0 ps^2
ve/vg=4.0 -> reverse ~17.06 ps RMS;  difference ~220.8 ps^2
```

These are reduced-order targets, not device predictions.

## 5. Measurement protocol

First physics demonstration:

1. operate the APD below breakdown in linear mode;
2. illuminate with a pulse short compared with the detector response scale;
3. acquire the intrinsic/matched-line current impulse response for forward propagation;
4. reverse only the optical propagation direction while keeping bias and electrical readout unchanged;
5. normalize pulse area and calculate first and second central temporal moments;
6. compare `sigma_r^2-sigma_f^2`, not only FWHM;
7. repeat versus bias to separate conditional-mean matching from the minimum-total-RMS operating point.

A direct/unmapped control remains useful, but forward/reverse on the same device is the cleaner first causal test.

## 6. Important waveform caveat

The probability-mixture interpretation requires a nonnegative normalized intrinsic detector-current kernel. AC coupling, transmission-line reflections, or aggressive equalization can create signed/bipolar waveforms for which naive temporal moments are not probability moments.

Therefore use a well-terminated line and either the intrinsic current response or a de-embedded causal response before applying the variance identity.

## 7. Prior-art disposition

Established prior art already covers:

- APD impulse response with arbitrary space/time ionization and carrier transport;
- traveling-wave APD distributed-current models including microwave loss, velocity mismatch, reflection, and multiplication/transport;
- waveguide/directional-coupler control of longitudinal absorption profiles;
- conventional transit-time, RC, and avalanche-buildup optimization.

The linear-mode impulse-response method is therefore **not** the research contribution.

The only surviving candidate device distinction remains the deliberate mapping of **transverse absorption depth** onto longitudinal optical/electrical propagation delay to flatten the conditional mean response time while retaining a substantial absorption volume.

Targeted searching has not yet established novelty or priority for that geometry/objective.

## 8. Decision

Use linear-mode traveling-wave APD operation as the preferred **first validation platform** because it removes local Geiger quench/TDC complexity while testing the same variance mechanism.

Do not reframe the work as a new impulse-response or bandwidth theory.

Next hard step: construct the minimal continuous common-junction electro-optic geometry that can realize three transverse absorption-depth states without creating separate local electrical timing branches.