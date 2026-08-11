# Step 26 — Coupled High-Band Boundary Derivative Along the Physical Detector Trajectories

**Date:** 2026-08-11 19:48 EDT  
**Status:** DERIVED / NUMERICAL ASYMPTOTIC / CONDITIONAL / REFINEMENT / OPEN. Step 25 proved that the local two-parameter generalized Pickands constant `H(chi,zeta)` is coordinatewise monotone, but that did not determine the sign of the physical fast/slow boundary derivative because bandwidth simultaneously changes finite-duration SNR, available threshold, integration time, `chi`, and `zeta`. This step expands the actual coupled boundary at large physical bandwidth. The finite-window SNR approaches its infinite-band value as `O(1/kappa)`, whereas Dieker–Yakir data show the finite-band generalized Pickands constant approaching its rough endpoint as `O(zeta^-1/2) = O(kappa^-1/2)` along the relevant trajectories. Under that numerically validated leading smoothing law, the `r=2` calibration has

```math
\boxed{
\Lambda_\times(\kappa_f)
=\Lambda_\infty
+\frac{C_\Lambda}{\sqrt{\kappa_f}}
+O(\kappa_f^{-1}),
\qquad C_\Lambda>0,
}
```

so

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa_f}<0
}
```

for sufficiently large `kappa_f`: the boundary approaches the direct rough-limit value from above. This excludes an **asymptotic** high-band reversal, but does not yet rigorously exclude a bounded pre-asymptotic re-entrant pocket because the `zeta^-1/2` smoothing law and its uniform remainder have not yet been proved for this two-parameter field. No novelty claim.

---

## 1. Question

The Step-25 local constant satisfies

```math
\partial_\zeta\mathcal H\ge0,
\qquad
\partial_\chi\mathcal H\ge0.
```

But the physical bandwidth sweep is not a one-coordinate path. For common physical bandwidth,

```math
\kappa_f=\kappa,
\qquad
\kappa_s=r\kappa,
```

and at common physical decision time `X=T/tau_f`,

```math
x_f=X,
\qquad
x_s=X/r.
```

Each detector has its own

```text
rho_i(X,kappa_i)
u_i = rho_i - Phi^-1(beta)
chi_i = a_i u_i/sqrt(b_i)
zeta_i = kappa_i/(sqrt(2) u_i sqrt(b_i)).
```

The actual question is therefore the sign of

```math
\frac{d\Lambda_\times}{d\kappa}
```

along the common-time equality of the two detector task boundaries.

---

## 2. Exact implicit derivative structure

Let

```math
A_f(X,\kappa)
```

be the maximum physical timing uncertainty `Lambda=L/tau_f` admissible by the fast detector at common decision time `X`, and let

```math
A_s(X,\kappa)
```

be the same physical quantity inferred from the slow detector. The preference boundary satisfies

```math
\boxed{
F(X,\kappa)=A_f(X,\kappa)-A_s(X,\kappa)=0.
}
```

Then

```math
\frac{dX}{d\kappa}
=-\frac{A_{f,\kappa}-A_{s,\kappa}}
{A_{f,X}-A_{s,X}}.
```

Since

```math
\Lambda_\times=A_f(X(\kappa),\kappa),
```

the exact chain rule gives

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa}
=
\frac{
A_{f,X}A_{s,\kappa}
-A_{s,X}A_{f,\kappa}
}
{A_{f,X}-A_{s,X}}.
}
```

This identity is approximation-independent. The remaining work is the high-band asymptotics of the four partial derivatives.

---

## 3. High-band SNR recovery for a finite hard window

The finite template is

```math
h_x(v)=ve^{-v}1_{[0,x]}(v).
```

Its Fourier transform has endpoint asymptotic

```math
H_x(\nu)
=-\frac{x e^{-x}e^{-i\nu x}}{i\nu}
+O(\nu^{-2}),
```

so

```math
|H_x(\nu)|^2
=\frac{x^2e^{-2x}}{\nu^2}
+o(\nu^{-2}).
```

With Gaussian information weighting `exp[-(nu/kappa)^2]`, the missing spectral energy is therefore

