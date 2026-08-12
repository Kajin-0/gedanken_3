# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-six logical steps completed. Step 36 converts the Step-35 threshold-buffer problem from global Gaussian anti-concentration into a fixed-excursion-cluster maximum strip measure. The strip probability is bounded by an exact lower-level occupation-Palm first moment that survives the rough endpoint. For the original fast high-band trajectory, numerical strip intensity near `u~4.959` is about `5 alpha` per unit threshold across `kappa_f=170,300,1000,infinity`, showing the required rare-event `O(alpha delta)` scale. The current frontier is an analytic uniform hazard/density bound for that cluster-maximum measure. No universal scalar replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/TAIL_SENSITIVE_CLUSTER_STRIP_CONTINUITY_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/cluster_maximum_strip.py`
6. preceding continuity step: `experiments/01-equal-dstar-different-speed/Q_COUPLING_CONTINUITY_OBSTRUCTION_STEP.md`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, cancellations, counterexamples, negative results, rejected shortcuts, failed numerical estimates, numerical validations, invalidations, asymptotic limits, refinements, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:
1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch exact current blob SHA before replacing existing files;
4. never overwrite stale state;
5. preserve failed/corrected branches and why they changed;
6. make narrow edits or explicit compact consolidations;
7. update `CURRENT_STATE.md` whenever the frontier changes;
8. append or explicitly consolidate `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides chat summaries, memory, and stale recovery notes.**

---

## 2. Epistemic labels

Use where useful:
- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization.
- **DERIVED** — follows mathematically from stated assumptions.
- **CONDITIONAL** — true only under listed assumptions.
- **CONDITIONAL THEOREM SKETCH** — theorem structure identified but technical probability steps remain.
- **COUNTEREXAMPLE** — construction sufficient to disprove implication.
- **REFINEMENT** — sharpens prior statement without erasing it.
- **NEGATIVE RESULT** — candidate effect tested and absent under stated model.
- **REJECTED SHORTCUT** — tempting inference shown not to answer actual question.
- **FAILED NUMERICAL ESTIMATE** — failed validation; never reuse as result.
- **NUMERICAL VALIDATION** — survived stated cross-checks within scope.
- **NUMERICAL COLLAPSE** — independent data collapse under a derived scaling variable.
- **NUMERICAL ASYMPTOTIC** — numerically stable limiting law not yet fully proved.
- **NUMERICAL CLOSURE** — multiple independent numerical/asymptotic pieces exclude a candidate behavior for the stated calibration, without constituting a theorem.
- **PARTIAL CERTIFICATE** — analytic inequality settles the stated comparison on a tested parameter range; numerical evaluation may still be non-interval floating point or Monte Carlo.
- **NUMERICAL ENDPOINT CERTIFICATE** — exact inequality plus statistically resolved endpoint moment estimates; not formal interval arithmetic.
- **PAIRED NUMERICAL INTERVAL CLOSURE** — common-random-number differences plus explicit Monte Carlo/grid/mesh allowances cover an adaptively sampled/interpolated parameter interval; not theorem-level continuity.
- **TAIL-SENSITIVE ENVELOPE** — exact rare-event probability bound expressed through a physical excursion-cluster maximum measure rather than a global supremum density; local numerical intensity may still require certification.
- **INVALIDATED** — previously reported result fails stronger calculation.
- **INVALIDATED INTERMEDIATE** — provisional same-turn value shown wrong; preserve why.
- **INVALIDATED NUMERICAL INTERPRETATION** — generated values remain data but stronger analysis shows they were not estimates of the quantity previously assigned to them.
- **ASYMPTOTIC** — controlled limiting regime only.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is permitted only for the explicitly derived model-reduced canonical crossover function.

---

## 3. Compact surviving chain

### Steps 01–13
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem; finite observation can make phase/temporal placement operationally relevant. Finite-record SNR and task-level detection time were derived. Faster SNR accumulation can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.  
**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.  
**FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid `ell~49` crossover invalid.

### Steps 14–23
A genuine timing-information bandwidth removes the hard-window cusp. Exact smooth Palm rare-event identity is available; Rice becomes nonuniform as bandwidth grows. With common physical bandwidth, fixed physical signal/noise produces a genuine finite large-`r` optimum; Palm later confirms a shallow optimum. At finite `r=2`, `Lambda=0.895`, Rice's upper switch at `130.1945883` is **INVALIDATED**; Palm preserves only the lower switch `~21.7 +/-0.3`. Palm maps the high-band boundary near `Lambda~0.91`; direct occupation sampling gives rough endpoint `Lambda_cross^infinity~0.905 +/-0.004`, leaving `Lambda=0.895` fast-preferred.

### Steps 24–30
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Common-noise coupling, Bessel extremum zoom-in, and Brownian–parabola scaling identify the high-band smoothing structure. **INVALIDATED INTERMEDIATE:** coupling coefficient `0.8131`; correct pointwise value is `0.8906480701 sqrt(chi/zeta)`. Small-`chi` crossover uses `mu=sqrt(2)zeta chi^(1/3)` and reduces to

```math
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were grid biased; refined full-field values agree with the canonical function. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31
Canonical crossover plus empirical finite-`u` anchoring gave a one-hump boundary peaking near `kappa_f~94.9`, `Lambda~0.91068`, then descending toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** no high-band re-entrant pocket supported for `Lambda=0.895`. Later direct finite-`u` steps remove dependence on this empirical fit for the original conclusion.

