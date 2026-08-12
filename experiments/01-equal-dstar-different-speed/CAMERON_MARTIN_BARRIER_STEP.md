# Step 40 — Cameron–Martin RKHS Barrier Gives a Direct Rare-Event Threshold Bound

**Date:** 2026-08-12 07:24 EDT  
**Status:** DERIVED / EXACT CAMERON–MARTIN TRANSLATION BOUND / EXACT RKHS BARRIER / NUMERICAL VALIDATION / REJECTED SHORTCUT / PARTIAL CERTIFICATE / OPEN. Step 39 showed that the finite-`u` correction factor `R=N_a/N_tan` is large in amplitude but has a modest numerical threshold slope. This step bypasses that factorization entirely for the threshold-buffer problem. Cameron–Martin change of measure gives a sharp probit bound for translating an arbitrary Gaussian path event by a Cameron–Martin vector. An exactly constant path need not belong to the finite-band RKHS, but it is unnecessary: a positive covariance-kernel representer provides a Cameron–Martin barrier that raises the entire timing path by at least `delta` on the search interval. This yields a direct finite-threshold anti-concentration bound for the exact false-alarm event, with the correct rare-event scale. For the fast high-band trajectory, the covariance floor is numerically about `0.92524`; using a deliberately conservative working floor `0.92`, a `delta=1e-4` threshold displacement changes the rough-endpoint fast upper false-alarm probability from `0.98968 alpha` to at most about `0.99021 alpha`, still safely below `alpha`. The inequality is analytic; the explicit uniform covariance floor is currently numerically certified rather than formal interval arithmetic. No novelty claim.

---

## 1. Cameron–Martin translation of an arbitrary event

Let `mu` be a centered Gaussian measure on a separable path space with Cameron–Martin space `H`. Let `h in H`,

```math
r=||h||_H,
```

and let `mu_h` be the law after translation by `h`.

The Cameron–Martin formula gives

```math
\frac{d\mu_h}{d\mu}(x)
=\exp\left(\widehat h(x)-\frac{r^2}{2}\right),
```

where

```math
\widehat h/r \sim N(0,1)
```

under `mu` when `r>0`.

For a measurable event `A` with

```math
p=\mu(A),
```

the likelihood ratio is monotone in the scalar Gaussian variable `\widehat h`. Therefore, among all events with probability `p`, its shifted probability is minimized by the lower tail of `\widehat h` and maximized by the upper tail. This gives the sharp translation bracket

```math
\boxed{
\Phi\!\left(\Phi^{-1}(p)-r\right)
\le
\mu(A+h)
\le
\Phi\!\left(\Phi^{-1}(p)+r\right).
}
```

The same bracket holds for `A-h` because the Cameron–Martin norm is unchanged by the sign of `h`.

This is a direct consequence of the Cameron–Martin density plus one-dimensional monotone rearrangement; no Gaussian-supremum anti-concentration approximation is involved.

Primary classical source for Gaussian translation/quasi-invariance: R. H. Cameron and W. T. Martin, *Transformations of Wiener integrals under translations*, Annals of Mathematics 45 (1944), 386–396. Gaussian isoperimetric results of Sudakov–Tsirelson and Borell provide a closely related Gaussian-quantile geometry, but the event-translation bracket above is derived directly here from the Cameron–Martin density.

---

## 2. Exact threshold-event barrier lemma

For one timing process `z(t)` on

```math
T=[0,ell],
```

define the exceedance event

```math
A_u=\{x:\sup_{t\in T}x(t)>u\},
```

and

```math
p(u)=P(A_u).
```

Suppose there exists `h_delta in H` such that

```math
h_delta(t)>=delta
\qquad\forall t\in T,
```

and let

```math
r_delta=||h_delta||_H.
```

Then pathwise

```math
A_{u-delta}+h_delta \subseteq A_u,
```

because any path exceeding `u-delta` somewhere exceeds `u` after adding `h_delta`.

Likewise,

```math
A_u+h_delta \subseteq A_{u+delta}.
```

Apply the lower side of the Cameron–Martin translation bracket to these two inclusions. Writing

```math
z_u=\Phi^{-1}(p(u)),
```

gives

```math
\boxed{
p(u-delta)
\le
\Phi(z_u+r_delta),
}
```

