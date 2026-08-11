# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 19:21 EDT  
**Status:** twenty-four logical steps completed. Step 24 shows that the Step-23 one-parameter mixed Pickands constant is only the `kappa=infinity` endpoint theory. Finite information bandwidth introduces a second high-excursion coordinate `zeta=kappa/(sqrt(2) u sqrt(b_x))`. The Gaussian smoothing of the hard-window `1/nu^2` endpoint tail is integrated exactly, yielding a two-parameter tangent variogram and generalized Pickands object `H(chi,zeta)`. No proof yet excludes a bounded high-band re-entrant pocket. No universal replacement metric and no novelty claim.

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

### Steps 01–04 — limits of scalar and magnitude-only `D*`
- Equal reference scalar `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- For known waveform/full observation,

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int |P|^2D^{*2}(f)\,df.
```

- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite windows can break equivalence because magnitude `D*(f)` discards phase/temporal placement; a causal all-pass construction removes the pure-delay loophole.

### Steps 05–12 — finite-record SNR and task-level timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)],
```

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Unknown timing raises a global threshold governed by timing-scan covariance, not digital sample count.

Controlled family:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster SNR acquisition can be offset by larger unknown-time search burden.

**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be combined directly with full-template timing bandwidth as one exact statistic.

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in that original scaled family.

### Step 13 — rough hard-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
a_x=\frac{2x^2e^{-2x}}{\eta(x)}.
```

The ideal-white-noise finite hard-window timing scan is locally Brownian-like / nondifferentiable.

**FAILED NUMERICAL ESTIMATE:** Step-13 rough-grid crossover near `ell~49` moved under grid refinement and is invalid.

### Steps 14–17 — genuine timing-information bandwidth and Palm rare events

An invertible common low-pass is not necessarily a true information-band limit because optimal whitening can undo it.

Use the smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the covariance cusp.

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

### Steps 18–19 — one physical bandwidth and a genuine finite optimum

Use

```math
\kappa_i=\Omega_B\tau_i.
```

With accessible eventual SNR artificially held fixed, the large-r crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f` and has **no** interior bandwidth optimum.

Remove SNR renormalization:

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)}.
```

At wide band, SNR loss is `O(1/kappa^2)` while timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-r bandwidth optimum exists in the Rice objective. Later Palm validation confirms that a shallow finite optimum survives exact rare-event correction.

### Steps 20–21 — finite-r Rice double reversal corrected by Palm

For common physical bandwidth without SNR renormalization, the slower scaled detector has a narrow-band SNR advantage with

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

finite-duration Rice gave apparent switches `25.4898402` and `130.1945883`, i.e. apparent `slow -> fast -> slow`.

Palm correction changes the topology:

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3}
```

survives, while the upper Rice switch near `130.19` is **INVALIDATED**. Palm checks at `kappa_f=130`, `160`, and `300` keep fast preferred for `Lambda=0.895`.

Cause: nonuniform Rice micro-upcrossing overcount, especially severe for the shorter slow-detector finite window.

### Step 22 — Palm boundary map and survival of the finite optimum

Representative finite-r Palm boundary:

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

**REFINEMENT:** high-band slow-preferred tasks survive above a lifted boundary. Palm removes the old `Lambda=0.895` second crossing but does not erase the slow-preferred side of task space.

Large-r full-template Palm scan:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

**NUMERICAL VALIDATION / CONDITIONAL:** the finite bandwidth optimum survives Palm correction, broad near `kappa~50–65` with only `~0.3–0.4%` gain over infinite bandwidth for this calibration.

### Step 23 — matched infinite-band rough/smooth limit

Exact finite-hard-window covariance:

```math
R_x(y)=
\frac{(1+y)e^{-y}-e^{-2x+y}(2x^2-2xy+2x-y+1)}{\eta(x)}.
```

Local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
```

