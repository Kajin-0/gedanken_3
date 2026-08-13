# Progress Log — Experiment 01

**Consolidation note — 2026-08-13 01:14 EDT:** the detector/detection-theory core is complete; the mathematical stress-test branch remains hard-stopped after Step 49; Paper A's acquisition-clock and scan-power semantics are repaired; the controlling quantitative witness is a continuous-time Rice/Slepian feasibility bracket; novelty remains unestablished. The active work has moved to a separate **external-paper / Applied Optics submission phase** on branch `agent/paper-a-submission-package`.

Detailed step files remain the authoritative source for individual derivations. This log preserves the path, failed branches, corrections, and current direction.

---

# Steps 01–12 — detector/detection-theory core

The initial equal-`D*`, different-speed thought experiment established the following chain.

1. Equal scalar reference `D*` does not determine arbitrary temporal-signal performance.
2. For a known deterministic waveform, full observation, LTI response, and stationary Gaussian noise,

```math
\mathrm{SNR}_{max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

A complete frequency-dependent magnitude sensitivity can therefore be sufficient for this restricted problem.
3. Unknown arrival time alone does not break that full-observation magnitude equivalence when the complete matched-filter weighting is identical; detector phase cancels from the time-shift covariance.
4. Finite observation windows make phase/time placement relevant. Pure-delay and all-pass-dispersion counterexamples survive the appropriate controls.
5. Exact finite-record matched-filter SNR is

```math
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
```

6. Known-time Gaussian detection gives

```math
P_D=\Phi[\rho_T-\Phi^{-1}(1-\alpha)].
```

7. Unknown timing introduces one global threshold over a correlated timing scan; raw ADC sample count is not a universal trial count.
8. A controlled causal detector family was constructed from one common optical event:

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

holds the **event-specific eventual matched-filter SNR** fixed:

```math
\rho_{\tau,\infty}=\rho_0.
```

10. Finite evidence accumulation is

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
\qquad
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
```

11. The same detector time scale controls both the evidence clock and the physical correlation length of the unknown-arrival timing scan.
12. Fast wins at known arrival, but fast reaches the normalized-search feasibility boundary at a smaller physical timing uncertainty. This produced the both / slow-only / neither feasibility partition and the fast-to-slow task-ordering theorem.

Historical notation used `T_D`; the final theorem uses operational sufficient guarantee time `T_G`.

---

# Steps 13–49 — mathematical stress-test branch

This branch tested whether the detector-facing construction survived continuous-time Gaussian-extreme-value scrutiny.

## Critical failed routes and corrections

- **FAILED numerical estimate:** Step-13 `ell~49` hard-window grid crossover. The truncated matched-filter template produces a local covariance cusp and Brownian-like scan roughness, so coarse maxima miss between-grid extrema.
- Genuine finite accessible information bandwidth regularizes the cusp. An invertible noiseless common low-pass does **not** impose such a restriction because optimal whitening cancels it.
- Finite-band Rice/Monte Carlo work validated a smooth-information companion regime, but Rice's apparent high-band upper switch near `kappa_f~130` was **invalidated by Palm correction**. Only the lower switch survived that calibration.
- **Invalid intermediate coupling coefficient:** `.8131`; corrected to `.8906480701 sqrt(chi/zeta)`.
- **Invalid numerical interpretation:** raw Step-27 tiny-`chi` values were grid biased.
- Raw upcrossing counts failed because one physical excursion generates many micro-upcrossings. Finite-amplitude excursion clusters replaced those counts.
- Step 39 found a finite-`u` remainder ratio of order unity, rejecting the hoped-for “small correction” shortcut.
- Step 40 introduced Cameron-Martin exact-event threshold translation.
- Step 41 replaced empirical interpolation by analytic Gaussian-process control and corrected the earlier tiny-`q` RMS estimate.
- Step 44 produced a genuine **finite-grid** 95% pointwise certificate, but the margin was smaller than the unresolved continuum grid correction. It is not continuum truth.
- Step 45 showed that retuning the witness trades one near-boundary problem for another.
- Step 46 identified missed between-sample maxima as the dominant grid error. The five-event run supports sign/scale only, not a precise coefficient.
- Step 47 obtained the exact pure rough (`alpha=1`) discrete Pickands correction.
- Step 48 showed the mixed finite-`u` tangent correction differs from the pure rough benchmark only at `O(1e-5)` while the grid loss is `O(1e-3)`.
- Step 49 simulated the exact finite-window covariance and found the same grid-loss scale; higher-order covariance did not supply the required cancellation.

## Hard stop

**HARD STOP TRIGGERED AT STEP 49. DO NOT CREATE STEP 50 BY DEFAULT.**

The unresolved publication-grade finite-`u` transfer problem is not required for the final Paper-A theorem or its continuum feasibility witness.

---

# Detector-facing prior-art and first manuscript phase — 2026-08-12

## First prior-art audit

`PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md` established that these broad claims are old:

