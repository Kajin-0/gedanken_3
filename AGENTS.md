# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Nineteen logical steps completed. Step 19 removes the artificial equal-accessible-SNR normalization and shows that a genuine finite readout-bandwidth optimum appears for the large-speed-ratio/full-template unknown-time objective when physical signal/noise are held fixed. No universal replacement metric and no novelty claim.

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
14. `experiments/01-equal-dstar-different-speed/NUMERICAL_SCAN_CONVERGENCE_STEP.md`
15. `experiments/01-equal-dstar-different-speed/FINITE_BANDWIDTH_REGULARIZATION_STEP.md`
16. `experiments/01-equal-dstar-different-speed/FINITE_BANDWIDTH_NUMERICAL_STEP.md`
17. `experiments/01-equal-dstar-different-speed/RARE_EVENT_UPCROSSING_STEP.md`
18. `experiments/01-equal-dstar-different-speed/HIGH_THRESHOLD_CROSSOVER_ASYMPTOTICS_STEP.md`
19. `experiments/01-equal-dstar-different-speed/FIXED_PHYSICAL_BANDWIDTH_STEP.md`
20. `experiments/01-equal-dstar-different-speed/PHYSICAL_BANDWIDTH_OPTIMUM_STEP.md`
21. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`
22. `experiments/01-equal-dstar-different-speed/numerics/regularized_scan_mc.py`
23. `experiments/01-equal-dstar-different-speed/numerics/upcrossing_importance_sampling.py`
24. `experiments/01-equal-dstar-different-speed/numerics/asymptotic_crossover.py`
25. `experiments/01-equal-dstar-different-speed/numerics/fixed_physical_bandwidth.py`
26. `experiments/01-equal-dstar-different-speed/numerics/physical_bandwidth_optimum.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, cancellations, counterexamples, negative results, rejected shortcuts, failed numerical estimates, numerical validations, asymptotic limits, refinements, and unresolved branches.

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

**Live `main` overrides chat summaries, memory, and stale recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior statement without erasing it.
- **NEGATIVE RESULT** — a natural candidate effect was tested and shown absent under the stated model.
- **REJECTED SHORTCUT** — a tempting inference/formula was shown not to answer the actual question.
- **FAILED NUMERICAL ESTIMATE** — failed convergence/validation and must never be reused as a result.
- **NUMERICAL VALIDATION** — survived stated numerical cross-checks within scope.
- **NUMERICAL SPOT CHECK** — supporting calculation that is not a complete optimization/convergence result.
- **ASYMPTOTIC** — derived only in a controlled limiting regime.
- **OPEN** — not established.
- **INVALIDATED** — shown false under its stated generality.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Original question

Two detectors satisfy

```math
D_A^*=D_B^*
```

but initially have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 4. Compact surviving chain

### Steps 01–04 — `D*`, full observation, finite-window phase
- Equal reference scalar `D*` does not guarantee equal arbitrary-temporal-signal SNR.
- Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that ideal stationary-Gaussian full-observation equivalence.
- Finite windows can break it because magnitude `D*(f)` discards phase/temporal placement; an all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-time SNR and timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

and unknown timing raises a global threshold governed by scan covariance, not sample count.

### Step 09 — finite-deadline correction and ranking reversal
**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be combined with full-template timing bandwidth as one exact statistic.

For

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

faster members acquire SNR sooner but can pay a larger timing-search penalty. Ranking can reverse.

### Steps 10–12 — task surface and fast/slow boundary

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum.

Fast/slow boundary:

```math
X_D(r\ell)-rX_D(\ell)=0.
```

### Step 13 — failed rough-grid phase boundary
**FAILED NUMERICAL ESTIMATE:** diagnostic `ell ~ 49` is invalid.

Cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so the ideal-white-noise finite scan is locally Brownian-like.

### Steps 14–15 — genuine finite timing-information bandwidth
**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily an information-band limit because whitening can undo it.

Use the smooth surrogate

```math
J_{x,\kappa}=|H_x|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the cusp; correlated numerics and Rice agree at validation points.

### Step 16 — exact Palm rare-event identity

```math
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; its error is multiple excursions plus endpoint overlap. Palm sampling makes `alpha=1e-6` practical.

