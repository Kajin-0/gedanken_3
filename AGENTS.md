# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. **Forty-nine logical steps completed. Mathematical closure branch HARD-STOPPED.** Step 49 executes the final target permitted by the Step-48 stopping rule: the exact finite-window covariance remainder beyond the mixed tangent. The exact covariance is simulated through an exact two-state linear-filter representation with delayed subtraction. Two independent `3000`-path runs (`6000` paired paths) comparing physical `dt=.001` with `dt/32` give exact-covariance relative grid loss `8.3682629e-4`, paired SE `6.8953e-6`, approximate normal 95% interval `[8.2331e-4,8.5034e-4]`. The exact pure-alpha1 benchmark for the same refinement is `8.3657896e-4`, leaving exact-covariance minus pure residual only `+2.47e-7 +/-6.90e-6` (1 SE). Higher-order finite-window covariance therefore does not cancel the rough-grid effect at order `1e-4`. The remaining publication-grade mapping from exact-covariance spectral intensity to the exact finite-search false-alarm event is no longer proportionate to the detector question. **Do not continue to Step 50 of this proof chain by default.** Next phase: consolidate detector/detection-theory core, separate mathematical companion material, and perform prior-art/novelty audit. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest/final closure step: `experiments/01-equal-dstar-different-speed/EXACT_COVARIANCE_GRID_TRANSFER_STOP_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/exact_covariance_grid_transfer.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/MIXED_TANGENT_GRID_TRANSFER_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target and exact blob SHA; never overwrite stale state; preserve failed/corrected paths. `CURRENT_STATE.md` and `PROGRESS_LOG.md` must move whenever the frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, PARTIAL CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, PAIRED NESTED-GRID DIAGNOSTIC, EXACT CANONICAL FINITE-GRID CORRECTION, EXACT CELLWISE BRIDGE DECOMPOSITION, PAIRED FINITE-LEVEL TRANSFER INTERVAL, PAIRED EXACT-COVARIANCE TRANSFER INTERVAL, HARD-GATE PASSED, HARD-STOP TRIGGERED, INVALIDATED, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–12 — detector result
Scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite records make phase/time placement operationally relevant. Unknown arrival introduces a global-false-alarm timing search. In the defined scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because speed changes both evidence accumulation and timing-search complexity. This is protocol/task specific, not a universal detector theorem.

### Steps 13–23
Hard-window scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** early `ell~49` crossover invalid. Genuine finite information bandwidth removes cusp; fixed physical signal/noise yields shallow finite bandwidth optimum. Rice upper switch near `130` is **INVALIDATED**; Palm preserves lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004`; original `.895` numerically fast-preferred.

### Steps 24–30
Finite bandwidth creates generalized Pickands variogram `t^2+sqrt(2)chi F_zeta`. Exact Brown-Resnick Slepian monotonicity does not imply physical-boundary monotonicity. **INVALIDATED INTERMEDIATE:** `.8131` coupling coefficient; corrected `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling uses `mu=sqrt(2)zeta chi^(1/3)`. Raw tiny-chi Step-27 values grid biased.

### Steps 31–41
Crossing moments work through `kappa_f~170`, then fail from micro-upcrossings; finite-amplitude excursion clusters replace them. Step 34 numerical high-band closure. Step 35 q-regularity; generic anti-concentration fails at rare-event scale. Step 36 cluster-strip measure. Steps 37–38 overshoot scale and exact Pickands cross-elasticity. Step 39 `R=N_a/N_tan~1.56`; small-amplitude remainder rejected. Step 40 Cameron-Martin threshold translation. Step 41 analytic inter-node q control. **INVALIDATED NUMERICAL VALUE:** tiny-q pair RMS `~5.4e-5`; corrected `~2.69e-5`.

### Steps 42–44
Raw inverse-duration Palm concentration is formally bounded but useless. Duration truncation at `L0=.02` separates bounded long contributions from analytically negligible short clusters. Step 44 pools `n=200000` and obtains pointwise finite-grid 95% bound `P_FA/alpha<.999957771`; remaining margin `.00004223 alpha`, so continuum bias dominates.

### Step 45
Witness retuning: `X=7.50` gains fast `~.001575 alpha` with slow lower `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower `~1.013`. **NEGATIVE RESULT:** retuning alone trades one knife-edge for another.

### Step 46
Nested `.001 -> .00025` correction `(5.301 +/-2.507)e-4 alpha`; five missed maxima account for `.00052149 alpha`, duration-only interpolation only `(8.61 +/-4.13)e-6 alpha`. **WORDING CORRECTION:** five-event result supports sign/scale consistency only, not precise coefficient verification.

### Step 47
Pure alpha1 Brownian finite-grid correction is explicit:

```math
H_1^delta=nu(sqrt(2delta)),
\qquad delta=a_Xu^2dt.
```

At `dt=.001`, exact canonical loss `1.0161323e-3`. Do not equate this with exact finite-u false-alarm ratio.

### Step 48
Mixed finite-u tangent has exact Brownian-bridge cell decomposition. Paired DY (`9000` paths, `Delta` vs `Delta/128`) gives mixed relative loss `9.3748649e-4`, paired SE `5.5146e-6`; pure-alpha1 loss `9.2635965e-4`; mixed-pure residual `-1.11268e-5 +/-5.5088e-6`. **HARD-GATE PASSED:** mixed finite-u transfer is `O(1e-5)` versus `O(9e-4)` grid loss.

### Step 49 — FINAL closure step
Exact finite-window covariance:

```math
R_x(y)=e^{-y}[I_2(x-y)+yI_1(x-y)]/D_x.
```

Exact filter-state construction:

```math
dU=-Udt+dW,
\qquad dV=(U-V)dt,
```

```math
Z_raw(t)=V(t)-e^{-x}[V(t-x)+xU(t-x)].
```

Two independent `3000`-path exact-covariance runs, `dt=.001` vs `dt/32`, pooled `6000` paths:

```text
H_exact^Delta          .5528146649
H_exact^(Delta/32)     .5532776622
relative loss          8.3682629e-4
paired SE              6.8953e-6
approx 95% interval    [8.2331e-4,8.5034e-4]
pure-alpha1 loss       8.3657896e-4
exact-minus-pure       +2.47e-7 +/-6.90e-6
```

**PAIRED EXACT-COVARIANCE TRANSFER INTERVAL:** higher-order covariance does not cancel the rough-grid effect at order `1e-4`.

**HARD-STOP TRIGGERED:** no Step 50 of the same closure chain by default.

---

## Active next phase
1. Consolidate detector/detection-theory result from Steps 01–12.
2. Separate Steps 13–49 as technical companion/appendix material.
3. Perform serious prior-art/novelty audit before novelty language.
4. Reopen mathematical closure only if external review identifies a decision-relevant gap.

## Scope boundary
Do not claim: faster universally better/worse; universal scalar replacement for `D*`; scanning protocol universally optimal; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 continuum certificate; Step-46 precise coefficient validation; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.
