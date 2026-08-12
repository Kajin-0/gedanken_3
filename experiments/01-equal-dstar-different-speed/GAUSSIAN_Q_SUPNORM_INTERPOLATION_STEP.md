# Step 41 — Analytic Sup-Norm Interpolation Between High-Band `q` Nodes

**Date:** 2026-08-12 09:42 EDT  
**Status:** DERIVED / ANALYTIC INTER-NODE ENVELOPE / REFINEMENT / INVALIDATED NUMERICAL VALUE / PARTIAL CERTIFICATE / OPEN. Step 40 converted a deterministic sup-norm perturbation of the timing field into a sharp rare-event probability shift by a Cameron–Martin RKHS barrier. This step bounds the remaining common-white-noise difference process `d_{q,r}(t)=z_q(t)-z_r(t)` between sampled `q=kappa_f^-1/2` nodes. The rough endpoint requires a grid-plus-modulus argument; every strictly positive finite-`q` pair is differentiable and admits a sharp Rice upcrossing bound for its sup norm. Combined with the Step-34 node envelopes and the Step-40 threshold translation, these bounds replace the empirical `0.0006 alpha` inter-node allowance for the original fast high-band tail. The continuous-`q` interpolation is therefore analytically controlled conditional on the existing numerical node/grid envelopes. This is not formal interval arithmetic and does not turn the Step-34 Monte Carlo node estimates into a theorem. No novelty claim.

---

## 1. Common-white-noise difference field

At fixed witness time `X=7.16`, let

```math
A_q(omega)
=|H_X(omega)|e^{-omega^2q^4/2}/sqrt(I_X(q)),
```

with

```math
I_X(q)=int |H_X(omega)|^2e^{-omega^2q^4}domega.
```

Generate every timing field from one common Gaussian spectral measure. Then

```math
\boxed{
d_{q,r}(t)=z_q(t)-z_r(t)
}
```

is a centered stationary Gaussian process with point variance

```math
\boxed{
sigma_{q,r}^2=||A_q-A_r||_2^2.
}
```

Step 35 already proved

```math
partial_q A_q
=-2q^3(omega^2-M_2(q))A_q,
```

and that `||partial_q A_q||_2` remains finite as `q->0`.

The event sandwich is

```math
p(r)
<=p_q(u_q-epsilon-|u_r-u_q|)
+P(||d_{q,r}||_infinity>epsilon).
```

Step 40 controls the first term once `epsilon` is supplied. This step controls the second.

---

## 2. REFINE Step 35 endpoint chord calculation

For finite `X`,

```math
|H_X(omega)|^2
~c_X^2/omega^2,
qquad
c_X=Xe^{-X}.
```

Let

```math
I_0=I_X(0)=pi eta(X)/2.
```

The Gaussian information factor removes high-frequency mass according to

```math
\boxed{
I_X(q)
=I_0-2sqrt(pi)c_X^2q^2+o(q^2).
}
```

For the exact common-noise overlap between `q=0` and `q=r`, the mixed Gaussian exponent has

```math
q_m^4=r^4/2,
```

hence `q_m^2=r^2/sqrt(2)`. Expanding the exact overlap formula gives

```math
\boxed{
sigma_{0,r}^2
=(sqrt(2)-1)L_0^2r^2+o(r^2),
}
```

where

```math
\boxed{
L_0^2
=2sqrt(pi)c_X^2/I_0.
}
```

At `X=7.16`,

```text
c_X      ~= 0.0055637106
I_0      ~= 1.5706845486
L_0      ~= 0.0083583877
sqrt(sqrt(2)-1)L_0 ~= 0.0053794103.
```

Therefore

```text
q=0 -> .005   RMS ~= 2.69e-5  (leading endpoint chord)
q=0 -> .0025  RMS ~= 1.34e-5.
```

**INVALIDATED NUMERICAL VALUE:** Step 35's helper reported an `exact pairwise` endpoint value around `5.4e-5` for `0 -> .005`. That number is inconsistent with Step 35's own Hilbert-space derivative bound and is traced to ill-conditioned direct quadrature/cancellation of nearly equal `I(q)` values at tiny `q`. The exact overlap formula remains valid; that particular tiny-`q` numerical evaluation does not. The Step-35 qualitative conclusion that the field is `L2`-regular in `q` remains valid.

The calculator for this step uses the asymptotic chord law and deliberately larger working envelopes rather than the invalidated value.

---

## 3. Rough endpoint: deterministic net plus Brownian-type modulus

For `r>0`, write

```math
D_r(omega)=A_0(omega)-A_r(omega).
```

For the tiny endpoint cell used below, the normalized amplitude ratio has the form

