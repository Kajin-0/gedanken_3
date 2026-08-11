# Progress Log — Experiment 01

## 2026-08-11 11:21 EDT — Initialization and first consequence

### Prompted question

Two photodetectors have equal conventional `D*` but response times `1 ns` and `1 s`. Determine whether equal `D*` guarantees equal ability to detect an arbitrary optical signal, proceeding only one logical step.

### Important assumptions made explicit

- The initial `D*` equality is interpreted as equality at a low-frequency/reference condition; a bare `D*` without conditions is incomplete.
- Both detectors are linear and first-order in temporal response.
- Equal active area `A`.
- Equal low-frequency responsivity `R0`.
- Equal additive white output-noise density `n0`.
- The dominant noise is placed after the detector pole; this is a physically consistent readout-noise-dominated counterexample, not a universal model.
- The comparison signal is a sinusoidal optical-power component measured with identical equivalent noise bandwidth `B`.

### Derivation

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i},
```

```math
D_0^*=\frac{\sqrt A R_0}{n_0},
```

```math
\mathrm{SNR}_i
=\frac{P_mD_0^*}{\sqrt{AB}}|H_i(f_m)|.
```

At `f_m=1 Hz`:

```text
A: tau = 1 ns -> |H_A| ~ 1
B: tau = 1 s  -> |H_B| ~ 0.157
SNR_A / SNR_B ~ 6.36
```

### First nontrivial consequence

**DERIVED / COUNTEREXAMPLE:** equal reference-condition `D*` does not guarantee equal SNR for every optical waveform.

### Adversarial check

If the dominant noise is filtered by the same detector pole, signal and noise attenuation can cancel. Likewise, equal `D*(f_m)` specified at the actual measurement frequency implies equal narrowband tone SNR under equal area, incident tone amplitude, and estimator bandwidth.

Therefore the correct conclusion is **not** `fast is always better`; it is that a scalar `D*` at one reference condition is insufficient to determine arbitrary-signal performance.

### Stopping point

No pulse analysis, matched filtering, generalized metric, or speed-detectivity theory has been pursued.

### Next question, held open

For a specified optical waveform and fully specified linear detector transfer/noise spectrum, what determines maximum achievable SNR?

---

## 2026-08-11 11:32 EDT — Known-waveform optimal SNR

### Prompted continuation

Proceed to the single next question from Step 01: for a specified optical waveform and a fully specified linear detector with signal transfer and noise PSD, determine the maximum achievable measurement SNR.

### Minimal model

Use a deterministic finite-energy optical waveform `p(t)` with transform `P(f)`, an LTI optical-to-output transfer `G(f)`, and additive zero-mean wide-sense-stationary output noise with two-sided PSD `S_n(f)`.

The output signal spectrum is

```math
S(f)=G(f)P(f).
```

For an arbitrary linear measurement filter `Q(f)`,

```math
\mathrm{SNR}_Q^2
=\frac{
\left|\int Q^*(f)S(f)df\right|^2
}{
\int |Q(f)|^2S_n(f)df
}.
```

### Derivation

Cauchy-Schwarz with noise whitening gives

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int_{-\infty}^{\infty}\frac{|S(f)|^2}{S_n(f)}df
}
```

and

```math
\boxed{
Q_{\mathrm{opt}}(f)\propto\frac{S(f)}{S_n(f)}.
}
```

Therefore

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

Using

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

this becomes

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

All displayed integrals use the two-sided PSD convention.

### First nontrivial consequence

**DERIVED / CONDITIONAL:** in the known-waveform, LTI, additive-stationary-noise limit, maximum linear-filter SNR is a spectral overlap integral between the optical waveform and the detector's frequency-resolved signal-to-noise sensitivity.

The detector factor is

```math
|G(f)|^2/S_n(f),
```

not bandwidth, response time, responsivity, or noise PSD separately.

A single scalar `D*` is therefore only local information. The complete frequency dependence enters for broadband signals.

### Important cancellation retained

If the same transfer magnitude filters signal and dominant noise, it can cancel in `|G|^2/S_n`. If dominant additive noise enters after the signal pole, it does not. The formalism therefore contains the Step-01 counterexample and its cancellation case without contradiction.

### Scope boundary

This is only a maximum over linear filters with known timing, finite signal energy, full observation/delay freedom, LTI response, and additive stationary noise. Gaussianity is unnecessary for the maximum-linear-SNR result, but is required for the stronger standard known-signal Gaussian detection interpretation.

### Stopping point

No finite-window, unknown-arrival-time, nonlinear, signal-dependent-noise, or nonstationary analysis has been performed.

### Next question, held open

If two detectors have the same complete magnitude function `D*(f)` at every frequency, can they nevertheless differ in detectability once the optical event has an unknown arrival time or the observation window is finite?

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

### Prompted continuation

Test whether two detectors with identical complete magnitude `D*(f)` can nevertheless differ when arrival time is unknown or only a finite output window is recorded.

### Unknown arrival time: negative result

Define the whitened signal template

```math
K_i(f)=\frac{G_i(f)P(f)}{\sqrt{S_{n,i}(f)}}.
```

Equal complete `D*(f)` implies

```math
|K_A(f)|^2=|K_B(f)|^2
=\frac{|P(f)|^2D^{*2}(f)}{A}.
```

For additive stationary Gaussian noise, unlimited observation, exact detector knowledge, and an unrestricted matched-filter search over delay, both the matched-filter mean as a function of trial delay and the covariance of the noise-only search process are determined by the Fourier transform of `|K_i(f)|^2`.

Therefore:

**DERIVED / CONDITIONAL:** unknown arrival time by itself does not break the ideal detectability equivalence when complete `D*(f)` is identical.

This was not assumed in advance; it is a genuine negative result.

### Finite fixed window: counterexample

Use

```math
G_A(f)=1,
```

```math
G_B(f)=e^{-i2\pi f\Delta},
```

with identical white output-noise PSD `N`.

Then

```math
D_A^*(f)=D_B^*(f)=\sqrt{A/N}
```

for every frequency because the second detector differs only by phase (pure delay).

Record only

```math
W=[0,T].
```

Choose a finite-energy optical pulse supported on `0 <= t <= T_p<T`. Then

```math
s_A(t)=p(t),
```

```math
s_B(t)=p(t-\Delta).
```

For white noise, the maximum linear SNR available from the recorded interval is

```math
\rho_{i,W}^2=\frac1N\int_0^T|s_i(t)|^2dt.
```

If `Delta>T`, detector A's pulse is inside the window while detector B's is outside:

```math
\rho_{A,W}^2>0,
\qquad
\rho_{B,W}^2=0.
```

Hence

```math
\boxed{
D_A^*(f)=D_B^*(f)\ \forall f
\not\Rightarrow
\rho_{A,W}=\rho_{B,W}.
}
```

### First new consequence

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can be insufficient under a fixed finite measurement window because it discards transfer-function phase/latency, which controls where the signal falls in time.

### Critical qualification

This does not make latency an intrinsic sensitivity loss. If the observation window can be shifted to compensate a known pure delay, this specific counterexample disappears.

### Stopping point

No nontrivial all-pass dispersion or latency-compensated phase comparison has been performed.

### Next question, held open

After compensating any known overall latency, can two detectors with identical complete `D*(f)` still have different finite-window detectability because of nontrivial transfer-function phase or temporal dispersion?
