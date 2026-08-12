# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Thirty logical steps completed. Step 30 derives a detector-independent small-`chi` Brownian-minus-parabola/Gaussian-mollifier crossover function `F(mu)=(2/sqrt(pi))E[M_inf-M_mu]`, validates it against continuum-extrapolated full fast-channel Dieker–Yakir calculations, and identifies a grid-resolution bias in the raw Step-27 tiny-`chi` fast points. The universal bridge refines the fast Bessel-tail coefficient to about `C_H~0.0088` rather than the pre-asymptotic `~0.0061` used in Step 26. The next task is to propagate this one-dimensional bridge through the coupled finite-`r` boundary and test whether any bounded high-band re-entrant pocket remains. No finite certified onset bandwidth, universal replacement metric, or novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/UNIVERSAL_CROSSOVER_FUNCTION_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/universal_crossover_function.py`
6. preceding scaling step: `experiments/01-equal-dstar-different-speed/BROWNIAN_PARABOLA_DOUBLE_SCALING_STEP.md`

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
- **INVALIDATED** — previously reported result fails stronger calculation.
- **INVALIDATED INTERMEDIATE** — provisional same-turn value shown wrong; preserve why.
- **INVALIDATED NUMERICAL INTERPRETATION** — numerical values remain generated data but a stronger analysis shows they were not estimates of the quantity previously assigned to them.
- **ASYMPTOTIC** — controlled limiting regime only.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit. The word `universal` is allowed only when referring to the explicitly derived **model-reduced canonical crossover function**, not as a novelty or hardware claim.

---

## 3. Compact surviving chain

### Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make temporal phase/placement operationally relevant. Finite-record SNR and task-level detection time are derived consistently. In the controlled `t exp(-t/tau)` family, faster SNR acquisition can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.  
**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed instead gives a genuine finite large-`r` bandwidth optimum; later Palm work confirms a shallow optimum survives beyond Rice.

### Steps 20–21
At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch `kappa_cross~21.7 +/-0.3`. The upper Rice switch is **INVALIDATED**. Palm checks at `130,160,300` keep fast preferred.

### Step 22
Palm boundary reaches about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above it. Large-`r` Palm optimum is broad near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Step 23
Finite hard-window rough/smooth matching gives `chi_x=a_xu/sqrt(b_x)`. Exact occupation-time importance sampling handles `u~5`. Direct rough-limit boundary is `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` is fast-preferred at the endpoint.

### Step 24
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the `zeta=infinity` endpoint.

### Step 25
Generalized Pickands constant has continuous Dieker–Yakir form. Brown–Resnick Slepian comparison proves coordinatewise monotonicity in `chi` and `zeta`. This does not by itself prove the detector boundary monotone.

### Step 26
Exact common-time physical boundary derivative derived. Finite-hard-window SNR recovery is `O(kappa^-1)`. Positive `H_mix-H~C_H/sqrt(zeta)` would force eventual negative high-band boundary slope for the `r=2` calibration.

### Step 27
Common-white-noise Gaussian coupling proves the path-amplitude scale and gives

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum. Coupling alone supplies no positive lower coefficient.

### Step 28
Brownian-extremum / two-sided-BES(3) zoom-in identifies a positive Gaussian-mollifier `zeta^-1/2` coefficient under stable convergence/localization/UI. The Dieker–Yakir denominator is lower order. Quantitative finite-band remainder remains open.

### Step 29
Small `chi` is singular. Natural Brownian-parabola width/height:

```math
h_chi=sqrt(2) chi^(1/3),
qquad
m_chi=2 chi^(2/3).
```

Correct crossover variable:

```math
mu=sqrt(2) zeta chi^(1/3).
```

At the `r=2` endpoint,

```math
mu_f~0.009776 kappa_f,
qquad
mu_s~0.16139 kappa_f.
```

Slow is already in Bessel tail around `kappa_f=100–300`; fast is still in crossover. **REFINEMENT:** Step-26 fast `C_H~0.0061` is pre-asymptotic.

### Step 30 — current frontier
The small-`chi` crossover reduces to the canonical Brownian-minus-parabola problem

```math
Y_inf(s)=B(s)-s^2,
```

with finite `mu` obtained by Gaussian filtering the white derivative of `B` with amplitude transfer `exp[-q^2/(8 mu^2)]`.

Let

```math
M_inf=sup_s[B(s)-s^2],
qquad
M_mu=sup_s[B_mu(s)-s^2].
```

Then

```math
\boxed{
F(mu)=\frac{2}{\sqrt\pi}E[M_inf-M_mu].
}
```

Representative continuum-extrapolated values:

```text
mu:       0     .5     1      2      3      5      10     20
F(mu):  .892   .806   .729   .597   .512   .410   .297   .213
```

and `sqrt(mu)F(mu)->A_K~0.98` in the Bessel tail.

**NUMERICAL VALIDATION:** nested-grid full fast-channel Dieker–Yakir gaps agree with the canonical function at the percent level at `mu=1.37,2.74,5.49`.

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by under-resolving the rough Brownian maximum; do not reuse them as continuum crossover values. Step 29's scaling variable remains correct.

Effective bridge:

```math
C_H,eff=2^{-1/4}\sqrt\chi\,\sqrt\mu F(mu).
```

For the fast endpoint, `C_H(infinity)~0.0088`; using that in the same Step-26 surrogate moves illustrative `C_Lambda` from `~0.020` to `~0.032`, preserving and strengthening the positive asymptotic coefficient sign.

---

## 4. Current frontier

Insert the canonical `F(mu)` bridge into the coupled finite-`r` boundary and test whether the corrected boundary is monotone from the existing Palm high-band map into the rough endpoint.

---

## 5. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is exact;
- monotonic `H(chi,zeta)` alone proves monotonic detector preference;
- Step-28 is quantitatively uniform in `chi` at moderate `zeta`;
- raw Step-27 fast values are continuum crossover data;
- Step-26 fast `C_H~0.0061` is final asymptotic;
- the canonical crossover table is an exact analytic evaluation;
- a finite certified onset bandwidth is known;
- no bounded pre-asymptotic pocket exists yet;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> If the universal `F(mu)` bridge is inserted into the coupled finite-`r` boundary equation, does the corrected boundary remain monotone from the mapped Palm high-band region into the rough endpoint, thereby eliminating the last plausible bounded re-entrant pocket without full-process Monte Carlo at every bandwidth?
