# Step 14 — Finite-Bandwidth Regularization and Survival of the Task Boundary

**Date:** 2026-08-11 14:10 EDT  
**Status:** DERIVED / REFINEMENT / REJECTED SHORTCUT. A true finite accessible measurement bandwidth removes the Step-13 covariance cusp and makes every finite-duration timing scan mean-square differentiable. Merely appending a noiseless invertible low-pass to both signal and noise does **not** necessarily regularize optimal detection because whitening can undo it; the bandwidth restriction must represent genuine loss of accessible high-frequency information or an equivalent processing constraint. For a co-scaled finite-bandwidth version of the Step-09 family, the dimensionless task structure and fast/slow regime boundary survive with one additional dimensionless bandwidth parameter. No numerical crossover is claimed and no novelty claim is made.

---

## 1. Question

Step 13 showed that the exact finite hard-window scan in ideal white noise has

```math
R_x(y)=1-a_x|y|+O(y^2),
```

so it is locally Brownian-like and a naive timing grid converges slowly to the continuous supremum.

The next question is:

> Can a physically finite measurement/readout bandwidth regularize the continuous scan in a controlled way, and does the fast/slow task boundary survive?

The clean answer is **yes**, provided `finite bandwidth` means a true limitation on accessible high-frequency information rather than a merely invertible common filter.

---

## 2. REJECTED SHORTCUT — an invertible noiseless low-pass is not enough

Suppose a common LTI transfer `F(f)` is appended after the detector and acts on both the deterministic signal and all of the relevant additive noise:

```math
S(f)\to F(f)S(f),
```

```math
S_n(f)\to |F(f)|^2S_n(f).
```

Where `F(f)` is nonzero,

```math
\frac{|F(f)S(f)|^2}{|F(f)|^2S_n(f)}
=
\frac{|S(f)|^2}{S_n(f)}.
```

Thus the full-observation noise-whitened signal spectrum is unchanged in magnitude. An optimal detector that knows `F` can whiten/deconvolve the common attenuation.

Therefore the statement

```text
add any low-pass pole -> statistical timing bandwidth is finite
```

is false in this ideal information-theoretic sense.

**REJECTED SHORTCUT:** an invertible noiseless common low-pass does not by itself constitute a genuine information-bandwidth limit.

A physical regularization must instead contain at least one of the following:

- true inaccessible frequency support / anti-alias measurement band;
- irreducible out-of-band noise that prevents deconvolution from recovering useful SNR;
- an explicit bandwidth constraint on admissible processing;
- another mechanism that makes the noise-weighted timing spectrum have a finite second moment.

The remainder uses the cleanest exact model: a true accessible measurement band.

---

## 3. True finite accessible bandwidth

Use angular frequency `omega` and assume the finite-duration search statistic can access only

```math
|\omega|\le\Omega_B.
```

Let `q_{t,B}` be the optimal finite-record filter within that actual accessible measurement space, with transform `Q_{t,B}(omega)`, and let the accessible noise PSD be `S_{n,B}(omega)`.

The normalized noise-only timing-scan covariance is

```math
\boxed{
r_{t,B}(\Delta)
=
\frac{
\int_{-\Omega_B}^{\Omega_B}
|Q_{t,B}(\omega)|^2S_{n,B}(\omega)e^{i\omega\Delta}d\omega
}{
\int_{-\Omega_B}^{\Omega_B}
|Q_{t,B}(\omega)|^2S_{n,B}(\omega)d\omega
}.
}
```

Define the normalized scan spectral weight

```math
W_{t,B}(\omega)
=
\frac{|Q_{t,B}(\omega)|^2S_{n,B}(\omega)}
{\int |Q_{t,B}|^2S_{n,B}d\omega}.
```

It has compact support in `[-Omega_B,Omega_B]`.

---

## 4. Exact removal of the cusp

Because the scan spectral weight has compact support, all spectral moments are finite. In particular,

```math
r_{t,B}'(0)=0
```

for the real stationary scan, and

```math
\boxed{
-r_{t,B}''(0)
=
\int \omega^2W_{t,B}(\omega)d\omega
\le
\Omega_B^2.
}
```

Hence near zero lag

```math
\boxed{
r_{t,B}(\Delta)
=
1-
\frac12\sigma_{\omega,t,B}^2\Delta^2
+o(\Delta^2),
}
```

where

```math
\sigma_{\omega,t,B}^2
=\int\omega^2W_{t,B}(\omega)d\omega.
```

The linear `|Delta|` cusp from Step 13 is gone.

Equivalently,

```math
E[(z(t+h)-z(t))^2]
=
\sigma_{\omega,t,B}^2h^2+o(h^2),
```

so the finite-duration timing scan is mean-square differentiable.

For a differentiable unit-variance stationary Gaussian scan, Rice's exact mean upcrossing density is again available:

```math
\boxed{
\nu_u^+
=
\frac{\sigma_{\omega,t,B}}{2\pi}
 e^{-u^2/2}.
}
```

