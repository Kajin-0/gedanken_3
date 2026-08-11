# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 13:39 EDT:** This log is intentionally compact but preserves every scientific milestone, correction, negative result, rejected shortcut, and stopping point. Full derivations live in the dedicated step files.

---

## 2026-08-11 11:21 EDT — Scalar D* insufficiency

Started from equal reference `D*` with `tau_A=1 ns`, `tau_B=1 s`. A physically allowed first-order + additive-output-noise construction gave `SNR_A/SNR_B ~ 6.36` for the same 1 Hz tone.

**DERIVED / COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**QUALIFICATION:** if dominant noise is filtered by the same pole, signal/noise attenuation can cancel. The result is not `fast is always better`.

---

## 2026-08-11 11:32 EDT — Known-waveform full-observation SNR

Derived

```math
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

**DERIVED / CONDITIONAL:** full-observation known-waveform detectability is a spectral overlap between waveform and detector signal-to-noise sensitivity.

Full derivation: `MATCHED_FILTER_SNR_STEP.md`.

---

## 2026-08-11 12:02 EDT — Unknown timing versus finite observation

**NEGATIVE RESULT:** under stationary Gaussian full observation, equal complete `D*(f)` gives equal ideal unknown-arrival matched-filter search statistics; unknown timing alone does not break the equivalence.

A finite fixed record can nevertheless distinguish a pure-delay pair with identical complete magnitude `D*(f)` because phase/temporal placement is discarded.

**QUALIFICATION:** compensating known latency removes the pure-delay example.

Full derivation: `FINITE_WINDOW_PHASE_STEP.md`.

---

## 2026-08-11 12:09 EDT — Latency-compensated dispersion

A stable causal all-pass phase factor preserved complete magnitude `D*(f)` and total infinite-time SNR while spreading a compact response into a tail. Even after arbitrary constant alignment,

```math
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
```

**DERIVED / COUNTEREXAMPLE:** finite-window insufficiency survives the pure-delay loophole.

Full derivation: `LATENCY_COMPENSATED_DISPERSION_STEP.md`.

---

## 2026-08-11 12:18 EDT — Exact finite-time SNR accumulation

Derived

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

**CONSEQUENCE:** eventual detectability and rate of access to it are distinct.

Full derivation: `SNR_ACCUMULATION_STEP.md`.

---

## 2026-08-11 12:30 EDT — Detection probability by deadline

For the simple known-time Gaussian test,

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

**DERIVED / CONDITIONAL:** equal eventual SNR can coexist with radically unequal early-deadline detection probability.

Full derivation: `DEADLINE_DETECTION_PROBABILITY_STEP.md`.

---

## 2026-08-11 12:38 EDT — Independent-slot unknown-time search

For `M` independent timing hypotheses,

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**DERIVED / CONDITIONAL:** timing uncertainty consumes SNR margin through a global search threshold.

**WARNING:** `M` is not digital sample count in a continuous timing scan.

Full derivation: `UNKNOWN_TIME_SEARCH_STEP.md`.

---

## 2026-08-11 12:47 EDT — Continuous-time search correlation

Defined the noise-whitened template and derived scan covariance

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
```

When the second moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not determine timing trials. For the same waveform, identical complete `D*(f)` gives identical full-observation timing-search covariance.

**REGULARITY WARNING:** the ideal abrupt exponential has divergent second moment in ideal white noise; Rice curvature needs high-frequency regularization or a smoother waveform.

Full derivation: `CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`.

---

## 2026-08-11 13:01 EDT — Finite-deadline correction and ranking reversal

The actual finite-deadline search must use the finite filter

```math
q_t=C_t^{-1}s_t
```

and its own covariance `r_t(Delta)`.

**CORRECTION / INVALID SHORTCUT:** do not combine finite-window `eta(t)` with Step-08 full-template `f_rms` as one exact finite-deadline formula.

Constructed the stable causal equal-eventual-SNR family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR at every finite duration, but face a larger full-template unknown-time search threshold over fixed physical `L`. Under standard finite-to-full threshold convergence, the detection ranking reverses at sufficiently large finite duration.

**DERIVED / CONDITIONAL:** faster SNR acquisition is not guaranteed to dominate timing-search complexity.

Full derivation: `SEARCH_PENALTY_REVERSAL_STEP.md`.

---

## 2026-08-11 13:18 EDT — Task-level detection-time surface

For each finite filter duration `t`, compute both the signal SNR and unknown-time threshold from the same filter. Defined

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is a task-level surface, not a detector-only replacement for `D*`.

A rational by-deadline detector may use any shorter filter; generic finite interior `t_opt` was left open.

Full derivation: `DETECTION_TIME_SURFACE_STEP.md`.

---

## 2026-08-11 13:28 EDT — Dimensionless surface and filter-duration ordering

For the Step-09 family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

and

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

The exact finite-duration covariance scales as `R_x(|Delta|/tau)`.

For fixed lag, `R_x` is nondecreasing with `x`. Slepian comparison therefore makes the global search threshold nonincreasing with filter duration, while accumulated SNR increases strictly.

**DERIVED / NEGATIVE RESULT:** this family has no finite interior `t_opt`; the optimal filter uses all data allowed by the deadline.

**INTERPRETATION:** Step-09 reversal is a cross-detector scaling effect caused by different `L/tau`, not poor integration choice.

Full derivation: `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`.

---

## 2026-08-11 13:39 EDT — Fast/slow task-regime boundary

### Exact preference boundary

For

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

```math
T_{D,f}=\tau_fX_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}=r\tau_fX_D(\rho_0,\alpha,\beta,\ell).
```

Therefore the fast/slow boundary is

```math
\boxed{
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

### Rejected shortcut

**REJECTED:** asymptotic-margin equality is not the preference boundary. The slow detector has the better asymptotic search margin for every `L>0`, yet the fast detector wins for known or sufficiently small timing uncertainty because its physical time unit is smaller. Minimum decision times, not eventual margins, must be compared.

### Exact feasibility partition

Let

```math
c=\rho_0-\Phi^{-1}(\beta).
```

With `Gamma_infinity(ell,alpha)` the full-template search threshold:

```text
both feasible:
    c > Gamma_infinity(r ell,alpha)

slow-only feasible:
    Gamma_infinity(ell,alpha) < c <= Gamma_infinity(r ell,alpha)

neither feasible:
    c <= Gamma_infinity(ell,alpha)
```

**DERIVED:** slow-only feasibility can occur; fast-only feasibility cannot under equal `rho_0`.

Define

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<\rho_0-\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{L_{crit}(\tau)=\tau\ell_{crit}.}
```

so

```math
L_{crit,s}/L_{crit,f}=\tau_s/\tau_f.
```

### Crossover existence

At `L=0`, the fast detector wins because both detectors face the same dimensionless task but `tau_f<tau_s`. The fast detector reaches its feasibility limit first as `L` grows; near that limit its required detection time diverges while the slow detector remains feasible. Under standard continuity/extreme-value conditions, at least one finite fast-to-slow crossover must therefore occur before `L_{crit,f}`.

**OPEN:** crossover uniqueness and exact location are not established.

A high-threshold Rice estimate was recorded only as an illustration of the feasibility scaling, not as the exact boundary.

Full derivation: `TASK_REGIME_BOUNDARY_STEP.md`.

### Next question, held open

Can the exact finite-duration Gaussian scan with covariance `R_x` be evaluated numerically well enough to map `Gamma(x,ell,alpha)`, solve the crossover boundary, and produce an actual fast/slow phase diagram without using an uncontrolled independent-trials approximation?
