# Step 33 — Excursion-Cluster Moment Enclosure Through the Rough Endpoint

**Date:** 2026-08-11 21:49 EDT  
**Status:** DERIVED / CLUSTER-RENORMALIZED ENCLOSURE / NUMERICAL VALIDATION / PARTIAL CERTIFICATE / OPEN. Step 32 showed that ordinary first/second upcrossing moments lose sharpness when one physical high excursion contains many microscopic level crossings. This step replaces the raw level-crossing count by a finite-amplitude excursion-cluster count. The resulting upper/lower probability enclosure is exact for continuous paths, does not use derivatives, and remains well-defined at the nondifferentiable `kappa=infinity` endpoint. A lower-level occupation-Palm identity gives the first two cluster moments without sampling a `10^-6` event directly. For the original `r=2`, `Lambda=0.895` calibration, the cluster enclosure numerically separates fast and slow at `kappa_f=300`, `1000`, and directly at the rough endpoint, thereby bridging beyond the Step-32 micro-upcrossing failure. The moment inequalities are exact; the reported cluster moments are Monte Carlo/grid estimates rather than formal interval arithmetic. No novelty claim.

---

## 1. Why raw upcrossings are the wrong high-band variable

Step 32 used the level-`u` upcrossing count `N_u^+`. At large finite bandwidth,

```math
E[N_u^+(N_u^+-1)]
```

grows because one physical excursion is split into many microscopic recrossings. The event probability remains finite, but the crossing-count second moment does not remain informative.

The replacement should satisfy two requirements:

1. one physical high excursion should count approximately once even when its boundary becomes rough;
2. the variable should still identify the exact event `sup z > u`.

A fixed **amplitude** separation does this more naturally than a fixed time separation.

---

## 2. Finite-amplitude excursion clusters

Choose any fixed

```math
\Delta>0,
```

and define the lower level

```math
\boxed{a=u-\Delta.}
```

For one continuous path on `[0,ell]`, decompose the lower excursion set

```math
E_a=\{t\in[0,\ell]:z(t)>a\}
```

into its connected components `I_j`.

Call component `I_j` **successful** when

```math
\sup_{t\in I_j}z(t)>u.
```

Define

```math
\boxed{
C_\Delta
=\sum_j 1_{\{\sup_{I_j}z>u\}}.
}
```

Every level-`u` exceedance lies inside exactly one lower-level component. Therefore, path by path,

```math
\boxed{
\sup_{0\le t\le\ell}z(t)>u
\iff
C_\Delta\ge1.
}
```

Hence

```math
\boxed{
P_{FA}=P(C_\Delta\ge1).
}
```

No separate endpoint term is needed: a successful component touching either endpoint is counted automatically.

---

## 3. Why `C_Delta` survives the rough limit

For a continuous path on a compact interval, uniform continuity implies that a full amplitude change of at least `Delta` cannot occur on arbitrarily small path-dependent time scales everywhere. Distinct successful lower-level components must be separated by a return to `z<=a` and a later rise above `u=a+Delta`.

Thus, for every fixed `Delta>0`,

```math
\boxed{C_\Delta<\infty\quad\text{a.s.}}
```

for the continuous rough endpoint as well as every smooth finite-band process.

This is the essential renormalization: the number of microscopic level-`u` crossings may diverge, but the number of lower-level excursion components that traverse a nonzero amplitude gap does not.

A publication-grade uniform moment theorem for the full Gaussian family is still open; the numerical work below tests the first two moments directly through the endpoint.

---

## 4. Exact moment enclosure

Because `C_Delta` is a nonnegative integer and the false-alarm event is exactly `{C_Delta>=1}`,

```math
P_{FA}\le E[C_\Delta].
```

Cauchy–Schwarz / Paley–Zygmund at zero gives

```math
P_{FA}
\ge
\frac{E[C_\Delta]^2}{E[C_\Delta^2]}.
```

Therefore

```math
\boxed{
\frac{E[C_\Delta]^2}{E[C_\Delta^2]}
\le P_{FA}
\le E[C_\Delta].
}
```

