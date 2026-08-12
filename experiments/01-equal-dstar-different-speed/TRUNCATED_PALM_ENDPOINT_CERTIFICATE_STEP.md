# Step 44 — Truncated Occupation-Palm Finite-Grid Endpoint Certificate

**Date:** 2026-08-12 18:18 EDT  
**Status:** RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE / NUMERICAL RUN / REFINEMENT / OPEN. Step 43 showed that successful clusters shorter than `L0=.02` contribute less than `3.9e-11` absolute false-alarm probability. This step performs the dedicated `L0=.02` long-cluster occupation-Palm calculation requested by Step 43 and applies the Maurer-Pontil empirical-Bernstein inequality directly to the pooled bounded per-path contributions. Four independent batches of `50000` paths (`n=200000` total) give pooled `E[C_long]` estimate `0.992616066 alpha`, sample SD `9.61850e-7`, and a 95% one-sided empirical-Bernstein radius `0.007302705 alpha`. Adding the Step-43 short-cluster envelope gives `0.999957771 alpha < alpha`. Thus the **implemented finite-grid fast rough-endpoint statistic is certified at 95% pointwise confidence**. The surviving gap is now timing-grid/continuum bias: adding the prior conservative `0.002 alpha` grid allowance raises the total to `1.00195777 alpha`, so this step is not a continuum certificate. No novelty claim.

---

## 1. Bounded long-cluster estimator

Step 42 split successful clusters by duration at

```math
L_0=0.02.
```

For the long-cluster contribution,

```math
Y^{(L_0)}
=m_a\frac{S}{L}1_{\{L\ge L_0\}},
```

we have the exact finite-grid support

```math
\boxed{
0\le Y^{(L_0)}\le B_0=\frac{m_a}{L_0}.
}
```

At the established fast rough endpoint,

```text
X       = 7.16
Lambda  = 0.895
Delta   = 0.15
L0      = 0.02
kappa_f = infinity
alpha   = 1e-6
```

with

```text
u ~= 4.9589834838
a  ~= 4.8089834838
Q(a) ~= 7.5849869161e-7
m_a  ~= 6.7885632899e-7,
```

so

```math
\boxed{
B_0
=3.39428164495\times10^{-5}.
}
```

This support bound is forty times smaller than the raw Step-42 inverse-duration support.

---

## 2. Dedicated independent runs

Use the same finite-grid Gaussian model as Step 33:

```text
timing spacing ~= 0.001
FFT period target = 16
nfft = 16384.
```

For each path:

1. draw the lower-level occupation-Palm conditioned timing field;
2. find the lower-level component containing the selected time;
3. require that component to be successful (`max > u`);
4. compute its linearly interpolated duration `L`;
5. record `m_a/L` only when `L>=.02`, otherwise record zero.

Four independent batches were generated:

```text
seed       paths     mean/alpha       sample SD
------------------------------------------------------
20260812   50000     0.994615198      9.57248e-7
20260813   50000     0.984590252      9.55595e-7
20260814   50000     0.995087976      9.65325e-7
20260815   50000     0.996170838      9.69148e-7
```

Every batch had

```text
selected successful clusters with L<.02 = 0.
```

This observed zero count is consistent with Step 43 but is **not** used as the short-cluster probability bound; Step 43's analytic envelope is retained.

Pooling the four independent batches is equivalent to one i.i.d. sample of size

```math
\boxed{n=200000.}
```

The pooled statistics are

```math
\boxed{
\bar Y/\alpha=0.992616066144,
}
```

```math
\boxed{
s_n=9.61849509624\times10^{-7}.
}
```

---

## 3. Genuine finite-sample empirical-Bernstein bound

For independent samples in `[0,B_0]`, Step 42 used the Maurer-Pontil empirical-Bernstein inequality

```math
E[Y]
\le
\bar Y
+\sqrt{\frac{2s_n^2\ln(2/\delta_c)}{n}}
+\frac{7B_0\ln(2/\delta_c)}{3(n-1)}
```

with probability at least `1-delta_c`.

Use the pointwise endpoint confidence level

```text
delta_c = .05.
```

For the pooled run,

```text
variance term / alpha = 0.00584190324
range term / alpha    = 0.00146080182
------------------------------------------------
total radius / alpha  = 0.00730270506.
```

Therefore

