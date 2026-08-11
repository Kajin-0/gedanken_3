# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 12:09 EDT  
**Status:** four logical steps completed. Step 01 showed scalar reference `D*` is insufficient for arbitrary temporal signals. Step 02 derived known-waveform full-observation matched-filter SNR. Step 03 showed unknown arrival time alone does not break equivalence for identical complete `D*(f)` under ideal Gaussian full-observation conditions, while a fixed finite window can via phase/latency. Step 04 removes the pure-delay loophole: nonlinear all-pass phase can change finite-window SNR even after arbitrary constant latency compensation, despite identical complete magnitude `D*(f)`. No generalized replacement metric or novelty claim.

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

For deterministic finite-energy optical waveform `p(t)`, LTI transfer `G(f)`, and additive stationary output noise PSD `S_n(f)`, maximum linear-filter SNR is

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

For frequency-resolved detectivity

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Thus complete magnitude `D*(f)` is sufficient for this restricted known-waveform, full-observation maximum-linear-SNR problem.

See `MATCHED_FILTER_SNR_STEP.md`.

---

## 4. Step 03 — unknown timing versus a finite fixed window

If two detectors have identical complete `D*(f)`, their whitened templates have identical magnitude.

With stationary Gaussian noise, exact detector knowledge, unlimited observation, and unrestricted matched-filter delay search:

> **DERIVED / CONDITIONAL:** unknown arrival time alone does not break detectability equivalence.

A pure-delay pair

```math
G_A(f)=1,
\qquad
G_B(f)=e^{-i2\pi f\Delta}
```

with equal white output noise has identical `D*(f)` for all `f`, yet a fixed observation window can include A's pulse and exclude B's delayed pulse.

Therefore:

> **DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can be insufficient under finite time truncation because it discards transfer-function phase/temporal placement.

Critical qualification: compensating a known pure delay removes this specific example.

See `FINITE_WINDOW_PHASE_STEP.md`.

---

## 5. Step 04 — pure-delay loophole removed

Use a common finite-bandwidth stable causal response

```math
G_0(s)=\frac{b}{s+b}
```

and define

```math
G_A(s)=G_0(s),
```

```math
G_B(s)=G_0(s)\frac{s-a}{s+a},
\qquad a>0.
```

The second factor is a stable causal all-pass:

```math
\left|\frac{i\omega-a}{i\omega+a}\right|=1.
```

With equal white output-noise PSD `N`,

```math
\boxed{
D_A^*(f)=D_B^*(f)
=\frac{\sqrt A|G_0(f)|}{\sqrt N}
\qquad \forall f.
}
```

The all-pass group delay is

```math
\boxed{
\tau_g(\omega)=\frac{2a}{a^2+\omega^2},
}
```

which is frequency dependent. No constant latency shift removes it.

Choose a physically regular small-signal optical modulation so detector A outputs the compact pulse

```math
x(t)=\sin^2(\pi t/T),
\qquad 0\le t\le T,
```

and zero otherwise. One explicit choice is

```math
p(t)=x(t)+\frac1b\dot x(t),
```

implemented around a positive optical DC level if necessary.

Then

```math
s_A(t)=x(t),
```

while detector B has

```math
s_B(t)
=x(t)-2a\int_0^t e^{-a(t-u)}x(u)du.
```

For `t>T`,

```math
\boxed{
s_B(t)
=-2ae^{-at}\int_0^T e^{au}x(u)du\ne0.
}
```

Thus the all-pass redistributes signal energy into an infinite causal tail while preserving total energy exactly:

```math
\int|s_A(t)|^2dt
=\int|s_B(t)|^2dt
=E,
```

with

```math
E=\frac{3T}{8}.
```

Detector A can capture all `E` in one `T`-long window. For detector B, even allowing an arbitrary constant shift `delta`, every interval `[delta,delta+T]` omits nonzero energy. The captured-energy function is continuous and vanishes for sufficiently early/late shifts, so its maximum is attained and is strictly less than `E`:

```math
\boxed{
\max_\delta\int_\delta^{\delta+T}|s_B(t)|^2dt<E.
}
```

For equal white noise,

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

Therefore:

> **DERIVED / COUNTEREXAMPLE:** identical complete magnitude `D*(f)` can still correspond to unequal finite-window detectability after arbitrary constant latency compensation. Nonlinear phase / temporal dispersion is sufficient.

See `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 6. Current scientific frontier

The surviving hierarchy is now

```text
single reference D*
-> insufficient for arbitrary temporal signals

complete magnitude D*(f)
-> sufficient for known-waveform/full-observation maximum linear SNR
-> sufficient for ideal unknown-arrival matched-filter search in stationary Gaussian noise
-> insufficient for finite-window measurements

pure delay
-> one finite-window failure mechanism, but removable by alignment

nonlinear all-pass phase / temporal dispersion
-> finite-window failure survives arbitrary constant latency compensation
```

The detector information discarded by magnitude `D*(f)` can therefore be operationally relevant even after trivial timing alignment.

---

## 7. What has been established

- **DERIVED:** equal reference scalar `D*` does not determine arbitrary-signal SNR.
- **DERIVED:** full-observation known-waveform maximum linear SNR is `integral |P|^2|G|^2/S_n df`.
- **DERIVED / CONDITIONAL:** identical complete `D*(f)` remains sufficient for ideal full-observation unknown-arrival Gaussian matched-filter search.
- **DERIVED / COUNTEREXAMPLE:** finite time truncation can make magnitude `D*(f)` insufficient.
- **DERIVED / COUNTEREXAMPLE:** this failure survives arbitrary constant latency compensation when transfer-function phase is dispersive.
- **DERIVED:** equal magnitude bandwidth and equal total infinite-time signal energy do not imply equal finite-time SNR accumulation.

---

## 8. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No new scalar performance metric.
- No claim that phase dispersion is always detrimental.
- No proof that full complex `G(f)` plus noise statistics is sufficient for every protocol.
- No treatment of signal-dependent shot noise, nonlinearities, saturation, dead time, nonstationary noise, or globally optimal non-Gaussian decisions.
- No novelty claim.

---

## 9. Single natural next question — DO NOT ANSWER YET

> For a finite observation time, what is the simplest exact quantity that measures how much of a detector's full matched-filter SNR has become available by a deadline `T`?

This returns directly to the original fast-versus-slow detector intuition without presupposing a universal new metric.