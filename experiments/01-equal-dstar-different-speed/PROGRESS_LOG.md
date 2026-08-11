# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 16:37 EDT:** compact chronology preserving every consequential scientific result, correction, failed shortcut, invalidated numerical estimate, asymptotic qualification, and current stopping point. Full derivations live in the dedicated step files.

---

## Step 01 — 11:21 EDT — scalar `D*` insufficiency
Equal reference scalar `D*` with `tau_A=1 ns`, `tau_B=1 s` does not guarantee equal arbitrary-signal SNR. A 1 Hz first-order/additive-output-noise example gave `SNR_A/SNR_B ~6.36`.

**COUNTEREXAMPLE / QUALIFICATION:** do not infer fast is universally better; signal/noise filtering can cancel.

## Step 02 — 11:32 EDT — full-observation known-waveform SNR

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int |P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted problem.

## Step 03 — 12:02 EDT — unknown timing negative result; finite truncation
**NEGATIVE RESULT:** identical complete magnitude `D*(f)` gives identical stationary-Gaussian full-observation timing-search statistics for the same waveform. Finite windows can still distinguish detectors because phase/temporal placement is discarded.

## Step 04 — 12:09 EDT — latency-compensated dispersion
A stable causal all-pass factor preserves complete magnitude `D*(f)` and infinite-time SNR while changing finite-window SNR after latency alignment.

## Step 05 — 12:18 EDT — exact finite-record SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Eventual detectability and rate of access to it are distinct.

## Step 06 — 12:30 EDT — detection probability by deadline

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

## Step 07 — 12:38 EDT — independent-slot timing search

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**WARNING:** `M` is not digital sample count in a continuous scan.

## Step 08 — 12:47 EDT — continuous timing covariance
Timing-search covariance is determined by the noise-whitened template. When the timing spectrum has finite second moment, RMS timing frequency controls local curvature and Rice upcrossing density.

## Step 09 — 13:01 EDT — finite-deadline correction and ranking reversal
The actual finite scan must use `q_t=C_t^-1 s_t` and its own covariance.

**REJECTED SHORTCUT:** do not combine finite-window SNR accumulation directly with full-template timing bandwidth.

Controlled family:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members acquire SNR sooner but can pay a larger unknown-time search burden. Cross-detector ranking can reverse.

## Step 10 — 13:18 EDT — task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

## Step 11 — 13:28 EDT — dimensionless collapse; no interior integration optimum

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

## Step 12 — 13:39 EDT — fast/slow task boundary
For `r=tau_s/tau_f`, `ell=L/tau_s`:

```math
X_D(r\ell)-rX_D(\ell)=0.
```

Task space can contain both-feasible, slow-only, and neither-feasible regions. At least one crossover exists under stated continuity/extreme-value assumptions.

## Step 13 — 13:50 EDT — direct correlated numerics; failed rough-grid result

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad a_x=2x^2e^{-2x}/\eta(x).
```

The finite hard-window scan is locally Brownian-like in ideal white noise.

**FAILED NUMERICAL ESTIMATE:** the apparent `ell~49` crossover moved under grid refinement and is invalid.

## Step 14 — 14:10 EDT — genuine finite information bandwidth
**REJECTED SHORTCUT:** an invertible common low-pass is not necessarily an information-band limit because whitening can undo it.

A genuine finite timing-information band removes the cusp.

## Step 15 — 14:18 EDT — smooth-band numerical validation
Use

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation has controlled grid behavior and agrees with Rice/EC at validation points.

## Step 16 — 14:33 EDT — exact Palm rare-event identity

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
}
```

with `lambda_u=L sigma/(2pi) exp(-u^2/2)`.

Rice/EC is therefore an upper bound; its error is multiple excursions plus endpoint overlap. Palm importance sampling makes `alpha=1e-6` tractable.

Validation at `kappa=8`, `r=1.2` gave Palm `ell_cross~0.5721 +/-0.001` versus Rice `0.57144`.

## Step 17 — 15:00 EDT — high-threshold law; nonuniform Rice limit; extreme speed ratio
A compact endpoint-retaining Rice law follows from the exact Palm structure for isolated excursions.

**REJECTED SHORTCUT:** small `alpha` does not justify deleting `Q(u)`.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is not uniform toward the rough limit.

For the co-scaled extreme-speed-ratio branch,

