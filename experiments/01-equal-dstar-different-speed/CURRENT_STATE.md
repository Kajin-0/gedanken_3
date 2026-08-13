# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 22:54 EDT  
**Status:** mathematical closure branch hard-stopped after 49 logical steps; prior-art audit completed; severe adversarial review completed; **Paper A blocking acquisition-clock and true-alignment claim-scope issues repaired on the active revision branch.** Core theorem now concerns an operationally defined **post-window guarantee time**, not ordinary online latency or exact full signal-present scan detection time. **Robust exact-model quantitative example remains open. Novelty not established.**

Read next:
1. `PAPER_A_DRAFT.md`
2. `PAPER_A_MAJOR_REVISION_2026-08-12.md`
3. `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
4. `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`
5. `TASK_REGIME_BOUNDARY_STEP.md`
6. `PROGRESS_LOG.md`

---

## Paper A — revised authoritative manuscript on this branch

Working title:

> **Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR**

Authoritative draft: `PAPER_A_DRAFT.md`.

### Common optical event and detector realization

All channels receive

```math
p(t)=e^{-bt}u(t)
```

through

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

so

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

The output-noise convention is now explicit:

```math
E[n(t)n(t')]=N\delta(t-t'),
```

with

```math
\rho^2=\frac1N\int s^2(t)dt.
```

Choosing

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

gives the same **event-specific eventual matched-filter SNR** `rho_0` for every `tau`.

Finite-time accumulation remains

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
\qquad x=t/\tau.
```

### Exact batch acquisition clock

Event arrival is known only to lie in `[0,L]`. A duration-`t` matched filter must be available at every candidate arrival, including the latest candidate `L`, so the batch record extends through `L+t`.

The revised object is

```math
\boxed{
T_G=\text{minimum post-window integration duration satisfying the guarantee criterion}.
}
```

The physical wall-clock batch decision time is

```math
\boxed{
T_{wall}=L+T_G.
}
```

At fixed `L`, `T_wall` and `T_G` induce exactly the same fast/slow ordering.

### Global scan threshold and guarantee criterion

Noise-only threshold:

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]\le\alpha,
\qquad \ell=L/\tau.
```

True-alignment probability:

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

Complete signal-present scan probability:

```math
P_D^{scan}
=\Pr\left[\sup_qY_x(q)>\Gamma\right].
```

The revised manuscript now makes the exact one-sided logic central:

```math
\boxed{
P_D^{scan}\ge P_{D,true}.
}
```

Thus `P_D,true>=beta` is a **sufficient guarantee** that the complete scan detects with probability at least `beta`.

The paper does **not** claim that the exact first solution of `P_D^scan=beta` has the same fast/slow ordering.

### Guarantee-time scaling

Define

```math
M_G(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha),
```

and

```math
X_G(\rho_0,\alpha,\beta,\ell)
=\inf\{x:M_G(x;\ell)\ge\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G(\rho_0,\alpha,\beta,L/\tau).
}
```

For `tau_f<tau_s`, `r=tau_s/tau_f`, `ell=L/tau_s`, the guarantee-time boundary is

```math
\boxed{
B_r(\ell)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
}
```

---

## Proposition 1 — strengthened

The prior manuscript assumed both large-search threshold divergence and first-crossing divergence at the feasibility boundary. The revision derives both.

### Large-search threshold divergence

The full-template covariance is

```math
R_\infty(y)=(1+y)e^{-y}\to0.
```

Widely separated samples have arbitrarily small pairwise covariance. Comparing them by Slepian with an equicorrelated Gaussian vector shows that the sampled maximum diverges in probability as the number of separated points grows. Therefore

```math
\boxed{
\Gamma_\infty(\ell,\alpha)\to\infty
\qquad(\ell\to\infty).
}
```

A finite guarantee-feasibility boundary therefore exists whenever known-time operation is guarantee-feasible.

### Boundary divergence

For finite `x`,

```math
\eta(x)<1,
\qquad
R_x(y)\le R_\infty(y),
\qquad
\Gamma(x,\ell,\alpha)\ge\Gamma_\infty(\ell,\alpha).
```

At a continuous boundary satisfying

```math
\Gamma_\infty(\ell_{crit},\alpha)
=\rho_0-\Phi^{-1}(\beta),
```

every finite `x` remains strictly below the guarantee requirement. Continuity then forces

```math
\boxed{
X_G(\ell)\to\infty
\quad\text{as}\quad
\ell\uparrow\ell_{crit}.
}
```

Thus Proposition 1 now assumes only known-time guarantee feasibility plus ordinary threshold/first-crossing continuity in the feasible region and at the boundary.

### Result

Fast wins for sufficiently small `L`. The fast channel reaches the guarantee-feasibility boundary first, while the slow channel remains strictly feasible there. Hence at least one finite fast-to-slow **guarantee-time** crossover exists.

No uniqueness claim.

---

## Exact scope after major revision

The manuscript now establishes:

```text
same optical event
+ causal time-scaled detector family
+ equal event-specific eventual matched-filter SNR
+ batch unknown-arrival scan
+ global noise-only false-alarm threshold
+ true-alignment sufficient detection guarantee
-> task-dependent guarantee-time ordering
-> both / slow-only / neither guarantee-feasibility partition
-> at least one fast-to-slow guarantee-time crossover.
```

It does **not** establish:

```text
exact online/sequential detection latency;
exact full signal-present scan detection-time reversal;
Bayes/minimax/sequential optimality;
crossover uniqueness;
universal slow-detector preference;
a universal scalar replacement for D*;
novelty.
```

---

## Quantitative example — still open

The severe review's request for one robust non-knife-edge quantitative example remains valid.

Do not use:

- Step-13 `ell~49`: invalid rough-grid crossover;
- Step-20 upper Rice reversal: invalidated by Palm correction;
- Step-44 pointwise finite-grid certificate as continuum truth;
- Steps 47–49 spectral-intensity grid transfer as exact finite-`u` scan probability.

The smooth finite-information model from Steps 14–16 is a valid companion stress test and demonstrates that the mechanism survives regularization, but it is not the exact hard-window Paper A model.

**Next numerical target:** choose a new parameter set for margin first and obtain a continuum-controlled exact-hard-window example showing fast preference at low `L`, a crossover while both channels are comfortably guarantee-feasible, and slow-only guarantee feasibility at larger `L`.

Do not tune around the old `r=2, Lambda=0.895` knife edge.

---

## Mathematical companion — Steps 13–49

**HARD STOP REMAINS ACTIVE. DO NOT CREATE STEP 50 BY DEFAULT.**

Preserve the complete correction history:

- Step-13 rough-grid crossover invalid;
- finite information bandwidth regularizes the cusp, but an invertible common low-pass is not a physical information restriction;
- Step-20 upper Rice switch invalidated;
- raw Step-27 tiny-`chi` values grid biased;
- excursion clusters replaced unstable micro-upcrossing counts;
- Step-44 is finite-grid only;
- Steps 46–49 show the rough-grid effect is real and not canceled by higher-order covariance structure;
- Step-49 intentionally stopped before another publication-grade finite-`u` transfer branch.

The Paper A revision does not reopen any of these branches.

---

## Prior-art / novelty status

Established ingredients still include pulse/energy detectivity from frequency-dependent response, explicit detectivity-bandwidth benchmarking, correlated unknown-arrival matched-filter false alarms, and acquisition-time/range-window detection problems.

The candidate contribution remains the narrower detector-facing synthesis:

```text
same optical event
-> equal eventual matched-filter SNR channels
-> time-scale-dependent unknown-arrival search geometry
-> conservative global-scan guarantee criterion
-> guarantee-feasibility partition and ordering reversal.
```

Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

A deeper radar/sonar/ladar/synchronization citation-network audit is still required before any priority language.

---

## Active next phase

1. Validate the revised Paper A manuscript against the adversarial-review blockers.
2. Build one new **margin-first continuum-controlled quantitative example** for the exact hard-window model.
3. Perform final closest-prior-art / citation audit.
4. Only then consider figures, journal formatting, or submission.

### Current single next question

> Can a robust exact-hard-window quantitative example be designed away from the old feasibility-edge calibration, without reopening the Step-49 closure program?
