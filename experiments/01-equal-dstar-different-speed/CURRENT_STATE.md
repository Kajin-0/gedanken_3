# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 15:22 EDT  
**Status:** eighteen logical steps completed. Step 18 replaces the similarity-preserving equal-`kappa` readout with one shared physical information bandwidth `Omega_B`, derives the corresponding large-speed-ratio crossover, and identifies an electronics-limited regime in which making the detector intrinsically faster no longer moves the task boundary. No universal replacement metric and no novelty claim.

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

### Step 01 — scalar reference `D*` insufficiency
A physically allowed first-order response with additive output noise gives unequal temporal-signal SNR despite equal reference `D*`; the explicit 1 Hz example gives `SNR_A/SNR_B ~ 6.36`.

**QUALIFICATION:** signal/noise filtering can cancel. Do not infer `fast is always better`.

### Step 02 — full-observation known-waveform SNR

```math
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation problem.

### Step 03 — unknown timing negative result; finite truncation failure
**NEGATIVE RESULT:** identical complete `D*(f)` gives identical stationary-Gaussian full-observation timing-search statistics. Finite truncation can break equivalence because magnitude `D*(f)` discards phase/temporal placement.

### Step 04 — pure-delay loophole removed
A stable causal all-pass factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing latency-compensated finite-window SNR.

### Step 05 — exact finite-time SNR

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
\qquad
\eta(t)=\rho_t^2/\rho_\infty^2.
```

### Step 06 — known-time Gaussian decision

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

### Step 07 — independent-slot timing-search penalty

```math
\gamma_{M,\alpha}=\Phi^{-1}[(1-\alpha)^{1/M}].
```

`M` is not digital sample count in a continuous timing scan.

### Step 08 — continuous timing-search covariance
The timing scan is governed by the autocorrelation of the noise-whitened template. When the second spectral moment exists, its RMS timing frequency controls local curvature and Rice upcrossing density.

**REFINEMENT:** digital sample rate alone does not determine timing-search complexity.

### Step 09 — finite-deadline correction and conditional ranking reversal
The finite search must use

```math
q_t=C_t^{-1}s_t
```

and its own covariance.

**REJECTED SHORTCUT:** finite-window `eta(t)` cannot be combined directly with full-template `f_rms` as one exact finite-deadline statistic.

A controlled equal-eventual-SNR family was introduced:

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2},
\qquad
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

Faster members accumulate more finite-time SNR but can face a larger fixed-physical-`L` unknown-time search burden. A cross-detector ranking reversal can occur.

### Step 10 — task-level detection-time surface

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t>0:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

This is task-level, not a detector-only replacement for `D*`.

### Step 11 — dimensionless collapse; no finite interior integration optimum
For the scaled family,

```math
\mathcal T_D
=\tau X_D(\rho_0,\alpha,\beta,L/\tau).
```

Pointwise covariance ordering plus Slepian comparison makes the global search threshold nonincreasing with filter duration while SNR rises strictly.

**NEGATIVE RESULT:** no finite interior `t_opt` in this family; use all data allowed by the deadline.

### Step 12 — exact fast/slow task-regime boundary
For

```math
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s,
```

the exact preference boundary is

```math
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
```

**REJECTED SHORTCUT:** asymptotic-margin equality is not the minimum-decision-time boundary.

Task space has both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR. Under standard conditions at least one fast-to-slow crossover exists; uniqueness remains open.

### Step 13 — direct correlated-scan numerics; continuum obstruction
A direct FFT moving-average Monte Carlo simulated the correlated grid-sampled finite-duration scan without independent-trials replacement.

**FAILED NUMERICAL ESTIMATE:** diagnostic crossover values around `ell ~ 49` moved under timing-grid refinement and must never be quoted as continuous-time results.

The exact finite hard-window covariance has

```math
\boxed{
a_x=-R_x'(0^+)=\frac{2x^2e^{-2x}}{\eta(x)}}
```

and

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so the ideal-white-noise finite scan is locally Brownian-like / mean-square nondifferentiable.

