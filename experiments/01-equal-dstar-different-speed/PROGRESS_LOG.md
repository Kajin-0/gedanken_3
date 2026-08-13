# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 23:22 EDT:** mathematical closure remains hard-stopped after Step 49; Paper A semantic blockers repaired; robust full-template quantitative regime witness established; deeper acquisition / optical-acquisition prior-art audit completed; final integrated hostile-review QA is now the active task. **Novelty not established.**

---

## Steps 01–12 — detector/detection-theory core

Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite windows make phase/time placement relevant. Unknown arrival introduces global false-alarm timing-search complexity. In the defined scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because temporal compression changes both evidence accumulation and timing-search correlation length. This is protocol/task specific, not a universal detector theorem.

Historical detector-facing scaling before the major-revision semantic repair:

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For `r=tau_s/tau_f>1` and `ell=L/tau_s`:

```math
B_r(\ell)=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions: fast wins at known time; approaching the fast feasibility boundary, fast detection time diverges while slow remains feasible; at least one finite fast-to-slow crossover therefore exists. Slow-only feasibility is possible, fast-only feasibility is excluded in this deliberately equal-eventual-SNR scaled family, and uniqueness is not established.

This historical notation is retained here for provenance. The active Paper A manuscript now replaces unqualified `T_D` by operational guarantee time `T_G`; see the 22:54 revision entry below.

---

## Steps 13–49 — mathematical stress-test branch

The later branch tested whether continuous timing-search statistics invalidated the detector-facing construction.

Consequential corrections and surviving results:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` invalid; hard-window timing scans are locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Rice's apparent upper switch near `kappa_f~130` was **INVALIDATED**; Palm preserved only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.
- Crossing counts fail from micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 found `R=N_a/N_tan~1.56`, rejecting a small-amplitude finite-u remainder.
- Step 40 introduced Cameron-Martin exact-event threshold translation.
- Step 41 replaced empirical q interpolation with analytic Gaussian-process control and corrected Step-35 tiny-q pair RMS from `~5.4e-5` to `~2.69e-5` asymptotically.
- Step 44 gave a genuine pointwise finite-grid 95% bound `P_FA/alpha<.999957771`, but only `.00004223 alpha` margin; continuum grid bias dominated.
- Step 45 showed witness retuning trades one near-boundary problem for another.
- Step 46 isolated missed between-sample maxima as the dominant grid error. **WORDING CORRECTION:** the five-event result supports sign/scale consistency only, not precise coefficient verification.
- Step 47 obtained the exact pure-alpha1 discrete Pickands correction.
- Step 48 found mixed finite-u transfer only `O(1e-5)` relative to an `O(9e-4)` discretization loss.
- Step 49 simulated the exact finite-window covariance directly and found the same grid-loss scale; higher-order covariance did not cancel it at order `1e-4`.

**HARD-STOP TRIGGERED at Step 49:** do not create Step 50 by default.

---

## Detector-facing prior-art audit — 20:31 EDT

`PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md` found direct prior art for pulse/energy detectivity from frequency-dependent response, detectivity-bandwidth benchmarking, unknown-arrival matched-filter search penalties, and standard all-pass magnitude/phase separation.

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## Paper A drafting and consolidation

### 20:42 EDT — architecture

`PAPER_ARCHITECTURE_TASK_REVERSAL.md` fixed a five-section detector-facing paper and moved Steps 13–49 out of the main narrative.

### 20:52 EDT — opening manuscript

`PAPER_A_DRAFT_OPENING.md` drafted title, abstract, Introduction, and Section II through exact finite-record timing covariance.

### 21:03 EDT — Sections III–IV

`PAPER_A_DRAFT.md` added the exact correlated-scan threshold, true-alignment margin, dimensionless task surface, feasibility partition, and Proposition 1 crossover proof.

### 21:35 EDT — Section V

`PAPER_A_SECTION_V.md` drafted detector-task interpretation, limitations, and experiment-design implications.

### 21:47 EDT — merge and consistency pass

`PAPER_A_DRAFT.md` became the single authoritative five-section manuscript. Section IV ends with the theorem/proof; Section V alone carries interpretation. Body terminology standardized on eventual matched-filter SNR. True-alignment criterion explicitly distinguished from full signal-present scan probability. No new theorem claims or Steps 13–49 machinery added.

