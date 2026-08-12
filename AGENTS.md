# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Forty-eight logical steps completed. A hard stopping rule now applies: no new conceptual branch unless it directly reduces the remaining exact-process discretization remainder. Step 48 passes that gate. The finite-u mixed Brownian-parabola tangent has an exact cellwise Brownian-bridge decomposition; at `X=7.16`, physical `dt=.001` maps to tangent `Delta=.003506747946` and pure-rough canonical `delta=1.5225630594e-6`. A paired generalized Dieker-Yakir calculation on `9000` paths comparing `Delta` to `Delta/128` gives mixed relative loss `9.3748649e-4` with paired SE `5.5146e-6`; the exact pure-alpha=1 finite-level loss is `9.2635965e-4`. The mixed-to-pure transfer residual is only `-1.11268e-5` with paired SE `5.5088e-6`. This is a controlled Monte Carlo diagnostic, not a theorem. The next and only allowed target is the exact finite-window process remainder beyond the mixed tangent; if that cannot be bounded usefully, stop the mathematical closure branch and consolidate. No universal scalar replacement metric and no novelty claim.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. latest step: `experiments/01-equal-dstar-different-speed/MIXED_TANGENT_GRID_TRANSFER_STEP.md`
4. latest helper: `experiments/01-equal-dstar-different-speed/numerics/mixed_tangent_grid_transfer.py`
5. preceding step: `experiments/01-equal-dstar-different-speed/EXACT_ALPHA1_DISCRETE_PICKANDS_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol
Before material writes: fetch live target; fetch exact blob SHA before replacement; never overwrite stale state; preserve failed/corrected paths; update `CURRENT_STATE.md` and `PROGRESS_LOG.md` whenever the frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, NUMERICAL CLOSURE, PARTIAL CERTIFICATE, NUMERICAL ENDPOINT CERTIFICATE, PAIRED NUMERICAL INTERVAL CLOSURE, TAIL-SENSITIVE ENVELOPE, EXACT VARIOGRAM ORDERING, ANALYTIC INTER-NODE ENVELOPE, RIGOROUS FINITE-GRID CONCENTRATION TEST, SHORT-CLUSTER GAUSSIAN ENVELOPE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, PAIRED NUMERICAL WITNESS SCAN, PAIRED NESTED-GRID DIAGNOSTIC, EXACT CANONICAL FINITE-GRID CORRECTION, EXACT CELLWISE BRIDGE DECOMPOSITION, PAIRED FINITE-LEVEL TRANSFER INTERVAL, HARD-GATE PASSED, ASYMPTOTIC, INVALIDATED, INVALIDATED INTERMEDIATE, INVALIDATED NUMERICAL VALUE, INVALIDATED NUMERICAL INTERPRETATION, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is allowed only for the explicitly model-reduced canonical crossover function.

---

## Compact surviving chain

### Steps 01–12 — detector result
Scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite records make phase/time placement operationally relevant. Unknown arrival introduces a global-false-alarm timing search. In the defined scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because speed changes both evidence accumulation and timing-search complexity. This is protocol/task specific, not a universal detector theorem.

### Steps 13–23
Hard-window scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** early `ell~49` crossover invalid. Genuine finite information bandwidth removes the cusp; fixed physical signal/noise gives a shallow finite bandwidth optimum. Rice upper switch near `130` is **INVALIDATED**; Palm preserves only lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004` leaves original `.895` numerically fast-preferred.

### Steps 24–30
Finite bandwidth creates generalized Pickands variogram `t^2+sqrt(2)chi F_zeta`. Exact Brown-Resnick Slepian monotonicity does not imply physical-boundary monotonicity. **INVALIDATED INTERMEDIATE:** `.8131` coupling coefficient; corrected `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling uses `mu=sqrt(2)zeta chi^(1/3)`. Raw tiny-chi Step-27 values were grid biased.

### Steps 31–41
Crossing moments work through `kappa_f~170`, then fail from micro-upcrossings; finite-amplitude excursion clusters replace them. Step 34 gives paired numerical high-band closure. Step 35 proves `L2` q-regularity; generic anti-concentration fails at rare-event scale. Step 36 gives fixed-cluster strip intensity. Steps 37–38 derive overshoot scale and exact Pickands cross-elasticity. Step 39 finds `R=N_a/N_tan~1.56`; small-amplitude remainder rejected. Step 40 gives Cameron-Martin threshold translation. Step 41 gives analytic inter-node q control. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.

### Steps 42–44
Raw inverse-duration Palm concentration is formally bounded but useless. Duration truncation at `L0=.02` separates long bounded weights from analytically negligible short clusters. Step 44 pools `n=200000` and gives genuine pointwise finite-grid 95% upper bound `P_FA/alpha<.999957771`; margin only `.00004223 alpha`, so continuum bias dominates.

### Step 45
Witness scan: `X=7.50` gains fast `~.001575 alpha` with slow lower `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower falls `~1.013`. **NEGATIVE RESULT:** witness retuning alone trades one knife-edge for another.

