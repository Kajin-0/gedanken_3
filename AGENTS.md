# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-eight logical steps completed. Step 38 proves the exact cross-elasticity ordering `H(chi,lambda zeta)<=H(lambda chi,zeta)` from `0<=zeta d_zeta F_zeta<=F_zeta` plus Brown–Resnick Slepian comparison. Hence `0<=zeta d_zeta log H<=chi d_chi log H` wherever derivatives exist. Along the fixed-`kappa` threshold trajectory (`chi~u`, `zeta~1/u`), `H` is nondecreasing in `u`, so the matched tangent hazard is uniformly bounded by `phi(u)/Q(u)-1/u`. At `u~4.959` this is `~4.9452`, with symmetric tangent-strip factor `~9.89e-4` for `delta=1e-4`. Step-36 exact finite-`u` cluster strips remain somewhat larger, so the active frontier is now finite-threshold remainder control between the tangent/Pickands intensity and the exact cluster-maximum measure. No universal scalar replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/PICKANDS_ELASTICITY_ORDERING_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/pickands_elasticity_ordering.py`
6. preceding hazard step: `experiments/01-equal-dstar-different-speed/CLUSTER_HAZARD_OVERSHOOT_STEP.md`

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
- **CONDITIONAL CLUSTER EXTENSION** — fixed-class Gaussian extreme-value theorem transferred to finite-amplitude successful clusters under explicit asymptotic single-cluster/multiple-cluster-negligibility assumptions.
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
- **EXACT VARIOGRAM ORDERING** — deterministic pointwise ordering of tangent variograms yielding an exact Brown–Resnick Slepian comparison of generalized Pickands constants.
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
Finite-amplitude excursion-cluster count `C_Delta` satisfies `sup z>u iff C_Delta>=1` and gives first-/second-moment probability bounds with exact lower-level occupation-Palm identities. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`. **NUMERICAL ENDPOINT CERTIFICATE.**

### Step 34
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955`, slow `L_s/alpha~>1.10` over `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE.** Inter-node allowance remains empirical.

### Step 35
Normalized spectral amplitude obeys

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

The common-noise field is `L2`-Lipschitz in `q` through the rough endpoint. Fast `Delta q=0.005` gives pointwise RMS process change `~<7.5e-5` and threshold motion `~<2.8e-5`. **REJECTED SHORTCUT:** cluster moments are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders too coarse at `alpha=1e-6`.

### Step 36
Freeze one lower excursion level `a`; physical excursion-component maxima define

```math
nu_a(B)=ell Q(a)E_a[1_{M_I in B}/L].
```

Exact strip envelope:

```math
P(y1<sup z<=y2)<=nu_a((y1,y2]).
```

Fast high-band diagnostics near `u~4.959` give local strip intensity `~5 alpha` per threshold unit, hence observed `~10 delta alpha` symmetric-strip scaling. **TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION.**

### Step 37
For fixed Gaussian local covariance class, Pickands high-threshold theory plus asymptotic single-successful-cluster separation gives

```math
N_a(u+s/u)/N_a(u)->exp(-s),
```

so cluster overshoot is asymptotically exponential on the `1/u` height scale and `h_a(u)~uN_a(u)` in the iterated limit. This explains the Step-36 rare-event scale. **REFINEMENT / REJECTED SHORTCUT:** fixed-class asymptotics are nonuniform through `q->0` at physical `u~4.96`. The matched tangent hazard left an apparently dangerous positive `zeta d_zeta log H` term.

### Step 38 — current frontier
The finite-band smoothing function obeys exactly

```math
0<=zeta d_zeta F_zeta(t)<=F_zeta(t).
```

Hence for `lambda>=1`,

```math
F_{lambda zeta}(t)<=lambda F_zeta(t),
```

so tangent variograms satisfy

```math
g_{chi,lambda zeta}(t)<=g_{lambda chi,zeta}(t).
```

Brown–Resnick Slepian comparison yields

```math
\boxed{H(chi,lambda zeta)<=H(lambda chi,zeta).}
```

Thus, wherever logarithmic derivatives exist,

```math
\boxed{0<=zeta d_zeta log H<=chi d_chi log H.}
```

Along fixed physical `kappa`, `chi~u` and `zeta~1/u`, so `H` is nondecreasing with threshold exactly. Therefore the matched tangent hazard obeys

```math
\boxed{h_tan/N_tan<=phi(u)/Q(u)-1/u.}
```

At `u~4.959`, this is `~4.9452`. Finite-difference monotonicity gives explicit symmetric tangent-strip factor

```math
B(u,delta)
=((u-delta)/u)Q(u-delta)/Q(u)
-((u+delta)/u)Q(u+delta)/Q(u),
```

with `B(u,1e-4)~9.89e-4`, i.e. `~9.9e-10` when `N_tan~alpha=1e-6`.

**NEGATIVE RESULT / REFINEMENT:** exact Step-36 finite-`u` strip intensity can exceed this tangent coefficient. Therefore the positive smoothing elasticity is not the source of the observed `~5–10%` finite-crossover excess. The outstanding error is the finite-threshold remainder mapping the tangent/Pickands approximation to the exact physical cluster-max measure.

---

## 4. Current frontier

Control the finite-threshold correction factor between exact cluster first moment and matched tangent intensity, especially its threshold variation near `u~5`.

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
- Step-37 fixed-class Pickands asymptotics are quantitatively uniform through `q->0` at `u~5`;
- Step-38 tangent hazard bound is an exact finite-`u` bound for the physical cluster measure;
- Step-36 exact strip excess is caused by `zeta` elasticity;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the exact cluster first moment be factorized as `N_a(u,q)=N_tan(u,q) R(u,q)` with a controlled finite-threshold remainder, and can the threshold variation of `R` be bounded tightly enough at `u~5` to account for the observed `~5–10%` excess in the Step-36 strip intensity?
