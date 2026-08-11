# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 18:42 EDT  
**Status:** twenty-two logical steps completed. Step 22 maps representative points of the Palm-corrected finite-`r` preference boundary and performs a higher-statistics Palm scan of the Step-19 large-`r` bandwidth optimum. The high-band slow-preferred region survives at larger timing uncertainty; the old `Lambda=0.895` second crossing disappeared because Palm correction lifts the boundary to about `Lambda~0.91`. The finite bandwidth optimum also survives Palm correction, but is shallower and broader than Rice predicted. No universal replacement metric and no novelty claim.

---

## 1. Original question

Two detectors satisfy

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

## 2. Surviving chain

### Steps 01–04 — limits of scalar and magnitude-only `D*`
- Equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals; an explicit 1 Hz first-order/additive-output-noise example gave `SNR_A/SNR_B~6.36`.
- For a known waveform with unrestricted full observation,

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}(f)\,df.
```

- **NEGATIVE RESULT:** unknown timing alone does not break this ideal stationary-Gaussian full-observation equivalence when complete magnitude `D*(f)` is identical.
- Finite observation can break it because magnitude `D*(f)` discards phase/temporal placement; a causal all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-record SNR and timing search

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

and

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold governed by timing-scan covariance, not digital sample count.

### Step 09 — finite-deadline correction and ranking reversal
**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be combined directly with full-template timing bandwidth as one exact finite-deadline statistic.

Controlled family:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members acquire SNR sooner but can pay a larger unknown-time search burden. Cross-detector ranking can reverse.

### Steps 10–12 — task-level detection time and scaled boundary

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

For `r=tau_s/tau_f`, the exact fast/slow task boundary is

```math
X_D(r\ell)-rX_D(\ell)=0.
```

### Step 13 — rough finite-window obstruction

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
 a_x=\frac{2x^2e^{-2x}}{\eta(x)}.
```

The ideal-white-noise finite hard-window scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** the Step-13 rough-grid crossover near `ell~49` is invalid.

### Steps 14–15 — genuine finite timing-information bandwidth
**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily a true information-band limit because optimal whitening can undo it.

Use the smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the cusp and gives controlled correlated-scan numerics.

### Step 16 — exact continuous Palm rare-event identity

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
}
```

with

```math
\lambda_u=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Rice/EC is an upper bound; its error is multiple excursions plus endpoint overlap. Palm importance sampling makes `alpha=1e-6` practical.

### Step 17 — high-threshold law and nonuniform Rice limit
The exact smooth crossover contains Palm correction factors. For isolated excursions a compact endpoint-retaining Rice law follows.

**REJECTED SHORTCUT:** small `alpha` does not justify dropping the endpoint `Q(u)` term.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform as `kappa->infinity` toward the rough limit.

For the co-scaled extreme-speed-ratio branch,

```math
L_\times\to\tau_f\ell_{crit,\kappa}.
```

### Step 18 — common physical bandwidth with accessible SNR forced equal

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

With accessible eventual SNR artificially held fixed, the large-`r` crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no interior bandwidth optimum exists under that artificial normalization.

### Step 19 — fixed physical signal/noise; finite bandwidth optimum
Remove SNR renormalization:

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
\qquad
\sigma^2(\kappa)=I_2/I_0.
```

Wide band:

```math
\rho_\infty=\rho_{full}[1-1/(2\kappa^2)+O(\kappa^{-3})],
```

while

```math
\sigma=1-2/(\sqrt\pi\kappa)+O(\kappa^{-2}).
```

Thus SNR loss is `O(1/kappa^2)` but timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** a finite large-`r` Rice bandwidth optimum exists whenever the full-band detector is strictly known-time feasible.

### Step 20 — finite-r common-bandwidth Rice double reversal
At common finite physical bandwidth the slower scaled member has the larger accessible eventual SNR, with

```math
\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r
```

in the narrow-band limit.

For

```text
r=2
rho_full=6.2407571
alpha=1e-6
beta=0.90
Lambda=0.895
```

finite-duration Rice gave apparent switches

```text
25.4898402
130.1945883
```

and apparent topology `slow -> fast -> slow`. The spectral quadrature was converged, but Palm validation remained open.

### Step 21 — Palm correction changes the Step-20 topology
Use

```math
u_{avail}(x)=\rho(x)-\Phi^{-1}(\beta)
```

and test directly

```math
P_{FA}^{Palm}(u_{avail})\le\alpha.
```

The lower switch survives:

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.}
```

