# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-two logical steps completed. Step 22 maps the Palm-corrected finite-r bandwidth boundary and validates that the Step-19 finite bandwidth optimum survives continuous rare-event correction. The high-band slow-preferred region survives above a lifted boundary near `Lambda~0.91`; the old `Lambda=0.895` second crossing remains invalid. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/PALM_BOUNDARY_MAP_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/palm_boundary_map.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, cancellations, counterexamples, negative results, rejected shortcuts, failed numerical estimates, numerical validations, invalidations, asymptotic limits, refinements, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch exact current blob SHA before replacing existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and why they changed;
6. make narrow edits or explicit compact consolidations;
7. update `CURRENT_STATE.md` whenever scientific frontier changes;
8. append or explicitly consolidate `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides chat summaries, memory, and stale recovery notes.**

---

## 2. Epistemic labels

Use where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — construction sufficient to disprove implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens prior statement without erasing it.
- **NEGATIVE RESULT** — candidate effect tested and absent under stated model.
- **REJECTED SHORTCUT** — tempting inference shown not to answer actual question.
- **FAILED NUMERICAL ESTIMATE** — failed validation; never reuse as result.
- **NUMERICAL VALIDATION** — survived stated cross-checks within scope.
- **NUMERICAL COUNTEREXAMPLE** — converged numerical construction disproves broader implication within stated approximation/model.
- **INVALIDATED** — previously reported result fails stronger calculation.
- **ASYMPTOTIC** — controlled limiting regime only.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without separate prior-art audit.

---

## 3. Compact surviving chain

### Steps 01–04
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. Unknown timing alone does not break that ideal stationary-Gaussian equivalence, but finite windows can because magnitude `D*(f)` discards phase/temporal placement.

### Steps 05–12
Finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`. Define task-level detection time

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled scaled family, faster SNR accumulation can be offset by larger unknown-time search burden. **NEGATIVE RESULT:** no finite interior integration-duration optimum in that original family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like: `R_x(y)=1-a_x|y|+...`.

**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–15
A genuine finite timing-information bandwidth removes the cusp. Smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}
```

has controlled correlated-scan numerics.

### Step 16
Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

### Step 17
Rice accuracy is nonuniform toward the finite-window rough limit because `sigma_kappa^2~a_x kappa/sqrt(pi)`. Co-scaled extreme-speed-ratio crossover tends to fast full-template feasibility edge.

### Step 18
Common physical bandwidth with accessible SNR forced equal produces electronics-limited `~1/Omega_B` and detector-limited `~tau_f` regimes.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

### Step 19
Hold physical signal/noise fixed. Wide-band SNR loss is `O(1/kappa^2)` while timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r Rice bandwidth optimum exists. Initial Palm spot check preserved finite-vs-infinite ordering.

### Step 20
Finite-r `r=2`, fixed physical bandwidth, `Lambda=0.895`: converged Rice produced apparent `slow -> fast -> slow` with switches `25.4898402` and `130.1945883`.

### Step 21
Palm correction changes the topology:

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

survives, while the upper Rice switch near `130.19` is **INVALIDATED**. Palm checks at `130`, `160`, and `300` keep fast preferred for `Lambda=0.895`.

### Step 22 — current frontier
Map the Palm-corrected preference boundary by locally iterating

```math
\frac{\ell_{Rice,f}}{C_f}
=
r\frac{\ell_{Rice,s}}{C_s}.
```

For the same `r=2` calibration:

```text
kappa_f     Lambda_cross^Palm
~10         ~0.794
~20         ~0.891
21.7         0.895
30          ~0.9052
60          ~0.9098
100         ~0.9103
200         ~0.9099
```

**REFINEMENT:** the high-band slow-preferred region survives. Palm correction lifted the boundary above the old `Lambda=0.895` slice; it did not erase the slow-preferred side of task space.

Higher-statistics large-r full-template Palm scan:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** Step-19 finite bandwidth optimum survives Palm correction. It is shallower and broader than Rice predicted, with present localization `kappa_opt^Palm~50–65` and only `~0.3–0.4%` gain over infinite bandwidth for this calibration.

---

## 4. Current frontier

The topological questions from Step 21 are now answered within the mapped range:

- high-band slow-preferred tasks still exist at larger `Lambda`;
- the `Lambda=0.895` second crossing was spurious;
- the large-r finite-band optimum survives exact rare-event correction.

The unresolved problem is the analytic finite-r high-band boundary as `kappa_f->infinity`, where finite-hard-window roughness and smooth full-template convergence do not commute.

---

## 5. Scope boundary

Do not claim:

- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is an exact physical result;
- high-band slow-preferred region disappears after Palm correction;
- exact finite-r `kappa_f->infinity` boundary is known;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the high-band finite-r Palm boundary be derived asymptotically by matching the finite-hard-window rough excursion law to the smooth full-template limit, so that the `kappa_f -> infinity` boundary and the possibility of any additional reversals can be settled analytically rather than by Monte Carlo mapping?
