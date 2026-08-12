# Step 34 — Adaptive Paired Excursion-Cluster Closure of the High-Band Tail

**Date:** 2026-08-11 22:22 EDT  
**Status:** DERIVED / PAIRED NUMERICAL INTERVAL CLOSURE / REFINEMENT / OPEN. Step 33 replaced divergent level-`u` micro-upcrossing counts by finite-amplitude excursion clusters and showed sharp finite-`u` moment enclosures at representative high bandwidths and directly at `kappa_f=infinity`. This step removes the remaining large Monte Carlo cost of scanning every bandwidth independently. It uses the natural high-band coordinate `q=kappa_f^(-1/2)`, common-random-number coupling of the cluster **upper moment** to the rough endpoint, a lower-cost absolute scan of the slow cluster **lower moment**, and a paired nested-grid check of the rough endpoint. For the original `r=2`, `Lambda=0.895` task, the resulting conservative numerical envelope separates fast and slow over the full sampled/interpolated tail `170 <= kappa_f <= infinity` without the empirical Step-31 `delta(kappa)` boundary fit. This is a numerical interval closure with explicit Monte Carlo/grid/inter-node allowances, not formal interval arithmetic or a theorem of continuous-parameter monotonicity. No novelty claim.

---

## 1. Why use `q = kappa_f^(-1/2)`

Steps 26–30 showed that the high-band corrections naturally contain powers of

```math
kappa_f^{-1/2}.
```

Define

```math
\boxed{q=\kappa_f^{-1/2}.}
```

Then

```text
q = 0          <-> kappa_f = infinity
q = 0.0767     <-> kappa_f ~= 170.
```

The entire unresolved Step-33 tail therefore becomes one finite interval

```math
0\le q\le0.0767.
```

This is numerically better conditioned than trying to adapt directly on an unbounded `kappa_f` axis.

---

## 2. Declustering gap screen

Step 33 used

```math
Delta=0.15.
```

A preliminary lower-level occupation-Palm screen at `X=7.16`, timing spacing about `0.0015`, and `2500` paths per detector compared

```text
Delta = 0.08, 0.12, 0.15, 0.20, 0.25
```

at `kappa_f=200` and `infinity`.

The broad result was:

- `Delta~0.08–0.15` gives the lowest Monte Carlo variance;
- smaller `Delta` modestly increases the successful-multiple-cluster fraction but it remains of order `10^-3–10^-2`;
- `Delta>=0.20` clearly increases variance because the lower-level occupation proposal succeeds less often;
- the screen does **not** resolve a unique optimum.

**REFINEMENT:** retain

```math
\boxed{Delta=0.15}
```

as the conservative working value because Step 33 already validated it on the finest rough-endpoint grid and its successful-multiple-cluster fraction is essentially negligible. Do not call `0.15` a mathematically optimal declustering gap.

---

## 3. Adaptive witness time

To establish

```math
T_{D,f}<T_{D,s}
```

at a given bandwidth, it is unnecessary to evaluate both detectors exactly at either detector's decision time. It is enough to find any common physical time `X` such that

```math
P_{FA,f}^{upper}(X)<alpha<P_{FA,s}^{lower}(X).
```

This freedom increases the statistical margin. Representative direct Step-33 cluster calculations give, for example:

```text
kappa_f   X      fast upper/alpha   SE upper/alpha   slow lower/alpha   SE lower/alpha
--------------------------------------------------------------------------------------
180       7.18       0.98215            0.00670          1.18354            0.00721
200       7.20       0.98664            0.00669          1.16833            0.00715
250       7.18       0.98740            0.00675          1.19268            0.00719
500       7.50       0.97916            0.00864          1.05629            0.00833
2000      7.50       0.97723            0.00950          1.08798            0.00943
```

Using a one-sided Gaussian Monte Carlo allowance `z=1.645`, the corresponding witness inequalities remain separated at these points. These are **pointwise numerical certificates**, not yet the tail-wide construction below.

---

## 4. Common-random-number endpoint coupling

