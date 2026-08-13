# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 23:22 EDT  
**Status:** mathematical closure branch remains hard-stopped after 49 logical steps; Paper A acquisition-clock and scan-power claim-scope blockers repaired; **robust quantitative regime witness now established without reopening Step 50; deeper acquisition / optical-acquisition prior-art audit completed; novelty burden narrowed; novelty not established.** Active work is on draft PR #1, branch `agent/paper-a-guarantee-semantics`.

Read next:

1. `PAPER_A_DRAFT.md`
2. `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
3. `PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`
4. `PAPER_A_POST_REVISION_AUDIT_2026-08-12.md`
5. `PAPER_A_POST_REVISION_AUDIT_ADDENDUM_2026-08-12.md`
6. `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
7. `PROGRESS_LOG.md`

---

## 1. Authoritative Paper A object

Working title:

> **Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR**

The authoritative manuscript on the active branch is `PAPER_A_DRAFT.md`.

The physical construction is

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

so the same optical event produces

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

Finite-time SNR accumulation is

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
\qquad x=t/\tau.
```

The finite-template timing covariance remains

```math
R_x(y)
=\frac{\int_0^{x-y}v(v+y)e^{-2v-y}dv}
{\int_0^xv^2e^{-2v}dv},
```

for `0<=y<x`, and zero beyond the template overlap.

The full-template limit is

```math
\boxed{
R_\infty(y)=(1+|y|)e^{-|y|}.
}
```

---

## 2. Operational guarantee-time semantics — repaired

Event arrival is known only to satisfy

```math
0\le\theta\le L.
```

A duration-`t` finite matched filter applied to every candidate arrival requires data through `L+t`. The paper therefore studies a **batch** receiver.

The central object is

```math
\boxed{
T_G=\text{minimum post-window integration duration satisfying the guarantee criterion}.
}
```

The wall-clock batch time is

```math
\boxed{
T_{wall}=L+T_G.
}
```

At fixed `L`, `T_G` and `T_wall` induce identical pairwise channel ordering.

The global noise-only threshold is

```math
\Gamma(x,\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>u\right]\le\alpha
\right\},
\qquad \ell=L/\tau.
```

At the generative true alignment `q0`, which is an **analysis variable only and is not supplied to the receiver**,

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

The complete signal-present scan probability satisfies pathwise

```math
\boxed{
P_D^{scan}\ge P_{D,true}.
}
```

Thus the paper proves ordering of a **sufficient guarantee time**, not exact ordering of the first solutions of `P_D^scan=beta`.

Define

```math
X_G(\rho_0,\alpha,\beta,\ell)
=\inf\{x:
\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\ge\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G(\rho_0,\alpha,\beta,L/\tau).
}
```

---

## 3. Fast/slow theorem — current strengthened form

For

```math
\tau_f<\tau_s,
\qquad
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the exact guarantee-time boundary is

```math
\boxed{
B_r(\ell)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
}
```

The full-template guarantee-feasibility budget is

```math
c=\rho_0-\Phi^{-1}(\beta).
```

The regimes are

```math
\begin{array}{ll}
\text{both feasible:} & c>\Gamma_\infty(r\ell,\alpha),\\
\text{slow only:} & \Gamma_\infty(\ell,\alpha)<c\le\Gamma_\infty(r\ell,\alpha),\\
\text{neither:} & c\le\Gamma_\infty(\ell,\alpha).
\end{array}
```

Fast-only guarantee feasibility is impossible in this equal-eventual-SNR scaled family.

The physical feasibility limit obeys

```math
L_{crit}(\tau)=\tau\ell_{crit}.
```

Two former assumptions are now derived:

1. `Gamma_infty(ell,alpha)->infinity` follows from `R_infty(y)->0` and Slepian comparison with widely separated/equicorrelated Gaussian samples.
2. `X_G(ell)->infinity` as `ell->ell_crit` from below follows from `eta(x)<1`, `R_x<=R_infty`, threshold ordering, boundary equality, and continuity.

Therefore, assuming known-time guarantee feasibility and ordinary threshold/first-crossing continuity:

```text
small L -> fast guarantee-time preference;
near fast feasibility boundary -> slow preference / slow-only feasibility;
-> at least one finite fast-to-slow guarantee-time crossover.
```

No uniqueness theorem.

---

## 4. NEW — robust quantitative regime witness

File:

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

The exact dimensionless root is

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

so fast is quantitatively preferred.

### Finite physical timing uncertainty

Choose

```math
\boxed{
L=3.30\tau_f=2.75\tau_s.
}
```

The full-template feasibility threshold is

