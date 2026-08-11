# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 12:47 EDT  
**Status:** eight logical steps completed. The project has progressed from scalar `D*` insufficiency to an exact continuous-time Gaussian timing-search correlation structure. No universal replacement metric and no novelty claim.

---

## 1. Original starting point

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

Original question: does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Step 01 — scalar reference D* is insufficient

Under equal area, equal low-frequency responsivity, equal additive white output-noise density, and first-order response

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i},
```

equal low-frequency/reference `D*` does not guarantee equal SNR for a 1 Hz optical tone. The explicit example gives

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.
```

**DERIVED / COUNTEREXAMPLE:** scalar reference `D*` is insufficient for arbitrary temporal signals.

**Qualification:** if dominant noise is filtered by the same pole, signal/noise attenuation can cancel. Do not infer `fast is always better`.

---

## 3. Step 02 — known-waveform full-observation SNR

For optical waveform `P(f)`, LTI detector transfer `G(f)`, and additive stationary output-noise PSD `S_n(f)`,

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

With

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

```math
\boxed{
\rho_\infty^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

**DERIVED / CONDITIONAL:** complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

See `MATCHED_FILTER_SNR_STEP.md`.

---

## 4. Step 03 — unknown timing alone versus finite truncation

For stationary Gaussian noise, exact detector knowledge, unlimited observation, and unrestricted matched-filter delay search, identical complete `D*(f)` gives identical full-observation search statistics.

**DERIVED / CONDITIONAL:** unknown arrival time by itself does not break the ideal full-observation equivalence.

A finite fixed record can break the equivalence because magnitude `D*(f)` discards phase/temporal placement.

**Qualification:** a known pure delay can be removed by shifting the record.

See `FINITE_WINDOW_PHASE_STEP.md`.

---

## 5. Step 04 — latency-compensated phase dispersion

A stable causal all-pass factor can preserve `|G(f)|`, complete magnitude `D*(f)`, magnitude bandwidth, and total infinite-time SNR while redistributing signal energy in time.

For the constructed pair,

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can be insufficient for finite-time detection even after arbitrary constant latency compensation.

See `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 6. Step 05 — exact SNR accumulation by deadline

For finite record `[0,T]`, with restricted noise covariance operator `C_T`,

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
}
```

Define

```math
\boxed{
\eta(T)=\rho_T^2/\rho_\infty^2.
}
```

In white noise,

```math
\eta(T)=
\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
```

For the ideal exponential output

```math
s_\tau(t)=S_0e^{-t/\tau}u(t),
```

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`, `tau_A=1 ns` gives `eta_A~1`, whereas `tau_B=1 s` gives `eta_B~2e-6`.

**CONSEQUENCE:** eventual detectability `rho_infinity` and the rate at which it becomes accessible `eta(T)` are distinct.

See `SNR_ACCUMULATION_STEP.md`.

---

## 7. Step 06 — operational detection probability by deadline

For the simple known-time Gaussian binary decision,

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

With equal eventual SNR `rho_infinity=6`, deadline `T=1 us`, and `P_FA=1e-6`, the exponential examples give approximately

```text
fast: P_D ~ 0.89372
slow: P_D ~ 1.043e-6
```

while both have the same eventual detection probability.

See `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 8. Step 07 — independent-slot unknown-arrival search penalty

For `M` independent normalized Gaussian timing hypotheses scanned by their maximum, a global false-alarm probability `alpha` gives

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

The true signal-bearing slot crosses threshold with probability

```math
\boxed{
P_{D,true}
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\gamma_{M,\alpha}
\right].
}
```

For `alpha=1e-6`, increasing from `M=1` to `M=1e6` raises the threshold from about `4.7534` to `7.0345` sigma.

**DERIVED / CONDITIONAL:** unknown timing introduces a search-complexity threshold in addition to SNR accumulation.

See `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 9. Step 08 — continuous-time matched-filter search correlation

Define the noise-whitened template

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}}
```

and normalized SNR spectral weight

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'}.
```

For a stationary full-observation Gaussian matched-filter scan, the normalized noise-only covariance between two candidate arrival times separated by `Delta` is

```math
\boxed{
r(\Delta)
=\int W(f)e^{i2\pi f\Delta}df.
}
```

Using frequency-resolved detectivity,

```math
\boxed{
W(f)=
\frac{|P(f)|^2D^{*2}(f)}
{\int |P(f')|^2D^{*2}(f')df'}.
}
```

Therefore **digital sample count is not the timing trials factor**. Oversampling only evaluates the same correlated process more densely.

