# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Eleven logical steps completed. Step 11 gives an exact dimensionless form of the task-level detection-time surface for the controlled equal-eventual-SNR time-scaled family and proves a negative result: within that family the true-alignment task margin increases strictly with filter duration, so no finite interior optimal integration time exists. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`
6. `experiments/01-equal-dstar-different-speed/SNR_ACCUMULATION_STEP.md`
7. `experiments/01-equal-dstar-different-speed/DEADLINE_DETECTION_PROBABILITY_STEP.md`
8. `experiments/01-equal-dstar-different-speed/UNKNOWN_TIME_SEARCH_STEP.md`
9. `experiments/01-equal-dstar-different-speed/CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`
10. `experiments/01-equal-dstar-different-speed/SEARCH_PENALTY_REVERSAL_STEP.md`
11. `experiments/01-equal-dstar-different-speed/DETECTION_TIME_SURFACE_STEP.md`
12. `experiments/01-equal-dstar-different-speed/DIMENSIONLESS_DETECTION_SURFACE_STEP.md`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, refinements, invalidations, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the current blob SHA before replacing an existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and explain why they changed;
6. make narrow edits or explicit compact consolidations;
7. update `CURRENT_STATE.md` whenever the scientific frontier changes;
8. append or consolidate a timestamped entry in `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — physically consistent construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior conditional statement without invalidating the prior restricted result.
- **NEGATIVE RESULT** — a natural candidate effect was tested and shown absent under the stated model.
- **OPEN** — not established.
- **INVALIDATED** — shown false under its stated generality.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Original starting question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Question:

> Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 4. Surviving logical chain

### Step 01 — scalar reference `D*` is insufficient

Equal reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**Do not infer:** `fast is always better`; signal and noise filtering can cancel.

### Step 02 — known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation problem.

### Step 03 — full-observation unknown timing versus finite truncation

Identical complete `D*(f)` gives identical ideal stationary-Gaussian full-observation timing-search statistics. Finite truncation can break the equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A stable causal all-pass factor can preserve complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after arbitrary latency compensation.

### Step 05 — finite-time SNR accumulation

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

### Step 06 — known-time detection probability

```math
P_D(t;\alpha)=
\Phi\!\left[
\rho_t-\Phi^{-1}(1-\alpha)
\right].
```

### Step 07 — independent-slot unknown-time penalty

```math
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
```

**Warning:** `M` is not digital sample count in a continuous timing scan.

### Step 08 — continuous-time full-template timing correlation

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
\qquad
W(f)=\frac{|K(f)|^2}{\int|K|^2df},
```

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
```

When the second moment exists, `f_rms^2=integral f^2W df`; differentiable Gaussian scans obey Rice upcrossing statistics.

**REFINEMENT:** sample rate alone does not raise timing-search complexity. For the same waveform, identical complete `D*(f)` gives identical full-observation timing covariance.

### Step 09 — exact finite-deadline scan and conditional cross-detector reversal

Use the finite filter

```math
q_t=C_t^{-1}s_t
```

and its exact timing covariance

```math
r_t(\Delta)
=\frac{\int |Q_t|^2S_ne^{i2\pi f\Delta}df}
{\int |Q_t|^2S_ndf}.
```

**CORRECTION:** do not mix finite-window `eta(t)` with full-template `f_rms` as one exact statistic.

For the controlled equal-eventual-SNR family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

faster members accumulate more SNR at every finite duration, but over a fixed physical timing-search interval they face a larger full-template search threshold. Under standard finite-to-full threshold convergence, the detection ranking reverses at sufficiently large finite duration.

**DERIVED / CONDITIONAL:** rapid SNR acquisition is not guaranteed to dominate timing-search complexity.

### Step 10 — task-level detection-time surface

For each finite duration `t`, use the same filter for signal SNR and timing search.

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau),
```

```math
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha),
```

```math
P_{D,true}
=\Phi[\rho_t-\gamma_t(L,\alpha)].
```

Define

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
}
```

This is a task-level surface, not a detector-only scalar.

### Step 11 — exact dimensionless collapse and no finite interior optimum

For the Step-09 family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
```

and

```math
r_{\tau,t}(\Delta)=R_x(|\Delta|/\tau),
```

with

```math
R_x(y)
=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv}
```

for `0<=y<x`, zero otherwise.

Therefore

```math
\gamma_{\tau,t}(L,\alpha)
=\Gamma(x,\ell,\alpha)
```

and

```math
\boxed{
\mathcal T_D
=\tau\,X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

For fixed lag, `R_x` is pointwise nondecreasing with filter duration. Slepian comparison then makes the global search threshold nonincreasing with `x`, while `eta'(x)>0`.

Hence

```math
\boxed{
M(x)=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\text{ is strictly increasing.}
}
```

**DERIVED / NEGATIVE RESULT:** this family has no finite interior `t_opt`; for a maximum allowed delay `T`, the optimal filter uses `t=T`.

This does not undo Step 09. Its ranking reversal is a cross-detector scaling effect caused by different `L/tau`, not by poor filter-duration choice.

---

## 5. Current scientific frontier

For the controlled family:

```text
rho_0
    equal eventual known-time SNR

x=t/tau
    dimensionless filter duration

ell=L/tau
    dimensionless timing uncertainty

eta(x)
    accumulated SNR fraction

R_x
    exact finite-duration timing covariance

Gamma(x,ell,alpha)
    exact global false-alarm threshold

M(x)=rho_0 sqrt(eta)-Gamma
    true-alignment task margin

T_D/tau=X_D(rho_0,alpha,beta,L/tau)
    dimensionless detection-time surface
```

At fixed physical `L`, smaller `tau` both shrinks the physical unit of decision time and enlarges the normalized timing-search burden. No monotonic ranking by `tau` alone follows.

---

## 6. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff;
- `eta`, `f_rms`, `mathcal T_D`, or any finite tuple is a universal detector-only replacement for `D*`;
- Step-09 ranking reversal is common in practical detectors;
- all detector families have monotone filter-duration margins;
- a finite interior `t_opt` can never occur outside the Step-09 family;
- the hard-window finite scan is always differentiable;
- true-alignment crossing equals exact global rejection/localization probability;
- the max scan is Bayes-optimal for every arrival-time prior;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, repeated/sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> For two members of the Step-09 family with different `tau` but equal `rho_0`, what is the boundary in task space `(L, alpha, beta)` where their detection-time surfaces cross — i.e. where the detector that reaches the required decision first switches from the faster member to the slower member?