```math
c=\rho_0-\Phi^{-1}(\beta)
=2.21844843446.
```

A paired `120000`-path simulation of the smooth full-template process used `x_tail=12`, leaving only

```math
1-\eta(12)=1.18\times10^{-8}
```

of squared template energy outside the numerical filter.

Nested timing grids gave:

| `delta` | slow `ell=2.75` PFA | fast `ell=3.30` PFA |
|---:|---:|---:|
| `0.0100` | `0.0472083` | `0.0539250` |
| `0.0050` | `0.0472417` | `0.0539583` |
| `0.0025` | `0.0472417` | `0.0539583` |

Finest-grid exact 95% Clopper-Pearson intervals:

```math
P_{FA,s}\in[0.0460481,0.0484572],
```

```math
P_{FA,f}\in[0.0526866,0.0552516].
```

Since `alpha=0.05` lies cleanly between them:

```math
\boxed{
\text{slow guarantee-feasible / fast guarantee-infeasible}
}
```

at that same physical `L`.

This is a **regime witness**, not a numerical localization of `L_x`.

The key methodological advantage is that the witness uses the smooth **full-template feasibility process**, so it does not suffer the Step-13 hard-window covariance cusp. The Step-49 hard stop remains intact.

The severe review's request for a robust quantitative Paper-A example is therefore considered **resolved**.

---

## 5. NEW — closest prior-art / acquisition-lineage audit

File:

`PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`

The deeper audit materially narrowed the novelty burden.

Classical PN/spread-spectrum acquisition already establishes that acquisition time depends on combinations of:

```text
unknown code phase / delay search region;
a priori epoch information;
predetection SNR;
detection probability;
false-alarm probability;
dwell / integration strategy;
matched-filter / correlator receiver structure;
serial / parallel / sequential search architecture.
```

Canonical matched-filter acquisition sources include Polydoros & Weber (1984) and Su (1988).

The same conceptual structure exists in **optical** systems:

- Mustapha & Ormondroyd 2000: optical-CDMA sequential synchronization / mean acquisition time;
- Keshavarzian & Salehi 2002: optical orthogonal code serial-search acquisition;
- Pham & Yashima 2005: multiple-dwell serial-search optical-CDMA acquisition;
- Milstein et al. 2008: direct-detection Geiger-mode APD ladar acquisition in a specified range window under constant false alarm.

Therefore Paper A must NOT claim novelty for

```text
unknown delay search;
search-size penalties;
acquisition time depending on dwell/integration;
PFA/Pd tradeoffs;
optical acquisition itself.
```

The only remaining plausible synthesis contribution is narrower:

```text
same optical event
+ causal photodetector channel family
+ equal eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous rescaling of evidence accumulation and timing-search correlation length
+ one fixed physical arrival uncertainty
-> fast/slow guarantee-time ordering reversal and slow-only feasibility.
```

No direct source reproducing that full detector-scaling construction was found in this audit.

Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

## 6. Historical numerical hard stop — remains active

**DO NOT CREATE STEP 50 BY DEFAULT.**

Preserve these invalidations/corrections:

- Step-13 `ell~49` hard-window grid crossover invalid;
- an invertible noiseless common low-pass does not by itself impose finite information bandwidth;
- Step-20 upper Rice switch invalidated by Palm correction;
- raw Step-27 tiny-`chi` values grid biased;
- Step-44 is a finite-grid pointwise certificate, not continuum truth;
- Step-46 missed-event run supports sign/scale only, not a precise coefficient;
- Step-47 pure-alpha1 correction is not the exact finite-`u` false-alarm ratio;
- Steps 48–49 show higher-order covariance structure does not cancel the dominant rough-grid loss at the needed scale;
- Step 49 intentionally stopped before another publication-grade finite-`u` closure branch.

The new Paper-A witness avoids this branch rather than overriding it.

---

## 7. Exact current claim boundary

Paper A now establishes, within the stated idealized family and batch guarantee protocol:

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

It does NOT establish:

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

## 8. Active next phase

The two major open items from the previous state are now resolved:

```text
robust Paper-A quantitative example -> RESOLVED via full-template regime witness;
deeper acquisition prior-art audit -> COMPLETED, novelty burden narrowed.
```

The next appropriate action is **final adversarial manuscript and citation QA** on the current integrated `PAPER_A_DRAFT.md`.

Do not reopen the Gaussian-extremes branch unless that final audit identifies a genuinely new mathematical defect requiring it.

### Current single next question

> Does the integrated Paper A now survive a fresh hostile-review pass when its theorem, numerical witness, acquisition-theory positioning, references, and claim boundaries are checked together?
