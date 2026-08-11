# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 15:33 EDT  
**Status:** nineteen logical steps completed. Step 19 removes the artificial equal-accessible-SNR normalization and holds the underlying detector signal/noise fixed while readout bandwidth varies. In the large-speed-ratio full-fast-template high-threshold problem, a genuine finite readout-bandwidth optimum necessarily appears in the chosen Gaussian information-band model whenever the full-band detector is strictly task-feasible. No universal replacement metric and no novelty claim.

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

### Steps 01–04 — what equal `D*` does and does not guarantee

- Equal reference scalar `D*` does not guarantee equal SNR for arbitrary temporal signals; the explicit 1 Hz counterexample gave `SNR_A/SNR_B ~ 6.36`.
- Complete magnitude `D*(f)` is sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem:

```math
\rho_\infty^2
=\int |P|^2|G|^2/S_n\,df
=\frac1A\int|P|^2D^{*2}\,df.
```

- **NEGATIVE RESULT:** unknown arrival time alone does not break that ideal stationary-Gaussian full-observation equivalence.
- Finite windows can break it because magnitude `D*(f)` discards temporal phase/placement; a stable causal all-pass construction removes the pure-delay loophole.

### Steps 05–08 — finite-time SNR and timing search

Exact finite-record linear SNR:

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle.
```

Known-time Gaussian detection:

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold governed by the timing-scan covariance, not digital sample count. When the noise-weighted timing spectrum has finite second moment, local covariance curvature and Rice upcrossing density are controlled by its RMS timing frequency.

### Step 09 — finite-deadline correction and conditional ranking reversal

The actual finite search must use

```math
q_t=C_t^{-1}s_t
```

and its own covariance.

**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be mixed with full-template timing bandwidth as one exact finite-deadline statistic.

Controlled equal-eventual-SNR family:

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

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in that family; use all data allowed by the deadline.

For `r=tau_s/tau_f` and `ell=L/tau_s`, the fast/slow boundary is

```math
X_D(r\ell)-rX_D(\ell)=0.
```

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. At least one crossover exists under the stated continuity/extreme-value assumptions; uniqueness remains open.

### Step 13 — failed rough-grid crossover

Direct correlated Monte Carlo reproduced the broad regime structure, but the apparent crossover moved with timing-grid refinement.

**FAILED NUMERICAL ESTIMATE:** diagnostic `ell ~ 49` is invalid and must never be quoted as a continuous-time result.

Exact cause:

```math
R_x(y)=1-a_x|y|+O(y^2),
\qquad
 a_x=\frac{2x^2e^{-2x}}{\eta(x)},
```

so the finite hard-window scan in ideal white noise is locally Brownian-like / mean-square nondifferentiable.

### Steps 14–15 — genuine finite information bandwidth

**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening can undo it.

Use a genuine smooth information penalty

```math
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Finite `kappa` removes the covariance cusp. Direct correlated FFT simulation has controlled timing-grid behavior and agrees with Rice/Euler-characteristic predictions at validation points.

### Step 16 — exact Palm rare-event identity

For a differentiable stationary Gaussian scan,

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

Therefore Rice/EC is an upper bound; its error comes exactly from multiple high excursions and endpoint/upcrossing overlap. A Palm sampler makes `alpha=1e-6` tractable with thousands of paths.

Validation task:

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8
```

gave `ell_cross^Palm ~= 0.5721 +/- 0.001` versus Rice `0.57144`.

### Step 17 — high-threshold crossover law and extreme speed ratio

The exact smooth Palm-corrected crossover is

```math
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
```

For isolated excursions `C_s,C_f~1`, this gives a compact endpoint-retaining Rice law.

**REJECTED SHORTCUT:** small `alpha` does not justify dropping `Q(u)`; in the Step-16 task the endpoint term consumes about half the false-alarm budget.

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

### Step 18 — one shared physical electronics bandwidth

Use one physical information scale:

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s.
```

Step 18 still forced equal accessible eventual SNR to isolate timing/search effects.

**REFINEMENT:** the clean large-`r` fast-feasibility-edge limit requires `ell_crit(kappa_f)/r -> 0`; `r->infinity` alone is insufficient if `kappa_f` simultaneously collapses.

Under that condition,

```math
\boxed{
L_\times\to\tau_f\ell_{crit}(\Omega_B\tau_f).
}
```

With equal accessible SNR, the high-threshold crossover changes from

```math
L_\times\sim1/\Omega_B
```

when electronics is limiting to

```math
L_\times\sim\tau_f
```

when the readout is wide.

**NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum exists while accessible eventual SNR is artificially held fixed.

### Step 19 — fixed physical signal/noise; finite bandwidth optimum

Remove the Step-18 SNR renormalization. Let `rho_full` be the unregularized full-template eventual SNR and define

```math
I_0(\kappa)
=\int\frac{e^{-(\nu/\kappa)^2}}{(1+\nu^2)^2}d\nu,
```

```math
I_2(\kappa)
=\int\frac{\nu^2e^{-(\nu/\kappa)^2}}{(1+\nu^2)^2}d\nu.
```

Then

```math
\boxed{
F(\kappa)=I_0/(\pi/2),
\qquad
\rho_\infty(\kappa)=\rho_{full}\sqrt{F(\kappa)},
}
```

