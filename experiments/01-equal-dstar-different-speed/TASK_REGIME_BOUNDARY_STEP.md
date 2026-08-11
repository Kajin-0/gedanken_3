# Step 12 — Fast/Slow Task-Regime Boundary

**Date:** 2026-08-11 13:39 EDT  
**Status:** DERIVED / CONDITIONAL for the Step-09 time-scaled equal-eventual-SNR family and the Step-10/11 true-alignment Gaussian max-scan criterion. The fast/slow preference boundary is an implicit surface in task space, not a detector-only ordering. A stronger feasibility partition is obtained: at fixed eventual SNR there can be a slow-only region, but no fast-only feasibility region. Under standard continuity/divergence conditions, at least one finite fast-to-slow detection-time crossover must occur as timing uncertainty grows. No uniqueness or novelty claim.

---

## 1. Question

For two members of the controlled family with

```math
\tau_f<\tau_s
```

and equal eventual matched-filter SNR

```math
\rho_{f,\infty}=\rho_{s,\infty}=\rho_0,
```

where in task space `(L, alpha, beta)` does the detector that reaches the required decision first switch from the faster member to the slower member?

Here

```text
L      physical interval over which event arrival time is unknown
alpha  allowed global false-alarm probability
beta   required true-alignment detection probability
```

and the Step-11 dimensionless detection-time surface is used exactly.

---

## 2. Step-11 surface recalled

For a detector time scale `tau`,

```math
\boxed{
\mathcal T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

The dimensionless function `X_D` is defined by the first `x=t/tau` for which

```math
\rho_0\sqrt{\eta(x)}
-\Gamma(x,L/\tau,\alpha)
\ge\Phi^{-1}(\beta).
```

For this family the margin is strictly increasing in `x`, so the first crossing is unambiguous whenever the task is feasible.

---

## 3. Exact dimensionless fast/slow comparison

Define the response-time ratio

```math
\boxed{
r\equiv\frac{\tau_s}{\tau_f}>1
}
```

and measure the physical timing uncertainty in slow-detector units,

```math
\boxed{
\ell\equiv\frac{L}{\tau_s}.
}
```

Then

```math
\frac{L}{\tau_f}=r\ell.
```

The two physical detection times are therefore

```math
\boxed{
T_{D,f}
=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
}
```

```math
\boxed{
T_{D,s}
=\tau_s X_D(\rho_0,\alpha,\beta,\ell)
=r\tau_f X_D(\rho_0,\alpha,\beta,\ell).
}
```

Hence the exact preference rules are

```math
\boxed{
\text{fast wins}
\iff
X_D(\rho_0,\alpha,\beta,r\ell)
<rX_D(\rho_0,\alpha,\beta,\ell),
}
```

```math
\boxed{
\text{slow wins}
\iff
X_D(\rho_0,\alpha,\beta,r\ell)
>rX_D(\rho_0,\alpha,\beta,\ell),
}
```

and the fast/slow task-regime boundary is the zero set

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
\equiv
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)
=0.
}
```

This is exact but implicit because the correlated Gaussian-scan quantile `Gamma` does not yet have a closed form.

---

## 4. REJECTED SHORTCUT — asymptotic-margin equality is not the preference boundary

A tempting shortcut would be to compare only the full-template asymptotic margins

```math
M_\infty(\ell)
=\rho_0-\Gamma_\infty(\ell,\alpha).
```

That does **not** determine which detector reaches a finite required decision first.

For every positive physical `L`, the faster member has the larger normalized search interval and therefore the larger asymptotic search threshold,

```math
\Gamma_\infty(L/\tau_f,\alpha)
\ge
\Gamma_\infty(L/\tau_s,\alpha).
```

Thus the slow member has at least as large an asymptotic margin for every `L>0`.

Yet at known event time `L=0`, the dimensionless detection requirement is identical for both detectors, so

```math
\boxed{
T_{D,f}(0)
=\frac{\tau_f}{\tau_s}T_{D,s}(0)
<T_{D,s}(0).
}
```

Therefore asymptotic-margin ordering and minimum-decision-time ordering are distinct. The crossing boundary must compare the complete detection-time surfaces.

This failed shortcut is retained explicitly because it is an easy way to draw the wrong physical conclusion.

---

## 5. Exact feasibility partition

Let

```math
z_\beta=\Phi^{-1}(\beta)
```

and define the available asymptotic margin budget

