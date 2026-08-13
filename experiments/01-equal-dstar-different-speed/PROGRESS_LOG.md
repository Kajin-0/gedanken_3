# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 20:52 EDT:** mathematical closure stopped after Step 49; detector-facing prior-art audit and short-paper architecture completed; Paper A opening draft written. Novelty is not established. Full derivations remain in dedicated step files.

---

## Steps 01–12 — detector/detection-theory core

Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite windows make phase/time placement relevant. Unknown arrival introduces global false-alarm timing-search complexity. In the defined continuous scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because temporal compression changes both early evidence accumulation and timing-search correlation length. This is protocol/task specific, not a universal detector theorem.

Exact detector-facing scaling:

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact task boundary is

```math
B_r(\ell)=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions: fast wins at known time; approaching the fast feasibility boundary, fast detection time diverges while slow remains feasible; therefore at least one finite fast-to-slow crossover exists. Slow-only feasibility is possible, fast-only feasibility is excluded in this equal-eventual-SNR scaled family, and uniqueness is not established.

## Steps 13–23 — continuous search / bandwidth

Hard-window scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** early `ell~49` crossover invalid. Genuine finite information bandwidth removes the cusp; fixed physical signal/noise gives a shallow finite bandwidth optimum. Rice upper switch near `130` is **INVALIDATED**; Palm preserves only lower switch `~21.7 +/- .3`. Rough endpoint `Lambda_cross^infinity~.905 +/- .004` leaves original `.895` numerically fast-preferred.

## Steps 24–30 — generalized Pickands structure

Finite bandwidth gives generalized Pickands variogram `t^2+sqrt(2)chi F_zeta`. Exact Brown-Resnick Slepian monotonicity does not imply physical-boundary monotonicity. **INVALIDATED INTERMEDIATE:** `.8131` coupling coefficient; corrected `.8906480701 sqrt(chi/zeta)`. Brownian-parabola scaling uses `mu=sqrt(2)zeta chi^(1/3)`. Raw tiny-chi Step-27 values were grid biased and invalidated as continuum values.

## Steps 31–41 — finite-u closure machinery

Crossing moments work through `kappa_f~170`, then fail from micro-upcrossings; finite-amplitude excursion clusters replace them. Step 34 gives paired numerical high-band closure. Step 35 proves `L2` q-regularity; generic anti-concentration is too coarse. Step 36 gives rare-event cluster-strip control. Steps 37–38 derive overshoot scale and exact Pickands cross-elasticity. Step 39 finds `R=N_a/N_tan~1.56`, rejecting a small-amplitude remainder. Step 40 gives Cameron-Martin exact-event threshold translation. Step 41 gives analytic inter-node q control. **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.

## Steps 42–44 — finite-sample endpoint statistics

Raw inverse-duration Palm concentration is formally bounded but useless because support is huge. Duration truncation at `L0=.02` separates bounded long weights from analytically negligible short clusters. Step 44 pools `n=200000` and gives genuine pointwise finite-grid 95% upper bound

```text
P_FA/alpha < .999957771
```

with only `.00004223 alpha` margin. Continuum timing-grid bias becomes dominant.

## Step 45 — witness-time test

`X=7.50` gains fast `~.001575 alpha` while slow lower remains `~1.089`; `X=7.70` gains `~.002006 alpha` but slow lower falls to `~1.013`. **NEGATIVE RESULT:** witness retuning alone trades one knife-edge for another.

## Step 46 — rough-grid mechanism

Nested `.001,.0005,.00025` grids, 24k paired paths give coarse-to-fine correction `(5.301 +/-2.507)e-4 alpha`. Five missed fine-grid successes contribute `.00052149 alpha`; duration-only interpolation contributes only `(8.61 +/-4.13)e-6 alpha`. **WORDING CORRECTION:** the five-event result supports sign/scale consistency only, not precise coefficient verification.

## Step 47 — exact canonical alpha=1 correction

For pure rough tangent `W(s)=sqrt(2)B(s)-|s|`, `delta=a_Xu^2dt` and

```math
H_1^delta=nu(sqrt(2delta)).
```

At `dt=.001`, exact canonical loss is `1.0161323e-3`. **EXACT CANONICAL FINITE-GRID CORRECTION.** Do not equate this with the exact finite-u physical false-alarm ratio.

## Step 48 — hard-gated mixed-tangent transfer

Paired DY on `9000` paths, `Delta` versus `Delta/128`, gives mixed relative loss `9.3748649e-4`, paired SE `5.5146e-6`; pure alpha=1 loss `9.2635965e-4`; mixed-pure residual `-1.11268e-5 +/-5.5088e-6`. **HARD-GATE PASSED:** finite-u Brownian-parabola transfer is `O(1e-5)`, much smaller than the `O(9e-4)` grid effect.

## Step 49 — exact finite-window covariance transfer / HARD STOP

The exact finite-window covariance is simulated through an exact two-state filter representation. Two independent `3000`-path runs, physical `dt=.001` versus `dt/32`, pooled `6000` paired paths:

```text
H_exact^Delta          .5528146649
H_exact^(Delta/32)     .5532776622
relative loss          8.3682629e-4
paired SE              6.8953e-6
approx 95% interval    [8.2331e-4,8.5034e-4]
pure-alpha1 loss       8.3657896e-4
exact-minus-pure       +2.47e-7 +/-6.90e-6
```

**PAIRED EXACT-COVARIANCE TRANSFER INTERVAL:** higher-order finite-window covariance terms do not generate an order-`1e-4` cancellation of the discretization effect.

**HARD-STOP TRIGGERED:** the remaining publication-grade theorem connecting exact-covariance spectral intensity to the exact finite-search false-alarm event is no longer proportionate to the detector question. Stop this mathematical closure branch.

---

# Detector-facing prior-art audit — 20:31 EDT

Full audit: `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

