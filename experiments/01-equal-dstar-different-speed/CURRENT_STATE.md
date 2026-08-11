# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 12:02 EDT  
**Status:** three logical steps completed. Step 01 showed that equal reference-condition `D*` does not guarantee equal SNR for arbitrary signals. Step 02 derived the known-waveform matched-filter SNR functional. Step 03 shows that unknown arrival time alone does not break equivalence for identical complete `D*(f)` under ideal full-observation Gaussian conditions, but a fixed finite observation window can because `D*(f)` discards transfer-function phase/latency. No generalized replacement metric or novelty claim.

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

Interpret the given equality as equality at a low-frequency/reference condition. Choose equal area `A`, equal low-frequency responsivity `R0`, equal additive white output-noise density `n0`, and first-order temporal responses

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i}.
```

Then

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A\,R_0}{n_0}.
```

For the same 1 Hz optical tone and the same estimator bandwidth,

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal low-frequency/reference `D*` does not guarantee equal SNR for every optical signal.

Critical qualification: this is an insufficiency result, not `fast is always better`. If dominant noise is filtered by the same pole, signal/noise attenuation can cancel.

---

## 3. Step 02 — known-waveform optimal SNR

For deterministic finite-energy optical waveform `p(t)` with transform `P(f)`, complete LTI optical-to-output transfer `G(f)`, and additive zero-mean stationary output noise with two-sided PSD `S_n(f)`, Cauchy-Schwarz gives

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int_{-\infty}^{\infty}
|P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

For

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

this is

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\frac1A\int_{-\infty}^{\infty}|P(f)|^2D^{*2}(f)df.
}
```

**DERIVED / CONDITIONAL:** with known timing and unlimited observation, detectability is a spectral overlap between the waveform and frequency-resolved signal-to-noise sensitivity.

See `MATCHED_FILTER_SNR_STEP.md`.

---

## 4. Step 03A — unknown arrival time alone

For detector `i`, define the whitened signal template

```math
K_i(f)=\frac{G_i(f)P(f)}{\sqrt{S_{n,i}(f)}}.
```

If

```math
D_A^*(f)=D_B^*(f)
\qquad \forall f,
```

then

```math
|K_A(f)|^2=|K_B(f)|^2
=\frac{|P(f)|^2D^{*2}(f)}{A}.
```

With additive stationary Gaussian noise, unlimited observation, exact detector knowledge, and an unrestricted matched-filter search over arrival time, both the matched-filter mean-versus-delay function and its noise covariance are Fourier transforms of this same `|K(f)|^2`.

Therefore:

> **DERIVED / CONDITIONAL:** unknown arrival time by itself does not break the ideal full-observation detectability equivalence of two detectors with identical complete `D*(f)`.

This is an important negative result. Detector phase cancels from the time-shift autocorrelation used by the ideal matched-filter search.

---

## 5. Step 03B — finite observation window

Now record output only during the externally fixed interval

```math
W=[0,T].
```

Choose

```math
G_A(f)=1,
```

```math
G_B(f)=e^{-i2\pi f\Delta},
```

with identical white output-noise PSD

```math
S_{n,A}(f)=S_{n,B}(f)=N.
```

The two detectors differ only by a pure delay. Since

```math
|G_A(f)|=|G_B(f)|=1,
```

we have

```math
\boxed{
D_A^*(f)=D_B^*(f)=\sqrt{A/N}
\quad \forall f.
}
```

Choose a finite-energy optical pulse `p(t)` supported on `0 <= t <= T_p`, with `T_p<T`.

Then

```math
s_A(t)=p(t),
```

```math
s_B(t)=p(t-\Delta).
```

For white noise, the maximum linear SNR available from only the recorded interval is

```math
\rho_{i,W}^2
=\frac1N\int_0^T|s_i(t)|^2dt.
```

Choose `Delta>T`. Then

```math
\rho_{A,W}^2
=\frac1N\int_0^{T_p}|p(t)|^2dt>0,
```

while

```math
\rho_{B,W}^2=0.
```

Therefore

```math
\boxed{
D_A^*(f)=D_B^*(f)\ \forall f
\not\Rightarrow
\rho_{A,W}=\rho_{B,W}
}
```

for an externally fixed finite observation window.

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can still be insufficient because it discards the phase of `G(f)`. A finite time window can make that phase/latency operationally relevant.

See `FINITE_WINDOW_PHASE_STEP.md`.

---

## 6. Critical qualification

The Step-03 counterexample does not establish that latency is an intrinsic sensitivity loss.

If the measurement window can be shifted separately for each detector to compensate a known pure delay, the specific delay-only pair becomes equivalent again.

Thus the surviving statement is protocol-dependent:

> complete magnitude `D*(f)` is insufficient for a fixed finite-time measurement because temporal phase information discarded by `D*(f)` can determine how much useful signal is actually observed.

---

## 7. What has been established

- **DERIVED:** equal reference scalar `D*` does not determine arbitrary-signal SNR.
- **DERIVED:** in the known-waveform/full-observation LTI stationary-noise problem, maximum linear SNR is `integral |P|^2 |G|^2/S_n df`.
- **DERIVED / CONDITIONAL:** identical complete `D*(f)` remains sufficient for the ideal Gaussian unknown-arrival matched-filter search when observation is unlimited.
- **DERIVED / COUNTEREXAMPLE:** identical complete magnitude `D*(f)` need not imply equal SNR under a fixed finite observation window.
- **DERIVED:** the first missing detector information exposed by time truncation is transfer-function phase/temporal placement, not another scalar bandwidth number.

---

## 8. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No new scalar performance metric.
- No proof that nontrivial phase dispersion matters after ordinary latency is compensated.
- No treatment yet of signal-dependent shot noise, nonlinearities, saturation, dead time, nonstationary noise, or globally optimal non-Gaussian decisions.
- No claim that complex `G(f)` plus noise statistics is sufficient for every possible measurement protocol.
- No novelty claim.

---

## 9. Single natural next question — DO NOT ANSWER YET

> After compensating any known overall latency, can two detectors with identical complete `D*(f)` still have different finite-window detectability because of nontrivial transfer-function phase or temporal dispersion?

This tests whether Step 03 is merely a clock-alignment counterexample or reveals a deeper need for the full complex temporal response.