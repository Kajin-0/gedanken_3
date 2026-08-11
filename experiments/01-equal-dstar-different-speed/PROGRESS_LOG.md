# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 18:54 EDT:** compact chronology preserving every consequential result, correction, failed shortcut, invalidation, numerical validation, asymptotic qualification, and stopping point. Full derivations live in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude `D*(f)` discards phase/temporal placement; causal all-pass construction removes the pure-delay loophole.

## Steps 05–12 — finite-record SNR, deadline detection, and task boundary
Derived `rho_t^2=<s_t,C_t^-1s_t>`, Gaussian deadline detection, and task-level `T_D(alpha,beta,L)`. Unknown timing raises a global threshold governed by timing-scan covariance rather than digital sample count. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

## Step 13 — rough finite-window obstruction
`R_x(y)=1-a_x|y|+...`; the ideal-white-noise finite hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid `ell~49` crossover is invalid.

## Steps 14–15 — genuine finite timing-information bandwidth
**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily a true information-band limit because whitening can undo it. Smooth Gaussian information weighting removes the cusp and gives controlled correlated-scan numerics.

## Step 16 — exact smooth Palm rare-event identity

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

## Step 17 — nonuniform Rice limit and extreme speed ratio
For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform as bandwidth grows. Co-scaled large-r crossover tends to the fast full-template feasibility edge.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives wide-band SNR loss `O(1/kappa^2)` but timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** large-r Rice unknown-time objective has a finite bandwidth optimum. Palm validation later confirms the optimum survives exact rare-event correction.

## Step 20 — finite-r Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged finite-duration Rice gave apparent switches at `25.4898402` and `130.1945883`, i.e. apparent `slow -> fast -> slow`.

## Step 21 — Palm correction changes topology
Use `u_avail=rho(x)-Phi^-1(beta)` and test `P_FA^Palm(u_avail)<=alpha` directly.

- lower switch survives at `kappa_f~21.7 +/-0.3`;
- **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch;
- Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`;
- cause: nonuniform Rice micro-upcrossing overcount, strongest for the shorter slow-detector finite window.

## Step 22 — 18:42 EDT — Palm boundary map and survival of finite optimum
Representative finite-r Palm boundary:

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

**REFINEMENT:** high-band slow-preferred tasks survive; Palm lifts the boundary above the old `Lambda=0.895` slice rather than eliminating the slow-preferred region.

Higher-statistics large-r full-template Palm scan:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** finite bandwidth optimum survives Palm correction. It is broad (`kappa~50–65`) and shallow (`~0.3–0.4%` gain over infinite bandwidth).

Full derivation: `PALM_BOUNDARY_MAP_STEP.md`.  
Code: `numerics/palm_boundary_map.py`.

## Step 23 — 18:54 EDT — matched rough/smooth high-band limit
Derived the exact unregularized finite-window covariance

```math
R_x(y)=
\frac{(1+y)e^{-y}-e^{-2x+y}(2x^2-2xy+2x-y+1)}{\eta(x)},
\qquad 0\le y<x.
```

Its local expansion is

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

with

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

At threshold `u`, rough and smooth high-excursion geometry is organized by

```math
\boxed{\chi_x=a_xu/\sqrt{b_x}}.
```

On scale `q(u)=sqrt(2)/(u sqrt(b_x))`, the matched tangent process has stationary increments with variance

```math
\operatorname{Var}\eta_\chi(t)=t^2+\sqrt2\chi|t|.
```

A generalized Pickands constant `H_mix(chi)` bridges `H_mix(0)=1/sqrt(pi)` (smooth) to `H_mix(chi)~sqrt(2)chi` (rough).

**REFINEMENT:** finite-window nondifferentiability does not imply distinct high excursions are rough-controlled. For `chi<<1`, the cusp mainly creates micro-recrossings within a smooth-core excursion.

At the present `u~5`, leading high-threshold asymptotics retain percent-level Mills-ratio error, too large to settle the boundary alone.

Derived an exact occupation-time identity for the nondifferentiable rough process. If

```math
V_u=\int_0^\ell1_{z(t)>u}dt
```

and a uniformly selected search time is conditioned to lie above `u`, then

```math
\boxed{
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
}
```

This avoids divergent upcrossing counts entirely.

Direct `kappa=infinity` occupation-time importance sampling for the Step-20 `r=2` calibration gives

```math
\boxed{
\Lambda_{cross}^{kappa=\infty}\approx0.905\pm0.004,
\qquad X_{cross}\approx7.75.
}
```

At representative `X=7.7528`, `Lambda=0.90513`, a `40000`-path run gives

```text
fast P_FA/alpha = 1.0049 +/-0.0080
slow P_FA/alpha = 0.9954 +/-0.0094.
```

**REFINEMENT:** the old `Lambda=0.895` slice is fast-preferred in the direct infinite-band rough limit. The Step-20 second reversal therefore does not reappear asymptotically.

**OPEN:** no proof yet excludes a bounded re-entrant slow-preferred pocket at some untested very high finite bandwidth; monotonic convergence of the finite-`kappa` boundary is not established.

Full derivation: `HIGH_BAND_MATCHED_ROUGH_SMOOTH_STEP.md`.  
Code: `numerics/rough_limit_occupation_is.py`.

---

## Current stopping point

The noncommuting high-band limits are now organized by the matched coordinate `chi_x`, and the finite-r `kappa=infinity` boundary is directly anchored without upcrossing counts.

### Single natural next question

> Can `H_mix(chi)` and its finite-threshold correction be computed accurately enough to turn the Step-23 matched boundary into a deterministic formula and prove or exclude any bounded high-band re-entrant preference pocket without further full-process Monte Carlo?
