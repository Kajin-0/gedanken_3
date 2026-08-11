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

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion survives

### Prompted continuation

Test whether the finite-window insufficiency of complete magnitude `D*(f)` survives after removing the trivial pure-delay / clock-alignment mechanism.

### Detector construction

Use a common finite-bandwidth stable causal response

```math
G_0(s)=\frac{b}{s+b}
```

and

```math
G_A(s)=G_0(s),
```

```math
G_B(s)=G_0(s)\frac{s-a}{s+a}.
```

The second factor is a stable causal all-pass, so

```math
|G_A(f)|=|G_B(f)|
```

for all frequency. With equal active area and equal white output-noise PSD `N`,

```math
D_A^*(f)=D_B^*(f)
=\frac{\sqrt A|G_0(f)|}{\sqrt N}
```

for every frequency.

Its group delay is

```math
\tau_g(\omega)=\frac{2a}{a^2+\omega^2},
```

which is frequency dependent and therefore cannot be removed by any constant latency correction.

### Physically regular waveform

Choose

```math
x(t)=\sin^2(\pi t/T)
```

on `0 <= t <= T`, zero otherwise, and choose optical small-signal modulation

```math
p(t)=x(t)+\frac1b\dot x(t).
```

Then detector A outputs exactly `x(t)`. The modulation is finite-energy and can be implemented around a sufficiently large positive optical DC level.

For detector B,

```math
s_B(t)
=x(t)-2a\int_0^t e^{-a(t-u)}x(u)du.
```

For `t>T`,

```math
s_B(t)
=-2ae^{-at}\int_0^T e^{au}x(u)du\ne0.
```

Thus nonlinear all-pass phase spreads the signal into a nonzero exponential tail.

### Infinite-time equality retained

Because the added factor is all-pass,

```math
\int|s_A(t)|^2dt
=\int|s_B(t)|^2dt
=E,
```

with

```math
E=3T/8.
```

So full-observation matched-filter SNR remains exactly equal, consistent with Step 02.

### Finite-time result after arbitrary alignment

Detector A captures all `E` in a window of duration `T`.

For detector B, allow any shifted window `[delta,delta+T]`. Because `s_B` has a nonzero tail extending to arbitrarily late times, no interval of duration `T` contains all its energy. The captured-energy function is continuous and tends to zero for extreme shifts, so its maximum is attained and remains strictly below `E`:

```math
\boxed{
\max_\delta\int_\delta^{\delta+T}|s_B(t)|^2dt<E.
}
```

Therefore with equal white noise,

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

### First new consequence

**DERIVED / COUNTEREXAMPLE:** the finite-window insufficiency of complete magnitude `D*(f)` is not merely a clock-alignment artifact. It survives arbitrary constant latency compensation when the detector transfer phase is genuinely dispersive.

Equal complete `D*(f)`, equal magnitude bandwidth, and equal total infinite-time matched-filter SNR do not imply equal finite-time SNR accumulation.

### Illustrative tail size

For the unshifted `[0,T]` window and `aT=1`, the chosen pulse has

```text
E_tail/E ~= 0.5068
```

outside the window. This numerical value is illustrative only; the strict latency-optimized inequality above is the actual result.

### Scope boundary

No universal scalar phase penalty or replacement metric is claimed. Phase dispersion need not always be harmful for every waveform. Signal-dependent noise, nonlinear response, dead time, saturation, and nonstationarity remain untouched.

### Next question, held open

For a finite observation time, what is the simplest exact quantity that measures how much of a detector's full matched-filter SNR has become available by a deadline `T`?

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation by deadline

### Prompted continuation

Identify the simplest exact quantity measuring how much of a detector's full matched-filter SNR is available from data acquired by time `T`.

### Exact finite-record result

For output

```math
y(t)=s(t)+n(t)
```

restricted to `W_T=[0,T]`, let `C_T` be the restricted additive-noise covariance operator. Maximizing over all linear statistics supported in the record gives

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
}
```

This is the exact finite-record maximum linear SNR. For colored noise, it is important not to replace this blindly by a truncated globally whitened signal; finite restriction and covariance inversion need not commute.

### Normalized accumulation curve

Define

```math
\boxed{
\eta(T)=\frac{\rho_T^2}{\rho_\infty^2}.
}
```

This is the fraction of eventual matched-filter `SNR^2` available by deadline `T`. The SNR-amplitude fraction is `sqrt(eta)`.

For nested windows, `0<=eta<=1` and `eta(T)` is nondecreasing because a longer-record estimator can always ignore later data.

### White-noise limit

For white output-noise covariance `N delta(t-t')`,

```math
\rho_T^2=\frac1N\int_0^T|s(t)|^2dt,
```

so for a causal finite-energy signal

```math
\boxed{
\eta(T)
=\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
}
```

Thus `eta` is exactly cumulative signal-energy fraction in white noise.

### Return to the original time constants

For the minimal exponential output

```math
s_tau(t)=S_0 exp(-t/tau)u(t),
```

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`:

```text
tau_A = 1 ns -> eta_A ~ 1

tau_B = 1 s  -> eta_B ~ 2.0e-6
```

This is a comparison of each detector's fraction of its own eventual `SNR^2`; absolute deadline SNR additionally depends on `rho_infinity`. If eventual SNRs are equalized, the `eta` difference directly controls the finite-deadline SNR difference.

### SNR-acquisition thresholds

For a chosen squared-SNR fraction `q`, define

```math
T_q=inf{T: eta(T)>=q}.
```

For the exponential example,

```math
\boxed{
T_q=-\frac{\tau}{2}\ln(1-q).
}
```

Hence 50%, 90%, 95%, and 99% of eventual `SNR^2` arrive at approximately `0.3466 tau`, `1.1513 tau`, `1.4979 tau`, and `2.3026 tau`, respectively.

### First new consequence

**DERIVED / CONDITIONAL:** finite-time detector performance separates naturally into

```text
total eventual matched-filter detectability -> rho_infinity
rate at which that detectability becomes available -> eta(T)
```

`eta(T)` is a task/protocol-specific accumulation curve, not a universal detector-only replacement for `D*`.

### Stopping point

No probability-of-detection calculation has yet been performed.

### Next question, held open

At fixed false-alarm probability, how does finite-time `rho_T` translate into actual probability of detecting the optical event by deadline `T`, and can detectors with equal asymptotic SNR have sharply different deadline detection probabilities?