---

## 22:09 EDT — severe adversarial reviewer audit

New file: `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`.

### Core mathematics that survived

Direct checking found no fatal internal contradiction in:

```text
A_tau normalization;
eta(x);
R_x(y);
covariance ordering and Slepian direction;
strict margin monotonicity;
T_D=tau X_D(...,L/tau);
feasibility partition;
conditional intermediate-value crossover proof.
```

### Blocking issue A — acquisition clock

The stationary full-template scan over an arrival window `L` implicitly requires a batch record of about `L+t`. Current `T_D=t` is therefore not automatically an online wall-clock detection latency. Define the batch protocol and either call `T_D` the required post-window integration duration or define `T_wall=L+T_D`.

### Blocking issue B — true-alignment criterion

```math
P_{D,true}=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma]
```

is not the exact full signal-present scan probability. It is a conservative guarantee because

```math
P_D^{scan}\ge P_{D,true}.
```

A reversal of guarantee times does not by itself prove a reversal of exact scan detection times. Default repair: explicitly reframe Paper A around a **true-alignment guaranteed detection criterion** rather than reopening the full Gaussian-extremes theorem.

### Major issue C — physical detector realization

Restore the fixed optical event and stable causal detector family:

```math
p(t)=e^{-bt}u(t),
```

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

which produces the manuscript template. State that equal eventual matched-filter SNR is event-specific and deliberately stronger than equal scalar `D*`.

### Major issue D — Proposition 1 assumptions

Strengthen rather than merely assume large-search growth and boundary divergence. The latter can largely be derived from `eta(x)<1`, `Gamma(x,ell)>=Gamma_infty(ell)`, boundary equality, and continuity. Add explicit Slepian and stationary-Gaussian extreme-value support.

### Major issue E — no robust quantitative example

The existence theorem may cross only near the feasibility singularity. After conceptual repairs, add one continuum-validated non-knife-edge example/phase diagram with comfortable margins. Do not reuse invalidated Step-13 or treat Step-44 as continuum truth.

### Presentation/citation repairs

- distinguish `D*` noise-bandwidth normalization from detector temporal bandwidth;
- define the white-noise PSD/covariance convention exactly;
- reconsider title wording "equal asymptotic sensitivity" because `rho_0` is event-specific;
- add Yang DOI `10.1038/s41467-026-72259-1`;
- add Slepian/extreme-value support;
- define `Phi` and standardize crossover notation.

### Additional novelty risk

Milstein et al., *Applied Optics* 47, 296–311 (2008), DOI `10.1364/AO.47.000296`, studies constant-false-alarm acquisition time in a specified range window for direct-detection ladar with Geiger-mode APDs. It is not a direct fast/slow reversal match, but it confirms substantial adjacent prior art at the photodetection/unknown-delay/acquisition-time intersection.

### Reviewer-style disposition

```text
MAJOR REVISION BEFORE SUBMISSION.
Do not format or submit yet.
```

---

## 22:54 EDT — Paper A operational guarantee-time major revision

New audit trail: `PAPER_A_MAJOR_REVISION_2026-08-12.md`.

Revised authoritative manuscript: `PAPER_A_DRAFT.md` on the active revision branch.

### Blocking issue A resolved — exact batch clock

For every candidate arrival in `[0,L]` to receive the same duration-`t` post-arrival template, the record must extend to `L+t`.

The paper now defines

```math
\boxed{
T_G=\text{minimum required post-window integration duration}.
}
```

The actual batch wall time is

```math
\boxed{
T_{wall}=L+T_G.
}
```

Since `L` is common to both channels, `T_wall` and `T_G` have identical pairwise ordering.

### Blocking issue B resolved by exact claim narrowing

The manuscript now explicitly defines complete signal-present scan power and proves only the one-sided implication

```math
\boxed{
P_D^{scan}\ge P_{D,true}.
}
```

Thus `P_D,true>=beta` is a sufficient guarantee, and the theorem concerns the time required to satisfy that guarantee.

**No claim remains that the exact first solutions of `P_D^scan=beta` reverse ordering.**

