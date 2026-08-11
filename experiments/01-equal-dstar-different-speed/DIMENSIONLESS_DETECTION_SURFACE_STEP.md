# Step 11 — Dimensionless Detection Surface and Filter-Duration Ordering

**Date:** 2026-08-11 13:28 EDT  
**Status:** DERIVED for the Step-09 time-scaled equal-eventual-SNR family under equal white output noise and the Step-10 true-alignment Gaussian max-scan criterion. The entire detection-time surface collapses onto the dimensionless variables `x=t/tau`, `ell=L/tau`, `rho_0`, `alpha`, and `beta`. A further exact null result is obtained: for this family the task margin is strictly increasing with filter duration, so there is no finite interior optimal integration/filter duration. This does not contradict the Step-09 cross-detector ranking reversal. No novelty claim.

---

## 1. Question

For the time-scaled equal-eventual-SNR family introduced in Step 09:

1. does the Step-10 detection-time surface reduce to a dimensionless form involving only `t/tau`, `L/tau`, `rho_infinity`, `P_FA`, and `P_D`?;
2. does the competition between SNR accumulation and unknown-time search penalty create a finite optimal filter duration?

The answer is:

- **yes** to the dimensionless collapse;
- **no** to a finite interior optimum for this specific family.

The second answer is a genuine negative result and is retained explicitly.

---

## 2. Step-09 detector family

Use the same optical event

```math
p(t)=e^{-bt}u(t),
\qquad b>0,
```

and the stable causal detector/readout family

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}.
```

For this event,

```math
\boxed{
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
}
```

Assume equal white output-noise PSD `N` and choose

```math
A_\tau
=\frac{2\rho_0\sqrt N}{\tau^{3/2}},
```

so every member has the same full-observation matched-filter SNR amplitude

```math
\boxed{
\rho_{\tau,\infty}=\rho_0.
}
```

The parameter `b` disappears from the output template for this deliberately matched optical event/detector construction. The task performance derived below therefore depends on the output scale `tau`, not separately on `b`.

---

## 3. Dimensionless finite-time SNR

Choose a finite filter duration `t` and define

```math
\boxed{
x\equiv\frac{t}{\tau}.
}
```

In white output noise, the finite-record optimal filter is proportional to the restricted signal:

```math
q_{\tau,t}(u)\propto
u e^{-u/\tau}\,1_{[0,t]}(u).
```

The accumulated squared-SNR fraction from Step 09 is

```math
\boxed{
\eta(x)
=1-e^{-2x}(1+2x+2x^2).
}
```

Hence

```math
\boxed{
\rho_{\tau,t}
=\rho_0\sqrt{\eta(x)}.
}
```

No additional dimensional parameter remains in the SNR term.

Also,

```math
\boxed{
\frac{d\eta}{dx}=4x^2e^{-2x}>0
\qquad (x>0),
}
```

so finite-time SNR is strictly increasing with the dimensionless filter duration.

---

## 4. Dimensionless finite-duration timing-scan covariance

Amplitude normalization does not affect the normalized scan covariance. Define the dimensionless finite template

```math
h_x(v)=v e^{-v}\,1_{[0,x]}(v).
```

Let

```math
\boxed{
y\equiv\frac{|\Delta|}{\tau}.
}
```

Then the exact white-noise timing-scan covariance from Step 09 becomes

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}
v(v+y)e^{-2v-y}dv
}{
\int_0^x v^2e^{-2v}dv
}
\qquad 0\le y<x,
}
```

with

```math
\boxed{
R_x(y)=0
\qquad y\ge x.
}
```

Therefore

```math
\boxed{
r_{\tau,t}(\Delta)
=R_{t/\tau}(|\Delta|/\tau).
}
```

This is the exact finite-deadline covariance scaling. It does not require differentiability or a Rice approximation.

---

## 5. Dimensionless monitoring interval and threshold

Define the dimensionless arrival-time uncertainty length

```math
\boxed{
\ell\equiv\frac{L}{\tau}.
}
```

Under noise only, rescale candidate arrival time as

```math
u=\frac{\tau_{trial}}{\tau}.
```

The normalized Gaussian scan over the physical interval `[0,L]` is then statistically equivalent to a dimensionless Gaussian process with covariance `R_x` scanned over

```math
0\le\nu\le\ell.
```

Hence its exact global false-alarm threshold has the form

```math
\boxed{
\gamma_{\tau,t}(L,\alpha)
=\Gamma(x,\ell,\alpha),
}
```

where `Gamma` is the `(1-alpha)` quantile of the supremum of the unit-variance Gaussian process with covariance `R_x` over `[0,ell]`.

No separate dependence on `t`, `tau`, or `L` remains once `x=t/tau` and `ell=L/tau` are specified.

