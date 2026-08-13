# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 23:22 EDT:** mathematical closure remains hard-stopped after Step 49. Paper A's operational/claim-scope blockers are repaired, its central theorem survives final adversarial checking, the main quantitative witness is now continuum-bracketed without timing-grid extrapolation, and acquisition/optical-acquisition prior art has been explicitly incorporated. **Novelty remains unestablished.**

---

## Steps 01–12 — detector/detection-theory core

The initial equal-`D*`, different-speed thought experiment established the following sequence.

1. Equal scalar reference `D*` does not determine arbitrary temporal-signal performance.
2. For a known deterministic waveform, full observation, LTI response, and stationary Gaussian noise,

```math
\mathrm{SNR}_{max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

A complete frequency-dependent magnitude sensitivity can therefore be sufficient for this restricted problem.
3. Unknown arrival time alone does not break equivalence when the complete matched-filter magnitude weighting is identical; detector phase cancels from the full-observation timing-scan covariance.
4. Finite observation windows make phase/time placement relevant; pure-delay and all-pass-dispersion counterexamples survive latency compensation.
5. Exact finite-record matched-filter SNR is

```math
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
```

6. Known-time Gaussian detection gives

```math
P_D=\Phi[\rho_T-\Phi^{-1}(1-\alpha)].
```

7. Unknown timing introduces a global threshold over a correlated timing scan; raw sample count is not a universal effective trial count.
8. A controlled detector family was constructed from one common optical event:

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

9. Choosing

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
```

holds the event-specific eventual matched-filter SNR fixed:

```math
\rho_{\tau,\infty}=\rho_0.
```

10. Finite evidence accumulation is

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
```

11. The same time scale `tau` controls both evidence accumulation and the physical correlation length of the unknown-arrival timing scan.
12. For `tau_f<tau_s`, the faster channel wins at known arrival but reaches the global-search feasibility boundary at a smaller physical arrival-time uncertainty. This led to the task-dependent fast/slow crossover theorem and the both / slow-only / neither feasibility partition.

Historical notation used `T_D`. The final manuscript replaces it by operational guarantee time `T_G`; see the major-revision entries below.

---

## Steps 13–49 — mathematical stress-test branch

The later branch tested whether continuous timing-search statistics invalidated the detector-facing construction.

### Critical failures and corrections preserved

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` is invalid. A finite hard-window template produces a locally Brownian-like covariance cusp, so grid maxima converge slowly.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless common low-pass does not, because optimal whitening cancels it.
- Rice's apparent high-band upper switch near `kappa_f~130` was **INVALIDATED** by Palm correction. Only the lower switch survived that calibration.
- **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected to `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` values were grid biased.
- Raw crossing counts fail because one physical excursion generates many micro-upcrossings; finite-amplitude excursion clusters replaced them.
- Step 39 found a finite-`u` remainder ratio of order unity, rejecting a hoped-for small remainder.
- Step 40 introduced Cameron-Martin exact-event threshold translation.
- Step 41 replaced empirical `q` interpolation by analytic Gaussian-process control and corrected the earlier tiny-`q` RMS value.
- Step 44 produced a genuine **finite-grid** pointwise 95% bound, but its margin was much smaller than the unresolved continuum grid correction. It is not continuum truth.
- Step 45 showed that witness retuning trades one near-boundary problem for another rather than solving the underlying issue.
- Step 46 identified missed between-sample maxima as the dominant grid error. The five-event check supports sign/scale only, not a precise coefficient.
- Step 47 obtained the exact pure-`alpha=1` discrete Pickands correction.
- Step 48 showed the mixed finite-`u` tangent correction differs from the pure rough benchmark only at `O(1e-5)` while grid loss is `O(1e-3)`.
- Step 49 simulated the exact finite-window covariance and found the same grid-loss scale; higher-order covariance did not provide an `O(1e-4)` escape.

**HARD STOP:** do not create Step 50 by default. The remaining publication-grade finite-`u` transfer problem is not required for the final Paper-A theorem or continuum feasibility witness.

---

## 20:31 EDT — first detector-facing prior-art audit

`PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md` established that several broad ingredients are old:

