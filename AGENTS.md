# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-three logical steps completed. Step 23 derives the matched rough/smooth high-band scaling, introduces an exact occupation-time rare-event identity valid in the nondifferentiable `kappa=infinity` limit, and anchors the `r=2` infinite-band boundary near `Lambda~0.905`. The old `Lambda=0.895` slice is fast-preferred in the direct rough limit; the Step-20 upper Rice switch remains invalid. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/HIGH_BAND_MATCHED_ROUGH_SMOOTH_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/rough_limit_occupation_is.py`

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
Finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>`. Task-level detection time is

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled scaled family, faster SNR acquisition can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like:

```math
R_x(y)=1-a_x|y|+... .
```

**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}
```

has controlled correlated-scan numerics.

Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one shared physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible SNR equal produces electronics-limited and detector-limited regimes but **no** interior bandwidth optimum.

Holding physical signal/noise fixed instead gives wide-band SNR loss `O(1/kappa^2)` versus timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists; later Palm validation confirms survival beyond Rice.

### Steps 20–21
At finite `r=2`, fixed physical bandwidth and `Lambda=0.895`, converged Rice produced apparent `slow -> fast -> slow` switches at `25.4898402` and `130.1945883`.

Palm correction gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Palm checks at `130`, `160`, and `300` keep fast preferred for `Lambda=0.895`.

### Step 22
Palm boundary map:

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

**REFINEMENT:** high-band slow-preferred tasks survive above the lifted boundary.

Large-r full-template Palm scan has shallow finite optimum:

```text
kappa~50–65: ell_crit^Palm ~0.912
infinity:    ell_crit^Palm ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** finite bandwidth optimum survives Palm correction with only `~0.3–0.4%` gain.

### Step 23 — current frontier
Exact finite-hard-window covariance:

```math
R_x(y)=
\frac{(1+y)e^{-y}-e^{-2x+y}(2x^2-2xy+2x-y+1)}{\eta(x)}.
```

Local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

where

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

Matched rough/smooth coordinate:

```math
\boxed{\chi_x=a_xu/\sqrt{b_x}}.
```

On `q(u)=sqrt(2)/(u sqrt(b_x))`, the tangent process has stationary-increment variance

```math
\operatorname{Var}\eta_\chi(t)=t^2+\sqrt2\chi|t|.
```

A generalized Pickands constant `H_mix(chi)` bridges the smooth and rough high-threshold laws.

**REFINEMENT:** mathematical nondifferentiability at finite `x` need not mean distinct excursions are rough-controlled; when `chi<<1`, the cusp mainly produces micro-recrossings inside a smooth-core excursion.

Because the task has only `u~5`, leading high-threshold formulas retain percent-level finite-`u` error. Step 23 therefore introduces the exact occupation-time identity

```math
V_u=\int_0^\ell1_{z(t)>u}dt,
```

```math
\boxed{
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
}
```

This remains valid in the nondifferentiable rough limit where crossing counts diverge.

Direct `kappa=infinity` calculation for the Step-20 `r=2` calibration gives

```math
\boxed{
\Lambda_{cross}^{kappa=\infty}\approx0.905\pm0.004,
\qquad X_{cross}\approx7.75.
}
```

Representative `40000`-path equality check:

```text
X=7.7528, Lambda=0.90513
fast P_FA/alpha = 1.0049 +/-0.0080
slow P_FA/alpha = 0.9954 +/-0.0094
```

**REFINEMENT:** `Lambda=0.895` is fast-preferred in the direct infinite-band rough limit, so the invalid Step-20 upper reversal does not reappear asymptotically.

**OPEN:** a bounded re-entrant slow-preferred pocket at some untested very high finite bandwidth is not rigorously excluded because monotonic convergence of the finite-`kappa` boundary has not been proved.

---

## 4. Current frontier

Compute `H_mix(chi)` and the finite-threshold correction accurately enough to replace full-process rough-limit Monte Carlo with a deterministic boundary formula and determine whether any bounded high-band re-entrant preference pocket can exist.

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
- no bounded high-band re-entrant pocket can exist without monotonicity proof;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can `H_mix(chi)` and its finite-threshold correction be computed accurately enough to turn the Step-23 matched boundary into a deterministic formula and prove or exclude any bounded high-band re-entrant preference pocket without further full-process Monte Carlo?
