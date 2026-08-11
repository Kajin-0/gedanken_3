# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 12:30 EDT  
**Status:** six logical steps completed. Step 01 showed scalar reference `D*` is insufficient for arbitrary temporal signals. Step 02 derived known-waveform full-observation matched-filter SNR. Step 03 showed unknown arrival time alone does not break equivalence for identical complete `D*(f)` under ideal Gaussian full-observation conditions, while a finite window can via phase/latency. Step 04 removed the pure-delay loophole using nonlinear all-pass phase. Step 05 identified exact finite-record SNR accumulation. Step 06 maps that accumulated SNR to operational fixed-false-alarm detection probability by a deadline. No universal replacement metric or novelty claim.

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

For output `y=s+n` observed only on `[0,T]`, let `C_T` be the additive-noise covariance operator restricted to that record.

The exact maximum linear SNR available by the deadline is

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

`eta(T)` is the fraction of eventual matched-filter **SNR squared** accessible by deadline `T`; the SNR-amplitude fraction is `sqrt(eta)`.

For white output noise `N`,

```math
\boxed{
\eta(T)
=\frac{\int_0^T|s(t)|^2dt}
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

Thus essentially all of A's eventual `SNR^2` is available by `1 us`, while only about two parts per million of B's is available.

Important colored-noise qualification: finite-window covariance restriction and infinite-record whitening do not generally commute. The exact object is `C_T^{-1}`.

See `SNR_ACCUMULATION_STEP.md`.

---

## 7. Step 06 — detection probability by deadline

Now impose the simple Gaussian binary test on `[0,T]`:

```math
H_0:y_T=n_T,
```

```math
H_1:y_T=s_T+n_T,
```

with the same Gaussian covariance `C_T` under both hypotheses and known signal timing/waveform/amplitude.

The Neyman-Pearson statistic can be normalized so that

```math
z_T|H_0\sim\mathcal N(0,1),
```

```math
z_T|H_1\sim\mathcal N(\rho_T,1).
```

For per-decision false-alarm probability

```math
P_{FA}=\alpha,
```

the threshold is

```math
\gamma_\alpha=\Phi^{-1}(1-\alpha),
```

and the detection probability is

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left(\rho_T-\gamma_\alpha\right).
}
```

Using

```math
\rho_T=\rho_\infty\sqrt{\eta(T)},
```

this becomes

```math
\boxed{
P_D(T;\alpha)
=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-\Phi^{-1}(1-\alpha)
\right].
}
```

This gives a direct operational meaning to the Step-05 separation:

```text
rho_infinity -> eventual decision-distribution separation
eta(T)       -> fraction of squared separation available by deadline
```

### Explicit equal-asymptotic-SNR example

Normalize the fast and slow exponential examples to

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

```math
\gamma_\alpha\approx4.753424.
```

Therefore

```text
P_D,A(1 us) ~ 0.89372
P_D,B(1 us) ~ 1.043e-6
```

while both converge as `T->infinity` to the same eventual

```text
P_D,infinity ~ 0.89372.
```

**DERIVED / CONDITIONAL:** equal eventual detectability can coexist with radically unequal deadline detection probability purely because the SNR accumulation curves differ.

For target detection probability `beta`, the required finite-time SNR is

```math
\boxed{
\rho_T\ge\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta).
}
```

Thus the required accumulation fraction is

```math
\boxed{
\eta_{req}
=
\left[
\frac{\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta)}
{\rho_\infty}
\right]^2,
}
```

and for the exponential model the earliest deadline is

```math
\boxed{
T_{\alpha,\beta}
=-\frac{\tau}{2}\ln(1-\eta_{req})
}
```

when the requested operating point is asymptotically feasible.

See `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

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

fixed-deadline Gaussian detection
-> P_D(T;alpha)=Phi[rho_infinity sqrt(eta(T))-Phi^{-1}(1-alpha)]
```

The original `1 ns` versus `1 s` intuition now has a precise operational interpretation: a detector can possess the same eventual matched-filter detectability but fail a short decision deadline because insufficient SNR has accumulated.

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
- **DERIVED:** for the stated Gaussian simple-hypothesis problem, `rho_T` determines the ROC and therefore the operational deadline probability of detection.
- **DERIVED / EXAMPLE:** two detectors with equal `rho_infinity=6` can have `P_D~0.894` versus `P_D~1e-6` at the same `1 us` deadline and `P_FA=1e-6`.

---

## 10. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- `eta(T)` is not detector-only; it depends on waveform, noise, timing convention, and observation protocol.
- No unknown-time finite-monitoring search threshold yet.
- No repeated-look or sequential-detection result.
- No signal-dependent shot noise, nonlinearities, saturation, dead time, nonstationary noise, or globally optimal non-Gaussian decisions.
- No novelty claim.

---

## 11. Single natural next question — DO NOT ANSWER YET

> If the optical event may occur at an unknown time within a monitoring interval, how does the requirement to search over many possible arrival times change the false-alarm threshold and the advantage conferred by rapid SNR accumulation?

This is the next logical step because Step 06 used one known-time decision and therefore did not include the trials factor / search-statistic threshold created by unknown event time.