### Step 46
Nested grids show `.001 -> .00025` correction `(5.301 +/-2.507)e-4 alpha`; five missed threshold maxima contribute `.00052149 alpha`, duration-only interpolation only `(8.61 +/-4.13)e-6 alpha`. Rough cusp gives Brownian `sqrt(dt)` continuity scale. **WORDING CORRECTION:** because this estimate is driven by five events with ~47% relative SE, describe it only as statistically consistent in sign/scale with theory, not as precise coefficient verification.

### Step 47
Pure alpha=1 Brownian finite-grid correction is explicit:

```math
H_1^delta=nu(sqrt(2delta)),
\qquad delta=a_Xu^2dt.
```

At `dt=.001`, canonical loss `1.0161323e-3`. **EXACT CANONICAL FINITE-GRID CORRECTION.** Do not equate with finite-u physical ratio. Earlier phrase "essentially exact empirical agreement" is withdrawn.

### Step 48 — current frontier
Finite-u mixed tangent:

```math
W_chi(t)=sqrt(2)Zt-t^2+2^(3/4)sqrt(chi)B(t)-sqrt(2)chi|t|.
```

At `X=7.16`:

```text
chi   = 3.0701227479e-4
Delta = 3.506747946e-3
delta = 1.5225630594e-6
```

Exact cellwise decomposition:

```math
W(t_k+theta Delta)
=(1-theta)W_k+theta W_{k+1}
+sqrt(2delta) B_bridge(theta)
+Delta^2 theta(1-theta),
```

with parabolic bulge `<=3.07432e-6`.

**REJECTED SHORTCUT:** Slepian variogram ordering does not order `H^Delta/H^0`.

Paired DY, grids `Delta` and `Delta/128`, 9000 paths:

```text
mixed relative loss          9.3748649e-4
paired SE                    5.5146e-6
exact pure-alpha=1 loss      9.2635965e-4
transfer residual           -1.11268e-5
paired SE residual           5.5088e-6
approx 95% residual interval [-2.1924e-5,-3.30e-7]
```

**PAIRED FINITE-LEVEL TRANSFER INTERVAL / HARD-GATE PASSED:** finite-u Brownian-parabola transfer is `O(1e-5)` at the working parameters, much smaller than the resolved `O(9e-4)` grid loss. This is not theorem-level or distribution-free. Nested-grid monotonicity means the mixed-tangent continuum loss is at least the resolved coarse-to-fine loss.

---

## Hard stopping rule from Step 48 onward
No new conceptual branches. The only legitimate next task is the higher-order exact-process remainder beyond the mixed tangent. It must either:

1. produce an explicit covariance/process bracket;
2. produce a controlled numerical interval strong enough to settle the witness;
3. fail clearly, in which case stop the mathematical closure branch and consolidate the detector result.

### Single next question — DO NOT ANSWER UNTIL PROMPTED
> Can the exact finite-window covariance be bracketed around the mixed tangent on the `Delta/128` extremal neighborhood strongly enough to bound the remaining exact-process remainder, or does that final remainder fail the hard stopping test and force consolidation?

---

## Scope boundary
Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; scanning protocol universally optimal; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 tiny-chi values as continuum truth; Step-31 empirical fit exact/required; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; `L_R=.8` analytic; numerical covariance constants as interval-certified; raw empirical Bernstein certifies Step-33; `L0=.02` optimal; Step-44 as continuum certificate; Step-45 witness differences as formal confidence statements; Step-46 coefficient precisely verified; Step-47 canonical ratio as the finite-u physical ratio; Step-48 paired interval as theorem-level/distribution-free; `X=7.16` mathematically optimal; simultaneous 95% coverage across q nodes; no re-entrant pocket for other task parameters; uniqueness of bandwidth optimum; illustrative hardware interpretations; novelty.