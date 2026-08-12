# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-three logical steps completed. Step 33 replaces raw level-upcrossing multiplicity by a finite-amplitude excursion-cluster count whose event is exactly the false-alarm event. The first two cluster moments have an exact lower-level occupation-Palm representation and remain sharp at representative finite high bandwidths and directly at the rough endpoint. For the original `r=2`, `Lambda=0.895` task, cluster calculations separate fast and slow at `kappa_f=300`, `1000`, and `infinity`. The remaining frontier is continuous-interval numerical/statistical certification from the Step-32 bound near `kappa_f~170` to the endpoint. No universal scalar replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/excursion_cluster_moment_enclosure.py`
6. preceding finite-`u` enclosure: `experiments/01-equal-dstar-different-speed/FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`

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
- **PARTIAL CERTIFICATE** — an analytic inequality settles the stated comparison on a tested parameter range; numerical evaluation may still be non-interval floating point or Monte Carlo.
- **NUMERICAL ENDPOINT CERTIFICATE** — exact inequality plus statistically resolved endpoint moment estimates; not formal interval arithmetic.
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

### Steps 24–28
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity but not physical-boundary monotonicity. Common-white-noise coupling gives the correct rough/smoothed path scale. **INVALIDATED INTERMEDIATE:** `0.8131`; correct RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Two-sided-BES(3) Brownian-extremum zoom-in identifies a positive Gaussian-mollifier `zeta^-1/2` correction under stable-convergence/localization/UI.

### Steps 29–30
Small `chi` introduces Brownian–parabola scales `h_chi=sqrt(2)chi^(1/3)`, `m_chi=2chi^(2/3)` and crossover `mu=sqrt(2)zeta chi^(1/3)`. The difficult fast channel reduces to

```math
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
```

Continuum-extrapolated canonical/full-field calculations agree at percent level. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31
Insert `F(mu)` into the coupled tangent boundary and anchor residual finite-`u` offset to Palm/occupation results. Central bridge peaks near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** original `Lambda=0.895` task has no numerically supported bounded high-band re-entrant pocket. **CONDITIONAL:** finite-`u` offset law remains empirical.

### Step 32
For a smooth finite-band scan,

```math
X_u=1_{\{z(0)\le u\}}N_u^+,
```

and exactly

```math
P_FA=Q(u)+P(X_u\ge1).
```

First-/second-order Rice moments give

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_FA
\le Q(u)+m_1.
}
```

At `Lambda=0.895`, `X=7.04`, the fast upper is below `alpha` and slow lower above `alpha` through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, the bound loses sharpness because slow-channel `lambda2` grows from micro-upcrossing clusters. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

### Step 33 — current frontier
Choose `Delta>0`, set

```math
\boxed{a=u-\Delta,}
```

and decompose `{t:z(t)>a}` into connected components. Count only components whose maximum exceeds `u`; call this `C_Delta`.

Pathwise,

```math
\boxed{\sup z>u\iff C_\Delta\ge1.}
```

For fixed finite amplitude gap, `C_Delta` remains finite on continuous compact paths even as raw level-`u` crossings proliferate.

Moment enclosure:

```math
\boxed{
\frac{E[C_\Delta]^2}{E[C_\Delta^2]}
\le P_FA
\le E[C_\Delta].
}
```

Under the lower-level occupation-Palm law `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`, exact identities are

```math
\boxed{
E[C_\Delta]=\ell Q(a)E_{Q_a}[S/L],
}
```

```math
\boxed{
E[C_\Delta^2]=\ell Q(a)E_{Q_a}[S C_\Delta/L].
}
```

No derivative/upcrossing count appears.

For the original task at `X=7.16`, `Delta=0.15`:

```text
kappa_f    detector    lower/alpha    upper/alpha
300        fast          0.98604        0.98624
300        slow          1.19896        1.19990
1000       fast          0.98417        0.98423
1000       slow          1.21537        1.21725
```

Direct rough endpoint (`50000` paths, grid `~0.001`):

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

**NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE:** the cluster bounds remain sharp at `kappa=infinity` and separate fast/slow at the same physical time. The divergence seen in Step 32 belongs to the micro-upcrossing count, not the physical excursion event.

**OPEN:** exact inequalities are analytic; displayed moments are finite-grid Monte Carlo estimates. The continuous interval `~170 < kappa_f < infinity` is not yet formally/statistically covered pointwise.

---

## 4. Current frontier

Evaluate the excursion-cluster enclosure on an adaptive bandwidth grid, tune `Delta` for numerical efficiency, and control Monte Carlo/grid error strongly enough to close the entire interval from the Step-32 certificate to the rough endpoint.

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
- Step-32 raw crossing moments stay sharp in the rough limit;
- Step-33 Monte Carlo moments are formal interval arithmetic;
- the continuous `170<kappa_f<infinity` interval is certified yet;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the excursion-cluster enclosure be evaluated on an adaptive bandwidth grid with controlled Monte Carlo/grid error and optimized `Delta`, so that the entire interval from `kappa_f~170` to the rough endpoint is closed without the empirical Step-31 boundary fit?