### Common optical event restored

All channels now receive

```math
p(t)=e^{-bt}u(t)
```

through

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

producing

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Equal eventual matched-filter SNR is explicitly event-specific.

### Noise and detector terminology tightened

The revision fixes

```math
E[n(t)n(t')]=N\delta(t-t'),
\qquad
\rho^2=(1/N)\int s^2dt,
```

and distinguishes `D*` noise-equivalent measurement-bandwidth normalization from detector temporal / `-3 dB` bandwidth.

### Proposition 1 strengthened

Two previous assumptions are now derived.

1. `Gamma_infty(ell,alpha)->infinity` follows directly from `R_infty(y)=(1+y)e^{-y}->0`: widely separated samples are compared by Slepian with an equicorrelated Gaussian vector whose maximum diverges.
2. `X_G->infinity` at `ell_crit` follows from `eta(x)<1`, `R_x<=R_infty`, `Gamma(x)>=Gamma_infty`, boundary equality, and continuity.

The proposition now assumes only known-time guarantee feasibility and ordinary threshold/first-crossing continuity.

### Hard stop explicitly preserved

No Step 50 was created. No Pickands/Palm/Rice closure branch was reopened.

The revision does **not** revive:

```text
Step-13 ell~49;
Step-20 upper Rice switch;
raw Step-27 tiny-chi values;
Step-44 as continuum truth;
Steps 47-49 as exact finite-u scan probabilities.
```

---

## 23:06 EDT — finite-information robustness companion consolidated

New file: `PAPER_A_FINITE_INFORMATION_COMPANION.md`.

The already-validated smooth finite-information calculation was extracted from the historical Steps 14–16 rather than recomputed as part of a new Gaussian-extremes branch.

For the documented calibration near

```text
rho0 ~ 6.2
r = 1.2
alpha = 1e-6
beta = 0.90
kappa = 8,
```

continuous Rice theory gave

```text
ell_s = 0.571441752,
```

while Palm-corrected rare-event validation gave approximately

```text
ell_s = 0.5721 +/- 0.001.
```

The relative shift is only about `0.12%`.

This is retained strictly as **robustness evidence for a smooth finite-information companion model**, not the exact hard-window Paper-A phase boundary.

---

## 23:14 EDT — post-revision hostile audit and cleanup

New files:

- `PAPER_A_POST_REVISION_AUDIT_2026-08-12.md`
- `PAPER_A_POST_REVISION_AUDIT_ADDENDUM_2026-08-12.md`

The revised theorem was re-audited after the semantic repair.

Two presentation-level issues were found and fixed:

1. `q_0` is now explicitly an **analysis variable only**, never receiver side information.
2. `Gamma_infty` is now defined directly from the full-template process rather than only through a limit symbol.

The finite-template/full-template link was tightened using normalized-template `L2` convergence and the uniform covariance bound

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
```

No new fatal contradiction was found.

---

## 23:22 EDT — robust Paper-A quantitative regime witness

New file:

`PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`

New reproducible numerical script:

`numerics/paper_a_full_template_feasibility.py`

### Strategy

Do **not** numerically relocalize the rough finite-duration crossover.

Instead combine:

```text
exact known-time fast preference
+
full-template slow-only guarantee-feasibility witness
+
analytic crossover theorem.
```

This avoids the Step-13 covariance-cusp failure because the feasibility boundary is governed by the smooth full-template process

```math
R_\infty(y)=(1+|y|)e^{-|y|}.
```

### Parameters

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=1.2.
```

At known arrival,

```math
\boxed{x_0=1.80519795247,}
```

so

```text
T_G,f(0)/tau_f = 1.80520
T_G,s(0)/tau_f = 2.16624
```

and fast is strictly preferred.

Choose the common physical uncertainty

```math
\boxed{L=3.30\tau_f=2.75\tau_s.}
```

The full-template feasibility threshold is

```math
c=\rho_0-\Phi^{-1}(\beta)=2.21844843446.
```

### Production numerical run

```text
240000 paired paths
seed = 20260818
x_tail = 16
delta = .01, .005, .0025 nested grids
```

Tail truncation:

```math
1-\eta(16)=6.90\times10^{-12}.
```

