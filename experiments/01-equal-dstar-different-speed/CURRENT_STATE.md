# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 21:35 EDT  
**Status:** mathematical closure branch stopped after 49 logical steps; prior-art audit and paper architecture completed; **Paper A is drafted through Section IV and Section V is now drafted as a separate manuscript module. NOVELTY NOT ESTABLISHED.** Active core manuscript: `PAPER_A_DRAFT.md`. New discussion/conclusion module: `PAPER_A_SECTION_V.md`. `PAPER_A_DRAFT_OPENING.md` remains the earlier opening-draft milestone. Do not create Step 50 of the old Gaussian-extremes proof chain by default.

Read next:
1. `PAPER_A_DRAFT.md`
2. `PAPER_A_SECTION_V.md`
3. `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
4. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
5. `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
6. `TASK_REGIME_BOUNDARY_STEP.md`
7. `PROGRESS_LOG.md`

---

## Paper A — active manuscript track

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

The manuscript core contains:

- Abstract and Introduction with established `D*`, pulse-detection, sensitivity-bandwidth, and unknown-arrival matched-filter search results explicitly treated as prior art.
- Controlled equal-eventual-SNR family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
\qquad
\rho_{\tau,\infty}=\rho_0.
```

- Finite-time SNR accumulation

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
```

- Exact finite-record timing-scan covariance

```math
R_x(y)=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
\qquad 0\le y<x,
```

with `R_x(y)=0` for `y>=x` and

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

### Section III — dimensionless detection-time surface

The correlated-scan threshold is defined by

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
\qquad \ell=L/\tau.
```

The true-alignment margin is

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha),
```

and

```math
P_{D,\mathrm{true}}=\Phi[M].
```

Using the exact covariance ordering plus standard Gaussian comparison, `Gamma(x,ell,alpha)` is nonincreasing in `x`, while the SNR term is strictly increasing. Hence `M` is strictly increasing and

```math
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\{x>0:M(x)\ge\Phi^{-1}(\beta)\}
```

is an unambiguous first crossing whenever feasible.

The central exact scaling is

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
}
```

This preserves the Step-11 negative result: the reversal is not caused by one detector using a self-suboptimal integration duration; each member benefits monotonically from more observation time.

### Section IV — task boundary and crossover proof

For

```math
\tau_f<\tau_s,
\qquad r=\tau_s/\tau_f>1,
\qquad \ell=L/\tau_s,
```

```math
T_{D,f}=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}=r\tau_f X_D(\rho_0,\alpha,\beta,\ell),
```

and the exact preference boundary is

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

With

```math
c=\rho_0-\Phi^{-1}(\beta),
```

and

```math
\ell_{\mathrm{crit}}
=\sup\{\ell\ge0:\Gamma_\infty(\ell,\alpha)<c\},
```

physical feasibility scales as

```math
L_{\mathrm{crit}}(\tau)=\tau\ell_{\mathrm{crit}}.
```

The exact feasibility regimes are both-feasible / slow-only / neither; fast-only feasibility is excluded in this deliberately equal-eventual-SNR scaled family.

Under the explicitly stated assumptions of known-time feasibility, continuity away from singularities, unbounded large-search threshold growth, and divergence at the feasibility boundary:

- `L=0`: fast reaches the decision first;
- `L_{crit,f}=tau_f ell_crit < tau_s ell_crit=L_{crit,s}`;
- as `L -> L_crit,f^-`, `T_D,f -> infinity` while the slow detector remains strictly feasible;
- therefore at least one

```math
L_\times\in(0,L_{\mathrm{crit},f})
```

satisfies

```math
T_{D,f}(L_\times)=T_{D,s}(L_\times).
```

**No crossover uniqueness is claimed.** The theorem is task/protocol specific and does not establish a universal faster/slower ordering.

### Section V — interpretation, limitations, and detector-specification implications

New module: `PAPER_A_SECTION_V.md`.

The section fixes the practical interpretation:

```text
response time changes two things in the stated task:
1. how quickly signal evidence is accumulated;
2. the normalized size/correlation structure of the unknown-arrival search through L/tau.
```

The main conclusion is **not** to replace `D*` with a new detector-only sensitivity-speed scalar. The relevant ordering is a detector–task ordering. For the controlled model, the compact task descriptor is

```math
X_D(\rho_0,\alpha,\beta,L/\tau),
```

which explicitly contains arrival-time uncertainty and the global decision criterion.

Section V distinguishes **device characterization** from **task qualification**: device metrics such as responsivity, noise, detectivity, bandwidth, and response time remain useful, but they do not by themselves rank devices for every finite-time unknown-arrival decision problem.

Scope restrictions are explicit: linear time-scaled family, additive stationary Gaussian output noise, equal eventual matched-filter SNR, arrival time as the nuisance parameter, and a true-alignment detection criterion with a global noise-only scan threshold. No claim is made for Bayesian/minimax/sequential receivers, unknown amplitude/phase, nonlinear response, saturation, dead time, nonstationarity, or arbitrary practical detectors.

The concluding detector-facing statement is:

> **Detector specifications rank devices only relative to the task for which the ranking is being made. When arrival time is uncertain, response time affects both signal accumulation and the statistical size of the timing search.**

Within the controlled family, that coupling is sufficient to reverse the fast/slow detection-time ordering despite equal eventual matched-filter sensitivity.

---

## Prior-art status

Focused audit remains `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

Established ingredients are not novelty targets:

- pulse/energy detectivity from frequency-dependent detector sensitivity;
- sensitivity-speed / detectivity-bandwidth comparison;
- unknown-arrival matched-filter search penalties controlled by correlated peak statistics/template correlation;
- all-pass magnitude preservation with altered phase/dispersion.

Only the complete equal-eventual-SNR photodetector task-reversal synthesis remains a **POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED**.

---

## Technical mathematical companion — Steps 13–49

The mathematical closure branch remains hard-stopped and separate. It is robustness/stress-test material, not the main detector proof.

Critical preserved corrections/negative results include:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** rough/smoothed coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 values were grid biased.
- Crossing moments fail from micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 finds `R=N_a/N_tan~1.56`; finite-u correction is not a small-amplitude remainder.
- Step 40 gives Cameron-Martin exact-event threshold translation.
- Step 41 replaces empirical q interpolation with analytic Gaussian-process control.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic value `~2.69e-5`.
- Step 44 gives a genuine pointwise finite-grid 95% bound `P_FA/alpha<.999957771`, but with only `.00004223 alpha` margin.
- Step 46 identifies missed between-sample maxima as the dominant continuum-grid error; its five-event coefficient supports sign/scale consistency only, not precise validation.
- Step 47 gives the exact pure-alpha1 discrete Pickands correction.
- Steps 48–49 show mixed-tangent and exact-covariance transfer corrections are only `O(1e-5)` relative to an `O(1e-3)` grid effect.
- **HARD-STOP:** do not reopen this chain unless external review identifies a decision-relevant gap.

---

## Active next drafting step

Stay inside **Paper A**.

The detector-facing narrative is now drafted in modular form through Section V. The next logical action is to **merge Section V into `PAPER_A_DRAFT.md` and perform a manuscript-level consistency/editing pass**: remove duplication, standardize notation and terminology, check theorem assumptions against the abstract/conclusion, and ensure the references and novelty language are internally consistent. Do not add new mathematical claims or numerical phase-diagram claims during that pass.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can Section V now be merged into the active manuscript and the full Paper A draft receive a consistency/compression pass without broadening the theorem or reopening the mathematical companion?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival search penalties as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.