---

## 6. Exact dimensionless task margin

The Step-10 true-alignment margin becomes

```math
m_{\tau}(t;L,\alpha)
=\rho_{\tau,t}-\gamma_{\tau,t}(L,\alpha).
```

Therefore

```math
\boxed{
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}
-\Gamma(x,\ell,\alpha).
}
```

and

```math
\boxed{
P_{D,true}
=\Phi\!\left[M(x;\ell,\rho_0,\alpha)\right].
}
```

Thus the complete task dependence of this time-scaled family is contained in

```text
x       = chosen filter duration / detector time scale
ell     = arrival-time uncertainty interval / detector time scale
rho_0   = eventual known-time matched-filter SNR amplitude
alpha   = allowed global false-alarm probability
beta    = required true-alignment detection probability
```

---

## 7. Detection-time surface collapse

Let

```math
z_\beta=\Phi^{-1}(\beta).
```

Define the dimensionless required delay

```math
\boxed{
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\left\{
x>0:
M(x;\ell,\rho_0,\alpha)
\ge z_\beta
\right\}.
}
```

Then the physical Step-10 detection-time surface is exactly

```math
\boxed{
\mathcal T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

This is the desired dimensionless collapse.

Important interpretation:

- if two tasks have the same `L/tau`, `rho_0`, `alpha`, and `beta`, their required decision times scale linearly with `tau`;
- for a **fixed physical** monitoring interval `L`, changing `tau` also changes `ell=L/tau`, so the scaling is not simply `mathcal T_D proportional to tau`.

A faster detector has a smaller physical time unit but simultaneously faces a longer timing-search interval in its own natural units.

That is precisely the competition exposed in Step 09.

---

## 8. Does this family have a finite optimal filter duration?

The generic Step-10 framework allowed the possibility that

```math
m(t)=\rho_t-\gamma_t
```

might have an interior maximum.

For the present family, it does not.

The reason can be shown exactly from covariance ordering.

For fixed dimensionless lag `y>=0`, rewrite the covariance numerator using `v=u+y`:

```math
R_x(y)
=
\frac{
\int_0^x w(v)H_y(v)dv
}{
\int_0^x w(v)dv
},
```

where

```math
w(v)=v^2e^{-2v}>0
```

and

```math
H_y(v)
=
\begin{cases}
0,&0\le v<y,\\
 e^y\left(1-\frac{y}{v}\right),&v\ge y.
