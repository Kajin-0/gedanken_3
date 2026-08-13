# Paper A — Quantitative Regime Witness Without Crossover Localization

**Date:** 2026-08-12  
**Status:** ROBUST NUMERICAL REGIME WITNESS / EXACT PAPER-A FULL-TEMPLATE FEASIBILITY PROCESS / NOT A NUMERICAL CROSSOVER LOCATION / STEP-49 HARD STOP PRESERVED

---

## 1. Purpose

The adversarial review asked for a quantitative example showing that the analytical fast/slow ordering theorem is not merely formal. The obvious approach—directly locating the finite-duration hard-window crossover—was already shown in Steps 13–49 to be numerically delicate because the truncated template produces a locally rough timing scan.

That branch is intentionally hard-stopped.

A cleaner quantitative example is available without reopening it.

The Paper-A theorem itself separates two facts:

1. at known event time, both channels solve the same dimensionless finite-duration problem, so the faster channel wins exactly;
2. guarantee feasibility is determined by the **full-template** timing process

```math
R_\infty(y)=(1+|y|)e^{-|y|},
```

which is smooth and does not have the finite-window covariance cusp.

Therefore a useful quantitative regime witness can combine:

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

This deliberately uses a moderate global false-alarm probability rather than the `10^-6` rare-event calibration explored in the mathematical companion. The theorem is not restricted to rare `alpha`; the purpose here is to provide a numerically transparent Paper-A illustration with ordinary Monte Carlo statistics.

The normal quantiles are

```text
z_(1-alpha) = 1.64485362695
z_beta      = 1.28155156554.
```

---

## 3. Known arrival: exact fast preference

At `L=0`, the global timing search collapses to one known alignment. The dimensionless guarantee equation is

```math
\rho_0\sqrt{\eta(x_0)}
-z_{1-\alpha}
=z_\beta,
```

with

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

Equivalently,

```math
\sqrt{\eta(x_0)}
=\frac{z_{1-\alpha}+z_\beta}{\rho_0}
=0.836115769285.
```

The scalar root is

```math
\boxed{x_0=1.80519795247.}
```

Hence, measured in fast-channel time units,

```math
\boxed{
\frac{T_{G,f}(0)}{\tau_f}=1.80519795247,
}
```

whereas

```math
\boxed{
\frac{T_{G,s}(0)}{\tau_f}
=r x_0
=2.16623754297.
}
```

Thus the fast channel is quantitatively and exactly preferred at known arrival time.

---

## 4. Full-template feasibility threshold

The asymptotic guarantee-margin budget is

```math
c
=\rho_0-z_\beta
=2.21844843446.
```

For the full-template process, a normalized search interval `ell` is guarantee-feasible when

```math
\Gamma_\infty(\ell,\alpha)<c.
```

Equivalently, because the full-template supremum has a continuous distribution at the operating point, evaluate the false-alarm probability at threshold `c`:

```math
p_\infty(\ell;c)
=\Pr\left[
\sup_{0\le q\le\ell}Z_\infty(q)>c
\right].
```

Then

```text
p_infinity(ell;c) < alpha  ->  Gamma_infinity(ell,alpha) < c  -> feasible,
p_infinity(ell;c) > alpha  ->  Gamma_infinity(ell,alpha) > c  -> infeasible.
```

---

## 5. One common physical uncertainty produces slow-only feasibility

Choose one physical arrival-time uncertainty

```math
\boxed{
L=3.30\,\tau_f=2.75\,\tau_s.
}
```

Therefore

```math
\ell_f=\frac{L}{\tau_f}=3.30,
\qquad
\ell_s=\frac{L}{\tau_s}=2.75.
```

The two channels have the same full-template covariance in their own dimensionless time coordinate; only the normalized search length differs.

The numerical calculation is implemented in

```text
numerics/paper_a_full_template_feasibility.py
```

with default seed

```text
20260816.
```

The simulation synthesizes the stationary moving-average process from

```math
h_\infty(v)=v e^{-v}u(v)
```

and evaluates the two nested search lengths on the **same simulated paths**.

For numerical convolution, the template is truncated at

```text
x_tail = 12,
```

for which the omitted squared-template-energy fraction is only

```math
1-\eta(12)
=1.1816171\times10^{-8}.
```

The finest timing grid is

```text
delta = 0.0025,
```

and coarser `0.005` and `0.01` grids are exact nested subsets of the same fine-grid paths.

Number of paths:

```text
120000.
```

---

## 6. Numerical result

At the common threshold

```math
c=2.21844843446,
```

the nested-grid results are:

| grid spacing | slow `ell=2.75` PFA | fast `ell=3.30` PFA |
|---:|---:|---:|
| `0.0100` | `0.04720833` | `0.05392500` |
| `0.0050` | `0.04724167` | `0.05395833` |
| `0.0025` | `0.04724167` | `0.05395833` |

On the finest grid, the exact two-sided 95% Clopper-Pearson binomial intervals are

```math
\boxed{
P_{FA,s}
\in[0.0460481,\,0.0484572]
}
```

and

```math
\boxed{
P_{FA,f}
\in[0.0526866,\,0.0552516].
}
```

The required global false-alarm probability

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

Grid refinement changes only four slow and four fast threshold classifications between `delta=0.01` and `0.005`, and none between `0.005` and `0.0025` in this paired run. The sign is therefore not a rough-grid knife edge of the Step-13 type.

---

## 7. What this establishes

For this concrete parameter set:

### At known arrival

```text
L = 0
-> both channels guarantee-feasible
-> fast channel has strictly smaller T_G.
```

### At a finite physical uncertainty

```text
L = 3.30 tau_f = 2.75 tau_s
-> slow channel remains guarantee-feasible
-> fast channel is already guarantee-infeasible.
```

Because Proposition 1 gives continuity of the guarantee-time ordering through the feasible interior and divergence of the fast guarantee time at its feasibility boundary, the quantitative example places at least one fast-to-slow guarantee-time crossover somewhere between these regimes.

The example therefore supplies **physical scale and a robust regime witness** without pretending that the precise hard-window crossover has been numerically localized.

---

## 8. What this does NOT establish

This calculation does not provide:

- the numerical value of `L_x`;
- the full finite-duration `X_G(ell)` surface;
- a proof of crossover uniqueness;
- a full signal-present scan-power crossover;
- a sequential/online acquisition-time result;
- a rare-event `alpha=10^-6` continuum certificate;
- a reopening of Step 49.

It also does not erase the historical failure of Step 13. The reason this calculation is numerically better conditioned is precisely that the guarantee-feasibility boundary is governed by the smooth **full-template** process rather than the rough finite-duration truncated-template process.

---

## 9. Paper-A use

This is the preferred quantitative example for the main manuscript.

The manuscript should report it as a **regime witness**, not a measured crossover:

```text
rho0=3.5, alpha=.05, beta=.90, r=1.2:
known arrival -> fast preferred;
L=3.30 tau_f=2.75 tau_s -> slow-only guarantee feasibility.
```

That is enough to demonstrate a nontrivial finite physical scale while preserving the exact analytical theorem as the source of crossover existence.

---

## Stopping point

The severe review's quantitative-example objection can now be answered without creating Step 50.

The remaining substantive Paper-A issue is the closest-prior-art / novelty audit, especially classical delay/code-phase acquisition theory and optical acquisition literature.