and

```math
\boxed{
p(u+delta)
\ge
\Phi(z_u-r_delta).
}
```

Therefore the exact finite-threshold strip obeys

```math
\boxed{
p(u-delta)-p(u+delta)
\le
\Phi(z_u+r_delta)-\Phi(z_u-r_delta).
}
```

For a rare event, this is automatically rare-event scaled because the derivative of `Phi` at the corresponding negative probit is itself of order `p(u) u`.

---

## 3. Covariance-kernel representer gives the needed positive barrier

Let the timing process have unit variance and covariance kernel

```math
K_q(s,t)=R_q(s-t),
\qquad K_q(t,t)=1.
```

Its RKHS contains every kernel section

```math
k_{q,t0}(t)=K_q(t,t0)=R_q(t-t0),
```

with exact norm

```math
||k_{q,t0}||_{H_q}=sqrt(K_q(t0,t0))=1.
```

Choose the center of the search interval,

```math
t0=ell/2,
```

and define the covariance floor

```math
\boxed{
m_q=\inf_{0\le t\le ell}R_q(t-ell/2).
}
```

Whenever

```math
m_q>0,
```

define

```math
\boxed{
h_{q,delta}(t)
=\frac{delta}{m_q}R_q(t-ell/2).
}
```

Then

```math
h_{q,delta}(t)>=delta
```

for every `t` in the search interval, while

```math
\boxed{
||h_{q,delta}||_{H_q}
=\frac{delta}{m_q}.
}
```

Thus the threshold-event bound becomes

```math
\boxed{
p_q(u-delta)
\le
\Phi\!\left[
\Phi^{-1}(p_q(u))+\frac{delta}{m_q}
\right],
}
```

```math
\boxed{
p_q(u+delta)
\ge
\Phi\!\left[
\Phi^{-1}(p_q(u))-\frac{delta}{m_q}
\right].
}
```

This construction needs only a **positive RKHS barrier**, not an exactly constant Cameron–Martin path.

---

## 4. Why this avoids a real finite-band obstruction

A tempting route is to use the exact constant shift

```math
h(t)=delta.
```

At the rough hard-window endpoint this constant path can be generated on a finite observation interval by a finite-energy shift of the underlying white noise, so it belongs to the restricted Cameron–Martin space.

For every finite Gaussian information bandwidth, however, the spectral amplitude has the Gaussian factor

```math
exp(-omega^2 q^4/2),
\qquad q>0.
```

The corresponding RKHS functions extend analytically. If such a function were exactly constant on a nonempty interval, analytic continuation would force it to be constant globally; but global stationary-kernel RKHS functions generated by the integrable spectral density vanish at infinity, so a nonzero constant is excluded.

**REJECTED SHORTCUT:** an exact constant Cameron–Martin shift is not available uniformly across the finite-band family.

The covariance representer barrier avoids this obstruction completely because it is an RKHS element by definition and only needs to stay **above** `delta`, not equal `delta`.

---

## 5. Positivity of the covariance floor

At the rough endpoint, the timing covariance is the normalized autocorrelation of the positive hard-window template

```math
h_x(v)=v e^{-v}1_{[0,x]}(v),
```

so

```math
R_0(t)>=0
```

and is strictly positive for `|t|<x`.

Finite Gaussian information weighting multiplies the spectral mass by

```math
exp(-omega^2 q^4),
```

which corresponds in time to convolving the rough covariance numerator with a positive Gaussian kernel. Hence the finite-band covariance is also strictly positive on the compact search interval.

Therefore, for every fixed `q` in the high-band family,

```math
m_q>0.
```

Continuity in `(q,t)` over the compact set

```math
0<=q<=1/sqrt(170),
\qquad |t|<=ell/2,
```

implies the existence of some uniform

```math
m_*>0.
```

The remaining quantitative task is to certify a useful numerical lower bound on `m_*`.

---

## 6. High-band covariance-floor diagnostic

For the established fast witness

```text
x   = 7.16
ell = 0.895,
```

the rough covariance has the exact finite-window form

```math
R_0(y)
=\frac{
 e^{-|y|}\int_0^{x-|y|}v(v+|y|)e^{-2v}dv
}{
 \int_0^x v^2e^{-2v}dv
}.
```

