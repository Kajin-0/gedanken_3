# Step 36 — Tail-Sensitive Cluster-Maximum Strip Continuity

**Date:** 2026-08-11 23:04 EDT  
**Status:** DERIVED / TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION / REFINEMENT / OPEN. Step 35 proved that the Gaussian timing field is regular in `q=kappa_f^(-1/2)` but found that generic Gaussian-supremum anti-concentration is useless at `alpha=1e-6`. This step fixes the lower declustering level and studies the maxima of the resulting physical excursion clusters. The probability that the global maximum lies in a narrow threshold strip is bounded by the expected number of fixed lower-level clusters whose maxima lie in that strip. That expected strip count has an exact occupation-Palm representation and remains well-defined at the rough endpoint. Numerically, for the Step-34 fast channel, the local cluster-maximum strip intensity near `u~4.959` is about `5 alpha` per unit threshold over `kappa_f=170,300,1000,infinity`, i.e. it follows the rare-event scale rather than the order-one global anti-concentration scale. A uniform analytic density/hazard bound is still open. No novelty claim.

---

## 1. Freeze the declustering geometry

Step 33 defined a lower level

```math
a=u-\Delta
```

and then used components of `{t:z(t)>a}` to count successful excursions above `u`.

For continuity in the success threshold, do **not** move `a` with the threshold. Fix one lower level `a` and let `I_j` be the connected components of

```math
E_a=\{t\in[0,\ell]:z(t)>a\}.
```

Let

```math
M_j=\sup_{t\in I_j}z(t)
```

be the maximum of component `I_j`.

For any success threshold `y>a`, define

```math
\boxed{
C_a(y)=\sum_j1_{\{M_j>y\}}.
}
```

Then, pathwise,

```math
\boxed{
\sup_{0\le t\le\ell}z(t)>y
\iff
C_a(y)\ge1.
}
```

Thus the same fixed collection of physical excursion components can be used while `y` varies in a narrow neighborhood of the decision threshold.

---

## 2. Exact cluster strip count

For

```math
a<y_1<y_2,
```

define

```math
\boxed{
D_a(y_1,y_2)
=C_a(y_1)-C_a(y_2)
=\sum_j1_{\{y_1<M_j\le y_2\}}.
}
```

This counts fixed lower-level excursion components whose maxima lie inside the success-threshold strip `(y_1,y_2]`.

If the global maximum lies inside that strip, at least one lower-level component has a maximum inside the strip. Therefore

```math
\{y_1<\sup z\le y_2\}
\subseteq
\{D_a(y_1,y_2)\ge1\}.
```

Hence

```math
\boxed{
P(y_1<\sup z\le y_2)
\le
P(D_a\ge1)
\le
E[D_a(y_1,y_2)].
}
```

This is a finite-threshold anti-concentration bound tailored to successful physical excursion clusters.

No differentiability, Rice crossing count, Pickands limit, or global Gaussian-supremum density bound is used.

---

## 3. Exact occupation-Palm strip identity

Use the Step-33 lower-level occupation-Palm law `Q_a`: choose a uniform time `T` in `[0,ell]` and condition on

```math
z(T)>a.
```

Its normalization is

```math
m_a=\ell Q(a).
```

Let

- `I(T)` be the lower-level component containing `T`;
- `L` be its duration inside the search interval;
- `M_I` be its maximum.

Fubini over components gives

```math
\boxed{
E[D_a(y_1,y_2)]
=
\ell Q(a)
E_{Q_a}\!\left[
\frac{1_{\{y_1<M_I\le y_2\}}}{L}
\right].
}
```

Proof: on one component with maximum in `(y_1,y_2]`, integrating `1/L_j` over that component gives exactly one. Components with maxima outside the strip contribute zero.

This identity remains meaningful at `kappa=infinity` because it contains no derivative or level-crossing multiplicity.

---

## 4. Cluster-maximum intensity measure

Define a finite measure on success-threshold height by

```math
\boxed{
\nu_a(B)
=
\ell Q(a)
E_{Q_a}\!\left[
\frac{1_{\{M_I\in B\}}}{L}
\right].
}
```

Then

```math
E[C_a(y)]=\nu_a((y,\infty)),
```

and the threshold-strip inequality is simply

```math
\boxed{
P(y_1<\sup z\le y_2)
\le
\nu_a((y_1,y_2]).
}
```

This is the correct tail-sensitive replacement for the global anti-concentration quantity used and rejected in Step 35.

If `nu_a` has a locally bounded density `h_a(y)` near the decision level, then automatically

```math
P(u-\delta<\sup z\le u+\delta)
\le
2\delta\sup_{|y-u|\le\delta}h_a(y).
```

**OPEN:** this step does not yet prove a uniform density bound for the full finite-band-to-rough family. The measure representation itself is exact.

---

## 5. Numerical strip-intensity diagnostic

The helper

```text
numerics/cluster_maximum_strip.py
```

