# Step 11 — Dimensionless Detection Surface and Filter-Duration Ordering

**Date:** 2026-08-11 13:28 EDT  
**Status:** DERIVED for the Step-09 time-scaled equal-eventual-SNR family under equal white output noise and the Step-10 true-alignment Gaussian max-scan criterion. The detection-time surface collapses exactly onto `x=t/tau`, `ell=L/tau`, `rho_0`, `alpha`, and `beta`. A further exact negative result is obtained: for this family the task margin is strictly increasing with filter duration, so no finite interior optimal integration duration exists. No novelty claim.

---

## 1. Family and normalization

Use the same optical event

```math
p(t)=e^{-bt}u(t),
```

and the stable causal family

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2}.
```

Then

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

With equal white output-noise PSD `N`, choose

```math
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}},
```

so every member has

```math
\boxed{\rho_{\tau,\infty}=\rho_0.}
```

For this matched event/detector construction, `b` cancels from the output template and from the task statistics below.

---

## 2. Dimensionless finite-time SNR

Define

```math
x=\frac{t}{\tau}.
```

In white output noise, the finite-record optimal filter is proportional to

```math
q_{\tau,t}(u)\propto u e^{-u/\tau}\,1_{[0,t]}(u).
```

The accumulated squared-SNR fraction is

```math
\boxed{
\eta(x)=1-e^{-2x}(1+2x+2x^2).
}
```

Hence

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
}
```

Moreover,

```math
\boxed{
\eta'(x)=4x^2e^{-2x}>0
\qquad (x>0),
}
```

so the finite-time SNR is strictly increasing with filter duration.

---

## 3. Exact dimensionless finite-duration scan covariance

Define the dimensionless finite template

```math
h_x(v)=v e^{-v}\,1_{[0,x]}(v)
```

and lag

```math
y=\frac{|\Delta|}{\tau}.
```

The normalized white-noise timing-scan covariance is

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}dv
}{
\int_0^x v^2e^{-2v}dv
},
\qquad 0\le y<x,
}
```

and

```math
\boxed{R_x(y)=0\qquad y\ge x.}
```

Therefore

```math
\boxed{
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
}
```

This is exact for the finite hard-window scan and does not use the differentiable-process Rice approximation.

---

## 4. Dimensionless search interval and threshold

Define

```math
\boxed{\ell=\frac{L}{\tau}.}
```

After rescaling trial arrival time by `tau`, the noise-only scan is a unit-variance Gaussian process with covariance `R_x` searched over `[0,ell]`.

Hence the exact global false-alarm threshold has the form

```math
\boxed{
\gamma_{\tau,t}(L,\alpha)=\Gamma(x,\ell,\alpha),
}
```

where `Gamma` is the `(1-alpha)` quantile of the supremum of that dimensionless Gaussian process.

Thus the Step-10 true-alignment margin is

```math
\boxed{
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
}
```

and

```math
\boxed{
P_{D,true}=\Phi[M(x;\ell,\rho_0,\alpha)].
}
```

---

## 5. Exact detection-time surface collapse

Let

```math
z_\beta=\Phi^{-1}(\beta).
```

Define

```math
\boxed{
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\left\{x>0:
M(x;\ell,\rho_0,\alpha)\ge z_\beta
\right\}.
}
```

Then

```math
\boxed{
\mathcal T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
}
```

This is the exact dimensionless collapse for this family.

If `L/tau`, `rho_0`, `alpha`, and `beta` are held fixed, decision time scales linearly with `tau`. For fixed physical `L`, however, decreasing `tau` simultaneously enlarges `ell=L/tau`, so there is no simple universal proportionality `mathcal T_D proportional to tau`.

---

## 6. Covariance ordering with filter duration

For fixed dimensionless lag `y>=0`, rewrite

```math
R_x(y)
=\frac{
\int_0^x w(v)H_y(v)dv
}{
\int_0^x w(v)dv
},
```

with

```math
w(v)=v^2e^{-2v}>0
```

and

```math
H_y(v)=
\begin{cases}
0,&0\le v<y,\\
e^y\left(1-\frac{y}{v}\right),&v\ge y.
\end{cases}
```

For fixed `y`, `H_y(v)` is nondecreasing in `v`. Therefore enlarging the upper limit `x` increases its positive-weight average:

```math
\boxed{
x_2>x_1
\Rightarrow
R_{x_2}(y)\ge R_{x_1}(y)
\qquad\forall y.
}
```

Longer filters therefore produce a timing scan that is at least as correlated at every pair of trial times.

---

## 7. Slepian ordering of the global threshold

Consider two zero-mean unit-variance Gaussian scans on the same dimensionless interval `[0,ell]`, with `x_2>x_1`.

Since

```math
R_{x_2}(|u-v|)\ge R_{x_1}(|u-v|)
```

for all pairs, Slepian's Gaussian comparison inequality gives the corresponding supremum ordering. At fixed `ell` and `alpha`,

```math
\boxed{
\Gamma(x_2,\ell,\alpha)
\le
\Gamma(x_1,\ell,\alpha).
}
```

Thus increasing filter duration does two favorable things in this family:

```text
rho_0 sqrt(eta(x)) increases strictly,
Gamma(x,ell,alpha) does not increase.
```

Therefore

```math
\boxed{
M(x;\ell,\rho_0,\alpha)
\text{ is strictly increasing in }x.
}
```

This result does not require scan differentiability and is unaffected by the hard-window regularity warning from Steps 08–10.

---

## 8. Negative result: no finite interior optimal filter duration

Because the margin is strictly increasing,

```math
\boxed{
\operatorname*{arg\,max}_{0<t\le T}
[\rho_t-\gamma_t(L,\alpha)]
=\{T\}.
}
```

Hence, for this family,

```math
\boxed{t_{opt}(T)=T.}
```

With no finite maximum allowed delay, the margin approaches its full-template limit and has no finite interior maximizer.

**DERIVED / NEGATIVE RESULT:** the generic finite-`t_opt` possibility introduced in Step 10 is not realized by this controlled family.

This strengthens the interpretation of Step 09: its cross-detector ranking reversal is not caused by either detector using a self-suboptimal filter duration. Each detector individually benefits from using all available data.

---

## 9. Full-template limit and feasibility boundary

As `x->infinity`,

```math
\eta(x)\to1
```

and

```math
R_x(y)\to(1+y)e^{-y}.
```

Define

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
=\lim_{x\to\infty}\Gamma(x,\ell,\alpha).
}
```