```text
pulse/energy detectivity from frequency-dependent sensitivity;
sensitivity-bandwidth combinations;
unknown-arrival matched-filter search penalties;
standard magnitude/phase separation.
```

Disposition became:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

## First complete Paper A draft

The initial detector-facing paper was assembled from:

- `PAPER_ARCHITECTURE_TASK_REVERSAL.md`
- `PAPER_A_DRAFT_OPENING.md`
- `PAPER_A_DRAFT.md`
- `PAPER_A_SECTION_V.md`

The intent was to move Steps 13–49 out of the main narrative and retain the detector/task theorem.

---

# Severe adversarial audit — 22:09 EDT

`PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md` found no fatal algebraic contradiction but identified two genuine submission blockers.

## Blocker A — acquisition clock

The scan over arrival window `[0,L]` using a duration-`t` template requires data through `L+t`. The old `T_D=t` was therefore not an ordinary online latency.

## Blocker B — full scan power versus true alignment

The quantity

```math
P_{D,true}=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma]
```

is not

```math
P_D^{scan}=\Pr[\sup_qY(q)>\Gamma].
```

Only the exact pathwise inequality

```math
P_D^{scan}\ge P_{D,true}
```

is guaranteed.

The correct repair was claim narrowing, not reopening the full signal-present Gaussian-extremes problem.

Additional requests were to restore the common optical event, fix the white-noise convention, distinguish `D*` measurement-bandwidth normalization from detector speed, strengthen theorem assumptions, obtain a robust quantitative example, and deepen acquisition prior art.

Disposition at that point:

```text
MAJOR REVISION BEFORE SUBMISSION.
```

---

# Operational guarantee-time revision — 22:54 EDT

`PAPER_A_MAJOR_REVISION_2026-08-12.md` records the repair.

The paper now defines

```math
\boxed{T_G=\text{minimum required post-window integration duration}}
```

and

```math
\boxed{T_{wall}=L+T_G.}
```

At fixed `L`, these induce identical channel ordering.

The theorem now concerns a **sufficient guarantee time** through

```math
\boxed{P_D^{scan}\ge P_{D,true}.}
```

The common optical event and causal channel family were restored. The noise convention is

```math
E[n(t)n(t')]=N\delta(t-t').
```

Two old theorem assumptions were strengthened into derived consequences:

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\quad(\ell\to\infty)
```

from separated-sample Slepian comparison, and

```math
X_G(\ell)\to\infty
\quad(\ell\uparrow\ell_{crit})
```

from `eta(x)<1`, covariance ordering, threshold ordering, and boundary continuity.

No Step 50 was created.

---

# Smooth finite-information companion — 23:06 EDT

`PAPER_A_FINITE_INFORMATION_COMPANION.md` preserved the already-validated smooth finite-information result rather than treating it as the hard-window theorem.

At the documented rare-event calibration near

```text
rho0 ~ 6.2
r = 1.2
alpha = 1e-6
beta = .90
kappa = 8,
```

Rice predicted `ell_s~0.571441752`; Palm correction gave about `0.5721 +/- .001`, a `~0.12%` relative change.

This remains companion robustness evidence only.

---

# Post-revision audit and full-template convergence — 23:14 EDT

`PAPER_A_POST_REVISION_AUDIT_2026-08-12.md` and its addendum fixed two remaining presentation gaps:

- `q_0` is analysis-only and is never receiver side information;
- `Gamma_infty` is defined directly from the full-template Gaussian process.

The finite-to-full-template connection was tightened through

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
```

No new fatal defect was found.

---

# Quantitative-witness evolution — 23:22 EDT onward

## Successful but superseded Monte Carlo witness

A paired full-template Monte Carlo calculation at moderate `alpha` used `240000` paired paths, `x_tail=16`, and nested grids. It gave stable slow-only feasibility for a modest `r=1.2` pair.

This result remains a useful independent cross-check in

`numerics/paper_a_full_template_feasibility.py`,

but it was superseded because the main paper could be made stronger without numerical supremum extrapolation.

## Deeper acquisition prior art

`PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md` established that classical spread-spectrum/PN acquisition already contains

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

Optical-CDMA synchronization/acquisition and direct-detection ladar establish the same broad acquisition concepts in optical systems. Pulse-width/range-resolution and range-estimation tradeoffs are also prior art.

Therefore none of those ingredients are claimed as new.

The only remaining possible synthesis contribution is the coupled detector construction:

```text
same optical event
+ causal detector family
+ equal event-specific eventual matched-filter SNR
+ detector time-scale variation
+ simultaneous evidence-clock and timing-search-correlation rescaling
+ fixed physical arrival uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

No direct source reproducing that complete construction was found, but absence of a hit is not proof of novelty.

---

# Controlling continuum feasibility witness

The final hostile pass found a stronger finite-scale example with no timing-grid extrapolation.

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

For the slow channel, since `R_infty''(0)=-1`, Rice's exact expected upcrossing rate gives

```math
\boxed{
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841
<.05.
}
```

For the fast channel, seven points across `[0,9]` at spacing `1.5` have off-diagonal covariance at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Slepian comparison with a seven-dimensional equicorrelated Gaussian vector gives

```math
\boxed{
P_{FA,f}\ge0.0624701020698>.05.
}
```

Therefore

```math
\boxed{
P_{FA,s}\le.0336428<.05<.0624701\le P_{FA,f},
}
```

which is a **continuous-time slow-only guarantee-feasibility witness**.

This result is recorded in

- `PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
- `numerics/paper_a_analytic_feasibility_bracket.py`