Thus a true finite measurement bandwidth converts the Step-13 locally Brownian finite-window process back into the smooth-process class.

---

## 5. What Step 13 was really telling us

Step 13's cusp was not a numerical artifact. It was the exact consequence of combining:

```text
hard finite decision window
+
ideal white noise extending to arbitrarily high frequency
+
no true information-bandwidth constraint.
```

Step 14 shows that the cusp is also **not physically unavoidable**.

A real measurement chain with genuine finite accessible information bandwidth, or any model whose scan spectrum has finite second moment, removes the singularity.

Therefore the correct interpretation is:

**REFINEMENT:** the Step-13 rough scan is a legitimate limiting idealization and must be handled correctly if used, but it should not automatically be treated as the generic finite-bandwidth photodetector case.

---

## 6. Add the bandwidth as a dimensionless task parameter

Return to the Step-09 time-scaled detector family. Introduce the dimensionless accessible angular bandwidth

```math
\boxed{
\kappa\equiv\Omega_B\tau.
}
```

For the cleanest similarity-preserving regularized family, hold `kappa` fixed as `tau` changes, i.e.

```math
\Omega_B=\kappa/\tau.
```

Also normalize the amplitudes so every regularized family member retains the same **band-limited eventual matched-filter SNR**

```math
\rho_{\infty,B}=\rho_0.
```

Under the time change

```math
x=t/\tau,
\qquad
\ell=L/\tau,
\qquad
\nu=\omega\tau,
```

both the finite-record covariance operator and its accessible frequency interval scale into a dimensionless problem on

```math
|\nu|\le\kappa.
```

Therefore the regularized finite-time SNR, scan covariance, and threshold have the forms

```math
\rho_{\tau,t,B}
=\rho_0\,\mathcal R_\kappa(x),
```

```math
r_{\tau,t,B}(\Delta)
=R_{x,\kappa}(|\Delta|/\tau),
```

```math
\boxed{
\gamma_{\tau,t,B}(L,\alpha)
=\Gamma_\kappa(x,\ell,\alpha).
}
```

The dimensionless task margin is

```math
\boxed{
M_\kappa(x;\ell,\rho_0,\alpha)
=
\rho_0\mathcal R_\kappa(x)
-
\Gamma_\kappa(x,\ell,\alpha).
}
```

No explicit closed form for `R_kappa(x)` or `Gamma_kappa` is asserted here; the point is the exact scaling structure.

---

## 7. Regularized detection-time surface

Define

```math
X_{D,\kappa}(\rho_0,\alpha,\beta,\ell)
=
\inf\left\{
x>0:
M_\kappa(x;\ell,\rho_0,\alpha)
\ge\Phi^{-1}(\beta)
\right\}.
```

Then

```math
\boxed{
\mathcal T_{D,\kappa}
=\tau\,
X_{D,\kappa}\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

The only new similarity parameter is the dimensionless measurement bandwidth `kappa`.

Thus finite bandwidth does **not** destroy the task-surface framework; it extends it.

---

## 8. Does the fast/slow boundary survive?

Take two regularized family members with

```math
r=\tau_s/\tau_f>1
```

and the same `rho_0` and `kappa`.

Write

```math
\ell=L/\tau_s.
```

Then

```math
T_{D,f}^{(\kappa)}
=\tau_f
X_{D,\kappa}(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}^{(\kappa)}
=r\tau_f
X_{D,\kappa}(\rho_0,\alpha,\beta,\ell).
```

Therefore the regularized crossover surface is still

```math
\boxed{
B_{r,\kappa}(\ell)
=
X_{D,\kappa}(\rho_0,\alpha,\beta,r\ell)
-rX_{D,\kappa}(\rho_0,\alpha,\beta,\ell)
=0.
}
```

So the **form of the fast/slow task boundary survives exactly**.

---

## 9. The feasibility ordering also survives for the co-scaled family

Let the regularized full-template threshold be

```math
\Gamma_{\infty,\kappa}(\ell,\alpha).
```

For one stationary Gaussian process, increasing the search interval from `ell` to `r ell` cannot lower its supremum quantile:

```math
\boxed{
\Gamma_{\infty,\kappa}(r\ell,\alpha)
\ge
\Gamma_{\infty,\kappa}(\ell,\alpha).
}
```

Thus, with equal eventual band-limited SNR `rho_0`, the same Step-12 feasibility ordering remains:

```text
both feasible
slow-only feasible
neither feasible
```

and **fast-only feasibility remains impossible** within this similarity-preserving regularized family.

If the regularized stationary scan has a nondegenerate continuous spectrum so correlations decay and the supremum threshold grows with search length, the same continuity argument gives at least one finite fast-to-slow crossover between `L=0` and the fast detector's feasibility edge.

Therefore:

**DERIVED / CONDITIONAL:** the Step-12 task-regime structure is not an artifact of infinite white-noise bandwidth. It survives a true finite-bandwidth regularization of the scaled family.

---

## 10. Large-bandwidth limit and another nonuniformity

Let

```math
\kappa\to\infty.
```

For fixed finite `x` and nonzero lag, a standard spectral truncation of the exact scan approaches the Step-13 hard-white-noise covariance.

But for every finite `kappa`,

```math
r_{x,\kappa}'(0)=0,
```

whereas the limiting hard-white-noise covariance has

```math
R_x'(0^+)=-a_x<0.
```

Thus the bandwidth-removal limit is again nonuniform at zero lag:

```text
finite kappa -> smooth scan
kappa -> infinity -> cusp can reappear.
```

This is the bandwidth analogue of the Step-13 noncommuting finite-window/full-template limits.

Under standard Gaussian-process convergence conditions, the regularized supremum thresholds and task boundary should converge to the rough ideal limit as `kappa` grows, but the convergence can be slow near the feasibility/crossover region. No numerical convergence rate is claimed yet.

---

## 11. Fixed physical bandwidth is a different comparison

Holding `kappa` fixed means the physical bandwidth scales as `1/tau`. This was chosen deliberately to preserve the time-scaled family and test whether the Step-12 mechanism survives regularization.

If instead the **same physical electronics bandwidth** `Omega_B` is imposed on both detectors, then

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=\Omega_B\tau_s
```

