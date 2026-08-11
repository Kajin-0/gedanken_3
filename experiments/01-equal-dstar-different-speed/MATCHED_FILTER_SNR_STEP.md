# Step 02 — Optimal SNR for a Specified Optical Waveform

**Date:** 2026-08-11 11:32 EDT  
**Status:** DERIVED under explicit linear/stationary assumptions. This is the next logical step after the scalar-`D*` counterexample. No generalized detector metric is proposed here.

---

## 1. Question

For a specified optical waveform and a fully specified linear detector with temporal transfer and output-noise PSD, what determines the maximum achievable measurement SNR?

---

## 2. Minimal assumptions

Assume:

1. the incident optical signal `p(t)` is deterministic, finite-energy, and known, including its timing;
2. the detector/readout chain is linear and time invariant;
3. the optical-to-output transfer function is the complex function `G(f)`;
4. additive output noise is zero-mean and wide-sense stationary with two-sided PSD `S_n(f)`;
5. signal and additive noise are independent;
6. the measurement may use any linear filter and enough delay/observation time to realize the matched filter;
7. `S_n(f) > 0` wherever the signal has support.

Gaussian noise is not required to maximize output SNR over linear filters. If the noise is Gaussian, the same matched-filter statistic also has the usual optimal known-signal detection interpretation.

Use the Fourier convention

```math
P(f)=\int_{-\infty}^{\infty}p(t)e^{-i2\pi ft}\,dt.
```

The detector output signal spectrum is

```math
S(f)=G(f)P(f).
```

---

## 3. General linear measurement

Let a linear measurement filter have frequency response `Q(f)` and form one scalar output. Its signal contribution is proportional to

```math
\mu_Q=\int_{-\infty}^{\infty}Q^*(f)S(f)\,df,
```

while the output-noise variance is

```math
\sigma_Q^2
=\int_{-\infty}^{\infty}|Q(f)|^2S_n(f)\,df.
```

Therefore

```math
\mathrm{SNR}_Q^2
=\frac{
\left|\int Q^*(f)S(f)\,df\right|^2
}{
\int |Q(f)|^2S_n(f)\,df
}.
```

---

## 4. Maximize the SNR

Write

```math
a(f)=Q(f)\sqrt{S_n(f)},
```

```math
b(f)=\frac{S(f)}{\sqrt{S_n(f)}}.
```

Then Cauchy-Schwarz gives

```math
\left|\int a^*(f)b(f)\,df\right|^2
\le
\left(\int|a|^2df\right)
\left(\int|b|^2df\right).
```

Hence

```math
\boxed{
\mathrm{SNR}_{\max}^2
=
\int_{-\infty}^{\infty}
\frac{|S(f)|^2}{S_n(f)}\,df
}
```

with equality for

```math
\boxed{
Q_{\mathrm{opt}}(f)\propto\frac{S(f)}{S_n(f)}
=\frac{G(f)P(f)}{S_n(f)}.
}
```

This is the colored-noise matched filter.

Substituting `S(f)=G(f)P(f)` gives

```math
\boxed{
\mathrm{SNR}_{\max}^2
=
\int_{-\infty}^{\infty}
|P(f)|^2
\frac{|G(f)|^2}{S_n(f)}\,df.
}
```

---

## 5. Connection back to frequency-specific D*

For active area `A`, define the local spectral-density detectivity

```math
D^*(f)
=\frac{\sqrt A\,|G(f)|}{\sqrt{S_n(f)}}.
```

Therefore

```math
\frac{|G(f)|^2}{S_n(f)}
=\frac{D^{*2}(f)}{A},
```

and

```math
\boxed{
\mathrm{SNR}_{\max}^2
=
\frac{1}{A}
\int_{-\infty}^{\infty}
|P(f)|^2D^{*2}(f)\,df.
}
```

This equation uses a two-sided PSD convention. A one-sided convention gives the equivalent result with the corresponding integration limits/factors.

---

## 6. First nontrivial consequence

**DERIVED / CONDITIONAL:** for a known finite-energy waveform in an LTI detector with additive stationary noise, maximum linear-filter SNR is a spectral overlap integral between the optical waveform and the detector's frequency-resolved signal-to-noise sensitivity.

A single scalar `D*` samples only one local part of that weighting and therefore cannot in general determine broadband-waveform SNR.

Equivalently, the detector quantity entering the integral is

```math
\frac{|G(f)|^2}{S_n(f)},
```

not `|G(f)|`, bandwidth, response time, or noise PSD separately.

This formulation automatically contains the cancellation noted in Step 01: if the same transfer function multiplies signal and dominant noise, its magnitude can cancel from `|G|^2/S_n`; if dominant additive noise enters after the signal pole, it does not cancel.

---

## 7. What this does NOT yet establish

- No new universal scalar detector metric has been defined.
- No claim that faster response is universally better.
- No treatment of unknown arrival time.
- No finite observation-window constraint.
- No signal-dependent shot noise or nonlinear detector behavior.
- No nonstationary or non-Gaussian optimal-decision theory.
- No statement yet about whether the full function `D*(f)` is sufficient once timing/window constraints are imposed.
- No novelty claim.

---

## 8. Stopping point

The first new principle is only:

> **Known-waveform detectability in the linear stationary-noise limit is determined by spectral signal-to-noise overlap, not by a single reference detectivity.**

Do not proceed further in this file.

### Single natural next question

> If two detectors have the same complete magnitude function `D*(f)` at every frequency, can they nevertheless differ in detectability once the optical event has an unknown arrival time or the observation window is finite?

This directly tests which information was discarded by the matched-filter/full-observation idealization without presupposing the answer.
