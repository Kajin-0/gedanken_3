# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 12:38 EDT:** This log is intentionally compact. Every scientific milestone, correction, negative result, stopping point, and timestamp is retained here; full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Initialization and first consequence

Two detectors were assigned equal low-frequency/reference `D*`, equal area, equal low-frequency responsivity, equal additive white output-noise density, but first-order response times

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

For the same 1 Hz optical tone and estimator bandwidth,

```text
SNR_A/SNR_B ~ 6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal reference-condition scalar `D*` does not guarantee equal SNR for every optical signal.

**Qualification:** if dominant noise is filtered by the same temporal pole, signal/noise attenuation can cancel. This is an insufficiency result, not `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform optimal SNR

For finite-energy waveform `P(f)`, LTI transfer `G(f)`, and additive stationary output-noise PSD `S_n(f)`, covariance-weighted Cauchy-Schwarz gives

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

**DERIVED / CONDITIONAL:** known-waveform full-observation detectability is a spectral overlap between waveform and detector signal-to-noise sensitivity.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

For stationary Gaussian noise, unlimited observation, exact detector knowledge, and unrestricted matched-filter delay search, equal complete `D*(f)` gives equal full-observation search statistics.

**DERIVED / CONDITIONAL:** unknown arrival time alone does not break ideal full-observation equivalence.

A pure-delay pair with identical complete `D*(f)` can nevertheless yield unequal finite-window SNR if the fixed record contains one response and not the other.

**DERIVED / COUNTEREXAMPLE:** finite time truncation can make transfer-function phase/temporal placement operationally relevant.

**Qualification:** compensating a known pure delay removes this specific example.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion survives

Use

```math
G_A(s)=\frac{b}{s+b},
```

```math
G_B(s)=\frac{b}{s+b}\frac{s-a}{s+a}.
```

The second factor is stable, causal, and all-pass, so both chains have identical magnitude response, magnitude bandwidth, and—under equal white output noise—identical complete `D*(f)`.

Its frequency-dependent group delay cannot be removed by a constant shift. A compact output pulse in A becomes a response with a nonzero exponential tail in B while total signal energy is preserved.

Therefore

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can remain insufficient for finite-time detection after latency compensation because nonlinear phase redistributes recoverable SNR in time.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation by deadline

For output `y=s+n` restricted to `[0,T]`, with restricted covariance operator `C_T`, maximum finite-record linear SNR is

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

For white output noise,

```math
\eta(T)
=\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
```

For

```math
s_\tau(t)=S_0e^{-t/\tau}u(t),
```

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`, the `1 ns` detector has `eta~1` while the `1 s` detector has `eta~2e-6`.

**CONSEQUENCE:** finite-time performance separates into eventual detectability `rho_infinity` and the rate of access to it `eta(T)`.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

For the simple known-time Gaussian test, normalized statistic

```math
z_T|H_0\sim\mathcal N(0,1),
```

```math
z_T|H_1\sim\mathcal N(\rho_T,1).
```

At per-decision false-alarm probability `alpha`,

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

Normalize both exponential detectors to `rho_infinity=6`. At `T=1 us`, `P_FA=1e-6`:

```text
P_D,A ~ 0.89372
P_D,B ~ 1.043e-6
```

while both approach the same eventual `P_D~0.89372`.

**DERIVED / CONDITIONAL:** equal eventual detectability can coexist with radically unequal deadline detection probability purely because SNR accumulates at different rates.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Unknown-arrival-time search penalty

### Prompted continuation

Determine how searching many possible arrival times changes the false-alarm threshold and whether this alters the value of rapid SNR accumulation.

### Simplest exact search model

Use `M` independent normalized matched-filter timing hypotheses and the max scan

```math
Z_{max}=\max_k z_k.
```

Under noise only, `z_k~N(0,1)` independently. A global false-alarm requirement `alpha` gives

```math
1-\Phi(\gamma)^M=\alpha,
```

so

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

If the signal occupies one slot with finite-time SNR amplitude

```math
\rho_T=\rho_\infty\sqrt{\eta(T)},
```

then the probability that the **true signal slot** crosses the globally calibrated threshold is

```math
\boxed{
P_{D,true}
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\gamma_{M,\alpha}
\right].
}
```

The global test rejection probability is slightly different because unrelated noise crossings in other slots can trigger the max statistic. For weak signals and very small `alpha`, this distinction matters; `P_D,true` is retained as the cleaner event-attributable quantity.

### Numerical result

For

```text
alpha = 1e-6
M = 1e6
```

```text
known-time threshold: 4.75342 sigma
million-slot threshold: 7.03449 sigma
increase: 2.28107 sigma
```

With the prior equal-eventual-SNR normalization `rho_infinity=6` and deadline `T=1 us`:

```text
tau_A = 1 ns -> rho_A,T ~ 6       -> P_D,true ~ 0.15045
tau_B = 1 s  -> rho_B,T ~ 0.00849 -> P_D,true ~ 1.06e-12
```

Thus unknown timing can greatly reduce absolute detection probability even for the fast detector, but the extreme SNR-accumulation advantage remains.

### First new consequence

**DERIVED / CONDITIONAL:** unknown timing introduces a second resource requirement beyond SNR accumulation: a **search-complexity threshold**.

For fixed `M`, rapid SNR accumulation always helps because `P_D,true` is monotone in `rho_T`. However, if a faster/narrower temporal response produces more effectively independent arrival-time hypotheses within a fixed monitoring interval, then it also incurs a larger look-elsewhere threshold. The two effects oppose one another.

For small `alpha/M`,

```math
\gamma_{M,\alpha}
\approx\Phi^{-1}(1-\alpha/M)
\sim\sqrt{2\ln(M/\alpha)}
```

up to Gaussian-tail logarithmic corrections, so the independent-trial penalty grows only logarithmically with trial count.

### Critical scope boundary

Real continuous-time matched-filter outputs at nearby delays are correlated. It is generally wrong to set `M = number of digital samples`. The exact continuous-search threshold depends on the covariance/autocorrelation of the scan process.

The max scan is the deliberately simplest unknown-time rule; it is not claimed to be the globally optimal composite-hypothesis decision rule for every arrival-time prior.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

### Next question, held open

In a continuous-time matched-filter search, what determines the correlation time / effective number of statistically distinct arrival-time trials, and how is that related to the detector's noise-whitened temporal response rather than to sampling rate alone?
