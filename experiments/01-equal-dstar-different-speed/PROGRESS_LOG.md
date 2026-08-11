# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 12:47 EDT:** This log is intentionally compact. Every scientific milestone, correction, negative result, stopping point, and timestamp is retained; full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar D* insufficiency

Two detectors with equal low-frequency/reference `D*`, equal area, equal low-frequency responsivity, equal additive white output-noise density, and

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}
```

were compared using first-order temporal response. For the same 1 Hz optical tone and estimator bandwidth,

```text
SNR_A/SNR_B ~ 6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for every temporal signal.

**Qualification:** if dominant noise is filtered by the same pole, signal/noise attenuation can cancel. This is not `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform full-observation SNR

For waveform `P(f)`, LTI transfer `G(f)`, and additive stationary noise PSD `S_n(f)`,

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int|P(f)|^2D^{*2}(f)df.
}
```

**DERIVED / CONDITIONAL:** full-observation known-waveform detectability is a spectral overlap between waveform and detector signal-to-noise sensitivity.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

For stationary Gaussian noise, unlimited observation, exact detector knowledge, and unrestricted matched-filter delay search, equal complete `D*(f)` gives equal full-observation search statistics.

**DERIVED / CONDITIONAL:** unknown arrival time alone does not break ideal equivalence.

A finite fixed record can nevertheless distinguish a pure-delay pair with identical complete magnitude `D*(f)`.

**DERIVED / COUNTEREXAMPLE:** finite truncation can make phase/temporal placement operationally relevant.

**Qualification:** compensating known latency removes this specific example.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion survives

A stable causal all-pass phase factor preserves magnitude response, complete magnitude `D*(f)`, and total infinite-time SNR while spreading a compact response into a tail.

Even after arbitrary constant alignment,

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** finite-window insufficiency of magnitude `D*(f)` survives removal of the pure-delay loophole.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation by deadline

For finite record `[0,T]` with restricted covariance `C_T`,

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

In white noise, `eta(T)` is cumulative signal-energy fraction. For the ideal exponential response,

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`, the `1 ns` example has `eta~1` while the `1 s` example has `eta~2e-6`.

**CONSEQUENCE:** eventual detectability `rho_infinity` and rate of access to it `eta(T)` are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

For the simple known-time Gaussian test,

```math
\boxed{
P_D(T;\alpha)=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

With equal `rho_infinity=6`, `T=1 us`, and `P_FA=1e-6`:

```text
fast exponential: P_D ~ 0.89372
slow exponential: P_D ~ 1.043e-6
```

while both approach the same eventual detection probability.

**DERIVED / CONDITIONAL:** equal eventual detectability can coexist with radically unequal deadline detection probability purely because SNR accumulates at different rates.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-arrival search penalty

For `M` independent Gaussian timing hypotheses scanned by their maximum, global false-alarm requirement `alpha` gives

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

For `alpha=1e-6`, `M=1e6` raises the threshold from about `4.7534` to `7.0345` sigma.

**DERIVED / CONDITIONAL:** timing uncertainty introduces a search-complexity threshold in addition to SNR accumulation.

**Open issue:** real continuous-time matched-filter outputs are correlated, so `M` cannot be identified with digital sample count.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time search correlation

### Prompted continuation

Determine the physically meaningful correlation time / effective number of distinct arrival-time trials in a continuous matched-filter search.

### Exact scan covariance

Define the noise-whitened template

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}}
```

and normalized SNR spectral weight

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'}.
```

The stationary normalized noise-only matched-filter scan has covariance

```math
\boxed{
r(\Delta)
=\int W(f)e^{i2\pi f\Delta}df.
}
```

Using `D*(f)`,

```math
\boxed{
W(f)=
\frac{|P(f)|^2D^{*2}(f)}
{\int |P(f')|^2D^{*2}(f')df'}.
}
```

**DERIVED:** sample count is not the trials factor. Oversampling only evaluates the same correlated process more densely.

### Natural local timing scale

If the second spectral moment exists, define

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
-r''(0)=(2\pi)^2f_{\mathrm{rms}}^2,
}
```

so the local curvature correlation scale is

```math
\boxed{
\tau_{\mathrm{curv}}=1/(2\pi f_{\mathrm{rms}}).
}
```

### Exact mean threshold-crossing density

For a differentiable unit-variance stationary Gaussian scan, Rice's formula gives

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

For monitoring duration `L`,

```math
E[N_u^+]=L f_{\mathrm{rms}}e^{-u^2/2}.
```

At high thresholds,

```math
P_{FA,global}(u)
\approx Q(u)+L f_{\mathrm{rms}}e^{-u^2/2}
```

up to endpoint and multiple-excursion corrections.

If one forces an independent-trials representation,

```math
M_{\mathrm{eff}}(u)
\sim\sqrt{2\pi}\,uL f_{\mathrm{rms}}
```

at high threshold, so **no universal threshold-independent effective `M` exists**.

### Refinement of Step 07

For the same optical waveform, identical complete magnitude `D*(f)` gives identical `W(f)`, scan covariance, `f_rms`, and full-observation timing-search penalty. Phase-only detector differences or higher ADC sample rate do not increase the trials factor under these assumptions.

A speed-related search penalty appears only insofar as the detector broadens or changes the frequencies that actually contribute SNR.

### Regularity warning

The ideal abrupt exponential `S_0 exp(-t/tau)u(t)` used earlier has divergent SNR-weighted second spectral moment in ideal white noise. Its finite-energy SNR-accumulation results remain valid, but the differentiable-process Rice formula requires physical high-frequency regularization or a smoother waveform.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

### Next question, held open

Given the competing effects `eta(T)` and `f_rms`, can a faster detector's larger continuous-time search penalty actually reverse the finite-time detection ranking, or does rapid SNR accumulation dominate under broad conditions?
