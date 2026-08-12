# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty-four logical steps completed. Step 34 uses the excursion-cluster variable from Step 33 in the natural coordinate `q=kappa_f^(-1/2)` and a common-random-number coupling to the rough endpoint. For the original `r=2`, `Lambda=0.895` task, a dense paired `q` scan plus explicit Monte Carlo/grid/inter-node allowances gives a conservative fast upper envelope `U_f/alpha~<0.99955` and slow lower envelope `L_s/alpha~>1.10` over the adaptively sampled/interpolated tail `170<=kappa_f<=infinity`. This removes the empirical Step-31 `delta(kappa)` fit from the original high-band conclusion. It remains a paired numerical interval closure, not formal interval arithmetic or a theorem-level continuity result. No universal scalar replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/adaptive_cluster_tail_closure.py`
6. preceding cluster step: `experiments/01-equal-dstar-different-speed/EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`

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
- **PAIRED NUMERICAL INTERVAL CLOSURE** — common-random-number differences plus explicit Monte Carlo/grid/mesh allowances cover an adaptively sampled/interpolated parameter interval; not a theorem-level continuity enclosure.
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
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

Continuum-extrapolated canonical/full-field calculations agree at percent level. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31
Insert `F(mu)` into the coupled tangent boundary and anchor residual finite-`u` offset to Palm/occupation results. Central bridge peaks near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** original `Lambda=0.895` task has no numerically supported bounded high-band re-entrant pocket. **CONDITIONAL:** finite-`u` offset law remains empirical.

### Step 32
For a smooth finite-band scan,

```math
X_u=1_{z(0)<=u}N_u^+,
P_FA=Q(u)+P(X_u>=1).
```

First-/second-order Rice moments give

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `Lambda=0.895`, `X=7.04`, fast upper is below `alpha` and slow lower above `alpha` through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, the bound loses sharpness because slow-channel `lambda2` grows from micro-upcrossing clusters. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

### Step 33
Choose `Delta>0`, set `a=u-Delta`, and decompose `{t:z(t)>a}` into connected components. Count only components whose maximum exceeds `u`; call this `C_Delta`.

Pathwise,

```math
sup z>u iff C_Delta>=1.
```

For fixed finite amplitude gap, `C_Delta` remains finite on continuous compact paths even as raw level-`u` crossings proliferate.

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Under lower-level occupation-Palm `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`,

```math
E[C_Delta]=ell Q(a)E_a[S/L],
E[C_Delta^2]=ell Q(a)E_a[S C_Delta/L].
```

At `X=7.16`, `Delta=0.15`, cluster bounds separate fast/slow at `kappa_f=300`, `1000`, and directly at `infinity`. Rough endpoint (`50000` paths, grid `~0.001`):

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

**NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE:** Step-32 divergence belongs to the micro-upcrossing count, not the physical excursion event.

### Step 34 — current frontier
Use

```math
q=kappa_f^(-1/2)
```

so the high-band tail is finite: `0<=q<=0.0767` corresponds to `infinity>=kappa_f>=~170`.

A preliminary gap screen finds a broad low-variance region around `Delta~0.08–0.15`; no unique optimum. Retain `Delta=0.15` conservatively because Step 33 already validated it on the finest rough grid.

For fast `U_f(q)=E[C_Delta(q)]`, generate finite-`q` and endpoint fields from common white noise, common truncated-normal uniforms, and common selected occupation times. Dense `3000`-path scan on `q=0,0.005,...,0.075,0.0767` plus refined midpoints gives

```text
max positive paired correction/alpha ~= +1.9e-8
min paired correction/alpha          ~= -0.00188
max paired SE/alpha                  ~= 0.00106
max adjacent 0.005-node change/alpha ~= 0.000548.
```

Paired rough-grid check relative to a fine `~0.000751` timing grid gives only `~-0.00093 alpha` shift at `~0.00150` and `~-0.00134 alpha` at `~0.00300`.

Using Step-33 endpoint anchor `0.98968 +/-0.00429`, one-sided Gaussian factor `1.645`, grid allowance `0.002`, and inter-node allowance `0.0006` gives

```math
U_f/alpha ~<0.99955<1.
```

Slow absolute `3000`-path scan has minimum central lower ratio `~1.18296` near `kappa_f~170`; even after deliberately conservative MC/grid/inter-node deductions its envelope remains

```math
L_s/alpha ~>1.10>1.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** at common witness time `X=7.16`, the original `Lambda=0.895` task is numerically separated over the adaptively sampled/interpolated tail `170<=kappa_f<=infinity` without the Step-31 empirical `delta(kappa)` fit.

**QUALIFICATION:** the allowances are measured/conservative numerical scales, not formal interval arithmetic, exact confidence sequences, or an analytic continuity modulus for every unsampled `q`.

---

## 4. Current frontier

The original high-band re-entrant-pocket conclusion is now supported by direct finite-`u` cluster enclosures through the rough endpoint without the empirical Step-31 fit. The remaining mathematical task is analytic continuity of the cluster moments in `q`.

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
- Step-34 is a theorem-level continuous-parameter enclosure;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the common-white-noise coupling be converted into an analytic continuity modulus for the excursion-cluster moments as a function of `q=kappa_f^(-1/2)`, replacing the empirical inter-node allowance and turning the Step-34 numerical tail closure into a theorem-level parameter-interval enclosure?
