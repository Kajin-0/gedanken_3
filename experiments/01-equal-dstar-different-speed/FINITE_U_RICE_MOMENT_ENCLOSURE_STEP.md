# Step 32 — Finite-`u` Rice Moment Enclosure

**Date:** 2026-08-11 21:39 EDT  
**Status:** DERIVED / NUMERICAL VALIDATION / PARTIAL CERTIFICATE / NEGATIVE RESULT / OPEN. Step 31 numerically closed the high-band re-entrant pocket for the original `r=2`, `Lambda=0.895` task, but still transported the finite-threshold correction with an empirical `delta(kappa)` fit. This step removes that fit over part of the high-band interval by deriving a non-asymptotic upper/lower false-alarm enclosure from the first two moments of the upcrossing count. The result directly certifies fast preference through at least `kappa_f=170` for the stated calibration. The enclosure then loses resolving power as the slow channel develops strong micro-upcrossing clustering; this is a limitation of the second-moment bound, not evidence for a preference reversal. No novelty claim.

---

## 1. Exact event decomposition

For a smooth finite-band stationary unit-variance Gaussian timing scan `z(t)` over `[0,ell]`, let

```math
N_u^+
```

be the number of upcrossings of level `u`. Define

```math
\boxed{
X_u
=1_{\{z(0)\le u\}}N_u^+.
}
```

For continuous sample paths,

```math
\boxed{
P_{FA}(u)
=Q(u)+P(X_u\ge1).
}
```

The first term is the event that the scan starts above threshold. If it starts below, exceeding `u` somewhere in the interval requires at least one upcrossing.

This identity is exact at finite `u`; no high-threshold/Pickands approximation has been used.

---

## 2. Moment enclosure

Because `X_u` is a nonnegative integer-valued random variable,

```math
P(X_u\ge1)\le E[X_u].
```

Cauchy–Schwarz / Paley–Zygmund at zero gives

```math
P(X_u\ge1)
\ge
\frac{E[X_u]^2}{E[X_u^2]}.
```

Since

```math
X_u^2\le (N_u^+)^2,
```

we obtain the computable lower bound

```math
P(X_u\ge1)
\ge
\frac{m_1^2}{E[(N_u^+)^2]},
```

where

```math
m_1
=E[N_u^+1_{\{z(0)\le u\}}].
```

Write

```math
\lambda=E[N_u^+],
```

```math
\lambda_2=E[N_u^+(N_u^+-1)].
```

Then

```math
E[(N_u^+)^2]=\lambda+\lambda_2.
```

Therefore

```math
\boxed{
Q(u)+\frac{m_1^2}{\lambda+\lambda_2}
\le P_{FA}(u)
\le Q(u)+m_1.
}
```

This is the finite-`u` second-moment Rice enclosure used below.

The framework is standard Rice-factorial-moment Gaussian crossing theory; relevant primary references include Kratz & León, *Annals of Probability* 34 (2006), arXiv:math/0609682, and Azaïs & Wschebor, *Stochastic Processes and their Applications* 118 (2008), arXiv:math/0607041.

---

## 3. First moment and endpoint-overlap correction

For a stationary differentiable unit-variance Gaussian process with

```math
\sigma^2=-R''(0),
```

the ordinary Rice mean is

```math
\boxed{
\lambda
=\ell\frac{\sigma}{2\pi}e^{-u^2/2}.
}
```

The start-below moment is

```math
m_1
=\lambda-J_0,
```

where

```math
J_0
=E[N_u^+1_{\{z(0)>u\}}].
```

`J_0` is a one-dimensional first-order Rice integral. At lag `t`, condition on `z(t)=u`; the pair `(z(0),z'(t))` is Gaussian with covariance determined completely by `R(t)` and `R'(t)`. Thus `J_0` is evaluated deterministically from the known covariance, without Palm Monte Carlo.

---

## 4. Second factorial moment

The second Rice formula gives

```math
\boxed{
\lambda_2
=2\int_0^\ell(\ell-h)\rho_2(h)\,dh,
}
```

with

```math
\rho_2(h)
=p_{z(0),z(h)}(u,u)
E[z'(0)_+z'(h)_+\mid z(0)=z(h)=u].
```

For

```math
r=R(h),\qquad p=R'(h),\qquad q=R''(h),
```

the value density is

```math
p_{z(0),z(h)}(u,u)
=
\frac{1}{2\pi\sqrt{1-r^2}}
\exp\!\left[-\frac{u^2}{1+r}\right].
```

The conditional derivative means are

```math
m_-= -\frac{pu}{1+r},
\qquad
m_+= \frac{pu}{1+r},
```

and their common conditional variance and covariance are

```math
v
=\sigma^2-\frac{p^2}{1-r^2},
```

```math
c
=-q-\frac{rp^2}{1-r^2}.
```

The remaining positive-part bivariate Gaussian moment is evaluated by deterministic Gauss–Hermite quadrature.

Thus every quantity entering the enclosure is determined by the finite-band covariance.

---

## 5. Covariance used for the detector family

For the finite-window controlled template,

```math
H_x(\omega)
=
\frac{1-e^{-(1+i\omega)x}[1+(1+i\omega)x]}
{(1+i\omega)^2},
```

