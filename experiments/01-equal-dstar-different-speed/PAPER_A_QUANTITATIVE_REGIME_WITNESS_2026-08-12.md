# Paper A — Continuum Quantitative Regime Witness Without Crossover Localization

**Date:** 2026-08-12  
**Status:** CONTINUUM-LEVEL FEASIBILITY BRACKET / EXACT FULL-TEMPLATE GAUSSIAN PROCESS / NOT A NUMERICAL CROSSOVER LOCATION / STEP-49 HARD STOP PRESERVED

---

## 1. Purpose

The adversarial review asked for a quantitative example showing that the analytical fast/slow ordering theorem is not merely formal. Directly locating the finite-duration hard-window crossover was already shown in Steps 13–49 to be numerically delicate because the truncated template produces a locally rough timing scan. That branch remains intentionally hard-stopped.

A stronger example is available without reopening it.

The Paper-A theorem separates:

1. exact known-time fast preference; and
2. full-template guarantee feasibility governed by the smooth stationary Gaussian process

```math
R_\infty(y)=(1+|y|)e^{-|y|}.
```

The new witness brackets the slow and fast full-template false-alarm probabilities on opposite sides of `alpha` **directly in continuous time**. No timing-grid extrapolation is needed.

---

## 2. Parameter choice

Use

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=\frac{\tau_s}{\tau_f}=6.
```

The full-template feasibility threshold is

```math
\boxed{
c=\rho_0-\Phi^{-1}(\beta)
=2.21844843445540.
}
```

The moderate false-alarm level is intentional. Paper A is not restricted to rare-event operation; the purpose is to give a transparent continuum witness without invoking the Step-13–49 rare-event machinery.

---

## 3. Known arrival: exact fast preference

At `L=0`, the scan collapses to one known alignment and

```math
\rho_0\sqrt{\eta(x_0)}-\Phi^{-1}(1-\alpha)
=\Phi^{-1}(\beta).
```

With

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2),
```

the exact scalar solution is

```math
\boxed{x_0=1.80519795247291.}
```

Therefore

```math
\boxed{
\frac{T_{G,f}(0)}{\tau_f}=1.80519795247,
}
```

while

```math
\boxed{
\frac{T_{G,s}(0)}{\tau_f}
=6x_0
=10.83118771484.
}
```

The fast channel is exactly preferred at known arrival.

---

## 4. Choose one common physical timing uncertainty

Take

```math
\boxed{
L=9\tau_f=1.5\tau_s.
}
```

Thus

```math
\ell_f=\frac{L}{\tau_f}=9,
\qquad
\ell_s=\frac{L}{\tau_s}=1.5.
```

The two channels have the same normalized full-template covariance law; only the normalized search length differs.

---

## 5. Slow channel: rigorous continuous-time upper bound

For the full-template process,

```math
R_\infty''(0)=-1.
```

Hence the exact mean upcrossing rate of level `c` is, by Rice's formula,

```math
\nu_c^+
=\frac{1}{2\pi}e^{-c^2/2}.
```

A continuous path whose supremum on `[0,ell]` exceeds `c` must either begin above `c` or contain at least one upcrossing. Therefore

```math
\Pr\left[
\sup_{0\le q\le\ell}Z_\infty(q)>c
\right]
\le
Q(c)+E[N_c^+]
```

and thus

```math
\boxed{
P_{FA}(\ell;c)
\le
Q(c)+\frac{\ell}{2\pi}e^{-c^2/2}.
}
```

At the slow-channel search length `ell_s=1.5`,

```text
Q(c) = 0.0132621359043
(1/(2*pi)) exp(-c^2/2) = 0.0135871091198.
```

Therefore

```math
\boxed{
P_{FA,s}
\le0.0336427995841
<0.05.
}
```

So the slow channel is **guarantee-feasible** at this physical `L`.

This is an inequality for the continuous process, not a Rice approximation to the probability.

---

## 6. Fast channel: Slepian lower bound from seven sampled points

For the fast channel, consider only seven points in `[0,9]` separated by

```math
d=1.5.
```

Because `R_infty(y)` decreases for positive `y`, every off-diagonal covariance among these sampled points satisfies

```math
\operatorname{Cov}(Z_i,Z_j)
\le
\epsilon,
\qquad
\epsilon=R_\infty(1.5).
```

