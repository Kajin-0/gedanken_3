# Paper A — Final Integrated Adversarial QA

**Date:** 2026-08-12  
**Status:** TECHNICAL CORE PASSES / NO NEW FATAL MATHEMATICAL DEFECT FOUND / FINAL MANUSCRIPT SYNCHRONIZATION REQUIRED / NOVELTY NOT ESTABLISHED

---

## 1. Referee-style disposition

After re-reading the full Step-01–49 correction history, the adversarial-review repair, the current Paper-A manuscript, the new continuum feasibility witness, and the deeper acquisition-lineage audit, I do **not** find a new fatal contradiction in the central result.

The appropriate disposition has improved from

```text
MAJOR REVISION BEFORE SUBMISSION
```

to

```text
TECHNICAL CORE PASSES.
FINAL CLAIM/CITATION/MANUSCRIPT SYNCHRONIZATION REQUIRED.
NOVELTY NOT ESTABLISHED.
```

The two original blocking problems are genuinely repaired:

1. the acquisition clock is now operationally explicit;
2. the theorem is explicitly about a conservative guarantee time, not the exact full signal-present scan detection time.

The new continuum quantitative witness also removes the strongest numerical-presentation objection without reopening the Step-49 hard stop.

---

## 2. Central detector normalization — PASS