\end{cases}
```

For every fixed `y`, `H_y(v)` is nondecreasing in `v`.

Therefore `R_x(y)` is the weighted average of a nondecreasing function over `[0,x]`. Enlarging `x` can only increase that weighted average:

```math
\boxed{
x_2>x_1
\quad\Rightarrow\quad
R_{x_2}(y)\ge R_{x_1}(y)
\qquad\forall y.
}
```

So longer filters produce a noise-only timing scan that is at least as correlated at every pair of trial times.

---

## 9. Slepian ordering of the search threshold

Consider two zero-mean unit-variance Gaussian scans over the same dimensionless monitoring interval `[0,ell]`, with filter durations `x_2>x_1`.

Section 8 gives

```math
R_{x_2}(|u-v|)
\ge
R_{x_1}(|u-v|)
```

for every pair `u,v`.

By Slepian's Gaussian comparison inequality, the more strongly correlated process has a stochastically smaller supremum. Therefore, at fixed `ell` and `alpha`,

```math
\boxed{
\Gamma(x_2,\ell,\alpha)
\le
\Gamma(x_1,\ell,\alpha).
}
```

Thus increasing filter duration has **both** of the following effects for this family:

```text
rho_0 sqrt(eta(x)) increases strictly,
Gamma(x,ell,alpha) does not increase.
```

Consequently

```math
\boxed{
M(x;\ell,\rho_0,\alpha)
\text{ is strictly increasing in }x.
}
```

This conclusion does not use the Step-08 differentiable-process/Rice approximation and is unaffected by the hard-window regularity issue.

---

## 10. Negative result: no finite interior t_opt in this family

Because the margin is strictly increasing,

```math
\boxed{
\operatorname*{arg\,max}_{0<t\le T}
[\rho_t-\gamma_t(L,\alpha)]
=\{T\}.
}
```

So if the task permits a maximum delay `T`, the optimal filter for this family uses all available data:

```math
\boxed{
t_{opt}(T)=T.
}
```

With no finite maximum allowed delay, the unrestricted margin approaches its full-template limit and has no finite interior maximizer.

**DERIVED / NEGATIVE RESULT:** the generic possibility of a finite optimal integration duration introduced in Step 10 is **not realized** by the Step-09 time-scaled pulse family.

This is scientifically useful: the cross-detector ranking reversal of Step 09 does not require either detector to be using a self-suboptimal filter duration.

Each detector individually improves as it uses more of its own response; the reversal arises because the two detectors approach different unknown-time search-threshold limits over the same physical monitoring interval.

---

## 11. Full-template limit and feasibility boundary

As

```math
x\to\infty,
```

```math
\eta(x)\to1
```

and

```math
R_x(y)
\to
(1+y)e^{-y},
```

the Step-09 full-template covariance.

Define its exact dimensionless global threshold

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

This is the supremum of the true-alignment decision margin over all filter durations for this family.

Therefore the requested operating point has a finite detection time whenever

```math
\Phi^{-1}(\beta)
<
M_\infty(\ell,\rho_0,\alpha).
```

If the target lies above this asymptotic margin, it is impossible under the stated criterion. Equality is an asymptotic boundary and, under ordinary strict convergence, requires infinite decision time rather than a finite crossing.

---

## 12. Relationship to the Step-09 ranking reversal

There is no contradiction between

```text
for each detector separately:
longer filter duration always helps,
```

and

```text
between two detectors:
the slower detector can eventually have the larger unknown-time detection margin.
```

For a fixed detector `tau`, increasing `t` means increasing `x=t/tau` at fixed

```math
\ell=L/\tau.
```

The margin increases monotonically.

But comparing two detector time scales at the same physical task changes

```math
\ell_f=L/\tau_f,
\qquad
\ell_s=L/\tau_s.
```

A faster detector has

```math
\ell_f>\ell_s,
```

so it faces a larger dimensionless arrival-time search domain and therefore a larger asymptotic search threshold.

The Step-09 reversal is therefore a **cross-detector scaling effect**, not a failure to choose the optimal filter duration within either detector.

---

## 13. First nontrivial consequence

**DERIVED:** for the Step-09 equal-eventual-SNR family,

```math
\boxed{
\frac{\mathcal T_D}{\tau}
=
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

The detector time scale enters the task in two opposing ways:

```text
smaller tau
-> shrinks the physical unit of decision time

smaller tau
-> enlarges L/tau and therefore the normalized timing-search burden
```

This explains why no universal monotonic ranking by `tau` alone is possible even in this highly structured family.

At the same time, for any one fixed detector in this family,

```math
\boxed{
M(x)\text{ increases strictly with }x,
}
```

so there is no finite interior optimum integration duration.

---

## 14. What has been established

- **DERIVED:** the finite-time SNR depends on filter duration only through `x=t/tau` and `rho_0`.
- **DERIVED:** the exact finite-duration timing-scan covariance scales as `R_x(|Delta|/tau)`.
- **DERIVED:** the global unknown-time threshold has the dimensionless form `Gamma(x,L/tau,alpha)`.
- **DERIVED:** the detection-time surface collapses to `mathcal T_D=tau X_D(rho_0,alpha,beta,L/tau)`.
- **DERIVED:** for fixed `x` ordering, the finite-template covariance is pointwise nondecreasing with filter duration.
- **DERIVED / CONDITIONAL ON STANDARD GAUSSIAN COMPARISON CONDITIONS:** Slepian ordering makes the global search threshold nonincreasing with filter duration.
- **DERIVED / NEGATIVE RESULT:** the task margin is strictly increasing with filter duration, so the Step-09 family has no finite interior `t_opt`.
- **DERIVED:** Step-09 cross-detector reversal remains compatible with each detector individually benefiting from all available data.

---

## 15. What has not been established

- No universal monotonic ordering of `mathcal T_D` with detector `tau` at fixed physical `L`.
- No closed-form exact `Gamma(x,ell,alpha)` or `X_D` for the correlated Gaussian supremum.
- No claim that all detector families have monotone filter-duration margins; the no-interior-optimum result uses the special covariance ordering proved here.
- No claim that a finite interior optimum cannot occur for other waveforms, noise spectra, detector responses, or search protocols.
- No exact global-rejection/localization surface; the criterion remains true-alignment threshold crossing.
- No Bayes-optimal unknown-arrival test, sequential stopping, unknown amplitude/phase, signal-dependent noise, nonlinear response, saturation, dead time, or nonstationarity.
- No universal scalar replacement for `D*`.
- No novelty claim.

---

## 16. Stopping point

The Step-10 surface now has an exact dimensionless form for the controlled time-scaled family, and the proposed finite optimal integration duration has produced a useful null result rather than a forced new effect.

### Single natural next question

> For two members of this family with different `tau` but equal `rho_0`, what is the boundary in task space `(L, alpha, beta)` where their dimensionless detection-time surfaces cross — i.e. where the detector that reaches the required decision first switches from the faster member to the slower member?