Nested-grid PFA results:

| `delta` | slow `ell=2.75` | fast `ell=3.30` |
|---:|---:|---:|
| `.0100` | `.04733333` | `.05362917` |
| `.0050` | `.04736250` | `.05365000` |
| `.0025` | `.04737083` | `.05365833` |

Finest-grid exact 95% Clopper-Pearson **sampling** intervals:

```math
P_{FA,s}\in[0.0465243,0.0482283],
```

```math
P_{FA,f}\in[0.0527601,0.0545674].
```

Since `alpha=.05` lies cleanly between the intervals,

```text
slow -> guarantee-feasible
fast -> guarantee-infeasible
```

at the same physical `L`.

The CP intervals quantify Monte Carlo sampling uncertainty only. Grid and filter-tail approximation were checked separately by nested-grid stability and the `6.9e-12` omitted squared-template-energy fraction.

**Interpretation:** this is a robust finite-scale regime witness, not a numerical localization of `L_x` and not a computer-assisted continuum proof.

The severe-review quantitative-example objection is considered resolved without creating Step 50.

---

## 23:22 EDT — deeper acquisition / optical-acquisition prior-art audit

New file:

`PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`

The novelty burden narrowed materially.

### Direct conceptual prior art

Classical PN/spread-spectrum acquisition already treats acquisition time as a function of combinations of:

```text
unknown code phase / delay uncertainty;
a priori epoch information;
predetection SNR;
Pd and Pfa;
dwell/integration time;
matched-filter structure;
serial/parallel/sequential search.
```

Canonical matched-filter acquisition lineage includes Polydoros & Weber (1984) and Su (1988).

### Optical acquisition prior art

Optical-CDMA literature already studies synchronization/acquisition time, including threshold and dwell/search effects. Direct-detection Geiger-mode APD ladar has also been studied for target acquisition within a specified range window under constant false alarm.

Additional ladar literature establishes pulse-width / range-resolution and range-estimation tradeoffs.

Therefore do **not** claim novelty for:

```text
unknown-delay search;
search-size penalty;
acquisition time versus dwell/integration;
Pd/Pfa tradeoffs;
optical acquisition;
pulse-width / range-resolution tradeoffs.
```

### Remaining candidate contribution

No reviewed source directly reproduced the complete construction

```text
same optical event
+ causal detector family
+ equal eventual matched-filter SNR
+ detector time-scale change
+ simultaneous evidence-clock and search-correlation rescaling
+ fixed physical arrival uncertainty
-> fast/slow guarantee-time reversal and slow-only feasibility.
```

Disposition remains

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

No `first`, `novel`, or priority language is authorized.

---

## 23:22 EDT — Paper A integrated with witness and acquisition positioning

`PAPER_A_DRAFT.md` was revised so that:

- the Introduction explicitly acknowledges mature acquisition theory and optical acquisition;
- the candidate contribution is narrowed to the detector-time-scale coupling under equal event-specific eventual SNR;
- the quantitative regime witness appears immediately after Proposition 1;
- the paper no longer says the quantitative example or acquisition audit are open;
- numerical language distinguishes a regime witness from a measured hard-window crossover;
- the Step-49 hard stop remains explicit in the surrounding audit trail.

A final production run with `x_tail=16` and `240000` paths strengthens the originally inserted `120000`-path witness; the dedicated quantitative-witness file and `CURRENT_STATE.md` carry the production numbers. The qualitative manuscript regime classification is unchanged. Before final typesetting, synchronize any preliminary numerical table values in `PAPER_A_DRAFT.md` to the production run if they are still present.

---

## Current stopping point

The prior two major Paper-A blockers beyond semantics are now resolved at the scientific-presentation level:

```text
robust quantitative regime witness -> RESOLVED;
deeper acquisition / optical-acquisition prior-art audit -> COMPLETED.
```

The active task is a **final integrated hostile-review and citation QA**.

Do not reopen the Gaussian-extremes branch unless that audit identifies a genuinely new mathematical defect.

### Single next question

> Does the integrated Paper A survive a fresh hostile-review pass when the theorem, quantitative witness, acquisition-theory positioning, references, and claim boundaries are tested together?
