# Paper A — Final Integrated Adversarial QA

**Date:** 2026-08-12  
**Status:** TECHNICAL CORE PASSES / AUTHORITATIVE MANUSCRIPT SYNCHRONIZED / NOVELTY NOT ESTABLISHED

This file is the final disposition after the complete Step-01–49 history, the severe adversarial review, the guarantee-time semantic repair, the acquisition-lineage audit, the continuum feasibility witness, and the final manuscript regression pass were checked together. The longer pre-synchronization version of this audit remains preserved in Git history; `PROGRESS_LOG.md` preserves the detailed path, failed branches, corrections, and reasons.

---

## Final referee-style disposition

I do **not** find a fatal mathematical, probabilistic, or operational contradiction in the current Paper-A technical core.

```text
INTERNAL MATHEMATICAL CONSISTENCY: PASS
OPERATIONAL TASK DEFINITION: PASS
CLAIM SCOPE: PASS
CONTINUUM QUANTITATIVE WITNESS: PASS
HARD-STOP DISCIPLINE: PASS
PRIOR-ART HONESTY: PASS
NOVELTY: NOT ESTABLISHED
CROSSOVER UNIQUENESS: NOT ESTABLISHED / NOT CLAIMED
EXACT FULL-SCAN DETECTION-TIME REVERSAL: NOT ESTABLISHED / NOT CLAIMED
```

No additional Gaussian-extremes closure branch is justified by the present manuscript.

---

## 1. Detector normalization — PASS

For

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

with

```math
E[n(t)n(t')]=N\delta(t-t'),
```

the eventual matched-filter SNR is

```math
\rho_{\tau,\infty}^2
=\frac{A_\tau^2\tau^3}{4N}.
```

Thus

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

gives

```math
\rho_{\tau,\infty}=\rho_0
```

for every channel in the family. The finite squared-SNR fraction remains

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\eta'(x)=4x^2e^{-2x}>0.
```

No normalization regression was found.

---

## 2. Physical realization — PASS AS AN EXISTENCE CONSTRUCTION

All channels receive

```math
p(t)=e^{-bt}u(t)
```

through

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

which is causal, stable, and proper and gives the required output family.

The authoritative manuscript now explicitly says that the pole-zero matching is a **controlled existence construction**, not a generic microscopic detector model.

The channel impulse response is

```math
\boxed{
g_\tau(t)
=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac1\tau\right)t\right]u(t).
}
```

For a finite pair `tau_f<tau_s`, choosing

```math
b\ge1/\tau_f
```

makes both compared impulse responses nonnegative for all `t>=0`.

---

## 3. Equal eventual SNR versus equal D* — PASS

Paper A does **not** assume that equal scalar conventional `D*` implies equal eventual event SNR.

The active theorem instead imposes the distinct event-specific normalization

```math
\rho_{\tau,\infty}=\rho_0
```

to remove eventual matched-filter sensitivity as a confounding variable for the chosen optical event.

The synchronized manuscript explicitly states that this normalization must not be identified with equality of scalar `D*`.

---

## 4. Acquisition clock — ORIGINAL BLOCKER RESOLVED

The event is known to arrive in `[0,L]`. A duration-`t` matched filter evaluated at every candidate arrival requires a record through `L+t`.

The paper therefore defines

```math
T_G=\text{minimum required post-window integration duration}
```

and

```math
T_{wall}=L+T_G.
```

For fixed `L`, the added term is common to both channels and does not change the ordering.

The result is explicitly batch, not a generic sequential or online detection-latency theorem.

---

## 5. True-alignment guarantee — STRONGEST ORIGINAL BLOCKER RESOLVED

The manuscript distinguishes

```math
P_{D,true}=\Pr[Y_x(q_0)>\Gamma]
```

from

```math
P_D^{scan}=\Pr[\sup_qY_x(q)>\Gamma].
```

`q_0` is analysis-only and is not supplied to the receiver.

Pathwise,

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

Thus `P_D,true>=beta` is a sufficient guarantee that the complete scan detects with probability at least `beta`.

The theorem orders the corresponding **guarantee time**. It does not claim ordering of the exact first solutions of

```math
P_D^{scan}(t)=\beta.
```

---

## 6. Covariance ordering and guarantee-time surface — PASS

The finite-template timing covariance is monotone in integration duration:

```math
x_2>x_1
\Longrightarrow
R_{x_2}(y)\ge R_{x_1}(y).
```

Slepian comparison therefore gives

```math
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
```

Together with increasing signal accumulation, the guarantee margin is strictly increasing in `x`.

The physical scaling is

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G(\rho_0,\alpha,\beta,L/\tau).
}
```

---

## 7. Full-template limit and theorem strengthening — PASS

The full-template covariance is

```math
R_\infty(y)=(1+|y|)e^{-|y|}.
```