Then

```math
\boxed{
M_\infty(\ell,\rho_0,\alpha)
=\rho_0-\Gamma_\infty(\ell,\alpha).
}
```

This is the supremum margin over all filter durations for this family.

A finite detection time exists whenever

```math
\Phi^{-1}(\beta)<M_\infty.
```

If the target lies above `M_infinity`, it is impossible under the stated criterion. Equality is an asymptotic boundary and, under ordinary strict convergence, requires infinite decision time.

---

## 10. Why Step 09 can still reverse detector ranking

For one fixed detector, increasing `t` increases

```math
x=t/\tau
```

while leaving

```math
\ell=L/\tau
```

fixed; its margin therefore increases monotonically.

Across two detector time scales in the same physical task,

```math
\ell_f=\frac{L}{\tau_f},
\qquad
\ell_s=\frac{L}{\tau_s}.
```

If `tau_f<tau_s`, then

```math
\ell_f>\ell_s.
```

So the faster detector has a smaller physical time unit but a larger dimensionless timing-search domain.

The Step-09 reversal is therefore a **cross-detector scaling effect**, not an integration-duration optimization effect.

---

## 11. First nontrivial consequence

For this equal-eventual-SNR family,

```math
\boxed{
\frac{\mathcal T_D}{\tau}
=X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
}
```

The detector time scale enters the task in two opposing ways:

```text
smaller tau
-> shrinks the physical unit of decision time

smaller tau
-> enlarges L/tau and the normalized timing-search burden
```

Therefore no monotonic detector ranking by `tau` alone follows even in this highly structured family.

At the same time,

```math
\boxed{M(x)\text{ increases strictly with }x,}
```

so no finite interior integration optimum exists here.

---

## 12. What has been established

- **DERIVED:** finite-time SNR depends on filter duration only through `x=t/tau` and `rho_0`.
- **DERIVED:** exact finite-duration scan covariance scales as `R_x(|Delta|/tau)`.
- **DERIVED:** exact global threshold has the form `Gamma(x,L/tau,alpha)`.
- **DERIVED:** `mathcal T_D=tau X_D(rho_0,alpha,beta,L/tau)`.
- **DERIVED:** finite-template covariance is pointwise nondecreasing with filter duration.
- **DERIVED / CONDITIONAL ON STANDARD GAUSSIAN COMPARISON CONDITIONS:** the search threshold is nonincreasing with filter duration.
- **DERIVED / NEGATIVE RESULT:** the task margin is strictly increasing with filter duration, so this family has no finite interior `t_opt`.
- **DERIVED:** Step-09 cross-detector reversal is compatible with each detector individually benefiting from all available data.

---

## 13. What has not been established

- No universal monotonic ordering of `mathcal T_D` with detector `tau` at fixed physical `L`.
- No closed-form exact `Gamma(x,ell,alpha)` or `X_D` for the correlated Gaussian supremum.
- No claim that all detector families have monotone filter-duration margins.
- No claim that a finite interior optimum cannot occur for other waveforms, noise spectra, detector responses, or search protocols.
- No exact global-rejection/localization surface; the criterion remains true-alignment threshold crossing.
- No Bayes-optimal unknown-arrival test, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No universal scalar replacement for `D*`.
- No novelty claim.

---

## 14. Stopping point

The Step-10 surface now has an exact dimensionless form for the controlled family, and the proposed finite optimal integration duration has yielded a useful null result.

### Single natural next question

> For two members of this family with different `tau` but equal `rho_0`, what is the boundary in task space `(L, alpha, beta)` where their detection-time surfaces cross — i.e. where the detector that reaches the required decision first switches from the faster member to the slower member?
