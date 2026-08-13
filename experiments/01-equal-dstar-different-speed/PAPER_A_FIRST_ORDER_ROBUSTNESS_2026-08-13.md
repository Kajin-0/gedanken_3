# Paper A — first-order detector robustness corollary

**Date:** 2026-08-13  
**Status:** ANALYTIC ROBUSTNESS RESULT / DOES NOT REOPEN STEP 49

The main Paper-A witness uses a controlled double-pole existence construction because its smooth full-template covariance supports a simple continuum Rice/Slepian bracket. A referee can reasonably ask whether the crossover mechanism is unique to that family.

It is not.

## 1. Standard first-order family

Take an ideal impulsive optical event and the causal stable single-pole detector channel

```math
G_\tau(s)=\frac{A_\tau}{s+1/\tau}.
```

The output signal is

```math
s_\tau(t)=A_\tau e^{-t/\tau}u(t).
```

With output white noise

```math
E[n(t)n(t')]=N\delta(t-t'),
```

the eventual matched-filter SNR is

```math
\rho_{\tau,\infty}^2
=\frac{A_\tau^2\tau}{2N}.
```

Choose

```math
\boxed{
A_\tau=\rho_0\sqrt{\frac{2N}{\tau}}
}
```

so every member has

```math
\rho_{\tau,\infty}=\rho_0.
```

This uses the same deliberate thought-experiment normalization as Paper A: the ordinary detector sensitivity/noise-bandwidth tradeoff is removed so that the timing-search effect can be isolated.

## 2. Finite-time evidence

Let `x=t/tau`. The accumulated squared-SNR fraction is

```math
\boxed{
\eta_1(x)=1-e^{-2x}.
}
```

Therefore

```math
\rho_{\tau,t}=\rho_0\sqrt{1-e^{-2x}},
```

which is strictly increasing in `x`. At known arrival, the faster channel again reaches every fixed evidence fraction sooner in physical time.

## 3. Finite-template timing covariance

The normalized finite template is proportional to

```math
h_x(v)=e^{-v}1_{[0,x]}(v).
```

For `0<=y<x`,

```math
\boxed{
R_{1,x}(y)
=\frac{e^{-y}-e^{-2x+y}}{1-e^{-2x}},
}
```

and `R_{1,x}(y)=0` for `y>=x`.

The full-template covariance is

```math
\boxed{
R_{1,\infty}(y)=e^{-y}.
}
```

For fixed `y>0`, write `a=e^{-2x}`. Then

```math
R_{1,x}(y)=\frac{e^{-y}-ae^y}{1-a}.
```

Differentiating with respect to `a`,

```math
\frac{\partial R_{1,x}}{\partial a}
=\frac{e^{-y}-e^y}{(1-a)^2}<0,
```

while

```math
\frac{da}{dx}=-2a<0.
```

Hence

```math
\boxed{
\frac{\partial R_{1,x}(y)}{\partial x}>0
}
```

for every `0<y<x`.

Also

```math
R_{1,x}(y)<R_{1,\infty}(y)
```

for finite `x` and `y>0`.

Therefore increasing integration duration increases the finite-template covariance pointwise, so the Slepian threshold ordering used in Paper A survives:

```math
x_2>x_1
\Longrightarrow
\Gamma_1(x_2,\ell,\alpha)
\le
\Gamma_1(x_1,\ell,\alpha).
```

The signal term increases strictly at the same time, so the sufficient guarantee margin is strictly increasing in `x`.

## 4. Feasibility and crossover

Since

```math
R_{1,\infty}(y)=e^{-y}\to0,
```

widely separated samples have arbitrarily small covariance. The same Slepian/equicorrelated comparison used in Paper A therefore gives

```math
\Gamma_{1,\infty}(\ell,\alpha)\to\infty
\qquad(\ell\to\infty).
```

For finite `x`,

```math
\eta_1(x)<1,
\qquad
R_{1,x}(y)\le R_{1,\infty}(y),
```

so

```math
\Gamma_1(x,\ell,\alpha)
\ge
\Gamma_{1,\infty}(\ell,\alpha).
```

Thus the same boundary-divergence argument applies. Under the same ordinary threshold/first-crossing continuity regularity:

- fast wins at `L=0`;
- the fast physical guarantee-feasibility boundary occurs first because `L_crit(tau)=tau ell_crit`;
- the fast sufficient guarantee time diverges at that boundary while the slow channel remains feasible;
- therefore at least one finite fast-to-slow **sufficient-guarantee-time crossover** exists.

## 5. Meaning

The crossover mechanism is therefore **not unique to the double-pole Gamma(2)-shaped family** used for the main continuum witness. It already occurs in the standard single-pole exponential detector response under the same equal-eventual-SNR thought-experiment normalization.

The main double-pole family remains useful because its smooth full-template covariance

```math
(1+y)e^{-y}
```

permits the clean Rice/Slepian finite-scale bracket. The first-order full-template covariance `e^{-|y|}` is locally rough, so it is not used to replace that witness.

This result is a robustness corollary, not a new Step 50 and not a reopening of finite-window crossover localization.