```math
I_0(\infty)-I_0(\kappa)
=
\frac{2\sqrt\pi\,x^2e^{-2x}}{\kappa}
+o(\kappa^{-1}).
```

Since

```math
I_0(\infty)=\frac\pi2\eta(x),
```

and

```math
a_x=\frac{2x^2e^{-2x}}{\eta(x)},
```

the finite-duration matched-filter SNR obeys

```math
\boxed{
\rho(x,\kappa)
=\rho_\infty(x)
\left[
1-\frac{a_x}{\sqrt\pi\,\kappa}
+o(\kappa^{-1})
\right].
}
```

Thus the finite-window SNR deficit is `O(kappa^-1)`.

**REFINEMENT:** this differs from the Step-19 **full-template** SNR deficit, which was `O(kappa^-2)`. The hard finite endpoint changes the high-frequency tail from `1/nu^4` to `1/nu^2`.

---

## 4. Observed convergence law of the generalized Pickands constant

Step 25 gave, at `chi=0.1`,

```text
zeta      H(0.1,zeta)
9         0.67671
19        0.70538
40        0.72422
infinity  0.76698
```

The products

```text
sqrt(zeta) * [H(infinity)-H(zeta)]
```

are approximately

```text
zeta=9:   0.2708
zeta=19:  0.2685
zeta=40:  0.2705.
```

This is a striking `zeta^-1/2` sequence over the tested range.

The actual Step-23 rough-limit equality has approximately

```text
X ~ 7.75
chi_fast ~ 1.1e-4
chi_slow ~ 6.4e-2.
```

Additional Dieker–Yakir runs along those local values give approximately

```text
fast chi ~1.14e-4:
    C_H = sqrt(zeta)[H(infinity)-H(zeta)]
    ~0.0058, 0.0061, 0.0061 for zeta=20,40,80

slow chi ~0.0645:
    C_H
    ~0.210, 0.204, 0.192 for zeta=20,40,80.
```

Within Monte Carlo error and pre-asymptotic drift, both are consistent with

```math
\boxed{
\mathcal H(\chi,\zeta)
=\mathcal H_{mix}(\chi)
-\frac{C_H(\chi)}{\sqrt\zeta}
+O(\zeta^{-1}),
\qquad C_H(\chi)>0.
}
```

**NUMERICAL ASYMPTOTIC / NOT YET A THEOREM:** the `zeta^-1/2` rate is empirically very strong, but this step does not claim a proved uniform expansion for the present Gaussian smoothing family.

The square-root rate is physically consistent with the Brownian local roughness of the hard-window endpoint: smoothing acts over lag `~1/zeta`, while Brownian-scale fluctuations over that lag are `O(zeta^-1/2)`.

---

## 5. Why the extreme-statistics correction dominates the SNR correction

At fixed finite `x`,

```math
\zeta_i
=\frac{\kappa_i}
{\sqrt2\,u_i\sqrt{b_i}}
=O(\kappa_i).
```

Therefore the observed generalized-Pickands correction is

```math
\mathcal H_{mix}-\mathcal H
=O(\kappa_i^{-1/2}),
```

whereas

```math
\rho_\infty-\rho
=O(\kappa_i^{-1}).
```

Hence, if the positive `zeta^-1/2` coefficient persists asymptotically,

```math
\boxed{
\text{finite-band extreme-statistics correction}
\gg
\text{finite-band SNR correction}
}
```

at sufficiently large bandwidth.

This gives the first controlled ordering of the two effects along the **finite-window** physical trajectory.

---

## 6. Finite-`u` boundary surrogate used for the derivative coefficient

To estimate the derivative coefficient without pretending the leading `uQ(u)` Pickands law is percent-level exact at `u~5`, use the Mills-corrected tangent surrogate

```math
P_{FA}
\approx
Q(u)
+\ell\,
\frac{\sqrt b}{\sqrt2}
\mathcal H(\chi,\zeta)\phi(u).
```

At `chi=0` this reproduces the exact smooth Rice coefficient because

```math
\mathcal H(0,\zeta)=1/\sqrt\pi.
```