Direct prior art establishes pulse/energy detectivity from frequency-dependent response, sensitivity-speed/bandwidth joint benchmarking, unknown-arrival matched-filter search penalties controlled by correlated peak statistics/template autocorrelation, and standard all-pass magnitude preservation with altered phase/dispersion.

No direct hit was found in the focused audit for the complete equal-eventual-SNR detector construction leading to an explicit fast/slow task reversal. Disposition remains

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

# Detector-facing paper architecture — 20:42 EDT

Full architecture: `PAPER_ARCHITECTURE_TASK_REVERSAL.md`.

**CONSOLIDATION RESULT:** the main detector paper contains only five conceptual sections: prior-art framing, controlled equal-eventual-SNR family, dimensionless detection-time surface, task-reversal theorem/feasibility partition, and interpretation/limits. The mathematical closure chain is moved to a companion track.

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

Main equations:

```math
T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau)
```

and

```math
B_r(\ell)=X_D(r\ell)-rX_D(\ell)=0.
```

No crossover uniqueness, universal faster/slower ordering, universal scan optimality, or novelty is claimed.

---

# Paper A opening manuscript draft — 20:52 EDT

New active manuscript: `PAPER_A_DRAFT_OPENING.md`.

Drafted in publication style:

1. working title;
2. abstract;
3. central Proposition 1 with continuity/divergence assumptions stated inside the proposition;
4. full Introduction;
5. Section II.A equal-eventual-SNR time-scaled template;
6. Section II.B exact finite-record timing-scan covariance and physical scaling;
7. references [1]–[7] drawn from the prior-art audit.

Key rhetorical correction: the manuscript immediately concedes that scalar-`D*` pulse limitations, sensitivity-bandwidth tradeoffs, and unknown-arrival search penalties are established. The paper's actual question is isolated by enforcing

```math
\rho_{\tau,\infty}=\rho_0
```

for every detector time scale.

The opening derives

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
```

and

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau),
```

making the two competing effects explicit: faster evidence accumulation and a larger normalized timing search.

No Pickands, Palm, Rice, high-band endpoint certificate, or Step-13–49 numerical closure material appears in the draft.

---

## Current stopping point

Stay inside **Paper A**. Do not continue Step 50 of the mathematical proof chain.

### Single next question

> Can Sections III and IV now be drafted in publication style, carrying `PAPER_A_DRAFT_OPENING.md` through the dimensionless detection-time surface and the fast/slow task-reversal proof without reintroducing the mathematical companion?
