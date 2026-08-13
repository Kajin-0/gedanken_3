# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** detector-facing manuscript QA and repair. **MATHEMATICAL CLOSURE HARD-STOPPED. PRIOR-ART AUDIT COMPLETED. PAPER A MERGED. SEVERE ADVERSARIAL REVIEW COMPLETED. MAJOR REVISION REQUIRED. NOVELTY NOT ESTABLISHED.** Step 49 is the final default proof step. The authoritative manuscript remains `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md`; the authoritative reviewer audit is `experiments/01-equal-dstar-different-speed/PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`. Do not restart the Gaussian-extremes closure chain by default.

Read first:
1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
3. `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md`
4. `experiments/01-equal-dstar-different-speed/PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
5. `experiments/01-equal-dstar-different-speed/PAPER_ARCHITECTURE_TASK_REVERSAL.md`
6. `experiments/01-equal-dstar-different-speed/DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
7. `experiments/01-equal-dstar-different-speed/TASK_REGIME_BOUNDARY_STEP.md`
8. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`

Live `main` overrides chat summaries or stale notes.

---

## Mandatory repository protocol

Before material writes: fetch live target and exact blob SHA; never overwrite stale state; preserve failed/corrected paths. `CURRENT_STATE.md`, `PROGRESS_LOG.md`, and this file must move whenever the research frontier changes.

Useful epistemic labels include: **DEFINED, ASSUMED, DERIVED, CONDITIONAL, COUNTEREXAMPLE, REFINEMENT, NEGATIVE RESULT, REJECTED SHORTCUT, FAILED NUMERICAL ESTIMATE, NUMERICAL VALIDATION, RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE, EXACT CANONICAL FINITE-GRID CORRECTION, PAIRED FINITE-LEVEL TRANSFER INTERVAL, PAIRED EXACT-COVARIANCE TRANSFER INTERVAL, HARD-GATE PASSED, HARD-STOP TRIGGERED, PRIOR-ART AUDIT, PAPER ARCHITECTURE, MANUSCRIPT DRAFT, MANUSCRIPT CONSISTENCY PASS, ADVERSARIAL REVIEW, MAJOR REVISION, BLOCKING ISSUE, POSSIBLE SYNTHESIS CONTRIBUTION, NOVELTY NOT ESTABLISHED, INVALIDATED, ASYMPTOTIC, OPEN, NON-CLAIM.**

Do not use `novel`, `universal`, `fundamental`, `first`, or equivalent novelty language without a deeper audit that supports it.

---

## Paper A — authoritative manuscript

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

Active manuscript:

`experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md`

Core mathematics currently retained:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
\qquad
\rho_{\tau,\infty}=\rho_0,
```

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
```

```math
R_x(y)=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
```

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
\qquad
M=\rho_0\sqrt{\eta(x)}-\Gamma,
```

```math
T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For `tau_f<tau_s`, `r=tau_s/tau_f`, `ell=L/tau_s`:

```math
B_r(\ell)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Conditional Proposition 1: known-time fast preference + earlier fast feasibility boundary + divergence + continuity -> at least one finite fast-to-slow crossover. No uniqueness or universal ordering.

---

## Severe adversarial review — controlling QA status

Full report: `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`.

### Reviewer disposition

```text
MAJOR REVISION BEFORE SUBMISSION.
NO FATAL INTERNAL MATHEMATICAL CONTRADICTION FOUND.
BLOCKING OPERATIONAL / CLAIM-SCOPE ISSUES REMAIN.
```

### Blocking issue 1 — acquisition clock

The current stationary scan implicitly assumes enough data to fit a full length-`t` template after every candidate arrival in an uncertainty window `L`, i.e. a batch record of about `L+t`.

Do not call current `T_D=t` a general online detection latency. Preferred repair:

```text
define the batch acquisition protocol explicitly;
call T_D the required post-window integration duration;
or define T_wall=L+T_D and note fixed-L ordering is unchanged.
```

### Blocking issue 2 — true-alignment guarantee versus exact scan detection

Current criterion:

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

Exact signal-present scan probability would be