Numerically,

```math
\boxed{
\epsilon
=(1+1.5)e^{-1.5}
=0.557825400371075.
}
```

Compare the seven sampled values with the equicorrelated Gaussian vector

```math
Y_i
=\sqrt\epsilon\,V
+\sqrt{1-\epsilon}\,E_i,
\qquad i=1,\ldots,7,
```

where `V,E_1,...,E_7` are independent standard normal variables.

The comparison vector has covariance at least as large as the actual sampled vector at every distinct pair. Slepian's inequality therefore gives

```math
\Pr\left[\max_i Z_i>c\right]
\ge
\Pr\left[\max_iY_i>c\right].
```

The equicorrelated probability is one-dimensional:

```math
\Pr[\max_iY_i\le c]
=
\int_{-\infty}^{\infty}
\phi(v)
\Phi\!\left(
\frac{c-\sqrt\epsilon v}{\sqrt{1-\epsilon}}
\right)^7dv.
```

High-accuracy quadrature gives

```math
\boxed{
\Pr[\max_iY_i>c]
=0.0624701020698.
}
```

Because the continuous supremum contains the seven-point maximum,

```math
\boxed{
P_{FA,f}
\ge0.0624701020698
>0.05.
}
```

Thus the fast channel is **guarantee-infeasible** at the same physical `L`.

The reproducible calculation is

```text
numerics/paper_a_analytic_feasibility_bracket.py
```

and uses only a one-dimensional quadrature for the equicorrelated comparison probability.

---

## 7. Certified regime separation

At one and the same physical arrival-time uncertainty,

```math
L=9\tau_f=1.5\tau_s,
```

the continuum bounds give

```math
\boxed{
P_{FA,s}
\le0.0336428
<0.05
<0.0624701
\le P_{FA,f}.
}
```

Therefore

```math
\boxed{
\text{slow channel guarantee-feasible},
\qquad
\text{fast channel guarantee-infeasible}.
}
```

Combined with the exact known-time result,

```text
L=0 -> fast has smaller guarantee time,
L=9 tau_f=1.5 tau_s -> slow-only guarantee feasibility,
```

and Proposition 1 forces at least one fast-to-slow guarantee-time crossover before the fast feasibility boundary.

The witness provides a finite physical scale without numerically localizing the finite-duration crossover.

---

## 8. Why this is stronger than the earlier Monte Carlo witness

An earlier Paper-A draft used a paired full-template Monte Carlo witness at `r=1.2`. That calculation was stable under nested grids and agreed comfortably with the expected regime structure, but its slow-channel classification still depended on a numerical approximation to a continuous supremum.

The present `r=6` witness is preferable because:

- the slow side is bounded analytically by an exact Rice upcrossing expectation plus a union bound;
- the fast side is bounded from below by a finite sampled subset and Slepian comparison;
- no timing-grid continuum extrapolation is needed;
- no hard-window rough-process calculation appears;
- no rare-event asymptotic approximation is used.

The prior Monte Carlo file `numerics/paper_a_full_template_feasibility.py` remains useful as an independent numerical cross-check but is no longer the controlling Paper-A witness.

---

## 9. What this does NOT establish

The continuum bracket does not provide:

- the numerical value of `L_x`;
- the full finite-duration `X_G(ell)` surface;
- crossover uniqueness;
- a full signal-present scan-power crossover;
- sequential/online acquisition time;
- a general theorem outside the constructed equal-eventual-SNR family;
- novelty.

It also does not reopen Step 49. The full-template witness deliberately avoids the rough finite-window branch.

---

## 10. Paper-A use

The preferred quantitative statement is now:

```text
rho0=3.5, alpha=.05, beta=.90, tau_s/tau_f=6:
known arrival -> fast preferred exactly;
L=9 tau_f=1.5 tau_s ->
    slow PFA <= .0336428 < .05,
    fast PFA >= .0624701 > .05,
    therefore slow-only guarantee feasibility.
```

This is strong enough to answer the severe review's quantitative-example objection without locating `L_x` and without creating Step 50.

---

## Stopping point

The main Paper-A quantitative witness is now continuum-bracketed. The next action is final integrated hostile-review/citation QA and manuscript synchronization to this stronger witness.
