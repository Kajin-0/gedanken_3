# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Eighteen logical steps completed. Step 18 analyzes one shared physical electronics bandwidth, derives an electronics-limited crossover scale, and shows that no interior bandwidth optimum exists while accessible eventual SNR is artificially held fixed. No universal replacement metric and no novelty claim.

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
20. `experiments/01-equal-dstar-different-speed/numerics/correlated_scan_mc.py`
21. `experiments/01-equal-dstar-different-speed/numerics/regularized_scan_mc.py`
22. `experiments/01-equal-dstar-different-speed/numerics/upcrossing_importance_sampling.py`
23. `experiments/01-equal-dstar-different-speed/numerics/asymptotic_crossover.py`
24. `experiments/01-equal-dstar-different-speed/numerics/fixed_physical_bandwidth.py`

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
- **FAILED NUMERICAL ESTIMATE** — a computed value failed convergence/validation and must never be reused as a result.
- **NUMERICAL VALIDATION** — survived the stated numerical cross-checks within scope.
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

### Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
- Equal reference scalar `D*` does not guarantee equal arbitrary-signal SNR.
- Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence under stationary Gaussian full observation.
- Finite windows can break it because magnitude `D*(f)` discards temporal phase/placement; an all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-time SNR and timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold determined by the timing-scan covariance, not digital sample count.

### Step 09 — finite-deadline correction and ranking reversal
**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be mixed with full-template timing bandwidth as one exact statistic.

For the controlled family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

faster members acquire SNR sooner but can pay a larger unknown-time search penalty. Cross-detector ranking can reverse.

### Steps 10–12 — detection-time surface and task boundary

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration optimum exists in that family.

For `r=tau_s/tau_f`, the fast/slow boundary is

```math
X_D(r\ell)-rX_D(\ell)=0.
```

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR.

### Step 13 — failed rough-grid phase boundary
Direct correlated Monte Carlo reproduced the broad regime structure but the apparent crossover moved with timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** `ell ~ 49` is invalid.

Exact cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
a_x=2x^2e^{-2x}/\eta(x),
```

so the ideal-white-noise finite scan is locally Brownian-like.

### Steps 14–15 — genuine finite information bandwidth
**REJECTED SHORTCUT:** an invertible noiseless common low-pass is not necessarily an information-band limit because whitening can undo it.

A genuine finite timing-information spectrum removes the cusp. The smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}
```

has controlled timing-grid numerics and agrees with Rice/EC at validation points.

### Step 16 — rare-event Palm identity

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

Thus Rice/EC is an upper bound; its error is multiple excursions plus endpoint overlap. A Palm sampler makes `alpha=1e-6` tractable with thousands of paths.

### Step 17 — high-threshold law and extreme speed ratio
The exact smooth crossover has Palm correction factors; the isolated-excursion approximation gives a compact endpoint-retaining Rice equation.

**REJECTED SHORTCUT:** small global `alpha` does not justify dropping the endpoint `Q(u)` term.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform as bandwidth tends toward the rough Step-13 limit.

For the co-scaled extreme-speed-ratio branch,

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}}.
```

### Step 18 — same physical electronics bandwidth
Use one common physical information scale

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

Equal accessible eventual SNR is still imposed to isolate timing/search effects.

**REFINEMENT:** the clean large-`r` law requires `ell_crit(kappa_f)/r -> 0`; `r->infinity` alone is insufficient if `kappa_f` simultaneously collapses.

Under that condition,

```math
\boxed{
L_\times\to\tau_f\ell_{crit}(\Omega_B\tau_f).
}
```

For the Gaussian information-band full template, the timing curvature `sigma_infinity(kappa)` increases strictly with `kappa`, giving the high-threshold limits

```math
\boxed{
L_\times\sim\sqrt2\mathcal C/\Omega_B
\quad(\Omega_B\tau_f\ll1),
}
```

and

```math
\boxed{
L_\times\to\mathcal C\tau_f
\quad(\Omega_B\tau_f\gg1).
}
```

**FIRST NONTRIVIAL CONSEQUENCE:** once the intrinsic detector is faster than the accessible electronics, making it still faster no longer changes the task boundary at leading order.

**NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum exists while accessible eventual SNR is artificially held fixed. A real optimum remains open because changing bandwidth changes eventual SNR in a fixed physical detector.

---

## 5. Current frontier

The next physical branch is to stop renormalizing `rho_infinity` when `Omega_B` changes.

The key unresolved question is whether the competing effects

```text
narrower bandwidth -> less timing-search complexity
narrower bandwidth -> potentially less available SNR
```

produce a genuine finite optimum readout bandwidth.

---

## 6. Scope boundary

Do not claim:

- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the Step-13 `ell~49` diagnostic is real;
- arbitrary low-pass filtering is a true information-band limitation;
- the Gaussian information weighting is a literal circuit transfer function;
- Rice is always accurate to the Step-16 level;
- the Step-18 illustrative bandwidth numbers are hardware predictions;
- a physical bandwidth optimum has already been found;
- crossover uniqueness;
- fixed physical bandwidth preserves every equal-`kappa` ordering;
- true-alignment crossing equals exact global rejection/localization;
- novelty.

Unknown amplitudes/phases, signal-dependent shot noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> If physical detector signal and noise amplitudes are held fixed while `Omega_B` is varied—so reducing bandwidth can reduce eventual SNR as well as timing-search burden—does their competition produce a genuine finite optimal readout bandwidth for unknown-time detection?
