# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 23:22 EDT  
**Status:** **PAPER A TECHNICAL CORE PASSES FINAL INTERNAL ADVERSARIAL QA.** Mathematical closure remains hard-stopped after Step 49. The acquisition-clock and scan-power claim-scope blockers are repaired; the quantitative regime witness is continuum-bracketed without timing-grid extrapolation; acquisition/optical-acquisition/ladar prior art is explicitly incorporated; the authoritative manuscript has been synchronized to the final audit. **Novelty remains unestablished and no priority language is authorized.**

Read next:

1. `PAPER_A_DRAFT.md`
2. `PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md`
3. `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
4. `PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`
5. `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`
6. `PROGRESS_LOG.md`

---

## Authoritative Paper A claim

Working title:

> **Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR**

The compared channels receive the same optical event

```math
p(t)=e^{-bt}u(t)
```

through the causal, stable, proper family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

producing

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

The pole-zero matching is a controlled **existence construction**, not a proposed generic microscopic detector model. Its impulse response is

```math
g_\tau(t)
=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac1\tau\right)t\right]u(t).
```

For a finite pair with `tau_f<tau_s`, choosing

```math
b\ge1/\tau_f
```

makes both channel impulse responses nonnegative.

With

```math
E[n(t)n(t')]=N\delta(t-t'),
```

choose

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

so every channel has the same **event-specific eventual matched-filter SNR**

```math
\rho_{\tau,\infty}=\rho_0.
```

This is distinct from equal scalar `D*`; Paper A does not claim the two are equivalent.

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

## Operational guarantee time

Event arrival is known only to lie in `[0,L]`. A duration-`t` finite matched filter applied at every candidate arrival requires data through `L+t`, so the theorem is explicitly a **batch** result.

Define

```math
\boxed{
T_G=\text{minimum post-window integration duration satisfying the guarantee criterion},
}
```

with wall-clock batch time

```math
\boxed{T_{wall}=L+T_G.}
```

At fixed `L`, these induce identical channel ordering.

For `ell=L/tau`, the global noise-only threshold is

```math
\Gamma(x,\ell,\alpha)
=\inf\{u:\Pr[\sup_{0\le q\le\ell}Z_x(q)>u]\le\alpha\}.
```

At the generative true alignment `q_0`, which is analysis-only and **not** supplied to the receiver,

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

Pathwise,

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

Thus Paper A orders a **sufficient guarantee time**, not the exact first solution of `P_D^{scan}=beta`.

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

## Fast/slow theorem

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

Let

```math
c=\rho_0-\Phi^{-1}(\beta).
```

The full-template feasibility partition is

```math
\begin{array}{ll}
\text{both feasible:} & c>\Gamma_\infty(r\ell,\alpha),\\
\text{slow only:} & \Gamma_\infty(\ell,\alpha)<c\le\Gamma_\infty(r\ell,\alpha),\\
\text{neither:} & c\le\Gamma_\infty(\ell,\alpha).
\end{array}
```

Fast-only guarantee feasibility is impossible in this scaled family.

The manuscript now derives rather than assumes

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\quad(\ell\to\infty)
```

and

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit}),
```

leaving only ordinary threshold/first-crossing continuity regularity plus known-time feasibility as theorem assumptions.

Therefore at least one finite fast-to-slow **guarantee-time** crossover exists. Uniqueness is not established or claimed.

---

## Controlling continuum quantitative witness

Detailed record:

`PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`

Reproducible calculation:

`numerics/paper_a_analytic_feasibility_bracket.py`

Use

```math
\rho_0=3.5,
\qquad
\alpha=.05,
\qquad
\beta=.90,
\qquad
r=\tau_s/\tau_f=6.
```

Known arrival gives

```math
x_0=1.80519795247291,
```

so fast is exactly preferred.

At the common physical uncertainty

```math
\boxed{L=9\tau_f=1.5\tau_s,}
```

the threshold budget is

```math
c=2.21844843445540.
```

### Slow channel

For `R_infty''(0)=-1`, Rice's exact expected upcrossing rate gives

```math
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<.05.
```

This bound is sufficient to establish

```math
\Gamma_\infty(1.5,.05)<c,
```

so the slow channel is guarantee-feasible in continuous time.

### Fast channel

Seven samples over `[0,9]` at spacing `1.5` have off-diagonal covariance at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Slepian comparison with a seven-dimensional equicorrelated Gaussian vector gives

```math
P_{FA,f}
\ge0.0624701020698
>.05.
```

This lower bound establishes

```math
\Gamma_\infty(9,.05)>c,
```

so the fast channel is guarantee-infeasible at the same physical `L`.

Hence

```math
\boxed{
P_{FA,s}\le.0336428<.05<.0624701\le P_{FA,f},
}
```

which brackets the two channels on opposite sides of the full-template guarantee-feasibility boundary.

This is a continuous-process feasibility bracket. It does not locate `L_\times` numerically and does not reopen the rough finite-window branch.

---

## Prior-art / novelty position

Established prior art includes:

```text
pulse/energy detectivity from D*(f);
sensitivity-bandwidth combinations;
unknown-delay/code-phase acquisition;
search-region / Pd / Pfa / dwell / SNR acquisition tradeoffs;
matched-filter acquisition;
optical-CDMA synchronization/acquisition;
direct-detection ladar acquisition in specified range windows;
pulse-width / range-resolution and range-estimation tradeoffs.
```

Therefore none of those broad ingredients are claimed as new.

The remaining possible synthesis contribution is the narrower detector-scaling construction:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous rescaling of evidence accumulation and timing-search correlation length
+ fixed physical arrival uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No reviewed source directly reproduced that complete construction, but absence of a direct hit does not establish novelty.

Final position:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

## Historical hard stop

**DO NOT CREATE STEP 50 BY DEFAULT.**

Preserve these corrections:

- Step-13 `ell~49` grid crossover invalid;
- invertible noiseless common low-pass is not genuine finite information bandwidth;
- Step-20 upper Rice switch invalidated by Palm correction;
- raw Step-27 tiny-`chi` values grid biased;
- Step-44 is finite-grid only, not continuum truth;
- Step-46 five-event run supports sign/scale only;
- Step-47 canonical discrete correction is not the exact finite-`u` false-alarm ratio;
- Steps 48–49 show higher-order covariance does not cancel the dominant rough-grid loss at the needed scale;
- Step 49 intentionally stopped before another publication-grade finite-`u` transfer branch.

The final Paper-A continuum witness avoids this branch entirely.

---

## Final internal QA disposition

From `PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md`:

```text
MATHEMATICAL CONSISTENCY: PASS
OPERATIONAL TASK DEFINITION: PASS
CLAIM SCOPE: PASS
CONTINUUM QUANTITATIVE WITNESS: PASS
HARD-STOP DISCIPLINE: PASS
PRIOR-ART HONESTY: PASS
NOVELTY: NOT ESTABLISHED
CROSSOVER UNIQUENESS: NOT ESTABLISHED / NOT CLAIMED
EXACT FULL-SCAN DETECTION-TIME REVERSAL: NOT ESTABLISHED / NOT CLAIMED
```

Regression search of the synchronized manuscript found no obsolete `T_D`, no old `r=1.2` controlling witness, and no accidental full-scan/online claim.

---

## Next phase

No additional Gaussian-extremes closure work is currently justified.

The appropriate next phase is external-style paper preparation or independent review:

```text
figure design / phase-regime graphic;
journal-format rendering;
fresh independent referee report;
final journal-specific literature/citation check.
```

Keep novelty language conservative unless a subsequent priority audit provides materially stronger evidence.