At the midpoint-to-edge separation

```text
ell/2 = 0.4475,
```

this gives

```text
R_0(ell/2) ~= 0.92523805.
```

Direct deterministic spectral quadrature of the finite-band covariances gives

```text
kappa_f        R_q(ell/2)
-------------------------
170             0.92525794
200             0.92525250
300             0.92524457
500             0.92524045
1000            0.92523868
infinity        0.92523805
```

and a dense timing scan finds the minimum at the interval edge to the displayed precision.

**NUMERICAL VALIDATION:** the covariance floor is essentially constant through the high-band tail and is about

```math
m_q\simeq0.92524.
```

For subsequent conservative arithmetic, use the deliberately lower working value

```math
\boxed{m_*=0.92.}
```

This `0.92` is not yet formal interval arithmetic, but it has much larger slack than the observed finite-band variation.

The helper is stored in

```text
numerics/cameron_martin_barrier.py
```

and evaluates the covariance floor and the resulting probit threshold bounds.

---

## 7. Direct false-alarm consequence at the rough endpoint

Step 33 gives the rough-endpoint fast upper false-alarm estimate

```math
p_f(u)\le0.98968\,alpha,
\qquad alpha=10^{-6}.
```

Take

```math
delta=10^{-4}
```

and the conservative barrier floor

```math
m_*=0.92.
```

Then

```math
r=delta/m_*
=1.0869565\times10^{-4}.
```

Using the upper endpoint probability in the monotone probit bound gives

```math
p_f(u-delta)
\le
\Phi\!\left[
\Phi^{-1}(0.98968\times10^{-6})+r
\right].
```

Numerically,

```math
\boxed{
p_f(u-delta)
\lesssim0.990213\,alpha
<alpha.
}
```

Thus even a threshold decrease as large as `1e-4` cannot consume the rough-endpoint fast feasibility margin under the conservative covariance barrier.

At fixed `p=0.98968 alpha`, the corresponding symmetric strip bound using the observed `m=0.925238` is approximately

```math
\Phi(z+delta/m)-\Phi(z-delta/m)
\approx1.06\times10^{-9}.
```

This lands on the same rare-event scale inferred through Steps 36–39, but it is obtained directly from the exact false-alarm event rather than from tangent/Pickands or cluster-remainder modeling.

---

## 8. First nontrivial consequence

The finite-`u` threshold-buffer problem no longer requires control of the factor

```math
R=N_a/N_tan.
```

A positive covariance RKHS barrier plus Cameron–Martin translation gives a direct exact event-level bound:

```math
\boxed{
p_q(u-delta)-p_q(u+delta)
\le
\Phi\!\left(z+\frac{delta}{m_q}\right)
-
\Phi\!\left(z-\frac{delta}{m_q}\right).
}
```

For the detector-relevant high-band covariance, `m_q` is close to `0.925`, so the multiplier on `delta` is only about `1.08`.

This removes the conceptual finite-`u` remainder slope as the threshold-continuity bottleneck.

---

## 9. What remains open

- convert the numerical covariance floor `m_*=0.92` into formal interval/analytic arithmetic over the entire `q` interval;
- derive a sharp sup-norm probability bound for the **change of the process itself** between adjacent `q` values, i.e. the Step-35 coupling tail `eta`;
- combine that `q`-coupling tail with the present exact threshold-buffer barrier to obtain a theorem-level continuous-parameter closure;
- formal confidence/interval treatment of the Step-33 endpoint probability anchor;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 10. Stopping point

The exact finite-threshold strip can be controlled directly by Cameron–Martin geometry using a covariance-kernel RKHS barrier. An exactly constant shift is unnecessary and, at finite bandwidth, generally unavailable. The remaining theorem gap is now primarily the **sup-norm coupling tail between neighboring bandwidth processes**, not finite-`u` threshold anti-concentration.

### Single natural next question

> Can the common-white-noise difference process `d_{q,r}(t)=z_q(t)-z_r(t)` be given a sharp Borell–TIS / metric-entropy sup-norm tail bound at `|q-r|<=0.005`, small enough that its failure probability `eta` fits inside the remaining `~1e-8` fast false-alarm margin?