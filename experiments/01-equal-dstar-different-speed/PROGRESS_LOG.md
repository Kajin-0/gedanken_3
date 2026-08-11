# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 15:33 EDT:** This log intentionally preserves every scientific milestone, correction, negative result, rejected shortcut, failed numerical estimate, numerical validation, asymptotic result, and stopping point. Full derivations live in dedicated step files.

---

## 2026-08-11 11:21 EDT — Step 01: scalar `D*` insufficiency
Equal reference `D*` with `tau_A=1 ns`, `tau_B=1 s` was tested in a physically allowed first-order + additive-output-noise model. The same 1 Hz tone gave `SNR_A/SNR_B ~ 6.36`.

**COUNTEREXAMPLE:** equal scalar reference `D*` does not guarantee equal SNR for arbitrary temporal signals.

**QUALIFICATION:** signal/noise filtering can cancel; no universal `fast is better` conclusion.

---

## 2026-08-11 11:32 EDT — Step 02: known-waveform full-observation SNR
Derived

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}\,df.
```

Complete magnitude `D*(f)` is sufficient for this restricted problem.

---

## 2026-08-11 12:02 EDT — Step 03: unknown timing negative result; finite truncation
**NEGATIVE RESULT:** equal complete `D*(f)` gives equal ideal stationary-Gaussian full-observation timing-search statistics.

Finite truncation can still distinguish detectors because magnitude `D*(f)` discards temporal phase/placement.

---

## 2026-08-11 12:09 EDT — Step 04: latency-compensated dispersion
A stable causal all-pass preserved complete magnitude `D*(f)` and infinite-time SNR while changing latency-compensated finite-window SNR.

**COUNTEREXAMPLE:** finite-window insufficiency is not merely a pure-delay artifact.

---

## 2026-08-11 12:18 EDT — Step 05: exact finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

Eventual detectability and rate of access to it are distinct.

---

## 2026-08-11 12:30 EDT — Step 06: detection probability by deadline

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

---

## 2026-08-11 12:38 EDT — Step 07: independent-slot timing search

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

**WARNING:** `M` is not digital sample count in a continuous timing scan.

---

## 2026-08-11 12:47 EDT — Step 08: continuous timing covariance
Derived the correlated timing scan from the noise-whitened template. When the second spectral moment exists, RMS timing frequency controls local curvature and Rice upcrossing density.

**REFINEMENT:** sample rate alone does not set timing-search complexity.

---

## 2026-08-11 13:01 EDT — Step 09: finite-deadline correction and ranking reversal
The actual finite search must use `q_t=C_t^-1s_t` and its own covariance.

**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be combined directly with full-template timing bandwidth.

Constructed

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members acquire SNR sooner but can pay a larger unknown-time search penalty; ranking can reverse.

---

## 2026-08-11 13:18 EDT — Step 10: task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

Task-level, not a detector scalar.

---

## 2026-08-11 13:28 EDT — Step 11: dimensionless collapse; integration-time negative result

```math
\mathcal T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Pointwise covariance ordering plus Slepian comparison makes search threshold nonincreasing with filter duration while SNR rises.

**NEGATIVE RESULT:** no finite interior `t_opt`; use all data allowed by the deadline.

---

## 2026-08-11 13:39 EDT — Step 12: fast/slow task-regime boundary
For `r=tau_s/tau_f`,

```math
X_D(r\ell)-rX_D(\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time boundary.

Task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one crossover exists under stated conditions; uniqueness remains open.

---

## 2026-08-11 13:50 EDT — Step 13: direct correlated-scan prototype and continuum obstruction
Direct FFT moving-average Monte Carlo reproduced the broad regime structure but the apparent crossover moved with timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic `ell ~ 49` is not continuum-converged and must never be quoted.

Exact cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
a_x=2x^2e^{-2x}/\eta(x),
```

so the finite hard-window scan is locally Brownian-like in ideal white noise.

---

## 2026-08-11 14:10 EDT — Step 14: genuine finite information bandwidth
**REJECTED SHORTCUT:** an invertible noiseless common low-pass is not necessarily an information-band limit because whitening can undo it.

A true finite timing-information spectrum removes the cusp. For fixed dimensionless `kappa=Omega_B tau`, the scaled task structure survives.

---

## 2026-08-11 14:18 EDT — Step 15: smooth-band numerical validation
Use

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation is stable under practical timing-grid refinement and compatible with Rice/EC at validation points.

For `rho_0=5`, `r=1.2`, `alpha=0.01`, `beta=0.90`, Rice showed the approximate trend

```text
kappa:       2     4     8     16    32
ell_cross: 75.56 61.58 54.75 51.43 49.89
```

**CONDITIONAL TREND:** more timing bandwidth moved the switch to smaller `L/tau_s` in this tested model. These were not exact phase boundaries.

---