### Step 17 — high-threshold law and extreme speed ratio
Exact smooth crossover has Palm factors; isolated excursions give a compact endpoint-retaining Rice equation.

**REJECTED SHORTCUT:** small `alpha` does not justify dropping endpoint `Q(u)`.

Rice accuracy is nonuniform into the finite-window rough limit.

Extreme-speed-ratio branch:

```math
L_\times\to\tau_f\ell_{crit,\kappa}.
```

### Step 18 — same physical electronics bandwidth, equal accessible SNR

```math
\kappa_i=\Omega_B\tau_i.
```

Large-`r` crossover changes from electronics-limited

```math
L_\times\sim1/\Omega_B
```

to detector-limited

```math
L_\times\sim\tau_f.
```

**NEGATIVE RESULT / QUALIFICATION:** no finite bandwidth optimum appears while accessible eventual SNR is artificially held fixed.

### Step 19 — fixed physical signal/noise; genuine bandwidth optimum
Let `rho_full` be the unregularized full-template SNR. Then

```math
\rho_\infty(\kappa)
=\rho_{full}\sqrt{F(\kappa)},
```

where

```math
F(\kappa)
=\frac{2}{\pi}
\int\frac{e^{-(\nu/\kappa)^2}}{(1+\nu^2)^2}d\nu,
```

and

```math
\sigma^2(\kappa)
=\frac{\int \nu^2(1+\nu^2)^{-2}e^{-(\nu/\kappa)^2}d\nu}
{\int (1+\nu^2)^{-2}e^{-(\nu/\kappa)^2}d\nu}.
```

Narrow bandwidth drives accessible SNR to zero, so a finite minimum bandwidth is required for known-time feasibility.

Wide-band asymptotics:

```math
\rho_\infty(\kappa)
=\rho_{full}[1-1/(2\kappa^2)+O(\kappa^{-3})],
```

but

```math
\sigma(\kappa)
=1-2/(\sqrt\pi\kappa)+O(\kappa^{-2}).
```

Thus near infinite bandwidth:

```text
SNR penalty from narrowing          ~ O(kappa^-2)
search-complexity benefit           ~ O(kappa^-1)
```

and for the large-`r` full-template Rice feasibility/crossover objective,

```math
\ell_{crit}(\kappa)
=\ell_{crit}(\infty)
[1+2/(\sqrt\pi\kappa)+O(\kappa^{-2})].
```

**DERIVED / CONDITIONAL:** if the full-band detector is strictly task-feasible, infinite bandwidth is suboptimal and at least one finite bandwidth optimum must exist in the chosen Gaussian information-band model.

Step-16-calibrated illustration:

```text
rho_full ~= 6.240757
alpha=1e-6, beta=0.90
kappa_min ~= 3.14545
kappa_opt^Rice ~= 42.23
ell_crit,opt ~= 0.90083
ell_crit,infinity ~= 0.88906
```

A `10000`-path Palm spot check preserves the finite-candidate-over-infinite ordering, but the exact Palm-optimal bandwidth and uniqueness remain open.

---

## 5. Current frontier

The next question is finite speed ratio with one common physical bandwidth and no SNR renormalization. Bandwidth then changes **both detectors'** accessible SNR and timing-search covariance simultaneously.

---

## 6. Scope boundary

Do not claim:

- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the Step-13 `ell~49` diagnostic is real;
- arbitrary low-pass filtering is a true information-band limitation;
- the Gaussian information weighting is a literal circuit transfer function;
- Rice is always as accurate as in Step 16;
- the Step-19 illustrative GHz optimum is a hardware recommendation;
- bandwidth-optimum uniqueness;
- the exact Palm optimum has been solved;
- maximizing `L_cross` necessarily optimizes every fixed-`L` decision task;
- finite-r common-bandwidth behavior has already been solved;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Does the finite readout-bandwidth optimum survive when the speed ratio is finite and the same physical bandwidth simultaneously changes both detectors' accessible SNR and timing-search covariance, and can that produce multiple fast/slow preference reversals as bandwidth is swept?