The fast cluster upper moment is the limiting quantity because it lies much closer to `alpha` than the slow lower moment.

Let

```math
U_f(q)=E[C_Delta(q)]
```

be the fast first cluster moment at fixed

```text
X      = 7.16
Lambda = 0.895
Delta  = 0.15.
```

Instead of estimating every `U_f(q)` independently, generate all finite-`q` fields from the **same white-noise realization**, the same truncated-normal uniform, and the same selected occupation time as the rough endpoint `q=0`.

Each marginal sample is still distributed according to its correct lower-level occupation-Palm law. Therefore

```math
\boxed{
E[\widehat U_f(q)-\widehat U_f(0)]
=U_f(q)-U_f(0)
}
```

while the common randomness makes the difference variance much smaller than the variance of either absolute estimate.

This is a control-variate / common-random-number construction; it changes only estimator variance, not the cluster moment definition.

---

## 5. Dense paired `q` scan

Use the endpoint anchor from Step 33:

```text
kappa_f=infinity, X=7.16, Delta=0.15, ~0.001 grid, 50000 paths
U_f(0)/alpha = 0.98968
SE[U_f(0)]/alpha = 0.00429.
```

Now estimate only

```math
Delta U_f(q)=U_f(q)-U_f(0)
```

with `3000` common-random-number paths on

```text
q = 0,
    0.005, 0.010, 0.015, ..., 0.075,
    0.0767.
```

Representative paired corrections are

```text
q        kappa_f approximately     Delta U_f/alpha
---------------------------------------------------
0.000       infinity                    0
0.025       1600                       -0.00048
0.040        625                       -0.00045
0.050        400                       -0.00070
0.060        278                       -0.00060
0.065        237                       -0.00115
0.070        204                       -0.00159
0.075        178                       -0.00152
0.0767       170                       -0.00188
```

The largest positive sampled correction is numerically negligible:

```text
max Delta U_f/alpha ~= +1.9e-8
```

and the largest paired standard error is

```text
max SE[Delta U_f]/alpha ~= 0.00106.
```

Additional midpoints in the steepest part of the profile,

```text
q = 0.0625, 0.0675, 0.0725, 0.07585,
```

also give negative paired corrections within their uncertainties.

The maximum absolute change between adjacent `0.005` grid nodes is approximately

```text
0.000548 alpha.
```

Thus the finite-band fast cluster upper moment does not show an upward excursion above the rough endpoint anywhere on the adaptive `q` mesh.

---

## 6. Paired rough-grid error check

The rough endpoint anchor itself still has time-discretization error. To isolate it from Monte Carlo noise, generate one conditioned rough path on a fine grid and evaluate the **same path** on nested sampled grids.

A `4000`-path paired check at `X=7.16`, `Delta=0.15` gives

```text
grid spacing      coarse-minus-fine U_f / alpha      paired SE / alpha
-----------------------------------------------------------------------
~0.00150                    -0.000929                    0.000655
~0.00300                    -0.001341                    0.000778
```

relative to a fine spacing

```text
~0.000751.
```

The absolute Monte Carlo level in this small paired run is irrelevant; only the paired grid differences are used.

A conservative numerical grid allowance

```math
\boxed{epsilon_grid,f=0.002\,alpha}
```

therefore exceeds the observed paired shift between the finest and coarser tested grids.

---

## 7. Fast tail-wide numerical envelope

Combine:

1. endpoint anchor
   ```text
   U_f(0)/alpha = 0.98968 +/- 0.00429;
   ```
2. worst paired finite-`q` standard error
   ```text
   0.00106;
   ```
3. one-sided Gaussian Monte Carlo factor
   ```text
   z = 1.645;
   ```
4. conservative rough-grid allowance
   ```text
   0.002;
   ```
5. conservative inter-node allowance larger than the maximum observed adjacent change
   ```text
   0.0006.
   ```

Using independent endpoint-anchor and paired-profile runs,