## 2026-08-11 14:33 EDT — Step 16: Palm rare-event method at `alpha=1e-6`
Derived

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\left[
\frac{1_{z(0)\le u}}{N_u^+}
\right]
}
```

with

```math
\lambda_u=L\sigma(2\pi)^{-1}e^{-u^2/2}.
```

Rice/EC is therefore an upper bound; its error is multiple excursions plus endpoint overlap.

A first point-exceedance importance sampler efficiently solved the grid maximum but retained finite-grid continuum bias; this was preserved as a valid discretized method, not mistaken for the continuous result.

For `rho_0=6.2`, `r=1.2`, `alpha=1e-6`, `beta=0.90`, `kappa=8`, Palm gave `ell_cross ~=0.5721 +/-0.001`; Rice gave `0.57144`.

---

## 2026-08-11 15:00 EDT — Step 17: high-threshold law and extreme speed ratio
Derived the exact smooth Palm-corrected crossover identity

```math
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
```

**REJECTED SHORTCUT:** small `alpha` does not justify dropping the endpoint `Q(u)` term.

For finite hard windows,

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi,
```

so Rice accuracy is nonuniform toward the rough limit.

Extreme-speed-ratio branch:

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}}.
```

**REFINEMENT:** bandwidth and speed-ratio limits do not commute.

---

## 2026-08-11 15:22 EDT — Step 18: one shared physical electronics bandwidth
Set

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

Equal accessible eventual SNR was still imposed to isolate timing/search effects.

**REFINEMENT:** the clean large-`r` limit requires `ell_crit(kappa_f)/r -> 0`; `r->infinity` alone is insufficient if `kappa_f` simultaneously vanishes.

Under that condition,

```math
L_\times\to\tau_f\ell_{crit}(\Omega_B\tau_f).
```

Two high-threshold regimes:

```math
L_\times\sim1/\Omega_B
```

when electronics limits timing, and

```math
L_\times\sim\tau_f
```

when readout is wide.

**NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum appears while accessible eventual SNR is artificially held fixed.

---

## 2026-08-11 15:33 EDT — Step 19: fixed physical signal/noise and finite bandwidth optimum

### Model change
Stop renormalizing eventual SNR as bandwidth changes. Let `rho_full` be the unregularized full-template SNR and use

```math
I_0(\kappa)=\int\frac{e^{-(\nu/\kappa)^2}}{(1+\nu^2)^2}d\nu,
```

```math
I_2(\kappa)=\int\frac{\nu^2e^{-(\nu/\kappa)^2}}{(1+\nu^2)^2}d\nu.
```

Then

```math
F(\kappa)=I_0/(\pi/2),
\qquad
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
```

and

```math
\sigma^2(\kappa)=I_2/I_0.
```

Exact Gaussian-weight forms were derived with `q=1/kappa`, `E=e^{q^2}erfc(q)`:

```math
I_0=\pi E(1/2-q^2)+\sqrt\pi q,
```

```math
I_2=\pi E(1/2+q^2)-\sqrt\pi q.
```

### Narrow-band result
Accessible SNR vanishes as

```math
\rho_\infty(\kappa)
\sim\rho_{full}\sqrt{2\kappa/\sqrt\pi},
```

so a finite minimum bandwidth is required even for known-time feasibility.

### Wide-band asymptotics

```math
\rho_\infty(\kappa)
=\rho_{full}[1-1/(2\kappa^2)+O(\kappa^{-3})],
```

while

```math
\sigma(\kappa)
=1-2/(\sqrt\pi\kappa)+O(\kappa^{-2}).
```

Therefore the finite-band SNR penalty is only `O(kappa^-2)` while the reduction in timing-search curvature is `O(kappa^-1)`.

For the large-`r` full-template Rice feasibility/crossover objective,

```math
\boxed{
\ell_{crit}^{Rice}(\kappa)
=\ell_{crit}^{Rice}(\infty)
[1+2/(\sqrt\pi\kappa)+O(\kappa^{-2})].
}
```

Thus sufficiently large but finite bandwidth beats infinite bandwidth. Because sufficiently narrow bandwidth is infeasible, continuity forces at least one finite optimum whenever the full-band detector is strictly known-time feasible.

**DERIVED / CONDITIONAL:** a genuine finite readout-bandwidth optimum exists for this objective in the chosen fixed-physics Gaussian information-band model.

### Step-16-calibrated illustration
Choose fixed `rho_full ~=6.240757` so the accessible SNR at `kappa=8` remains `6.2`, with `alpha=1e-6`, `beta=0.90`.

```text
known-time feasibility onset: kappa_min ~=3.14545
Rice optimum:               kappa_opt ~=42.23
ell_crit at optimum:        ~=0.90083
infinite-band ell_crit:     ~=0.88906
Rice gain:                  ~=1.32%
```

For `tau_f=1 ns`, the model translates this to `f_B,opt ~=6.72 GHz` and `L_cross,opt ~=0.901 ns`; these are not hardware recommendations.

### Palm spot check
A `10000`-path Palm check at the finite candidate and at the unregularized full-template limit preserved the finite-candidate-over-infinite ordering. The implied corrected feasibility lengths were approximately `0.91097` and `0.90915`, respectively.

**QUALIFICATION:** this is a spot check, not an exact Palm optimization; the exact optimum location and uniqueness remain open.

Full derivation: `PHYSICAL_BANDWIDTH_OPTIMUM_STEP.md`.  
Calculator: `numerics/physical_bandwidth_optimum.py`.

### Next question, held open
Does the finite bandwidth optimum survive at finite speed ratio when one common physical bandwidth simultaneously changes both detectors' accessible SNR and timing-search covariance, and can bandwidth sweeping produce multiple preference reversals?