Unlike Step 32, there is no `lambda_2` divergence from micro-upcrossing multiplicity.

---

## 5. Lower-level occupation-Palm representation

The cluster moments can be estimated without directly simulating a probability of order `10^-6`.

Choose `T` uniformly on `[0,ell]` and condition on

```math
z(T)>a.
```

Call the resulting measure `Q_a`. Its normalization is exactly

```math
m_a
=E\!\left[\int_0^\ell1_{\{z(t)>a\}}dt\right]
=\ell Q(a)
```

by stationarity.

Under `Q_a`, let

- `I(T)` be the lower-level component containing the selected time;
- `L` be the duration of `I(T)` inside `[0,ell]`;
- `S=1` if `I(T)` is successful, otherwise `0`;
- `C_Delta` be the total successful-component count for that path.

Fubini over each connected component gives the exact identities

```math
\boxed{
E[C_\Delta]
=\ell Q(a)
E_{Q_a}\!\left[\frac{S}{L}\right]
}
```

and

```math
\boxed{
E[C_\Delta^2]
=\ell Q(a)
E_{Q_a}\!\left[\frac{S C_\Delta}{L}\right].
}
```

Proof of the first identity: on a successful component `I_j`, integrating `1/L_j` over the component gives exactly one. Summing over all components gives `C_Delta`. The second identity replaces `1/L_j` by `C_Delta/L_j`, so each successful component contributes `C_Delta` and the total is `C_Delta^2`.

This is the cluster analogue of Step 23's occupation-time importance sampling, but now the weighting level is `a=u-Delta`, not the final decision level.

---

## 6. Why the importance variable is better conditioned

The Step-23 exact occupation estimator at level `u` contains `1/V_u`, where an arbitrarily short level-`u` occupation can create a large weight.

Here a selected component contributes only when it traverses the finite amplitude gap

```math
u-a=\Delta.
```

For the rough endpoint, a successful cluster therefore has a macroscopic excursion scale set by `Delta` and the local cusp coefficient rather than by the vanishing finite-band smoothing scale.

The numerical consequence is that the cluster moments remain stable while raw level-`u` crossing multiplicity grows.

---

## 7. Numerical implementation

The helper

```text
numerics/excursion_cluster_moment_enclosure.py
```

uses the same stationary Gaussian spectra as the preceding steps.

For either finite `kappa` or `kappa=infinity` it:

1. chooses a uniform search-window time;
2. conditions the Gaussian path at that time on `z>a`;
3. identifies connected components of `{z>a}` on a fine grid;
4. marks components whose sampled maximum exceeds `u`;
5. computes `S/L`, `S C_Delta/L`, and therefore `E[C_Delta]`, `E[C_Delta^2]`;
6. reports the Paley–Zygmund lower bound and first-moment upper bound.

Component endpoint times are linearly interpolated through the level `a` to reduce duration bias. Grid refinement is still required because an unresolved between-sample maximum can affect success classification.

The calculations below use

```text
Delta = 0.15
X     = 7.16
Lambda= 0.895.
```

`Delta` is a numerical declustering parameter only. The exact event `{C_Delta>=1}` is independent of its value for every `Delta>0`; the sharpness and estimator variance can depend on `Delta`.

---

## 8. Finite high-band validation beyond the Step-32 failure

For the original task, cluster-Palm calculations at common physical time `X=7.16` give representative moment enclosures:

```text
kappa_f    detector    lower/alpha    upper/alpha    SE[E(C)]/alpha
--------------------------------------------------------------------
300        fast          0.98604        0.98624          0.00679
300        slow          1.19896        1.19990          0.00721

1000       fast          0.98417        0.98423          0.00673
1000       slow          1.21537        1.21725          0.00729
```

These use `20000` lower-level occupation-Palm paths per detector and timing spacing approximately `0.001`.

The important feature is not the last decimal. It is the collapse of the cluster moment interval:

```text
E[C_Delta^2] ~= E[C_Delta]
```

at this rare-event level, because paths with two separate successful amplitude-`Delta` clusters are themselves rare. Thus the first-moment upper and second-moment lower bounds are nearly identical even though the raw level-crossing second moment has already become unusable.

