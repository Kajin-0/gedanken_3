# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-five logical steps completed. Step 35 analytically justifies `q=kappa_f^(-1/2)` as the regular high-band coordinate: the normalized common-white-noise Gaussian timing field is `L2`-Lipschitz in `q` through the nondifferentiable rough endpoint. For the Step-34 fast channel, a `Delta q=0.005` cell gives pointwise RMS process change `~<7.5e-5` and threshold motion `~<2.8e-5`. However, the excursion-cluster functional is not pathwise Lipschitz, and generic Gaussian-supremum anti-concentration is orders of magnitude too coarse at `alpha=1e-6`. The current frontier is a tail-sensitive successful-excursion continuity bound near `u~5`. No universal scalar replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/Q_COUPLING_CONTINUITY_OBSTRUCTION_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/q_coupling_continuity.py`
6. preceding closure step: `experiments/01-equal-dstar-different-speed/ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md`

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
A genuine timing-information bandwidth removes the hard-window cusp. Exact smooth Palm rare-event identity is available; Rice is nonuniform as bandwidth grows. With common physical bandwidth, fixed physical signal/noise produces a genuine finite large-`r` optimum; Palm later confirms a shallow optimum.

At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches at `25.4898402` and `130.1945883`; Palm preserves only the lower switch `~21.7 +/-0.3`. **INVALIDATED:** upper Rice switch. Palm maps the high-band boundary near `Lambda~0.91`. Direct occupation sampling gives rough endpoint `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` stays fast-preferred.

### Steps 24–30
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Common-white-noise coupling, Bessel extremum zoom-in, and the Brownian–parabola double scaling identify the high-band smoothing structure. **INVALIDATED INTERMEDIATE:** coupling coefficient `0.8131`; correct pointwise RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Small-`chi` crossover uses `mu=sqrt(2)zeta chi^(1/3)` and reduces to

```math
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were grid biased; continuum-extrapolated full-field values agree with the canonical function. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31
Canonical crossover inserted into the finite-`r` boundary; Palm/occupation anchoring gave a one-hump central bridge peaking near `kappa_f~94.9`, `Lambda~0.91068`, then descending toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** no high-band re-entrant pocket supported for `Lambda=0.895`. **CONDITIONAL:** finite-`u` offset was empirical.

### Step 32
Finite-`u` first-/second-order Rice moment enclosure gives

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `X=7.04`, fast is directly certified feasible and slow infeasible through at least `kappa_f=170`. **NEGATIVE RESULT:** raw crossing moments fail near `175–200` because micro-upcrossing multiplicity explodes inside one physical excursion.

### Step 33
Finite-amplitude excursion-cluster count `C_Delta` satisfies pathwise

```math
sup z>u iff C_Delta>=1
```

and

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Occupation-Palm identities for `E[C_Delta]` and `E[C_Delta^2]` use selected-component duration `L` and success indicator `S`, with no derivative/upcrossing count. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`. **NUMERICAL ENDPOINT CERTIFICATE.**

### Step 34
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense paired scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955` and slow envelope `L_s/alpha~>1.10` across `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE:** original high-band conclusion no longer depends on Step-31 empirical `delta(kappa)`. **QUALIFICATION:** inter-node allowance is empirical, not theorem-level continuity.

### Step 35 — current frontier
For normalized spectral amplitude

```math
A_q(w)=|H_x(w)| exp(-w^2q^4/2)/sqrt(I_x(q)),
```

exactly

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

Because the finite-window tail is `|H|^2~(xe^-x)^2/w^2`,

```math
lim_{q->0}||dA_q/dq||_2^2
=2sqrt(pi)(xe^-x)^2/I_x(0),
```

so the common-noise field is `L2`-Lipschitz in `q` through the rough endpoint.

Fast `x=7.16` derivative norm rises only from `~0.00836` at `q=0` to `~0.01493` at `q=0.0767`; `Delta q=0.005` therefore gives pointwise RMS change `~<7.5e-5`. The decision threshold obeys `u'(q)=-2q^3M2(q)rho(q)` and moves by only `~<2.8e-5` per standard Step-34 cell.

Pathwise event sandwich under a sup-norm coupling:

```math
p_q(u_q+delta)-eta <= p(r) <= p_q(u_q-delta)+eta,
```

where `delta=epsilon+|u_q-u_r|` and `eta=P(||z_q-z_r||_inf>epsilon)`.

**REJECTED SHORTCUT:** cluster counts/moments are not pathwise Lipschitz because small perturbations can merge/split lower excursion components, flip maxima across `u`, or amplify Palm weight `1/L`.

**NEGATIVE RESULT:** global Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`: even `epsilon=1e-4` gives a standard bound of at least `4e-4=400 alpha`, versus the Step-34 inter-node budget `6e-10` absolute. The missing theorem must be tail-sensitive to rare successful excursions near `u~5`.

---

## 4. Current frontier

Derive a tail-sensitive buffered-threshold continuity law for successful excursion clusters. The desired scale should follow the rare-event intensity, not an order-one global Gaussian supremum density.

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
- Step-31 empirical `delta(kappa)` is exact or still necessary for the original high-band conclusion;
- Step-32 raw crossing moments stay sharp in the rough limit;
- Step-33/34 Monte Carlo estimates are formal interval arithmetic;
- Step-34 is theorem-level continuous-parameter closure;
- Step-35 process Lipschitz continuity implies cluster-moment Lipschitz continuity;
- generic Gaussian anti-concentration is sharp enough at the rare-event scale;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the successful-excursion cluster representation yield a tail-sensitive buffered-threshold continuity bound near `u~5`, so that the probability of a cluster whose maximum lies in `[u-delta,u+delta]` scales like the rare-event intensity times `delta` rather than the global `O(delta)` Gaussian anti-concentration bound?
