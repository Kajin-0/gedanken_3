# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 16:37 EDT  
**Status:** twenty-one logical steps completed. Step 21 applies the exact continuous upcrossing-Palm identity to the finite-r fixed-physics bandwidth sweep. The lower bandwidth-driven slow-to-fast reversal survives but shifts from Rice `kappa_f ~=25.49` to Palm `~21.7 +/-0.3`. The reported upper Rice switch near `130.19` is invalidated: Palm calculations at `kappa_f=130`, `160`, and `300` all keep the fast detector preferred. A different unobserved high-band Palm reversal is not rigorously excluded. No universal replacement metric and no novelty claim.

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

## 2. Surviving logical path

### Steps 01–04 — scalar `D*`, complete magnitude `D*(f)`, and finite-window phase

- Equal reference scalar `D*` does **not** guarantee equal SNR for arbitrary temporal signals; an explicit 1 Hz counterexample gave `SNR_A/SNR_B ~6.36`.
- For a known finite-energy waveform under stationary additive noise and unrestricted full observation,

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int |P|^2D^{*2}(f)\,df.
```

- **NEGATIVE RESULT:** unknown arrival time alone does not break that full-observation stationary-Gaussian equivalence when complete magnitude `D*(f)` is identical.
- Finite observation can break equivalence because magnitude `D*(f)` discards temporal phase/placement; a causal all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-record SNR and timing search

Exact finite-record linear SNR:

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Known-time Gaussian detection:

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold determined by the timing-scan covariance, not digital sample count. When the timing spectrum has finite second moment, its RMS frequency controls local covariance curvature and Rice upcrossing density.

### Step 09 — finite-deadline correction and ranking reversal

The actual finite search must use

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

### Steps 10–12 — task-level detection time and scaled fast/slow boundary

Define

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

For the scaled family,

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

For `r=tau_s/tau_f` and `ell=L/tau_s`, the exact preference boundary is

```math
X_D(r\ell)-rX_D(\ell)=0.
```

Task space can contain both-feasible, slow-only, and neither-feasible regions.

### Step 13 — direct correlated numerics and failed rough-grid crossover

The finite hard-window covariance has

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
 a_x=\frac{2x^2e^{-2x}}{\eta(x)}.
```

Thus the ideal-white-noise finite scan is locally Brownian-like / nondifferentiable.

**FAILED NUMERICAL ESTIMATE:** the diagnostic Step-13 crossover near `ell ~49` moved under timing-grid refinement and is invalid.

### Steps 14–15 — genuine finite timing-information bandwidth

**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily a true information-band limit because optimal whitening can undo it.

Use the smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the covariance cusp. Direct correlated FFT simulation has controlled grid behavior and agrees with Rice/EC at validation points.

### Step 16 — exact continuous Palm rare-event identity

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

Therefore Rice/EC is an upper bound; its error is exactly multiple high excursions plus endpoint/upcrossing overlap. Palm importance sampling makes `alpha=1e-6` practical.

### Step 17 — high-threshold crossover law and nonuniform Rice limit

The exact smooth crossover contains Palm correction factors. For isolated excursions the endpoint-retaining Rice law follows.

**REJECTED SHORTCUT:** small global `alpha` does not justify dropping the endpoint `Q(u)` term.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform as finite-window bandwidth tends toward the rough limit.

For the co-scaled extreme-speed-ratio branch,

```math
L_\times\to\tau_f\ell_{crit,\kappa}.
```

### Step 18 — one shared physical bandwidth with accessible SNR forced equal

Use

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

With accessible eventual SNR artificially held fixed, the large-r crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no interior bandwidth optimum exists under that artificial equal-accessible-SNR normalization.

### Step 19 — fixed physical signal/noise and genuine finite bandwidth optimum

Remove SNR renormalization:

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
\qquad
\sigma^2(\kappa)=I_2/I_0.
```

At wide bandwidth,

```math
\rho_\infty(\kappa)
=\rho_{full}[1-1/(2\kappa^2)+O(\kappa^{-3})],
```

while

```math
\sigma(\kappa)
=1-2/(\sqrt\pi\kappa)+O(\kappa^{-2}).
```

SNR loss is `O(1/kappa^2)` but timing-search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** for the large-r full-template Rice objective, infinite bandwidth is suboptimal whenever the full-band detector is strictly known-time feasible; at least one finite bandwidth optimum exists.

Step-16-calibrated Rice illustration:

```text
rho_full ~=6.240757
alpha=1e-6
beta=0.90
kappa_opt^Rice ~=42.23
ell_crit^Rice(opt) ~=0.90083
ell_crit^Rice(infinity) ~=0.88906
```

A Palm spot check preserved the finite-candidate-over-infinite ordering; exact Palm optimization remains open.

### Step 20 — finite-r common-bandwidth Rice double reversal

For one shared physical bandwidth without SNR renormalization,

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=r\kappa_f.
```

Because `F(kappa)` increases with bandwidth,

```math
\rho_{\infty,s}>\rho_{\infty,f}
```

