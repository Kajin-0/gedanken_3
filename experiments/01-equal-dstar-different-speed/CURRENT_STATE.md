# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 23:22 EDT  
**Status:** mathematical closure branch remains hard-stopped after Step 49. Paper A's acquisition-clock and scan-power claim-scope blockers are repaired. A robust quantitative regime witness is now established without reopening Step 50. A deeper acquisition / optical-acquisition / ladar prior-art audit has narrowed the novelty burden. **Novelty remains unestablished.** Active work is draft PR #1 on `agent/paper-a-guarantee-semantics`.

Read next:

1. `PAPER_A_DRAFT.md`
2. `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
3. `PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`
4. `PAPER_A_POST_REVISION_AUDIT_2026-08-12.md`
5. `PAPER_A_POST_REVISION_AUDIT_ADDENDUM_2026-08-12.md`
6. `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
7. `PROGRESS_LOG.md`

---

## Authoritative Paper A result

Working title:

> **Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR**

All channels receive the same optical event

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

With

```math
E[n(t)n(t')]=N\delta(t-t'),
```

choosing

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

gives equal **event-specific eventual matched-filter SNR**

```math
\rho_{\tau,\infty}=\rho_0.
```

Finite-time evidence accumulation is

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
\qquad x=t/\tau.
```

The full-template timing covariance is

```math
\boxed{R_\infty(y)=(1+|y|)e^{-|y|}.}
```

---

## Operational guarantee-time semantics

Event arrival is known only to lie in `[0,L]`. A duration-`t` matched filter applied at every candidate arrival requires data through `L+t`. The problem is therefore explicitly **batch**, not sequential.

Define

```math
\boxed{
T_G=\text{minimum post-window integration duration satisfying the guarantee criterion}.
}
```

The wall-clock batch time is

```math
\boxed{T_{wall}=L+T_G.}
```

At fixed `L`, `T_G` and `T_wall` induce the same pairwise channel ordering.

For normalized search length

```math
\ell=L/\tau,
```

the global noise-only threshold is

```math
\Gamma(x,\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>u\right]\le\alpha
\right\}.
```

At the generative true alignment `q_0`, which is an **analysis variable only** and is not supplied to the receiver,

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

The complete signal-present scan satisfies

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

Thus the paper proves ordering of a **sufficient guarantee time**, not exact ordering of the first solutions of `P_D^scan=beta`.

Define

```math
X_G(\rho_0,\alpha,\beta,\ell)
=\inf\{x:\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G(\rho_0,\alpha,\beta,L/\tau).
}
```

---

## Fast/slow theorem — strengthened form

For

```math
\tau_f<\tau_s,
\qquad
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the exact guarantee-time preference boundary is

```math
\boxed{
B_r(\ell)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
}
```

With

```math
c=\rho_0-\Phi^{-1}(\beta),
```

the full-template guarantee-feasibility regimes are

```math
\begin{array}{ll}
\text{both feasible:} & c>\Gamma_\infty(r\ell,\alpha),\\
\text{slow only:} & \Gamma_\infty(\ell,\alpha)<c\le\Gamma_\infty(r\ell,\alpha),\\
\text{neither:} & c\le\Gamma_\infty(\ell,\alpha).
\end{array}
```

Fast-only guarantee feasibility is impossible in this equal-eventual-SNR scaled family.

Two former assumptions are now derived:

1. because `R_infty(y)->0`, widely separated samples plus Slepian comparison imply

```math
\Gamma_\infty(\ell,\alpha)\to\infty;
```

2. because `eta(x)<1`, `R_x<=R_infty`, and hence `Gamma(x)>=Gamma_infty`, continuity at the critical boundary implies

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit}).
```

Therefore, given known-time guarantee feasibility and ordinary threshold/first-crossing continuity:

```text
small L -> fast guarantee-time preference;
near the fast feasibility boundary -> slow preference / slow-only feasibility;
-> at least one finite fast-to-slow guarantee-time crossover.
```

No uniqueness theorem is claimed.

---

## Robust quantitative regime witness — RESOLVED

Detailed record:

`PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`

Reproducible script:

`numerics/paper_a_full_template_feasibility.py`

Use

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=1.2.
```

### Known arrival

The exact dimensionless guarantee root is

```math
\boxed{x_0=1.80519795247.}
```

Hence

```math
T_{G,f}(0)/\tau_f=1.80520,
```

```math
T_{G,s}(0)/\tau_f=2.16624,
```

so the fast channel is quantitatively preferred.

### Finite physical timing uncertainty

Choose the same physical uncertainty for both channels:

```math
\boxed{L=3.30\tau_f=2.75\tau_s.}
```

The full-template feasibility threshold is

```math
c=\rho_0-\Phi^{-1}(\beta)=2.21844843446.
```

