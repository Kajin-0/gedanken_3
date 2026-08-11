# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 12:38 EDT  
**Status:** seven logical steps completed. Step 01 showed scalar reference `D*` is insufficient for arbitrary temporal signals. Step 02 derived known-waveform full-observation matched-filter SNR. Step 03 showed unknown arrival time alone does not break equivalence for identical complete `D*(f)` under ideal Gaussian full-observation conditions, while a finite window can via phase/latency. Step 04 removed the pure-delay loophole using nonlinear all-pass phase. Step 05 identified exact finite-record SNR accumulation. Step 06 mapped accumulated SNR to fixed-false-alarm detection probability by a deadline. Step 07 adds the simplest exact unknown-arrival-time search penalty: searching `M` independent timing hypotheses raises the global false-alarm threshold and partially opposes the benefit of rapid SNR accumulation. No universal replacement metric or novelty claim.

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

**DERIVED / CONDITIONAL:** unknown arrival time alone does not break the ideal full-observation equivalence.

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

For the simple known-time Gaussian binary test on `[0,T]`, the normalized Neyman-Pearson statistic obeys

```math
z_T|H_0\sim\mathcal N(0,1),
```

```math
z_T|H_1\sim\mathcal N(\rho_T,1).
```

For per-decision false-alarm probability `alpha`,

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-\Phi^{-1}(1-\alpha)
\right].
}
```

With equal eventual SNR

```math
\rho_{A,\infty}=\rho_{B,\infty}=6,
```

deadline `T=1 us`, and `P_FA=1e-6`, the exponential examples give

```text
P_D,A ~ 0.89372
P_D,B ~ 1.043e-6
```

while both converge to the same eventual `P_D,infinity ~ 0.89372`.

**DERIVED / CONDITIONAL:** equal eventual detectability can coexist with radically unequal deadline detection probability solely because the SNR-accumulation curves differ.

See `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 8. Step 07 — unknown arrival time and search penalty

Now let the event occupy one of `M` independent candidate arrival slots, and scan the normalized matched-filter outputs

```math
Z_{max}=\max_{1\le k\le M}z_k.
```

Under noise only, the `z_k` are independent `N(0,1)`. Requiring a **global** false-alarm probability `alpha` over the whole timing search gives

```math
1-\Phi(\gamma)^M=\alpha,
```

hence the exact threshold

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

If the event is in slot `j`, the probability that the true signal-bearing slot crosses this globally calibrated threshold is

```math
\boxed{
P_{D,true}
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-\gamma_{M,\alpha}
\right].
}
```

For small `alpha/M`,

```math
\gamma_{M,\alpha}
\approx\Phi^{-1}\!\left(1-\frac{\alpha}{M}\right)
\sim\sqrt{2\ln(M/\alpha)}
```

up to Gaussian-tail logarithmic corrections.

Thus unknown timing raises the required SNR threshold only logarithmically with the number of independent searched times.

### Numerical example

With

```text
alpha = 1e-6
M = 1e6
```

```math
\gamma\approx7.03449,
```

compared with `4.75342` for a known event time.

Retaining `rho_infinity=6`, `tau_A=1 ns`, `tau_B=1 s`, and `T=1 us` gives

```text
rho_A,T ~ 6
rho_B,T ~ 0.0084853
```

and therefore

```text
P_D,true,A ~ 0.15045
P_D,true,B ~ 1.06e-12
```

under the million-slot search.

**DERIVED / CONDITIONAL:** unknown timing introduces a second resource requirement beyond SNR accumulation: the search threshold associated with timing uncertainty.

A faster/narrower response can, in some protocols, resolve more effectively independent arrival-time hypotheses, which raises the search threshold and partially opposes the benefit of rapid SNR accumulation. This effect is not yet quantified for continuous correlated searches.

See `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 9. Current scientific frontier

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

known-time fixed-deadline detection
-> threshold determined by one Gaussian tail

unknown-time independent-slot scan
-> threshold rises to gamma_{M,alpha}=Phi^{-1}[(1-alpha)^(1/M)]
-> detection depends on accumulated SNR minus search threshold
```

The next unresolved issue is the realistic continuous-time search, where nearby matched-filter delays are correlated and the number of effective trials cannot be identified with the digital sample count.

---

## 10. What has been established

- **DERIVED:** equal reference scalar `D*` does not determine arbitrary-signal SNR.
- **DERIVED:** full-observation known-waveform maximum linear SNR is `integral |P|^2|G|^2/S_n df`.
- **DERIVED / CONDITIONAL:** identical complete `D*(f)` remains sufficient for ideal full-observation unknown-arrival Gaussian matched filtering.
- **DERIVED / COUNTEREXAMPLE:** finite observation can make complete magnitude `D*(f)` insufficient, even after latency compensation.
- **DERIVED:** exact finite-record maximum linear SNR is `rho_T^2=<s_T,C_T^{-1}s_T>`.
- **DEFINED:** `eta(T)=rho_T^2/rho_infinity^2` measures the fraction of full matched-filter `SNR^2` accessible by a specified deadline.
- **DERIVED:** in white noise, `eta(T)` is cumulative signal-energy fraction.
- **DERIVED:** for a one-pole exponential output, `eta_tau(T)=1-exp(-2T/tau)`.
- **DERIVED:** for the known-time Gaussian simple-hypothesis problem, `rho_T` determines the ROC.
- **DERIVED:** for `M` independent Gaussian timing hypotheses, the global max-scan threshold is `Phi^{-1}[(1-alpha)^(1/M)]`.
- **DERIVED / EXAMPLE:** at `alpha=1e-6`, increasing from one known timing hypothesis to `10^6` independent hypotheses raises the threshold from about `4.7534` to `7.0345` sigma.
- **CONDITIONAL:** if faster temporal response increases the number of effectively independent timing hypotheses, this introduces an opposing look-elsewhere penalty.

---

## 11. What has not been established

- No universal statement that faster detectors are better.
- No universal speed-detectivity tradeoff.
- No universal scalar replacement for `D*`.
- `eta(T)` is not detector-only; it depends on waveform, noise, timing convention, and observation protocol.
- No exact continuous-time correlated-search threshold.
- No universal formula for effective number of timing trials.
- No globally optimal composite-hypothesis solution for arbitrary arrival-time priors; Step 07 uses the deliberately simplest max-scan rule.
- No repeated-look or sequential-detection result.
- No signal-dependent shot noise, nonlinearities, saturation, dead time, nonstationary noise, or globally optimal non-Gaussian decisions.
- No novelty claim.

---

## 12. Single natural next question — DO NOT ANSWER YET

> In a continuous-time matched-filter search, what determines the correlation time / effective number of statistically distinct arrival-time trials, and how is that quantity related to the detector's noise-whitened temporal response rather than to sampling rate alone?

This is the next logical step because the independent-slot model isolates the search penalty exactly but does not yet tell us how detector temporal response determines the actual trials factor in continuous monitoring.