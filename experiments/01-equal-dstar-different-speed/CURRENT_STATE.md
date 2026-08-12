# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 21:17 EDT  
**Status:** thirty-one logical steps completed. Step 31 inserts the Step-30 canonical Brownian–parabola crossover into the finite-`r` high-band boundary and calibrates only the residual finite-`u` offset to the existing Palm boundary anchors plus the direct rough endpoint. The central bridge has one shallow maximum near `kappa_f~95`, then decreases continuously toward `Lambda_infinity~0.90513`. For the original `r=2`, `Lambda=0.895` calibration, no bounded high-band re-entrant slow-preferred pocket is numerically supported. This is a numerical closure for that task, not a theorem-level interval enclosure or a global statement for all task parameters. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical detectors satisfy equal conventional specific detectivity but have radically different temporal responses. Does equal `D*` imply equal ability to detect arbitrary optical signals?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar and magnitude-only `D*`
- Equal scalar reference `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation Gaussian maximum-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that ideal full-observation equivalence.
- Finite observation can because magnitude `D*(f)` discards phase/temporal placement.

### Steps 05–12 — finite records and task-level timing search
Derived

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle
```

and task-level detection time

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise scans have `R_x(y)=1-a_x|y|+...` and are locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid `ell~49` crossover invalid.

