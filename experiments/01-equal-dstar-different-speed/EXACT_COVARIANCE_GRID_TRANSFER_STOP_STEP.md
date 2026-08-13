# Step 49 — Exact finite-window covariance transfer and hard stop

**Date:** 2026-08-12 19:53 EDT  
**Status:** DERIVED / EXACT-COVARIANCE SPECTRAL REPRESENTATION / PAIRED EXACT-COVARIANCE TRANSFER INTERVAL / HARD-STOP TRIGGERED / CONSOLIDATION. Step 48 allowed exactly one further mathematical target: the higher-order exact finite-window covariance remainder beyond the mixed Brownian-parabola tangent. This step evaluates that remainder directly. The exact finite-window covariance can be represented by a two-state linear filter with a delayed subtraction, so the finite-`u` Brown-Resnick spectral process can be simulated without replacing the covariance by its cusp-plus-quadratic expansion. On two independent `3000`-path runs (`6000` paired paths total), the exact-covariance coarse-to-`32x`-refined generalized-Pickands loss is `8.3682629e-4` with paired SE `6.8953e-6`; approximate normal 95% interval `[8.2331e-4,8.5034e-4]`. The exact pure-`alpha=1` benchmark over the same refinement is `8.3657896e-4`, so the exact-covariance transfer residual is centered at only `+2.47e-7` with SE `6.90e-6`. The higher-order covariance remainder therefore does not provide an order-`1e-4` escape from the rough-grid effect. This settles the practical `X=7.16` witness direction at the covariance-spectral level. The remaining gap would be a publication-grade finite-`u` transfer from this spectral intensity calculation to the exact finite-window false-alarm event. Under the hard stopping rule, that additional closure is not worth opening another mathematical branch; the closure program stops here and the detector/detection-theory result should now be consolidated. No novelty claim.

---

## 1. Exact finite-window covariance

For the dimensionless finite template

```math
h_x(v)=v e^{-v}1_{[0,x]}(v),
```

the normalized scan covariance is exactly

```math
R_x(y)
=\frac{e^{-y}[I_2(x-y)+yI_1(x-y)]}{D_x},
\qquad 0\le y<x,
```

with

```math
I_1(A)=\frac{1-(1+2A)e^{-2A}}4,
```

```math
I_2(A)=\frac{1-(1+2A+2A^2)e^{-2A}}4,
```

and

```math
D_x=I_2(x).
```

For `y>=x`, `R_x(y)=0`.

At the working point

```text
x = X = 7.16
u = 4.9589834838
```

Step 46/48 coefficients are

```text
a_X = 6.1914157127e-5
b_X = 1.0001238283.
```

The exact finite-`u` tangent-coordinate variogram is therefore

```math
\boxed{
g_u^{exact}(t)
=u^2\left[1-R_x\left(\frac{\sqrt2|t|}{u\sqrt{b_X}}\right)\right].
}
```

The mixed tangent retained only

```math
g_{mix}(t)=t^2+\sqrt2\chi|t|,
\qquad \chi=\frac{a_Xu}{\sqrt{b_X}}.
```

The exact covariance is not globally equal to this quadratic/cusp truncation. For example, on the tangent scale the ratio `g_exact/g_mix` is about `.83` at `|t|=1` and about `.49` at `|t|=4`. Thus a global uniform Taylor bracket would be too loose to certify the discretization ratio.

However, over one physical `dt=.001` cell, the exact and mixed variograms are extremely close:

```text
g_exact(cell endpoint) ~= 1.38116497e-5
g_mix(cell endpoint)   ~= 1.38198442e-5
difference             ~= 8.19e-9.
```

This motivates evaluating the exact-covariance discretization ratio directly rather than trying to force a global Taylor comparison.

---

## 2. Exact two-state representation of the truncated template

Let white noise be `xi(t)`. Define the stationary filter states

```math
U=(e^{-t}1_{t\ge0})*\xi,
```

