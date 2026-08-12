# Step 35 — Analytic `q`-Coupling Continuity and the Rare-Event Obstruction

**Date:** 2026-08-11 22:54 EDT  
**Status:** DERIVED / REFINEMENT / REJECTED SHORTCUT / NEGATIVE RESULT / OPEN. Step 34 closed the original high-band tail numerically in the coordinate `q=kappa_f^(-1/2)` but still used an empirical inter-node allowance. This step derives an analytic common-white-noise continuity law for the *Gaussian timing process itself*. The normalized spectral field is genuinely Lipschitz in `q`, including at the nondifferentiable `q=0` rough endpoint. For the fast channel, the pointwise RMS change across a `Delta q=0.005` mesh cell is bounded at roughly `7.5e-5`, and the decision threshold moves by only about `2.8e-5`. However, the excursion-cluster functional is not pathwise Lipschitz, and generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6` to turn those pathwise scales into the `~1e-9` absolute probability control needed by the Step-34 fast margin. The remaining theorem gap is therefore a **tail-sensitive rare-excursion continuity bound**, not continuity of the Gaussian field itself. No novelty claim.

---

## 1. Normalized common-white-noise spectral family

At fixed dimensionless observation time `x`, define the finite-band spectral mass

```math
I_x(q)
=\int_{-\infty}^{\infty}
|H_x(\omega)|^2 e^{-\omega^2 q^4}\,d\omega,
\qquad
q=\kappa^{-1/2},
```

with

```math
H_x(\omega)
=\frac{1-e^{-(1+i\omega)x}[1+(1+i\omega)x]}
{(1+i\omega)^2}.
```

A unit-variance stationary Gaussian timing scan may be generated from one common complex Gaussian spectral measure using normalized amplitude

```math
\boxed{
A_q(\omega)
=\frac{|H_x(\omega)|e^{-\omega^2q^4/2}}
{\sqrt{I_x(q)}}.
}
```

Thus

```math
\int A_q(\omega)^2\,d\omega=1.
```

The phase convention of the spectral factor is irrelevant for the covariance comparison; the same real stationary field can be constructed from this nonnegative spectral amplitude.

---

## 2. Exact derivative with respect to `q`

Define the normalized spectral moments

```math
M_{2n}(q)
=\frac{\int \omega^{2n}|H_x(\omega)|^2e^{-\omega^2q^4}\,d\omega}
{I_x(q)}.
```

Since

```math
I_x'(q)=-4q^3 I_x(q)M_2(q),
```

differentiating the normalized amplitude gives

```math
\boxed{
\partial_q A_q(\omega)
=-2q^3\bigl(\omega^2-M_2(q)\bigr)A_q(\omega).
}
```

Therefore

```math
\boxed{
\|\partial_q A_q\|_2^2
=4q^6\operatorname{Var}_q(\omega^2)
=4q^6\bigl[M_4(q)-M_2(q)^2\bigr].
}
```

This is exact for every finite `q>0`.

---

## 3. The rough endpoint is regular in `q`

For finite `x`, the hard endpoint of the time-domain template gives

```math
H_x(\omega)
\sim
\frac{i x e^{-x}e^{-i\omega x}}{\omega},
\qquad |\omega|\to\infty.
```

Hence

```math
|H_x(\omega)|^2
\sim\frac{c_x^2}{\omega^2},
\qquad
c_x=x e^{-x}.
```

Although `M_4(q)` diverges like `q^-6` as `q->0`, the prefactor `q^6` in the derivative norm cancels that divergence. Using

```math
\int_{-\infty}^{\infty}
\omega^2e^{-q^4\omega^2}\,d\omega
=\frac{\sqrt\pi}{2q^6},
```

we obtain

```math
\boxed{
\lim_{q\to0^+}\|\partial_q A_q\|_2^2
=\frac{2\sqrt\pi\,c_x^2}{I_x(0)}.
}
```

Thus the rough endpoint is not singular in the `L2` spectral geometry when parameterized by `q=kappa^-1/2`.

**FIRST REFINEMENT:** Step 34's use of `q` was not merely a convenient plotting coordinate. It is the coordinate in which the common-white-noise spectral family has a finite first derivative at the rough endpoint.

---

## 4. Pointwise Gaussian coupling modulus

Let `z_q(t)` and `z_r(t)` be generated from the same spectral Gaussian measure. Then, for every fixed `t`,

```math
\operatorname{Var}[z_q(t)-z_r(t)]
=\|A_q-A_r\|_2^2.
```

By the fundamental theorem of calculus in `L2`,

```math
\boxed{
\operatorname{SD}[z_q(t)-z_r(t)]
\le
\int_{\min(q,r)}^{\max(q,r)}
\|\partial_s A_s\|_2\,ds.
}
```

Therefore, if

```math
L_x^*=\sup_{0\le s\le q_{max}}\|\partial_sA_s\|_2,
```

then

```math
\boxed{
\operatorname{SD}[z_q(t)-z_r(t)]
\le L_x^*|q-r|.
}
```

There is also an exact pairwise covariance formula. Define `q_m` by

```math
q_m^4=(q^4+r^4)/2.
```

Then

```math
\boxed{
\operatorname{Var}[z_q(t)-z_r(t)]
=2\left[
1-
\frac{I_x(q_m)}{\sqrt{I_x(q)I_x(r)}}
\right].
}
```

No simulation enters either relation.

---

## 5. Fast-channel numerical scale

For the Step-34 common witness time

```text
x_f = X = 7.16,
q_f in [0,0.0767],
```

we have

```math
I_x(0)=\frac{\pi}{2}\eta(x),
\qquad
\eta(x)=1-e^{-2x}(1+2x+2x^2).
```

The endpoint derivative norm is

```text
||dA/dq||(q=0) ~= 0.00836.
```

Direct deterministic spectral quadrature over the Step-34 interval gives representative values

```text
q        ||dA/dq||_2
--------------------
0        0.00836
0.020    0.00840
0.040    0.00898
0.060    0.01130
0.0767   0.01493
```

so a conservative interval value is

```math
L_f^*\approx0.015.
```

For the standard Step-34 mesh cell

```math
\Delta q=0.005,
```

this gives

```math
\boxed{
\operatorname{SD}[z_q(t)-z_{q+\Delta q}(t)]
\lesssim7.5\times10^{-5}.
}
```

The exact pair formula gives the same order. For example, near the finite end of the tail,

```text
q=0.070 -> 0.075:
pointwise RMS ~= 6.9e-5.
```

At the endpoint,

```text
q=0 -> 0.005:
pointwise RMS ~= 5.4e-5.
```

**NUMERICAL VALIDATION:** these are deterministic spectral-integral evaluations, not Monte Carlo estimates. They are not formal interval arithmetic.

---

## 6. Decision-threshold motion is also Lipschitz

At fixed `x`, the accessible matched-filter SNR is

```math
\rho(q)
=\rho_{full}
\sqrt{\frac{I_x(q)}{\pi/2}}.
```

Therefore

```math
\boxed{
\rho'(q)
=-2q^3M_2(q)\rho(q).
}
```

Since

```math
u(q)=\rho(q)-\Phi^{-1}(\beta),
```

the same derivative applies to the available decision threshold.

For the fast Step-34 interval, deterministic quadrature gives approximately

```text
max |u_f'(q)| ~= 5.6e-3.
```

Thus across `Delta q=0.005`,

```math
\boxed{
|u_f(q+\Delta q)-u_f(q)|
\lesssim2.8\times10^{-5}.
}
```

So both the process and the decision threshold vary very smoothly in `q`.

---

## 7. Exact event sandwich under a sup-norm coupling

Let

```math
M_q=\sup_{0\le t\le\ell}z_q(t),
\qquad
p(q)=P[M_q>u_q].
```

For any two bandwidth coordinates `q,r`, define

```math
d_u=|u_q-u_r|.
```

On the coupling event

```math
\|z_q-z_r\|_\infty\le\epsilon,
```

we have pathwise

```math
M_q-\epsilon\le M_r\le M_q+\epsilon.
```

Therefore, with

```math
\delta=\epsilon+d_u
```

and

```math
\eta=P(\|z_q-z_r\|_\infty>\epsilon),
```

we obtain the exact probability sandwich

```math
\boxed{
p_q(u_q+\delta)-\eta
\le p(r)
\le p_q(u_q-\delta)+\eta,
}
```

where `p_q(v)=P[M_q>v]` denotes the same process evaluated at threshold `v`.

This shows that a theorem-level inter-node enclosure does **not** require continuity of the cluster-count functional itself. It is enough to control:

1. the sup-norm coupling tail `eta`;
2. the finite-threshold probability in a narrow buffer around `u_q`.

The Step-33 cluster moment machinery can, in principle, bound the buffered probabilities `p_q(u_q +/- delta)` directly.

---

## 8. REJECTED SHORTCUT — the cluster moment is not pathwise Lipschitz

A small sup-norm perturbation can change `C_Delta` discontinuously if either:

- a lower-level component minimum lies arbitrarily close to `a=u-Delta`, causing two components to merge or one to split;
- a component maximum lies arbitrarily close to `u`, changing success/failure;
- a selected lower component becomes very short, amplifying the occupation-Palm weight `1/L`.

Therefore no deterministic inequality of the form

```math
|C_Delta(z)-C_Delta(zt)|
<= K ||z-zt||_infinity
```

can hold uniformly over continuous paths.

**REJECTED SHORTCUT:** process `L2` Lipschitz continuity in `q` does not directly imply Lipschitz continuity of `E[C_Delta]` or `E[C_Delta^2]`.

A probabilistic near-critical-event bound is unavoidable.

---

## 9. NEGATIVE RESULT — generic Gaussian anti-concentration is far too coarse

A standard anti-concentration theorem for a separable centered unit-variance Gaussian process `X_t` gives

```math
\sup_y P(|\sup_t X_t-y|\le\epsilon)
\le4\epsilon\bigl(E[\sup_t X_t]+1\bigr).
```

Primary source: Chernozhukov, Chetverikov & Kato, *Anti-concentration and honest, adaptive confidence bands*, Theorem 2.1, arXiv:1303.7152.

This theorem is rigorous and applies to the present unit-variance Gaussian timing scan, but it is intentionally global rather than high-tail specific.

At our false-alarm target

```math
\alpha=10^{-6},
```

even an extremely small threshold buffer of only

```math
\epsilon=10^{-4}
```

gives the trivial lower floor

```math
4\epsilon=4\times10^{-4}=400\alpha
```

before the factor `E[sup X]+1>1` is included.

By contrast, the Step-34 empirical inter-node allowance was

```math
0.0006 alpha = 6e-10
```

in absolute probability.

Thus generic supremum anti-concentration misses the required probability scale by many orders of magnitude.

**NEGATIVE RESULT:** common-white-noise continuity plus a dimension-free Gaussian supremum anti-concentration theorem cannot, by itself, upgrade Step 34 to a useful theorem-level interval enclosure at `alpha=1e-6`.

---

## 10. First nontrivial consequence

The high-band continuity problem has now split cleanly into two layers:

```text
Gaussian field versus q:
    analytically regular and L2-Lipschitz, including q=0;

