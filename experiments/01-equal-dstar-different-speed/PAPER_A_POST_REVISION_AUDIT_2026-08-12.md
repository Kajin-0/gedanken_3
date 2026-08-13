# Paper A post-revision adversarial audit

**Date:** 2026-08-12  
**Manuscript:** `PAPER_A_DRAFT.md` on `agent/paper-a-guarantee-semantics`  
**Status:** BLOCKING SEMANTIC REPAIRS PASS / NO NEW FATAL MATHEMATICAL CONTRADICTION FOUND / TWO MINOR-MAJOR PRESENTATION ITEMS + QUANTITATIVE EXAMPLE + NOVELTY AUDIT REMAIN

---

## 1. Disposition

The revised manuscript is materially stronger than the pre-audit version.

The two previous submission-blocking claim-scope defects are now repaired:

```text
1. acquisition clock is operationally defined;
2. the true-alignment statistic is explicitly a sufficient guarantee for the full scan, not the exact scan-power theorem.
```

The central algebra remains consistent after the notation change from `T_D/X_D` to `T_G/X_G`.

No reason was found to reopen the Step-13–49 Gaussian-extremes closure branch.

The manuscript is still **not submission-ready**, but the remaining problems are now narrower:

```text
A. make explicit that q0 is used only for performance analysis, not by the receiver;
B. tighten the full-template threshold-limit presentation;
C. add/decide the final quantitative example strategy;
D. complete closest-prior-art / novelty audit.
```

---

## 2. Blocking issue A from the original review — PASS

The revised protocol explicitly states:

```text
arrival window: [0,L]
post-window integration: t
batch record length: L+t
```

and defines

```math
T_G=\text{minimum required post-window integration duration}.
```

The batch wall time is

```math
T_{wall}=L+T_G.
```

At fixed `L`,

```math
T_{wall,f}-T_{wall,s}
=T_{G,f}-T_{G,s}.
```

Thus the operational clock is exact and the detector ordering is unchanged.

The manuscript no longer presents `T_G` as an online stopping latency.

**Disposition: RESOLVED.**

---

## 3. Blocking issue B from the original review — PASS

The revised manuscript defines both

```math
P_{D,true}
=Pr[Y_x(q_0)>\Gamma]
```

and

```math
P_D^{scan}
=Pr[\sup_qY_x(q)>\Gamma].
```

It then uses the pathwise inclusion

```math
\{Y_x(q_0)>\Gamma\}
\subseteq
\{\sup_qY_x(q)>\Gamma\}
```

to obtain

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

The central theorem is now explicitly a **guarantee-time** theorem. It states no ordering theorem for the exact first solution of `P_D^scan=beta`.

A search of the revised manuscript found no residual `T_D` symbols. The remaining phrase “detection time” occurs only in explicit disclaimers about the stronger unproved full-scan quantity.

**Disposition: RESOLVED.**

---

## 4. Detector realization and normalization — PASS

The same optical event

```math
p(t)=e^{-bt}u(t)
```