at every finite common bandwidth in the equal-full-band-SNR scaled family, with

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
Lambda=L/tau_f=0.895
```

finite-duration Rice gave

```text
kappa_cross_1^Rice ~=25.4898402
kappa_cross_2^Rice ~=130.1945883
```

and apparent topology

```math
\text{slow}\to\text{fast}\to\text{slow}.
```

The spectral quadrature was highly converged, but Step 20 explicitly left Palm validation open.

### Step 21 — Palm correction changes the topology

For any candidate duration `x`, define the largest threshold compatible with target detection probability:

```math
\boxed{
u_{avail}(x)=\rho(x)-\Phi^{-1}(\beta).}
```

The exact smooth-process decision condition is

```math
\boxed{
P_{FA}^{Palm}(u_{avail}(x))\le\alpha.
}
```

This avoids repeatedly inverting a noisy rare-event threshold inside the detection-time solve.

#### Lower switch

Refined Palm correction near the displaced switch gave correction factors near

```text
C_fast ~0.994
C_slow ~0.952-0.956.
```

Solving the two same-physical-time Palm balance equations and halving the local correction grid gives the conservative summary

```math
\boxed{
\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.
}
```

This is about `15%` below the Rice value `25.49`.

**NUMERICAL VALIDATION / CONDITIONAL:** the lower slow-to-fast reversal survives.

#### Upper Rice switch

At `kappa_f=130`, direct Palm evaluation at the same physical time gives

```text
X=7.0:
    fast P_FA/alpha ~=0.9918 +/-0.0014
    slow P_FA/alpha ~=1.2668 +/-0.0079

X=7.5:
    fast P_FA/alpha ~=0.9897 +/-0.0014
    slow P_FA/alpha ~=1.0444 +/-0.0060
```

So fast is already feasible at physical times where slow is not.

Wider-band checks preserve that ordering:

```text
kappa_f=160, X=7.0:
    fast P_FA/alpha ~=0.9903
    slow P_FA/alpha ~=1.2565

kappa_f=300, X=6.5:
    fast P_FA/alpha ~=0.9950
    slow P_FA/alpha ~=1.7006
```

**INVALIDATED:** `kappa_cross_2^Rice ~=130.1945883` is not a continuous Palm switch.

The failure mechanism is the nonuniform Rice limit: high-band finite-window micro-upcrossings cluster into the same rough excursion. The slow detector's shorter dimensionless window has the larger hard-window endpoint and receives the much larger Rice overcount.

A rough-limit high-threshold Pickands check also favors fast strongly, but is not an exact finite-alpha proof.

The surviving directly validated topology through `kappa_f<=300` is therefore

```math
\boxed{\text{slow}\to\text{fast}.}
```

**OPEN:** a different unobserved high-band Palm reversal at some other finite bandwidth is not rigorously excluded.

See `PALM_CORRECTED_FINITE_R_BANDWIDTH_STEP.md` and `numerics/finite_r_palm_validation.py`.

---

## 3. Current frontier

The main lesson of Step 21 is methodological as well as physical: a fully converged numerical calculation of an asymptotic approximation can still have the wrong phase topology when the approximation fails nonuniformly.

The next frontier is to map the Palm-corrected preference boundary in

```text
(Lambda, kappa_f)
```

well enough to answer two questions:

1. does the high-band slow-preferred region disappear entirely after Palm correction?;
2. does the Step-19 finite-bandwidth optimum survive as a true maximum of the Palm-corrected boundary?

---

## 4. What is established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete magnitude `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make temporal phase/placement operationally relevant.
- Finite SNR and timing search must come from the same finite measurement problem.
- The controlled family admits conditional fast/slow ranking reversals.
- **NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.
- **FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` is invalid.
- Genuine finite timing-information bandwidth removes the hard-window cusp.
- Smooth scans admit efficient exact-Palm rare-event identities and practical Palm importance sampling.
- **DERIVED:** Rice accuracy is nonuniform toward the finite-window rough limit.
- **DERIVED / CONDITIONAL:** fixed physical signal/noise creates a finite large-r bandwidth optimum in the Rice objective; Palm spot checks preserve the finite-vs-infinite ordering.
- **DERIVED:** common finite physical bandwidth gives the slower scaled member a low-band accessible-SNR advantage approaching `sqrt(r)`.
- **NUMERICAL VALIDATION:** the Step-20 lower bandwidth reversal survives Palm correction at `kappa_f ~21.7 +/-0.3`.
- **INVALIDATED:** the Step-20 reported upper Rice switch near `130.19` is not a Palm switch.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover or bandwidth-optimum uniqueness for arbitrary parameters.
- No exact finite-alpha proof that no other high-band Palm reversal exists.
- No complete Palm-corrected `(Lambda,kappa_f)` phase boundary yet.
- No exact Palm optimization of the Step-19 finite bandwidth optimum.
- No claim that the Gaussian information weighting is a literal circuit transfer function.
- No hardware bandwidth recommendation.
- No exact global-rejection/localization surface, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity treatment.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> Can the full Palm-corrected preference boundary in `(Lambda,kappa_f)` be mapped well enough to determine whether the high-band slow-preferred region disappears entirely, and whether the finite bandwidth optimum from Step 19 survives as a true Palm boundary maximum?