```math
\boxed{
c\equiv\rho_0-z_\beta.
}
```

For a detector with normalized timing uncertainty `ell`, the task has a finite detection time only if

```math
\boxed{
\Gamma_\infty(\ell,\alpha)<c.
}
```

Equality is the asymptotic boundary: under ordinary strict convergence the target is approached only as `t->infinity`. If `Gamma_infinity>c`, the requested operating point is impossible under the stated true-alignment criterion.

For the slow detector the normalized interval is `ell`; for the fast detector it is `r ell`. Since the supremum threshold is nondecreasing with search interval,

```math
\Gamma_\infty(r\ell,\alpha)
\ge
\Gamma_\infty(\ell,\alpha).
```

Therefore task space partitions into only three feasibility regimes.

### Both detectors feasible

```math
\boxed{
c>\Gamma_\infty(r\ell,\alpha).
}
```

Both detection times are finite, and the winner is determined by the exact boundary `B_r=0`.

### Slow detector feasible, fast detector infeasible

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
<c
\le
\Gamma_\infty(r\ell,\alpha).
}
```

Then

```text
T_D,s < infinity,
T_D,f = infinity.
```

This is an exact **slow-only feasibility region**.

### Neither detector feasible

```math
\boxed{
c\le\Gamma_\infty(\ell,\alpha).
}
```

Then neither detector can reach the requested `(alpha,beta)` operating point, irrespective of integration duration.

### Impossible regime: fast-only feasibility

Because

```math
\Gamma_\infty(r\ell,\alpha)
\ge
\Gamma_\infty(\ell,\alpha),
```

there is no task point at which the fast member is asymptotically feasible while the slow member is not, under the equal-`rho_0` assumptions of this family.

**DERIVED:** slow-only feasibility is possible; fast-only feasibility is impossible.

---

## 6. Physical timing-uncertainty limit scales linearly with tau

Define the dimensionless maximum timing uncertainty supported by the requested operating point using the generalized inverse

```math
\boxed{
\ell_{crit}(\rho_0,\alpha,\beta)
\equiv
\sup\{\ell\ge0:
\Gamma_\infty(\ell,\alpha)<\rho_0-\Phi^{-1}(\beta)\}.
}
```

Then the corresponding physical timing-uncertainty limit for a detector with time scale `tau` is

```math
\boxed{
L_{crit}(\tau)
=\tau\,\ell_{crit}.
}
```

Therefore for the two detectors

```math
\boxed{
\frac{L_{crit,s}}{L_{crit,f}}
=\frac{\tau_s}{\tau_f}
=r.
}
```

Within this equal-eventual-SNR scaled family, the slower detector tolerates a proportionally larger **physical** arrival-time uncertainty before the requested false-alarm/detection operating point becomes impossible.

This is not a claim of universally better slow detectors; it follows from the deliberately fixed eventual SNR together with the time-scaled timing-search process.

---

## 7. Existence of a fast-to-slow detection-time crossover

Assume the requested `(alpha,beta)` point is feasible for known event time, so

```math
\rho_0-\Phi^{-1}(1-\alpha)
>\Phi^{-1}(\beta).
```

Also use the standard properties already implicit in the Gaussian-search construction:

1. `X_D` varies continuously with the search interval away from feasibility singularities;
2. the exponentially decorrelating full-template scan has a global threshold that grows without bound as the normalized search interval grows;
3. as the fast detector approaches its feasibility boundary from below,

```math
T_{D,f}\to\infty.
```

At

```math
L=0,
```

both detectors face the same dimensionless known-time task, so

```math
\boxed{T_{D,f}<T_{D,s}.}
```

But the fast detector reaches its feasibility boundary first,

```math
L_{crit,f}=\tau_f\ell_{crit}
<
\tau_s\ell_{crit}=L_{crit,s}.
```

As

```math
L\uparrow L_{crit,f},
```

`T_D,f` diverges while the slow detector remains strictly inside its feasible region and has finite `T_D,s`.

Therefore, by continuity, there exists at least one

```math
\boxed{
L_\times\in(0,L_{crit,f})
}
```

such that

```math
\boxed{
T_{D,f}(L_\times)=T_{D,s}(L_\times).
}
```

For sufficiently small `L`, the fast detector wins. Near the fast detector's feasibility boundary, the slow detector wins.

**DERIVED / CONDITIONAL:** at least one finite fast-to-slow task crossover exists under the stated continuity/extreme-value conditions.

No uniqueness has been established. The boundary could in principle have more complicated structure in `(L,alpha,beta)` space.

---

## 8. High-threshold Rice estimate of the feasibility boundary — illustration only

For the full-template covariance of this family,

```math
r_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)e^{-|\Delta|/\tau},
```

the Step-08 RMS frequency is

```math
f_{rms}=\frac{1}{2\pi\tau}.
```

In dimensionless variables, the high-threshold rare-excursion approximation is

```math
\alpha
\approx
Q(u)+\frac{\ell}{2\pi}e^{-u^2/2}.
```

At the asymptotic feasibility boundary set

```math
u=c=\rho_0-\Phi^{-1}(\beta).
```

Then

```math
\boxed{
\ell_{crit}^{Rice}
\approx
2\pi\,[\alpha-Q(c)]\,e^{c^2/2},
}
```

provided `c` is above the known-time threshold and the rare-excursion approximation is appropriate.

### Extreme illustrative example

Take

```text
rho_0 = 8
alpha = 1e-6
beta = 0.90
```

so

```text
Phi^{-1}(beta) ~= 1.28155
c ~= 6.71845
Q(c) ~= 9.18e-12.
```

The Rice estimate gives approximately

```text
ell_crit ~= 3.98e4.
```

For the deliberately extreme original response scales

```text
tau_f = 1 ns
tau_s = 1 s,
```

this corresponds approximately to

```text
L_crit,f ~= 39.8 us
L_crit,s ~= 3.98e4 s ~= 11.1 h.
```

These numbers are only a high-threshold illustration of the scaling law, not an exact computed task boundary. The exact crossover `L_x` still requires the finite-duration correlated-scan quantile `Gamma(x,ell,alpha)`.

---

## 9. First nontrivial consequence

**DERIVED:** the controlled family has an exact task-regime classification, not merely an abstract possibility of ranking reversal.

For equal eventual SNR and `tau_f<tau_s`:

```text
small timing uncertainty
    -> fast detector reaches the required decision first

