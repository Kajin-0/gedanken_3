# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-seven logical steps completed. Step 27 derives the exact common-white-noise coupling scale between the finite-band Gaussian-smoothed tangent field and the rough Brownian endpoint. It proves an `O(sqrt(chi/zeta))` pointwise path perturbation, gives a conservative `O(sqrt(log zeta/zeta))` Pickands convergence envelope, and uses a paired Dieker–Yakir estimator to sharply validate a positive `1/sqrt(zeta)` correction along the actual fast/slow endpoint trajectories. The missing theorem is now specifically a positive Brownian-extremum continuity correction for Gaussian mollification; no exact finite onset bandwidth `K` is certified yet. No universal replacement metric and no novelty claim.

Read first:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/GAUSSIAN_MOLLIFIER_COUPLING_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/gaussian_mollifier_coupling.py`

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
- **INVALIDATED INTERMEDIATE** — same-turn or provisional value shown wrong before finalizing the step; preserve why.
- **ASYMPTOTIC** — controlled limiting regime only.
- **NUMERICAL ASYMPTOTIC** — numerically stable limiting law not yet proved.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Compact surviving chain

### Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal performance. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. Finite observation can make phase/temporal placement operationally relevant.

Finite-record SNR is

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Task-level detection time is

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
At finite `r=2`, `Lambda=0.895`, converged Rice produced apparent switches `25.4898402` and `130.1945883`.

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

### Step 26
The exact common-time physical boundary derivative is

```math
\frac{d\Lambda_\times}{d\kappa}
=\frac{A_{f,X}A_{s,\kappa}-A_{s,X}A_{f,\kappa}}
{A_{f,X}-A_{s,X}}.
```

For a finite hard window,

```math
\rho(x,\kappa)
=\rho_\infty(x)[1-a_x/(\sqrt\pi\kappa)+o(\kappa^{-1})],
```

so SNR recovery is `O(kappa^-1)`.

Dieker–Yakir data support

```math
H_{mix}(\chi)-H(\chi,\zeta)
\approx C_H(\chi)\zeta^{-1/2},
```

with positive coefficient. Conditional on that law, the `r=2` physical boundary has an eventual negative slope and approaches the direct rough endpoint from above.

### Step 27 — current frontier
Construct the rough Brownian endpoint and finite-band smoothed endpoint on one white-noise field. The smoothing multiplier is

```math
e^{-\omega^2/(8\zeta^2)}
```

and the time-domain kernel is

```math
K_\zeta(t)=\sqrt2\zeta/\sqrt\pi\;e^{-2\zeta^2t^2}.
```

Exact deterministic gap:

```math
0\le|t|-F_\zeta(t)\le1/(\sqrt\pi\zeta).
```

Exact coupled random difference:

```math
\operatorname{Var}[B_\infty(t)-B_\zeta(t)]
=\zeta^{-1}v(\zeta|t|).
```

The explicit profile has

```text
s_*   = 0.7016406021...
v_max = 0.2804576359...
```

and therefore

```math
\boxed{
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
}
```

**INVALIDATED INTERMEDIATE:** `0.8131 sqrt(chi/zeta)` used the large-lag variance rather than the true variance supremum and must not be propagated.

On fixed truncation intervals the coupling plus Gaussian maximal bounds gives

```math
0\le H_{mix}(\chi)-H(\chi,\zeta)
\le C_\chi\sqrt{\log\zeta/\zeta}.
```

A paired common-random-number Dieker–Yakir estimator sharply resolves the small correction. Representative values of `sqrt(zeta)[H_mix-H]`:

```text
chi_fast~1.14e-4:  0.00579, 0.00651, 0.00681  at zeta=20,40,80
chi_slow~0.0645:   0.2037,  0.2072,  0.2116   at zeta=20,40,80
chi=0.1:           0.2757,  0.2760,  0.2783   at zeta=20,40,80
```

with paired Monte-Carlo errors much smaller than the differences themselves.

**NUMERICAL VALIDATION / NUMERICAL ASYMPTOTIC:** the positive square-root correction is strongly supported and now has an exact Brownian path-amplitude origin.

**NEGATIVE RESULT:** the coupling is an upper-scale argument and does not prove a positive lower asymptotic coefficient. Thus there is still no theorem-level finite `K` beyond which the exact detector boundary derivative is certified negative.

Classical Brownian grid-discretization results rigorously establish `sqrt(delta)` extreme-value continuity corrections and a two-sided-Bessel zoom-in field around extrema, but Gaussian convolution is a different approximation and requires its own continuity-correction argument.

---

## 4. Current frontier

Adapt the Brownian-extremum zoom-in / two-sided-Bessel machinery to **Gaussian mollification** of the Dieker–Yakir spectral field. The desired result is a positive kernel-specific limit

```math
\sqrt\zeta[H_{mix}(\chi)-H(\chi,\zeta)]\to C_H(\chi)>0
```

with a uniform remainder over the relevant fast/slow `chi` range. That would finally convert the conditional Step-26 eventual negative slope into a certified exact-process statement.

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
- the positive Gaussian-mollifier `1/sqrt(zeta)` coefficient is already proved;
- the invalidated `0.8131` coupling coefficient is valid;
- no bounded pre-asymptotic pocket exists yet;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 6. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the Brownian-extremum zoom-in / two-sided-Bessel theorem be adapted from grid discretization to Gaussian mollification of the Dieker–Yakir spectral field, yielding a positive kernel-specific continuity-correction constant `C_H(chi)` and finally converting the Step-26 eventual negative slope into a theorem with a finite certified onset bandwidth?
