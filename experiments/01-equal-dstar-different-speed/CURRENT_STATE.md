# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 16:12 EDT  
**Status:** twenty logical steps completed. Step 20 extends the fixed-physics bandwidth problem to a genuinely finite speed ratio and gives a converged finite-duration Rice counterexample in which sweeping one common physical readout bandwidth changes the preferred detector twice: `slow -> fast -> slow`. Exact Palm-corrected switch locations remain open. No universal replacement metric and no novelty claim.

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

## 2. Surviving logical path

### Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase

- Equal reference scalar `D*` does **not** guarantee equal SNR for arbitrary temporal signals; the explicit 1 Hz first-order/additive-output-noise example gave `SNR_A/SNR_B ~ 6.36`.
- Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem:

```math
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

- **NEGATIVE RESULT:** unknown arrival time alone does not break that ideal stationary-Gaussian full-observation equivalence.
- Finite observation can break it because magnitude `D*(f)` discards temporal phase/placement; a stable causal all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-record SNR and timing search

Exact finite-record linear SNR:

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Known-time Gaussian detection:

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold governed by the timing-scan covariance, not by digital sample count. When the noise-weighted timing spectrum has finite second moment, its RMS timing frequency controls local covariance curvature and Rice upcrossing density.

### Step 09 — finite-deadline correction and conditional ranking reversal

The finite search must use

```math
q_t=C_t^{-1}s_t
```

and its own covariance.

**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be combined directly with full-template timing bandwidth as one exact finite-deadline statistic.

Controlled family:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members acquire SNR sooner but can pay a larger unknown-time search penalty. Cross-detector ranking can reverse.

### Steps 10–12 — task-level detection time and fast/slow boundary

Define

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the scaled family,

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family; use all data permitted by the deadline.

For `r=tau_s/tau_f` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(r\ell)-rX_D(\ell)=0.
```

Task space contains both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one crossover exists under the stated continuity/extreme-value assumptions; uniqueness remains open.

### Step 13 — direct correlated numerics and a failed continuum estimate

A direct FFT moving-average Monte Carlo simulated the actual correlated grid-sampled finite-duration scan without independent-trials replacement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell ~ 49` moved under timing-grid refinement and must never be quoted as continuous-time results.

Exact cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
 a_x=\frac{2x^2e^{-2x}}{\eta(x)},
```

so the ideal-white-noise finite hard-window scan is locally Brownian-like / mean-square nondifferentiable.

### Steps 14–15 — genuine finite timing-information bandwidth

**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening can undo it.

Use the explicit smooth information penalty

```math
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the covariance cusp. Direct correlated FFT simulation has controlled timing-grid behavior and agrees with Rice/Euler-characteristic predictions at validation points.

### Step 16 — exact Palm rare-event identity

For a differentiable stationary Gaussian timing scan,

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

Thus Rice/EC is an upper bound; its error is exactly multiple high excursions plus endpoint/upcrossing overlap. A Palm sampler makes `alpha=1e-6` tractable with thousands of paths.

For the validation task `rho_0=6.2`, `r=1.2`, `alpha=1e-6`, `beta=0.90`, `kappa=8`, Palm gave

```text
ell_cross ~= 0.5721 +/- 0.001
```

versus Rice `0.57144`.

### Step 17 — high-threshold law and extreme speed ratio

The exact smooth Palm-corrected crossover has the structure

```math
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
```

For isolated excursions `C_s,C_f~1`, this becomes the endpoint-retaining Rice law.

**REJECTED SHORTCUT:** small global `alpha` does not justify dropping the endpoint `Q(u)` term; in the Step-16 task it consumes roughly half the false-alarm budget.

For finite hard windows,

```math
\sigma_\kappa^2(x)
\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform as `kappa -> infinity` toward the rough Step-13 limit.

