# Paper A — Quantitative Regime Witness Without Crossover Localization

**Date:** 2026-08-12  
**Status:** ROBUST NUMERICAL REGIME WITNESS / EXACT PAPER-A FULL-TEMPLATE FEASIBILITY PROCESS / NOT A NUMERICAL CROSSOVER LOCATION / STEP-49 HARD STOP PRESERVED

---

## 1. Purpose

The adversarial review asked for a quantitative example showing that the analytical fast/slow ordering theorem is not merely formal. Directly locating the finite-duration hard-window crossover was already shown in Steps 13–49 to be numerically delicate because the truncated template produces a locally rough timing scan. That branch is intentionally hard-stopped.

A cleaner quantitative example is available without reopening it. The Paper-A theorem separates two facts:

1. at known event time, both channels solve the same dimensionless finite-duration problem, so the faster channel wins exactly;
2. guarantee feasibility is determined by the **full-template** timing process

```math
R_\infty(y)=(1+|y|)e^{-|y|},
```

which is smooth and does not have the finite-window covariance cusp.

The quantitative witness therefore combines

```text
an exact known-time fast-preferred point
+
a continuum-stable full-template slow-only feasibility point
```

without numerically claiming the exact crossover location.

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
r=\frac{\tau_s}{\tau_f}=1.2.
```

A moderate global false-alarm probability is intentional. The theorem is not restricted to rare `alpha`; this example is designed for transparent ordinary Monte Carlo rather than to repeat the `10^-6` rare-event companion branch.

```text
z_(1-alpha) = 1.64485362695
z_beta      = 1.28155156554.
```

---

## 3. Known arrival: exact fast preference

At `L=0`,

```math
\rho_0\sqrt{\eta(x_0)}-z_{1-\alpha}=z_\beta,
```

with

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

Thus

```math
\sqrt{\eta(x_0)}
=\frac{z_{1-\alpha}+z_\beta}{\rho_0}
=0.836115769285,
```

and

```math
\boxed{x_0=1.80519795247.}
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
=r x_0
=2.16623754297.
}
```

The fast channel is quantitatively and exactly preferred at known arrival time.

---

## 4. Full-template feasibility threshold

The asymptotic guarantee-margin budget is

```math
c=\rho_0-z_\beta=2.21844843446.
```

For the full-template process, define

```math
p_\infty(\ell;c)
=\Pr\left[
\sup_{0\le q\le\ell}Z_\infty(q)>c
\right].
```

At a continuous supremum distribution,

```text
p_infinity(ell;c) < alpha  -> Gamma_infinity(ell,alpha) < c -> feasible,
p_infinity(ell;c) > alpha  -> Gamma_infinity(ell,alpha) > c -> infeasible.
```

---

## 5. One common physical uncertainty produces slow-only feasibility

Choose

```math
\boxed{
L=3.30\,\tau_f=2.75\,\tau_s.
}
```

Hence

```math
\ell_f=3.30,
\qquad
\ell_s=2.75.
```

The reproducible calculation is

```text
numerics/paper_a_full_template_feasibility.py
```

with production defaults

```text
seed       = 20260818
paths      = 240000 paired paths
x_tail     = 16
delta_fine = 0.0025.
```

The simulation synthesizes the stationary moving-average process from

```math
h_\infty(v)=v e^{-v}u(v)
```

and evaluates both nested search lengths on the **same simulated paths**.

At `x_tail=16`, the omitted squared-template-energy fraction is

```math
\boxed{
1-\eta(16)=6.90\times10^{-12}.
}
```

The `0.005` and `0.01` timing grids are exact nested subsets of the `0.0025` grid.

---

## 6. Production numerical result

At

```math
c=2.21844843446,
```

the paired nested-grid results are:

| grid spacing | slow `ell=2.75` PFA | fast `ell=3.30` PFA |
|---:|---:|---:|
| `0.0100` | `0.04733333` | `0.05362917` |
| `0.0050` | `0.04736250` | `0.05365000` |
| `0.0025` | `0.04737083` | `0.05365833` |

On the finest grid, the exact two-sided 95% Clopper-Pearson binomial intervals are

```math
\boxed{
P_{FA,s}
\in[0.0465243,\,0.0482283]
}
```

and

```math
\boxed{
P_{FA,f}
\in[0.0527601,\,0.0545674].
}
```

The target

```math
\alpha=0.05
```

lies cleanly between these intervals.

Therefore the numerical classification is

```math
\boxed{
\text{slow channel guarantee-feasible},
\qquad
\text{fast channel guarantee-infeasible}
}
```

at the **same physical arrival-time uncertainty** `L=3.30 tau_f=2.75 tau_s`.

The paired grid refinement is also benign: relative to `delta=0.01`, the finest grid adds only nine slow exceedances and seven fast exceedances out of `240000` paths. The classification is not a Step-13-type rough-grid knife edge.

---

## 7. What this establishes

For this concrete parameter set:

```text
L=0
-> both guarantee-feasible
-> fast has strictly smaller T_G.
```

At

```text
L=3.30 tau_f=2.75 tau_s
-> slow remains guarantee-feasible
-> fast is already guarantee-infeasible.
```

Proposition 1 then ensures at least one fast-to-slow guarantee-time crossover between the known-time regime and the fast feasibility boundary. The calculation supplies **physical scale and a robust regime witness** without pretending that the precise finite-duration crossover has been numerically localized.

---

## 8. What this does NOT establish

This calculation does not provide:

- the numerical value of `L_x`;
- the full finite-duration `X_G(ell)` surface;
- crossover uniqueness;
- a full signal-present scan-power crossover;
- sequential/online acquisition time;
- a rare-event `alpha=10^-6` continuum certificate;
- any reopening of Step 49.

It does not erase the historical failure of Step 13. The reason this calculation is better conditioned is precisely that guarantee feasibility is governed by the smooth **full-template** process rather than the rough finite-duration truncated-template process.

---

## 9. Paper-A use

This is the preferred quantitative example for the main manuscript:

```text
rho0=3.5, alpha=.05, beta=.90, r=1.2:
known arrival -> fast preferred;
L=3.30 tau_f=2.75 tau_s -> slow-only guarantee feasibility.
```

That is enough to demonstrate a nontrivial finite physical scale while preserving the analytical theorem as the source of crossover existence.

---

## Stopping point

The severe review's quantitative-example objection is resolved without creating Step 50.

The remaining manuscript task is final integrated adversarial/citation QA after the acquisition-lineage prior-art revision.
