# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-13 01:14 EDT  
**Status:** **PAPER A TECHNICAL CORE PASSES FINAL INTERNAL ADVERSARIAL QA; APPLIED OPTICS MANUSCRIPT HAS BEEN TYPESET AND PAGE-QA'D.** The Step-13–49 Gaussian-extremes branch remains hard-stopped. The scientific theorem is frozen unless a genuinely new defect appears. Novelty remains unestablished and no priority language is authorized.

## Read next

1. `PAPER_A_DRAFT.md` — authoritative audited theorem manuscript
2. `PAPER_A_APPLIED_OPTICS_DRAFT.md` — journal-facing scientific text (Rev. 3; final rendered bibliography is superseded by the reference audit where noted)
3. `PAPER_A_OPTICA_RENDER_QA_2026-08-13.md`
4. `PAPER_A_REFERENCE_AUDIT_2026-08-13.md`
5. `PAPER_A_APPLIED_OPTICS_COVER_LETTER.md`
6. `PAPER_A_SUBMISSION_READINESS_2026-08-13.md`
7. `PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md`
8. `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
9. `PROGRESS_LOG.md`

---

# Scientific theorem — frozen state

All detector channels receive the same optical event

```math
p(t)=e^{-bt}u(t),
```

through the controlled causal channel family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

giving

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

The transfer family is an **existence construction** used to isolate temporal scaling, not a generic microscopic detector model. For a finite pair `tau_f<tau_s`, choosing `b>=1/tau_f` makes both channel impulse responses nonnegative.

With

```math
E[n(t)n(t')]=N\delta(t-t'),
```

choose

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

so all channels have the same **event-specific eventual matched-filter SNR**

```math
\rho_{\tau,\infty}=\rho_0.
```

This is not the same assumption as equal conventional scalar `D*`.

Finite-time evidence accumulation is

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)},
\qquad x=t/\tau.
```

The full-template timing covariance is

```math
R_\infty(y)=(1+|y|)e^{-|y|}.
```

---

# Operational quantity and claim boundary

Arrival is known only to lie in `[0,L]`. A duration-`t` matched filter evaluated for every candidate requires data through `L+t`, so the protocol is explicitly **batch**.

Define

```math
T_G=\text{minimum post-window integration duration satisfying the sufficient guarantee},
```

with

```math
T_{wall}=L+T_G.
```

For normalized search length

```math
\ell=L/\tau,
```

the global noise-only threshold is

```math
\Gamma(x,\ell,\alpha)
=\inf\{u:\Pr[\sup_{0\le q\le\ell}Z_x(q)>u]\le\alpha\}.
```

At the true generative alignment `q_0`, used only for analysis,

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)].
```

The receiver is not given `q_0`; it scans the full interval. Pathwise,

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

Therefore Paper A proves ordering of a **sufficient guarantee time**, not exact full-scan detection time and not online/sequential latency.

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

# Fast/slow theorem

For

```math
\tau_f<\tau_s,
\qquad
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the sufficient-guarantee-time boundary is

```math
B_r(\ell)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
```

With

```math
c=\rho_0-\Phi^{-1}(\beta),
```

only three full-template feasibility regimes exist:

```math
\begin{array}{ll}
\text{both feasible:} & c>\Gamma_\infty(r\ell,\alpha),\\
\text{slow only:} & \Gamma_\infty(\ell,\alpha)<c\le\Gamma_\infty(r\ell,\alpha),\\
\text{neither:} & c\le\Gamma_\infty(\ell,\alpha).
\end{array}
```

Fast-only feasibility is impossible within this deliberately scaled family.

The manuscript derives

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\quad(\ell\to\infty)
```

and

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit}).
```

Thus fast is preferred at known arrival, reaches its physical guarantee-feasibility boundary first, and under ordinary continuity regularity at least one finite fast-to-slow guarantee-time crossover exists. Crossover uniqueness is not claimed.

---

# Controlling continuum quantitative witness

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

These are proof-friendly witness values chosen so the continuous-time bounds separate transparently. They are not recommended false-alarm specifications and are not claimed to be a representative detector pair.

Known arrival gives

```math
x_0=1.80519795247291,
```

so fast is exactly preferred.

At one common physical uncertainty

```math
\boxed{L=9\tau_f=1.5\tau_s,}
```

the threshold budget is

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

For the fast channel, a seven-point sampled subset plus Slepian comparison to an equicorrelated Gaussian vector gives

```math
P_{FA,f}\ge0.0624701020698>.05.
```

Hence

