# Paper A — Adversarial Reviewer Audit

**Date:** 2026-08-12  
**Status:** ADVERSARIAL REVIEW / MAJOR REVISION / NO FATAL INTERNAL MATHEMATICAL CONTRADICTION FOUND / BLOCKING OPERATIONAL-INTERPRETATION ISSUES / NOVELTY NOT ESTABLISHED

**Manuscript audited:** `PAPER_A_DRAFT.md` at blob `00db20f3d2c91587415decfd97861a87cf1693ba`.

This audit deliberately reads the manuscript as a skeptical technical reviewer looking for reasons to reject it before figures, formatting, or submission work.

---

## 1. Overall disposition

### Reviewer-style disposition

**MAJOR REVISION BEFORE SUBMISSION.**

I did **not** find a fatal algebraic or Gaussian-comparison contradiction in the present core derivation. In particular, the following survive direct checking under the manuscript's stated white-Gaussian normalization:

- the equal-eventual-SNR normalization `A_tau ∝ tau^(-3/2)`;
- the accumulated squared-SNR fraction

```math
eta(x)=1-e^{-2x}(1+2x+2x^2);
```

- the finite-template autocorrelation `R_x(y)`;
- the positive-weight-average rewrite used to prove `R_x(y)` is nondecreasing in `x`;
- the Slepian comparison direction: larger covariance -> stochastically smaller supremum -> no larger global threshold;
- the strict increase of the true-alignment margin with observation duration;
- the dimensionless scaling

```math
T_D=tau X_D(rho_0,alpha,beta,L/tau);
```

- the both-feasible / slow-only / neither feasibility partition;
- the exclusion of fast-only feasibility within the deliberately equal-eventual-SNR scaled family;
- the intermediate-value crossover proof **conditional on Proposition 1's assumptions**.

The manuscript is therefore not failing because the central algebra is obviously wrong.

However, two interpretation issues are severe enough that I would not submit the paper in its present form:

1. `T_D` is not yet operationally defined as an ordinary wall-clock or online detection latency.
2. `P_D,true` is a true-alignment exceedance criterion, not the full signal-present scan detection probability.

Those two points can make the title/abstract read as a stronger result than is actually established.

---

# 2. BLOCKING ISSUE A — what exactly is `T_D` in physical time?

The manuscript says event arrival is unknown over a fixed physical interval `L`, then scans every candidate arrival with a finite template of duration `t` and calls the first qualifying `t` the "detection time."

For the scan to be stationary and for every candidate arrival in `[0,L]` to have the same full template support `[0,t]`, the available data record must contain the entire template after the latest candidate arrival. Operationally that means a batch record of length approximately

```math
L+t.
```

The present manuscript never states this acquisition protocol explicitly.

That creates an immediate reviewer question:

> From what clock origin is `T_D=t` measured if the true arrival is unknown?

If the receiver waits until the complete uncertainty interval has elapsed and then requires `t` additional samples after the latest possible arrival, the actual elapsed batch-decision time from the start of the window is

```math
T_wall=L+T_D.
```

Because `L` is common to the two detectors, the fast/slow ordering in `T_D` is unchanged. So this is **fixable without changing the theorem**.

But the protocol must be stated. Otherwise a reader can reasonably interpret `T_D` as an online stopping latency after an unknown event, which is not the problem solved here.

### Required correction

Define one explicit acquisition protocol, e.g.:

```text
The event is known to occur somewhere in a fixed window of length L.
A batch decision is made after acquiring enough data to contain t post-arrival
samples for every candidate arrival, i.e. a record of duration L+t.
T_D is the additional post-window integration duration required by the criterion.
```

Then either:

- retain `T_D` but call it **required integration duration** / **post-window integration duration**, or
- define `T_wall=L+T_D` and note that the ordering is identical at fixed `L`.

Do not describe the current result as a general sequential or online detection latency.

**Severity:** BLOCKING / FIXABLE.

---

# 3. BLOCKING ISSUE B — `P_D,true` is not the actual scan detection probability

The manuscript defines

```math
P_{D,true}
=Phi[rho_0 sqrt(eta(x))-Gamma(x,ell,alpha)].
```

This is the probability that the statistic evaluated at the **true alignment** exceeds a threshold chosen from the maximum of the noise-only scan.

It is not

```math
P_D^{scan}
=Pr[sup_q Z_signal(q)>Gamma].
```

The manuscript correctly acknowledges this distinction in Section III, but the title, abstract, theorem name, and repeated phrase "detection time" can still be read as referring to the actual global scan detector.

There is an important one-sided relationship:

```math
{true-alignment statistic > Gamma}
subseteq
{supremum of signal-present scan > Gamma},
```

hence