with

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
\qquad
b_x=\frac{1+e^{-2x}(2x^2-2x-1)}{\eta(x)}.
```

At threshold `u`, infinite-band rough/smooth excursion geometry is organized by

```math
\boxed{\chi_x=\frac{a_xu}{\sqrt{b_x}}}.
```

On `q(u)=sqrt(2)/(u sqrt(b_x))`, the `kappa=infinity` tangent variance is

```math
\operatorname{Var}\eta_\chi(t)
=t^2+\sqrt2\chi|t|.
```

A generalized Pickands constant `H_mix(chi)` bridges the smooth and rough high-threshold limits.

Because `u~5`, leading asymptotics retain percent-level finite-threshold error. Step 23 therefore introduces exact occupation-time importance sampling:

```math
V_u=\int_0^\ell1_{z(t)>u}dt,
```

```math
\boxed{
P(\sup z>u)=\ell Q(u)E_{occ}[1/V_u].
}
```

This remains valid in the nondifferentiable rough limit.

Direct `kappa=infinity` calculation for the `r=2` calibration gives

```math
\boxed{
\Lambda_{cross}^{kappa=\infty}\approx0.905\pm0.004,
\qquad X_{cross}\approx7.75.
}
```

Thus `Lambda=0.895` is fast-preferred in the direct infinite-band rough limit as well as at checked finite high bandwidths.

**OPEN:** a bounded re-entrant slow-preferred pocket at some untested very high finite bandwidth is not rigorously excluded.

### Step 24 — finite-band tangent bridge requires a second coordinate

The hard endpoint produces a universal `1/nu^2` timing-spectrum tail. Under Gaussian information weighting, define

```math
J(y,\kappa)
=\int_0^\infty
\frac{1-\cos(\nu y)}{\nu^2}
 e^{-(\nu/\kappa)^2}d\nu.
```

It has the exact closed form

```math
\boxed{
J(y,\kappa)
=\frac{\pi|y|}{2}
\operatorname{erf}\!\left(\frac{\kappa|y|}{2}\right)
+\frac{\sqrt\pi}{\kappa}
\left[e^{-(\kappa y)^2/4}-1\right].
}
```

Hence the matched local finite-band covariance obeys

```math
1-R_{x,\kappa}(y)
\sim\frac{b_x}{2}y^2+\frac{2a_x}{\pi}J(y,\kappa).
```

For `kappa|y|<<1`, this gives

```math
-R_{x,\kappa}''(0)
\sim b_x+\frac{a_x\kappa}{\sqrt\pi},
```

recovering the Step-17 curvature growth directly from the smoothed endpoint tail.

On the Step-23 high-excursion scale, finite bandwidth introduces a second coordinate

```math
\boxed{
\zeta_x
=\frac{\kappa}{\sqrt2\,u\sqrt{b_x}}.
}
```

The two independent coordinates are therefore

```math
\boxed{
\chi_x=\frac{a_xu}{\sqrt{b_x}},
\qquad
\zeta_x=\frac{\kappa}{\sqrt2\,u\sqrt{b_x}}.
}
```

The two-parameter tangent variogram is

```math
\boxed{
\begin{aligned}
g_{\chi,\zeta}(t)
&=t^2+\sqrt2\chi\Bigg[
|t|\operatorname{erf}(\zeta|t|)\\
&\qquad+\frac{e^{-\zeta^2t^2}-1}{\sqrt\pi\,\zeta}
\Bigg].
\end{aligned}
}
```

Endpoints:

```math
g_{\chi,\infty}(t)=t^2+\sqrt2\chi|t|
```

recovers Step 23, while `zeta->0` gives a purely quadratic smooth tangent with the finite-band curvature above.

Define the corresponding generalized Pickands constant

```math
\mathcal H(\chi,\zeta)
=\lim_{T\to\infty}\frac1T
E\exp\left[\sup_{0\le t\le T}
(\sqrt2\eta_{\chi,\zeta}(t)-g_{\chi,\zeta}(t))\right].
```

Then

```math
\boxed{\mathcal H(\chi,\infty)=\mathcal H_{mix}(\chi).}
```

**REJECTED SHORTCUT / REFINEMENT:** computing only `H_mix(chi)` cannot determine the finite-`kappa` boundary or rule out a bounded re-entrant pocket. The approach to the endpoint is genuinely two-parameter and requires at least `H(chi,zeta)` plus finite-`u` control.

See `FINITE_BAND_TANGENT_BRIDGE_STEP.md` and `numerics/finite_band_tangent_bridge.py`.

---

## 3. Current frontier

The correct local object for deterministic finite-band continuation has now been identified:

```math
\boxed{\mathcal H(\chi,\zeta)}.
```

The next problem is to evaluate this two-parameter generalized Pickands constant efficiently, preferably through a Dieker–Yakir-type representation, and determine whether its `zeta` dependence plus a controlled finite-threshold correction is strong enough to establish monotonic high-band convergence or exclude a bounded re-entrant preference pocket.

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
- `H_mix(chi)` alone describes finite-band convergence;
- no bounded high-band re-entrant pocket can exist without a monotonicity/error proof;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 5. Single natural next question — DO NOT ANSWER YET

> Can the two-parameter generalized Pickands constant `H(chi,zeta)` be evaluated efficiently using a Dieker–Yakir representation, and does its dependence on `zeta` have enough monotonic structure to control the finite-band approach and rule out a bounded re-entrant preference pocket?
