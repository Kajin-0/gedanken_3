# Step 04 — Latency-Compensated Phase Dispersion

**Date:** 2026-08-11 12:09 EDT  
**Status:** DERIVED / COUNTEREXAMPLE under explicit LTI, additive-white-noise, finite-window assumptions. A known pure delay is no longer the mechanism: nonlinear all-pass phase alone can change finite-window detectability while the complete magnitude `D*(f)` remains identical.

---

## 1. Question

After compensating any known overall latency, can two detectors with identical complete magnitude detectivity

```math
D_A^*(f)=D_B^*(f)
\qquad \forall f
```

still have different finite-window detectability because of nontrivial transfer-function phase / temporal dispersion?

The purpose is to determine whether Step 03 was only a clock-alignment artifact.

---

## 2. Finite-bandwidth detector pair with identical D*(f)

Use a common stable causal low-pass optical-to-output response

```math
G_0(s)=\frac{b}{s+b},
\qquad b>0.
```

Detector A is

```math
G_A(s)=G_0(s).
```

Detector B has the same magnitude response followed by the stable causal first-order all-pass factor

```math
A_{ap}(s)=\frac{s-a}{s+a},
\qquad a>0,
```

so

```math
G_B(s)=G_0(s)A_{ap}(s).
```

On the frequency axis `s=i2 pi f`,

```math
|A_{ap}(i2\pi f)|=1.
```

Therefore

```math
|G_A(f)|=|G_B(f)|
\qquad \forall f.
```

Let both detectors have the same additive white output-noise PSD `N` and the same active area `A`. Then

```math
\boxed{
D_A^*(f)=D_B^*(f)
=\frac{\sqrt A\,|G_0(f)|}{\sqrt N}
\qquad \forall f.
}
```

Thus they have the same complete magnitude detectivity curve and the same magnitude bandwidth.

---

## 3. This is not a pure delay

The all-pass phase may be written

```math
\phi_{ap}(\omega)
=\pi-2\arctan(\omega/a)
```

(up to an irrelevant `2 pi` branch), with group delay

```math
\boxed{
\tau_g(\omega)
=-\frac{d\phi_{ap}}{d\omega}
=\frac{2a}{a^2+\omega^2}.
}
```

The group delay is frequency dependent.

Multiplying by any compensating pure shift `exp(+i omega Delta)` can remove only a constant delay. It cannot make this nonlinear phase flat.

So this pair contains genuine temporal dispersion after any ordinary latency alignment.

---

## 4. Choose a physically regular finite-energy optical modulation

Let the desired output of the common path be the smooth compact pulse

```math
x(t)=
\begin{cases}
\sin^2(\pi t/T), & 0\le t\le T,\\
0, & \text{otherwise}.
\end{cases}
```

Because `x(0)=x(T)=0` and `x'(0)=x'(T)=0`, choose the small-signal optical modulation

```math
p(t)=x(t)+\frac{1}{b}\frac{dx}{dt}.
```

For the common first-order path `G_0`, this gives exactly

```math
(G_0*p)(t)=x(t).
```

The modulation is finite-energy and compactly supported. If `p(t)` takes negative small-signal values, realize it physically as a modulation about a sufficiently large positive optical DC level.

Hence

```math
s_A(t)=x(t).
```

---

## 5. Detector B redistributes the same total energy in time

The all-pass impulse response is

```math
h_{ap}(t)=\delta(t)-2a e^{-at}u(t).
```

Therefore

```math
s_B(t)
=x(t)-2a\int_0^t e^{-a(t-u)}x(u)\,du.
```

For `t>T`, the compact input term is zero and

```math
\boxed{
s_B(t)
=-2a e^{-at}
\int_0^T e^{au}x(u)\,du.
}
```

Because `x(u)>=0` and is not identically zero,

```math
\int_0^T e^{au}x(u)\,du>0.
```

Thus detector B has a strictly nonzero exponential tail for every `t>T`.

Yet the all-pass factor preserves total signal energy:

```math
\boxed{
\int_{-\infty}^{\infty}|s_B(t)|^2dt
=\int_{-\infty}^{\infty}|s_A(t)|^2dt
=E.
}
```

For the chosen pulse,

```math
E=\int_0^T\sin^4(\pi t/T)dt
=\frac{3T}{8}.
```