```text
pulse/energy detectivity from D*(f);
sensitivity-bandwidth combinations;
unknown-arrival matched-filter search penalties;
all-pass magnitude/phase separation.
```

Disposition became

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## 20:42–21:47 EDT — Paper A architecture and first complete draft

- `PAPER_ARCHITECTURE_TASK_REVERSAL.md` fixed a detector-facing five-section architecture and moved Steps 13–49 out of the main narrative.
- `PAPER_A_DRAFT_OPENING.md` drafted the opening and detector family.
- `PAPER_A_DRAFT.md` added the correlated-scan threshold, finite-time surface, feasibility partition, and crossover proof.
- `PAPER_A_SECTION_V.md` drafted interpretation and limitations.
- At 21:47, `PAPER_A_DRAFT.md` became the controlling merged manuscript.

---

## 22:09 EDT — severe adversarial reviewer audit

`PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md` found **no fatal algebraic contradiction**, but identified two submission blockers.

### Blocker A — acquisition clock

The stationary scan requires a record of length `L+t`; the old `T_D=t` was not an ordinary online wall-clock latency.

### Blocker B — scan power

The old

```math
P_{D,true}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma]
```

is true-alignment threshold crossing, not

```math
P_D^{scan}=\Pr[\sup_qY(q)>\Gamma].
```

The exact relationship is only

```math
P_D^{scan}\ge P_{D,true}.
```

The audit recommended claim narrowing rather than reopening the full signal-present Gaussian-extremes problem.

Additional major requests:

- restore the common optical event / transfer function;
- tighten white-noise normalization and `D*` bandwidth language;
- derive rather than merely assume large-search/boundary divergence where possible;
- add a robust quantitative example;
- deepen the acquisition prior-art audit.

Disposition at that point:

```text
MAJOR REVISION BEFORE SUBMISSION.
```

---

## 22:54 EDT — operational guarantee-time major revision

`PAPER_A_MAJOR_REVISION_2026-08-12.md` documents the repair.

The batch protocol now defines

```math
\boxed{
T_G=\text{minimum required post-window integration duration},
}
```

with

```math
\boxed{T_{wall}=L+T_G.}
```

At fixed `L`, these clocks induce identical detector ordering.

The manuscript explicitly states

```math
\boxed{P_D^{scan}\ge P_{D,true}}
```

and treats `T_G` as a **sufficient guarantee time**. No exact full-scan detection-time reversal is claimed.

The same optical event and detector transfer functions were restored, and the noise convention was fixed to

```math
E[n(t)n(t')]=N\delta(t-t').
```

Two old theorem assumptions were strengthened:

1. from `R_infty(y)->0`, separated samples plus Slepian comparison prove

```math
\Gamma_\infty(\ell,\alpha)\to\infty;
```

2. from `eta(x)<1`, `R_x<=R_infty`, threshold ordering, and boundary continuity,

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit}).
```

No Step 50 was created.

---

## 23:06 EDT — smooth finite-information robustness companion

`PAPER_A_FINITE_INFORMATION_COMPANION.md` consolidated the already-validated Step-14–16 smooth finite-information result rather than creating new closure work.

For the documented rare-event calibration near

```text
rho0 ~ 6.2
r = 1.2
alpha = 1e-6
beta = .90
kappa = 8,
```

Rice predicted a crossover near `ell_s=0.571441752`; Palm-corrected rare-event validation gave about `0.5721 +/- .001`, a `~0.12%` relative shift.

This remains **companion robustness evidence**, not the controlling hard-window Paper-A result.

---

## 23:14 EDT — post-revision audit

`PAPER_A_POST_REVISION_AUDIT_2026-08-12.md` and its addendum rechecked the repaired theorem.

Two remaining presentation issues were fixed:

- `q_0` is explicitly analysis-only, never receiver side information;
- `Gamma_infty` is defined directly from the full-template Gaussian process.

The finite-template/full-template link was tightened through

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
```

No new fatal defect was found.

---

## 23:22 EDT — first robust full-template numerical witness

A paired Monte Carlo full-template witness was built at moderate `alpha` to avoid rare-event conditioning and the hard-window covariance cusp.