```math
L_\times\to\tau_f\ell_{crit,\kappa}.
```

## Step 18 — 15:22 EDT — one shared physical bandwidth, accessible SNR forced equal
Use `kappa_i=Omega_B tau_i`. With accessible SNR artificially fixed, the crossover changes from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no interior bandwidth optimum exists under this artificial normalization.

## Step 19 — 15:33 EDT — fixed physical signal/noise; finite bandwidth optimum
Remove SNR renormalization:

```math
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
\qquad \sigma^2=I_2/I_0.
```

Wide band:

```math
\rho_\infty=\rho_{full}[1-1/(2\kappa^2)+...],
```

```math
\sigma=1-2/(\sqrt\pi\kappa)+...
```

Thus SNR loss is `O(1/kappa^2)` while search simplification is `O(1/kappa)`.

**DERIVED / CONDITIONAL:** infinite bandwidth is suboptimal for the large-r Rice unknown-time objective whenever the full-band detector is strictly known-time feasible; a finite optimum exists.

Illustration: `kappa_opt^Rice~42.23`; Palm spot check preserved finite-candidate-over-infinite ordering.

## Step 20 — 16:12 EDT — finite-r common-bandwidth Rice double reversal
For common physical bandwidth without SNR renormalization,

```math
\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r
```

in the narrow-band limit, so slow gets a low-band SNR head start.

For

```text
r=2
rho_full=6.2407571
alpha=1e-6
beta=0.90
Lambda=0.895
```

finite-duration Rice gave

```text
kappa_cross_1^Rice ~=25.4898402
kappa_cross_2^Rice ~=130.1945883
```

and apparent topology `slow -> fast -> slow`. The spectral quadrature was converged.

**IMPORTANT:** Step 20 established a converged Rice-level numerical counterexample only; exact Palm validation remained open.

## Step 21 — 16:37 EDT — Palm correction changes the finite-r topology
Use the available-threshold formulation

```math
u_{avail}(x)=\rho(x)-\Phi^{-1}(\beta),
```

and test directly

```math
P_{FA}^{Palm}(u_{avail})\le\alpha.
```

### Lower switch
Refined Palm correction factors around the displaced equality are approximately

```text
C_fast ~0.994
C_slow ~0.952-0.956.
```

Two same-physical-time Palm balance solves plus a factor-of-two local-grid refinement give

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.}
```

This is about `15%` below Rice `25.49`.

**NUMERICAL VALIDATION / CONDITIONAL:** the lower slow-to-fast reversal survives.

### Upper Rice switch
At `kappa_f=130`:

```text
X=7.0:
  fast P_FA/alpha ~=0.9918 +/-0.0014
  slow P_FA/alpha ~=1.2668 +/-0.0079

X=7.5:
  fast P_FA/alpha ~=0.9897 +/-0.0014
  slow P_FA/alpha ~=1.0444 +/-0.0060
```

Thus fast is already feasible while slow is not.

Further checks:

```text
kappa_f=160, X=7.0:
  fast ~=0.9903 alpha
  slow ~=1.2565 alpha

kappa_f=300, X=6.5:
  fast ~=0.9950 alpha
  slow ~=1.7006 alpha
```

**INVALIDATED:** `kappa_cross_2^Rice ~=130.1945883` is not a continuous Palm switch.

Cause: nonuniform high-band Rice micro-upcrossing overcount. The shorter slow-detector finite window has the larger hard endpoint and much larger clustering correction.

A rough-limit high-threshold Pickands check also favors fast strongly, but does not rigorously exclude a different finite-alpha high-band switch.

### Corrected surviving topology
Directly Palm-validated through `kappa_f<=300`:

```math
\boxed{\text{slow}\to\text{fast}.}
```

**OPEN:** a different unobserved high-band Palm reversal is not rigorously excluded.

Full derivation: `PALM_CORRECTED_FINITE_R_BANDWIDTH_STEP.md`.  
Code: `numerics/finite_r_palm_validation.py`.

---

## Current stopping point

The Step-20 double reversal must not be propagated as an exact continuous-process result. The lower reversal survives; the reported upper Rice reversal is invalidated.

### Single natural next question

> Can the full Palm-corrected preference boundary in `(Lambda,kappa_f)` be mapped well enough to determine whether the high-band slow-preferred region disappears entirely, and whether the finite bandwidth optimum from Step 19 survives as a true Palm boundary maximum?
