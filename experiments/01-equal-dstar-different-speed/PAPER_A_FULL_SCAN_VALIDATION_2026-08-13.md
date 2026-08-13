# Paper A — full-template exact-scan numerical validation

**Date:** 2026-08-13  
**Status:** NUMERICAL ROBUSTNESS CHECK / COMPLETE SIGNAL-PRESENT SCAN / NOT A FINITE-TIME CROSSOVER THEOREM

## Purpose

Paper A proves a crossover of a conservative sufficient guarantee time through

```math
P_D^{scan}\ge P_{D,true}.
```

A referee correctly asks whether the complete signal-present scan points in the same direction or whether the result could be only a certificate artifact.

The finite-window process is deliberately not used for this check because its hard truncation creates the covariance cusp documented in Steps 13–49. Instead, this calculation uses the smooth **full-template** process at the controlling Paper-A witness.

## Process

For the double-pole family,

```math
R_\infty(y)=(1+|y|)e^{-|y|}.
```

This is the stationary Matérn-3/2 covariance with unit scale. It has the exact state-space realization

```math
\frac{d}{dq}
\begin{bmatrix}Z\\V\end{bmatrix}
=
\begin{bmatrix}0&1\\-1&-2\end{bmatrix}
\begin{bmatrix}Z\\V\end{bmatrix}
+
\begin{bmatrix}0\\2\end{bmatrix}\xi(q),
```

with stationary covariance `Var(Z)=Var(V)=1`, `Cov(Z,V)=0`.

The exact discrete transition over a grid spacing `Delta` is obtained by matrix exponentiation; process noise covariance is computed from stationarity rather than by Euler approximation. Therefore the only continuum approximation is the sampling of the smooth path maximum on the timing grid.

Under a full matched signal at true alignment `q0`, the deterministic scan mean is

```math
m(q)=\rho_0R_\infty(|q-q_0|).
```

Thus the complete signal-present scan is

```math
Y(q)=Z(q)+m(q).
```

For each normalized search length, the 95th percentile of the noise-only grid maximum sets the numerical global threshold (`alpha=.05`), and the complete scan power is

```math
P_D^{scan,\infty}
=\Pr[\max_qY(q)>\Gamma_{grid}].
```

## Parameters

Use the same witness as Paper A:

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=6.
```

At

```math
L=9\tau_f=1.5\tau_s,
```

the normalized search lengths are

```math
\ell_s=1.5,
\qquad
\ell_f=9.
```

Production run:

```text
100000 stationary Gaussian paths
nested timing grids Delta = 0.020, 0.010, 0.005
true-arrival positions q0/L = 0, .25, .50, .75, 1
seed = 2026081307
```

## Results

### Slow channel, ell=1.5

At the finest grid `Delta=.005`, the numerical global threshold is

```text
Gamma_grid = 2.0288572.
```

Complete full-template scan power:

| `q0/L` | `P_D^scan,infinity` |
|---:|---:|
| 0 | 0.94593 |
| .25 | 0.95294 |
| .50 | 0.95468 |
| .75 | 0.95345 |
| 1 | 0.94553 |

All tested placements are comfortably above

```math
\beta=0.90.
```

Grid refinement is negligible: the values at `Delta=.020`, `.010`, and `.005` differ by at most a few `10^-5` to `10^-4` for a fixed placement in this paired run.

### Fast channel, ell=9

At the finest grid `Delta=.005`,

```text
Gamma_grid = 2.5872927.
```

Complete full-template scan power:

| `q0/L` | `P_D^scan,infinity` |
|---:|---:|
| 0 | 0.85658 |
| .25 | 0.88143 |
| .50 | 0.88190 |
| .75 | 0.88473 |
| 1 | 0.85902 |

All tested placements remain below

```math
\beta=0.90.
```

The largest estimate in the tested placement set is `0.88473`; its binomial standard error is approximately `0.00101`, leaving a substantial separation from `0.90`.

The nested-grid values are again essentially stable from `Delta=.020` to `.005`.

## Interpretation

This calculation addresses an important concern without changing the theorem:

```text
slow channel:
  sufficient full-template guarantee says feasible;
  complete full-template scan simulation gives P_D > .90.

fast channel:
  sufficient full-template guarantee says infeasible;
  complete full-template scan simulation gives P_D < .90
  for every tested true-arrival placement.
```

Therefore, at the controlling finite physical timing uncertainty, the complete signal-present scan points in the **same direction** as the conservative guarantee criterion.

This materially reduces the concern that the slow/fast separation is merely an artifact of evaluating the true-alignment certificate.

## What this does not prove

It does **not** establish that

```math
P_D^{scan}(x)
```

is monotone in finite integration duration, nor does it prove the first finite solutions of

```math
P_D^{scan}(x)=\beta
```

reverse ordering.

It is a smooth full-template robustness check, not a theorem of exact finite-time scan crossover.

The finite-window hard-cusp branch remains hard-stopped after Step 49.
