# Step 03 — Does Complete D*(f) Determine Detectability with Unknown Timing or a Finite Window?

**Date:** 2026-08-11 12:02 EDT  
**Status:** DERIVED under explicit linear/Gaussian assumptions. Unknown arrival time alone does not break the ideal full-observation equivalence; a finite externally fixed observation window does. No generalized metric is proposed.

---

## 1. Question

Assume two detectors have the same active area and exactly the same complete magnitude detectivity function at every frequency,

```math
D_A^*(f)=D_B^*(f)
\qquad \text{for all }f.
```

Can they nevertheless differ in detectability when:

1. the optical event time is unknown; or
2. only a finite time window of detector output is observed?

The purpose is to test whether the complete magnitude function `D*(f)` has discarded detector information that becomes relevant outside the known-time/full-observation matched-filter problem.

---

## 2. Definitions retained from Step 02

For detector `i`, let

```math
G_i(f)
```

be the complex optical-power-to-output transfer function and let

```math
S_{n,i}(f)
```

be the two-sided stationary output-noise PSD.

Define

```math
D_i^*(f)
=\frac{\sqrt A\,|G_i(f)|}{\sqrt{S_{n,i}(f)}}.
```

For an optical waveform `p(t)` with transform `P(f)`, define the whitened signal template

```math
K_i(f)
=\frac{G_i(f)P(f)}{\sqrt{S_{n,i}(f)}}.
```

Then equal complete `D*(f)` implies

```math
|K_A(f)|^2
=|K_B(f)|^2
=\frac{|P(f)|^2D^{*2}(f)}{A}.
```

The two whitened templates may still have different phase.

---

## 3. Unknown arrival time with unlimited observation

Let the optical event arrive at an unknown time `t0`. Its frequency-domain shift is

```math
P(f)\to P(f)e^{-i2\pi f t_0}.
```

Assume additive Gaussian stationary noise and enough observation time to whiten the noise and search over all candidate delays.

For a matched-filter search, the mean response at trial delay `tau` is governed by

```math
R_i(\tau-t_0)
=\int_{-\infty}^{\infty}
|K_i(f)|^2
 e^{i2\pi f(\tau-t_0)}\,df.
```

Under noise alone, the covariance of the matched-filter output at two trial delays is proportional to the same function,

```math
\operatorname{Cov}[z_i(\tau),z_i(\tau')]
\propto
\int |K_i(f)|^2
 e^{i2\pi f(\tau-\tau')}\,df.
```

Because equal complete `D*(f)` gives equal `|K_i(f)|^2`, both detectors have the same matched-filter mean shape and the same Gaussian search-process covariance.

Therefore, within this idealized model,

> **DERIVED / CONDITIONAL:** unknown arrival time by itself does not make two detectors with identical complete `D*(f)` distinguishable in optimal matched-filter detection performance.

The detector phase cancels from the full-observation time-shift autocorrelation.

This statement requires Gaussian stationary noise (or stronger information than a PSD if non-Gaussian false-alarm statistics are to be compared), exact knowledge of each detector transfer function, and unrestricted observation/search time.

---

## 4. Finite observation window: minimal counterexample

Now observe detector output only in the fixed interval

```math
W=[0,T].
```

Choose the simplest pair of LTI detector/readout chains:

```math
G_A(f)=1,
```

```math
G_B(f)=e^{-i2\pi f\Delta}.
```

Detector B differs from detector A only by a pure delay `Delta`.

Let both have the same additive white output-noise PSD

```math
S_{n,A}(f)=S_{n,B}(f)=N.
```

Then

```math
|G_A(f)|=|G_B(f)|=1,
```

so

```math
\boxed{
D_A^*(f)=D_B^*(f)=\sqrt{A/N}
\quad \text{for every } f.
}
```

Thus even the entire magnitude detectivity curve is identical.

Choose a known finite-energy optical pulse `p(t)` supported inside

```math
0\le t\le T_p,
\qquad T_p<T.
```

Then

```math
s_A(t)=p(t),
```

while

```math
s_B(t)=p(t-\Delta).
```

For white noise, the maximum linear SNR available from only the window `W` is

```math
\rho_{i,W}^2
=\frac{1}{N}\int_0^T|s_i(t)|^2dt.
```

Choose

```math
\Delta>T.
```

Then detector A's pulse is fully inside the recorded interval, while detector B's response is entirely outside it:

```math
\rho_{A,W}^2
=\frac{1}{N}\int_0^{T_p}|p(t)|^2dt>0,
```

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

when the observation window is externally fixed.

This is an explicit counterexample.

---

## 5. What information did D*(f) lose?

The complete magnitude detectivity function contains

```math
\frac{|G(f)|^2}{S_n(f)},
```

but not the phase of `G(f)`.

A pure delay changes only phase:

```math
G(f)\to G(f)e^{-i2\pi f\Delta},
```

so it leaves `D*(f)` unchanged.

With unlimited observation, that phase-only delay does not change total matched-filter SNR because all output energy remains available.

With finite observation, time truncation does not commute with arbitrary phase/latency changes. The amount of signal accessible inside the window can therefore differ even when complete `D*(f)` is identical.

Thus the first new information beyond complete magnitude `D*(f)` is not another scalar bandwidth parameter. It is temporal information carried by the complex response, together with the measurement window.

---

## 6. Critical qualification

This counterexample does **not** prove that latency is an intrinsic sensitivity loss.

If each detector's observation window may be shifted to compensate a known pure delay, the two examples become equivalent again.

Therefore the result is specifically:

> **DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` is insufficient for a measurement protocol with an externally fixed finite observation window, because it discards phase/latency information that controls how much signal lies inside that window.

It is a protocol-dependent insufficiency result, not a universal claim that delayed detectors are worse.

---

## 7. What has been established

- **DERIVED / CONDITIONAL:** in stationary Gaussian noise with unlimited observation and an unrestricted matched-filter delay search, unknown arrival time alone does not break equivalence when complete `D*(f)` is identical.
- **DERIVED / COUNTEREXAMPLE:** a finite fixed observation window can break that equivalence even when `D_A^*(f)=D_B^*(f)` for every frequency.
- **DERIVED:** complete magnitude `D*(f)` discards transfer-function phase; finite-time measurement can make that discarded phase operationally relevant.

---

## 8. What has not been established

- No claim that a pure delay is the only or most important missing information.
- No result yet for nonlinear phase/dispersion after trivial latency is compensated.
- No universal finite-window detector metric.
- No treatment of signal-dependent shot noise, saturation, dead time, nonstationary noise, or nonlinear detectors.
- No claim that the complete complex transfer function plus PSD is always sufficient under arbitrary protocols.
- No novelty claim.

---

## 9. Stopping point

The first finite-window consequence is now established and no broader theory should be added yet.

### Single natural next question

> After compensating any known overall latency, can two detectors with identical complete `D*(f)` still have different finite-window detectability because of nontrivial transfer-function phase or temporal dispersion?

This tests whether the finite-window failure is merely a trivial clock-alignment effect or reflects a deeper need for the detector's full complex temporal response.