```math
V=(t e^{-t}1_{t\ge0})*\xi.
```

They obey the linear SDE

```math
dU=-U\,dt+dW,
```

```math
dV=(U-V)\,dt.
```

Their stationary covariance is

```math
P=
\begin{pmatrix}
1/2 & 1/4\\
1/4 & 1/4
\end{pmatrix}.
```

Because

```math
t e^{-t}1_{t\ge x}
=e^{-x}[(t-x)+x]e^{-(t-x)}1_{t\ge x},
```

the exactly truncated-filter scan process can be written

```math
\boxed{
Z_{raw}(t)
=V(t)-e^{-x}\left[V(t-x)+xU(t-x)\right].
}
```

Normalize by

```math
\sqrt{D_x}
```

to obtain unit variance. This reproduces the exact covariance `R_x`.

The state transition over any time step `h` is exact:

```math
S(t+h)=e^{Ah}S(t)+\epsilon_h,
```

with

```math
A=\begin{pmatrix}-1&0\\1&-1\end{pmatrix},
\qquad
Cov(\epsilon_h)=P-e^{Ah}Pe^{A^Th}.
```

Therefore no small-step Euler approximation is used in the exact-covariance simulation.

---

## 3. Exact finite-u Brown-Resnick spectral process

Exponential Gaussian tilting at the origin gives the exact finite-`u` spectral process associated with the covariance:

```math
\boxed{
W_u(t)
=u[Z(y(t))-Z(0)]-g_u^{exact}(t),
}
```

where

```math
y(t)=\frac{\sqrt2 t}{u\sqrt{b_X}}.
```

Its increment variance is exactly `2 g_u^{exact}` and its mean is exactly `-g_u^{exact}`. Thus this step evaluates the higher-order covariance remainder beyond the mixed tangent at finite `u`, rather than inserting another asymptotic covariance model.

**QUALIFICATION:** the resulting generalized-Pickands intensity remains a spectral/extremal object. This step does not claim that it is itself an exact finite-`u` false-alarm probability for the original finite search interval.

---

## 4. Paired coarse/refined exact-covariance calculation

Use the Step-44 physical timing step

```text
dt_coarse = .001
```

and a nested refinement

```text
dt_fine = .001/32 = 3.125e-5.
```

In tangent coordinates this is `Delta` versus `Delta/32`.

For each path, the same exact Gaussian realization is evaluated on both lattices. The generalized discrete Dieker-Yakir ratios are therefore strongly paired.

Two independent seeds of `3000` paths each give:

```text
seed        exact relative loss        paired SE
-------------------------------------------------
20260820      8.23907e-4               9.49009e-6
20260821      8.49716e-4               1.00011e-5
```

Pooling the two independent runs (`6000` paths total):

```math
\boxed{
H_{exact}^{\Delta}=0.5528146649,
}
```

```math
\boxed{
H_{exact}^{\Delta/32}=0.5532776622,
}
```

and therefore

```math
\boxed{
1-\frac{H_{exact}^{\Delta}}{H_{exact}^{\Delta/32}}
=8.368262916\times10^{-4}.
}
```

The paired delta-method standard error is

```math
\boxed{6.8953\times10^{-6}.}
```

Approximate normal 95% interval:

```math
\boxed{
[8.23312,\ 8.50341]\times10^{-4}.
}
```

**PAIRED EXACT-COVARIANCE TRANSFER INTERVAL:** this is a controlled Monte Carlo interval, not a distribution-free finite-sample theorem.

---

## 5. Compare with the exact pure-alpha=1 benchmark

For the same coarse-to-`32x` canonical refinement, Step 47 gives

```math
\boxed{
1-\frac{H_1^{\delta}}{H_1^{\delta/32}}
=8.36578957\times10^{-4}.
}
```

Hence the exact-covariance minus pure-rough loss residual is

```math
\boxed{
2.47335\times10^{-7},
}
```

with the same Monte Carlo SE

```math
6.8953\times10^{-6}.
```

