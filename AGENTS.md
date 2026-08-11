# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Nine logical steps completed. Step 09 corrects the naive mixing of finite-window `eta(T)` with full-template `f_rms`, derives the exact finite-deadline timing-scan covariance, and gives a conditional equal-eventual-SNR family in which the faster detector's larger unknown-time search penalty eventually reverses its finite-time detection ranking even while it retains slightly more accumulated SNR. No universal replacement metric and no novelty claim.

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

### Step 01 — scalar reference D* is insufficient

A physically allowed one-pole + additive-output-noise construction gives unequal temporal-signal SNR despite equal reference `D*`.

**Do not infer:** `fast is always better`; filtering of dominant noise can cancel signal attenuation.

### Step 02 — known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing alone is not enough; finite truncation is

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical matched-filter timing-search statistics.

A finite fixed window can break the equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after arbitrary latency compensation.

### Step 05 — exact finite-time SNR accumulation

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

This separates eventual detectability from rate of access to that detectability.

### Step 06 — fixed-deadline detection probability

For the simple known-time Gaussian decision,

```math
\boxed{
P_D(T;\alpha)=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

Equal eventual SNR can coexist with radically unequal early-deadline detection probability.

### Step 07 — independent-slot unknown-time search penalty

For `M` independent candidate arrival slots scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes extra SNR margin through a global threshold.

**Warning:** `M` is not digital sample count in a continuous scan.

### Step 08 — continuous-time full-observation scan

Define

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

If the second moment exists,

```math
\boxed{
f_{\mathrm{rms}}^2=\int f^2W(f)df,
}
```

and for a differentiable stationary Gaussian scan

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

**REFINEMENT:** sample rate alone does not raise the trials factor. For the same waveform, identical complete magnitude `D*(f)` gives identical full-observation scan covariance and search penalty.

### Step 09 — finite-deadline scan and conditional ranking reversal

#### Correct finite-deadline search object

For a search that must decide using only `T` seconds after each candidate event time, use

```math
q_T=C_T^{-1}s_T.
```

Its translated normalized noise-only scan has covariance

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

**REFINEMENT / CORRECTION:** do not combine Step-05 finite-window `eta(T)` with Step-08 full-observation `f_rms` as if they were an exact single finite-deadline protocol.

Hard window truncation can also destroy differentiability, so a Rice `f_rms` reduction may require physical bandwidth regularization or a non-differentiable extreme-value treatment.

#### Equal-eventual-SNR family

For the same optical event

```math
p(t)=e^{-bt}u(t)
```

and stable causal family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

choose amplitude scaling so every detector has the same `rho_infinity=rho_0`.

The output is

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

with accumulation

```math
\boxed{
\eta_\tau(T)=1-e^{-2x}(1+2x+2x^2),
\qquad x=T/\tau.
}
```

For `tau_f<tau_s`, the faster member has strictly more finite-time SNR at every finite `T`, while the difference tends to zero as `T->infinity`.

The full-template scan covariance is

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

Over a fixed physical monitoring duration `L`, the faster detector explores a longer normalized interval and therefore has a strictly larger full-template global max threshold for ordinary nontrivial false-alarm quantiles.

Let `gamma_{i,T}` be the exact finite-deadline threshold and assume standard convergence to the full-template threshold as `T->infinity`. Then

```text
Delta rho_T > 0 but -> 0
Delta gamma_T -> positive constant
```

so for sufficiently large finite `T`,

```math
\boxed{
0<\Delta\rho_T<\Delta\gamma_T.
}
```

Therefore

```math
\boxed{
P_{D,true,f}<P_{D,true,s}
}
```

while still

```math
\boxed{
\rho_{f,T}>\rho_{s,T}.
}
```

**DERIVED / CONDITIONAL:** rapid SNR acquisition is not guaranteed to dominate unknown-time search complexity. A controlled finite-deadline ranking reversal exists under the stated convergence condition.

This does not contradict Step 03 because the Step-09 family has equal integrated asymptotic SNR but different SNR-weighted spectra; it does not have identical complete `D*(f)`.

---

## 5. Current scientific frontier

The present task-level ingredients are now

```text
rho_infinity
    total eventual known-time matched-filter separation

rho_T / eta(T)
    finite-deadline accessible separation

r_T(Delta)
    finite-deadline timing-search covariance

gamma_T(L,alpha)
    global unknown-time search threshold

rho_T - gamma_T
    true-time Gaussian crossing margin for the simple max-scan problem
```

The project has therefore moved beyond any monotonic one-dimensional `speed versus sensitivity` picture: faster SNR acquisition and finer timing-search resolution can oppose one another, and either can dominate depending on the measurement protocol.

---

## 6. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff;
- `eta(T)`, `f_rms`, or any two-number pair is a universal detector-only replacement for `D*`;
- the Step-09 reversal is common in practical detectors; it is an existence/conditional result;
- a universal reversal deadline exists;
- the finite-deadline hard-window scan is always differentiable;
- the max scan is Bayes-optimal for every arrival-time prior;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, repeated/sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Is there a compact task-level description — perhaps a detection-time surface in `(P_FA, P_D, L)` rather than a scalar figure of merit — that contains both SNR accumulation and timing-search uncertainty without discarding the detector response information exposed in Steps 01–09?