```math
A_r/A_0=C_r e^{-omega^2r^4/2},
```

with `1<C_r<2`. Therefore

```math
|D_r(omega)|<=A_0(omega).
```

Consequently the canonical increment metric of the difference field is bounded by the rough endpoint metric:

```math
\boxed{
E[(d_r(t+s)-d_r(t))^2]
<=2[1-R_0(s)].
}
```

Near zero,

```math
R_0(s)=1-a_X|s|+O(s^2),
```

with

```text
a_X ~= 6.19142e-5.
```

For the sub-nanosecond-sized mathematical net used below, retain the deliberately loose local metric envelope

```math
\boxed{
E[(d_r(t+s)-d_r(t))^2]
<=K_*|s|,
\qquad K_*=2e-4.
}
```

This is far above the limiting coefficient `2a_X ~=1.2383e-4`.

Cover the search interval `ell=.895` by a deterministic net of spacing

```text
h=1e-9,
N=ceil(ell/h)+1 ~= 8.95e8.
```

For the endpoint subinterval `0<=q<=.0035`, the leading chord is about `1.88e-5`; use the larger working point-SD envelope

```math
\boxed{sigma_* = 2.1e-5.}
```

At the net points, a Gaussian union bound gives

```math
P(max_j|d(t_j)|>e_0)
<=2N exp[-e_0^2/(2sigma_*^2)].
```

Inside a net cell, Sudakov–Fernique comparison with `sqrt(K_*) B(t)` gives the one-sided mean modulus

```math
m_h<=sqrt(2K_*h/pi).
```

Borell concentration followed by a union bound over cells and signs gives

```math
P(max_cells sup_cell |d(t)-d(t_j)|>m_h+x)
<=2N exp[-x^2/(2K_*h)].
```

Choose

```text
eta_grid = 9e-12
eta_mod  = 3e-13.
```

Then

```text
e_0      ~= 2.03037e-4
m_h      ~= 3.56825e-7
x        ~= 4.47841e-6
--------------------------------
epsilon  ~= 2.07872e-4.
```

The maximum threshold motion over `Delta q=.0035` is bounded by

```text
|Delta u| <= 1.96e-5.
```

Using the Step-40 numerical covariance floor `m_*=.92` and the endpoint node envelope

```text
p_0/alpha
<= .98968 + 1.645(.00429) + .002
= .99873705,
```

Cameron–Martin translation plus the coupling failure probabilities gives

```math
\boxed{
p(q)/alpha <= 0.999970
\qquad(0<=q<=.0035).
}
```

Thus the singular rough endpoint interval is covered without any differentiability assumption on `d_{0,q}`.

The enormous time net is only a mathematical covering device; no simulation on `8.95e8` points is performed.

---

## 4. Strictly positive `q`: exact Rice sup-tail bound

If both `q>0` and `r>0`, the Gaussian information factors make `d_{q,r}` differentiable. Define

```math
sigma^2=Var[d_{q,r}(0)],
```

```math
tau^2=Var[d'_{q,r}(0)],
```

and

```math
lambda_d=tau/sigma.
```

For a stationary differentiable centered Gaussian process, Rice's formula gives the expected positive upcrossing count of level `epsilon` on length `ell`:

```math
E[N_epsilon^+]
=ell lambda_d/(2pi)
 exp[-epsilon^2/(2sigma^2)].
```

If the process ever exceeds `epsilon`, either it begins above `epsilon` or has an upcrossing. Applying the same argument to `-d` yields the exact union envelope

```math
\boxed{
P(||d||_infinity>epsilon)
<=2Q(v)
+ell lambda_d/pi e^{-v^2/2},
\qquad v=epsilon/sigma.
}
```

This is substantially sharper here than inserting a generic expected-supremum constant into Borell–TIS.

For each sampled `q` node, optimize `v` against the Step-40 translation cost. Deterministic positive-integrand spectral quadrature supplies conservative half-cell envelopes for `sigma` and `lambda_d`; the low-`q` values are cross-checked against the analytic high-frequency asymptotics.

---

## 5. Node probability envelope inherited from Step 34

Before the old empirical mesh allowance, Step 34's common endpoint/paired numerical envelope is

```math
p_node/alpha
<=
0.98968
+1.645 sqrt(.00429^2+.00106^2)
+.002
+Delta U_node/alpha.
```

The common part is

```math
\boxed{0.99894928.}
```

The sampled paired profile reported

```text
max positive Delta U/alpha ~= 1.9e-8,
```

so nodes without a separately useful negative correction can conservatively use essentially zero correction.

Representative negative corrections retained from Step 34 are