An approximate 95% residual interval is therefore roughly

```math
[-1.33,\ 1.38]\times10^{-5}.
```

Thus the exact higher-order covariance changes the resolved discretization loss by at most the `O(1e-5)` scale at the available precision. It does not produce an `O(1e-4)` cancellation.

For comparison, Step 48's mixed tangent at `Delta/32` differed from the pure benchmark by only a few `1e-6`, with paired uncertainty of the same order. The exact covariance therefore preserves the same conclusion: the finite-u discretization ratio is extremely close to the pure rough benchmark even though the absolute continuous generalized-Pickands constant itself can differ substantially.

---

## 6. Truncation-window sensitivity

Independent `1000`-path pilots give

```text
DY half-window T=3: loss = 8.4862e-4 +/- 1.82e-5
DY half-window T=5: loss = 8.5836e-4 +/- 1.78e-5
```

Both overlap the pooled `T=4` interval. This is a sensitivity check only, not a formal truncation-error proof.

---

## 7. Consequence for the X=7.16 witness

The Step-44 finite-grid statistical margin was only

```text
4.22e-5 alpha.
```

The exact-covariance coarse-to-`32x` relative loss has a lower approximate 95% endpoint

```text
8.23e-4,
```

which is about `19.5x` the normalized Step-44 margin.

This comparison is made at the rare-event intensity level; it is not presented as a theorem-level conversion to the exact finite-window false-alarm probability. But it decisively removes the proposed escape route in which higher-order finite-window covariance terms cancel the rough-grid correction.

**NEGATIVE RESULT / WITNESS DISPOSITION:** the `X=7.16`, `dt~.001` finite-grid knife-edge should not be promoted as a continuum certificate. The exact covariance retains essentially the same discretization loss as the pure rough benchmark.

---

## 8. Hard-stop decision

The external Step-47 assessment required that further work either close the finite-u transfer, materially bound it, or stop.

Step 48 showed the mixed Brownian-parabola transfer is only `O(1e-5)` relative to an `O(1e-3)` grid effect. Step 49 now shows the higher-order **exact finite-window covariance** transfer is likewise only `O(1e-5)` at the available paired precision.

The remaining unclosed layer would be a publication-grade theorem connecting this exact-covariance spectral-intensity discretization ratio to the exact finite-search false-alarm event at `u~4.96`, plus formal interval arithmetic and simultaneous confidence allocation.

That work is possible in principle but is no longer proportionate to the detector-physics question. It would deepen the specialized Gaussian-extremes companion problem without materially changing the detector conclusion.

Therefore:

```math
\boxed{\text{HARD-STOP TRIGGERED: stop the mathematical closure branch here.}}
```

The next research action should be consolidation and prior-art/novelty audit of the detector/detection-theory result, not Step 50 of the same proof chain.

---

## 9. Final scope statement for this branch

What is supported:

- scalar `D*` does not order arbitrary temporal tasks;
- even magnitude `D*(f)` is insufficient for finite-window tasks because phase/time placement matters;
- under the defined unknown-arrival global-false-alarm scanning protocol, temporal compression changes both evidence accumulation and timing-search complexity and can reverse the fast/slow ranking in the constructed equal-eventual-SNR family;
- the high-band rough-endpoint numerical/covariance analysis is internally consistent with a real missed-maximum grid correction, not a numerical artifact;
- the exact finite-window covariance does not materially alter the finite-grid correction predicted by the pure rough benchmark at the working point.

What is **not** supported:

- a universal statement that faster detectors are worse;
- universal optimality of the scanning protocol;
- a theorem-level continuum false-alarm certificate for the `X=7.16` knife-edge;
- novelty.

---

## 10. Stopping point

No Step 50 should continue this mathematical closure chain unless a later external review identifies a genuinely decision-relevant gap. The active project should now return to the detector-level result: consolidate the core theorem/task statement, separate the mathematical companion material, and perform a serious prior-art audit before any novelty claim.