and

```math
\boxed{
\sigma^2(\kappa)=I_2/I_0.
}
```

Exact Gaussian-weight forms with `q=1/kappa` and `E=e^{q^2}erfc(q)` are

```math
I_0=\pi E(1/2-q^2)+\sqrt\pi q,
```

```math
I_2=\pi E(1/2+q^2)-\sqrt\pi q.
```

Known-time feasibility requires

```math
\rho_\infty(\kappa)>
\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta).
```

Hence sufficiently narrow bandwidth is infeasible.

For the large-`r` full-fast-template isolated-excursion objective,

```math
\ell_{crit}^{Rice}(\kappa)
=
\frac{2\pi[\alpha-Q(u(\kappa))]e^{u(\kappa)^2/2}}
{\sigma(\kappa)},
```

with

```math
u(\kappa)=\rho_{full}\sqrt{F(\kappa)}-\Phi^{-1}(\beta).
```

Wide-band asymptotics:

```math
\rho_\infty(\kappa)
=\rho_{full}\left[1-\frac1{2\kappa^2}+O(\kappa^{-3})\right],
```

but

```math
\sigma(\kappa)
=1-\frac{2}{\sqrt\pi\kappa}+O(\kappa^{-2}).
```

Therefore

```math
\boxed{
\ell_{crit}^{Rice}(\kappa)
=
\ell_{crit}^{Rice}(\infty)
\left[1+\frac{2}{\sqrt\pi\kappa}+O(\kappa^{-2})\right].
}
```

**DERIVED / CONDITIONAL:** if the full-band detector is strictly known-time feasible, infinite bandwidth is suboptimal for this unknown-time objective and at least one finite `kappa_opt` must exist. The finite-band search-complexity benefit is `O(1/kappa)`, while SNR loss is only `O(1/kappa^2)` near the wide-band limit; stronger narrowing eventually loses enough SNR to destroy feasibility.

Step-16-calibrated illustration: choose fixed `rho_full ~= 6.240757` so `rho_infinity(8)=6.2`, with `alpha=1e-6`, `beta=0.90`.

```text
kappa_min ~= 3.14545
kappa_opt^Rice ~= 42.23
ell_crit^Rice(kappa_opt) ~= 0.90083
ell_crit^Rice(infinity) ~= 0.88906
Rice gain ~= 1.32%
```

For `tau_f=1 ns`, this corresponds in the model to `f_B,opt ~= 6.72 GHz` and `L_cross,opt ~= 0.901 ns`; these are not hardware recommendations.

A `10000`-path Palm spot check preserves the finite-candidate-over-infinite ordering, but the exact Palm-optimal bandwidth has not been solved.

See `PHYSICAL_BANDWIDTH_OPTIMUM_STEP.md` and `numerics/physical_bandwidth_optimum.py`.

---

## 3. Current frontier

A true finite readout-bandwidth optimum now exists for one well-defined task objective:

```text
maximize the large-r fast detector's tolerable unknown-arrival interval /
fast-to-slow crossover under fixed physical signal and noise.
```

The next unresolved issue is whether this optimum survives at finite speed ratio, where changing one common physical bandwidth simultaneously changes both detectors' accessible SNR and search covariance.

---

## 4. What is established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make phase/temporal placement operationally relevant.
- Finite SNR and timing search must come from the same finite measurement problem.
- The controlled family admits a conditional fast/slow ranking reversal and task-regime boundary.
- **NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.
- **FAILED NUMERICAL ESTIMATE:** the Step-13 rough-grid `ell~49` crossover is invalid.
- Genuine finite information bandwidth removes the hard-window cusp without removing the task-regime mechanism.
- Smooth scans admit efficient Palm rare-event evaluation at `alpha=1e-6`.
- **DERIVED:** Rice accuracy is nonuniform toward the finite-window rough limit.
- **DERIVED / ASYMPTOTIC:** extreme speed ratio reduces the crossover to the fast detector's full-template feasibility edge.
- **DERIVED / ASYMPTOTIC:** shared physical electronics introduces an electronics-limited `1/Omega_B` regime.
- **NEGATIVE RESULT:** no bandwidth optimum exists if eventual accessible SNR is artificially renormalized to remain fixed.
- **DERIVED / CONDITIONAL:** restoring physical SNR loss produces a genuine finite bandwidth optimum for the large-`r` crossover/feasibility objective in the Gaussian information-band model.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover or bandwidth-optimum uniqueness for arbitrary parameters.
- No exact rough finite-`r`, infinite-bandwidth crossover.
- No claim that the Gaussian information weighting is a literal circuit transfer function.
- No claim that the illustrative GHz values are hardware recommendations.
- No proof yet of a finite exact-Palm optimum for every strictly feasible task.
- No proof that the bandwidth maximizing `L_cross` also minimizes detection time for every fixed `L`.
- No finite-`r` common-bandwidth optimization with both detectors' SNR changing yet.
- No exact global-rejection/localization surface, Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single next question — DO NOT ANSWER YET

> Does the finite readout-bandwidth optimum survive when the speed ratio is finite and the same physical bandwidth simultaneously changes both detectors' accessible SNR and timing-search covariance, and can that produce multiple fast/slow preference reversals as bandwidth is swept?