are different.

The comparison becomes

```math
T_{D,f}
=\tau_fX_D(\rho_0,\alpha,\beta,L/\tau_f,\kappa_f),
```

```math
T_{D,s}
=\tau_sX_D(\rho_0,\alpha,\beta,L/\tau_s,\kappa_s).
```

The simple Step-12 feasibility ordering need not follow automatically in that case because changing `tau` now also changes the dimensionless readout bandwidth.

**OPEN:** the fixed-physical-bandwidth comparison requires separate analysis.

---

## 12. First nontrivial consequence

**DERIVED / REFINEMENT:** a true finite accessible measurement bandwidth removes the finite-window covariance cusp,

```math
\boxed{
-r_{t,B}''(0)
=\int\omega^2W_{t,B}(\omega)d\omega
\le\Omega_B^2,
}
```

so the continuous scan becomes mean-square differentiable and Rice-type continuous-time threshold methods become mathematically admissible again.

At the same time, for the similarity-preserving regularized Step-09 family,

```math
\boxed{
\mathcal T_{D,\kappa}
=\tau X_{D,\kappa}(\rho_0,\alpha,\beta,L/\tau)
}
```

and the fast/slow boundary retains the exact form

```math
\boxed{
X_{D,\kappa}(r\ell)-rX_{D,\kappa}(\ell)=0.
}
```

Therefore the previously derived fast/slow task-regime mechanism **survives finite-bandwidth regularization**; the Step-13 numerical obstruction was a property of the infinite-white-bandwidth hard-window limit, not the source of the regime reversal itself.

---

## 13. What has been established

- **REJECTED SHORTCUT:** a noiseless invertible common low-pass does not necessarily reduce optimal-detection information bandwidth because whitening can cancel it.
- **DERIVED:** a true finite accessible frequency band makes the finite-window timing scan mean-square differentiable and removes the Step-13 cusp.
- **DERIVED:** the regularized scan curvature is bounded by the physical accessible bandwidth.
- **DERIVED:** the controlled time-scaled family gains one dimensionless parameter `kappa=Omega_B tau`.
- **DERIVED:** with fixed `kappa` and equal band-limited eventual SNR, the detection-time surface retains its scaled form and the fast/slow crossover equation survives.
- **DERIVED / CONDITIONAL:** the both-feasible / slow-only / neither-feasible task structure and at least one fast-to-slow crossover survive for the co-scaled finite-bandwidth family under the same continuity/mixing conditions.
- **REFINEMENT:** the Step-13 roughness is an exact feature of the infinite-white-bandwidth hard-window idealization, but not a generic necessity of finite-bandwidth detector measurements.

---

## 14. What has not been established

- No numerical `Gamma_kappa(x,ell,alpha)` table yet.
- No regularized numerical crossover or phase diagram yet.
- No convergence rate as `kappa->infinity`.
- No proof of crossover uniqueness.
- No result yet for a common fixed **physical** readout bandwidth across unequal `tau` detectors.
- No claim that an ideal brick-wall information band is itself a causal analog circuit; it is the clean exact representation of finite accessible frequency support. Sufficient physical rolloff/processing constraints can provide the same finite-second-moment regularity.
- No novelty claim.

---

## 15. Stopping point

The cleaner route is now identified: regularize the actual accessible timing information, not merely append an invertible filter.

### Single natural next question

> For a finite dimensionless bandwidth `kappa`, can the now-smooth Gaussian timing scan be simulated with controlled grid convergence and Rice/extreme-value cross-checks to obtain a trustworthy `Gamma_kappa(x,ell,alpha)` and fast/slow crossover, and how does that crossover move as `kappa` is increased toward the rough white-noise limit?
