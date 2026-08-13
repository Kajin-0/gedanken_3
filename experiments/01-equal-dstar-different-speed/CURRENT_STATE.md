# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 22:09 EDT  
**Status:** mathematical closure branch hard-stopped after 49 logical steps; prior-art audit completed; Paper A drafted and consistency-compressed; **severe adversarial review completed. MAJOR REVISION REQUIRED. NOVELTY NOT ESTABLISHED.** The core algebra survives review, but the manuscript is **not submission-ready** because its acquisition clock and true-alignment detection criterion are not yet operationally framed tightly enough.

Read next:
1. `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
2. `PAPER_A_DRAFT.md`
3. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
4. `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
5. `DIMENSIONLESS_DETECTION_SURFACE_STEP.md`
6. `TASK_REGIME_BOUNDARY_STEP.md`
7. `PROGRESS_LOG.md`

---

## Paper A — authoritative manuscript

Working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

Authoritative draft: `PAPER_A_DRAFT.md`.

Central family:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
\qquad
\rho_{\tau,\infty}=\rho_0.
```

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
\qquad x=t/\tau.
```

```math
R_x(y)=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^x v^2e^{-2v}dv},
\qquad
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

Global timing-scan threshold:

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
\qquad \ell=L/\tau.
```

True-alignment margin:

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
```

Covariance ordering plus Gaussian comparison gives

```math
x_2>x_1
\Rightarrow
\Gamma(x_2,\ell,\alpha)\le\Gamma(x_1,\ell,\alpha),
```

so the margin is strictly increasing with observation duration and

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For `tau_f<tau_s`, `r=tau_s/tau_f>1`, `ell=L/tau_s`, the implicit task boundary is

```math
B_r(\ell)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

With

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<\rho_0-\Phi^{-1}(\beta)\},
```

physical feasibility scales as

```math
L_{crit}(\tau)=\tau\ell_{crit}.
```

Under Proposition 1 assumptions: known-time operation is feasible; `X_D` is continuous away from singularities; `Gamma_infty` grows without bound; and `X_D` diverges at the feasibility boundary. Then fast wins at `L=0`, fast diverges first, and at least one finite fast-to-slow crossover exists. No uniqueness or universal ordering is claimed.

---

## Adversarial reviewer audit — completed 22:09 EDT

Full audit: `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`.

### Disposition

```text
MAJOR REVISION / NO FATAL INTERNAL MATHEMATICAL CONTRADICTION FOUND
/ BLOCKING OPERATIONAL-INTERPRETATION ISSUES
/ NOVELTY NOT ESTABLISHED
```

### Mathematical pieces that survived direct audit

- equal-eventual-SNR normalization `A_tau ∝ tau^(-3/2)`;
- `eta(x)` and its monotonicity;
- finite-template covariance `R_x(y)`;
- the positive-weight-average covariance-ordering argument;
- the Slepian comparison direction;
- strict increase of the true-alignment margin with observation duration;
- the dimensionless task scaling;
- the both / slow-only / neither feasibility partition;
- exclusion of fast-only feasibility in this scaled family;
- the intermediate-value crossover proof **given the proposition assumptions**.

### Blocking issue 1 — acquisition clock / meaning of `T_D`

The current stationary scan with a full length-`t` template for every candidate arrival in a window of length `L` implicitly requires a batch record of duration approximately `L+t`. `T_D=t` is therefore not automatically an online wall-clock detection latency.

Repair without changing the theorem:

```text
define the batch acquisition protocol explicitly;
interpret T_D as required post-window integration duration;
or define T_wall=L+T_D and note that fixed-L detector ordering is unchanged.
```

### Blocking issue 2 — `P_D,true` is a conservative guarantee criterion

The manuscript uses

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)],
```

which is not the full signal-present scan probability

```math
P_D^{scan}=Pr[\sup_q Z_{signal}(q)>\Gamma].
```

Because true-alignment exceedance implies scan exceedance,

```math
P_D^{scan}\ge P_{D,true}.
```

Thus the present first-crossing time is a **guaranteed / sufficient integration duration** for the global scan, not necessarily the exact scan detection time. A reversal of these guarantee times does not by itself prove a reversal of exact signal-present scan detection times.

Default repair path: reframe the theorem explicitly as a **true-alignment guarantee criterion** rather than reopening the full signal-present Gaussian-extremes problem.

### Major issue 3 — restore the common optical input and detector transfer function

The paper should restore the already-derived physical realization

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

