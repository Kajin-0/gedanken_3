# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-nine logical steps completed. Step 29 shows that the Step-28 fixed-`chi` Bessel/Gaussian-mollifier asymptotic is not quantitatively uniform in raw `zeta` when `chi` is small. The mixed smooth/rough endpoint has Brownian-minus-parabola width `h_chi=sqrt(2) chi^(1/3)` and height `2 chi^(2/3)`, so the correct crossover coordinate is `mu=sqrt(2) zeta chi^(1/3)`. Paired data collapse strongly in these variables. For the `r=2` endpoint, the slow detector is already in the large-`mu` Bessel regime at the mapped high bandwidths, while the tiny-`chi` fast detector remains in crossover through `kappa_f=300`. No finite certified onset bandwidth, universal replacement metric, or novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/BROWNIAN_PARABOLA_DOUBLE_SCALING_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/double_scaling_crossover.py`
6. preceding asymptotic step: `experiments/01-equal-dstar-different-speed/BESSEL_MOLLIFIER_CONTINUITY_STEP.md`

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
- **ASYMPTOTIC** — controlled limiting regime only.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Compact surviving chain

### Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make temporal phase/placement operationally relevant. Finite-record SNR and task-level detection time are derived consistently. In the controlled `t exp(-t/tau)` family, faster SNR acquisition can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.  
**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like: `R_x(y)=1-a_x|y|+...`.  
**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible SNR equal gives electronics- and detector-limited regimes but no finite bandwidth optimum. Holding physical signal/noise fixed instead gives a genuine finite large-`r` bandwidth optimum; later Palm work confirms a shallow optimum survives beyond Rice.

### Steps 20–21
At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches `25.4898402` and `130.1945883`. Palm correction preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

The upper Rice switch is **INVALIDATED**. Palm checks at `130,160,300` keep fast preferred.

### Step 22
Palm boundary map reaches about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above the lifted boundary. Large-`r` Palm optimum is broad near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Step 23
Finite hard-window rough/smooth matching coordinate `chi_x=a_xu/sqrt(b_x)`. At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`. Exact occupation-time importance sampling handles `u~5`. Direct rough-limit boundary is `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` is fast-preferred at the endpoint.

### Step 24
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the `zeta=infinity` endpoint.

### Step 25
The two-parameter generalized Pickands constant has continuous Dieker–Yakir form

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Brown–Resnick Slepian comparison proves `partial_zeta H>=0`, `partial_chi H>=0`. The local extreme constant cannot oscillate with bandwidth, but this alone does not prove the physical boundary monotone.

### Step 26
The exact common-time boundary derivative is

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Finite-hard-window SNR recovery is `O(kappa^-1)`. Paired Dieker–Yakir data supported positive `H_mix-H~C_H/sqrt(zeta)`. Conditional on that law, the `r=2` physical boundary approaches the rough endpoint from above with eventual negative slope.

### Step 27
Common-white-noise Gaussian coupling gives

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum. A conservative fixed-window bound gives `0<=H_mix-H<=C_chi sqrt(log zeta/zeta)`. Paired simulations sharply resolve positive square-root scaling, but coupling alone supplies no positive lower coefficient.

### Step 28
Brownian-extremum/two-sided-BES(3) zoom-in plus Gaussian mollification gives, under stable convergence/localization/UI,

```math
H_mix(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+o(\zeta^{-1/2}),
```

with

```math
C_H(\chi)=2^{3/4}\sqrt\chi E[\Psi(W_\infty)M_K(R_*)]>0.
```

The Dieker–Yakir denominator is lower order. **REJECTED SHORTCUT:** do not factor the weighted expectation without an independence theorem. Existing zoom-in results do not supply a quantitative uniform remainder / finite exact onset bandwidth.

### Step 29 — current frontier
The Step-28 fixed-`chi` asymptotic is singular for small `chi`. Brownian fluctuation versus the smooth parabolic maximum gives

```math
\boxed{h_\chi=\sqrt2\chi^{1/3}},
\qquad
\boxed{m_\chi=2\chi^{2/3}}.
```

Gaussian smoothing is therefore controlled by

```math
\boxed{\mu=\zeta h_\chi=\sqrt2\zeta\chi^{1/3}}.
```

Natural double-scaling form:

```math
H_mix(\chi)-H(\chi,\zeta)
=\chi^{2/3}F(\mu)+o(\chi^{2/3}),
```

with `F(mu)~A_K mu^-1/2` for large `mu`, recovering Step 28.

**NUMERICAL COLLAPSE:** Step-27 paired values collapse strongly under `(mu, Delta H/chi^(2/3))`. Slow-endpoint and `chi=0.1` data have `sqrt(mu)F_emp~1` by `mu~10–50`; fast-endpoint values at `mu~1.4–5.5` remain in crossover.

At the `r=2` endpoint,

```math
\boxed{\mu_f\approx0.009776\kappa_f},
\qquad
\boxed{\mu_s\approx0.16139\kappa_f}.
```

Therefore at `kappa_f=100,200,300`, the fast channel has `mu_f~0.98,1.96,2.93`, while the slow has `mu_s~16.1,32.3,48.4`. The slow channel is already in the Bessel tail; the fast remains in the Brownian-parabola crossover.

**REFINEMENT:** the Step-26 fast `C_H~0.006` from `zeta<=80` is a pre-asymptotic effective coefficient, not a clean fixed-`chi` endpoint coefficient. This refines coefficient magnitude/onset, not the eventual asymptotic sign.

---

## 4. Current frontier

Compute the one-dimensional Brownian-minus-parabola/Gaussian-mollifier crossover function

```math
\boxed{F(\mu)}
```

directly, rather than simulating the full detector field, and determine whether it supplies a uniform crossover-to-Bessel envelope strong enough to close the remaining high-band interval.

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
- Step-26 fast `C_H~0.006` is the final asymptotic coefficient;
- a finite certified onset bandwidth is known;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can `F(mu)` be computed directly from the universal Brownian-minus-parabola local process, without full detector simulation, and can it provide a one-dimensional envelope from crossover through the Bessel tail strong enough to close the remaining high-band interval?
