# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 20:52 EDT  
**Status:** mathematical closure branch stopped after 49 logical steps; detector-facing prior-art audit and paper architecture completed; **Paper A opening draft now written. NOVELTY NOT ESTABLISHED.** The active manuscript file is `PAPER_A_DRAFT_OPENING.md`, containing the working title, abstract, central proposition, publication-style Introduction, and controlled equal-eventual-SNR setup through the exact finite-record timing-scan covariance. Do not create Step 50 of the old Gaussian-extremes proof chain by default.

Read next:
1. `PAPER_A_DRAFT_OPENING.md`
2. `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
3. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
4. `TASK_REGIME_BOUNDARY_STEP.md`
5. `PROGRESS_LOG.md`

---

## Paper A — active main track

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

The opening draft now contains:

- an abstract that concedes established pulse/sensitivity-bandwidth prior art before asking the actual equal-eventual-SNR question;
- a central proposition stated before the Introduction, with the continuity/divergence assumptions included explicitly;
- an Introduction that separates the present task question from established `D*`, pulse-detectivity, and unknown-arrival matched-filter literature;
- the controlled time-scaled family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

normalized so that

```math
\rho_{\tau,\infty}=\rho_0;
```

- the finite-time SNR fraction

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)};
```

- the exact finite-record timing-scan covariance

```math
R_x(y)
=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
\qquad 0\le y<x,
```

with `R_x(y)=0` for `y>=x` and physical scaling

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

The draft deliberately stops before Section III. No Pickands/Palm/Rice or Step-13–49 closure machinery appears in the main narrative.

### Central proposition retained

For

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau),
```

and two members with `tau_f<tau_s`, `r=tau_s/tau_f>1`, `ell=L/tau_s`,

```math
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions:

- `L=0`: fast reaches the decision first;
- the fast member reaches its physical feasibility boundary first;
- approaching that boundary, fast detection time diverges while slow remains feasible;
- at least one finite fast-to-slow crossover therefore exists;
- slow-only feasibility is possible;
- fast-only feasibility is excluded in this equal-eventual-SNR scaled family;
- no crossover uniqueness is claimed.

**Scope:** task/protocol result only. No claim that faster detectors are generally worse and no claim that the selected scan is universally optimal.

---

## Prior-art status

Focused audit remains `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

Established ingredients are cited as prior art in the opening draft:

- Jones 1960 for pulse/energy detectivity from frequency-dependent detector sensitivity;
- Garcia & Dereniak and modern detector-characterization literature for sensitivity-speed/bandwidth comparison;
- Vio/Andreani, Morras et al., and Croce et al. for unknown-arrival/correlated matched-filter false-alarm penalties.

Only the complete equal-eventual-SNR photodetector task-reversal synthesis remains a **POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED**.

---

## Technical mathematical companion — Steps 13–49

The mathematical closure branch remains hard-stopped and separate. Its role is robustness/stress testing, not the main detector theorem. Do not move its Pickands/Palm/Rice/high-band endpoint machinery back into Paper A unless a reviewer identifies a decision-relevant need.

Important retained caveats include the invalidated Step-13 rough-grid crossover, invalidated upper Rice switch, corrected coupling and tiny-q values, the finite-grid/continuum distinction, and the Step-46 wording correction that five-event Monte Carlo supports sign/scale consistency only.

---

## Active next drafting step

Stay inside **Paper A**.

The next logical action is to continue `PAPER_A_DRAFT_OPENING.md` with:

1. Section III: define `Gamma(x,ell,alpha)`, the decision margin, `X_D`, and derive the dimensionless detection-time surface;
2. Section IV: give the task-boundary and feasibility-partition proof in publication style;
3. stop before the Discussion/figures unless prompted.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can Sections III and IV now be drafted in publication style, carrying the opening manuscript through the dimensionless detection-time surface and the fast/slow task-reversal proof without reintroducing the mathematical companion?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival search penalties as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.