rare excursion probability versus q:
    still requires a tail-sensitive local bound.
```

For the fast detector, adjacent Step-34 `q` nodes differ by only `O(1e-4)` in process amplitude and `O(1e-5)` in threshold, yet the final probability certificate needs control at roughly the `1e-9` absolute level.

Therefore the missing theorem is **not** a generic continuity theorem for Gaussian processes. It must exploit the fact that the decision level is near `u~5` and that the relevant event is a rare successful excursion cluster.

---

## 11. What remains open

- a tail-sensitive anti-concentration / buffered-excursion bound whose scale is proportional to the rare-event intensity rather than order-one Gaussian supremum density;
- an analytic bound on the sup-norm coupling tail `eta` sharp enough for the `alpha=1e-6` task;
- a way to combine that bound with the Step-33 cluster moment enclosure at `u +/- delta`;
- formal interval arithmetic for the spectral constants `L_x^*` and threshold derivative bounds;
- theorem-level continuous-parameter closure of the Step-34 tail;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 12. Stopping point

The natural high-band coordinate `q=kappa_f^-1/2` is now analytically justified: the normalized common-noise Gaussian field is Lipschitz in `q` all the way to the rough endpoint. The obstruction to a theorem-level tail closure is specifically the sensitivity of an `alpha=1e-6` rare excursion event, not the detector field itself.

### Single natural next question

> Can the successful-excursion cluster representation be used to derive a **tail-sensitive buffered-threshold continuity bound** near `u~5`, so that the probability of a cluster whose maximum lies in `[u-delta,u+delta]` scales like the rare-event intensity times `delta` rather than the global `O(delta)` Gaussian anti-concentration bound?
