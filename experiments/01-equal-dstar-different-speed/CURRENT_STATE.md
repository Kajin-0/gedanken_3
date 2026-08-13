# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-13 01:14 EDT  
**Status:** **PAPER A TECHNICAL CORE PASSES FINAL INTERNAL ADVERSARIAL QA; EXTERNAL-PAPER PHASE ACTIVE.** The Step-13–49 mathematical closure branch remains hard-stopped. The authoritative theorem manuscript on `main` is unchanged scientifically. On branch `agent/paper-a-submission-package`, a journal-facing *Applied Optics* draft, journal-fit strategy, two external-style referee reviews, and reproducible figure-generation script have been added. **Novelty remains unestablished and no priority language is authorized.**

## Read next

For the scientific theorem:

1. `PAPER_A_DRAFT.md`
2. `PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md`
3. `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
4. `PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`
5. `PROGRESS_LOG.md`

For the active submission phase:

1. `PAPER_A_APPLIED_OPTICS_DRAFT.md`
2. `PAPER_A_SUBMISSION_STRATEGY_2026-08-13.md`
3. `PAPER_A_APPLIED_OPTICS_REFEREE_REVIEW_2026-08-13.md`
4. `PAPER_A_APPLIED_OPTICS_REFEREE_REVIEW_REV2_2026-08-13.md`
5. `numerics/paper_a_submission_figures.py`

---

# 1. Authoritative Paper A theorem

Working theorem title:

> **Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR**

The compared channels receive one common optical event

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

so each channel has the same **event-specific eventual matched-filter SNR**

```math
\rho_{\tau,\infty}=\rho_0.
```

This is distinct from equal scalar `D*`; Paper A does not claim the two assumptions are equivalent.

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

# 2. Operational guarantee time

Event arrival is known only to lie in `[0,L]`. A duration-`t` finite matched filter applied at every candidate arrival requires data through `L+t`, so the result is explicitly a **batch** protocol.

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

# 3. Fast/slow theorem

For

```math
\tau_f<\tau_s,
\qquad
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the exact sufficient-guarantee-time boundary is

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

The manuscript derives rather than assumes

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\quad(\ell\to\infty)
```

and

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit}).
```

Therefore, under ordinary threshold/first-crossing continuity regularity, at least one finite fast-to-slow **guarantee-time** crossover exists. Uniqueness is not established or claimed.

---

# 4. Controlling continuum quantitative witness

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

the full-template threshold budget is

```math
c=2.21844843445540.
```

For the slow channel, Rice's exact expected upcrossing rate plus the endpoint event gives

```math
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<.05.
```

For the fast channel, seven samples over `[0,9]` at spacing `1.5`, followed by Slepian comparison to an equicorrelated Gaussian vector, give

```math
P_{FA,f}
\ge0.0624701020698
>.05.
```

Hence

```math
\boxed{
P_{FA,s}\le.0336428<.05<.0624701\le P_{FA,f},
}
```

which is a **continuous-time slow-only guarantee-feasibility witness** at finite physical `L`.

This result does not locate `L_\times` numerically and does not reopen the rough finite-window branch.

The values `alpha=.05` and `r=6` are used because they produce a transparent analytic separation of the continuum upper and lower bounds. They are **not** proposed as a recommended false-alarm specification or as a representative detector pair.

---

# 5. Active Applied Optics submission package

Current journal-facing title:

> **Task-dependent photodetector ordering under unknown arrival time**

The journal-facing Rev. 3 draft is deliberately separate from the authoritative theorem manuscript.

Current structure:

```text
Introduction
Model and decision protocol
Results
    response time enters the task twice
    continuum feasibility witness
    general feasibility/crossover theorem
Discussion
Conclusion
```

The external-style review sequence produced these presentation changes:

1. show the physical mechanism before the general theorem;
2. present the continuum witness before the crossover proof;
3. explicitly describe `G_tau` as a small-signal optical-to-electrical existence construction;
4. give one scale illustration only:

```text
if tau_f = 10 microseconds,
tau_s = 60 microseconds,
L = 90 microseconds,
```

without associating it with a specific detector technology;
5. explain that `L` can represent trigger/synchronization uncertainty, an asynchronous transient window, a time-of-flight/range gate, or another pre-specified timing window;
6. explicitly state why `alpha=.05` and `r=6` were selected for the analytic witness;
7. keep the abstract near the Optica approximately-100-word target;
8. include Funding, Disclosures, and Data Availability placeholders without inventing author metadata.

Three main figures are defined and generated reproducibly by

`numerics/paper_a_submission_figures.py`:

- **Fig. 1:** accumulated matched-filter SNR fraction versus physical integration time;
- **Fig. 2:** physical full-template timing covariance for fast and slow channels over the same `L`;
- **Fig. 3:** one-sided continuum feasibility bounds around `alpha=.05`.

No smooth numerical `T_G(L)` crossover curve is authorized because no continuum-controlled crossover location has been computed and none is needed for the theorem.

---

# 6. Journal-target position

Current first target: **Applied Optics**.

Reason: the paper is most naturally an applications-centered optical detection / detector-qualification result rather than a claim of new Gaussian-extreme-value theory or a general device-physics model.

Fallback: **Journal of Applied Physics** if a more device/theory-oriented framing becomes preferable.

`Physical Review Applied` remains an aspirational target with a higher editorial-significance burden than the current novelty position justifies.

Journal choice is a submission strategy, not a scientific claim.

---

# 7. Prior-art / novelty position

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

Final position remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

# 8. Historical hard stop

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

# 9. Current next action

Do not reopen the mathematics unless a genuinely new technical defect appears.

The next useful work is external submission preparation:

1. freeze the Rev. 3 journal-facing text after one final regression/readability check;
2. retain the three generated figure files plus their reproduction script;
3. create an Optica-compatible LaTeX/Word submission package only after the scientific text is frozen;
4. perform journal-specific reference formatting and final citation verification;
5. obtain a truly independent referee-style review of the rendered manuscript.
