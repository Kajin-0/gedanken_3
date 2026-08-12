# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-one logical steps completed. Step 31 propagates the Step-30 canonical Brownian–parabola crossover through the finite-`r` high-band boundary and anchors only the residual finite-`u` offset to the existing Palm boundary points plus the direct rough endpoint. The central bridge has one shallow maximum near `kappa_f~95`, then decreases toward `Lambda_infinity~0.90513`. For the original `r=2`, `Lambda=0.895` task, the high-band re-entrant slow-preferred pocket is numerically closed. This is not yet a theorem-level interval enclosure because the finite-`u` Palm/occupation discrepancy is still represented empirically. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/UNIVERSAL_BRIDGE_BOUNDARY_CLOSURE_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/universal_bridge_boundary.py`
6. preceding crossover step: `experiments/01-equal-dstar-different-speed/UNIVERSAL_CROSSOVER_FUNCTION_STEP.md`

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
- **NUMERICAL COLLAPSE** — independently parameterized numerical data collapse under a derived scaling variable.
- **NUMERICAL ASYMPTOTIC** — numerically stable limiting law not yet fully proved.
- **NUMERICAL CLOSURE** — multiple independent numerical/asymptotic pieces jointly exclude a candidate behavior for the stated calibration, without constituting a theorem.
- **INVALIDATED** — previously reported result fails stronger calculation.
- **INVALIDATED INTERMEDIATE** — provisional same-turn value shown wrong; preserve why.
- **INVALIDATED NUMERICAL INTERPRETATION** — generated values remain data but a stronger analysis shows they were not estimates of the quantity previously assigned to them.
- **ASYMPTOTIC** — controlled limiting regime only.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. `Universal` is permitted only for the explicitly derived model-reduced canonical crossover function.

---

## 3. Compact surviving chain

### Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make temporal phase/placement operationally relevant. Finite-record SNR and task-level detection time are derived consistently. Faster SNR acquisition can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.  
**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity available; Rice/EC is an upper bound. Finite hard windows make Rice nonuniform as bandwidth grows.

### Steps 18–19
Common physical bandwidth with artificially fixed accessible SNR gives no finite bandwidth optimum. Holding physical signal/noise fixed produces a genuine finite large-`r` optimum; Palm later confirms a shallow optimum survives beyond Rice.

### Steps 20–21
At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches at `25.4898402` and `130.1945883`. Palm preserves only the lower switch `kappa_cross~21.7 +/-0.3`. The upper Rice switch is **INVALIDATED**. Palm checks at `130,160,300` keep fast preferred.

### Step 22
Palm boundary reaches about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above it. Large-`r` Palm optimum broad near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Step 23
Finite hard-window rough/smooth matching plus occupation-time importance sampling gives direct rough endpoint `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

### Step 24
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint.

### Step 25
Generalized Pickands constant has continuous Dieker–Yakir form. Brown–Resnick Slepian comparison proves monotonicity in `chi,zeta`, but not monotonicity of the physical detector boundary.

### Step 26
Exact common-time boundary derivative derived. Finite-hard-window SNR recovery is `O(kappa^-1)`. Positive `H_mix-H~C_H/sqrt(zeta)` implies eventual negative high-band boundary slope for the calibration.

### Step 27
Common-white-noise Gaussian coupling proves the path-amplitude scale and correct coefficient `0.8906480701 sqrt(chi/zeta)`. **INVALIDATED INTERMEDIATE:** `0.8131` used the wrong variance limit. Coupling alone does not prove a positive lower Pickands coefficient.

### Step 28
Brownian-extremum/two-sided-BES(3) zoom-in identifies a positive Gaussian-mollifier `zeta^-1/2` coefficient under stable-convergence/localization/UI. Dieker–Yakir denominator is lower order. Quantitative finite-band remainder remains open.

### Step 29
Small `chi` introduces Brownian–parabola scales

```math
h_chi=sqrt(2) chi^(1/3),
qquad m_chi=2 chi^(2/3),
```

and crossover coordinate `mu=sqrt(2) zeta chi^(1/3)`. At the `r=2` endpoint, `mu_f~0.009776 kappa_f`, `mu_s~0.16139 kappa_f`; slow is already in Bessel tail at `100–300`, fast still in crossover. **REFINEMENT:** old fast `C_H~0.0061` is pre-asymptotic.

### Step 30
Small-`chi` crossover reduces to canonical Brownian-minus-parabola maximum loss

```math
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
```

Representative continuum values: `F(0)~.892`, `.806,.729,.597,.512,.410,.297,.213` at `mu=.5,1,2,3,5,10,20`; `sqrt(mu)F(mu)->~0.98`. Continuum-extrapolated full fast-channel calculations agree at percent level.

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Fast endpoint asymptotic coefficient refines to `C_H~0.0088`.

### Step 31 — current frontier
Insert `F(mu)` into the finite-`u` coupled tangent boundary. Tangent shape tends to `Lambda_tan(infinity)~0.88564`. Anchor the residual finite-`u` correction to Palm points at `kappa_f=60,100,200` and the occupation endpoint `Lambda_inf=0.90513` with minimal relaxation

```math
delta(kappa)=delta_inf+A kappa^{-p},
```

where

```text
delta_inf=0.01949
A~0.18206
p~0.77501.
```

Central bridge:

```text
kappa_f:       60      80      100     130     160     200     300     500     1000    2000    infinity
Lambda:       .90966  .91056  .91066  .91042  .91008  .90964  .90882  .90790  .90695  .90632   .90513
```

Dense interpolation gives one shallow maximum near `kappa_f~94.9`, `Lambda~0.91068`, then a decreasing central bridge for `kappa_f>=100`.

**NUMERICAL CLOSURE for original calibration:** `Lambda=0.895` stays below the entire high-band bridge and rough endpoint; even `0.90513-0.004~0.9011` remains above it. No bounded high-band slow-preferred re-entrant pocket is numerically supported after the validated lower switch.

**CONDITIONAL:** the finite-`u` discrepancy relaxation is empirical. This is not a theorem-level interval enclosure and does not establish boundary topology for other task parameters.

---

## 4. Current frontier

Replace the Step-31 empirical finite-`u` discrepancy anchoring with a direct Palm/occupation correction or certified bound.

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
- monotonic `H(chi,zeta)` alone proves monotonic detector preference;
- raw Step-27 fast values are continuum crossover data;
- Step-31 empirical `delta(kappa)` is exact;
- a theorem-level finite onset bandwidth is known;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the finite-`u` Palm/occupation discrepancy be derived or bounded directly, replacing the empirical `delta_infinity+A kappa^-p` anchoring with a certified interval enclosure for `Lambda_cross(kappa_f)`?
