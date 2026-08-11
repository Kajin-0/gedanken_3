# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 12:30 EDT:** This log was compacted while preserving every scientific milestone, correction, negative result, stopping point, and timestamp. Full derivations remain in the dedicated step files referenced below. No scientific branch was discarded.

---

## 2026-08-11 11:21 EDT — Initialization and first consequence

### Prompted question

Two photodetectors have equal conventional `D*` but response times `1 ns` and `1 s`. Determine whether equal `D*` guarantees equal ability to detect an arbitrary optical signal, proceeding only one logical step.

### Explicit assumptions

- Treat the quoted equality as low-frequency/reference-condition `D*` equality.
- Equal active area `A`.
- Equal low-frequency responsivity `R0`.
- Equal additive white output-noise density `n0`.
- First-order temporal responses

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i}.
```

- Dominant noise is placed after the detector pole as one physically allowed readout-noise-dominated construction.

Then

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A R_0}{n_0}.
```

For the same 1 Hz optical tone and estimator bandwidth,

```text
A: tau = 1 ns -> |H_A| ~ 1
B: tau = 1 s  -> |H_B| ~ 0.157
SNR_A / SNR_B ~ 6.36
```

### Result

**DERIVED / COUNTEREXAMPLE:** equal reference-condition scalar `D*` does not guarantee equal SNR for every optical signal.

### Adversarial qualification

If dominant noise is filtered by the same pole, signal and noise attenuation can cancel. Therefore the result is **not** `fast is always better`; it is an insufficiency result about a single scalar `D*`.

### Stopping point

No matched-filter or generalized theory yet.

---

## 2026-08-11 11:32 EDT — Known-waveform optimal SNR

### Question

For a specified finite-energy optical waveform and fully specified linear detector/noise spectrum, what is the maximum achievable measurement SNR?

### Result

For waveform `P(f)`, LTI transfer `G(f)`, and additive stationary output noise PSD `S_n(f)`, covariance-weighted Cauchy-Schwarz gives

```math
\boxed{
\rho_\infty^2
=\int_{-\infty}^{\infty}
|P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
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

### Consequence

**DERIVED / CONDITIONAL:** known-waveform full-observation detectability is a spectral overlap between the optical waveform and detector signal-to-noise sensitivity. The detector factor is `|G|^2/S_n`, not response time, bandwidth, responsivity, or noise PSD separately.

### Important cancellation retained

If the same transfer magnitude acts on signal and dominant noise, it can cancel inside `|G|^2/S_n`.

### Scope

Known timing, finite signal energy, LTI response, additive stationary noise, full observation, optimization over linear filters. Gaussianity is not required for maximum linear SNR but is required for the standard optimal Gaussian decision interpretation.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

### Unknown arrival time: negative result

Define the whitened template

```math
K_i(f)=\frac{G_i(f)P(f)}{\sqrt{S_{n,i}(f)}}.
```

Equal complete `D*(f)` implies equal `|K_i(f)|^2`.

For additive stationary Gaussian noise, unlimited observation, exact detector knowledge, and unrestricted matched-filter delay search, the matched-filter mean versus delay and noise covariance depend on the Fourier transform of this same `|K|^2`.

**DERIVED / CONDITIONAL:** unknown arrival time by itself does **not** break ideal detectability equivalence when complete `D*(f)` is identical.

This negative result was preserved deliberately.

### Fixed finite window: counterexample

Use

```math
G_A(f)=1,
\qquad
G_B(f)=e^{-i2\pi f\Delta},
```

with identical white output noise. Then `D_A^*(f)=D_B^*(f)` for every frequency.

A finite fixed observation interval can contain A's pulse while B's delayed pulse falls outside it, yielding

```math
\boxed{
D_A^*(f)=D_B^*(f)\ \forall f
\not\Rightarrow
\rho_{A,W}=\rho_{B,W}.
}
```

### Qualification

A known pure delay can be removed by shifting the observation window, so latency alone is not an intrinsic sensitivity penalty.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion survives

### Question

Does the finite-window failure survive after arbitrary constant latency compensation?

### Construction

Use the common stable causal low-pass

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

The second factor is a stable causal all-pass, so the detectors have identical `|G(f)|`, identical magnitude bandwidth, and, with equal white noise, identical complete `D*(f)`.

Its group delay

```math
\tau_g(\omega)=\frac{2a}{a^2+\omega^2}
```

is frequency dependent and cannot be removed by a constant time shift.

Choose a regular modulation such that A outputs the compact pulse

```math
x(t)=\sin^2(\pi t/T),
\qquad 0\le t\le T.
```

B's output has a nonzero exponential tail for all `t>T`, while the all-pass preserves total signal energy exactly.

Therefore A can capture all its energy in one `T`-long record whereas B cannot do so in **any** `T`-long record, even after arbitrary alignment:

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

### Result

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can remain insufficient for finite-time detection after latency compensation. Nonlinear phase / temporal dispersion can alter when recoverable SNR appears without altering total infinite-time SNR.

For the illustrative unshifted case `aT=1`, about `50.68%` of signal energy lies after the nominal window; the rigorous result is the latency-optimized strict inequality above.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation by deadline

### Question

What exact quantity measures how much of the full matched-filter SNR is available by deadline `T`?

### Exact finite-record result

For output `y=s+n` restricted to `[0,T]`, let `C_T` be the restricted additive-noise covariance operator. Maximization over all linear finite-record statistics gives

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
}
```

