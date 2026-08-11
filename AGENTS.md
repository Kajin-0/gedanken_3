# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twelve logical steps completed. Step 12 derives the exact implicit fast/slow detection-time boundary for the controlled equal-eventual-SNR scaled family, identifies a slow-only feasibility region and proves fast-only feasibility impossible under the model, and conditionally establishes at least one finite fast-to-slow crossover as timing uncertainty grows. No universal replacement metric and no novelty claim.

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
13. `experiments/01-equal-dstar-different-speed/TASK_REGIME_BOUNDARY_STEP.md`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, rejected shortcuts, refinements, invalidations, and unresolved branches.

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
- **REJECTED SHORTCUT** — a tempting inference/formula was shown not to answer the actual question.
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

### Step 01 — scalar reference D* insufficiency

Equal reference `D*` does not guarantee equal SNR for arbitrary temporal signals. Signal/noise filtering can cancel, so do not infer `fast is always better`.

### Step 02 — full-observation known-waveform SNR

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation problem.

### Step 03 — unknown timing negative result; finite-window failure

Identical complete `D*(f)` gives identical ideal stationary-Gaussian full-observation timing-search statistics.

**NEGATIVE RESULT:** unknown arrival time alone does not break equivalence.

Finite truncation can break it because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A stable causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR after latency compensation.

### Step 05 — finite-time SNR accumulation

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

### Step 06 — known-time Gaussian decision

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

### Step 07 — independent-slot unknown-time penalty

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

`M` is not digital sample count in a continuous scan.

### Step 08 — continuous-time full-template timing covariance

```math
K=GP/\sqrt{S_n},
\qquad
W=|K|^2/\int|K|^2df,
```

```math
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
```

When the second moment exists, `f_rms` controls local covariance curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not raise timing-search complexity. Identical complete `D*(f)` gives identical full-observation search covariance for the same waveform.

### Step 09 — exact finite-deadline scan and conditional reversal

The finite scan must use

```math
q_t=C_t^{-1}s_t
```

and its own covariance `r_t(Delta)`.

**REJECTED / INVALID SHORTCUT:** finite-window `eta(t)` and full-template `f_rms` cannot be inserted into one exact finite-deadline formula without deriving the finite filter's scan covariance.

For the controlled equal-eventual-SNR family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

faster members accumulate more SNR at every finite duration but face larger fixed-physical-`L` timing-search burden. Under standard finite-to-full convergence, the cross-detector ranking reverses at sufficiently large finite duration.

### Step 10 — task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This packages finite SNR and unknown-time search into a task-level surface, not a detector scalar.

### Step 11 — dimensionless collapse and negative filter optimum

For the scaled family,

```math
x=t/\tau,
\qquad
\ell=L/\tau,
```

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Finite-duration covariance is `R_x(|Delta|/tau)`. Pointwise covariance ordering plus Slepian comparison makes the search threshold nonincreasing with filter duration, while SNR rises strictly.

**NEGATIVE RESULT:** no finite interior `t_opt` exists in this family; use all data allowed by the deadline. Step-09 reversal is therefore cross-detector, not self-suboptimal filtering.

### Step 12 — task-regime boundary

Let

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s.
```

The exact detection-time preference boundary is

```math
\boxed{
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time preference boundary. The slow detector has the better eventual search margin for every `L>0`, while the fast detector still wins at `L=0` and sufficiently small `L` because its physical time unit is smaller.

Let

```math
c=\rho_0-\Phi^{-1}(\beta).
```

With full-template threshold `Gamma_infinity(ell,alpha)`:

```text
both feasible:
    c > Gamma_infinity(r ell,alpha)

slow-only feasible:
    Gamma_infinity(ell,alpha) < c <= Gamma_infinity(r ell,alpha)

neither feasible:
    c <= Gamma_infinity(ell,alpha)
```

**DERIVED:** slow-only feasibility can occur; fast-only feasibility cannot under equal eventual SNR.

Define

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<\rho_0-\Phi^{-1}(\beta)\}.
```

Then

```math
L_{crit}(\tau)=\tau\ell_{crit},
```

so `L_crit,s/L_crit,f=tau_s/tau_f`.

Under standard continuity and Gaussian extreme-value growth, fast wins at `L=0`, becomes infeasible first as `L` grows, and slow remains feasible there; hence at least one finite fast-to-slow crossover must occur. Crossover uniqueness is **OPEN**.

---

## 5. Current scientific frontier

The exact analytic regime structure is known, but the correlated Gaussian supremum quantile

```math
\Gamma(x,\ell,\alpha)
```

has not yet been computed exactly/numerically over the task plane.

The next task is numerical rather than conceptual: evaluate the finite-duration Gaussian scan with covariance `R_x`, solve the crossover equation, and map the fast/slow phase diagram without replacing the correlated search by an uncontrolled independent-trials count.

---

## 6. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better or worse;
- a universal speed-detectivity tradeoff;
- `eta`, `f_rms`, `mathcal T_D`, or the task boundary is a universal detector-only replacement for `D*`;
- Step-09/12 ranking reversal is common in practical detectors;
- crossover uniqueness;
- all detector families have monotone filter-duration margins;
- true-alignment crossing equals exact global rejection/localization probability;
- the max scan is Bayes-optimal for every arrival-time prior;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the finite-duration Gaussian scan with covariance `R_x` be computed numerically accurately enough to map `Gamma(x,ell,alpha)`, solve the fast/slow crossover equation, and produce an actual task phase diagram for chosen `(rho_0,r,alpha,beta)` without reverting to an uncontrolled independent-trials approximation?
