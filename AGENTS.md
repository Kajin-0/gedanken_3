# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty logical steps completed. Step 20 extends the fixed-physics common-bandwidth problem to finite speed ratio and gives a quadrature-converged finite-duration Rice counterexample with two bandwidth-driven detector-preference reversals: `slow -> fast -> slow`. Exact Palm-corrected switch values remain open. No universal replacement metric and no novelty claim.

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
21. `experiments/01-equal-dstar-different-speed/FINITE_R_BANDWIDTH_REVERSAL_STEP.md`
22. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`
23. `experiments/01-equal-dstar-different-speed/numerics/regularized_scan_mc.py`
24. `experiments/01-equal-dstar-different-speed/numerics/upcrossing_importance_sampling.py`
25. `experiments/01-equal-dstar-different-speed/numerics/asymptotic_crossover.py`
26. `experiments/01-equal-dstar-different-speed/numerics/fixed_physical_bandwidth.py`
27. `experiments/01-equal-dstar-different-speed/numerics/physical_bandwidth_optimum.py`
28. `experiments/01-equal-dstar-different-speed/numerics/finite_r_bandwidth_reversal.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, cancellations, counterexamples, negative results, rejected shortcuts, failed numerical estimates, numerical validations, asymptotic limits, refinements, invalidations, and unresolved branches.

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
8. append or explicitly consolidate a timestamped `PROGRESS_LOG.md` entry for consequential work.

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
- **FAILED NUMERICAL ESTIMATE** — a computed value failed convergence/validation and must never be reused as a result.
- **NUMERICAL VALIDATION** — survived stated numerical cross-checks within scope.
- **NUMERICAL COUNTEREXAMPLE** — a numerically converged construction disproves a broader implication within the stated model/approximation.
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

### Steps 01–04 — limits of scalar and magnitude-only `D*`

- Equal reference scalar `D*` does not determine arbitrary temporal-signal SNR.
- Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that ideal stationary-Gaussian full-observation equivalence.
- Finite observation can break it because magnitude `D*(f)` discards temporal phase/placement; an all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-record SNR and timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold determined by timing-scan covariance, not digital sample count.

### Step 09 — finite-deadline correction and ranking reversal

**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be mixed with full-template timing bandwidth as one exact statistic.

For

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

faster members acquire SNR sooner but can pay a larger unknown-time search penalty. Cross-detector ranking can reverse.

### Steps 10–12 — task surface and preference boundary

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in that original family.

For `r=tau_s/tau_f`, the exact boundary is `X_D(r ell)-r X_D(ell)=0`. Task space can contain both-feasible, slow-only, and neither-feasible regions.

### Step 13 — failed rough-grid boundary

Direct correlated Monte Carlo reproduced broad behavior but the apparent crossover moved under grid refinement.

**FAILED NUMERICAL ESTIMATE:** `ell ~ 49` is invalid.

Exact cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so the ideal-white-noise finite hard-window scan is locally Brownian-like / nondifferentiable.

### Steps 14–15 — genuine finite information bandwidth

**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily an information-band limit because optimal whitening can undo it.

The smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}
```

removes the cusp. Direct correlated simulation has controlled grid behavior and agrees with Rice/EC at validation points.

### Step 16 — exact rare-event Palm identity

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
}
```

with

```math
\lambda_u=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Rice/EC is therefore an upper bound; its error is multiple excursions plus endpoint overlap. Palm importance sampling makes `alpha=1e-6` tractable.

### Step 17 — high-threshold law and extreme speed ratio

The exact smooth crossover has Palm correction factors; isolated excursions give a compact endpoint-retaining Rice law.

**REJECTED SHORTCUT:** small `alpha` does not justify dropping the endpoint `Q(u)` term.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform into the rough limit.

For the co-scaled extreme-speed-ratio branch,

```math
L_\times\to\tau_f\ell_{crit,\kappa}.
```

### Step 18 — common physical bandwidth with accessible SNR forced equal

Use

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

With accessible eventual SNR artificially fixed, the large-`r` crossover transitions from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum appears under this artificial SNR normalization.

### Step 19 — fixed physical signal/noise; finite bandwidth optimum

Remove accessible-SNR renormalization:

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
\qquad
\sigma^2(\kappa)=I_2/I_0.
```

At wide bandwidth, SNR loss is `O(1/kappa^2)` while timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** for the large-`r` full-template Rice objective, infinite bandwidth is suboptimal whenever the full-band detector is strictly known-time feasible; at least one finite bandwidth optimum exists.

Step-16-calibrated example: `kappa_opt^Rice ~=42.23`, giving about `1.32%` larger tolerable arrival uncertainty than infinite bandwidth. A Palm spot check preserves the finite-candidate-over-infinite ordering but does not solve the exact optimum.

### Step 20 — finite-r common-bandwidth double reversal

Use common physical bandwidth with fixed underlying full-band detector SNR:

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=r\kappa_f.
```

Because the accessible fraction `F` increases with `kappa`, the slower detector has larger accessible eventual SNR at every finite bandwidth; in the narrow-band limit

```math
\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r.
```

Explicit finite-duration Rice counterexample:

```text
r=2
rho_full=6.2407571
alpha=1e-6
beta=0.90
Lambda=L/tau_f=0.895
```

The preferred detector changes as

```math
\boxed{\text{slow}\to\text{fast}\to\text{slow}}
```

with finite switch points

```text
kappa_cross_1 ~=25.4898402
kappa_cross_2 ~=130.1945883.
```

Both detectors are feasible at both switches. Halving spectral quadrature spacing from `0.02` to `0.01` changes the two switch values by only `~1.4e-8` and `~5.4e-7`.

**NUMERICAL COUNTEREXAMPLE / CONDITIONAL:** common readout bandwidth can change detector preference more than once even for only a factor-of-two intrinsic speed difference.

Mechanism:

```text
narrow band       -> accessible-SNR asymmetry favors slow
intermediate band -> intrinsic speed favors fast
wide band         -> unknown-time search burden favors slow
```

Exact Palm-corrected switch locations remain open, especially the high-band switch where finite-window Rice accuracy is least uniform.

---

## 5. Current frontier

The fixed-physics branch now has both a finite large-`r` bandwidth optimum and a finite-`r` double detector-preference reversal versus one common physical bandwidth.

The next task is to use the Step-16 Palm machinery to check whether both Step-20 reversals survive exact continuous rare-event correction and to quantify the switch shifts.

---

## 6. Scope boundary

Do not claim:

- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the Step-13 `ell~49` diagnostic is real;
- arbitrary low-pass filtering is a true information-band limitation;
- the Gaussian information weighting is a literal circuit transfer function;
- Rice is always quantitatively accurate at the Step-16 level;
- Step-19 or Step-20 GHz translations are hardware recommendations;
- every finite-r task exhibits two bandwidth reversals;
- there are at most two reversals;
- the Step-20 Rice switch locations are exact Palm values;
- crossover or bandwidth-optimum uniqueness;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Does the exact continuous Palm correction preserve both finite-`r` bandwidth reversals, especially the high-bandwidth switch where finite-window Rice accuracy is least uniform, and how far do the two switch points move?
