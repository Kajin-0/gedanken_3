# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 23:22 EDT  
**Status:** mathematical closure branch remains hard-stopped after Step 49. Paper A's acquisition-clock and scan-power claim-scope blockers are repaired. The quantitative regime witness has now been strengthened from Monte Carlo to a **continuum-level slow/fast feasibility bracket** that avoids timing-grid extrapolation. A deeper acquisition / optical-acquisition / ladar prior-art audit has narrowed the novelty burden. **Novelty remains unestablished.** Active work is draft PR #1 on `agent/paper-a-guarantee-semantics`.

Read next:

1. `PAPER_A_DRAFT.md`
2. `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
3. `PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`
4. `PAPER_A_POST_REVISION_AUDIT_2026-08-12.md`
5. `PAPER_A_POST_REVISION_AUDIT_ADDENDUM_2026-08-12.md`
6. `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
7. `PROGRESS_LOG.md`

---

## Authoritative Paper A construction

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

Finite-time accumulation is

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

Event arrival is known only to lie in `[0,L]`. A duration-`t` matched filter applied at every candidate arrival requires data through `L+t`, so the current theorem is explicitly **batch**, not sequential.

Define

```math
\boxed{
T_G=\text{minimum post-window integration duration satisfying the guarantee criterion}.
}
```

and

```math
\boxed{T_{wall}=L+T_G.}
```

At fixed `L`, these induce identical pairwise detector ordering.

For `ell=L/tau`, define

```math
\Gamma(x,\ell,\alpha)
=\inf\left\{u:\Pr[\sup_{0\le q\le\ell}Z_x(q)>u]\le\alpha\right\}.
```

At the generative true alignment `q_0`, which is **analysis-only** and not receiver side information,

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

The complete signal-present scan satisfies

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

Thus the paper orders a **sufficient guarantee time**, not the exact first solution of `P_D^scan=beta`.

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

Fast-only guarantee feasibility is impossible in this scaled equal-eventual-SNR family.

Two former assumptions are now derived:

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\quad(\ell\to\infty),
```

from `R_infty(y)->0` and Slepian comparison; and

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit}),
```

from `eta(x)<1`, `R_x<=R_infty`, threshold ordering, boundary equality, and continuity.

Therefore, assuming known-time feasibility and ordinary threshold/first-crossing continuity, at least one finite fast-to-slow guarantee-time crossover exists. No uniqueness is claimed.

---

## Continuum quantitative regime witness — controlling example

Detailed record:

`PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`

Reproducible calculation:

`numerics/paper_a_analytic_feasibility_bracket.py`

Use

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=\tau_s/\tau_f=6.
```

At known arrival,

```math
\boxed{x_0=1.80519795247,}
```

so

```math
T_{G,f}(0)/\tau_f=1.80520,
```

```math
T_{G,s}(0)/\tau_f=10.83119,
```

and fast is exactly preferred.

Choose one common physical uncertainty

```math
\boxed{L=9\tau_f=1.5\tau_s.}
```

The full-template threshold budget is

```math
c=2.21844843445540.
```

### Slow channel — continuous-time upper bound

For `R_infty''(0)=-1`, the exact Rice mean upcrossing rate is

```math
\nu_c^+=\frac{1}{2\pi}e^{-c^2/2}.
```

The event `sup Z>c` implies either the left endpoint already exceeds `c` or an upcrossing occurs, hence

```math
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<0.05.
```

Thus the slow channel is guarantee-feasible in continuous time.

### Fast channel — continuous-time lower bound

Sample seven points across `[0,9]` separated by `d=1.5`. All off-diagonal covariances are at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Compare by Slepian with

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i,
\qquad i=1,\ldots,7,
```

where the Gaussian variables on the right are independent except for their common `V` component.

The equicorrelated maximum probability is the one-dimensional integral

```math
1-\int\phi(v)
\Phi\left(\frac{c-\sqrt\epsilon v}{\sqrt{1-\epsilon}}\right)^7dv
=0.0624701020698.
```

Therefore

```math
P_{FA,f}
\ge0.0624701020698
>0.05.
```

Thus, at the same physical `L`,

```math
\boxed{
P_{FA,s}\le0.0336428<0.05<0.0624701\le P_{FA,f},
}
```

so the **slow channel is guarantee-feasible while the fast channel is guarantee-infeasible**.

This is the preferred Paper-A regime witness because it does not require timing-grid continuum extrapolation, rare-event asymptotics, or a numerical localization of `L_\times`.

The earlier full-template Monte Carlo file remains an independent cross-check only.

---

## Closest prior art / novelty position

Classical spread-spectrum and PN acquisition already establish acquisition-time dependence on delay/code-phase uncertainty, a-priori epoch information, SNR, detection/false-alarm probability, dwell/integration strategy, and matched-filter/search architecture.

Optical acquisition is also established through optical-CDMA synchronization/acquisition and direct-detection ladar in specified range windows. Additional ladar literature establishes pulse-width / range-resolution and range-estimation tradeoffs.

Therefore do **not** claim novelty for:

```text
unknown-delay search;
search-size penalties;
acquisition time versus dwell/integration;
Pd/Pfa tradeoffs;
optical acquisition;
pulse-width / range-resolution tradeoffs.
```

The remaining plausible synthesis contribution is narrower:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous rescaling of evidence accumulation and timing-search correlation length
+ fixed physical arrival-time uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No reviewed source directly reproduces this complete construction.

Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

## Mathematical companion — HARD STOP REMAINS ACTIVE

**DO NOT CREATE STEP 50 BY DEFAULT.**

Preserve the correction history:

- Step-13 `ell~49` hard-window grid crossover invalid;
- an invertible noiseless common low-pass does not impose genuine information bandwidth;
- Step-20 upper Rice switch invalidated by Palm correction;
- raw Step-27 tiny-`chi` values grid biased;
- Step-44 is finite-grid only, not continuum truth;
- Step-46 missed-event run supports sign/scale only;
- Step-47 canonical discrete correction is not the exact finite-`u` false-alarm ratio;
- Steps 48–49 show higher-order covariance does not cancel the dominant rough-grid loss at the needed scale;
- Step 49 intentionally stopped before another publication-grade finite-`u` transfer branch.

The new continuum witness avoids this branch rather than overriding it.

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
a continuum-bracketed finite-scale regime witness.
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

The final task before any journal-formatting phase is **integrated hostile-review and citation QA**, including synchronization of the authoritative manuscript to the stronger continuum witness.

Do not reopen the Gaussian-extremes branch unless that audit identifies a genuinely new mathematical defect.

### Current single next question

> Does the integrated Paper A survive a fresh hostile-review pass once the continuum witness, theorem, acquisition-theory positioning, references, physical detector realization, and claim boundaries are checked together?
