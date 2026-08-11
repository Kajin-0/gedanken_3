# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 13:01 EDT:** This log is intentionally compact. Every scientific milestone, correction, negative result, stopping point, and timestamp is retained; full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar D* insufficiency

Equal low-frequency/reference `D*` does not guarantee equal temporal-signal SNR. Under the explicit one-pole/additive-output-noise construction, the `1 ns` and `1 s` detectors differ by about `6.36x` in SNR for the same 1 Hz tone.

**Qualification:** signal/noise filtering can cancel; this is not `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int|P(f)|^2D^{*2}(f)df.
}
```

**DERIVED / CONDITIONAL:** complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

Unknown arrival time alone does not break full-observation equivalence when complete `D*(f)` is identical under stationary Gaussian matched filtering.

A finite fixed record can nevertheless make phase/temporal placement matter.

**Qualification:** known pure latency can be compensated.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion

A stable causal all-pass factor preserves magnitude response, complete magnitude `D*(f)`, and total infinite-time SNR while redistributing signal energy in time.

Even after arbitrary constant alignment,

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** finite-window insufficiency of magnitude `D*(f)` survives removal of the pure-delay loophole.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact SNR accumulation

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle,
}
```

```math
\boxed{
\eta(T)=\rho_T^2/\rho_\infty^2.
}
```

For white-noise ideal exponential output,

```math
\eta_\tau(T)=1-e^{-2T/\tau}.
```

At `T=1 us`, the `1 ns` example has `eta~1`; the `1 s` example has `eta~2e-6`.

**CONSEQUENCE:** eventual detectability and the rate at which it becomes accessible are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

For the simple known-time Gaussian test,

```math
\boxed{
P_D(T;\alpha)=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

With equal `rho_infinity=6`, `T=1 us`, and `P_FA=1e-6`, the fast and slow exponential examples give approximately `0.89372` and `1.043e-6`, while sharing the same eventual detection probability.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

For `M` independent timing hypotheses scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes extra SNR margin through the global search threshold.

**Critical warning:** `M` is not the number of digital samples in a real continuous search.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time search correlation

Define the full-observation whitened template and normalized SNR spectrum

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
```

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'}.
```

Then

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

If the second spectral moment exists,

```math
\boxed{
f_{\mathrm{rms}}^2=\int f^2W(f)df,
}
```

and Rice gives exact mean upcrossing density

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

**REFINEMENT:** higher ADC sampling rate alone does not raise the trials factor. For the same waveform, identical complete magnitude `D*(f)` gives identical full-observation scan covariance and search penalty.

**Regularity warning:** the ideal abrupt exponential has divergent second spectral moment in ideal white noise, so Rice curvature analysis requires physical high-frequency regularization or a smoother waveform.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Search-penalty reversal and finite-deadline correction

### Correction before attempting the ranking comparison

The finite-deadline SNR `rho_T` / `eta(T)` from Step 05 and the full-observation `f_rms` from Step 08 do **not** automatically belong to the same scan statistic.

For a true finite-deadline unknown-time scan, the optimal filter is

```math
q_T=C_T^{-1}s_T,
```

and its translated noise-only covariance is

```math
\boxed{
r_T(\Delta)
=\frac{
\int |Q_T(f)|^2S_n(f)e^{i2\pi f\Delta}df
}{
\int |Q_T(f)|^2S_n(f)df
}.
}
```

**REFINEMENT / CORRECTION:** do not combine finite-window `eta(T)` with full-template `f_rms` as an exact finite-deadline detection formula.

Hard truncation can also destroy differentiability at the record boundary, so the Rice curvature formula may not apply directly without regularization.

### Controlled equal-eventual-SNR family

Use the same optical event

```math
p(t)=e^{-bt}u(t)
```

and stable causal detector family

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}.
```

Then

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

With equal white noise and

```math
A_\tau=2\rho_0\sqrt N/\tau^{3/2},
```

every member has identical full-observation SNR `rho_0`.

Its finite-time accumulation is

```math
\boxed{
\eta_\tau(T)
=1-e^{-2x}(1+2x+2x^2),
\qquad x=T/\tau.
}
```

Thus for `tau_f<tau_s`, the faster member has strictly larger finite-time SNR for every finite `T`, but the gap tends to zero as `T->infinity`.

### Exact full-template search-threshold ordering

For this family,

```math
\boxed{
r_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)e^{-|\Delta|/\tau}.
}
```

Hence

```math
z_\tau(t)\overset d=z_1(t/\tau).
```

Searching fixed physical duration `L` means the faster member searches a longer normalized interval `[0,L/tau]`. Therefore its exact full-template global max threshold is strictly higher for ordinary nontrivial false-alarm quantiles.

### Conditional reversal theorem

Let `gamma_{i,T}` be the exact finite-deadline scan threshold and assume the standard convergence

```math
\gamma_{i,T}\to\gamma_i^\infty
```

as the finite-deadline scan approaches the full-template scan.

Then

```text
fast SNR advantage Delta rho_T > 0 but -> 0
fast search-threshold gap Delta gamma_T -> positive constant
```

so for sufficiently large but finite `T`,

```math
\boxed{
0<\Delta\rho_T<\Delta\gamma_T.
}
```

Thus the true-time decision margin satisfies

```math
\boxed{
\rho_{f,T}-\gamma_{f,T}
<
\rho_{s,T}-\gamma_{s,T},
}
```

which implies

```math
\boxed{
P_{D,true,f}<P_{D,true,s}
}
```

**even though**

```math
\boxed{
\rho_{f,T}>\rho_{s,T}.
}
```

**DERIVED / CONDITIONAL:** rapid SNR accumulation is not guaranteed to dominate unknown-time search complexity. A finite-deadline ranking reversal must occur in this controlled family under the stated convergence condition.

This does not contradict Step 03 because the present family has equal integrated asymptotic SNR but different SNR-weighted spectra; it does not have identical complete `D*(f)`.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

### Next question, held open

Is there a compact task-level description — perhaps a detection-time surface in `(P_FA, P_D, L)` rather than a scalar figure of merit — that contains both SNR accumulation and timing-search uncertainty without discarding the detector-response information exposed in Steps 01–09?