### Step 32
Finite-`u` first-/second-order Rice moment enclosure certifies fast feasible / slow infeasible through at least `kappa_f=170`. **NEGATIVE RESULT:** raw crossing moments fail around `175–200` because micro-upcrossing multiplicity explodes inside one physical excursion.

### Step 33
Finite-amplitude excursion-cluster count `C_Delta` satisfies

```math
sup z>u iff C_Delta>=1
```

and gives first-/second-moment probability bounds with exact lower-level occupation-Palm identities. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`. **NUMERICAL ENDPOINT CERTIFICATE.**

### Step 34
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955`, slow `L_s/alpha~>1.10` over `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE.** Inter-node allowance remains empirical.

### Step 35
Normalized spectral amplitude obeys

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

The common-noise field is `L2`-Lipschitz in `q` through the rough endpoint. Fast `Delta q=0.005` gives pointwise RMS process change `~<7.5e-5` and threshold motion `~<2.8e-5`. **REJECTED SHORTCUT:** cluster moments are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders too coarse at `alpha=1e-6`.

### Step 36 — current frontier
Freeze one lower excursion level `a`; let `M_j` be maxima of its connected components and define

```math
C_a(y)=sum_j1_{M_j>y}.
```

For `a<y1<y2`,

```math
D_a(y1,y2)=C_a(y1)-C_a(y2)
=sum_j1_{y1<M_j<=y2}.
```

Then

```math
\boxed{
P(y1<sup z<=y2)<=E[D_a(y1,y2)].
}
```

Under lower-level occupation-Palm,

```math
\boxed{
E[D_a(y1,y2)]
=ell Q(a)E_a[1_{y1<M_I<=y2}/L].
}
```

Equivalently define

```math
nu_a(B)=ell Q(a)E_a[1_{M_I in B}/L],
```

so the strip probability is bounded by `nu_a((y1,y2])`. This is derivative-free and rough-endpoint valid.

Fast high-band diagnostics (`x=7.16`, `ell=.895`, `Delta=.15`, `u~4.959`) give

```text
kappa_f   nu((u-w,u+w])/(2w alpha), w=.005-.02
170                ~4.95–5.16
300                ~5.03–5.17
1000               ~5.17–5.54
infinity           ~5.19–5.53
```

so local cluster-max strip intensity is numerically `~5 alpha` per unit threshold. Therefore the observed buffered probability scales as `~10 delta alpha`; a `delta=1e-4` linear extrapolation is order `1e-9` absolute rather than global `O(1e-4)`.

**TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION:** the correct rare-event object has been isolated and has the required scale. **OPEN:** no analytic uniform local density/hazard bound yet.

---

## 4. Current frontier

Derive a uniform analytic bound on the local cluster-maximum intensity over `0<=q<=0.0767`, ideally in hazard form tied to the rare successful-cluster intensity.

---

## 5. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is exact;
- raw Step-27 fast values are continuum crossover data;
- Step-31 empirical `delta(kappa)` is exact or required for the original high-band conclusion;
- Step-33/34 Monte Carlo estimates are formal interval arithmetic;
- Step-34 is theorem-level continuous-parameter closure;
- Step-35 field Lipschitz continuity implies cluster-moment Lipschitz continuity;
- generic Gaussian anti-concentration is sharp enough at the rare-event scale;
- Step-36 proves a uniform density/hazard bound;
- the `delta=1e-4` strip value is analytically certified;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the local cluster-maximum intensity `h_{a,q}(u)` be bounded analytically and uniformly over the high-band `q` interval—ideally by a rare-event hazard form such as `h_{a,q}(u) <= C u E[C_a(u)]`—so that the buffered-threshold term becomes theorem-level rather than numerically extrapolated?