```math
\boxed{
P_{FA,s}\le.0336428<.05<.0624701\le P_{FA,f}.
}
```

This is a **continuous-time slow-only guarantee-feasibility witness**. It does not numerically locate the crossover.

---

# Applied Optics submission package

Current journal-facing title:

> **Task-dependent photodetector ordering under unknown arrival time**

Current first target: **Applied Optics**.

The manuscript is applications-facing rather than a claim of new Gaussian-extreme-value theory. It explicitly connects `L` to optical timing uncertainty such as trigger/synchronization uncertainty, asynchronous transient timing, or a time-of-flight/range gate.

One dimensional mapping is illustrative only:

```text
tau_f = 10 microseconds
tau_s = 60 microseconds
L = 90 microseconds
```

No detector material is assigned to these numbers.

Three main figures are generated by

`numerics/paper_a_submission_figures.py`:

1. accumulated matched-filter SNR fraction versus physical integration time;
2. physical timing covariance over the same `L`;
3. one-sided continuum false-alarm bounds around `alpha=.05`.

No numerical `T_G(L)` crossover curve is authorized.

---

# Rendered manuscript QA

A standard single-file LaTeX version has been compiled locally into an **11-page letter-size PDF** and visually inspected page by page at the key title/figure/reference locations.

Production checks:

```text
LaTeX compile: PASS
PDF opens/preflight: PASS
no clipping/overlap/broken glyphs: PASS
all three figure pages: PASS
reference pages after citation repair: PASS
```

The first TeX pass exposed a package conflict between `newtxmath` and redundant `amssymb`; removing `amssymb` fixed the compile without changing manuscript mathematics.

After the first visual render, the title was made left-aligned and figure labels were changed from `Figure` to `Fig.`.

See `PAPER_A_OPTICA_RENDER_QA_2026-08-13.md`.

---

# Citation audit correction

The final rendered source corrects two material bibliography errors that remained in the earlier Markdown Rev. 3:

### Croce et al. 2004

Correct author order/list:

```text
R. P. Croce; Th. Demma; M. Longo; S. Marano; V. Matta; V. Pierro; I. M. Pinto.
```

### Milstein et al. 2008

Correct Applied Optics author list:

```text
Adam B. Milstein; Leaf A. Jiang; Jane X. Luu; Eric L. Hines; Kenneth I. Schultz.
```

The rendered LaTeX/PDF and `PAPER_A_REFERENCE_AUDIT_2026-08-13.md` are controlling for final citation metadata. The older Markdown Rev. 3 reference list is superseded where it conflicts with that audit.

No scientific conclusion changed.

---

# Prior art and novelty

Established ingredients include:

```text
pulse/energy detectivity from D*(f);
sensitivity-bandwidth combinations;
unknown-delay/code-phase acquisition;
search-region / Pd / Pfa / dwell / SNR acquisition tradeoffs;
matched-filter acquisition;
optical-CDMA acquisition and synchronization;
direct-detection ladar acquisition in range windows;
pulse-width/range-resolution and range-estimation tradeoffs.
```

The remaining possible synthesis contribution is the narrow detector-scaling construction:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ response-time variation
+ simultaneous evidence-clock and timing-search-correlation rescaling
+ fixed physical timing uncertainty
-> task-dependent sufficient-guarantee-time ordering and slow-only feasibility.
```

Final status remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

# Historical hard stop

**DO NOT CREATE STEP 50 BY DEFAULT.**

Do not revive:

- invalid Step-13 `ell~49` grid crossover;
- invertible common low-pass as genuine finite information bandwidth;
- invalid Step-20 upper Rice switch;
- raw Step-27 tiny-`chi` values;
- Step-44 finite-grid certificate as continuum truth;
- Step-46 five-event run as a precise coefficient measurement;
- Steps 47–49 as exact finite-`u` scan-power closure.

The controlling Paper-A continuum witness avoids this branch entirely.

---

# Remaining before real submission

The following are now the only obvious production blockers:

1. confirm author name(s), affiliation(s), and corresponding-author email;
2. confirm Funding statement;
3. confirm Disclosures/conflicts statement;
4. decide whether to archive a versioned repository release/DOI for the final Data Availability statement;
5. update the final journal-facing bibliography from the citation audit if using the Markdown source;
6. submit the rendered manuscript plus required cover letter through Optica Prism only after author metadata are final.

A cover-letter draft is in `PAPER_A_APPLIED_OPTICS_COVER_LETTER.md`.

Do not reopen the mathematics unless external review identifies a genuinely new technical defect.