The production run used `240000` paired paths, `x_tail=16`, and nested grids. It gave a stable slow-only feasibility classification for a modest `r=1.2` example.

This was a successful numerical result, but the final hostile review correctly noted that the slow-side continuum classification still depended on numerical supremum approximation. The result is retained as an independent cross-check in

`numerics/paper_a_full_template_feasibility.py`,

but it is no longer the controlling manuscript witness.

---

## 23:22 EDT — deeper acquisition / optical-acquisition prior-art audit

`PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md` moved the novelty boundary materially.

Classical spread-spectrum/PN acquisition already contains:

```text
unknown delay/code phase;
search-region size;
a-priori epoch information;
Pd / Pfa;
predetection SNR;
dwell/integration time;
matched-filter/correlator receivers;
serial/parallel/sequential acquisition.
```

Optical-CDMA synchronization/acquisition and direct-detection ladar establish the same broad acquisition concepts in optical systems. Ladar literature also contains pulse-width / range-resolution and range-estimation tradeoffs.

Therefore Paper A must **not** claim novelty for those ingredients.

The only remaining plausible synthesis contribution is the narrower coupled detector construction:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous evidence-clock and timing-search-correlation rescaling
+ fixed physical arrival uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No direct source reproducing the complete construction was found, but absence of a hit is not proof of novelty.

Disposition remains:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## Final hostile review — continuum feasibility witness found

The last hostile pass found a stronger way to answer the quantitative objection without any timing-grid continuum extrapolation.

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

Choose

```math
\boxed{L=9\tau_f=1.5\tau_s.}
```

The full-template threshold budget is

```math
c=2.21844843445540.
```

### Slow side — exact continuous-process upper bound

Since

```math
R_\infty''(0)=-1,
```

Rice's exact expected upcrossing rate gives

```math
\nu_c^+=\frac1{2\pi}e^{-c^2/2}.
```

A path exceeding `c` must start above `c` or contain an upcrossing, hence

```math
\boxed{
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<.05.
}
```

### Fast side — Slepian lower bound

Select seven points across `[0,9]` at spacing `1.5`. Every off-diagonal covariance is at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Compare with the equicorrelated vector

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i.
```

Slepian gives the sampled fast maximum at least as large in tail probability as this comparison maximum. A one-dimensional Gaussian integral yields

```math
\boxed{
P_{FA,f}
\ge0.0624701020698
>.05.
}
```

Therefore

```math
\boxed{
P_{FA,s}\le.0336428<.05<.0624701\le P_{FA,f},
}
```

which is a **continuum slow-only guarantee-feasibility witness** at finite physical `L`.

This result is documented in

- `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
- `numerics/paper_a_analytic_feasibility_bracket.py`

and replaces the Monte Carlo witness as the controlling Paper-A example.

No Step 50 or hard-window grid analysis was required.

---

## Final integrated adversarial QA

`PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md` found no new fatal mathematical defect.

Final manuscript-only fixes applied:

1. the authoritative `PAPER_A_DRAFT.md` now uses the continuum `r=6` Rice/Slepian witness;
2. the constructed pole-zero matching is explicitly identified as an existence construction;
3. the detector impulse response is shown to be

```math
g_\tau(t)
=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac1\tau\right)t\right]u(t),
```

and choosing `b>=1/tau_f` makes both compared channel responses nonnegative;
4. equal eventual event SNR is explicitly distinguished from equal scalar `D*`;
5. S. O. Rice's original random-noise paper was added as the primary upcrossing reference;
6. regression search found no obsolete `T_D`, no old `r=1.2` controlling witness, and no accidental exact-scan/online claim.

Final internal scientific disposition:

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

---

## Current stopping point

No further Gaussian-extremes or crossover-localization theory is justified by the current manuscript.

The appropriate next phase is **external-style manuscript preparation/review**, e.g. final figure design, journal-format manuscript rendering, or a fresh independent referee report on the now-consolidated Paper A.

The repository should remain explicit that novelty is unresolved and that the result is a task-specific guarantee-time theorem for a constructed equal-eventual-SNR detector family.
