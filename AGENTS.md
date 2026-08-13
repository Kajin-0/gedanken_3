# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** detector-facing manuscript drafting. **MATHEMATICAL CLOSURE HARD-STOPPED. PRIOR-ART AUDIT COMPLETED. PAPER ARCHITECTURE FIXED. PAPER A OPENING DRAFT WRITTEN. NOVELTY NOT ESTABLISHED.** Step 49 is the final default proof step. The active manuscript is `PAPER_A_DRAFT_OPENING.md`, centered on the exact dimensionless detection-time surface and the protocol-specific equal-eventual-SNR fast/slow task boundary. Steps 13–49 are technical companion material, not the default main-paper narrative. Do not restart the Gaussian-extremes closure chain or invent a new scalar metric by default.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT_OPENING.md`
3. `experiments/01-equal-dstar-different-speed/PAPER_ARCHITECTURE_TASK_REVERSAL.md`
4. `experiments/01-equal-dstar-different-speed/PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
5. `experiments/01-equal-dstar-different-speed/TASK_REGIME_BOUNDARY_STEP.md`
6. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
7. final mathematical closure step: `experiments/01-equal-dstar-different-speed/EXACT_COVARIANCE_GRID_TRANSFER_STOP_STEP.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol

Before material writes: fetch live target and exact blob SHA; never overwrite stale state; preserve failed/corrected paths. `CURRENT_STATE.md`, `PROGRESS_LOG.md`, and this file must move whenever the research frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, PARTIAL CERTIFICATE, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, PAIRED NESTED-GRID DIAGNOSTIC, EXACT CANONICAL FINITE-GRID CORRECTION, EXACT CELLWISE BRIDGE DECOMPOSITION, PAIRED FINITE-LEVEL TRANSFER INTERVAL, PAIRED EXACT-COVARIANCE TRANSFER INTERVAL, HARD-GATE PASSED, HARD-STOP TRIGGERED, PRIOR-ART AUDIT, PAPER ARCHITECTURE, MANUSCRIPT DRAFT, POSSIBLE SYNTHESIS CONTRIBUTION, NOVELTY NOT ESTABLISHED, INVALIDATED, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, or equivalent novelty language without a deeper audit that actually supports it.

---

## Paper A — active manuscript track

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

Active manuscript: `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT_OPENING.md`.

The draft currently includes:

- Abstract.
- Central Proposition 1, with all continuity/divergence assumptions and scope restrictions explicit.
- Introduction.
- Section II.A: controlled time-scaled family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t)
```

with

```math
\rho_{\tau,\infty}=\rho_0.
```

- Finite-time SNR accumulation

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
```

- Section II.B: exact finite-record timing-scan covariance

```math
R_x(y)=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
\qquad 0\le y<x,
```

with `R_x(y)=0` for `y>=x` and

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

- Prior-art references [1]–[7] from the focused audit.

The main paper must keep the established ingredients clearly labeled as prior art. The novelty burden, if a deeper audit eventually supports novelty, rests only on the complete synthesis:

```text
equal eventual matched-filter SNR
+ different detector temporal scales
+ fixed physical unknown-arrival interval
+ one global false-alarm requirement
+ finite-time evidence accumulation
+ time-scale-dependent search correlation
-> explicit fast/slow task boundary and reversal.
```

The next manuscript step is Section III + IV only: derive the dimensionless detection-time surface and present/prove the task-reversal/feasibility theorem. Do not jump back to specialized closure mathematics.

---

## Detector-facing core — Steps 01–12

The surviving detector result is:

- Scalar reference `D*` does not determine arbitrary temporal-signal performance, but this is established pulse-detection prior art and is not a novelty target.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem.
- Finite records make phase/time placement operationally relevant even with identical magnitude response; the all-pass construction is pedagogically useful but not the novelty-bearing theorem.
- Finite-time optimal SNR is `rho_T^2=<s_T,C_T^-1 s_T>`.
- Unknown arrival introduces a global-false-alarm timing search governed by matched-filter scan covariance rather than raw ADC sample count; this mechanism is established adjacent detection theory.
- In the controlled equal-eventual-SNR family, faster response accumulates evidence sooner but shortens timing correlation length. Under the **defined scanning protocol**, those effects can reverse the fast/slow detection ranking.
- The exact task surface is

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

- For `r=tau_s/tau_f>1`, `ell=L/tau_s`, the exact fast/slow boundary is

```math
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions:

```text
L=0 -> fast wins;
near the fast feasibility boundary -> fast detection time diverges while slow remains feasible;
therefore at least one finite fast-to-slow crossover exists;
slow-only feasibility is possible;
fast-only feasibility is excluded in this equal-eventual-SNR scaled family.
```

No crossover uniqueness is established.

**Scope:** task/protocol result only. Do not state that faster detectors are generally worse or that the scan is universally optimal.

---

## Mathematical companion — Steps 13–49

Keep these as technical companion/appendix material unless an external reviewer identifies a decision-relevant gap.

Key surviving corrections and closure results:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window scan is locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Rice's apparent upper switch near `kappa_f~130` is **INVALIDATED**; Palm preserves only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw tiny-chi Step-27 values were grid biased.
- Crossing moments fail from micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 finds `R=N_a/N_tan~1.56`; finite-u correction is not a small-amplitude remainder.
- Step 40 gives Cameron-Martin exact-event threshold translation.
- Step 41 replaces empirical q interpolation with analytic Gaussian-process control.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.
- Duration truncation at `L0=.02` makes bounded-weight finite-sample concentration possible; Step 44 gives pointwise finite-grid 95% `P_FA/alpha<.999957771`, but only `.00004223 alpha` margin.
- Step 45 shows witness retuning trades one near-boundary problem for another.
- Step 46 isolates missed between-sample maxima as the dominant grid error. **WORDING CORRECTION:** the five-event paired result has ~47% relative SE and supports sign/scale consistency only, not precise coefficient validation.
- Step 47 gives exact pure-alpha1 discrete Pickands correction `H_1^delta=nu(sqrt(2delta))`.
- Step 48 gives mixed finite-u transfer only `O(1e-5)` relative to an `O(9e-4)` grid loss.
- Step 49 evaluates the exact finite-window covariance directly and finds the same grid-loss scale.

**HARD-STOP TRIGGERED:** do not create Step 50 of this proof chain by default.

---

## Prior-art audit disposition

Full audit: `experiments/01-equal-dstar-different-speed/PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

Established ingredients — not novelty targets:

1. pulse/energy detection from frequency-dependent detector sensitivity;
2. sensitivity-speed / detectivity-bandwidth comparison;
3. unknown-arrival matched-filter search penalties controlled by correlated peak statistics/template correlation;
4. all-pass magnitude preservation with altered phase/dispersion.

Focused audit found no direct match for the complete equal-eventual-SNR photodetector task-reversal construction. Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

Absence of a direct hit is not proof of novelty. A deeper citation-network/patent audit is required before any novelty claim.

---

## Active next phase

Stay inside **Paper A**.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can Sections III and IV now be drafted in publication style, carrying `PAPER_A_DRAFT_OPENING.md` through the dimensionless detection-time surface and the fast/slow task-reversal proof without reintroducing the mathematical companion?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival matched-filter search penalty as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.