# Paper A — Continuum Quantitative Regime Witness Without Crossover Localization

**Date:** 2026-08-12  
**Status:** FINAL CONTINUUM-LEVEL FEASIBILITY BRACKET / EXACT FULL-TEMPLATE GAUSSIAN PROCESS / STEP-49 HARD STOP PRESERVED

This file records the controlling quantitative witness for Paper A. It replaces the earlier Monte Carlo witness as the manuscript-level example while preserving that earlier calculation as an independent numerical cross-check in Git history and `numerics/paper_a_full_template_feasibility.py`.

---

## Parameters

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=\frac{\tau_s}{\tau_f}=6.
```

At known arrival,

```math
\rho_0\sqrt{\eta(x_0)}-\Phi^{-1}(1-\alpha)=\Phi^{-1}(\beta),
```

with

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
```

gives

```math
\boxed{x_0=1.80519795247291.}
```

Therefore

```math
T_{G,f}(0)/\tau_f=1.80519795247,
```

while

```math
T_{G,s}(0)/\tau_f=6x_0=10.83118771484,
```

so the fast channel is exactly preferred at `L=0`.

---

## Finite physical uncertainty

Choose

```math
\boxed{L=9\tau_f=1.5\tau_s.}
```

Thus

```math
\ell_f=9,
\qquad
\ell_s=1.5.
```

The full-template covariance is

```math
R_\infty(y)=(1+|y|)e^{-|y|},
```

and the feasibility threshold budget is

```math
\boxed{
c=\rho_0-\Phi^{-1}(\beta)=2.21844843445540.
}
```

---

## Slow channel — continuous-time upper bound

Since

```math
R_\infty''(0)=-1,
```

Rice's exact mean upcrossing rate of level `c` is

```math
\nu_c^+=\frac{1}{2\pi}e^{-c^2/2}.
```

A continuous path exceeding `c` on `[0,ell]` must either begin above `c` or contain at least one upcrossing. Hence

```math
P_{FA}(\ell;c)
\le Q(c)+\frac{\ell}{2\pi}e^{-c^2/2}.
```

At `ell_s=1.5`,

```math
\boxed{
P_{FA,s}
\le0.0336427995841
<0.05.
}
```

Therefore

```math
\boxed{\Gamma_\infty(1.5,0.05)<c,}
```

so the slow channel is guarantee-feasible.

This is a one-sided continuous-process inequality, not a Rice approximation to the false-alarm probability.

---

## Fast channel — Slepian lower bound

Take seven points over `[0,9]` at spacing

```math
d=1.5.
```

Every distinct pair has covariance at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Compare the sampled vector with

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i,
\qquad i=1,\ldots,7,
```

where `V,E_1,...,E_7` are independent standard normals. The comparison vector has at least as large covariance between every distinct pair, so Slepian gives

```math
\Pr[\max_i Z_i>c]\ge\Pr[\max_iY_i>c].
```

The equicorrelated probability is

```math
\Pr[\max_iY_i\le c]
=\int_{-\infty}^{\infty}
\phi(v)
\Phi\!\left(
\frac{c-\sqrt\epsilon v}{\sqrt{1-\epsilon}}
\right)^7dv.
```

One-dimensional quadrature gives

```math
\boxed{
\Pr[\max_iY_i>c]
=0.0624701020698.
}
```

The continuous supremum contains this seven-point maximum, so

```math
\boxed{
P_{FA,f}\ge0.0624701020698>0.05.
}
```

Therefore

```math
\boxed{\Gamma_\infty(9,0.05)>c,}
```

and the fast channel is guarantee-infeasible.

---

## Regime separation

At the same physical arrival-time uncertainty,

```math
\boxed{
P_{FA,s}\le0.0336428
<0.05
<0.0624701\le P_{FA,f}.
}
```

Thus

```math
\boxed{
\text{slow channel guarantee-feasible},
\qquad
\text{fast channel guarantee-infeasible}.
}
```

Combined with exact fast preference at `L=0` and Proposition 1, this provides a finite physical scale across which at least one fast-to-slow guarantee-time crossover must occur.

This witness does **not** numerically locate `L_\times`, prove uniqueness, or solve the exact full signal-present scan-power problem.

---

## Reproducibility

The one-dimensional calculation is stored in

`numerics/paper_a_analytic_feasibility_bracket.py`.

The older paired full-template Monte Carlo calculation remains in

`numerics/paper_a_full_template_feasibility.py`

as an independent cross-check only.

---

## Hard-stop boundary

This calculation does not reopen Steps 13–49. In particular, it does not use the invalid Step-13 hard-window grid crossover, the invalid Step-20 upper Rice switch, Step-44 as continuum truth, or Steps 47–49 as an exact finite-`u` scan-power closure.

**Do not create Step 50 by default.**

The appropriate next phase is external-style manuscript preparation/review, not another Gaussian-extremes branch.