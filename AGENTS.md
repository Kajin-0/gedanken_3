# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-eight logical steps completed. Step 28 adapts the Brownian-extremum/two-sided-BES(3) zoom-in mechanism to Gaussian mollification of the tangent field and identifies a strictly positive `zeta^-1/2` generalized-Pickands correction under explicit stable-convergence/localization/uniform-integrability assumptions. The Dieker–Yakir denominator is lower order (`O(zeta^-1)`) under the stationary high-pass coupling, so it cannot cancel the square-root extremum loss. A concrete finite onset bandwidth `K` is still open because a quantitative uniform remainder has not been proved. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/BESSEL_MOLLIFIER_CONTINUITY_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/bessel_mollifier_continuity.py`
6. preceding coupling helper: `experiments/01-equal-dstar-different-speed/numerics/gaussian_mollifier_coupling.py`

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
- **CONDITIONAL THEOREM SKETCH** — theorem structure identified but some technical probability steps (e.g. stable convergence/UI/uniform remainder) remain to be completed.
- **COUNTEREXAMPLE** — construction sufficient to disprove implication.
- **REFINEMENT** — sharpens prior statement without erasing it.
- **NEGATIVE RESULT** — candidate effect tested and absent under stated model.
- **REJECTED SHORTCUT** — tempting inference shown not to answer actual question.
- **FAILED NUMERICAL ESTIMATE** — failed validation; never reuse as result.
- **NUMERICAL VALIDATION** — survived stated cross-checks within scope.
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
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make temporal phase/placement operationally relevant.

Finite-record SNR and task-level detection time are derived consistently. In the controlled `t exp(-t/tau)` family, faster SNR acquisition can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like:

```math
R_x(y)=1-a_x|y|+... .
```

**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible SNR equal gives electronics- and detector-limited regimes but no finite bandwidth optimum.

Holding physical signal/noise fixed instead gives a genuine finite large-r bandwidth optimum; later Palm work confirms a shallow optimum survives beyond Rice.

### Steps 20–21
At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches `25.4898402` and `130.1945883`.

Palm correction preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

The upper Rice switch is **INVALIDATED**. Direct Palm checks at `130,160,300` keep fast preferred for that slice.

### Step 22
Palm boundary map reaches about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above the lifted boundary. The large-r Palm optimum is broad near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Step 23
Finite hard-window rough/smooth matching coordinate:

```math
\chi_x=a_xu/\sqrt{b_x}.
```

At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`.

Because `u~5`, use exact occupation-time importance sampling rather than leading Pickands alone. Direct rough-limit boundary for the `r=2` calibration is

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004.
```

Thus `Lambda=0.895` is fast-preferred at the endpoint.

### Step 24
Finite bandwidth introduces

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}),
```

so finite-band continuation is genuinely two-parameter. **REJECTED SHORTCUT:** `H_mix(chi)` alone is only the `zeta=infinity` endpoint.

### Step 25
The two-parameter generalized Pickands constant has continuous Dieker–Yakir form

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Brown–Resnick Slepian comparison proves

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0.
```

**REFINEMENT:** the local extreme constant cannot oscillate with bandwidth, but this does not by itself prove the physical boundary monotone.

### Step 26
The exact common-time boundary derivative is

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Finite-hard-window SNR recovery is `O(kappa^-1)`. Dieker–Yakir data support positive `H_mix-H ~ C_H/sqrt(zeta)`. Conditional on that law, the `r=2` physical boundary approaches the rough endpoint from above with eventual negative slope.

### Step 27
Common-white-noise Gaussian coupling proves the path-amplitude scale. Kernel:

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact coupled residual variance has maximum

```text
s_*   = 0.7016406021...
v_max = 0.2804576359...
```

and

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum.

A conservative bound gives

```math
0\le H_{mix}-H\le C_\chi\sqrt{\log\zeta/\zeta}.
```

Paired simulations sharply resolve positive square-root scaling.

**NEGATIVE RESULT:** the coupling supplies an upper scale, not a positive lower coefficient.

### Step 28 — current frontier
Define

```math
\sigma_\chi=2^{3/4}\sqrt\chi.
```

Under the Brownian-extremum stable zoom-in at the unique rough-field maximizer `tau_*`,

```math
\frac{M_\infty-W_\infty(\tau_*+\varepsilon s)}
{\sigma_\chi\sqrt\varepsilon}
\Longrightarrow R_*(s),
\qquad \varepsilon=1/\zeta,
```

with `R_*` a two-sided BES(3)-type extremal field.

Gaussian mollification acts through

```math
K_1(s)=\sqrt{2/\pi}\,e^{-2s^2}.
```

Define

```math
\mathcal M_K(R)
=\inf_u\int K_1(v)R(u-v)dv.
```

Then

```math
M_\infty-M_\zeta
=\sigma_\chi\zeta^{-1/2}\mathcal M_K(R_*)
+o_p(\zeta^{-1/2}).
```

Strict kernel positivity plus BES(3) positivity away from its unique zero gives

```math
\boxed{\mathcal M_K(R_*)>0\quad a.s.}
```

The stationary high-pass residual contributes only `O_p(zeta^-1)` to the **integrated** Dieker–Yakir denominator under the stated localization/moment assumptions. Therefore, with uniform integrability,

```math
\boxed{
H_{mix}(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+o(\zeta^{-1/2}),
}
```

where

```math
\boxed{
C_H(\chi)
=2^{3/4}\sqrt\chi\;E[\Psi(W_\infty)\mathcal M_K(R_*)]
>0.
}
```

**REJECTED SHORTCUT:** do not assume the Dieker–Yakir weight and local Bessel functional are independent. Unweighted standard BES simulation gives `E[M_K]~0.87`; paired full-field data imply a smaller effective weighted factor around `0.67–0.70` in the tested cases.

**REFINEMENT:** the positive square-root sign mechanism is now mathematically identified, not merely fitted.

**OPEN:** existing Brownian zoom-in results do not supply a quantitative **uniform remainder** for Gaussian mollification, so a finite exact onset bandwidth `K` is not yet certified.

---

## 4. Current frontier

The remaining problem is quantitative, not structural:

> derive a uniform remainder for the Bessel/Gaussian-mollifier expansion over the detector-relevant `chi` interval, then obtain a concrete finite `K` beyond which `d Lambda_cross/d kappa_f<0` is certified and close the remaining compact bandwidth interval.

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
- the Step-28 weighted Bessel expansion is already a publication-grade proof with quantitative remainder;
- a finite certified onset bandwidth `K` is known;
- `E[M_K]` may replace the weighted coefficient;
- the invalidated `0.8131` value is valid;
- no bounded pre-asymptotic pocket exists yet;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.
