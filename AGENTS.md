# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-six logical steps completed. Step 26 expands the actual finite-r physical task boundary at high common bandwidth. Conditional on the numerically stable `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)` smoothing law, the `r=2` boundary approaches its direct rough endpoint from above with eventual negative slope. This rules out an asymptotic second reversal but does **not** yet rigorously exclude a bounded pre-asymptotic re-entrant pocket because the square-root smoothing law and uniform remainder are not proved for this field. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/HIGH_BAND_BOUNDARY_DERIVATIVE_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/high_band_boundary_derivative.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, cancellations, counterexamples, negative results, rejected shortcuts, failed numerical estimates, numerical validations, invalidations, asymptotic limits, refinements, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch exact current blob SHA before replacing existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and why they changed;
6. make narrow edits or explicit compact consolidations;
7. update `CURRENT_STATE.md` whenever scientific frontier changes;
8. append or explicitly consolidate `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides chat summaries, memory, and stale recovery notes.**

---

## 2. Epistemic labels

Use where useful:
- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — construction sufficient to disprove implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens prior statement without erasing it.
- **NEGATIVE RESULT** — candidate effect tested and absent under stated model.
- **REJECTED SHORTCUT** — tempting inference shown not to answer actual question.
- **FAILED NUMERICAL ESTIMATE** — failed validation; never reuse as result.
- **NUMERICAL VALIDATION** — survived stated cross-checks within scope.
- **NUMERICAL COUNTEREXAMPLE** — converged numerical construction disproves broader implication within stated approximation/model.
- **INVALIDATED** — previously reported result fails stronger calculation.
- **ASYMPTOTIC** — controlled limiting regime only.
- **NUMERICAL ASYMPTOTIC** — numerically stable limiting law not yet proved.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without separate prior-art audit.

---

## 3. Compact surviving chain

### Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make phase/temporal placement operationally relevant.

Finite-record SNR is `rho_t^2=<s_t,C_t^-1s_t>` and task-level detection time is

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled scaled family, faster SNR acquisition can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like: `R_x(y)=1-a_x|y|+...`.

**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one physical bandwidth `kappa_i=Omega_B tau_i`, artificially forcing accessible SNR equal produces electronics- and detector-limited regimes but no finite bandwidth optimum.

Holding physical signal/noise fixed instead produces a genuine finite large-r bandwidth optimum. Later Palm work confirms a shallow optimum survives beyond Rice.

### Steps 20–21
At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches at `25.4898402` and `130.1945883`.

Palm correction gives

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Palm checks at `130`, `160`, `300` keep fast preferred for `Lambda=0.895`.

### Step 22
Palm boundary map rises to about `Lambda~0.91` at moderate/high finite bandwidth. High-band slow-preferred tasks survive above that lifted boundary. The large-r Palm optimum is broad near `kappa~50–65` and only `~0.3–0.4%` above infinity.

### Step 23
Exact finite-hard-window local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3).
```

Infinite-band matching coordinate `chi_x=a_xu/sqrt(b_x)` gives tangent variance `t^2+sqrt(2)chi|t|`.

At `u~5`, leading asymptotics are insufficient, so use exact occupation-time importance sampling:

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit boundary for the `r=2` calibration is `Lambda_cross^infinity~0.905 +/-0.004`; thus `Lambda=0.895` is fast-preferred at the endpoint.

### Step 24
Finite bandwidth adds a second local coordinate

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The two-parameter tangent variogram connects smooth finite-band and rough infinite-band excursion fields.

**REJECTED SHORTCUT:** `H_mix(chi)` alone cannot control finite-band convergence.

### Step 25
The two-parameter generalized Pickands constant has a continuous Dieker–Yakir representation and an efficient FFT derivative-process construction.

Brown–Resnick Slepian comparison gives exact coordinatewise monotonicity:

```math
\partial_\zeta H\ge0,
\qquad
\partial_\chi H\ge0.
```

**REFINEMENT:** local extreme statistics cannot oscillate with bandwidth, but this alone does not prove the physical boundary monotone.

### Step 26 — current frontier
Let `A_f(X,kappa)` and `A_s(X,kappa)` be admissible physical timing uncertainty for the two channels. The common-time equality gives

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
}
```

For a finite hard window,

```math
\rho(x,\kappa)
=\rho_\infty(x)[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})],
```

so SNR recovery is `O(kappa^-1)`.

Dieker–Yakir data show

```math
H_{mix}(\chi)-H(\chi,\zeta)
\approx C_H(\chi)\zeta^{-1/2},
```

with an exceptionally stable sequence at `chi=0.1` and compatible behavior along the actual endpoint fast/slow `chi` values.

**NUMERICAL ASYMPTOTIC / NOT YET A THEOREM:** conditional on a positive square-root smoothing coefficient,

```math
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+O(\kappa_f^{-1}).
```

For the `r=2` calibration the finite-u tangent surrogate gives `C_Lambda~+2e-2`, hence eventual

```math
\boxed{d\Lambda_\times/d\kappa_f<0.}
```

The high-band boundary therefore approaches the rough endpoint from above in the asymptotic tail.

**REFINEMENT / CONDITIONAL:** any hypothetical additional slow-preferred pocket must be bounded and pre-asymptotic; it cannot persist or recur arbitrarily far into the tail.

**OPEN:** prove the `zeta^-1/2` smoothing law and a uniform remainder, then certify a finite `kappa` beyond which the exact boundary derivative is negative.

---

## 4. Current frontier

Prove or rigorously bound the Gaussian-smoothed Brownian Pickands convergence

```math
H_{mix}(\chi)-H(\chi,\zeta)
\sim C_H(\chi)/\sqrt\zeta
```

with sufficient uniform control in the relevant `chi` range to turn conditional eventual monotonicity into a certified exact-process statement.

---

## 5. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is an exact physical result;
- monotonic `H(chi,zeta)` alone proves monotonic detector preference;
- the square-root smoothing law is already proved for this field;
- no bounded pre-asymptotic pocket exists yet;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)` be derived or bounded rigorously for the Gaussian-smoothed Brownian endpoint field, with a uniform remainder strong enough to certify a finite `kappa` beyond which the exact detector boundary must be monotone decreasing?
