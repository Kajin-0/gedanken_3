# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 11:32 EDT  
**Status:** two logical steps completed. Step 01 showed that equal reference-condition `D*` does not guarantee equal SNR for arbitrary signals. Step 02 derives the maximum linear-filter SNR for a known finite-energy optical waveform in additive stationary noise. No generalized replacement metric or novelty claim.

---

## 1. Starting point

Two detectors satisfy

```math
D_A^*=D_B^*,
```

with

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

The original question is whether equality of conventional specific detectivity alone guarantees equal ability to detect an arbitrary optical signal.

---

## 2. Step 01 — scalar D* is insufficient

Interpret the given equality as equality at a low-frequency/reference condition. Choose equal area `A`, equal low-frequency responsivity `R0`, equal additive white output-noise density `n0`, and first-order temporal responses

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i}.
```

Then

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A\,R_0}{n_0}.
```

For the same optical tone of RMS amplitude `P_m` at frequency `f_m`, measured in the same ENBW `B`,

```math
\mathrm{SNR}_i
=\frac{P_mD_0^*}{\sqrt{AB}}|H_i(f_m)|.
```

At `f_m=1 Hz`,

```math
|H_A|\approx1,
\qquad
|H_B|\approx0.157,
```

so

```math
\boxed{\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.}
```

**DERIVED / COUNTEREXAMPLE:** equal low-frequency/reference `D*` does not guarantee equal SNR for every optical signal.

Critical qualification: this is an insufficiency result, not `fast is always better`. If dominant noise is filtered by the same pole, signal/noise attenuation can cancel.

---

## 3. Step 02 — known-waveform optimal SNR

Now specify a deterministic finite-energy optical waveform `p(t)` with Fourier transform `P(f)`. Let the complete optical-to-output transfer function be `G(f)`, and let additive zero-mean wide-sense-stationary output noise have two-sided PSD `S_n(f)`.

The output signal spectrum is

```math
S(f)=G(f)P(f).
```

For an arbitrary linear measurement filter `Q(f)`,

```math
\mathrm{SNR}_Q^2
=\frac{
\left|\int Q^*(f)S(f)\,df\right|^2
}{
\int |Q(f)|^2S_n(f)\,df
}.
```

Cauchy-Schwarz gives the maximum

```math
\boxed{
\mathrm{SNR}_{\max}^2
=
\int_{-\infty}^{\infty}
\frac{|S(f)|^2}{S_n(f)}\,df
}
```

with matched filter

```math
\boxed{
Q_{\mathrm{opt}}(f)\propto\frac{S(f)}{S_n(f)}.
}
```

Thus

```math
\boxed{
\mathrm{SNR}_{\max}^2
=
\int_{-\infty}^{\infty}
|P(f)|^2\frac{|G(f)|^2}{S_n(f)}\,df.
}
```

For the frequency-resolved spectral-density convention

```math
D^*(f)=\frac{\sqrt A\,|G(f)|}{\sqrt{S_n(f)}},
```

this is equivalently

```math
\boxed{
\mathrm{SNR}_{\max}^2
=
\frac1A\int_{-\infty}^{\infty}|P(f)|^2D^{*2}(f)\,df.
}
```

See `MATCHED_FILTER_SNR_STEP.md` for the explicit derivation and assumptions.

---

## 4. First consequence of Step 02

**DERIVED / CONDITIONAL:** for a known finite-energy waveform, LTI response, additive stationary noise, and unrestricted linear filtering/full observation, detectability is governed by a spectral overlap integral between the waveform and the detector's frequency-resolved signal-to-noise sensitivity.

The detector factor entering the integral is

```math
\frac{|G(f)|^2}{S_n(f)},
```

not temporal bandwidth, response time, responsivity, or noise PSD separately.

A single scalar `D*` is only local information and cannot in general determine broadband-waveform SNR.

The formulation also automatically handles the Step-01 cancellation: if the same transfer magnitude acts on both signal and dominant noise, it can cancel inside `|G|^2/S_n`; if noise enters after the signal pole, it does not.

---

## 5. Assumptions that must not be silently dropped

The Step-02 result assumes:

- known deterministic waveform, including timing;
- finite signal energy;
- linear time-invariant detector/readout response;
- additive signal-independent stationary noise;
- a two-sided PSD convention in the displayed integrals;
- enough observation time/delay to realize the matched filter;
- maximization over linear filters;
- `S_n(f)>0` over signal support.

Gaussianity is not required for the maximum-linear-SNR derivation. It is needed for the stronger standard claim that the matched-filter statistic is also optimal in the usual known-signal Gaussian detection problem.

---

## 6. What has been established

**DERIVED:** equal reference-condition scalar `D*` does not determine arbitrary-signal SNR.

**DERIVED:** in the restricted known-waveform LTI/stationary-noise problem,

```math
\mathrm{SNR}_{\max}^2
=
\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
```

**DERIVED:** frequency-resolved `D*(f)` enters this restricted problem quadratically as a waveform-dependent spectral weighting.

---

## 7. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No new scalar performance metric.
- No result for unknown arrival time.
- No finite observation-window result.
- No treatment of signal-dependent shot noise, nonlinearities, saturation, nonstationary noise, or globally optimal non-Gaussian decisions.
- No claim yet that the full function `D*(f)` is sufficient once timing/window constraints are imposed.
- No novelty claim.

---

## 8. Single natural next question — DO NOT ANSWER YET

> If two detectors have the same complete magnitude function `D*(f)` at every frequency, can they nevertheless differ in detectability once the optical event has an unknown arrival time or the observation window is finite?

This tests which information was discarded by the known-timing/full-observation matched-filter idealization.