# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Ten logical steps completed. Step 10 defines a task-level detection-time surface `mathcal T_D(P_FA,P_D,L)` that combines finite-record SNR accumulation with the exact finite-record unknown-time search threshold from the same filter. It also distinguishes maximum allowed decision delay from chosen filter duration, ensuring best by-deadline performance can ignore later data. No universal replacement metric and no novelty claim.

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

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, refinements, invalidations, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the current blob SHA before replacing an existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and explain why they changed;
6. make narrow edits where practical;
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

Equal low-frequency/reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

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

A causal all-pass factor can preserve complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after arbitrary latency compensation.

### Step 05 — finite-time SNR accumulation

```math
\boxed{
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
}
```

```math
\boxed{
\eta(t)=\rho_t^2/\rho_\infty^2.
}
```

This separates eventual detectability from rate of access to it.

### Step 06 — known-time detection probability

```math
\boxed{
P_D(t;\alpha)=
\Phi\!\left[
\rho_t-\Phi^{-1}(1-\alpha)
\right].
}
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

### Step 07 — independent-slot unknown-time penalty

For `M` independent candidate times,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

**Warning:** `M` is not digital sample count in a continuous timing scan.

### Step 08 — continuous-time full-template search

With

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
```

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'},
```

scan covariance is

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

When the second moment exists,

```math
f_{rms}^2=\int f^2W(f)df
```

and a differentiable stationary Gaussian scan has Rice upcrossing density

```math
\nu_u^+=f_{rms}e^{-u^2/2}.
```

**REFINEMENT:** sample rate alone does not raise search complexity. For the same waveform, identical complete `D*(f)` gives identical full-observation timing-search covariance.

### Step 09 — finite-deadline scan and conditional reversal

The actual finite-deadline scan must use

```math
q_t=C_t^{-1}s_t
```

with covariance

```math
\boxed{
r_t(\Delta)
=\frac{
\int |Q_t(f)|^2S_n(f)e^{i2\pi f\Delta}df
}{
\int |Q_t(f)|^2S_n(f)df
}.
}
```

**CORRECTION:** do not combine finite-window `eta(t)` with Step-08 full-template `f_rms` as one exact finite-deadline statistic.

A stable causal time-scaled family with equal `rho_infinity` was constructed for which the faster member has more finite-time SNR at every finite duration, while its full-template timing search over fixed physical `L` has a larger threshold. Under standard finite-to-full threshold convergence, the unknown-time detection ranking reverses at sufficiently large finite duration even while the faster member still has more accumulated SNR.

**DERIVED / CONDITIONAL:** rapid SNR accumulation is not guaranteed to dominate timing-search complexity.

### Step 10 — task-level detection-time surface

For each chosen filter duration `t`, use the same finite-duration optimal filter to compute both the finite SNR `rho_t` and the unknown-time scan.

Let

```math
Z_{t,L}=\sup_{0\le\tau\le L}z_t(\tau).
```

Define the exact global false-alarm threshold

```math
\boxed{
\gamma_t(L,\alpha)
=F^{-1}_{Z_{t,L}|H_0}(1-\alpha).
}
```

At the true event alignment,

```math
\boxed{
P_{D,true}(t;L,\alpha)
=\Phi[\rho_t-\gamma_t(L,\alpha)].
}
```

Define raw task margin

```math
\boxed{
m(t;L,\alpha)=\rho_t-\gamma_t(L,\alpha).
}
```

The raw margin need not be monotone in filter duration because both signal accumulation and timing-search resolution change.

If the maximum allowed decision delay is `T`, a rational measurement may use any shorter filter duration. Therefore

```math
\boxed{
m^*(T;L,\alpha)
=\sup_{0<t\le T}m(t;L,\alpha).
}
```

This by-deadline envelope is nondecreasing.

For required event-attributable probability `beta`, define the task-level detection-time surface

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=\inf\left\{
t>0:
\rho_t-\gamma_t(L,\alpha)
\ge\Phi^{-1}(\beta)
\right\}.
}
```

If no duration satisfies the operating point, `mathcal T_D=infinity`.

This is **not** a detector-only replacement for `D*`. It retains the specified optical waveform, detector response, noise covariance, finite-record filter, monitoring interval, and global false-alarm protocol.

Define

```math
m_{max}(L,\alpha)=\sup_t[\rho_t-\gamma_t(L,\alpha)].
```

The requested `(alpha,beta,L)` point is feasible under the true-time criterion iff

```math
m_{max}(L,\alpha)\ge\Phi^{-1}(\beta).
```

If the supremum is attained, a task-optimal filter duration can be defined by

```math
t_{opt}\in\operatorname*{arg\,max}_t[\rho_t-\gamma_t(L,\alpha)].
```

A finite interior optimum is possible in principle but not yet established for a concrete regime.

---

## 5. Current scientific frontier

The present task-level structure is

```text
rho_infinity
    eventual known-time matched-filter separation

rho_t / eta(t)
    separation available to a chosen finite-duration filter

r_t(Delta)
    timing-search covariance generated by that same filter

gamma_t(L,alpha)
    global unknown-arrival threshold

m(t;L,alpha)=rho_t-gamma_t
    raw event-attributable decision margin

m*(T;L,alpha)
    best margin achievable by the allowed deadline

mathcal T_D(alpha,beta,L)
    minimum decision delay for the specified task
```

The next question is whether the Step-09 time-scaled detector family makes this surface collapse onto a small set of dimensionless variables and whether that exposes a finite optimal integration/filter duration.

---

## 6. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff;
- `eta(t)`, `f_rms`, `mathcal T_D`, or any finite tuple is a universal detector-only replacement for `D*`;
- the Step-09 reversal is common in practical detectors;
- a finite interior `t_opt` always exists;
- the hard-window finite scan is always differentiable;
- the true-time crossing probability equals the exact global-rejection or localization probability;
- the max scan is Bayes-optimal for every arrival-time prior;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, repeated/sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> For the time-scaled equal-eventual-SNR family introduced in Step 09, does the detection-time surface collapse onto dimensionless variables such as `t/tau`, `L/tau`, `rho_infinity`, `P_FA`, and `P_D`, and does that reveal a finite optimal integration/filter duration in any regime?