For the co-scaled extreme-speed-ratio branch,

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}}.
```

### Step 18 — one shared physical electronics bandwidth, equal accessible SNR

Impose one physical information scale:

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

Step 18 still forced equal **accessible eventual SNR** to isolate timing/search effects.

**REFINEMENT:** the clean large-`r` fast-feasibility-edge limit requires `ell_crit(kappa_f)/r -> 0`; `r->infinity` alone is insufficient if `kappa_f` simultaneously collapses.

Under that condition,

```math
L_\times\to\tau_f\ell_{crit}(\Omega_B\tau_f).
```

With accessible SNR artificially fixed, the crossover changes from an electronics-limited `~1/Omega_B` scale to an intrinsic-detector `~tau_f` scale.

**NEGATIVE RESULT / QUALIFICATION:** no finite bandwidth optimum exists while accessible eventual SNR is artificially held fixed.

### Step 19 — fixed physical signal/noise; genuine finite bandwidth optimum

Remove the Step-18 SNR renormalization. For the full fast template define

```math
F(\kappa)=I_0(\kappa)/(\pi/2),
\qquad
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
```

and

```math
\sigma^2(\kappa)=I_2(\kappa)/I_0(\kappa).
```

Known-time feasibility imposes a finite lower bandwidth threshold. Near the wide-band limit,

```math
\rho_\infty(\kappa)
=\rho_{full}\left[1-\frac1{2\kappa^2}+O(\kappa^{-3})\right],
```

while

```math
\sigma(\kappa)
=1-\frac{2}{\sqrt\pi\kappa}+O(\kappa^{-2}).
```

Thus SNR loss is `O(1/kappa^2)` while the reduction in timing-search curvature is the larger `O(1/kappa)` effect. Therefore, for the large-`r` full-template Rice objective,

```math
\ell_{crit}^{Rice}(\kappa)
=\ell_{crit}^{Rice}(\infty)
\left[1+\frac{2}{\sqrt\pi\kappa}+O(\kappa^{-2})\right].
```

**DERIVED / CONDITIONAL:** whenever the full-band detector is strictly known-time feasible, infinite bandwidth is suboptimal for this unknown-time objective and at least one finite bandwidth optimum exists.

Step-16-calibrated illustration:

```text
rho_full ~= 6.240757
alpha = 1e-6
beta = 0.90
kappa_min ~= 3.14545
kappa_opt^Rice ~= 42.23
ell_crit^Rice(kappa_opt) ~= 0.90083
ell_crit^Rice(infinity) ~= 0.88906
```

A `10000`-path Palm spot check preserved the finite-candidate-over-infinite ordering, but the exact Palm optimum remains open.

### Step 20 — finite speed ratio; two bandwidth-driven preference reversals

Now apply the same fixed physical bandwidth to both finite-`r` detectors **without** accessible-SNR renormalization:

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=r\kappa_f.
```

Because the full-template accessible fraction `F(kappa)` is strictly increasing,

```math
\boxed{
\rho_{\infty,s}(\kappa_f)
=\rho_{full}\sqrt{F(r\kappa_f)}
>
\rho_{\infty,f}(\kappa_f)
=\rho_{full}\sqrt{F(\kappa_f)}
}
```

for every finite bandwidth. In the narrow-band limit,

```math
\boxed{
\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r.
}
```

Thus the slow detector gets a low-band SNR head start.

For finite-duration scans use

```math
\rho_i(x)
=\rho_{full}
\sqrt{I_{0,i}(x)/(\pi/2)},
\qquad
\sigma_i^2(x)=I_{2,i}(x)/I_{0,i}(x),
```

with each detector's own `kappa_i`, search interval, and Rice threshold.

Explicit finite-r counterexample:

```text
r        = 2
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90
Lambda   = L/tau_f = 0.895
```

Direct finite-duration Rice solutions give

```text
kappa_f    T_f/tau_f    T_s/tau_f    preference
20         infeasible    7.56822       slow only
25          8.02316      7.61341       slow
30          6.81840      7.65936       fast
80          7.09937      8.03871       fast
120         7.93053      8.26231       fast
140         9.11095      8.35794       slow
160        infeasible    8.44554       slow only
```