```math
P_D^{scan} >= P_{D,true}.
```

Therefore the present criterion is a **conservative sufficient condition** guaranteeing at least `beta` total scan-detection probability.

But the corresponding first-crossing time is a guarantee time / sufficient integration duration. A reversal of these sufficient times does **not by itself prove** that the exact signal-present scan detection times reverse. Off-alignment signal contributions can lower the actual required time differently for the two templates.

This is the strongest current reviewer objection.

### Two legitimate repair paths

#### Path B1 — reframe, without new mathematics

Make the criterion the explicit object of the paper:

- call it a **true-alignment guarantee criterion**;
- define `T_G` or "guaranteed detection integration time" rather than an unqualified `T_D`;
- state that `P_D,true >= beta` guarantees the global scan declares a detection with probability at least `beta`;
- state explicitly that the theorem orders this guaranteed operating time, not the exact signal-present scan maximum.

This preserves the current proof almost unchanged but narrows the claim.

#### Path B2 — stronger but substantially harder

Replace the true-alignment surrogate by the actual signal-present supremum distribution and prove/map the corresponding task surface.

This would be scientifically stronger but risks reopening a difficult Gaussian-extremes branch that the project intentionally hard-stopped.

### Reviewer recommendation

Use **Path B1** unless a journal or reviewer specifically requires full scan-power ordering. It is better to make a narrower theorem exact than to imply a stronger one that has not been proved.

**Severity:** BLOCKING / CLAIM-SCOPE ISSUE.

---

# 4. MAJOR ISSUE C — the manuscript has hidden the common optical input / physical detector realization

The manuscript currently begins directly with the output family

```math
s_tau(t)=A_tau t e^{-t/tau}u(t).
```

It says the waveform "can be generated by a stable causal linear response," but does not show the common optical input or detector transfer function.

This makes the construction look like a generic family of hand-chosen Gaussian-channel templates rather than a photodetector thought experiment.

The earlier derivation already contains a clean physical realization:

```math
p(t)=e^{-bt}u(t),
```

and

```math
G_tau(s)
=A_tau (s+b)/(s+1/tau)^2,
```

which gives

```math
G_tau(s) P(s)=A_tau/(s+1/tau)^2
```

and hence

```math
s_tau(t)=A_tau t e^{-t/tau}u(t).
```

`G_tau` is causal, proper, and stable for positive `b,tau`.

### Why this matters

The paper's main value is detector-facing synthesis. If it does not show that the compared outputs arise from the **same incident optical event through realizable time-scaled linear detector channels**, a reviewer can dismiss the construction as generic signal processing.

### Required correction

Restore the fixed input and transfer-function construction in Section II, even if only in one compact paragraph/equation pair.

Also say explicitly that equal eventual matched-filter SNR is **event-specific**. It is a deliberately stronger/fairer normalization than equal scalar reference `D*`; it is not a universal equality of detector sensitivity for all possible inputs.

**Severity:** MAJOR / EASY TO FIX.

---

# 5. MAJOR ISSUE D — Proposition 1 is more conditional than it needs to be

The current central proposition assumes:

1. known-time feasibility;
2. continuity of `X_D` in `ell`;
3. `Gamma_infty(ell,alpha)->infinity`;
4. `X_D->infinity` at `ell_crit`.

A skeptical mathematical reviewer can say that assumptions 2–4 carry much of the burden of the crossover theorem, making the final result close to an intermediate-value observation.

At least part of this can be strengthened from the specific process rather than assumed.

## 5.1 Assumption 4 can largely be derived

For every finite `x`,

```math
eta(x)<1,
```

and the covariance ordering gives

```math
Gamma(x,ell,alpha)>=Gamma_infty(ell,alpha).
```

Thus

```math
M(x;ell)
< rho_0-Gamma_infty(ell,alpha)
=M_infty(ell).
```

If the boundary satisfies

```math
Gamma_infty(ell_crit,alpha)=rho_0-z_beta,
```

then every finite `x` satisfies

```math
M(x;ell_crit)<z_beta.
```

With ordinary continuity of the finite-`x` margin in `ell`, a bounded sequence of crossing times as `ell↑ell_crit` would give a contradiction. This supplies the divergence rather than assuming it separately.

## 5.2 Assumption 3 is standard extreme-value behavior for this covariance

The full-template covariance is

```math
R_infty(y)=(1+y)e^{-y},
```

which decays exponentially to zero. Classical stationary-Gaussian extreme-value theory implies that maxima over expanding intervals grow without bound. This should be cited or proved at the level needed by the paper rather than left as a naked assumption.

Relevant primary literature includes:

- D. Slepian, "The One-Sided Barrier Problem for Gaussian Noise," *Bell System Technical Journal* 41, 463–501 (1962), DOI `10.1002/j.1538-7305.1962.tb02419.x`.
- Classical Berman/Pickands stationary-Gaussian maximum results; the present exponentially decaying covariance is in the standard weak-dependence regime.

## 5.3 Slepian comparison itself needs an explicit citation

The monotone-threshold result is central enough that "standard Gaussian comparison" is too terse for the submitted paper.

### Required correction

Turn Proposition 1 into a theorem/corollary whose assumptions are minimized and whose continuity/extreme-value ingredients are either proved in a short appendix or tied to precise references.

**Severity:** MAJOR FOR MATHEMATICAL PRESENTATION; NOT A DISCOVERED COUNTEREXAMPLE TO THE RESULT.

---

# 6. MAJOR ISSUE E — no quantitative, non-knife-edge example remains in the main paper

The current manuscript proves that at least one crossover exists, but it does not show where one occurs for any representative `(rho_0,alpha,beta,r)`.

A reviewer can therefore say:

> The crossover may exist only arbitrarily close to the fast detector's divergence boundary and may have negligible practical relevance.

The later Steps 13–49 correctly showed that a particular high-band endpoint witness was numerically delicate. That is exactly why the paper should **not** resurrect the Step-44 knife edge.

But the main paper still needs at least one robust illustrative example or phase diagram away from a pathological endpoint.

### Required correction

After Issues A–D are fixed, generate one continuum-validated example with comfortable margins showing:

- known/low `L`: fast preferred;
- a finite crossover while both remain comfortably feasible;
- slow-only feasibility at larger `L`.

The numerical figure does not need to carry the theorem. Its purpose is physical scale and reader intuition.

Do not use the invalidated Step-13 `ell~49` result or present the Step-44 finite-grid knife edge as continuum truth.

**Severity:** MAJOR FOR IMPACT / NOT A THEOREM DEFECT.

---

# 7. MAJOR/MINOR ISSUE F — detector terminology and noise normalization need tightening

## 7.1 `D*` bandwidth wording

The Introduction says `D*` combines responsivity, noise, active area, and measurement bandwidth. This is easy to misread as detector temporal bandwidth.

Conventional `D*` uses a **noise-equivalent measurement bandwidth normalization** (typically through `sqrt(A Delta f)` / NEP); that is not the same object as the detector's temporal response bandwidth or 3-dB bandwidth.

Because the paper is specifically about speed, the manuscript should make this distinction explicit in the first paragraph.

## 7.2 White-noise convention

"two-sided spectral density `N` under a consistent normalization" is not publication-grade.

State a definite convention, e.g.

```math
E[n(t)n(t')]=N delta(t-t'),
```

so that

```math
rho^2=(1/N) int s^2(t) dt.
```

Under that convention the current

```math
A_tau=2 rho_0 sqrt(N)/tau^(3/2)
```

is correct.

Without the explicit convention, readers can reasonably wonder about a factor-of-two error.

**Severity:** MAJOR PRESENTATION / EASY TO FIX.

---

# 8. PRIOR-ART / NOVELTY RISK — still material

The manuscript's conservative novelty language is appropriate and should remain.

The following established ingredients were verified:

- Jones 1960 explicitly derives pulse/energy detectivity from frequency-dependent `D*(f)`; DOI `10.1364/JOSA.50.000883`.
- Garcia & Dereniak 1990 explicitly measure a `D* × bandwidth` product in an infrared photoconductor; DOI `10.1364/AO.29.000559`. An erratum exists at DOI `10.1364/AO.29.002838`.
- Yang et al. 2026 explicitly define `USBL = Detectivity × Bandwidth`; DOI `10.1038/s41467-026-72259-1`.
- Pecunia et al. 2025 explicitly emphasize accurate characterization/reporting and application-dependent benchmarking; DOI `10.1038/s41566-025-01759-1`.
- Vio & Andreani 2016 show that unknown signal position changes matched-filter false-detection statistics through the peaks of a correlated Gaussian field; arXiv `1602.02392`.
- Morras et al. show that matched-filter false-alarm behavior in Gaussian noise depends on template/PSD autocorrelation and can be represented through an effective sampling rate; *Phys. Rev. D* 107, 023027 (2023), arXiv `2209.05475`.
- Croce et al. treat whole-bank supremum false alarms for correlated matched-filter/template searches; *Phys. Rev. D* 70, 122001 (2004), arXiv `gr-qc/0405023`.

A particularly relevant adjacent optical/ranging paper is:

- A. B. Milstein et al., "Acquisition algorithm for direct-detection ladars with Geiger-mode avalanche photodiodes," *Applied Optics* 47, 296–311 (2008), DOI `10.1364/AO.47.000296`, which studies constant-false-alarm target acquisition within a specified range window and explicitly minimizes acquisition time.