The admissible normalized search length is therefore modeled as

```math
\ell_{adm}
=\frac{\alpha-Q(u)}
{(\sqrt b/\sqrt2)\mathcal H(\chi,\zeta)\phi(u)}.
```

For the fast detector `A_f=ell_adm`; for the slow detector `A_s=r ell_adm`.

**DEFINED / CONDITIONAL:** this is a deterministic finite-`u` tangent surrogate used to determine the high-band sign and scale. It is not substituted for the exact Palm/occupation calculations as the final finite-`alpha` boundary.

---

## 7. Coupled `1/sqrt(kappa)` boundary expansion

Suppose

```math
\mathcal H_i
=\mathcal H_{i,\infty}
-\frac{C_i}{\sqrt{\zeta_i}}
+O(\zeta_i^{-1}).
```

Let

```math
s_f=1,
\qquad
s_s=r,
```

so `kappa_i=s_i kappa_f`.

At fixed `X`, the dominant finite-band increase in admissible physical search length is

```math
A_i(X,\kappa_f)
=A_i^{\infty}(X)
+\frac{d_i(X)}{\sqrt{\kappa_f}}
+O(\kappa_f^{-1}),
```

where

```math
\boxed{
d_i
=A_i^{\infty}
\frac{C_i}{\mathcal H_{i,\infty}}
\left(
\frac{\sqrt2\,u_i\sqrt{b_i}}{s_i}
\right)^{1/2}.
}
```

Write the common-time solution as

```math
X(\kappa_f)
=X_\infty
+\frac{x_1}{\sqrt{\kappa_f}}
+O(\kappa_f^{-1}).
```

Then

```math
\boxed{
x_1
=-\frac{d_f-d_s}
{A_{f,X}^{\infty}-A_{s,X}^{\infty}}.
}
```

Finally,

```math
\boxed{
\Lambda_\times(\kappa_f)
=\Lambda_\infty
+\frac{C_\Lambda}{\sqrt{\kappa_f}}
+O(\kappa_f^{-1}),
}
```

with

```math
\boxed{
C_\Lambda
=
\frac{
A_{f,X}^{\infty}d_s
-A_{s,X}^{\infty}d_f
}
{A_{f,X}^{\infty}-A_{s,X}^{\infty}}.
}
```