### Step 14 — genuine finite information bandwidth
**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening can cancel it.

A genuine finite information band gives finite timing-spectrum second moment and removes the Step-13 cusp. For a similarity-preserving family with fixed

```math
\kappa=\Omega_B\tau,
```

the scaled task boundary survives.

### Step 15 — smooth-band numerical validation
Use the explicit smooth information weighting

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
```

Direct correlated FFT simulation is stable under practical timing-grid refinement and agrees with Rice/Euler-characteristic predictions at moderate validation points.

**CONDITIONAL TREND:** increasing accessible high-frequency timing information moves the fast-to-slow crossover to smaller `L/tau_s` in the tested regularization.

### Step 16 — rare-event Palm/upcrossing method
For a differentiable stationary Gaussian timing scan,

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right],
}
```

with

```math
\lambda_u=L\frac{\sigma}{2\pi}e^{-u^2/2}.
```

Therefore the first-order Rice/EC expression is an upper bound; its error is exactly multiple high excursions plus endpoint/upcrossing overlap.

For the validation task

```text
rho_0=6.2
r=1.2
alpha=1e-6
beta=0.90
kappa=8,
```

Palm gives `ell_cross ~= 0.5721 +/- 0.001`; Rice gives `0.57144`.

### Step 17 — endpoint-retaining high-threshold law and extreme-speed-ratio asymptote
The exact smooth Palm-corrected crossover is

```math
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}{\sigma_f C_f}
=r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}{\sigma_s C_s}.
```

For isolated excursions `C_s,C_f~1`, this gives the endpoint-retaining Rice law.

**REJECTED SHORTCUT:** small `alpha` does not imply `Q(u)<<alpha`; in the Step-16 task the endpoint term uses roughly half the false-alarm budget.

For finite hard-window duration,

```math
\sigma_\kappa^2(x)
\sim\frac{a_x}{\sqrt\pi}\kappa
\qquad(\kappa\to\infty),
```

so Rice accuracy cannot remain uniform into the Step-13 rough limit.

For the co-scaled extreme-speed-ratio branch, defining the fast full-template feasibility edge by

```math
\Gamma_{\infty,\kappa}(\ell_{crit,\kappa},\alpha)
=\rho_0-\Phi^{-1}(\beta),
```

gives

```math
\boxed{r\ell_\times\to\ell_{crit,\kappa}},
```

and physically

```math
\boxed{L_\times\to\tau_f\ell_{crit,\kappa}}.
```

### Step 18 — one shared physical electronics bandwidth
Now impose

```math
\Omega_{B,f}=\Omega_{B,s}=\Omega_B,
```

so

```math
\boxed{\kappa_f=\Omega_B\tau_f,}
```

```math
\boxed{\kappa_s=\Omega_B\tau_s=r\kappa_f.}
```

The comparison is still normalized to equal **accessible eventual SNR** `rho_0` to isolate timing/search effects.

The finite-`r` Palm/Rice crossover identity survives but the two detectors are evaluated at different `kappa`.

**REFINEMENT:** `r->infinity` alone is not enough if `kappa_f` is simultaneously allowed to vanish. The clean one-edge limit requires

```math
\ell_{crit}(\kappa_f)/r\to0,
```

which in the electronics-limited regime is equivalent to requiring the slow detector's dimensionless electronics bandwidth `kappa_s=r kappa_f` to become large.

Under that condition,

```math
\boxed{
L_\times
\to
\tau_f\ell_{crit}(\Omega_B\tau_f).
}
```

For the full-template Gaussian information-band model,

```math
\sigma_\infty^2(\kappa)
=
\frac{\int \nu^2(1+\nu^2)^{-2}e^{-(\nu/\kappa)^2}d\nu}
{\int (1+\nu^2)^{-2}e^{-(\nu/\kappa)^2}d\nu}
```

is strictly increasing with `kappa`. Writing `s=kappa^-2` gives

```math
\frac{d}{ds}\sigma_\infty^2
=-\operatorname{Var}_s(\nu^2)<0.
```

In the isolated-excursion Rice limit define

