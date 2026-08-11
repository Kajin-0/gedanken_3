# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 12:18 EDT  
**Status:** five logical steps completed. Step 01 showed scalar reference `D*` is insufficient for arbitrary temporal signals. Step 02 derived known-waveform full-observation matched-filter SNR. Step 03 showed unknown arrival time alone does not break equivalence for identical complete `D*(f)` under ideal Gaussian full-observation conditions, while a finite window can via phase/latency. Step 04 removed the pure-delay loophole using nonlinear all-pass phase. Step 05 identifies the exact finite-record SNR accumulation functional and reconnects it to the original `1 ns` versus `1 s` example. No universal replacement metric or novelty claim.

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

The original question is whether equality of conventional specific detectivity alone guarantees equal ability to detect an arbitrary optical signal.

---

## 2. Step 01 — scalar D* is insufficient

Interpret the initial equality as equality at a low-frequency/reference condition. With equal area `A`, equal low-frequency responsivity `R0`, equal additive white output-noise density `n0`, and

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i},
```

one has

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A R_0}{n_0}.
```

For the same 1 Hz optical tone and estimator bandwidth,

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal reference-condition scalar `D*` does not guarantee equal SNR for every optical signal.

Critical qualification: this is not `fast is always better`; if dominant noise is filtered by the same temporal pole, signal/noise attenuation can cancel.

---

## 3. Step 02 — known-waveform full-observation SNR

For deterministic finite-energy optical waveform `p(t)`, LTI transfer `G(f)`, and additive stationary output-noise PSD `S_n(f)`, maximum linear-filter SNR is

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

For frequency-resolved detectivity

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

```math
\boxed{
\rho_\infty^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Thus complete magnitude `D*(f)` is sufficient for this restricted known-waveform, full-observation maximum-linear-SNR problem.

See `MATCHED_FILTER_SNR_STEP.md`.

---

## 4. Step 03 — unknown timing versus finite observation

For stationary Gaussian noise, exact detector knowledge, unlimited observation, and unrestricted matched-filter delay search, identical complete `D*(f)` produces identical matched-filter search statistics.

**DERIVED / CONDITIONAL:** unknown arrival time alone does not break the ideal equivalence.

A pure-delay pair with identical complete `D*(f)` can nevertheless yield unequal SNR in an externally fixed finite record.

**DERIVED / COUNTEREXAMPLE:** finite time truncation can make transfer-function phase/temporal placement operationally relevant.

Critical qualification: compensating a known pure delay removes that specific example.

See `FINITE_WINDOW_PHASE_STEP.md`.

---

## 5. Step 04 — pure-delay loophole removed

Use

```math
G_0(s)=\frac{b}{s+b},
```

```math
G_A(s)=G_0(s),
```

```math
G_B(s)=G_0(s)\frac{s-a}{s+a}.
```

The added factor is stable, causal, and all-pass, so with equal white output noise

```math
D_A^*(f)=D_B^*(f)
\qquad \forall f.
```

Its frequency-dependent group delay cannot be removed by any constant latency shift.

For a compact output pulse in detector A, detector B develops a nonzero exponential tail while preserving total signal energy exactly. Detector A can capture all of its signal energy in a `T`-long window; detector B cannot do so in any `T`-long window, even after arbitrary constant alignment:

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can be insufficient for finite-time detection because nonlinear phase / temporal dispersion controls the temporal distribution of recoverable SNR.

See `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 6. Step 05 — exact SNR accumulation by deadline

Let the detector output be

```math
y(t)=s(t)+n(t)
```

and observe only `W_T=[0,T]`. Let `C_T` be the noise covariance operator restricted to that interval.

For an arbitrary linear finite-record statistic, covariance-weighted Cauchy-Schwarz gives the exact maximum linear SNR available by the deadline:

```math
\boxed{
\rho_T^2
=\langle s_T,C_T^{-1}s_T\rangle.
}
```

Define the dimensionless **SNR-squared availability fraction**

```math
\boxed{
\eta(T)=\frac{\rho_T^2}{\rho_\infty^2}.
}
```

The corresponding fraction of SNR amplitude is `sqrt(eta)`.

For nested records,

```math
0\le\eta(T)\le1,
```

and `eta(T)` is nondecreasing because a longer-record estimator can always ignore the extra data. Under ordinary convergence assumptions, `eta(T)->1` as `T->infinity`.

For white output noise `N`,