Therefore

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa_f}
=-\frac{C_\Lambda}{2\kappa_f^{3/2}}
+O(\kappa_f^{-2}).
}
```

The sign question is reduced to the sign of one explicit coefficient.

---

## 8. Sign for the `r=2` calibration

Using the Step-20/23 calibration and the deterministic tangent endpoint near

```text
X_infinity ~7.73
```

(close to the direct occupation-time value `~7.75`), the local boundary sensitivities are approximately

```text
A_f,X ~4.9e-3
A_s,X ~4.5e-1.
```

The slow detector's admissible physical search interval is therefore almost two orders of magnitude more sensitive to additional common integration time than the fast detector's nearly saturated interval.

Using the Dieker–Yakir endpoint/smoothing estimates

```text
C_fast ~0.006
C_slow ~0.20
```

gives representative high-band coefficients

```text
d_fast ~2.5e-2
d_slow ~4.7e-1.
```

Substitution into the coupled formula gives

```math
\boxed{
C_\Lambda\approx +2\times10^{-2}
}
```

in the finite-`u` tangent surrogate, together with

```text
x_1 ~ -1.
```

The coefficient magnitude is not treated as a precise physical boundary prediction—the exact Palm map is still pre-asymptotic enough to show a larger effective displacement—but its **sign is robust** to the Monte Carlo uncertainty of the local `C_i` estimates.

Hence

```math
\boxed{
\Lambda_\times(\kappa_f)
>\Lambda_\infty
}
```

for sufficiently large finite bandwidth, and

```math
\boxed{
\frac{d\Lambda_\times}{d\kappa_f}<0
}
```

in that asymptotic tail.

This agrees with the Step-22 Palm map, which was already approximately flat-to-decreasing from `kappa_f~100` to `200`, and with the Step-23 rough endpoint near `Lambda~0.905` lying below the finite-high-band boundary near `~0.91`.

---

## 9. Consequence for a re-entrant pocket

The Step-20 Rice calculation suggested a high-band second reversal for the horizontal slice `Lambda=0.895`. Steps 21–23 invalidated that switch numerically and showed fast preference again at `kappa=infinity`.

Step 26 adds a trajectory-level asymptotic constraint:

```math
\boxed{
\text{the high-band boundary eventually decreases toward its rough endpoint.}
}
```

Therefore an additional slow-preferred pocket, if it exists at all, cannot persist or reappear arbitrarily far into the high-band tail.

It would have to be a bounded pre-asymptotic structure:

```text
fast preferred
-> hypothetical slow pocket
-> fast preferred again
-> eventual monotone approach to Lambda_infinity.
```

No such pocket has appeared in the direct Palm checks through `kappa_f=300`, the Step-22 boundary map, or the direct infinite-band endpoint.

### But it is not yet rigorously excluded

The eventual-negative-slope conclusion currently rests on the numerically observed positive `zeta^-1/2` convergence law of `H(chi,zeta)`.

To turn this into a theorem strong enough to close the pocket completely, one still needs:

1. a proof of the leading finite-band smoothing expansion for `H(chi,zeta)` with positive coefficient along the relevant `chi` range;
2. a uniform remainder bound large enough to certify a finite bandwidth beyond which the derivative cannot change sign;
3. coverage of the remaining compact bandwidth interval below that certified threshold.

---

## 10. Relation to known Brownian discretization scaling

The observed square-root rate is not arbitrary: for the classical Brownian (`alpha=1`) Pickands constant, the discrete-to-continuous error is rigorously proportional to the square root of grid spacing. That result is **supporting analogy only**; finite-band Gaussian smoothing is not the same operation as discrete sampling, so it is not used as a proof of the present `zeta^-1/2` law.

---

## 11. What is established

### DERIVED

- exact implicit physical-boundary derivative formula;
- finite-hard-window SNR recovery `rho_infinity-rho = O(kappa^-1)`;
- coupled `1/sqrt(kappa)` boundary expansion **conditional on** the observed leading Pickands smoothing law;
- explicit coefficient controlling the high-band slope.

### NUMERICAL ASYMPTOTIC / CONDITIONAL

- `H_mix(chi)-H(chi,zeta)` follows a very clean `zeta^-1/2` law in the Step-25 `chi=0.1` sequence;
- the same rate is supported along the actual fast and slow endpoint `chi` values;
- the `r=2` coefficient `C_Lambda` is positive in the finite-`u` tangent surrogate;
- consequently the physical boundary approaches the rough endpoint from above with eventual negative slope.

### OPEN

- proof of the `zeta^-1/2` smoothing law for the present two-parameter field;
- a uniform remainder/error bound at finite `u~5`;
- a certified finite `kappa` beyond which `dLambda/dkappa<0` is guaranteed for the exact process;
- rigorous exclusion of a bounded pre-asymptotic re-entrant pocket;
- arbitrary task-parameter classification;
- hardware interpretation;
- novelty.

---

## 12. First nontrivial consequence

**REFINEMENT:** the remaining pocket question is no longer an unrestricted high-band topology problem.

Under the observed and numerically stable Brownian smoothing law,

```math
\boxed{
\Lambda_\times(\kappa_f)
=\Lambda_\infty+C_\Lambda\kappa_f^{-1/2}+\cdots,
\qquad C_\Lambda>0,
}
```

so any hypothetical re-entrant slow-preferred region must be confined to a bounded pre-asymptotic bandwidth interval.

---

## 13. Stopping point

The high-band physical derivative has a definite asymptotic sign conditional on the empirically stable `zeta^-1/2` generalized-Pickands convergence law.

### Single natural next question

> Can the `H_mix(chi)-H(chi,zeta) ~ C_H(chi)/sqrt(zeta)` law be derived or bounded rigorously for the Gaussian-smoothed Brownian endpoint field, with a uniform remainder strong enough to certify a finite `kappa` beyond which the exact detector boundary must be monotone decreasing?