```text
q=.025  -0.00048
q=.040  -0.00045
q=.050  -0.00070
q=.060  -0.00060
q=.065  -0.00115
q=.070  -0.00159
q=.075  -0.00152
q=.0767 -0.00188.
```

For the unprinted `.045` and `.055` nodes, the Step-34 measured maximum adjacent-node change `0.000548 alpha` plus the neighboring printed corrections gives the conservative central upper correction

```text
Delta U(.045)/alpha <= -0.000152
Delta U(.055)/alpha <= -0.000152.
```

This use of the Step-34 profile remains numerical; Step 41 is replacing the *inter-node interpolation allowance*, not re-proving the node Monte Carlo estimates.

---

## 6. Finite-`q` half-cell certificate

The following rounded spectral envelopes deliberately exceed the directly evaluated half-cell `sigma` and `lambda_d` values. The final column is the optimized upper false-alarm ratio after adding the Rice sup-tail failure probability and applying the Step-40 threshold translation with `|Delta u|<=1.4e-5` for a standard half-cell.

```text
anchor q    sigma_*      lambda_*     node correction/alpha   final p/alpha
----------------------------------------------------------------------------
.005        2.10e-5       8.0e4          ~0                 0.999983
.010        2.10e-5       2.0e4          ~0                 0.999965
.015        2.10e-5       8.0e3          ~0                 0.999952
.020        2.10e-5       4.0e3          ~0                 0.999942
.025        2.12e-5       2.5e3        -0.00048             0.999464
.030        2.15e-5       1.55e3         ~0                 0.999950
.035        2.21e-5       1.10e3         ~0                 0.999970
.040        2.28e-5       8.2e2        -0.00045             0.999544
.045        2.38e-5       6.3e2        -0.000152            0.999880
.050        2.52e-5       5.0e2        -0.00070             0.999386
.055        2.68e-5       4.0e2        -0.000152            0.999997
.060        2.89e-5       3.2e2        -0.00060             0.999630
.065        3.13e-5       2.6e2        -0.00115             0.999173
.070        3.41e-5       2.15e2       -0.00159             0.998842
.075        3.72e-5       1.8e2        -0.00152             0.999033
```

For the final short interval `.075 -> .0767`, the maximum anchor distance is only `.00085`; using the `.0767` node correction leaves a much larger margin.

The numerically tightest finite cell is near `q=.055`, but the conservative envelope remains below `alpha`.

---

## 7. First nontrivial consequence

The Step-34 empirical interpolation term

```text
0.0006 alpha
```

is no longer needed for the original fast high-band tail.

The continuous interval is covered by

```text
q in [0,.0035]:
    rough endpoint grid + Brownian-modulus Gaussian concentration;

q > .0035:
    differentiable difference field + exact Rice upcrossing envelope.
```

Each coupling bound feeds directly into the exact-event Cameron–Martin threshold translation from Step 40.

Thus, conditional on the Step-34 numerical node envelopes and the stated conservative spectral constants,

```math
\boxed{
p_f(q)<alpha
\quad\text{for all }0<=q<=0.0767.
}
```

Equivalently, the fast feasibility part of the original

```math
170<=kappa_f<=infinity
```

high-band tail no longer relies on an empirical inter-node probability allowance.

Combined with the much wider slow lower-bound margin from Step 34, this removes the principal *continuity* caveat from the numerical high-band closure.

---

## 8. What this does **not** prove

This step does **not** make the entire result a formal theorem-level certificate because:

- Step-34 node probabilities still use Monte Carlo standard-error allowances rather than rigorous concentration/confidence sequences;
- the spectral `sigma_*`, `lambda_*`, covariance-floor, and local rough-metric envelopes are conservative deterministic floating-point evaluations, not interval arithmetic;
- Step-33/34 finite timing-grid bias is controlled numerically, not by a continuum discretization theorem;
- the slow branch remains covered by the much looser Step-34 numerical lower envelope rather than a formal interval computation;
- no claim is made for other task parameters.

**REFINEMENT:** the remaining gap is no longer continuous-`q` interpolation itself. It is formal certification of the already sampled node/grid quantities.

---

## 9. Stopping point

For the original `r=2`, `Lambda=.895` task, the common-white-noise difference process is now controlled sharply enough between sampled high-band nodes. The previous empirical `0.0006 alpha` interpolation allowance can be replaced by analytic Gaussian-process probability bounds.

### Single natural next question

> Can the occupation-Palm node estimators themselves be given rigorous finite-sample concentration bounds (rather than Gaussian standard-error allowances), so that the remaining high-band certificate becomes statistically explicit rather than numerically heuristic?