That paper is **not** a direct match to the present fast/slow equal-eventual-SNR reversal, but it shows that the intersection of photodetection, unknown delay/range windows, false alarms, and acquisition time has substantial prior art.

### Novelty disposition remains

```text
POSSIBLE SYNTHESIS CONTRIBUTION / NOVELTY NOT ESTABLISHED.
```

Before any "first" or "novel" language, perform a deeper citation-network search in radar, sonar, ladar, optical receivers, synchronization/acquisition, and unknown-delay detection using terms such as:

```text
range window
acquisition time
unknown delay
matched-filter correlation width
number of resolution cells
time-bandwidth product
global false alarm
waveform duration / pulse width
```

**Severity:** PUBLICATION-POSITIONING RISK.

---

# 9. Citation and reference QA

### References currently well supported

- Jones 1960: strong and directly relevant.
- Garcia & Dereniak 1990: strong for established detectivity-bandwidth benchmarking.
- Yang et al. 2026: valid current example of an explicit detectivity-bandwidth product.
- Pecunia et al. 2025: strong for characterization/reporting/application benchmarking.
- Morras et al. and Croce et al.: strong adjacent matched-filter/global-false-alarm support.

### Improvements recommended

1. Add the DOI for Yang et al.: `10.1038/s41467-026-72259-1`.
2. Add a direct Slepian/Gaussian-comparison citation at the Section III covariance-ordering step.
3. Add a precise stationary-Gaussian extreme-value citation for the large-`ell` growth used in Proposition 1.
4. Consider replacing or supplementing the arXiv-only Vio & Andreani reference with a peer-reviewed follow-up if a clean journal version is available.
5. Garcia & Dereniak have a published erratum; it is not obviously relevant to the manuscript's use of that paper, but it should be checked before relying on any detailed equation from the original.

---

# 10. Minor/editorial issues

- Consider changing the title from **"equal asymptotic sensitivity"** to wording that says **"equal eventual matched-filter SNR"** or "equal event-integrated sensitivity." `rho_0` is event-specific, whereas "sensitivity" sounds detector-global.
- Consider "photodetector channels" rather than unqualified "photodetectors" unless the common optical input and transfer function are restored.
- Define `Phi` explicitly as the standard-normal CDF at first use.
- Keep one symbol for the crossover (`L_x` or `L_×`) throughout.
- If `Gamma` is defined via a generalized quantile, avoid phrases implying a unique exact equality for every `alpha` unless the no-atom property is stated.
- Make "more strongly correlated" explicitly family-specific whenever used in Section V.
- The current conclusion is appropriately cautious; do not strengthen it during revision.

---

# 11. What I would write as a hostile referee report today

> The manuscript presents a clean scaling construction showing that a shorter detector time scale can simultaneously accelerate signal accumulation and enlarge an unknown-arrival matched-filter search when eventual SNR is held fixed. The algebraic scaling and Gaussian covariance ordering appear internally consistent. However, in its present form the central "detection-time reversal" is not yet operationally defined as an online detection latency, and the stated detection probability is evaluated only at the true template alignment rather than for the full signal-present scan. Consequently the strongest wording of the title and abstract exceeds what is presently proved. The detector-specific realization should also be made explicit, and several assumptions in the crossover proposition should be proved or tied to standard Gaussian-extreme results rather than simply assumed. I would recommend major revision rather than rejection on mathematical grounds, provided the authors narrow the operating criterion, define the acquisition protocol precisely, and add one robust quantitative example.

---

# 12. Ranked repair order

Do **not** work on journal formatting or final figures yet.

Repair in this order:

1. **Operationally define the batch acquisition / decision clock and `T_D`.**
2. **Reframe `P_D,true` as a guaranteed true-alignment criterion, or explicitly solve the stronger full-scan problem.**
3. **Restore the fixed optical input + stable causal detector transfer-function realization.**
4. **Strengthen Proposition 1 by proving/citing the continuity, boundary-divergence, and large-search properties that are currently assumptions.**
5. **Add one robust, non-knife-edge numerical example/phase diagram.**
6. Tighten `D*` bandwidth wording, white-noise normalization, and citations.
7. Only then perform final novelty audit, figures, and journal formatting.

---

## Stopping point

This audit does **not** reopen Steps 13–49. The central detector-facing algebra survives, but the paper should not be submitted until the two blocking operational/criterion issues are repaired.

### Single next question

> Can the manuscript be revised first to make the acquisition clock and the true-alignment guarantee criterion operationally exact, without changing the existing Gaussian-extremes hard stop or claiming a full signal-present scan theorem?
