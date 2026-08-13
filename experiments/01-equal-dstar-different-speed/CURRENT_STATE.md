# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 21:03 EDT  
**Status:** mathematical closure branch stopped after 49 logical steps; prior-art audit and paper architecture completed; **Paper A is now drafted through Section IV, including the dimensionless detection-time surface and the fast/slow crossover proof. NOVELTY NOT ESTABLISHED.** The active manuscript is now `PAPER_A_DRAFT.md`. `PAPER_A_DRAFT_OPENING.md` is retained as the earlier opening-draft milestone. Do not create Step 50 of the old Gaussian-extremes proof chain by default.

Read next:
1. `PAPER_A_DRAFT.md`
2. `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
3. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
4. `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
5. `TASK_REGIME_BOUNDARY_STEP.md`
6. `PROGRESS_LOG.md`

---

## Paper A — active manuscript track

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

The manuscript now contains:

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

with `R_x(y)=0` for `y>=x` and physical scaling

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

### Section III — dimensionless detection-time surface

The global correlated-scan threshold is defined directly by

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
\qquad \ell=L/\tau.
```

The true-alignment decision margin is

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha),
```

and

```math
P_{D,\mathrm{true}}=\Phi[M].
```

Using the exact covariance ordering from Step 11 plus standard Gaussian comparison, `Gamma(x,ell,alpha)` is nonincreasing in `x`, while the SNR term is strictly increasing. Hence `M` is strictly increasing and the first-crossing time is unambiguous:

```math
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\{x>0:M(x;\ell,\rho_0,\alpha)\ge\Phi^{-1}(\beta)\}.
```

The central exact task scaling is

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
}
```

This also preserves the Step-11 negative result: the reversal is not caused by one detector using a self-suboptimal integration duration; each detector individually benefits from more observation time.

### Section IV — task boundary and crossover proof

For two members with

```math
\tau_f<\tau_s,
\qquad r=\tau_s/\tau_f>1,
\qquad \ell=L/\tau_s,
```

the exact physical detection times are

```math
T_{D,f}=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}=r\tau_f X_D(\rho_0,\alpha,\beta,\ell),
```

and their task boundary is

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

Let

```math
c=\rho_0-\Phi^{-1}(\beta),
```

and

```math
\ell_{\mathrm{crit}}
=\sup\{\ell\ge0:\Gamma_\infty(\ell,\alpha)<c\}.
```

Then

```math
L_{\mathrm{crit}}(\tau)=\tau\ell_{\mathrm{crit}}.
```

Since `Gamma_infty` is nondecreasing with search length, the exact feasibility partition is:

```text
both feasible:
    c > Gamma_infty(r ell, alpha)

slow only:
    Gamma_infty(ell, alpha) < c <= Gamma_infty(r ell, alpha)

neither feasible:
    c <= Gamma_infty(ell, alpha)
```

Fast-only feasibility is excluded in this deliberately equal-eventual-SNR scaled family.

Under the explicitly stated assumptions that known-time operation is feasible, `X_D` is continuous away from feasibility singularities, `Gamma_infty` grows without bound with search length, and `X_D` diverges on approach to the feasibility boundary:

- at `L=0`, both detectors solve the same dimensionless task and `T_D,f<T_D,s` because `tau_f<tau_s`;
- `L_crit,f=tau_f ell_crit < tau_s ell_crit=L_crit,s`;
- as `L -> L_crit,f^-`, `T_D,f -> infinity` while the slow detector remains strictly feasible;
- therefore continuity guarantees at least one

```math
L_\times\in(0,L_{\mathrm{crit},f})
```

with

```math
T_{D,f}(L_\times)=T_{D,s}(L_\times).
```

**No crossover uniqueness is claimed.** The theorem is task/protocol specific and does not establish a universal faster/slower ordering.

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
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.
- Step 44 gives a genuine pointwise finite-grid 95% bound `P_FA/alpha<.999957771`, but with only `.00004223 alpha` margin.
- Step 46 identifies missed between-sample maxima as the dominant continuum-grid error; its five-event coefficient supports sign/scale consistency only, not precise validation.
- Step 47 gives the exact pure-alpha1 discrete Pickands correction.
- Steps 48–49 show mixed-tangent and exact-covariance transfer corrections are only `O(1e-5)` relative to an `O(1e-3)` grid effect.
- **HARD-STOP:** do not reopen this chain unless external review identifies a decision-relevant gap.

---

## Active next drafting step

Stay inside **Paper A**.

The next logical action is to draft **Section V only**: interpretation, limitations, and detector-specification implications, then perform a manuscript-level consistency pass. Do not add numerical phase-diagram claims or reopen specialized closure mathematics unless separately justified.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can Section V now be drafted to finish the detector-facing narrative, with the practical implication stated strongly but without broadening the theorem beyond the defined task/protocol?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival search penalties as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.