uses the same lower-level occupation-Palm proposal as Step 33 but records the selected component maximum rather than only success/failure.

For the Step-34 fast detector,

```text
x      = 7.16
ell    = 0.895
Delta  = 0.15
u      ~= 4.959
alpha  = 1e-6
```

we estimate

```math
\frac{\nu_a((u-w,u+w])}{2w\alpha}
```

for moderate diagnostic half-widths `w=0.005,0.01,0.02`.

Representative `12000`-path calculations on timing spacing about `0.0015` give

```text
kappa_f     w=.005     w=.010     w=.020
------------------------------------------
170          4.97        4.95        5.16
300          5.17        5.06        5.03
1000         5.54        5.31        5.17
infinity     5.53        5.32        5.19
```

The independent `20000`-path rough-endpoint check gives the same scale, about `5.1–5.5` over these widths.

**NUMERICAL VALIDATION:** the cluster-maximum strip intensity is approximately

```math
\boxed{
h_a(u)\sim5\alpha\quad\text{per unit threshold}}
```

for this calibration across the finite high-band tail and rough endpoint.

This is close numerically to the decision level `u~4.96`, but no universal identity `h_a(u)=u alpha` is claimed.

---

## 6. Rare-event scaling versus global anti-concentration

Step 35's global Gaussian-supremum bound scales like

```math
O(\delta)
```

with an order-one coefficient, so a `1e-4` strip already produced a useless `O(1e-4)` probability bound.

The fixed-cluster strip measure instead gives, for the present calibration,

```math
\nu_a((u-\delta,u+\delta])
\approx
(2\delta)(5\alpha)
=10\delta\alpha.
```

Thus a **numerical linear extrapolation** to

```math
\delta=10^{-4}
```

would give

```math
\boxed{
\nu_a((u-\delta,u+\delta])
\sim10^{-3}\alpha
\sim10^{-9}
}
```

rather than `O(1e-4)`.

This is precisely the rare-event scale needed for the Step-34/35 continuity problem.

**QUALIFICATION:** the `delta=1e-4` value is an extrapolation from wider diagnostic strips. A rigorous local density bound at that width has not yet been established.

---

## 7. Coupling consequence

Recall Step 35. If two bandwidth coordinates `q,r` are coupled so that

```math
||z_q-z_r||_infinity<=epsilon
```

except with probability `eta`, and

```math
\delta=\epsilon+|u_q-u_r|,
```

then

```math
p_q(u_q+\delta)-\eta
\le p(r)\le
p_q(u_q-\delta)+\eta.
```

With the fixed lower level `a<u_q-\delta`, the threshold-motion pieces now obey

```math
p_q(u_q-\delta)-p_q(u_q)
\le\nu_{a,q}((u_q-\delta,u_q]),
```

```math
p_q(u_q)-p_q(u_q+\delta)
\le\nu_{a,q}((u_q,u_q+\delta]).
```

Therefore the inter-band continuity problem has been reduced to two quantities:

1. a sup-norm coupling tail `eta`;
2. a **rare cluster-maximum strip measure** `nu_a`, whose observed scale is `O(alpha delta)` rather than `O(delta)`.

This is a materially sharper decomposition than Step 35's global anti-concentration route.

---

## 8. First nontrivial consequence

A tail-sensitive buffered-threshold bound now exists in exact finite-threshold form:

```math
\boxed{
P(y_1<\sup z\le y_2)
\le
\ell Q(a)
E_{Q_a}\!\left[
\frac{1_{\{y_1<M_I\le y_2\}}}{L}
\right].
}
```

For the original fast high-band trajectory, numerical evaluation shows that the right-hand side carries the rare-event scale `~alpha`, not an order-one Gaussian density.

Thus the anti-concentration obstruction identified in Step 35 is not intrinsic. The correct variable is the maximum of a physical finite-amplitude excursion cluster.

---

## 9. What remains open

- prove a locally uniform density/hazard bound for `nu_{a,q}` over `0<=q<=0.0767`;
- determine whether one can bound `h_{a,q}(u)` directly by a multiple of `u E[C_a(u)]` or another rare-event intensity;
- derive a sharp analytic sup-norm coupling tail `eta` for adjacent `q` values;
- combine the two into a theorem-level inter-node probability enclosure;
- formal interval/concentration treatment of numerical cluster-strip estimates;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 10. Stopping point

The threshold-buffer part of the Step-35 continuity problem has been converted from a global Gaussian anti-concentration problem into a fixed-excursion-cluster maximum measure. The observed strip intensity is on the correct rare-event scale.

### Single natural next question

> Can the local cluster-maximum intensity `h_{a,q}(u)` be bounded analytically and uniformly over the high-band `q` interval—ideally by a rare-event hazard form such as `h_{a,q}(u) <= C u E[C_a(u)]`—so that the buffered-threshold term becomes theorem-level rather than numerically extrapolated?
