# Step 16 — Rare-Event Upcrossing Importance Sampling at `alpha = 10^-6`

**Date:** 2026-08-11 14:33 EDT  
**Status:** DERIVED / NUMERICAL VALIDATION / REFINEMENT. An exact Palm/upcrossing identity is used to construct a low-variance rare-event estimator for the smooth finite-`kappa` Gaussian timing scan. At `alpha=10^-6`, the tested `kappa=8` model is overwhelmingly a single-high-excursion problem, so the first-order Rice/Euler-characteristic threshold is quantitatively extremely accurate. A rare-event-corrected fast/slow crossover is obtained for a deliberately compact validation task and differs from the Rice crossover by only about `0.1%`. The result is model/task specific; no novelty claim.

---

## 1. Question

Can the smooth finite-bandwidth correlated timing scan from Steps 14–15 be evaluated directly at a detector-relevant global false-alarm probability such as

```math
\alpha=10^{-6}
```

without requiring `~10^8` brute-force paths, and how accurate is the Rice/Euler-characteristic prediction in that rare-event regime?

The answer for the present smooth regularized model is **yes**.

The key is to bias the simulation toward an actual high-level upcrossing rather than wait for a rare excursion to appear spontaneously.

---

## 2. First rare-event route tried — exact point-exceedance mixture on a timing grid

Let a correlated Gaussian timing scan be sampled at `n` timing points,

```math
X=(X_1,\ldots,X_n),
```

with target density `f`, and define

```math
A_u=\{\max_j X_j>u\}.
```

Choose an index `I` uniformly from `{1,...,n}` and sample from the exact conditional target law

```math
f(X\mid X_I>u).
```

Let

```math
K_u(X)=\sum_{j=1}^n 1_{\{X_j>u\}}
```

be the number of above-threshold grid samples. Since each standard-normal marginal has exceedance probability

```math
Q(u),
```

the mixture proposal density is

```math
q(X)
=f(X)\frac{K_u(X)}{nQ(u)}.
```

Therefore the exact grid-event importance weight is

```math
\boxed{
w(X)=\frac{nQ(u)}{K_u(X)}.
}
```

and

```math
\boxed{
P(A_u)=E_q[w(X)].
}
```

This sampler works and reduces the `10^-6` problem from an impossible brute-force tail to a few-thousand-path calculation.

However, it still estimates the **grid maximum**, not the continuous supremum. In the present smooth process that bias is much smaller than in Step 13, but at the precision required to locate a crossover near a feasibility edge it was still visible. This motivated a continuous-upcrossing construction.

**REFINEMENT:** the point-mixture sampler is not wrong; it answers the discretized event exactly. It is simply not the cleanest estimator of the continuous timing-search event.

---

## 3. Exact continuous event decomposition

Let `z(t)` be a differentiable stationary unit-variance Gaussian process on `[0,L]` with derivative standard deviation

```math
\sigma=\sqrt{-r''(0)}.
```

Let

```math
N_u^+
```

be the number of positive-slope crossings of level `u` in `(0,L)`.

Ignoring zero-probability tangential-touch pathologies, the event

```math
\sup_{0\le t\le L}z(t)>u
```

occurs in exactly one of two disjoint ways:

1. the record starts above threshold, `z(0)>u`; or
2. it starts at or below threshold and contains at least one upcrossing.

Thus

```math
\boxed{
P_{FA}(u)
=Q(u)
+P\!\left[z(0)\le u,\;N_u^+\ge1\right].
}
```

For a differentiable stationary Gaussian scan, Rice gives the exact expected number of upcrossings

```math
\boxed{
\lambda_u
\equiv E[N_u^+]
=L\frac{\sigma}{2\pi}e^{-u^2/2}.
}
```

---

## 4. Palm distribution of a randomly selected upcrossing

Define the upcrossing Palm law `P_up` by size-biasing paths by their number of level-`u` upcrossings:

```math
dP_\uparrow
=\frac{N_u^+}{\lambda_u}\,dP.
```

Equivalently, for the stationary Gaussian process, one can construct a Palm path by:

1. selecting the upcrossing time uniformly over the search interval;
2. conditioning

```math
z(T)=u;
```

3. drawing the derivative at the crossing from

```math
\boxed{
V=z'(T)\sim\text{Rayleigh}(\sigma),
}
```

because its Palm density is

```math
\boxed{
p_\uparrow(v)
=\frac{v}{\sigma^2}e^{-v^2/(2\sigma^2)},
\qquad v>0.
}
```

For a zero-mean stationary Gaussian process, `z(T)` and `z'(T)` are independent before conditioning because `r'(0)=0`.

If the selected upcrossing is placed at time zero for convenience, the conditional mean of the path is

```math
\boxed{
m(t)
=r(t)u
-\frac{r'(t)}{\sigma^2}V.
}
```

The residual covariance is obtained by the standard two-linear-functional Gaussian conditioning formula.

---

## 5. Exact rare-event identity

Under the Palm law, the marginal path density is proportional to `N_u^+` times the original path density. Therefore

```math
\boxed{
P\!\left[z(0)\le u,\;N_u^+\ge1\right]
=
\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

Hence the exact continuous false-alarm probability is

```math
\boxed{
P_{FA}(u)
=
Q(u)
+
\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
}
```

This is the central Step-16 rare-event identity.

It immediately gives the rigorous upper bound

```math
\boxed{
P_{FA}(u)
\le
Q(u)+\lambda_u.
}
```

The familiar first-order Rice/Euler-characteristic expression

```math
Q(u)+L\frac{\sigma}{2\pi}e^{-u^2/2}
```

is therefore an **upper bound** in this one-dimensional continuous differentiable setting, not merely a heuristic formula.

Its overcount has a precise origin:

- paths that start above `u` and later have an upcrossing would otherwise be counted twice;
- paths containing multiple upcrossings are counted multiple times by `E[N_u^+]`.

When almost every rare path is a single isolated excursion and starts below threshold, the Palm factor is nearly one and the Rice expression becomes extremely accurate.

---

## 6. Why the estimator has very low variance at high threshold

The Monte Carlo estimator is

```math
\widehat P_{FA}
=Q(u)
+\lambda_u\frac1M
\sum_{m=1}^M
\frac{1_{\{z_m(0)\le u\}}}{N_{u,m}^+},
```

where each `z_m` is drawn from the upcrossing Palm law.

At a sufficiently high threshold:

```text
N_u^+ = 1
```

for almost every Palm path, and the initial point is almost always below threshold. Then each importance contribution is nearly the constant `lambda_u`.

This is why the method can estimate a `10^-6` global false-alarm probability with only thousands of paths.

It also explains why a naive point-exceedance mixture has substantially larger variance: it size-biases by time spent above the threshold, so the cluster length remains in the importance weight.

---

## 7. Numerical model retained from Step 15

Use the same smooth Gaussian information weighting

```math
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2},
```

with

```math
H_x(\nu)
=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}{(1+i\nu)^2}.
```

The normalized spectral weight gives

```math
\sigma_\nu^2
=\frac{\int \nu^2J_{x,\kappa}(\nu)d\nu}
{\int J_{x,\kappa}(\nu)d\nu}.
```

The periodic FFT representation used in Step 15 is retained. Under each Palm draw the jointly simulated process and derivative are conditioned on

```math
z(0)=u,
\qquad
z'(0)=V>0.
```

Secondary upcrossings and the record-start condition are evaluated on a fine local timing grid. Since they are rare corrections to a forced continuous upcrossing, this grid requirement is much milder than resolving an unconditioned maximum directly.

The implementation is stored in

```text
numerics/upcrossing_importance_sampling.py
```

---

## 8. Detector-relevant rare-event validation task

At

```math
\alpha=10^{-6},
```

the earlier Step-15 value `rho_0=5` is infeasible even for known event time because

```math
\Phi^{-1}(1-10^{-6})+\Phi^{-1}(0.90)
\approx4.75342+1.28155
\approx6.03498
>5.
```

Therefore use the deliberately near-threshold validation task

```text
rho_0 = 6.2
r = tau_s/tau_f = 1.2
alpha = 1e-6
beta = 0.90
kappa = 8
```

This choice keeps the rare-event crossover in a compact normalized timing interval so the method itself can be tested before attempting large search domains or the original extreme response-time ratio.

---

## 9. Rice-predicted crossover at `alpha=10^-6`

For this validation task, the Step-15 Rice/Euler-characteristic calculation gives

```text
ell_s^Rice = L_cross/tau_s ~= 0.571441752
ell_f^Rice = r ell_s ~= 0.685730102
```

with dimensionless decision/filter durations

```text
x_s ~= 4.473364397
x_f ~= 5.368037276
```

and search thresholds

```text
u_s^Rice ~= 4.895464822
u_f^Rice ~= 4.913100340.
```

---

## 10. Palm rare-event test at the Rice crossover

Using an exact-length local interval, periodic synthesis period `~16`, target local step `~0.005`, and `5000` Palm paths:

### Slow scan

```text
Rice target alpha           = 1.0000000e-6
Palm estimate P_FA          = 9.9949037e-7
MC standard error           = 2.04e-10
fraction with N_u^+ > 1     ~= 8e-4
endpoint-overlap fraction   ~= 6e-4
```

### Fast scan

```text
Rice target alpha           = 1.0000000e-6
Palm estimate P_FA          = 9.9922753e-7
MC standard error           = 2.70e-10
fraction with N_u^+ > 1     ~= 8e-4
endpoint-overlap fraction   ~= 1e-3
```

Thus Rice slightly overestimates the exact false-alarm probability, exactly as the upper-bound identity requires, but the correction is tiny:

```text
slow relative probability correction ~= -0.051%
fast relative probability correction ~= -0.077%
```

The corresponding first-order threshold corrections are only approximately

```text
slow: delta Gamma ~= -1.02e-4
fast: delta Gamma ~= -1.55e-4.
```

So at this `10^-6` operating point the Rice threshold is quantitatively accurate to much better than `10^-3` in absolute Gaussian-threshold units for the tested smooth process.

---

## 11. Grid/refinement behavior of the Palm correction

The Palm estimator was repeated with target local steps

```text
0.01, 0.005, 0.0025
```

using `3000` paths at each resolution.

The resulting false-alarm estimates remained in the narrow neighborhood

```text
slow: ~9.993e-7 to ~9.997e-7
fast: ~9.984e-7 to ~9.994e-7.
```

No Step-13-like systematic continuum drift appeared.

The remaining spread is used as a numerical-systematic warning rather than hidden inside the very small conditional Monte Carlo standard error.

---

## 12. Rare-event-corrected crossover

Because the fast detector is close to its feasibility edge, even a `~10^-4` threshold correction can noticeably change its required dimensionless decision time. Therefore the threshold correction was propagated through the detection-time equations rather than comparing threshold values alone.

A first correction from the Rice crossover moved the estimated boundary to

```text
ell_s ~= 0.57233.
```

A second Palm evaluation at that point left a crossover residual statistically consistent with zero and gave the refined estimate

```math
\boxed{
\ell_{\times}^{Palm}
\approx0.5721.
}
```

The linearized Monte Carlo uncertainty from the Palm estimator is about

```text
+/- 0.0004
```

in `ell_s`; allowing conservatively for local-grid, finite-period, and first-order propagation effects, this step treats approximately

```text
ell_cross^Palm ~= 0.5721 +/- 0.001
```

as the appropriate numerical summary for this validation problem.

The Rice prediction was

```text
ell_cross^Rice ~= 0.57144.
```

Therefore the rare-event correction shifts the crossover by only about

```text
0.00066 in ell_s
~0.12% relative.
```

A direct re-evaluation near `ell_s ~=0.57210` gave a Palm-corrected crossover residual consistent with zero within the propagated uncertainty.

**NUMERICAL VALIDATION / CONDITIONAL:** for this smooth `kappa=8`, `alpha=10^-6`, near-threshold task, Rice theory predicts the fast/slow crossover to approximately `0.1%` accuracy in normalized timing uncertainty.

---

## 13. Why the earlier grid-point importance sampler appeared less accurate

The initial point-exceedance mixture estimates the event

```math
\max_j z(t_j)>u
```

on a discrete timing grid. At `alpha=10^-6`, it produced percent-level deficits relative to the Rice continuous prediction at practical grid spacings.

The Palm estimator instead forces a **continuous upcrossing** and uses the grid only to detect rare secondary crossings and endpoint overlap.

Therefore the discrepancy is not evidence that the Palm identity and point-mixture identity disagree. They estimate different events until the timing grid becomes sufficiently fine:

```text
point mixture -> exact grid maximum
Palm method   -> continuous upcrossing event, with discretized correction counting
```

This distinction is retained explicitly because otherwise the earlier percent-level grid deficit could be misread as a failure of Rice theory.

---

## 14. First nontrivial consequence

At very small global false-alarm probability, the smooth one-dimensional timing-search problem becomes simpler in a precise sense.

The exact identity

```math
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
```

shows that the Rice/Euler-characteristic prediction fails only through **multiple high excursions and endpoint/upcrossing overlap**.

For the tested `alpha=10^-6` process, both corrections are at the `10^-3` level in the Palm ensemble, so

```math
Q(u)+\lambda_u
```

is nearly exact.

Thus the increasingly stringent false-alarm requirement does **not** make the smooth-process threshold calculation harder in the same way brute-force Monte Carlo suggests; it actually drives the rare-event geometry toward isolated excursions where Rice/Palm methods become especially effective.

---

## 15. What has been established

- **DERIVED:** exact point-exceedance mixture importance weight `nQ(u)/K_u` for the discretized correlated Gaussian scan.
- **DERIVED:** exact continuous Palm/upcrossing identity

```math
P_{FA}=Q(u)+\lambda_uE_\uparrow[1_{z(0)\le u}/N_u^+].
```

- **DERIVED:** `Q(u)+lambda_u` is an upper bound for the one-dimensional differentiable stationary Gaussian continuous-supremum false-alarm probability.
- **DERIVED:** the Palm crossing slope is Rayleigh distributed with scale `sigma`.
- **IMPLEMENTED:** low-variance Palm rare-event simulation of the smooth Step-15 regularized scan.
- **NUMERICAL VALIDATION:** at `alpha=10^-6`, `kappa=8`, the Palm false-alarm estimates at the Rice thresholds differ from `10^-6` by less than `0.1%` for the tested slow and fast scans.
- **NUMERICAL VALIDATION / CONDITIONAL:** the rare-event-corrected crossover `ell_s ~=0.5721 +/-0.001` differs from Rice `0.57144` by only `~0.12%` for the stated validation task.
- **REFINEMENT:** the earlier point-mixture percent-level deficit is a finite-grid maximum effect, not evidence of a percent-level error in the continuous Rice threshold.

---

## 16. What has not been established

- No proof that Rice is this accurate for every `kappa`, search interval, covariance shape, or detector family.
- No rare-event phase diagram across broad `(rho_0,r,beta,kappa)` space yet.
- No result yet for the original extreme `tau_s/tau_f=10^9` comparison at `alpha=10^-6`.
- No proof of crossover uniqueness.
- No same-fixed-physical-bandwidth comparison across unequal `tau` detectors.
- The Palm implementation still uses a finite local grid to count rare secondary upcrossings and endpoint overlap; the observed resolution stability is numerical evidence, not an analytic error bound.
- No exact global-rejection/localization surface; the criterion remains true-alignment threshold crossing.
- No novelty claim.

---

## 17. Stopping point

A detector-relevant `10^-6` false-alarm calculation is now numerically tractable and Rice theory has been quantitatively validated for one smooth regularized task.

### Single natural next question

> Does the near-exact Rice/Palm result persist when the dimensionless timing bandwidth `kappa` and speed ratio `r` are varied, and can the rare-event method reveal a simple asymptotic law for the fast/slow crossover in the high-threshold limit?