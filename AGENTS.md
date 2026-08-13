# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** detector-facing manuscript drafting. **MATHEMATICAL CLOSURE HARD-STOPPED. PRIOR-ART AUDIT COMPLETED. PAPER ARCHITECTURE FIXED. PAPER A DRAFTED THROUGH SECTION IV. NOVELTY NOT ESTABLISHED.** Step 49 is the final default proof step. The active manuscript is now `PAPER_A_DRAFT.md`. `PAPER_A_DRAFT_OPENING.md` is retained as the opening-draft milestone. Steps 13–49 are technical companion material, not the default main-paper narrative. Do not restart the Gaussian-extremes closure chain or invent a new scalar metric by default.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md`
3. `experiments/01-equal-dstar-different-speed/PAPER_ARCHITECTURE_TASK_REVERSAL.md`
4. `experiments/01-equal-dstar-different-speed/PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
5. `experiments/01-equal-dstar-different-speed/DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
6. `experiments/01-equal-dstar-different-speed/TASK_REGIME_BOUNDARY_STEP.md`
7. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol

Before material writes: fetch live target and exact blob SHA; never overwrite stale state; preserve failed/corrected paths. `CURRENT_STATE.md`, `PROGRESS_LOG.md`, and this file must move whenever the research frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, EXACT CANONICAL FINITE-GRID CORRECTION, PAIRED FINITE-LEVEL TRANSFER INTERVAL, PAIRED EXACT-COVARIANCE TRANSFER INTERVAL, HARD-GATE PASSED, HARD-STOP TRIGGERED, PRIOR-ART AUDIT, PAPER ARCHITECTURE, MANUSCRIPT DRAFT, POSSIBLE SYNTHESIS CONTRIBUTION, NOVELTY NOT ESTABLISHED, INVALIDATED, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, or equivalent novelty language without a deeper audit that actually supports it.

---

## Paper A — active manuscript track

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

Active manuscript:

`experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md`

### Manuscript through Section II

The draft contains:

- Abstract and Introduction with established detector/signal-detection ingredients explicitly cited as prior art.
- Controlled time-scaled family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
\qquad
\rho_{\tau,\infty}=\rho_0.
```

- Finite-time evidence fraction

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
```

- Exact finite-record timing covariance

```math
R_x(y)=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
\qquad
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

### Section III — dimensionless task surface

Define the global correlated-scan threshold by

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
\qquad \ell=L/\tau.
```

The true-alignment decision margin is

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
```

The Step-11 covariance ordering plus standard Gaussian comparison gives

```math
x_2>x_1
\Rightarrow
\Gamma(x_2,\ell,\alpha)\le\Gamma(x_1,\ell,\alpha),
```

so `M` is strictly increasing. Define

```math
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\{x:M(x)\ge\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
}
```

This is the exact central scaling for the controlled family. The reversal is therefore a cross-detector scaling effect, not a finite integration-time optimum.

### Section IV — task boundary and feasibility proof

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

and

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
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<c\},
```

physical feasibility scales as

```math
L_{\mathrm{crit}}(\tau)=\tau\ell_{\mathrm{crit}}.
```

The exact feasibility regimes are:

```text
both feasible:
    c > Gamma_infty(r ell, alpha)

slow only:
    Gamma_infty(ell, alpha) < c <= Gamma_infty(r ell, alpha)

neither feasible:
    c <= Gamma_infty(ell, alpha)
```

Fast-only feasibility is excluded in this deliberately normalized family.

**Proposition 1 assumptions are explicit in the manuscript:** known-time feasibility; continuity of `X_D` away from singularities; unbounded growth of `Gamma_infty` with search length; divergence of `X_D` at the feasibility boundary.

Under those assumptions:

```text
L=0 -> fast wins;
L -> L_crit,f^- -> fast detection time diverges while slow remains finite;
therefore at least one finite fast-to-slow crossover exists.
```

No crossover uniqueness is established.

**Scope:** task/protocol result only. Do not state that faster detectors are generally worse or that the scan is universally optimal.

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

Absence of a direct hit is not proof of novelty. A deeper citation-network/patent audit is required before novelty language.

---

## Mathematical companion — Steps 13–49

Keep as technical robustness/stress-test material unless an external reviewer identifies a decision-relevant gap.

Critical preserved corrections:

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
- **HARD-STOP:** do not create Step 50 by default.

---

## Active next phase

Stay inside **Paper A**.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can Section V now be drafted to finish the detector-facing narrative, with the practical implication stated strongly but without broadening the theorem beyond the defined task/protocol?

---

## Scope boundary

Do not claim: faster universally better/worse; a universal scalar replacement for `D*`; `D* x bandwidth` as new; unknown-arrival matched-filter search penalty as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-34 fully formal theorem; Step-36 uniform hazard theorem; `R~1`; numerical covariance constants interval-certified; `L0=.02` optimal; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Step-48/49 Monte Carlo intervals as distribution-free theorem-level; `X=7.16` mathematically optimal; no re-entrant pocket for all task parameters; novelty.