```math
P_D^{scan}=Pr[\sup_q Z_{signal}(q)>\Gamma].
```

Because true-alignment exceedance is a subset of scan exceedance,

```math
P_D^{scan}\ge P_{D,true}.
```

Thus current `T_D` is a **sufficient / guaranteed integration time**, not necessarily the exact scan detection time. A reversal of these guarantee times is not by itself a theorem about exact signal-present scan detection times.

**Default repair path:** reframe Paper A explicitly around the true-alignment guarantee criterion. Do not reopen the full signal-present Gaussian-extremes theorem unless explicitly chosen later.

### Major repair 3 — restore photodetector realization

Reintroduce the fixed optical event and stable causal transfer family already derived:

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

which yields the manuscript signal. State that equal eventual matched-filter SNR is **event-specific** and deliberately stronger than equal scalar `D*`.

### Major repair 4 — strengthen Proposition 1

Do not leave all of continuity / large-search growth / boundary divergence as naked assumptions if they can be proved or cited for this covariance. Add explicit Slepian and stationary-Gaussian extreme-value references. The divergence at the boundary can largely be derived from `eta(x)<1`, `Gamma(x)>=Gamma_infty`, boundary equality, and continuity.

### Major repair 5 — add robust quantitative example after conceptual repairs

The theorem currently establishes existence only. Add one continuum-validated non-knife-edge example/phase diagram with comfortable margins. Do not use invalid Step-13 or promote Step-44 finite-grid results to continuum truth.

### Presentation repairs

- distinguish `D*` noise-equivalent bandwidth normalization from detector temporal bandwidth;
- define AWGN covariance/PSD convention exactly;
- consider event-specific title wording instead of global "asymptotic sensitivity";
- define `Phi`, standardize crossover notation;
- add Yang DOI and Gaussian-comparison/extreme-value citations.

---

## Prior-art / novelty status

Established ingredients remain non-novel: pulse/energy detectivity from `D*(f)`, sensitivity-speed products, and unknown-arrival matched-filter search penalties.

Additional adjacent prior art from audit: Milstein et al., *Applied Optics* 47, 296–311 (2008), DOI `10.1364/AO.47.000296`, on constant-false-alarm acquisition time in a specified range window for direct-detection ladar with Geiger-mode APDs.

Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No direct match to the complete equal-eventual-SNR fast/slow reversal has been found in the focused searches, but radar/sonar/ladar/synchronization literature remains a serious adjacent novelty risk.

---

## Mathematical companion — Steps 13–49

**HARD-STOP REMAINS ACTIVE.** Do not create Step 50 by default. The reviewer audit does not justify restarting Pickands/Palm/Rice closure work.

Preserve correction history: invalid Step-13 `ell~49`; invalid upper Rice switch; corrected coupling and tiny-q values; Step-44 finite-grid only; Step-46 sign/scale-only numerical wording; Steps 47–49 discrete-Pickands/mixed/exact-covariance grid-transfer results.

---

## Active next phase

Do not format or submit Paper A yet.

Repair order:

1. define the batch acquisition clock and meaning of `T_D`;
2. reframe the true-alignment criterion as a guaranteed scan-detection criterion;
3. restore fixed optical input + detector transfer-function realization;
4. strengthen/cite Proposition 1 assumptions;
5. add one robust non-knife-edge numerical illustration;
6. tighten `D*`, noise normalization, title, notation, and references;
7. only then final novelty audit / figures / journal formatting.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the manuscript be revised first to make the acquisition clock and the true-alignment guarantee criterion operationally exact, without changing the existing Gaussian-extremes hard stop or claiming a full signal-present scan theorem?

---

## Scope boundary

Do not claim: current `T_D` is exact online latency; current theorem proves exact full signal-present scan detection-time reversal; faster universally better/worse; a universal scalar replacement for `D*`; `D* × bandwidth` as new; unknown-arrival search penalties as new; universal scan optimality; crossover uniqueness; invalid Step-13/20/27 results; Step-44 continuum certification; precise Step-46 coefficient validation; Step-47 ratio as exact finite-u false-alarm ratio; Steps 48/49 as distribution-free theorem-level results; novelty.