The manuscript defines its threshold directly and relates the finite templates through

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
```

Threshold convergence is stated under ordinary compact-interval Gaussian-supremum/quantile continuity regularity rather than silently assumed as a proved theorem.

Two assumptions in the earlier crossover proposition are now derived:

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\qquad(\ell\to\infty),
```

using widely separated samples and Slepian comparison, and

```math
X_G(\ell)\to\infty
\qquad(\ell\uparrow\ell_{crit}),
```

using `eta(x)<1`, `R_x<=R_infty`, threshold ordering, boundary equality, and continuity.

---

## 8. Feasibility partition and crossover — PASS

For `tau_f<tau_s`, define

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s.
```

The fast and slow normalized searches are `r ell` and `ell`.

With

```math
c=\rho_0-\Phi^{-1}(\beta),
```

the family permits only

```text
both guarantee-feasible
slow guarantee-feasible only
neither guarantee-feasible
```

and excludes fast-only feasibility.

Fast is preferred at known arrival. The fast channel reaches its physical feasibility boundary first and its guarantee time diverges there while the slow channel remains feasible. Under the stated continuity regularity, at least one finite fast-to-slow guarantee-time crossover follows.

No uniqueness theorem is claimed.

---

## 9. Continuum quantitative witness — STRONG PASS

The controlling example uses

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
x_0=1.80519795247291,
```

so the fast channel is exactly preferred.

Choose

```math
\boxed{L=9\tau_f=1.5\tau_s.}
```

Then

```math
\ell_f=9,
\qquad
\ell_s=1.5,
\qquad
c=2.21844843445540.
```

### Slow side

Since

```math
R_\infty''(0)=-1,
```

Rice's exact mean-upcrossing formula and a union bound give

```math
\boxed{
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<0.05.
}
```

This upper bound is sufficient to establish

```math
\Gamma_\infty(\ell_s,\alpha)<c,
```

so the slow channel is guarantee-feasible.

### Fast side

Take seven points over `[0,9]` at spacing `1.5`. Every off-diagonal covariance is at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Slepian comparison with a seven-dimensional equicorrelated Gaussian vector gives

```math
\boxed{
P_{FA,f}
\ge0.0624701020698
>0.05.
}
```

This lower bound establishes

```math
\Gamma_\infty(\ell_f,\alpha)>c,
```

so the fast channel is guarantee-infeasible.

Therefore

```math
\boxed{
P_{FA,s}\le0.0336428
<0.05
<0.0624701\le P_{FA,f}.
}
```

This is a continuous-process slow-only feasibility witness. It does not require a timing-grid continuum extrapolation, a rare-event approximation to `P_FA`, or a numerical localization of `L_\times`.

The previous full-template Monte Carlo witness remains only an independent cross-check.

---

## 10. Hard-stop discipline — PASS

The final Paper-A argument does **not** revive the invalid or incomplete Step-13–49 branches.

In particular, it does not use:

```text
Step-13 ell~49 rough-grid crossover;
Step-20 upper Rice switch;
raw Step-27 tiny-chi values;
Step-44 as continuum truth;
Step-47 as an exact finite-u false-alarm ratio;
Steps 48–49 as an exact finite-u scan-power closure.
```

**Do not create Step 50 by default.**

---

## 11. Prior-art positioning — PASS, NOVELTY UNRESOLVED

The manuscript now acknowledges as established:

```text
pulse/energy detectivity from frequency-dependent sensitivity;
sensitivity-bandwidth combinations;
unknown-delay/code-phase acquisition;
search-region / SNR / Pd / Pfa / dwell tradeoffs;
matched-filter acquisition;
optical-CDMA acquisition and synchronization;
direct-detection ladar acquisition in range windows;
pulse-width / range-resolution and range-estimation tradeoffs.
```

The only remaining plausible synthesis contribution is the narrower coupling:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous evidence-clock and search-correlation rescaling
+ fixed physical arrival uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No reviewed source directly reproduced that complete construction, but absence of a direct hit is not proof of novelty.

Final position:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

## 12. Reference and regression QA — PASS

The synchronized manuscript includes appropriate claim-boundary references for detector sensitivity, Gaussian comparison, acquisition theory, optical acquisition, direct-detection ladar, and Rice upcrossings.

Regression search of `PAPER_A_DRAFT.md` found:

```text
obsolete T_D symbols: none
old r=1.2 controlling witness: none
"stronger than equal D*" wording: none
q0 treated as receiver side information: no
exact full-scan reversal claimed: no
online/sequential latency claimed: no
continuum r=6 witness present: yes
Rice primary reference present: yes
constructed-detector limitation present: yes
```

---

## Final stopping point

The current Paper-A technical core is internally coherent at the level tested here. I would **not** recommend another Gaussian-extremes or crossover-localization branch before manuscript preparation.

The appropriate next phase is external-style review or paper preparation:

```text
figure / regime-diagram design;
journal-specific formatting and citation checks;
a genuinely independent referee pass;
submission-target selection.
```

Keep novelty language conservative unless later priority work materially changes the evidence.