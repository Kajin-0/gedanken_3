# Step 08 — Continuous-Time Search Correlation and Timing-Trial Density

**Date:** 2026-08-11 12:47 EDT  
**Status:** DERIVED for a stationary, differentiable Gaussian matched-filter scan under full observation. The scan covariance is the autocorrelation of the noise-whitened signal template. A natural local correlation scale and exact mean high-level upcrossing rate follow from its SNR-weighted spectral second moment. There is no universal threshold-independent effective trial count. No novelty claim.

---

## 1. Question

In a continuous-time matched-filter search, what determines the correlation time / effective number of statistically distinct arrival-time trials, and how is that related to the detector's noise-whitened temporal response rather than to digital sampling rate?

This step replaces the independent-slot abstraction of Step 07 by the simplest continuous correlated Gaussian scan.

---

## 2. Noise-whitened template

For optical waveform `P(f)`, detector transfer `G(f)`, and stationary output-noise PSD `S_n(f)`, define

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}}.
```

Its total whitened energy is

```math
E_K=\int_{-\infty}^{\infty}|K(f)|^2df
=\rho_\infty^2.
```

Define the normalized spectral weight

```math
W(f)=\frac{|K(f)|^2}{E_K},
\qquad
\int W(f)df=1.
```

For a real-valued known-phase time-shift search, `W(f)` is even.

---

## 3. Continuous matched-filter scan under noise only

Let `z(tau)` be the normalized matched-filter output evaluated at candidate arrival time `tau`. Under additive stationary Gaussian noise and full observation,

```math
E[z(\tau)]=0,
```

```math
\operatorname{Var}[z(\tau)]=1.
```

Its covariance between two trial delays is

```math
\boxed{
r(\Delta)
=E[z(\tau)z(\tau+\Delta)]
=\int_{-\infty}^{\infty}
W(f)e^{i2\pi f\Delta}df.
}
```

Equivalently,

```math
\boxed{
r(\Delta)
=\frac{
\int |K(f)|^2e^{i2\pi f\Delta}df
}{
\int |K(f)|^2df
}.
}
```

Thus the timing-search correlation is set by the autocorrelation of the **noise-whitened signal template**, not by the ADC sample spacing.

Oversampling merely samples the same correlated Gaussian process more densely once the process is adequately resolved.

---

## 4. Connection directly to D*(f)

Using

```math
D^*(f)=\frac{\sqrt A\,|G(f)|}{\sqrt{S_n(f)}},
```

we have

```math
|K(f)|^2
=|P(f)|^2\frac{D^{*2}(f)}{A}.
```

Therefore

```math
\boxed{
W(f)
=\frac{|P(f)|^2D^{*2}(f)}
{\int |P(f')|^2D^{*2}(f')df'}.
}
```

The active-area factor cancels.

Hence, for a fixed optical waveform in this full-observation stationary problem, two detectors with identical complete magnitude `D*(f)` have identical `W(f)`, identical scan covariance `r(Delta)`, and therefore identical continuous-time timing-search statistics.

**REFINEMENT OF STEP 07:** phase-only differences or higher digital sampling rate do not create a larger full-observation timing trials factor when complete magnitude `D*(f)` is unchanged. A larger search penalty can arise only insofar as the SNR-weighted magnitude spectrum itself becomes broader or otherwise changes.

---

## 5. Local correlation scale from spectral second moment

Assume the second spectral moment is finite:

```math
\int f^2W(f)df<\infty.
```

Define the SNR-weighted RMS frequency

```math
\boxed{
f_{\mathrm{rms}}
=\left[\int f^2W(f)df\right]^{1/2}.
}
```

Since `W` is even,

```math
r'(0)=0,
```

and

```math
\boxed{
-r''(0)
=(2\pi)^2f_{\mathrm{rms}}^2.
}
```

Therefore, near zero delay,

```math
r(\Delta)
=1-2\pi^2f_{\mathrm{rms}}^2\Delta^2+O(\Delta^4).
```

A natural local curvature correlation time is

```math
\boxed{
\tau_{\mathrm{curv}}
\equiv\frac{1}{\sqrt{-r''(0)}}
=\frac{1}{2\pi f_{\mathrm{rms}}}.
}
```

This is a local decorrelation scale, not a claim of a universal independent-trial spacing.

In terms of the optical waveform and frequency-resolved detectivity,

```math
\boxed{
f_{\mathrm{rms}}^2
=\frac{
\int f^2|P(f)|^2D^{*2}(f)df
}{
\int |P(f)|^2D^{*2}(f)df
}.
}
```

Thus timing resolution/search correlation is governed by an **SNR-weighted spectral width**, not by detector bandwidth or response time in isolation.

---

## 6. Exact mean upcrossing rate: Rice result

For a differentiable stationary unit-variance Gaussian process, `z(tau)` and its derivative `dot z(tau)` are jointly Gaussian. Because `r'(0)=0`, they are independent, with

```math
\operatorname{Var}[\dot z]
=-r''(0)
=(2\pi f_{\mathrm{rms}})^2.
```

The Rice level-crossing calculation gives the exact mean number of **upcrossings** of threshold `u` per unit search time:

```math
\boxed{
\nu_u^+
=\frac{\sqrt{-r''(0)}}{2\pi}
 e^{-u^2/2}
=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

For a monitoring duration `L`,

```math
\boxed{
E[N_u^+]
=L f_{\mathrm{rms}}e^{-u^2/2}.
}
```

This is exact for the expected number of upcrossings under the stated differentiability assumptions. It is **not** by itself the exact probability that the supremum exceeds `u`.

At high thresholds where excursions are rare and well separated, the upcrossing count gives the leading continuous-search false-alarm approximation (up to endpoint and multiple-excursion corrections):

```math
P_{FA,global}(u)
\approx
Q(u)+L f_{\mathrm{rms}}e^{-u^2/2}.
```

For a long interval where the interior term dominates and the false-alarm probability is small,

```math
\boxed{
u
\approx
\sqrt{2\ln\!\left(\frac{L f_{\mathrm{rms}}}{\alpha}\right)}
}
```

is the leading threshold estimate. Standard Gaussian-extreme-value corrections are needed for precision work.

---

## 7. There is no universal effective M

If one insists on comparing the continuous search to the independent-slot approximation

```math
P_{FA}\approx M_{\mathrm{eff}}Q(u),
```

then matching the high-threshold Rice term gives

```math
\boxed{
M_{\mathrm{eff}}(u)
\approx
\frac{L f_{\mathrm{rms}}e^{-u^2/2}}{Q(u)}.
}
```

Using

```math
Q(u)\sim\frac{e^{-u^2/2}}{\sqrt{2\pi}\,u},
```

for large `u`,

```math
\boxed{
M_{\mathrm{eff}}(u)
\sim
\sqrt{2\pi}\,u\,L f_{\mathrm{rms}}.
}
```

Therefore the effective independent-trials count is **threshold dependent**. There is no unique detector-only scalar `M_eff` that is valid at all false-alarm levels.

The robust quantities are the full covariance `r(Delta)` and, locally, its curvature / `f_rms`.

---

## 8. Smooth illustrative example

Take a Gaussian SNR-weighted spectrum

```math
W(f)
=\frac{1}{\sqrt{2\pi}\sigma_f}
\exp\!\left(-\frac{f^2}{2\sigma_f^2}\right).
```

Then

```math
f_{\mathrm{rms}}=\sigma_f,
```

and

```math
\boxed{
r(\Delta)
=\exp(-2\pi^2\sigma_f^2\Delta^2).
}
```

Thus

```math
\tau_{\mathrm{curv}}=\frac{1}{2\pi\sigma_f},
```

and the exact mean upcrossing rate is

```math
\boxed{
\nu_u^+
=\sigma_f e^{-u^2/2}.
}
```

Changing the ADC sampling rate while leaving `sigma_f` unchanged leaves all of these continuous-time search statistics unchanged, provided sampling remains adequate to represent the process.

---

## 9. Important regularity failure of the ideal one-pole exponential

The earlier illustrative waveform

```math
s_\tau(t)=S_0e^{-t/\tau}u(t)
```

has an abrupt onset at `t=0`. In ideal white noise its spectral energy behaves only as `1/f^2` at high frequency. Consequently

```math
\int f^2W(f)df
```

diverges.

Therefore the idealized one-pole exponential produces a matched-filter scan that is not mean-square differentiable, and the curvature / Rice upcrossing formula above cannot be applied to it without additional high-frequency regularization.

This does **not** invalidate Steps 05–07, which used its finite-energy SNR accumulation. It only means that the continuous-time timing-search crossing density requires a physically finite high-frequency bandwidth or a smoother optical/detector response.

A real detector/readout chain necessarily supplies such regularization; alternatively one may use a smooth finite-bandwidth waveform as in Section 8.

This caveat is scientifically important and must not be hidden.

---

## 10. First nontrivial consequence

**DERIVED / CONDITIONAL:** in a continuous stationary Gaussian matched-filter timing search, the search correlation is determined by

```math
r(\Delta)
=\mathcal F^{-1}\{W(f)\},
```

with

```math
W(f)
\propto |P(f)|^2D^{*2}(f).
```

When the second spectral moment exists, the natural local timing scale is

```math
\boxed{
\tau_{\mathrm{curv}}=
\frac{1}{2\pi f_{\mathrm{rms}}}
}
```

and the exact mean threshold-upcrossing density is

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

Thus the trials penalty is controlled by the detector-waveform **SNR-weighted spectral shape**, not by sample count and not by response time alone.

This also sharpens the earlier speed/search competition: if a faster detector broadens the frequencies that contribute useful SNR, it can increase `f_rms` and therefore the search penalty; a phase-only speed difference at fixed complete `D*(f)` does not.

---

## 11. What has been established

- **DERIVED:** the continuous matched-filter scan covariance is the normalized autocorrelation of the noise-whitened signal template.
- **DERIVED:** for fixed waveform, `W(f)` is proportional to `|P(f)|^2D*^2(f)`.
- **DERIVED:** identical complete `D*(f)` implies identical full-observation continuous-time timing-search covariance for the same waveform.
- **DERIVED:** if the SNR-weighted second spectral moment is finite, `-r''(0)=(2pi)^2 f_rms^2` and `tau_curv=1/(2pi f_rms)`.
- **DERIVED:** Rice's formula gives exact mean upcrossing rate `nu_u^+=f_rms exp(-u^2/2)`.
- **DERIVED / CONDITIONAL:** high-threshold global false-alarm probability can be approximated from the upcrossing rate; the corresponding independent-trial `M_eff` is threshold dependent rather than universal.
- **REFINEMENT:** higher digital sampling rate alone does not increase the continuous-time trials penalty, and phase-only detector differences at equal complete `D*(f)` do not change it under the full-observation assumptions.
- **REGULARITY WARNING:** the ideal abrupt one-pole exponential has divergent second spectral moment in ideal white noise, so the differentiable-process Rice formula requires physical high-frequency regularization.

---

## 12. What has not been established

- No exact closed-form supremum distribution for arbitrary correlated matched-filter processes.
- No universal threshold-independent effective timing-trial count.
- No claim that `f_rms` alone determines the full search threshold away from the high-threshold/local-curvature regime; the full covariance `r(Delta)` can matter.
- No finite-window nonstationary edge treatment in the continuous scan.
- No unknown amplitude/phase, sequential stopping, shot-noise, nonlinear, saturation, dead-time, or nonstationary treatment.
- No universal scalar replacement for `D*`.
- No novelty claim.

---

## 13. Stopping point

The physically meaningful continuous-time search scale has been identified without equating it to digital sample count.

### Single natural next question

> Given the two competing effects now identified — SNR accumulation `eta(T)` and continuous-time search width `f_rms` — can one construct two detectors with equal asymptotic SNR for which the faster detector's larger search penalty actually reverses the finite-time detection ranking, or is rapid SNR accumulation guaranteed to dominate under some broad conditions?