```math
\boxed{
\rho_T^2=\frac1N\int_0^T|s(t)|^2dt
}
```

and therefore for a causal finite-energy signal

```math
\boxed{
\eta(T)
=\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
}
```

Important colored-noise qualification: finite-window covariance restriction and infinite-record whitening do not generally commute. The exact object is the restricted covariance inverse `C_T^{-1}`, not necessarily a naively truncated globally whitened waveform.

See `SNR_ACCUMULATION_STEP.md`.

---

## 7. Return to the original 1 ns versus 1 s intuition

For the minimal causal exponential output

```math
s_\tau(t)=S_0e^{-t/\tau}u(t),
```

the amplitude cancels in the normalized accumulation fraction. In white noise,

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`:

```text
tau_A = 1 ns -> eta_A = 1 - exp(-2000) ~ 1

tau_B = 1 s  -> eta_B = 1 - exp(-2e-6) ~ 2.0e-6
```

Thus essentially all of detector A's eventual `SNR^2` is available by `1 us`, whereas only about two parts per million of detector B's eventual `SNR^2` is available.

This compares each detector to its own asymptotic SNR. If the two are additionally normalized to have equal `rho_infinity`, then `eta(T)` directly controls the finite-deadline SNR comparison.

For a chosen accumulation fraction `q`, define

```math
T_q=\inf\{T:\eta(T)\ge q\}.
```

For the exponential example,

```math
\boxed{
T_q=-\frac{\tau}{2}\ln(1-q).
}
```

Examples:

```text
50% SNR^2 -> 0.3466 tau
90% SNR^2 -> 1.1513 tau
95% SNR^2 -> 1.4979 tau
99% SNR^2 -> 2.3026 tau
```

These are task-specific accumulation thresholds, not universal detector constants.

---

## 8. Current scientific frontier

The surviving hierarchy is now

```text
single reference D*
-> insufficient for arbitrary temporal signals

complete magnitude D*(f)
-> sufficient for known-waveform/full-observation maximum linear SNR
-> sufficient for ideal full-observation unknown-arrival Gaussian matched filtering
-> insufficient for finite-window measurements

nonlinear phase / temporal dispersion
-> can change how recoverable SNR is distributed in time even at equal complete D*(f)

finite-record comparison
-> exact available SNR^2 is <s_T,C_T^{-1}s_T>
-> normalized accumulation curve is eta(T)=rho_T^2/rho_infinity^2
```

The thought experiment has therefore separated two quantities that conventional scalar performance summaries can conflate:

```text
total eventual detectability -> rho_infinity
rate of access to that detectability -> eta(T)
```

`eta(T)` is explicitly waveform/noise/protocol dependent and is not claimed as a universal replacement for `D*`.

---

## 9. What has been established

- **DERIVED:** equal reference scalar `D*` does not determine arbitrary-signal SNR.
- **DERIVED:** full-observation known-waveform maximum linear SNR is `integral |P|^2|G|^2/S_n df`.
- **DERIVED / CONDITIONAL:** identical complete `D*(f)` remains sufficient for ideal full-observation unknown-arrival Gaussian matched filtering.
- **DERIVED / COUNTEREXAMPLE:** finite observation can make complete magnitude `D*(f)` insufficient, even after latency compensation.
- **DERIVED:** exact finite-record maximum linear SNR is `rho_T^2=<s_T,C_T^{-1}s_T>`.
- **DEFINED:** `eta(T)=rho_T^2/rho_infinity^2` measures the fraction of full matched-filter `SNR^2` accessible by a specified deadline.
- **DERIVED:** in white noise, `eta(T)` is cumulative signal-energy fraction.
- **DERIVED:** for a one-pole exponential output, `eta_tau(T)=1-exp(-2T/tau)`.

---

## 10. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- `eta(T)` is not detector-only; it depends on waveform, noise, timing convention, and observation protocol.
- No probability-of-detection result yet.
- No signal-dependent shot noise, nonlinearities, saturation, dead time, nonstationary noise, or globally optimal non-Gaussian decisions.
- No novelty claim.

---

## 11. Single natural next question — DO NOT ANSWER YET

> At a fixed false-alarm probability, how does the finite-time SNR `rho_T` translate into actual probability of detecting the optical event by deadline `T`, and can two detectors with equal asymptotic SNR have sharply different deadline detection probabilities?

This is the next logical test because `eta(T)` has quantified SNR accumulation but has not yet connected that accumulation to an operational detection probability.