```math
\boxed{
\frac{E[C_{long}]_{95\%,UCB}}{\alpha}
\le
0.992616066144+0.007302705060
=0.999918771204.
}
```

This is a true finite-sample upper confidence statement for the **implemented finite-grid long-cluster estimator**; it does not assume an asymptotically Gaussian Monte Carlo mean.

---

## 4. Add the analytic short-cluster probability

Step 43 gives, conditional on its conservative numerical covariance/metric constants,

```math
P(C_{short}\ge1)<3.9\times10^{-11}.
```

Since `alpha=1e-6`,

```math
\frac{P(C_{short}\ge1)}{\alpha}<3.9\times10^{-5}.
```

The exact duration decomposition is

```math
P_{FA}
\le E[C_{long}]+P(C_{short}\ge1).
```

Combining the empirical-Bernstein UCB with the Step-43 short-cluster envelope yields

```math
\boxed{
\frac{P_{FA}^{finite-grid,95\%}}{\alpha}
<0.999918771204+0.000039
=0.999957771204<1.
}
```

The remaining normalized margin is only

```math
\boxed{
1-0.999957771204
=4.2228796\times10^{-5}.
}
```

In absolute false-alarm probability this is about

```text
4.22e-11.
```

**RIGOROUS FINITE-GRID STATISTICAL CERTIFICATE:** at the fast rough endpoint and for the implemented timing grid, the duration-truncated occupation-Palm construction plus Step 43 gives a 95% pointwise upper bound below `alpha`.

---

## 5. The continuum timing-grid allowance now dominates

Step 34 retained the conservative numerical grid-bias allowance

```text
0.002 alpha.
```

If it is simply added here,

```math
0.999957771204+0.002
=
\boxed{1.001957771204},
```

which no longer certifies fast feasibility.

Thus the statistical problem has changed qualitatively:

```text
before Steps 42-43:
    raw importance-weight statistics were non-certifying;

after Step 44:
    finite-grid Monte Carlo statistics are certifying;

remaining bottleneck:
    continuum timing-grid bias.
```

The prior `0.002 alpha` allowance is roughly 47 times the new finite-grid statistical margin.

**REFINEMENT:** increasing Monte Carlo path count further is not the natural next move until the grid-bias scale is reduced or rigorously characterized.

---

## 6. Qualifications

This step does **not** claim a full theorem-level endpoint certificate because:

- the Step-43 short-cluster bound is analytic conditional on numerical `rho_*` and `K_*`, not formal interval constants;
- the present empirical-Bernstein statement is pointwise at the rough endpoint, not a simultaneous confidence statement across all bandwidth nodes;
- the finite timing grid may misclassify between-sample maxima and shifts component durations;
- the old `0.002 alpha` grid allowance remains numerical, not a rigorous continuum discretization theorem;
- spectral/FFT constants are deterministic floating-point calculations rather than interval arithmetic.

The four independent batches may be pooled without a Bonferroni penalty because the empirical-Bernstein inequality is applied once to the pooled `n=200000` i.i.d. sample. A future simultaneous multi-node certificate will require a separate confidence-budget allocation.

---

## 7. First nontrivial consequence

The main finite-sample statistical objection to the fast rough-endpoint node has now been removed on the implemented grid:

```math
\boxed{
P_{FA}^{finite-grid,95\%}/\alpha<0.9999578.
}
```

This is extremely close to the decision boundary, so it should not be overstated. But it is qualitatively different from the earlier Gaussian-SE heuristic: the bounded long-cluster estimator now carries an explicit finite-sample concentration guarantee, while the discarded short-duration region carries an analytic rare-event bound.

The dominant remaining uncertainty is no longer Monte Carlo sampling. It is **continuum recovery from the finite timing grid**.

---

## 8. Stopping point

The dedicated `L0=.02` truncated occupation-Palm run answers the Step-43 question positively for the implemented finite grid. The next logical issue is whether the continuum cluster probability can differ from that finite-grid calculation by less than the tiny remaining margin—or whether the witness time/grid must be redesigned to create more room.

### Single natural next question

> Can the finite-grid-to-continuum bias of the duration-truncated cluster upper bound be controlled sharply enough to replace the old `0.002 alpha` grid allowance, or should the common witness time `X` be shifted slightly to create a materially larger statistical margin before attempting a continuum proof?
