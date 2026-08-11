# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-five logical steps completed. Step 25 proves that the finite-band two-parameter generalized Pickands constant `H(chi,zeta)` has a continuous Dieker–Yakir representation and is nondecreasing in both `chi` and `zeta`. A practical FFT estimator validates the monotonic trend. This rules out oscillation of the local extreme constant as the source of any remaining high-band re-entrant detector-preference pocket, but does not yet prove the full detector boundary monotone. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/TWO_PARAMETER_PICKANDS_DY_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/two_parameter_pickands_dy.py`

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
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without separate prior-art audit.

---

## 3. Compact surviving chain

### Steps 01–12
Equal scalar `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make phase/temporal placement operationally relevant.

Finite-record SNR:

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Task-level detection time:

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled scaled family, faster SNR acquisition can be offset by unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like:

```math
R_x(y)=1-a_x|y|+... .
```

**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm sampling makes `alpha=1e-6` practical. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one shared physical bandwidth `kappa_i=Omega_B tau_i`, artificially forcing accessible SNR equal produces electronics-limited and detector-limited regimes but no finite bandwidth optimum.

Holding physical signal/noise fixed instead gives wide-band SNR loss `O(1/kappa^2)` versus timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists; Palm validation later confirms survival beyond Rice.

### Steps 20–21
At finite `r=2`, fixed physical bandwidth and `Lambda=0.895`, converged Rice produced apparent switches at `25.4898402` and `130.1945883`.

Palm correction gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Palm checks at `130`, `160`, `300` keep fast preferred for `Lambda=0.895`.

### Step 22
Palm boundary map:

```text
kappa_f     Lambda_cross^Palm
~10         ~0.794
~20         ~0.891
21.7         0.895
30          ~0.9052
60          ~0.9098
100         ~0.9103
200         ~0.9099
```

High-band slow-preferred tasks survive above the lifted boundary.

Large-r Palm scan has a shallow finite optimum near `kappa~50–65`, only `~0.3–0.4%` above the infinite-band boundary.

### Step 23
Exact local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3).
```

Infinite-band matching coordinate:

```math
\chi_x=a_xu/\sqrt{b_x}.
```

On the high-excursion scale, tangent variance is `t^2+sqrt(2)chi|t|`.

At `u~5`, leading asymptotics are not accurate enough. Exact occupation-time identity:

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct rough-limit boundary for the `r=2` calibration:

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004.
```

Thus `Lambda=0.895` is fast-preferred at the rough endpoint.

### Step 24
Finite bandwidth introduces a second coordinate

```math
\zeta_x=\kappa/(\sqrt2u\sqrt{b_x}).
```

The exact two-parameter tangent variogram is

```math
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2+\sqrt2\chi\Big[
|t|\operatorname{erf}(\zeta|t|)\\
&\qquad+(e^{-\zeta^2t^2}-1)/(\sqrt\pi\zeta)
\Big].
\end{aligned}
```

**REJECTED SHORTCUT:** the one-parameter `H_mix(chi)` is only the `zeta=infinity` endpoint.

### Step 25 — current frontier
For

```math
W_{\chi,\zeta}(t)=\sqrt2\eta_{\chi,\zeta}(t)-g_{\chi,\zeta}(t),
```

the generalized continuous Dieker–Yakir representation is

```math
\boxed{
\mathcal H(\chi,\zeta)
=E\left[\frac{\sup_t e^{W(t)}}{\int_{\mathbb R}e^{W(t)}dt}\right].
}
```

Efficient decomposition:

```math
\eta_{\chi,\zeta}(t)
=Zt+2^{1/4}\sqrt\chi B_\zeta(t),
```

with stationary derivative covariance

```math
E[B_\zeta'(0)B_\zeta'(t)]
=\frac{\zeta}{\sqrt\pi}e^{-\zeta^2t^2}.
```

Therefore `H` is practical to estimate by FFT derivative synthesis plus integration.

Exact variogram derivatives and Brown–Resnick Slepian comparison give

```math
\boxed{
\partial_\zeta\mathcal H\ge0,
\qquad
\partial_\chi\mathcal H\ge0.
}
```

and

```math
\boxed{
1/\sqrt\pi\le H(\chi,\zeta)\le H_{mix}(\chi).
}
```

Representative `chi=0.1` estimates:

```text
zeta:      1       3       9       19      40      infinity
H_hat:   .58683  .62310  .67671  .70538  .72422   .76698
```

**REFINEMENT:** the local extreme constant cannot oscillate with bandwidth. Any re-entrant preference pocket must arise from the coupled detector trajectory through SNR, threshold, decision time, `chi`, and `zeta`.

**REJECTED SHORTCUT:** monotonic `H` does not automatically make `Lambda_cross(kappa_f)` monotone.

---

## 4. Current frontier

Insert deterministic/low-variance Dieker–Yakir estimates into the finite-threshold boundary and expand along the actual fast and slow trajectories to determine the sign of the high-band physical boundary derivative.

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
- `H_mix(chi)` alone controls finite-band convergence;
- monotonic `H(chi,zeta)` proves monotonic detector preference;
- no bounded high-band re-entrant pocket exists yet;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the deterministic Dieker–Yakir estimates of `H(chi,zeta)` be inserted into the finite-`u` boundary equation and asymptotically expanded along the actual fast and slow detector trajectories to determine the sign of `d Lambda_cross / d kappa_f` at high bandwidth?