```math
\mathcal C
=2\pi[\alpha-Q(u_\infty)]e^{u_\infty^2/2},
\qquad
u_\infty=\rho_0-\Phi^{-1}(\beta).
```

Then

```math
\boxed{
L_\times^{Rice}
\sim
\tau_f\frac{\mathcal C}
{\sigma_\infty(\Omega_B\tau_f)}.
}
```

Two physical regimes follow:

```math
\boxed{
L_\times^{Rice}
\sim\frac{\sqrt2\,\mathcal C}{\Omega_B},
\qquad
\Omega_B\tau_f\ll1,
}
```

and

```math
\boxed{
L_\times^{Rice}
\to\mathcal C\tau_f,
\qquad
\Omega_B\tau_f\gg1.
}
```

**FIRST NONTRIVIAL CONSEQUENCE:** once the detector is much faster than the accessible electronics, making the intrinsic detector still faster no longer moves the crossover at leading order; the task boundary becomes electronics-limited.

**NEGATIVE RESULT / QUALIFICATION:** under the equal-accessible-eventual-SNR normalization, bandwidth moves the boundary monotonically and produces no interior bandwidth optimum. A genuine physical optimum remains open because changing real bandwidth would ordinarily change eventual SNR as well.

See `FIXED_PHYSICAL_BANDWIDTH_STEP.md` and `numerics/fixed_physical_bandwidth.py`.

---

## 3. Current frontier

The project now contains two distinct finite-bandwidth branches:

```text
co-scaled bandwidth:
    kappa_f = kappa_s
    -> exact similarity structure

shared physical bandwidth:
    kappa_i = Omega_B tau_i
    -> detector/electronics timescale competition
```

The most important new physical scale hierarchy is

```text
intrinsic fast-detector time tau_f
versus
electronics information time 1/Omega_B.
```

The next unresolved branch is to stop renormalizing the eventual SNR when bandwidth changes.

---

## 4. What is established

- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR.
- Complete `D*(f)` is sufficient only for the restricted full-observation known-waveform problem.
- Finite observation can make phase/temporal placement operationally relevant.
- Finite SNR and timing search must come from the same finite measurement problem.
- The controlled equal-eventual-SNR family admits a conditional fast/slow ranking reversal and task-regime boundary.
- **NEGATIVE RESULT:** no finite interior filter-duration optimum exists in the original scaled family.
- **FAILED NUMERICAL ESTIMATE:** the Step-13 rough-grid `ell~49` crossover is invalid.
- Genuine finite information bandwidth removes the hard-window cusp without removing the task-regime mechanism.
- Smooth finite-band scans admit efficient Palm rare-event evaluation at `alpha=1e-6`.
- **DERIVED:** Rice accuracy is nonuniform as finite-window timing bandwidth tends to infinity.
- **DERIVED / ASYMPTOTIC:** the extreme-speed-ratio crossover approaches the fast full-template feasibility edge.
- **DERIVED / ASYMPTOTIC:** with shared physical electronics, the crossover changes from `~1/Omega_B` to `~tau_f` as the electronics changes from limiting to wide-band.
- **NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum appears while eventual accessible SNR is artificially held fixed.

---

## 5. What is not established

- No universal statement that faster detectors are better or worse.
- No universal speed-detectivity tradeoff or scalar replacement for `D*`.
- No proof of crossover uniqueness for all parameters.
- No exact rough finite-`r`, infinite-bandwidth crossover.
- No claim that the Gaussian information weighting is a literal circuit transfer function.
- No claim that the illustrative Step-18 bandwidth numbers are real detector predictions.
- No true bandwidth optimum for a fixed physical detector with `rho_infinity(Omega_B)` allowed to vary.
- No exact global-rejection/localization surface, Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 6. Single natural next question — DO NOT ANSWER YET

> If the physical detector signal and noise amplitudes are held fixed while `Omega_B` is varied—so reducing bandwidth can reduce eventual SNR as well as timing-search burden—does their competition produce a genuine finite optimal readout bandwidth for unknown-time detection?
