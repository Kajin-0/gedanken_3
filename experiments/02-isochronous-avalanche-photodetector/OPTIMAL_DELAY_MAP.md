# Exact optimal delay map

**Date:** 2026-08-13
**Status:** EXACT MAXWELL-TO-TRANSPORT DESIGN RESULT / NOVELTY NOT CLAIMED

Let `X` denote optical propagation coordinate and `Z` the actual physical absorption depth. The optical field determines a joint detected-photon distribution `p(x,z)`. Let `t_c(Z)` be the conditional mean carrier-to-avalanche trigger delay associated with depth `Z`.

Suppose the photonic structure can add a deterministic optical delay `d(X)` that depends only on the optical coordinate. The deterministic part of the event timestamp is

```math
M=d(X)+t_c(Z).
```

Condition on `X` and define

```math
m_c(x)=E[t_c(Z)|X=x].
```

Then the law of total variance gives

```math
\boxed{
Var(M)
=Var_X[d(X)+m_c(X)]
+E_X[Var(t_c(Z)|X)].
}
```

The second term is independent of the chosen delay map. Therefore the variance-minimizing deterministic optical delay is any function satisfying

```math
\boxed{d_opt(x)+m_c(x)=C.}
```

Equivalently,

```math
\boxed{d_opt(x)=C-E[t_c(Z)|X=x].}
```

If optics may only add nonnegative delay, the smallest feasible common timestamp is obtained with

```math
\boxed{C=minimal=max_x E[t_c(Z)|X=x].}
```

The corresponding minimum achievable deterministic timing variance is

```math
\boxed{
min_d Var[d(X)+t_c(Z)]
=E_X[Var(t_c(Z)|X)].
}
```

## Physical meaning

A deterministic optical delay can remove **all between-slice variation** in mean carrier transit time, but it cannot remove the **within-slice spread** arising because photons absorbed at the same optical coordinate still occupy a finite distribution of physical depths.

Thus the correct design target is not a moving optical-mode centroid. It is the conditional mean carrier delay obtained by combining a Maxwell absorption map with carrier transport.

With electrical propagation and mean avalanche-build-up delay included, replace `m_c(x)` by

```math
m_int(x)=E[t_c+t_a|X=x]+t_e(x),
```

and use

```math
\boxed{d_opt(x)=C-m_int(x).}
```

Conditional stochastic avalanche, drift/diffusion, and electronics variance remain in the residual floor.

## Maxwell-to-transport workflow

1. Compute absorbed optical power density versus `(x,z)`.
2. Normalize it to obtain detected-photon `p(x,z)`.
3. Compute carrier mean transit `t_c(z)` and conditional transport variance from TCAD/Monte Carlo.
4. Evaluate `m_c(x)=E[t_c|x]` and `Var(t_c|x)`.
5. Compare the actual optical group-delay map with `C-m_c(x)`.
6. The best possible deterministic improvement is known before avalanche simulation from the variance decomposition above.

No novelty or priority claim is made for the mathematical conditional-expectation identity; its value here is as an exact design criterion for the proposed APD depth-compensation hypothesis.