For finite second spectral moment, define

```math
\boxed{
f_{\mathrm{rms}}^2
=\int f^2W(f)df
=\frac{
\int f^2|P(f)|^2D^{*2}(f)df
}{
\int |P(f)|^2D^{*2}(f)df
}.
}
```

Then

```math
\boxed{
-r''(0)=(2\pi)^2f_{\mathrm{rms}}^2
}
```

and the natural local curvature correlation scale is

```math
\boxed{
\tau_{\mathrm{curv}}=
\frac{1}{2\pi f_{\mathrm{rms}}}.
}
```

For a differentiable unit-variance Gaussian scan, Rice's formula gives the **exact mean upcrossing rate** of threshold `u`:

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

For monitoring duration `L`,

```math
E[N_u^+]=L f_{\mathrm{rms}}e^{-u^2/2}.
```

At high thresholds, this yields the leading rare-excursion approximation

```math
P_{FA,global}(u)
\approx Q(u)+L f_{\mathrm{rms}}e^{-u^2/2},
```

with endpoint and multiple-excursion corrections required for precision work.

If one forces an independent-trial representation, the corresponding high-threshold

```math
M_{\mathrm{eff}}(u)
\approx
\frac{L f_{\mathrm{rms}}e^{-u^2/2}}{Q(u)}
\sim\sqrt{2\pi}\,uL f_{\mathrm{rms}}
```

is threshold dependent. There is no universal threshold-independent `M_eff`.

### Important refinement of Step 07

For a fixed optical waveform, **identical complete `D*(f)` implies identical `W(f)`, scan covariance, `f_rms`, and full-observation continuous-time search penalty**. Phase-only detector differences do not change the trials factor in this restricted problem.

A faster detector can increase search penalty only insofar as it broadens or changes the frequencies that actually contribute SNR.

### Important regularity warning

The ideal abrupt exponential `S_0 exp(-t/tau)u(t)` used in Steps 05–07 has a divergent SNR-weighted second spectral moment in ideal white noise. Therefore its continuous-time scan is not mean-square differentiable, and the Rice curvature/upcrossing result cannot be applied without physical high-frequency regularization or a smoother waveform.

This does **not** invalidate its finite-energy SNR-accumulation results. It only limits the continuous-time crossing-density calculation.

See `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 10. Current scientific frontier

The surviving structure is now

```text
asymptotic signal/noise separation
    -> rho_infinity

finite-time accessibility of that separation
    -> eta(T)

known-time decision threshold
    -> one Gaussian tail

unknown-time search correlation
    -> full covariance r(Delta)

local continuous timing scale, when differentiable
    -> f_rms or tau_curv = 1/(2 pi f_rms)

high-threshold search excursion density
    -> nu_u^+ = f_rms exp(-u^2/2)
```

The search penalty is therefore controlled by the **SNR-weighted detector-waveform spectrum**, not sample count and not response time alone.

---

## 11. What has been established

- Scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Full-observation known-waveform SNR is `integral |P|^2|G|^2/S_n df`.
- Complete magnitude `D*(f)` is sufficient for that restricted full-observation problem.
- Finite observation can make magnitude `D*(f)` insufficient because phase/temporal dispersion can control SNR accumulation.
- Exact finite-record SNR is `rho_T^2=<s_T,C_T^-1 s_T>`.
- `eta(T)=rho_T^2/rho_infinity^2` separates SNR accumulation from eventual SNR.
- In the simple Gaussian decision problem, `rho_T` maps directly to deadline detection probability.
- Unknown timing raises a global search threshold.
- Continuous-time scan covariance is the autocorrelation of the noise-whitened template.
- When the second moment exists, `f_rms` determines local covariance curvature and Rice upcrossing density.
- Higher sampling rate alone does not increase the continuous-time trials penalty.

---

## 12. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- No universal threshold-independent effective timing-trial count.
- `f_rms` alone does not determine the exact supremum distribution for arbitrary covariance; the full `r(Delta)` can matter.
- No finite-window continuous-scan edge theory yet.
- No repeated/sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationary treatment.
- No novelty claim.

---

## 13. Single natural next question — DO NOT ANSWER YET

> Given the two competing effects now identified — SNR accumulation `eta(T)` and continuous-time search width `f_rms` — can one construct two detectors with equal asymptotic SNR for which the faster detector's larger search penalty actually reverses the finite-time detection ranking, or is rapid SNR accumulation guaranteed to dominate under some broad conditions?