So infinite-time matched-filter SNR remains identical, exactly as Step 02 predicts.

---

## 6. Finite window after arbitrary latency compensation

Give each detector an observation interval of the same duration `T`.

Detector A can align its window to `[0,T]`, capturing all of its signal energy:

```math
\rho_{A,T}^2=\frac{E}{N}.
```

For detector B, allow an arbitrary constant shift `delta` before placing the same-duration window:

```math
W_\delta=[\delta,\delta+T].
```

This is more generous than merely subtracting a specified latency; it optimizes over every possible constant time alignment.

Then

```math
\rho_{B,T}^2(\delta)
=\frac1N\int_\delta^{\delta+T}|s_B(t)|^2dt.
```

But `s_B(t)` has nonzero support extending to arbitrarily large positive times. No finite interval of duration `T` can contain its full energy.

Moreover, the captured-energy function is continuous in `delta` and tends to zero as the window is moved to very early or very late times, so its maximum is attained at a finite shift. Since every finite `T`-interval omits nonzero signal energy,

```math
\boxed{
\max_\delta
\int_\delta^{\delta+T}|s_B(t)|^2dt
<E.
}
```

Therefore

```math
\boxed{
\max_\delta\rho_{B,T}^2
<\rho_{A,T}^2.
}
```

This survives arbitrary constant latency compensation.

---

## 7. Explicit tail size for the unshifted window

For the natural window `[0,T]`, define

```math
C=\int_0^T e^{au}x(u)du.
```

The inaccessible tail energy after `T` is

```math
\boxed{
E_{tail}
=2a C^2 e^{-2aT}>0.
}
```

For the chosen `sin^2` pulse,

```math
C
=
\frac{2\pi^2T\,(e^{aT}-1)}
{(aT)[(aT)^2+4\pi^2]}.
```

For the illustrative choice `aT=1`,

```text
E_tail / E ~= 0.5068
```

for the unshifted `[0,T]` window. This number is illustrative only; the rigorous result above allows detector B to optimize its constant time shift and still proves strict inequality.

---

## 8. First nontrivial consequence

**DERIVED / COUNTEREXAMPLE:** the finite-window failure of complete magnitude `D*(f)` is not merely a pure-delay / clock-alignment artifact.

Two stable causal finite-bandwidth detector chains can have:

```text
identical active area
identical output-noise PSD
identical |G(f)| at every frequency
identical complete D*(f)
identical magnitude bandwidth
identical infinite-time matched-filter SNR
```

and still have different best achievable SNR in an equal-duration finite observation window, even after optimizing over an arbitrary constant latency shift.

The difference is caused by nonlinear transfer-function phase / temporal energy dispersion.

---

## 9. Critical qualification

This does not prove that phase dispersion is always harmful, nor that the displayed all-pass factor models a specific photocarrier mechanism.

It proves only insufficiency of magnitude-only `D*(f)` for finite-time protocols.

A different phase response could concentrate rather than spread energy for a particular waveform. Performance remains joint between detector response, noise, waveform, and observation protocol.

No universal scalar phase penalty is established.

---

## 10. What has been established

- **DERIVED:** equal complete magnitude `D*(f)` does not determine finite-window detectability in general.
- **DERIVED:** this remains true after arbitrary constant latency compensation.
- **DERIVED:** nonlinear phase / group-delay dispersion is sufficient to create the difference while preserving total infinite-time signal energy.
- **DERIVED:** the full complex temporal response contains operational information that magnitude `D*(f)` discards.

---

## 11. What has not been established

- No universal scalar replacement for `D*`.
- No claim that phase dispersion is always detrimental.
- No claim that full complex `G(f)` plus PSD is sufficient under every measurement protocol.
- No treatment of signal-dependent shot noise, saturation, nonlinear response, dead time, nonstationary noise, or non-Gaussian decision theory.
- No novelty claim.

---

## 12. Stopping point

The pure-delay objection has been removed. Do not generalize further in this file.

### Single natural next question

> For a finite observation time, what is the simplest exact quantity that measures how much of a detector's full matched-filter SNR has become available by a deadline `T`?

This returns directly to the original fast-versus-slow detector intuition without presupposing a new universal figure of merit.