intermediate timing uncertainty
    -> both may remain feasible, but a crossover boundary B_r=0 switches the preferred detector

larger timing uncertainty
    -> slow-only feasibility region is possible

still larger timing uncertainty
    -> neither detector can meet the task
```

The fast-only feasibility counterpart is forbidden by the search-threshold ordering in this family.

This converts the Step-09 existence result into a task-space regime structure while preserving the exact correlated-search problem.

---

## 10. What has been established

- **DERIVED:** the exact fast/slow preference boundary is `X_D(r ell)-r X_D(ell)=0` for fixed `(rho_0,alpha,beta,r)`.
- **REJECTED SHORTCUT:** asymptotic-margin equality is not the detection-time preference boundary.
- **DERIVED:** task space partitions into both-feasible, slow-only, and neither-feasible regions; fast-only feasibility is impossible under equal eventual SNR.
- **DERIVED:** the physical timing-uncertainty feasibility limit scales exactly as `L_crit=tau ell_crit`.
- **DERIVED / CONDITIONAL:** at least one finite fast-to-slow crossover exists between known-time operation and the fast detector's feasibility boundary under standard continuity/extreme-value conditions.
- **CONDITIONAL / ILLUSTRATIVE:** Rice theory gives a high-threshold approximation to `ell_crit`, not the exact crossover surface.

---

## 11. What has not been established

- No proof that the fast/slow crossover is unique.
- No exact closed form for `Gamma(x,ell,alpha)` or `X_D`.
- No exact numerical value of the crossover `L_x` yet.
- No claim that the extreme `1 ns` versus `1 s` illustrative feasibility scales are representative of practical photodetectors.
- No universal task boundary outside the Step-09 scaled Gaussian family.
- No exact global-rejection/localization boundary; the criterion remains true-alignment threshold crossing.
- No Bayes-optimal unknown-time detector, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No novelty claim.

---

## 12. Stopping point

The existence and structure of the fast/slow task-regime boundary are now established analytically, but its exact location is still implicit through the correlated Gaussian-process supremum threshold.

### Single natural next question

> Can the exact finite-duration Gaussian scan with covariance `R_x` be computed numerically well enough to map `Gamma(x,ell,alpha)`, solve the crossover equation, and produce an actual fast/slow phase diagram for chosen `(rho_0, r, alpha, beta)` without reverting to an uncontrolled independent-trials approximation?
