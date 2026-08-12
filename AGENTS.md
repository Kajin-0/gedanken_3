# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-two logical steps completed. Step 32 derives a direct finite-`u` false-alarm enclosure from first- and second-order Rice moments. For the original `r=2`, `Lambda=0.895` task, this independently certifies fast preference through at least `kappa_f=170` in the tested sequence without the empirical Step-31 finite-threshold bridge. The ordinary second-moment enclosure then loses sharpness as the slow channel develops clustered micro-upcrossings; the next frontier is an excursion-cluster or occupation-time moment variable that survives the rough limit. No universal scalar replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/finite_u_rice_moment_enclosure.py`
6. preceding bridge step: `experiments/01-equal-dstar-different-speed/UNIVERSAL_BRIDGE_BOUNDARY_CLOSURE_STEP.md`

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
- **PARTIAL CERTIFICATE** — an analytic inequality directly settles the stated comparison on a finite tested parameter range; numerical evaluation may still use non-interval floating-point quadrature.
- **INVALIDATED** — previously reported result fails stronger calculation.
- **INVALIDATED INTERMEDIATE** — provisional same-turn value shown wrong; preserve why.
- **INVALIDATED NUMERICAL INTERPRETATION** — generated values remain data but stronger analysis shows they were not estimates of the quantity previously assigned to them.
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

### Steps 22–23
Palm maps the finite-`r` boundary to about `Lambda~0.91` at moderate/high finite bandwidth. Direct occupation-time sampling gives rough endpoint `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

### Steps 24–28
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands/Dieker–Yakir structure is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity. Common-white-noise coupling yields the correct rough/smoothed path scale and correct RMS coefficient `0.8906480701 sqrt(chi/zeta)`; **INVALIDATED INTERMEDIATE:** `0.8131`. Brownian-extremum/two-sided-BES(3) zoom-in identifies a positive Gaussian-mollifier `zeta^-1/2` correction under stable-convergence/localization/UI.

### Steps 29–30
Small `chi` introduces Brownian–parabola width/height `h_chi=sqrt(2)chi^(1/3)`, `m_chi=2chi^(2/3)` and crossover `mu=sqrt(2)zeta chi^(1/3)`. The difficult fast channel reduces to the canonical function

```math
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
```

Continuum-extrapolated canonical/full-field calculations agree at percent level. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31
Insert `F(mu)` into the coupled tangent boundary and anchor residual finite-`u` offset to Palm/occupation results. The central bridge peaks near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** original `Lambda=0.895` task has no numerically supported bounded high-band re-entrant pocket. **CONDITIONAL:** the finite-`u` offset law remains empirical.

### Step 32 — current frontier
For a smooth finite-band scan define

```math
X_u=1_{\{z(0)\le u\}}N_u^+.
```

Then exactly

```math
P_FA=Q(u)+P(X_u\ge1).
```

With `m1=E[X_u]`, `lambda=E[N_u^+]`, and `lambda2=E[N_u^+(N_u^+-1)]`, Cauchy–Schwarz gives

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_FA
\le Q(u)+m_1.
}
```

The required moments are deterministic first-/second-order Rice integrals of the finite-band covariance. At `Lambda=0.895`, common physical time `X=7.04`:

```text
kappa_f   fast upper/alpha   slow lower/alpha
100           0.99737             1.04649
130           0.99861             1.02562
160           0.99961             1.00950
170           0.99990             1.00491
175           1.00004             1.00275
```

**PARTIAL CERTIFICATE:** through at least `kappa_f=170` in the tested sequence, fast is guaranteed feasible while slow is guaranteed infeasible at the same physical time, so fast preference is established without Step-31's empirical bridge.

**NEGATIVE RESULT:** around `kappa_f~175–200` the second-moment enclosure loses sharpness because slow-channel `lambda2` grows rapidly from micro-upcrossing clusters. This is not evidence of a preference reversal; it identifies raw crossing multiplicity as the wrong high-band variable.

---

## 4. Current frontier

Replace raw upcrossing count by an excursion-cluster or occupation-time variable whose moments remain finite and informative as the smooth finite-band process approaches the rough endpoint.

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
- Step-31 empirical `delta(kappa)` is exact;
- Step-32 second-moment crossing enclosure remains sharp in the rough limit;
- Step-32 floating-point quadrature is formal interval arithmetic;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can an excursion-cluster or occupation-time variable provide a finite-`u` upper/lower enclosure that remains sharp as micro-upcrossing multiplicity diverges, thereby extending the Step-32 direct certificate continuously into the rough endpoint?