The two finite switch points are

```math
\boxed{\kappa_{\times,1}\approx25.4898402,}
```

```math
\boxed{\kappa_{\times,2}\approx130.1945883.}
```

Both occur while both detectors are feasible. Halving the spectral quadrature spacing from `dnu=0.02` to `0.01` changes the switch values by only about `1.4e-8` and `5.4e-7`, respectively.

**NUMERICAL COUNTEREXAMPLE / CONDITIONAL:** even with only a factor-of-two intrinsic speed difference, sweeping one common physical readout bandwidth can produce

```math
\boxed{
\text{slow}\to\text{fast}\to\text{slow}.
}
```

The mechanism is:

```text
narrow band      -> accessible-SNR asymmetry favors slow
intermediate band-> response-time advantage favors fast
wide band        -> unknown-time search burden favors slow
```

The finite-r task boundary is therefore nonmonotone in bandwidth for this example, so the Step-19 finite-bandwidth structure is not merely an `r -> infinity` artifact.

See `FINITE_R_BANDWIDTH_REVERSAL_STEP.md` and `numerics/finite_r_bandwidth_reversal.py`.

---

## 3. Current frontier

The fixed-physics branch now demonstrates both:

```text
large-r finite bandwidth optimum
and
finite-r multiple detector-preference reversals versus one common bandwidth.
```

The next unresolved issue is exact rare-event validation of the finite-r double reversal. Step 17 proved that finite-window Rice accuracy becomes nonuniform at large `kappa`, making the upper switch especially important to check with the Step-16 Palm machinery.

---

## 4. What is established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make temporal phase/placement operationally relevant.
- Finite SNR and timing search must come from the same finite measurement problem.
- The controlled family admits a conditional fast/slow ranking reversal and task-regime boundary.
- **NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.
- **FAILED NUMERICAL ESTIMATE:** the Step-13 rough-grid `ell~49` crossover is invalid.
- Genuine finite information bandwidth removes the hard-window cusp without removing the task-regime mechanism.
- Smooth scans admit efficient Palm rare-event evaluation at `alpha=1e-6`.
- **DERIVED:** Rice accuracy is nonuniform toward the finite-window rough limit.
- **DERIVED / ASYMPTOTIC:** extreme speed ratio reduces the crossover to the fast full-template feasibility edge.
- **DERIVED / ASYMPTOTIC:** shared physical electronics introduces an electronics-limited `1/Omega_B` regime when accessible SNR is held fixed.
- **NEGATIVE RESULT:** no bandwidth optimum exists if accessible eventual SNR is artificially renormalized to remain fixed.
- **DERIVED / CONDITIONAL:** restoring physical SNR loss produces a genuine finite bandwidth optimum for the large-`r` crossover objective.
- **DERIVED:** at common finite physical bandwidth, the slower member has larger accessible eventual SNR in the equal-full-band-SNR family, with narrow-band ratio approaching `sqrt(r)`.
- **NUMERICAL COUNTEREXAMPLE / CONDITIONAL:** at finite `r=2`, a common bandwidth sweep can reverse detector preference twice in the finite-duration Rice model.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover, bandwidth-optimum, or reversal-count uniqueness for arbitrary parameters.
- No exact rough finite-`r`, infinite-bandwidth crossover.
- No claim that the Gaussian information weighting is a literal circuit transfer function.
- No claim that illustrative GHz values are hardware recommendations.
- No exact Palm optimization of Step 19's finite optimum.
- No exact Palm-corrected Step-20 switch locations yet.
- No proof that all tasks exhibit two bandwidth reversals; Step 20 is an existence counterexample.
- No exact global-rejection/localization surface, Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single next question — DO NOT ANSWER YET

> Does the exact continuous Palm correction preserve both finite-`r` bandwidth reversals, especially the high-bandwidth switch where finite-window Rice accuracy is least uniform, and how far do the two switch points move?