```math
\sigma_{comb}/\alpha
=\sqrt{0.00429^2+0.00106^2}
\approx0.004419.
```

Therefore

```math
\boxed{
\frac{U_f(q)}{\alpha}
\lesssim
0.98968
+1.645(0.004419)
+0.002
+0.0006
\approx0.99955
}
```

through the sampled/interpolated interval

```math
0\le q\le0.0767
\quad\Longleftrightarrow\quad
170\lesssim\kappa_f\le\infty.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** this is an explicit conservative numerical envelope assembled from measured Monte Carlo, grid, and mesh-variation scales. It is not a rigorous probability confidence interval or formal interval bound on every unsampled `q`.

---

## 8. Slow tail-wide lower envelope

The slow cluster lower bound is much farther from the decision threshold, so an absolute scan is sufficient.

Using `3000` occupation-Palm paths at the same `q` nodes and `X=7.16` gives

```text
q        kappa_f approximately     slow lower/alpha
---------------------------------------------------
0.000       infinity                  1.22933
0.020       2500                      1.22424
0.040        625                      1.19991
0.060        278                      1.18709
0.070        204                      1.18581
0.0767       170                      1.18296
```

The largest Monte Carlo lower-bound standard error on this scan is approximately

```text
0.01949 alpha.
```

The maximum adjacent `q`-node change is about

```text
0.0165 alpha.
```

Even with deliberately conservative allowances

```text
one-sided MC: 1.645 * 0.01949
rough/grid allowance: 0.03
inter-node allowance: 0.02,
```

we obtain

```math
\boxed{
\frac{L_s(q)}{\alpha}
\gtrsim
1.18296
-1.645(0.01949)
-0.03
-0.02
\approx1.101.
}
```

Thus the slow cluster lower envelope remains far above the false-alarm requirement across the same tail.

---

## 9. First nontrivial consequence

For the original calibration, the Step-33 pointwise cluster construction can be turned into a **tail-wide paired numerical enclosure** in the natural coordinate `q=kappa_f^(-1/2)`.

At the common witness time

```math
X=7.16,
```

the conservative envelopes are approximately

```math
\boxed{U_f/\alpha\lesssim0.99955<1,}
```

```math
\boxed{L_s/\alpha\gtrsim1.10>1.}
```

for the entire adaptively sampled/interpolated interval

```math
\boxed{170\lesssim\kappa_f\le\infty.}
```

Combined with the Step-32 direct finite-`u` certificate through `kappa_f=170`, this removes the empirical Step-31 `delta(kappa)` bridge from the original high-band preference conclusion.

The surviving one-dimensional topology for the stated `Lambda=0.895` task is therefore numerically supported by direct finite-`u` enclosures on both sides of the Step-32/33 handoff:

```text
slow preferred at low bandwidth
-> one validated switch near kappa_f~21.7
-> fast preferred through the entire high-band tail to kappa_f=infinity.
```

**Important:** this remains a numerical interval closure, not a proof that no arbitrary unsampled continuous-parameter pathology can exist.

---

## 10. What remains open

- a theorem-level continuity modulus in `q` for the cluster moments, replacing the empirical inter-node allowance;
- formal confidence-sequence or concentration bounds for the weighted occupation-Palm estimator rather than Gaussian SE allowances;
- formal interval arithmetic for spectral/grid discretization;
- proof of uniform first/second cluster-moment control over the finite-band-to-rough family;
- extension to other `Lambda`, `r`, SNR, and detector models;
- hardware interpretation;
- novelty.

---

## 11. Stopping point

The original high-band re-entrant-pocket question is no longer dependent on the empirical Step-31 boundary fit. The remaining gap is mathematical certification of the numerical allowances themselves, especially continuity between `q` nodes.

### Single natural next question

> Can the common-white-noise coupling be converted into an analytic continuity modulus for the excursion-cluster moments as a function of `q=kappa_f^(-1/2)`, replacing the empirical `0.0006` inter-node allowance and turning the Step-34 numerical tail closure into a theorem-level parameter-interval enclosure?