For

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t)
```

and

```math
E[n(t)n(t')]=N\delta(t-t'),
```

```math
\rho_{\tau,\infty}^2
=\frac1N\int_0^\infty s_\tau^2(t)dt
=\frac{A_\tau^2\tau^3}{4N}.
```

Thus

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

indeed gives

```math
\rho_{\tau,\infty}=\rho_0.
```

The finite squared-SNR fraction remains

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
```

with

```math
\eta'(x)=4x^2e^{-2x}>0.
```

No factor-of-two or normalization regression was found.

---

## 3. Physical detector realization — VALID EXISTENCE CONSTRUCTION, BUT PRESENT IT HONESTLY

The manuscript uses the common optical event

```math
p(t)=e^{-bt}u(t)
```

and detector channel

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

which yields

```math
G_\tau(s)P(s)=\frac{A_\tau}{(s+1/\tau)^2}
```

and therefore the desired output family.

This is causal, stable, and proper for `b,tau>0`.

A hostile reviewer may nevertheless object that the zero at `-b` is deliberately matched to the chosen event pole. That objection does **not** invalidate the counterexample, but the paper should not imply that this is a generic microscopic photodetector transfer function.

There is an additional useful physical check. The detector impulse response is

```math
\boxed{
g_\tau(t)
=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac1\tau\right)t\right]u(t).
}
```

For a compared pair with `tau_f<tau_s`, choosing

```math
\boxed{b\ge1/\tau_f}
```

makes

```math
g_{\tau_f}(t)\ge0,
\qquad
g_{\tau_s}(t)\ge0
```

for all `t>=0`. Thus the existence construction need not rely on a sign-changing detector impulse response.

### Required final wording

Add a compact sentence making both points explicit:

```text
The pole-zero matching is part of the controlled existence construction, not a claim of generic detector microphysics; for a finite fast/slow pair one may choose b>=1/tau_f, which makes both channel impulse responses nonnegative.
```

**Disposition:** NOT BLOCKING after this wording.

---

## 4. Equal eventual SNR versus equal D* — CLAIM BOUNDARY MUST REMAIN EXPLICIT

The project began from equal conventional `D*`, but Paper A's theorem now uses the cleaner event-specific normalization

```math
\rho_{\tau,\infty}=\rho_0.
```

These are not equivalent statements.

Equal event-specific eventual matched-filter SNR is a deliberate normalization that removes eventual sensitivity advantage for the chosen event. It does **not** prove equal `D*`, and equal scalar `D*` would not in general imply equal `rho0` for an arbitrary event.

The manuscript mostly handles this correctly. One phrase such as "stronger than equal D*" can still be read as a logical implication rather than a task-specific fairness condition.

### Required final wording

Prefer:

```text
This event-specific normalization is chosen to remove eventual matched-filter sensitivity as a confound; it is distinct from, and should not be identified with, equality of a scalar reference D*.
```

**Disposition:** PRESENTATION FIX, NOT THEOREM DEFECT.

---

## 5. Batch acquisition clock — PASS

The receiver now has an explicit operational record:

```text
arrival uncertainty window: [0,L]
finite post-arrival template duration: t
required record end: L+t.
```

The optimized quantity is

```math
T_G=\text{required post-window integration duration},
```

and

```math
T_{wall}=L+T_G.
```

For fixed physical `L`,

```math
T_{wall,f}-T_{wall,s}
=T_{G,f}-T_{G,s}.
```

Therefore the fast/slow ordering is unchanged by using the correct wall clock.

The manuscript no longer represents `T_G` as a generic sequential detection latency.

**Disposition:** BLOCKER RESOLVED.

---

## 6. True-alignment guarantee semantics — PASS

The manuscript now distinguishes

```math
P_{D,true}
=\Pr[Y_x(q_0)>\Gamma]
```

from

```math
P_D^{scan}
=\Pr[\sup_qY_x(q)>\Gamma].
```

Pathwise,

```math
\{Y_x(q_0)>\Gamma\}
\subseteq
\{\sup_qY_x(q)>\Gamma\},
```

so

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

The manuscript also states that `q_0` is an analysis variable under the signal-present hypothesis and is **not** receiver side information.

Thus satisfying

```math
P_{D,true}\ge\beta
```

is a valid sufficient guarantee of full-scan detection probability at least `beta`.

The paper now explicitly states that it does not prove ordering of the exact first solutions of

```math
P_D^{scan}(t)=\beta.
```

**Disposition:** STRONGEST ORIGINAL BLOCKER RESOLVED.

---

## 7. Covariance ordering / monotone guarantee margin — PASS

The weighted-average representation of `R_x(y)` shows that for each fixed lag

```math
x_2>x_1
\Longrightarrow
R_{x_2}(y)\ge R_{x_1}(y).
```

All processes have unit variance. Slepian therefore gives

```math
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
```

Since the SNR term increases strictly with `x`, the guarantee margin increases strictly.

The full-template limit satisfies

```math
R_x(y)\le R_\infty(y)=(1+|y|)e^{-|y|},
```

so

```math
\Gamma(x,\ell,\alpha)
\ge\Gamma_\infty(\ell,\alpha).
```

The Slepian directions remain correct after revision.

**Disposition:** PASS.

---

## 8. Full-template convergence — ACCEPTABLE WITH STATED REGULARITY

The manuscript now defines `Gamma_infty` directly from the stationary Gaussian process with covariance `R_infty`.

The normalized templates satisfy

```math
\|\hat h_x-\hat h_\infty\|_2\to0,
```

and

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2\to0.
```

The paper then invokes ordinary compact-interval Gaussian-supremum/quantile continuity regularity to pass to the threshold limit.

A measure-theory specialist could demand a longer tightness/quantile-continuity lemma, but the current paper explicitly states the regularity assumption rather than hiding it.

**Disposition:** ACCEPTABLE FOR THE PRESENT THEOREM; no reason to reopen Steps 13–49.

---

## 9. Large-search threshold divergence — PASS

For

```math
R_\infty(y)=(1+y)e^{-y}\to0,
```

select sufficiently separated points so every distinct covariance is at most `epsilon<1`. Compare the sampled vector with the equicorrelated vector

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i.
```

The comparison vector has larger pairwise covariance, so Slepian gives a stochastically smaller maximum. Since

```math
\max_iY_i\to\infty
```

in probability as the number of points grows, so does the actual sampled maximum, hence the continuous supremum.

Therefore

```math
\boxed{\Gamma_\infty(\ell,\alpha)\to\infty.}
```

This is now a derived property, not an assumed one.

**Disposition:** PASS.

---

## 10. Feasibility partition and boundary divergence — PASS

Let

```math
c=\rho_0-\Phi^{-1}(\beta).
```

For the slow and fast channels, the normalized searches are `ell` and `r ell` respectively. Since `Gamma_infty` is nondecreasing in search length, only

```text
both feasible
slow only
neither
```

are possible. Fast-only feasibility is excluded within this equal-eventual-SNR scaled family.

At the continuous critical boundary,

```math
\Gamma_\infty(\ell_{crit},\alpha)=c.
```

For every finite `x`,

```math
\eta(x)<1,
\qquad
\Gamma(x,\ell_{crit},\alpha)\ge\Gamma_\infty(\ell_{crit},\alpha),
```

so no finite `x` reaches the boundary target. Continuity then gives

```math
\boxed{X_G(\ell)\to\infty}
```

as the boundary is approached from below.

**Disposition:** PASS.

---

## 11. Crossover proposition — PASS, WITH ITS STATED SCOPE

At `L=0`, both channels have the same dimensionless first crossing `x0`, hence

```math
T_{G,f}(0)=\tau_fx_0
<\tau_sx_0=T_{G,s}(0).
```

The fast physical feasibility boundary is

```math
L_{crit,f}=\tau_f\ell_{crit}
```

and occurs before

```math
L_{crit,s}=\tau_s\ell_{crit}.
```

As `L` approaches the fast boundary, `T_G,f` diverges while the slow channel remains strictly feasible. The intermediate-value argument therefore gives at least one finite crossover.

The paper does not claim uniqueness.

**Disposition:** PASS under the explicitly stated continuity regularity.

---

## 12. NEW continuum quantitative witness — STRONG PASS

The current controlling witness is now stronger than the earlier Monte Carlo example.

Use

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=6.
```

At known arrival,

```math
x_0=1.80519795247291,
```

so fast is exactly preferred.

At

```math
L=9\tau_f=1.5\tau_s,
```

the normalized search lengths are

```math
\ell_f=9,
\qquad
\ell_s=1.5.
```

The threshold budget is

```math
c=2.21844843445540.
```

### Slow side

Since `R_infty''(0)=-1`, exact Rice theory gives mean upcrossing rate

```math
\nu_c^+=\frac1{2\pi}e^{-c^2/2}.
```

The event `sup Z>c` implies either a left-endpoint exceedance or at least one upcrossing, hence

```math
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<0.05.
```

This is a rigorous continuous-time upper bound, not a rare-event approximation to `P_FA`.

### Fast side

Take seven points over `[0,9]` at spacing `1.5`. Every distinct pair has covariance at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Slepian comparison with the equicorrelated seven-vector gives

```math
P_{FA,f}
\ge0.0624701020698
>0.05.
```

The comparison probability is obtained from a stable one-dimensional Gaussian integral.

Therefore

```math
\boxed{
P_{FA,s}\le0.0336428
<0.05
<0.0624701\le P_{FA,f}.
}
```

This establishes a genuine continuous-time slow-only guarantee-feasibility point at finite physical scale.

No hard-window grid maximum, Pickands transfer, or Step-44-style knife edge is involved.

**Disposition:** QUANTITATIVE-EXAMPLE OBJECTION RESOLVED.

---

## 13. Acquisition prior art — CLAIMS NOW APPROPRIATELY NARROW

The deeper audit shows that the following are established:

- unknown-delay/code-phase acquisition;
- acquisition time versus uncertainty region;
- Pd/Pfa/dwell/SNR/search-strategy tradeoffs;
- matched-filter acquisition;
- optical-CDMA acquisition and synchronization;
- direct-detection ladar acquisition in a range window;
- pulse-width/range-resolution and range-estimation tradeoffs.

The manuscript should not claim any of these as new.

No reviewed source directly reproduced the complete present construction:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous evidence-clock and timing-search-correlation rescaling
+ fixed physical arrival uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

However, absence of a direct hit is not a novelty proof.

**Disposition:** POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.

No `first`, `novel`, or priority language should appear.

---

## 14. Reference QA

The principal references used for claim boundaries are appropriate:

- Jones 1960 for pulse/energy detectivity;
- Garcia & Dereniak and Yang et al. for sensitivity/bandwidth context;
- Pecunia et al. for detector-characterization context;
- Vio/Andreani, Morras et al., and Croce et al. for correlated matched-filter false alarms;
- Milstein et al. for direct-detection range-window acquisition;
- Slepian for Gaussian comparison;
- Polydoros/Weber and Su for classical matched-filter acquisition;
- Mustapha/Ormondroyd, Keshavarzian/Salehi, and Pham/Yashima for optical code acquisition.

Primary publisher records checked in the current audit support the acquisition/optical-acquisition framing.

One optional improvement is to replace or supplement the arXiv-only Vio/Andreani citation with a peer-reviewed matched-filter false-alarm source if desired, but the manuscript already has Morras and Croce for peer-reviewed support.

**Disposition:** NO BLOCKING CITATION ERROR FOUND.

---

## 15. What must be changed in the authoritative manuscript before final formatting

Three final synchronization edits are required:

1. Replace the older `r=1.2` Monte Carlo regime witness in `PAPER_A_DRAFT.md` with the new continuum `r=6` Rice/Slepian feasibility bracket.
2. Add the physical-realization sentence noting that the exact pole-zero matching is a controlled existence construction and that `b>=1/tau_f` makes both compared impulse responses nonnegative.
3. Replace any wording that could imply equal eventual event SNR is logically "stronger than" equal `D*`; state instead that it is a distinct event-specific normalization chosen to remove eventual matched-filter sensitivity as a confound.

These are manuscript synchronization/positioning edits, not new research branches.

---

## 16. Final scientific disposition

Subject to the three synchronization edits above:

```text
INTERNAL MATHEMATICAL CONSISTENCY: PASS
OPERATIONAL TASK DEFINITION: PASS
CLAIM SCOPE: PASS
QUANTITATIVE REGIME EVIDENCE: PASS
HARD-STOP DISCIPLINE: PASS
PRIOR-ART HONESTY: PASS
NOVELTY: NOT ESTABLISHED
CROSSOVER UNIQUENESS: NOT ESTABLISHED / NOT CLAIMED
EXACT FULL-SCAN DETECTION-TIME REVERSAL: NOT ESTABLISHED / NOT CLAIMED
```

I would no longer recommend another mathematical closure branch before manuscript preparation.

The next step is to synchronize `PAPER_A_DRAFT.md` to this audit, re-read the resulting final text once, and only then move to figures/journal formatting or an external referee-style review.