### Steps 14–17 — genuine timing bandwidth and exact rare events
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm identity is available; Rice/EC is an upper bound. For finite hard windows `sigma_kappa^2~a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform toward the rough limit.

### Steps 18–19 — shared physical bandwidth and finite optimum
Use `kappa_i=Omega_B tau_i`. Artificially forcing accessible eventual SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed restores bandwidth-dependent SNR and produces a finite large-`r` optimum; later Palm work confirms a shallow optimum survives beyond Rice.

### Steps 20–21 — finite-`r` Rice double reversal corrected by Palm
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only the lower switch:

```math
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
```

**INVALIDATED:** upper Rice switch. Palm checks at `130,160,300` keep fast preferred for that slice.

### Step 22 — Palm boundary map and finite optimum
Representative finite-`r` Palm boundary:

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

High-band slow-preferred tasks survive above the lifted boundary. Large-`r` full-template Palm optimum is broad near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Step 23 — matched rough/smooth infinite-band limit
Finite hard-window local expansion:

```math
R_x(y)=1-a_x|y|-\frac{b_x}{2}y^2+O(|y|^3),
\qquad
\chi_x=a_xu/\sqrt{b_x}.
```

At `kappa=infinity`, tangent variance is `t^2+sqrt(2)chi|t|`. Exact occupation-time importance sampling handles `u~5`. Direct rough endpoint:

```math
\Lambda_{cross}^{\infty}\approx0.905\pm0.004,
\qquad X\approx7.75.
```

Thus `Lambda=0.895` is fast-preferred at the endpoint too.

### Step 24 — finite-band tangent bridge
Finite bandwidth adds

```math
\zeta=kappa/(\sqrt2u\sqrt b).
```

**REJECTED SHORTCUT:** one-parameter `H_mix(chi)` is only the `zeta=infinity` endpoint.

### Step 25 — generalized Dieker–Yakir representation

```math
H(\chi,\zeta)=E[\sup e^W/\int e^W].
```

Brown–Resnick Slepian comparison proves `partial_zeta H>=0`, `partial_chi H>=0`. Local extreme statistics cannot oscillate with bandwidth, but this alone does not prove the physical boundary monotone.

### Step 26 — coupled physical high-band derivative
Exact implicit boundary derivative derived. Finite-hard-window SNR recovery is `O(kappa^-1)`. Positive `H_mix-H~C_H/sqrt(zeta)` would force eventual negative boundary slope for the `r=2` calibration.

### Step 27 — exact Gaussian-mollifier coupling scale
Common-white-noise coupling gives

```math
\sup_t SD[W_\infty-W_\zeta]_{random}
\le0.8906480701\sqrt{\chi/\zeta}.
```

**INVALIDATED INTERMEDIATE:** `0.8131` used the large-lag variance instead of the true maximum. Conservative bound `0<=H_mix-H<=C_chi sqrt(log zeta/zeta)`. Coupling proves the scale but not a positive lower coefficient.

### Step 28 — Bessel zoom-in positive coefficient
Brownian-extremum/two-sided-BES(3) zoom-in plus Gaussian mollification gives, under stable-convergence/localization/UI,

```math
H_mix(\chi)-H(\chi,\zeta)
=C_H(\chi)\zeta^{-1/2}+o(\zeta^{-1/2}),
```

with positive kernel-specific `C_H`. The Dieker–Yakir denominator is lower order. Quantitative finite-band remainder remains open.

### Step 29 — Brownian–parabola double scaling
Small `chi` introduces

```math
h_\chi=\sqrt2\chi^{1/3},
\qquad
m_\chi=2\chi^{2/3},
```

and the correct crossover coordinate

```math
\mu=\sqrt2\zeta\chi^{1/3}.
```

At the `r=2` endpoint,

```math
\mu_f\approx0.009776\kappa_f,
\qquad
\mu_s\approx0.16139\kappa_f.
```

Slow is already in the Bessel tail around `kappa_f=100–300`; fast is still in crossover. **REFINEMENT:** Step-26 fast `C_H~0.0061` is pre-asymptotic.

### Step 30 — canonical crossover function
The small-`chi` crossover reduces to

```math
Y_\infty(s)=B(s)-s^2
```

with finite `mu` obtained by Gaussian filtering the white derivative. Let `M_inf=sup Y_inf`, `M_mu=sup Y_mu`. Then

```math
\boxed{
F(\mu)=\frac{2}{\sqrt\pi}E[M_\infty-M_\mu].
}
```

Continuum-extrapolated values:

```text
mu:       0     .5     1      2      3      5      10     20
F(mu):  .892   .806   .729   .597   .512   .410   .297   .213
```

and `sqrt(mu)F(mu)->A_K~0.98` in the Bessel tail. Nested-grid full fast-channel calculations agree at the percent level.

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by under-resolving the rough maximum; do not reuse them as continuum crossover values.

Fast endpoint asymptotic coefficient refines to `C_H~0.0088`, strengthening the Step-26 positive high-band boundary coefficient sign.

### Step 31 — Palm-anchored universal high-band bridge
Insert the Step-30 fast crossover into the finite-`u` tangent boundary. The resulting tangent shape has representative values

```text
kappa_f:       60      100      200      300      1000      infinity
Lambda_tan:  .88255   .88604   .88715   .88714   .88660     .88564
```

The absolute tangent boundary has the known finite-`u` rare-event offset. Define `delta=Lambda_exact-Lambda_tan`, fix

```math
\delta_\infty=0.90513-0.88564=0.01949,
```

and fit the minimal relaxation

```math
\delta(\kappa)=\delta_\infty+A\kappa^{-p}
```

to Step-22 Palm anchors at `kappa=60,100,200`. The fit gives

```text
A ~=0.18206
p ~=0.77501.
```

The central Palm-anchored bridge is

```text
kappa_f      Lambda_bridge
60           0.90966
80           0.91056
100          0.91066
130          0.91042
160          0.91008
200          0.90964
300          0.90882
500          0.90790
1000         0.90695
2000         0.90632
5000         0.90583
10000        0.90559
infinity      0.90513
```

Dense interpolation gives one shallow maximum near

```math
\boxed{\kappa_f\approx94.9,\quad \Lambda_{max}\approx0.91068}
```

and a strictly decreasing central bridge for `kappa_f>=100`.

**NUMERICAL CLOSURE for the original task:** `Lambda=0.895` lies below the whole high-band bridge and below the rough endpoint. Even subtracting the previously reported `0.004` endpoint uncertainty gives about `0.9011>0.895`. No bounded high-band re-entrant slow-preferred pocket is numerically supported for this calibration.

**CONDITIONAL / OPEN:** the finite-`u` discrepancy law is empirical. This is not a theorem-level interval enclosure, does not prove one maximum for all task parameters, and does not exclude other boundary topologies for other `Lambda`, `r`, SNR, or detector models.

See `UNIVERSAL_BRIDGE_BOUNDARY_CLOSURE_STEP.md` and `numerics/universal_bridge_boundary.py`.

---

## 3. Current frontier

For the original `r=2`, `Lambda=0.895` task, the high-band re-entrant pocket is numerically closed. The remaining mathematical gap is the finite-`u` correction between the tangent/cluster description and the exact Palm/occupation boundary.

### Single next question — DO NOT ANSWER YET

> Can the finite-`u` Palm/occupation discrepancy be derived or bounded directly, replacing the empirical `delta_infinity+A kappa^-p` anchoring with a certified interval enclosure for `Lambda_cross(kappa_f)`?

---

## 4. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is exact;
- monotonic `H(chi,zeta)` alone proves monotonic detector preference;
- raw Step-27 tiny-`chi` fast values are continuum crossover data;
- the Step-31 finite-`u` discrepancy law is exact;
- a theorem-level finite onset bandwidth is known;
- no re-entrant pocket can occur for other task parameters;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
