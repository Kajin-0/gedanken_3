# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-four logical steps completed. Step 24 shows that the finite-band high-excursion problem is genuinely two-parameter: `chi=a_x u/sqrt(b_x)` describes hard-window roughness relative to the smooth excursion core, while `zeta=kappa/(sqrt(2)u sqrt(b_x))` describes finite-band smoothing relative to the excursion scale. The Step-23 `H_mix(chi)` is only the `zeta=infinity` endpoint. No proof yet excludes a bounded high-band re-entrant pocket. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/FINITE_BAND_TANGENT_BRIDGE_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/finite_band_tangent_bridge.py`

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
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. Finite observation can make phase/temporal placement operationally relevant.

Finite-record SNR is

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

and task-level detection time is

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled scaled family, faster SNR acquisition can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR cannot be combined directly with full-template timing bandwidth.

**NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like:

```math
R_x(y)=1-a_x|y|+... .
```

**FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17
A genuine finite timing-information bandwidth removes the cusp. Smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}
```

has controlled correlated-scan numerics.

Exact smooth Palm identity:

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19
With one shared physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible SNR equal produces electronics-limited and detector-limited regimes but **no** interior bandwidth optimum.

Holding physical signal/noise fixed instead gives wide-band SNR loss `O(1/kappa^2)` versus timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists; later Palm validation confirms survival beyond Rice.

### Steps 20–21
At finite `r=2`, fixed physical bandwidth and `Lambda=0.895`, converged Rice produced apparent `slow -> fast -> slow` switches at `25.4898402` and `130.1945883`.

Palm correction gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

for the surviving lower switch and **INVALIDATES** the upper Rice switch. Palm checks at `130`, `160`, and `300` keep fast preferred for `Lambda=0.895`.

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

**REFINEMENT:** high-band slow-preferred tasks survive above the lifted boundary.

Large-r full-template Palm scan has shallow finite optimum:

```text
kappa~50–65: ell_crit^Palm ~0.912
infinity:    ell_crit^Palm ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** finite bandwidth optimum survives Palm correction with only `~0.3–0.4%` gain.

### Step 23
Exact finite-hard-window local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

where

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

Infinite-band rough/smooth high-excursion coordinate:

```math
\boxed{\chi_x=a_xu/\sqrt{b_x}}.
```

On `q(u)=sqrt(2)/(u sqrt(b_x))`, the `kappa=infinity` tangent variance is

```math
\operatorname{Var}\eta_\chi(t)=t^2+\sqrt2\chi|t|.
```

A generalized Pickands constant `H_mix(chi)` bridges smooth and rough endpoint laws.

At `u~5`, leading high-threshold asymptotics are not percent-level accurate enough. Exact occupation-time rare-event identity:

```math
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
```

Direct `kappa=infinity` calculation for the `r=2` calibration gives

```math
\Lambda_{cross}^{kappa=\infty}\approx0.905\pm0.004,
\qquad X_{cross}\approx7.75.
```

Thus `Lambda=0.895` is fast-preferred again at the direct rough endpoint.

### Step 24 — current frontier
The Step-23 one-parameter endpoint theory is insufficient for finite-band continuation.

The universal Gaussian smoothing integral for the endpoint `1/nu^2` tail is

```math
\boxed{
J(y,\kappa)=
\frac{\pi|y|}{2}\operatorname{erf}(\kappa|y|/2)
+\frac{\sqrt\pi}{\kappa}[e^{-(\kappa y)^2/4}-1].
}
```

Matched finite-band local covariance:

```math
1-R_{x,\kappa}(y)
\sim\frac{b_x}{2}y^2+\frac{2a_x}{\pi}J(y,\kappa).
```

This reproduces

```math
-R_{x,\kappa}''(0)
\sim b_x+\frac{a_x\kappa}{\sqrt\pi}.
```

Finite bandwidth introduces a second high-excursion coordinate

```math
\boxed{
\zeta_x=\frac{\kappa}{\sqrt2u\sqrt{b_x}}.
}
```

Together with `chi`, the tangent variogram is

```math
\boxed{
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2+\sqrt2\chi\Bigg[
|t|\operatorname{erf}(\zeta|t|)\\
&\qquad+\frac{e^{-\zeta^2t^2}-1}{\sqrt\pi\zeta}
\Bigg].
\end{aligned}
}
```

`zeta->infinity` recovers Step 23; `zeta->0` gives the smooth finite-band quadratic tangent.

Define the two-parameter generalized Pickands constant `H(chi,zeta)` from this stationary-increment tangent field, with

```math
\boxed{H(chi,infinity)=H_mix(chi).}
```

**REJECTED SHORTCUT / REFINEMENT:** `H_mix(chi)` alone cannot determine finite-band convergence or rule out a bounded re-entrant pocket. The correct local object is at least `H(chi,zeta)` plus finite-threshold control.

---

## 4. Current frontier

Evaluate `H(chi,zeta)` efficiently—preferably through a generalized Dieker–Yakir representation—and determine whether its dependence on `zeta` plus a controlled finite-`u` correction yields monotonic high-band convergence or can support a bounded re-entrant preference pocket.

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
- no bounded high-band re-entrant pocket can exist without a monotonicity/error proof;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the two-parameter generalized Pickands constant `H(chi,zeta)` be evaluated efficiently using a Dieker–Yakir representation, and does its dependence on `zeta` have enough monotonic structure to control the finite-band approach and rule out a bounded re-entrant preference pocket?