so the same optical event produces

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t)
```

through causal, proper, stable detector channels. Otherwise the manuscript risks reading as generic signal processing rather than a photodetector construction.

Also state that equal eventual matched-filter SNR is event-specific and deliberately stronger than equal scalar reference `D*`.

### Major issue 4 — Proposition 1 is more conditional than necessary

The divergence assumption can largely be derived from

```math
eta(x)<1,
\qquad
Gamma(x,ell,alpha)\ge Gamma_\infty(ell,alpha),
```

plus boundary equality/continuity. Exponential decay of

```math
R_\infty(y)=(1+y)e^{-y}
```

places the full-template scan in standard stationary-Gaussian extreme-value theory, so unbounded large-search maxima should be cited/proved rather than merely assumed. Add an explicit Slepian citation.

### Major issue 5 — no robust quantitative example in Paper A

The existence theorem alone permits a crossover arbitrarily close to the fast feasibility boundary. After the conceptual blockers are repaired, add one continuum-validated, non-knife-edge example/phase diagram with comfortable margins. Do not reuse invalidated Step-13 or treat Step-44 finite-grid results as continuum truth.

### Major presentation fixes

- distinguish `D*` noise-equivalent bandwidth normalization from detector temporal/3-dB bandwidth;
- define the white-noise convention exactly, e.g. `E[n(t)n(t')]=N delta(t-t')`;
- consider replacing title phrase "equal asymptotic sensitivity" with event-specific matched-filter wording;
- define `Phi` explicitly and standardize crossover notation;
- add DOI `10.1038/s41467-026-72259-1` for Yang et al.;
- add Slepian and stationary-Gaussian-extreme citations.

---

## Prior-art / novelty status after adversarial audit

Verified established ingredients remain:

- Jones 1960: pulse/energy detectivity from `D*(f)`;
- Garcia & Dereniak 1990: explicit infrared `D* × bandwidth` benchmarking;
- Yang et al. 2026: explicit `Detectivity × Bandwidth` USBL;
- Pecunia et al. 2025: characterization/reporting/application benchmarking guidance;
- Vio/Andreani, Morras et al., Croce et al.: unknown-position matched-filter/global-false-alarm statistics governed by correlated scan structure.

Additional adjacent prior art identified: Milstein et al., *Applied Optics* 47, 296–311 (2008), DOI `10.1364/AO.47.000296`, studies constant-false-alarm acquisition time in a specified range window for direct-detection ladar with Geiger-mode APDs.

No direct match to the complete equal-eventual-SNR fast/slow reversal was found in this audit, but the adjacent radar/sonar/ladar/synchronization literature remains a serious novelty risk.

Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## Mathematical companion — Steps 13–49

**HARD-STOP REMAINS ACTIVE.** Preserve the correction history and do not create Step 50 by default. The audit does not justify reopening the Gaussian-extremes branch; the preferred repair is narrower, operationally exact framing of the existing criterion.

Key preserved corrections include invalid Step-13 `ell~49`, invalid upper Rice switch, corrected coupling/tiny-q values, finite-grid-only Step 44, Step-46 sign/scale-only wording, and Steps 47–49 exact-canonical/mixed/exact-covariance grid-transfer results.

---

## Active next phase

Do **not** format or submit yet.

Repair in this order:

1. operationally define the batch acquisition clock and `T_D`;
2. reframe `P_D,true` as a guaranteed true-alignment criterion (default path), unless explicitly choosing the much harder full-scan theorem;
3. restore fixed optical input + detector transfer-function realization;
4. strengthen/cite Proposition 1 assumptions;
5. add one robust non-knife-edge numerical example;
6. tighten `D*`/noise/citation language;
7. only then perform final novelty audit, figures, and journal formatting.

### Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the manuscript be revised first to make the acquisition clock and the true-alignment guarantee criterion operationally exact, without changing the existing Gaussian-extremes hard stop or claiming a full signal-present scan theorem?

---

## Scope boundary

Do not claim: exact online detection latency under the current batch protocol; exact full signal-present scan detection-time reversal; faster universally better/worse; a universal scalar replacement for `D*`; `D* × bandwidth` as new; unknown-arrival search penalties as new; scanning protocol universally optimal; crossover uniqueness; Step-13 `ell~49`; Step-20 double reversal; raw Step-27 values as continuum truth; Step-44 as a continuum certificate; Step-46 coefficient precisely verified; Step-47 canonical ratio as exact finite-u false-alarm ratio; Steps 48/49 Monte Carlo intervals as distribution-free theorem-level; novelty.