The reported upper Rice switch near `130.19` is **INVALIDATED**. Palm tests at `kappa_f=130`, `160`, and `300` keep the fast detector preferred for the `Lambda=0.895` slice. Cause: nonuniform Rice micro-upcrossing overcount, especially severe for the shorter slow-detector finite window.

### Step 22 — Palm-corrected boundary map and true finite optimum
The Palm boundary is mapped locally by solving

```math
\boxed{
\frac{\ell_{Rice,f}(X,\kappa_f)}{C_f}
=
r\frac{\ell_{Rice,s}(X/r,r\kappa_f)}{C_s}
}
```

and iterating the Palm correction factors at the displaced boundary.

For the same `r=2` task, representative boundary points are

```text
kappa_f     Lambda_cross^Palm
~10         ~0.794
~20         ~0.891
21.7         0.895   (Step-21 validated slice crossing)
30          ~0.9052
60          ~0.9098
100         ~0.9103
200         ~0.9099
```

**REFINEMENT:** the high-band slow-preferred region does **not** disappear. Palm correction lifts the boundary above the old `Lambda=0.895` slice; tasks with larger timing uncertainty remain on the slow-preferred side of the tracked boundary.

The Step-19 large-`r` full-template objective was also rescanned with higher-statistics Palm simulation. Representative results:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

Independent `kappa=60` runs and a `30000`-path infinite-band run resolve a finite-minus-infinite advantage of roughly

```text
0.3–0.4%
```

at several combined standard errors.

**NUMERICAL VALIDATION / CONDITIONAL:** the finite bandwidth optimum survives Palm correction. It is shallower and broader than Rice predicted, with the present maximum localized only to roughly

```math
\boxed{\kappa_{opt}^{Palm}\sim50\text{–}65.}
```

No uniqueness claim.

See `PALM_BOUNDARY_MAP_STEP.md` and `numerics/palm_boundary_map.py`.

---

## 3. Current frontier

The remaining high-band question is now analytic rather than topological-by-spot-check:

- the high-band slow-preferred region exists at finite high bandwidth;
- the particular `Lambda=0.895` second reversal was spurious;
- the large-`r` finite-band optimum survives exact rare-event correction.

The unresolved problem is the finite-`r` asymptotic boundary as `kappa_f->infinity`, where finite-hard-window roughness and full-template convergence do not commute.

---

## 4. What is established

- Equal scalar `D*` does not determine arbitrary temporal-signal performance.
- Complete magnitude `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make temporal phase/placement operationally relevant.
- Finite SNR and timing search must be derived from the same finite measurement problem.
- The controlled family admits conditional fast/slow ranking reversal.
- **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` is invalid.
- Genuine finite timing-information bandwidth removes the hard-window cusp.
- Exact Palm rare-event correction is practical at `alpha=1e-6`.
- **DERIVED:** Rice accuracy is nonuniform toward the finite-window rough limit.
- **INVALIDATED:** the Step-20 upper Rice switch near `130.19` is not a Palm switch.
- **NUMERICAL VALIDATION:** the lower finite-r Palm switch is `~21.7 +/-0.3` for the stated task.
- **REFINEMENT:** high-band slow-preferred tasks survive above a Palm boundary near `Lambda~0.91` in the tested range.
- **NUMERICAL VALIDATION / CONDITIONAL:** the Step-19 finite-bandwidth optimum survives Palm correction, with a shallow maximum near `kappa~50–65` and only `~0.3–0.4%` gain over infinite bandwidth for the calibration used.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover or bandwidth-optimum uniqueness for arbitrary parameters.
- No exact finite-`r` `kappa_f->infinity` Palm boundary.
- No proof excluding additional horizontal-slice reversals for every `Lambda`.
- No claim that the Gaussian information weighting is a literal circuit transfer function.
- No hardware bandwidth recommendation.
- No exact global-rejection/localization, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity treatment.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> Can the high-band finite-r Palm boundary be derived asymptotically by matching the finite-hard-window rough excursion law to the smooth full-template limit, so that the `kappa_f -> infinity` boundary and the possibility of any additional reversals can be settled analytically rather than by Monte Carlo mapping?