Define

```math
\boxed{
\eta(T)=\frac{\rho_T^2}{\rho_\infty^2}.
}
```

`eta(T)` is the fraction of eventual matched-filter **SNR squared** available by deadline `T`; the SNR-amplitude fraction is `sqrt(eta)`.

For white output noise,

```math
\boxed{
\eta(T)=
\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
}
```

For the minimal exponential output

```math
s_\tau(t)=S_0e^{-t/\tau}u(t),
```

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`:

```text
tau_A = 1 ns -> eta_A ~ 1

tau_B = 1 s  -> eta_B ~ 2e-6
```

Thus essentially all of A's eventual `SNR^2` is available, while only about two parts per million of B's is available.

For target accumulation fraction `q`,

```math
T_q=-\frac{\tau}{2}\ln(1-q).
```

Examples:

```text
50% -> 0.3466 tau
90% -> 1.1513 tau
95% -> 1.4979 tau
99% -> 2.3026 tau
```

### Important colored-noise caution

Finite-window restriction and infinite-record whitening need not commute. The exact object is `C_T^{-1}`, not a naively truncated globally whitened waveform.

### Consequence

Finite-time detector performance separates naturally into

```text
total eventual detectability -> rho_infinity
rate at which it becomes available -> eta(T)
```

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

### Question

At fixed false-alarm probability, how does finite-time `rho_T` translate into probability of detecting the event by deadline `T`?

### Minimal decision model

On `[0,T]`, use the simple Gaussian hypotheses

```math
H_0:y_T=n_T,
```

```math
H_1:y_T=s_T+n_T,
```

with known signal waveform/timing/amplitude and the same Gaussian covariance `C_T` under both hypotheses.

The normalized Neyman-Pearson statistic satisfies

```math
z_T|H_0\sim\mathcal N(0,1),
```

```math
z_T|H_1\sim\mathcal N(\rho_T,1).
```

For per-decision false-alarm probability `alpha`,

```math
\gamma_\alpha=\Phi^{-1}(1-\alpha),
```

and

```math
\boxed{
P_D(T;\alpha)=\Phi(\rho_T-\gamma_\alpha).
}
```

Since

```math
\rho_T=\rho_\infty\sqrt{\eta(T)},
```

```math
\boxed{
P_D(T;\alpha)=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

### Equal-asymptotic-SNR example

Normalize both exponential detectors to

```math
\rho_{A,\infty}=\rho_{B,\infty}=6.
```

At `T=1 us`:

```text
rho_A,T ~ 6
rho_B,T ~ 0.0084853
```

For

```math
P_{FA}=10^{-6},
```

the threshold is

```math
\gamma\approx4.753424.
```

Hence

```text
P_D,A(1 us) ~ 0.89372
P_D,B(1 us) ~ 1.043e-6
```

while both detectors converge at infinite observation time to the same

```text
P_D,infinity ~ 0.89372.
```

### First new consequence

**DERIVED / CONDITIONAL:** two detectors with exactly equal eventual matched-filter SNR can have radically different detection probability at the same deadline and false-alarm probability solely because their SNR-accumulation curves differ.

The original speed distinction now has direct decision-theoretic meaning: speed can matter by controlling whether sufficient detectability has arrived before the decision deadline, even when total eventual detectability is unchanged.

### Required accumulation for a target operating point

For desired `P_D=beta`,

```math
\boxed{
\rho_T\ge
\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta).
}
```

Therefore

```math
\boxed{
\eta_{req}=
\left[
\frac{\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta)}
{\rho_\infty}
\right]^2.
}
```

For the exponential accumulation law,

```math
\boxed{
T_{\alpha,\beta}
=-\frac{\tau}{2}\ln(1-\eta_{req})
}
```

when the target is asymptotically feasible.

### Scope boundary

This is one known-time decision at a fixed deadline. It does not yet include unknown signal amplitude/phase, searching over many possible event times, repeated or sequential looks, trials-factor corrections, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

### Next question, held open

If the optical event may occur at an unknown time within a monitoring interval, how does searching over many possible arrival times change the false-alarm threshold and the advantage conferred by rapid SNR accumulation?