with Gaussian information weighting,

```math
S_{x,\kappa}(\omega)
\propto
|H_x(\omega)|^2e^{-(\omega/\kappa)^2}.
```

Normalize the inverse Fourier transform to `R(0)=1`. Then `R`, `R'`, and `R''` are obtained from the same spectrum by multiplying by `1`, `i omega`, and `-omega^2`, respectively.

The numerical helper

```text
numerics/finite_u_rice_moment_enclosure.py
```

performs these FFT covariance calculations and the one-/two-point Rice integrals. Timing-grid refinement is tied to the physical information bandwidth; the reported values were checked under multiple refinements.

---

## 6. Direct finite-`u` preference certificate for `Lambda=0.895`

Use the established task

```text
r        = 2
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90
Lambda   = 0.895.
```

At common physical decision time

```math
X=7.04,
```

the fast and slow search lengths are

```math
\ell_f=0.895,
\qquad
\ell_s=0.4475,
```

and the slow information bandwidth is `kappa_s=2 kappa_f`.

Representative second-moment enclosures are

```text
kappa_f   fast P_FA upper / alpha   slow P_FA lower / alpha
------------------------------------------------------------
100              ~0.99737                    ~1.04649
130              ~0.99861                    ~1.02562
160              ~0.99961                    ~1.00950
170              ~0.99990                    ~1.00491
175              ~1.00004                    ~1.00275
200              >1 at the useful X           bound overlap
```

Therefore, for `kappa_f=100,130,160,170`, at the same physical time `X=7.04`,

```math
P_{FA,f}^{upper}<\alpha
```

while

```math
P_{FA,s}^{lower}>\alpha.
```

Hence the fast detector is already guaranteed feasible while the slow detector is still guaranteed infeasible.

```math
\boxed{
T_{D,f}<T_{D,s}
}
```

for those tested bandwidths, using a finite-`u` moment enclosure rather than the empirical Step-31 offset.

**PARTIAL CERTIFICATE / NUMERICAL QUADRATURE:** the inequalities themselves are exact. The numerical values use deterministic FFT/Rice quadrature rather than formal interval arithmetic. Grid refinement changed the displayed ratios far less than the fast/slow separation through `kappa_f=170`.

---

## 7. Explicit convergence check at `kappa_f=160`

At

```text
kappa_f=160,
X=7.04,
```

varying the timing resolution scale gives approximately

```text
resolution scale   fast upper/alpha   slow lower/alpha
------------------------------------------------------
0.040                  0.9996055          1.0095019
0.030                  0.9996056          1.0095064
0.020                  0.9996055          1.0095019
0.015                  0.9996054          1.0094996
```

The second factorial moments are equally stable under this refinement.

Thus the finite-`u` separation at `kappa_f=160` is not a visible timing-grid artifact.

---

## 8. Why the second-moment certificate eventually fails

The failure near `kappa_f~175–200` is diagnostic rather than contradictory.

For the slow detector, increasing physical bandwidth produces many microscopic upcrossings inside one rough physical excursion. Consequently

```math
\lambda_2=E[N(N-1)]
```

grows rapidly.

For example, near `X~7`, the slow-channel second factorial moment increases from order

```text
~0.3e-6 at kappa_f=100
```

to

```text
~0.8e-6 at kappa_f=200
```

and continues growing thereafter.

The lower bound

```math
m_1^2/(\lambda+\lambda_2)
```

then becomes increasingly conservative even though the physical excursion probability itself remains well behaved.

This reproduces, in a non-asymptotic moment language, the same clustering obstruction that invalidated high-band Rice counting in Steps 17 and 21.

**NEGATIVE RESULT:** ordinary second crossing moments do not yield a useful global high-band interval enclosure. Their loss of sharpness is caused by cluster multiplicity, not by evidence for a new detector-preference reversal.

---

## 9. First nontrivial consequence

The empirical Step-31 finite-`u` bridge is no longer required over the whole mapped high-band region.

For the original `Lambda=0.895` task, a direct finite-threshold Rice-moment inequality independently certifies fast preference through at least

```math
\boxed{\kappa_f=170}
```

in the tested sequence.

The remaining unresolved region is now specifically the **clustered high-band regime**, where raw upcrossing second moments become inefficient.

---

## 10. What remains open

- a cluster-renormalized finite-`u` enclosure that stays sharp as `kappa_f` grows;
- an occupation-time or excursion-cluster moment bound that remains useful through the rough limit;
- a theorem-level interval enclosure for the complete high-band boundary;
- formal interval-arithmetic certification of the deterministic quadrature;
- extension to other `Lambda`, `r`, SNR, and detector models;
- hardware interpretation;
- novelty.

---

## 11. Stopping point

The finite-`u` discrepancy has now been bounded directly over a substantial high-band interval. The unresolved part is no longer a generic finite-threshold correction; it is specifically the conversion from many micro-upcrossings to one physical excursion in the roughening slow channel.

### Single natural next question

> Can we replace raw upcrossing multiplicity by an excursion-cluster or occupation-time variable whose first two moments remain finite and sharp as `kappa_f -> infinity`, thereby extending the finite-`u` enclosure continuously into the rough endpoint?