and replaces the Monte Carlo point as the controlling manuscript witness.

---

# Final integrated QA — 2026-08-12

`PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md` records the final theorem-level disposition:

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

The authoritative theorem manuscript uses `T_G`, the continuum `r=6` witness, explicit existence-construction language, and no priority claim.

---

# External-paper phase — 2026-08-13

The mathematical program was intentionally **not** extended. Work moved to branch

`agent/paper-a-submission-package`.

## Journal selection

Current first target: **Applied Optics**.

Reason: the result is most naturally an applications-centered optical detection / detector-qualification paper. Current Optica guidance favors a conventional Introduction / Method / Results / Discussion / Conclusion structure, an approximately 100-word abstract, ordered figure callouts, and explicit Disclosures / Data Availability sections.

Fallback: **Journal of Applied Physics** if a more device/theory-oriented framing becomes preferable.

`Physical Review Applied` remains aspirational because its editorial significance threshold is harder to justify while novelty remains unresolved.

Journal strategy is not a scientific claim.

## Submission-strategy document

Created:

`PAPER_A_SUBMISSION_STRATEGY_2026-08-13.md`

This fixed the journal-facing architecture and prohibited a fabricated numerical `T_G(L)` crossover curve.

## Applied Optics draft

Created and iterated:

`PAPER_A_APPLIED_OPTICS_DRAFT.md`

Current journal-facing title:

> **Task-dependent photodetector ordering under unknown arrival time**

Rev. 3 structure:

```text
Introduction
Model and decision protocol
Results
    response time enters the task twice
    continuous-time feasibility witness
    general feasibility/crossover theorem
Discussion
Conclusion
```

The journal-facing draft remains separate from the theorem manuscript so publication-oriented compression cannot silently alter the audited scientific checkpoint.

## First external-style referee review

`PAPER_A_APPLIED_OPTICS_REFEREE_REVIEW_2026-08-13.md`

Disposition:

```text
MAJOR REVISION FOR PRESENTATION AND SIGNIFICANCE;
NO FATAL TECHNICAL DEFECT IDENTIFIED.
```

The reviewer-style pass asked for:

- three figures;
- one dimensional scale illustration;
- continuum witness before general theorem;
- prominent existence-construction language;
- clearer detector relevance.

All were addressed in Rev. 2.

## Figures

Generated and visually QA'd:

1. `paper_a_fig1_evidence` — accumulated SNR fraction versus physical integration time;
2. `paper_a_fig2_covariance` — fast/slow physical timing covariance over one common `L`;
3. `paper_a_fig3_feasibility` — one-sided slow upper bound and fast lower bound around `alpha=.05`.

Reproduction script:

`numerics/paper_a_submission_figures.py`

Figure 3 deliberately uses arrows showing the direction of the unknown exact probability. No bar or point is presented as an exact PFA.

## Second significance/readability review

`PAPER_A_APPLIED_OPTICS_REFEREE_REVIEW_REV2_2026-08-13.md`

Disposition:

```text
MINOR-TO-MODERATE REVISION BEFORE EXTERNAL SUBMISSION.
```

Remaining requested framing edits were:

1. make the abstract opening match exactly what the controlled model proves;
2. state the experimental meaning of `L`;
3. explain that `alpha=.05` and `r=6` are witness-design values, not recommended operating values;
4. interpret `G_tau` explicitly as a small-signal optical-to-electrical existence construction.

These edits were applied in Rev. 3.

The draft now states that `L` can represent trigger/synchronization uncertainty, an asynchronous transient window, a time-of-flight/range gate, or another pre-specified timing window.

The dimensional mapping

```text
tau_f = 10 microseconds
tau_s = 60 microseconds
L = 90 microseconds
```

is labeled **illustrative only** and is not tied to HgCdTe, InSb, APDs, or another detector technology.

The draft also explicitly states that `alpha=.05` and `r=6` were chosen to make the continuum analytic bounds separate transparently, not because they are representative detector specifications.

---

# Current stopping point

The internal theory should remain frozen unless a genuinely new technical defect appears.

The journal-facing Rev. 3 has now addressed the two external-style review rounds and has a reproducible three-figure package.

The next useful work is:

1. one final regression/readability check of Rev. 3;
2. create an Optica-compatible LaTeX/Word submission package only after that check;
3. perform journal-specific reference formatting and final citation verification;
4. obtain a truly independent review of the rendered manuscript.

**Do not reopen Step 50 or invent a numerical crossover curve.**
