# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 21:03 EDT:** mathematical closure stopped after Step 49; prior-art audit and short-paper architecture completed; Paper A is now drafted through Section IV. Novelty is not established. Full derivations and all failed/corrected branches remain in dedicated step files.

---

## Steps 01–12 — detector/detection-theory core

Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Full magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian problem. Finite windows make phase/time placement relevant. Unknown arrival introduces global false-alarm timing-search complexity. In the defined continuous scanning protocol, a controlled equal-eventual-SNR family can reverse fast/slow ranking because temporal compression changes both early evidence accumulation and timing-search correlation length. This is protocol/task specific, not a universal detector theorem.

Exact detector-facing scaling:

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

For `r=tau_s/tau_f>1` and `ell=L/tau_s`, the exact task boundary is

```math
B_r(\ell)=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

Under the Step-12 continuity/extreme-value assumptions: fast wins at known time; approaching the fast feasibility boundary, fast detection time diverges while slow remains feasible; therefore at least one finite fast-to-slow crossover exists. Slow-only feasibility is possible, fast-only feasibility is excluded in this equal-eventual-SNR scaled family, and uniqueness is not established.

---

## Steps 13–49 — mathematical stress-test branch

The later branch tested whether the difficult continuous timing-search problem invalidated the detector-facing construction.

Key corrections and failures retained:

- **FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover `ell~49` was invalid; hard-window timing scans are locally Brownian-like.
- Genuine finite information bandwidth removes the cusp; an invertible noiseless low-pass does not because optimal whitening cancels it.
- Rice's apparent upper switch near `kappa_f~130` was **INVALIDATED**; Palm analysis preserved only the lower switch near `21.7 +/- .3`.
- **INVALIDATED INTERMEDIATE:** rough/smoothed coupling coefficient `.8131`; corrected `.8906480701 sqrt(chi/zeta)`.
- **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-chi values were grid biased.
- Crossing counts fail at high bandwidth because one physical excursion contains many micro-upcrossings; finite-amplitude excursion clusters replace them.
- Step 39 found `R=N_a/N_tan~1.56`, rejecting the shortcut that the finite-u correction is a small-amplitude remainder.
- Step 40 introduced Cameron-Martin exact-event threshold translation.
- Step 41 replaced empirical q interpolation with analytic Gaussian-process control.
- **INVALIDATED NUMERICAL VALUE:** Step-35 tiny-q pair RMS `~5.4e-5`; corrected asymptotic `~2.69e-5`.
- Raw inverse-duration Palm concentration was formally bounded but useless; duration truncation enabled a finite-sample endpoint calculation.
- Step 44 produced a genuine pointwise finite-grid 95% bound `P_FA/alpha<.999957771`, but with only `.00004223 alpha` margin, so continuum grid bias dominated.
- Step 45 showed witness retuning trades one near-boundary problem for another.
- Step 46 isolated missed between-sample maxima as the dominant grid error. **WORDING CORRECTION:** the five-event paired result has ~47% relative SE and supports sign/scale consistency only, not precise coefficient verification.
- Step 47 obtained the exact pure-alpha1 discrete Pickands correction.
- Step 48 found the mixed Brownian-parabola finite-level transfer correction only `O(1e-5)` relative to an `O(9e-4)` discretization loss.
- Step 49 simulated the exact finite-window covariance directly and found the same grid-loss scale; higher-order covariance did not cancel it at order `1e-4`.

**HARD-STOP TRIGGERED at Step 49:** the remaining publication-grade finite-u mapping from exact-covariance spectral intensity to exact finite-search false-alarm probability is no longer proportionate to the detector question. Do not create Step 50 by default.

---

## Detector-facing prior-art audit — 20:31 EDT

Full audit: `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

Direct prior art establishes:

- pulse/energy detectivity from frequency-dependent detector response;
- sensitivity-speed / detectivity-bandwidth joint benchmarking;
- unknown-arrival matched-filter search penalties controlled by correlated peak statistics/template autocorrelation;
- standard all-pass magnitude preservation with altered phase/dispersion.

No direct hit was found in the focused audit for the complete equal-eventual-SNR photodetector construction leading to an explicit fast/slow task reversal.

Disposition:

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

---

## Detector-facing paper architecture — 20:42 EDT

`PAPER_ARCHITECTURE_TASK_REVERSAL.md` fixed a five-section short paper:

1. established detector-metric context and actual finite-task question;
2. controlled equal-eventual-SNR family;
3. dimensionless detection-time surface;
4. task-reversal theorem and feasibility partition;
5. interpretation and limits.

The main paper explicitly excludes Pickands/Palm/Rice/high-band endpoint closure machinery.

---

## Paper A opening manuscript — 20:52 EDT

`PAPER_A_DRAFT_OPENING.md` drafted the title, abstract, Introduction, and Section II through the exact finite-record timing covariance.

Key rhetorical correction: established `D*`, pulse, bandwidth, and unknown-arrival search results are conceded immediately. The actual question is isolated by enforcing

```math
\rho_{\tau,\infty}=\rho_0
```

for every time scale.

---

## Paper A Sections III–IV — 21:03 EDT

New active manuscript: `PAPER_A_DRAFT.md`.

### Section III — detection-time surface

Defines the exact correlated-scan threshold

```math
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)\right]=\alpha,
```

the true-alignment margin

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha),
```

and

```math
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\{x:M(x)\ge\Phi^{-1}(\beta)\}.
```

The Step-11 covariance ordering plus standard Gaussian comparison gives

```math
x_2>x_1
\Rightarrow
\Gamma(x_2,\ell,\alpha)\le\Gamma(x_1,\ell,\alpha),
```

so `M` is strictly increasing. Thus the reversal is not caused by a self-suboptimal filter duration.

The exact physical task collapse is

```math
\boxed{
T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
}
```

The full-template limit defines

```math
\Gamma_\infty(\ell,\alpha),
\qquad
M_\infty=\rho_0-\Gamma_\infty,
```

with finite feasibility when

```math
\Gamma_\infty(\ell,\alpha)<\rho_0-\Phi^{-1}(\beta).
```

### Section IV — exact task boundary and proof

For `tau_f<tau_s`, `r=tau_s/tau_f`, `ell=L/tau_s`:

```math
T_{D,f}=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}=r\tau_f X_D(\rho_0,\alpha,\beta,\ell),
```

so

```math
\boxed{
B_r(\ell)=X_D(r\ell)-rX_D(\ell)=0
}
```

is the exact implicit preference boundary.

With

```math
c=\rho_0-\Phi^{-1}(\beta),
```

the exact feasibility partition is both-feasible / slow-only / neither; fast-only feasibility is excluded because `Gamma_infty` is nondecreasing with search length.

The physical feasibility limit scales exactly as

```math
L_{\mathrm{crit}}(\tau)=\tau\ell_{\mathrm{crit}}.
```

Under the explicitly stated assumptions of known-time feasibility, continuity away from singularities, unbounded large-search threshold growth, and divergence on approach to the feasibility boundary:

```text
L=0 -> fast wins;
L -> L_crit,f^- -> fast detection time diverges while slow remains finite;
therefore at least one finite fast-to-slow crossover exists.
```

No crossover uniqueness is claimed. No universal ordering is claimed.

---

## Current stopping point

Stay inside **Paper A**.

### Single next question

> Can Section V now be drafted to finish the detector-facing narrative, with the practical implication stated strongly but without broadening the theorem beyond the defined task/protocol?