Production simulation:

```text
240000 paired paths
seed = 20260818
x_tail = 16
delta = 0.01, 0.005, 0.0025 nested grids
```

The omitted squared-template-energy fraction at `x_tail=16` is only

```math
1-\eta(16)=6.90\times10^{-12}.
```

Results:

| `delta` | slow `ell=2.75` PFA | fast `ell=3.30` PFA |
|---:|---:|---:|
| `0.0100` | `0.04733333` | `0.05362917` |
| `0.0050` | `0.04736250` | `0.05365000` |
| `0.0025` | `0.04737083` | `0.05365833` |

Finest-grid exact 95% Clopper-Pearson **sampling** intervals:

```math
P_{FA,s}\in[0.0465243,0.0482283],
```

```math
P_{FA,f}\in[0.0527601,0.0545674].
```

Because `alpha=0.05` lies cleanly between them,

```math
\boxed{
\text{slow guarantee-feasible / fast guarantee-infeasible}
}
```

at that same physical `L`.

Important numerical wording: the Clopper-Pearson intervals quantify **Monte Carlo sampling uncertainty only**. Timing-grid and filter-tail approximation were checked separately through nested-grid stability and the `6.9e-12` omitted squared-energy fraction. This remains a strong numerical regime witness, not a computer-assisted continuum proof and not a numerical localization of `L_\times`.

The severe review's quantitative-example objection is considered resolved.

---

## Closest prior-art / novelty audit — completed, burden narrowed

Detailed record:

`PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`

Classical spread-spectrum/PN acquisition already establishes acquisition-time dependence on:

```text
unknown code phase / delay search region;
a priori epoch information;
predetection SNR;
detection and false-alarm probability;
dwell / integration strategy;
matched-filter / correlator structure;
serial / parallel / sequential search.
```

Optical acquisition is also established through optical-CDMA synchronization/acquisition and direct-detection ladar in a specified range window.

Additional ladar literature establishes pulse-width / range-resolution and range-estimation tradeoffs. Those are adjacent, not a direct reproduction of the Paper-A theorem.

Therefore do **not** claim novelty for:

```text
unknown-delay search;
search-size penalties;
acquisition time depending on dwell/integration;
PFA/Pd tradeoffs;
optical acquisition;
pulse-width / range-resolution tradeoffs.
```

The only remaining plausible synthesis contribution is:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous rescaling of evidence accumulation and timing-search correlation length
+ one fixed physical arrival-time uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No direct source reproducing that complete detector-scaling construction was found in the audits performed so far.

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

## Mathematical companion — HARD STOP REMAINS ACTIVE

**DO NOT CREATE STEP 50 BY DEFAULT.**

Preserve the correction history:

- Step-13 `ell~49` hard-window grid crossover invalid;
- an invertible noiseless common low-pass does not impose a genuine information bandwidth;
- Step-20 upper Rice switch invalidated by Palm correction;
- raw Step-27 tiny-`chi` values grid biased;
- Step-44 is finite-grid only, not continuum truth;
- Step-46 missed-event run supports sign/scale only, not a precise coefficient;
- Step-47 canonical discrete correction is not the exact finite-`u` false-alarm ratio;
- Steps 48–49 show higher-order covariance does not cancel the dominant rough-grid loss at the needed scale;
- Step 49 intentionally stopped before another publication-grade finite-`u` transfer branch.

The new quantitative witness avoids this branch rather than overriding it.

---

## Exact current claim boundary

Paper A establishes, within the stated idealized family and batch guarantee protocol:

```text
same optical event;
causal time-scaled detector channels;
equal event-specific eventual matched-filter SNR;
finite-time evidence accumulation;
correlated unknown-arrival global threshold;
operational post-window guarantee time;
both / slow-only / neither feasibility partition;
no fast-only feasibility;
at least one finite fast-to-slow guarantee-time crossover;
a robust finite-scale regime witness.
```

It does **not** establish:

```text
exact online or sequential latency;
exact full signal-present scan-time reversal;
Bayes/minimax/sequential optimality;
crossover uniqueness;
universal preference for slower detectors;
a new generic acquisition-time theory;
a universal scalar replacement for D*;
novelty or priority.
```

---

## Active next phase

The previous two major open items are now resolved:

```text
robust quantitative Paper-A example -> RESOLVED;
deeper acquisition / optical-acquisition prior-art audit -> COMPLETED.
```

The next appropriate action is **final integrated adversarial manuscript and citation QA** on `PAPER_A_DRAFT.md`.

Do not reopen the Gaussian-extremes branch unless that final audit identifies a genuinely new mathematical defect requiring it.

### Current single next question

> Does the integrated Paper A survive a fresh hostile-review pass when its theorem, numerical witness, acquisition-theory positioning, references, and claim boundaries are checked together?
