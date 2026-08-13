# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 21:47 EDT  
**Status:** mathematical closure branch hard-stopped after 49 logical steps; prior-art audit completed; paper architecture fixed; **Paper A is now merged into one complete detector-facing manuscript and has received a full consistency/compression pass. NOVELTY NOT ESTABLISHED.** Active manuscript: `PAPER_A_DRAFT.md`. `PAPER_A_SECTION_V.md` and `PAPER_A_DRAFT_OPENING.md` are retained only as drafting milestones. Do not create Step 50 of the old Gaussian-extremes chain by default.

Read next:
1. `PAPER_A_DRAFT.md`
2. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
3. `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
4. `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
5. `TASK_REGIME_BOUNDARY_STEP.md`
6. `PROGRESS_LOG.md`

---

## Paper A — authoritative manuscript

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

`PAPER_A_DRAFT.md` now contains the complete five-section paper plus references.

### Central controlled family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
\qquad
\rho_{\tau,\infty}=\rho_0.
```

Finite-time accumulated SNR:

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
\qquad x=t/\tau.
```

Exact finite-record timing-scan covariance:

```math
R_x(y)=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
\qquad 0\le y<x,
```

with `R_x(y)=0` for `y>=x` and

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

### Dimensionless detection-time surface

Define

```math
\ell=L/\tau
```

and the global correlated-scan threshold by

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha.
```

The true-alignment decision margin is

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
```

Covariance ordering plus standard Gaussian comparison gives

```math
x_2>x_1
\Rightarrow
\Gamma(x_2,\ell,\alpha)\le\Gamma(x_1,\ell,\alpha),
```

so `M` is strictly increasing. Hence

```math
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\{x>0:M(x)\ge\Phi^{-1}(\beta)\}
```

is unambiguous whenever feasible, and

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
}
```

The reversal is therefore a cross-detector scaling effect, not a self-suboptimal integration-time effect.

### Fast/slow task boundary

For

```math
\tau_f<\tau_s,
\qquad r=\tau_s/\tau_f>1,
\qquad \ell=L/\tau_s,
```

```math
T_{D,f}=\tau_fX_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}=r\tau_fX_D(\rho_0,\alpha,\beta,\ell),
```

with exact implicit preference boundary

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

Let

```math
c=\rho_0-\Phi^{-1}(\beta)
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

The feasibility regimes are both-feasible / slow-only / neither. Fast-only feasibility is excluded in this deliberately equal-eventual-SNR scaled family.

### Proposition 1 — exact scope

Assumptions stated in the manuscript:

1. known-time operation is feasible;
2. `X_D` is continuous in normalized search length away from feasibility singularities;
3. `Gamma_infty` grows without bound as search length grows, giving a finite critical search length;
4. `X_D` diverges on approach to the feasibility boundary.

Under these assumptions:

```text
L=0 -> fast detector reaches the decision first;
L -> L_crit,f^- -> fast detection time diverges while slow remains finite;
therefore at least one finite fast-to-slow crossover exists.
```

No crossover uniqueness is established.

---

## Consistency/compression pass — completed 21:47 EDT

The merged manuscript was edited without adding new scientific claims.

Key changes:

- `PAPER_A_SECTION_V.md` was merged into `PAPER_A_DRAFT.md`; references now follow Section V.
- Section IV now ends with the theorem/proof instead of repeating the discussion.
- Section V alone carries physical interpretation, limitations, detector-specification implications, and conclusion.
- Body terminology was standardized on **eventual matched-filter SNR**; “asymptotic sensitivity” remains mainly title/context language.
- The abstract and conclusion both state that the crossover requires the assumptions of Proposition 1 and do not imply a general preference for slower detectors.
- The true-alignment detection criterion is explicitly distinguished from the total signal-present scan-maximum probability.
- The paper rejects a new detector-only sensitivity-speed scalar as its conclusion; the relevant object is the detector–task surface `X_D(rho_0,alpha,beta,L/tau)`.
- No Step-13–49 Pickands/Palm/Rice/high-band endpoint material was reintroduced.

Detector-facing closing statement retained:

> **Detector specifications rank devices only relative to the task for which the ranking is being made. When arrival time is uncertain, response time affects both signal accumulation and the statistical size of the timing search.**

---

## Prior-art status

Focused audit: `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

Established ingredients — not novelty targets:

- pulse/energy detection from frequency-dependent detector sensitivity;
- sensitivity-speed / detectivity-bandwidth comparison;
- unknown-arrival matched-filter search penalties controlled by correlated peak statistics/template correlation;
- all-pass magnitude preservation with altered phase/dispersion.

Only the complete equal-eventual-SNR photodetector task-reversal synthesis remains

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

Absence of a direct hit in the focused audit is not proof of novelty.

---

## Mathematical companion — Steps 13–49

The mathematical branch remains hard-stopped and separate. Preserve the correction history:

- Step-13 rough-grid `ell~49` estimate invalid.
- Rice upper switch near `kappa_f~130` invalidated.
- Coupling coefficient `.8131` invalid; corrected `.8906480701 sqrt(chi/zeta)`.
- Raw Step-27 tiny-chi values grid biased.
- Crossing counts fail from micro-upcrossings; finite-amplitude clusters replace them.
- Step 39 rejects a small-amplitude finite-u remainder.
- Step 41 corrects Step-35 tiny-q RMS from `~5.4e-5` to `~2.69e-5` asymptotically.
- Step 44 is finite-grid only, not a continuum certificate.
- Step 46 five-event result supports sign/scale consistency only, not precise coefficient validation.
- Steps 47–49 show the rough-grid correction survives mixed-tangent and exact-covariance transfer.
- **HARD-STOP:** do not create Step 50 unless external review identifies a decision-relevant gap.

---

## Active next phase

Stay inside **Paper A**. The scientific narrative is now complete and internally compressed.

The next logical action is **manuscript QA rather than new theory**: adversarially review `PAPER_A_DRAFT.md` for mathematical correctness, hidden assumptions, citation adequacy, overclaiming, notation defects, and likely reviewer objections. Any fixes should tighten the existing result, not broaden it.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the now-complete `PAPER_A_DRAFT.md` receive a severe reviewer-style audit before any formatting or submission work?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival search penalties as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.