**NUMERICAL VALIDATION / PARTIAL CERTIFICATE:** at both tested finite high-band points, fast's cluster upper estimate lies below `alpha` while slow's cluster lower estimate lies far above `alpha` at the same physical time. The moment inequalities are exact; the displayed moment values have Monte Carlo/grid uncertainty.

---

## 9. Direct rough-endpoint cluster enclosure

The same calculation can be run with the Gaussian information cutoff removed entirely.

At

```text
kappa_f = infinity
X       = 7.16
Lambda  = 0.895
Delta   = 0.15
```

using `50000` occupation-Palm paths and grid spacing about `0.001`, the estimates are

```text
             lower/alpha    upper/alpha    SE[E(C)]/alpha
fast           0.98940        0.98968          0.00429
slow           1.22367        1.22583          0.00474
```

Thus the cluster variable remains finite and sharply concentrated all the way at the nondifferentiable endpoint.

For the fast channel, even a one-sided `1.645 SE` allowance on the estimated **upper moment** gives approximately

```text
0.98968 + 1.645(0.00429) ~= 0.9967 < 1.
```

The slow lower estimate exceeds one by more than forty times the quoted `E[C]` standard error scale.

**NUMERICAL ENDPOINT CERTIFICATE:** within the Monte Carlo/grid calculation, the fast detector is feasible and the slow detector infeasible at the same `X=7.16` even at `kappa=infinity`. This is independent of the Step-31 empirical `delta(kappa)` bridge and uses no derivative-based crossing statistic.

It is not formal interval arithmetic or an exact confidence statement for the lower-bound estimator; the quoted standard error is for `E[C_Delta]`.

---

## 10. Rough-grid refinement

At the rough endpoint, `12000`-path checks give

```text
grid       fast lower-upper/alpha        slow lower-upper/alpha
----------------------------------------------------------------
~0.002     0.98947 – 0.98980             1.20599 – 1.20687
~0.0015    0.99303 – 0.99347             1.22075 – 1.22366
~0.001     0.98488 – 0.98510             1.22706 – 1.22865
```

The fast variation is comparable with the Monte Carlo error of these shorter runs. The slow estimate shows a visible grid trend but remains far above `alpha`; the `50000`-path `~0.001` result is consistent with the finest-grid scale.

Further nested-grid extrapolation would be required for precision boundary work.

---

## 11. First nontrivial consequence

The high-band divergence in Step 32 was a property of the **chosen counting variable**, not of the excursion event.

Replacing

```math
N_u^+
```

by

```math
C_\Delta
```

changes the moment problem from

```text
one physical excursion -> many counted objects as kappa grows
```

to

```text
one physical excursion -> approximately one counted amplitude cluster.
```

The resulting first/second moment enclosure remains sharp at `kappa_f=300`, `1000`, and directly at `kappa=infinity` in the tested calibration.

This bridges the Step-32 finite-threshold method into the rough endpoint without using Rice micro-upcrossing multiplicity.

---

## 12. What remains open

- a statistically and numerically certified enclosure on the entire continuous interval `170 < kappa_f < infinity`, rather than representative finite points plus the endpoint;
- optimization of `Delta` for estimator variance and numerical conditioning;
- deterministic or formal interval evaluation of the cluster moments;
- a proof of uniform first/second cluster-moment bounds over the finite-band-to-rough family;
- precision nested-grid extrapolation of the rough cluster moment estimates;
- extension to other `Lambda`, `r`, SNR, and detector models;
- hardware interpretation;
- novelty.

---

## 13. Stopping point

A cluster-renormalized finite-`u` variable has now been found. It removes the micro-upcrossing divergence and directly reaches the rough endpoint.

### Single natural next question

> Can the excursion-cluster enclosure be evaluated on an adaptive bandwidth grid with controlled Monte Carlo/grid error and an optimized `Delta`, so that the remaining continuous interval from the Step-32 certificate (`kappa_f~170`) to the rough endpoint is closed without the empirical Step-31 boundary fit?
