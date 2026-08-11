# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 18:54 EDT  
**Status:** twenty-three logical steps completed. Step 23 derives the matched rough/smooth high-band scaling for the finite-hard-window timing scan, introduces an exact occupation-time rare-event identity that remains valid when the `kappa=infinity` process is nondifferentiable, and directly anchors the `r=2` infinite-band boundary near `Lambda~0.905`. The old `Lambda=0.895` slice is therefore fast-preferred in the infinite-band limit as well as at Palm-checked finite bandwidths through `kappa_f=300`. A bounded re-entrant pocket at some untested very high finite bandwidth is not rigorously excluded. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but initially have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
- Equal reference scalar `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- For known waveform/full observation,

```math
\rho_\infty^2=\int |P|^2|G|^2/S_n\,df
=\frac1A\int |P|^2D^{*2}(f)\,df.
```

- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite windows can break equivalence because magnitude `D*(f)` discards temporal phase/placement; a causal all-pass construction removes the pure-delay loophole.

### Steps 05–12 — finite-record SNR, detection time, and task boundary

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)],
```

and

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Unknown timing raises a global threshold governed by timing-scan covariance, not digital sample count.

For the controlled family

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

faster SNR acquisition can be offset by a larger search burden.

**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be combined directly with full-template timing bandwidth as one exact statistic.

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in that original family.

### Step 13 — rough hard-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
a_x=\frac{2x^2e^{-2x}}{\eta(x)}.
```

The ideal-white-noise finite hard-window timing scan is locally Brownian-like / nondifferentiable.

**FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover near `ell~49` moved under grid refinement and is invalid.

### Steps 14–17 — genuine finite timing bandwidth and Palm rare events

A genuine information-band limitation removes the cusp; an invertible common low-pass is not necessarily sufficient because optimal whitening can undo it.

Smooth surrogate:

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Exact smooth Palm identity:

```math
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow[1_{\{z(0)\le u\}}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform as `kappa->infinity`.

### Steps 18–19 — one physical electronics bandwidth and a true finite optimum

Use

```math
\kappa_i=\Omega_B\tau_i.
```

With accessible eventual SNR artificially held fixed, the large-r crossover changes from electronics-limited `~1/Omega_B` to detector-limited `~tau_f` and has **no** interior bandwidth optimum.

Remove that SNR renormalization:

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)}.
```

At wide band, SNR loss is `O(1/kappa^2)` while timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists in the Rice objective. Palm validation later confirms that the optimum survives exact rare-event correction.

### Steps 20–21 — finite-r Rice double reversal corrected by Palm

For common physical bandwidth without SNR renormalization, the slower scaled detector has a low-band SNR advantage with

```math
\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r.
```

For

```text
r=2
rho_full=6.2407571
alpha=1e-6
beta=0.90
Lambda=0.895
```

finite-duration Rice gave apparent switches at `25.4898402` and `130.1945883`, i.e. apparent `slow -> fast -> slow`.

Palm correction changes the topology:

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

survives, while the upper Rice switch near `130.19` is **INVALIDATED**. Palm checks at `kappa_f=130`, `160`, and `300` keep fast preferred for `Lambda=0.895`.

Cause: nonuniform Rice micro-upcrossing overcount, especially severe for the shorter slow-detector finite window.

### Step 22 — Palm boundary map and survival of finite optimum

Representative finite-r Palm boundary points:

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

**REFINEMENT:** the high-band slow-preferred region does not disappear. Palm lifts the boundary above the old `Lambda=0.895` slice; larger-`Lambda` tasks remain slow-preferred.

Higher-statistics large-r full-template Palm scan:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** the finite bandwidth optimum survives Palm correction. It is shallow and broad, with `kappa_opt^Palm~50–65` and only `~0.3–0.4%` gain over infinite bandwidth for this calibration.

### Step 23 — matched rough/smooth high-band limit

The exact unregularized finite-window covariance is

```math
\boxed{
R_x(y)=
\frac{(1+y)e^{-y}
-e^{-2x+y}(2x^2-2xy+2x-y+1)}
{\eta(x)},
\qquad 0\le y<x.
}
```

Its local expansion is

```math
\boxed{
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
}
```

with

```math
\boxed{
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
}
```

At threshold `u`, rough and smooth local geometry match through

```math
\boxed{
\chi_x=\frac{a_xu}{\sqrt{b_x}}.
}
```

On scale `q(u)=sqrt(2)/(u sqrt(b_x))`, the tangent variance is

```math
\boxed{
\operatorname{Var}\eta_\chi(t)
=t^2+\sqrt2\chi|t|.
}
```

A generalized Pickands constant `H_mix(chi)` bridges the smooth and rough high-threshold laws, with `H_mix(0)=1/sqrt(pi)` and `H_mix(chi)~sqrt(2)chi` for large `chi`.

**REFINEMENT:** mathematical nondifferentiability at finite `x` does not imply that distinct high excursions are rough-controlled. When `chi<<1`, the cusp mainly creates microscopic recrossings inside a smooth-core excursion.

Because `u~5`, leading high-threshold asymptotics retain percent-level finite-`u` error. To anchor the exact rough limit, define occupation time

```math
V_u=\int_0^\ell 1_{\{z(t)>u\}}dt.
```

If a uniformly selected search time is conditioned to lie above `u`, then

```math
\boxed{
P(\sup z>u)
=\ell Q(u)E_{occ}[1/V_u].
}
```

This identity is exact for continuous paths and remains valid when upcrossing counts diverge.

For the Step-20 `r=2` calibration, direct `kappa=infinity` occupation-time importance sampling gives

```math
\boxed{
\Lambda_{\times}^{kappa=\infty}
\approx0.905\pm0.004,
\qquad
X_\times\approx7.75.
}
```

At representative candidate `X=7.7528`, `Lambda=0.90513`, a `40000`-path run gives

```text
fast: P_FA/alpha = 1.0049 +/-0.0080
slow: P_FA/alpha = 0.9954 +/-0.0094.
```

**REFINEMENT:** the old `Lambda=0.895` slice is fast-preferred again in the direct infinite-band rough limit. The Step-20 second reversal therefore does not reappear asymptotically.

**OPEN:** a bounded re-entrant slow-preferred pocket at some untested very high finite bandwidth is not rigorously excluded because monotonic convergence of the finite-`kappa` boundary has not been proved.

See `HIGH_BAND_MATCHED_ROUGH_SMOOTH_STEP.md` and `numerics/rough_limit_occupation_is.py`.

---

## 3. Current frontier

The high-band limit is now organized by the single transition coordinate `chi_x` and anchored directly at `kappa=infinity` without upcrossing counts.

Remaining question: compute the mixed generalized Pickands constant and finite-threshold correction accurately enough to replace full-process occupation Monte Carlo and determine the high-band boundary deterministically, including whether any bounded re-entrant preference pocket can exist.

---

## 4. Scope boundary

Do not claim:

- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is an exact physical result;
- no bounded high-band re-entrant pocket can exist without a monotonicity proof;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 5. Single natural next question — DO NOT ANSWER YET

> Can the mixed generalized Pickands constant `H_mix(chi)` and its finite-threshold correction be computed accurately enough to turn the Step-23 matched boundary into a deterministic analytic/numerical formula, and thereby prove or exclude any bounded high-band re-entrant preference pocket without further full-process Monte Carlo?