passes through

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}
```

to give

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

`G_tau` is causal, proper, and stable for `b,tau>0`.

The output-noise convention is now explicit:

```math
E[n(t)n(t')]=N\delta(t-t'),
```

so

```math
\rho^2=(1/N)\int s^2dt
```

and

```math
A_\tau=2\rho_0\sqrt N/\tau^{3/2}
```

is internally consistent.

The text correctly labels equality of eventual matched-filter SNR as **event-specific**, not a universal equality of detector sensitivity.

**Disposition: RESOLVED.**

---

## 5. Proposition 1 strengthening — PASS with one presentation caveat

### 5.1 Large-search threshold divergence

The new proof uses

```math
R_\infty(y)=(1+y)e^{-y}\to0.
```

Choose a spacing such that every pair of distinct sampled points has covariance at most `epsilon`. Compare the sample vector to the equicorrelated Gaussian vector

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i.
```

The actual sample vector has no larger off-diagonal covariance, so Slepian gives

```math
Pr[max Z_i\le u]\le Pr[max Y_i\le u].
```

Since `max_i E_i->infinity`, `max_i Y_i->infinity` in probability; therefore the actual sampled maximum and continuous supremum also diverge. This is a valid route to

```math
\Gamma_\infty(\ell,\alpha)\to\infty.
```

No separate Pickands/Berman theorem is required for this limited conclusion.

### 5.2 Boundary divergence

For finite `x`,

```math
\eta(x)<1,
```

and the previously proved covariance ordering gives

```math
R_x(y)\le R_\infty(y).
```

Slepian therefore gives

```math
\Gamma(x,\ell,\alpha)
\ge\Gamma_\infty(\ell,\alpha).
```

At a continuous critical boundary,

```math
\Gamma_\infty(\ell_{crit},\alpha)
=\rho_0-z_\beta,
```

so every finite `x` has strict margin deficit. A bounded sequence of first-crossing times approaching the boundary would contradict continuity.

Thus `X_G->infinity` at `ell_crit` is correctly derived rather than separately assumed.

### 5.3 Remaining presentation caveat

The manuscript currently writes

```math
\Gamma_\infty(\ell,\alpha)
=\lim_{x\to\infty}\Gamma(x,\ell,\alpha)
```

and then treats `Gamma_infty` as the threshold of the full-template process with covariance `R_infty`.

This is natural and almost certainly harmless here, because the normalized truncated templates converge in `L2` to the full template and their autocovariances therefore converge uniformly in lag:

```math
|R_x(y)-R_\infty(y)|
\le 2\|\hat h_x-\hat h_\infty\|_2
\to0.
```

For submission, however, it would be cleaner either to:

```text
(a) define Gamma_infty directly as the quantile of the full-template Gaussian process and state that uniform covariance convergence gives Gamma_x->Gamma_infty under the same ordinary supremum-quantile continuity regularity; or
(b) add one sentence justifying the current limit notation.
```

This is a mathematical-presentation cleanup, not a discovered contradiction.

**Disposition: CORE STRENGTHENING PASSES / SMALL JUSTIFICATION STILL ADVISED.**

---

## 6. New clarity item — `q0` must be analysis-only

The revised manuscript correctly defines `q0` as the true event alignment, but a hostile reader could still ask whether the receiver is being given the true arrival time when evaluating `P_D,true`.

The intended logic is:

```text
receiver operation:
    scan every q in [0,ell];
    compare sup_q Y(q) with Gamma;

performance analysis only:
    identify the unknown true q0 after defining the generative hypothesis;
    evaluate the probability that Y(q0)>Gamma;
    use it as a sufficient lower bound on full-scan power.
```

The receiver never uses `q0` operationally.

Add one explicit sentence to Section III.C:

> `q0` is used only to analyze power under the signal-present hypothesis; it is not supplied to the receiver, which still scans the entire uncertainty interval.

**Disposition: EASY CLARITY FIX.**

---

## 7. Quantitative example — PARTIALLY IMPROVED, STILL OPEN FOR EXACT MODEL

New companion file:

`PAPER_A_FINITE_INFORMATION_COMPANION.md`.

It consolidates the already-validated smooth finite-information result:

```text
rho_0 = 6.2
alpha = 1e-6
beta = .90
r = 1.2
kappa = 8
```

with Palm-corrected crossover

```text
ell_s ~= .5721 +/- .001
```

versus continuous Rice

```text
ell_s^Rice ~= .57144,
```

a relative shift of only about `.12%`.

This is legitimate continuum robustness evidence and directly defeats the claim that the mechanism itself was manufactured by Step-13 independent/grid timing slots.

It is **not** the exact hard-window Paper A phase-boundary calculation.

The exact-hard-window numerical search should remain margin-first. Preliminary re-examination continues to suggest that the crossover tends to lie relatively near the fast guarantee-feasibility edge for the simple parameter sets tested. If that persists under controlled computation, the manuscript should report it rather than manufacture a “comfortable” example.

**Disposition: ROBUST COMPANION AVAILABLE / EXACT-MODEL EXAMPLE STILL OPEN.**

---

## 8. Novelty / prior-art risk — unchanged

The revised semantics make the possible contribution narrower and more defensible, but they do not establish priority.

Established neighboring ingredients remain:

```text
frequency-dependent pulse/energy detectivity;
detectivity-bandwidth products;
unknown-delay matched-filter false-alarm statistics;
correlator/template-bank global thresholds;
constant-false-alarm acquisition over a range window.
```

The candidate synthesis is now best stated as:

```text
same optical event
+ equal event-specific eventual matched-filter SNR
+ different detector time scales
+ unknown-arrival global-threshold batch scan
+ true-alignment sufficient guarantee
-> task-dependent guarantee-time ordering and feasibility reversal.
```

A deeper radar/sonar/ladar/synchronization citation-network search remains mandatory before any priority language.

---

## 9. Current referee-style disposition

> The major semantic defects of the original manuscript have been repaired. The acquisition clock is now explicit, and the paper no longer conflates true-alignment power with the exact signal-present scan power. The detector realization and noise normalization are also clearer, and two previously assumed asymptotic properties are now derived from the actual covariance structure. I find no new fatal mathematical contradiction in the revised core result. Before submission I would still request a brief justification connecting the finite-template threshold limit to the full-template Gaussian process, one sentence making clear that the true alignment is an analysis variable rather than receiver side information, a quantitative example strategy that does not reuse invalidated rough-grid results, and a deeper closest-prior-art audit.

### Disposition

```text
MAJOR-REVISION BLOCKERS: CLEARED
SUBMISSION READINESS: NOT YET
NEXT SCIENTIFIC TASK: QUANTITATIVE EXAMPLE + PRIOR-ART CLOSURE
GAUSSIAN-EXTREMES STEP-50 BRANCH: DO NOT REOPEN
```
