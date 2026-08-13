# Paper A post-revision audit addendum

**Date:** 2026-08-12  
**Status:** FINAL SEMANTIC / LIMIT-PRESENTATION CLEANUP COMPLETED ON REVISION BRANCH

This addendum closes the two manuscript-presentation items left open by `PAPER_A_POST_REVISION_AUDIT_2026-08-12.md`.

---

## 1. True alignment is now explicitly analysis-only

Section III.C now states that `q_0` is the true dimensionless event alignment **under the signal-present generative hypothesis** and is not supplied to the receiver.

Operationally, the receiver still scans the entire uncertainty interval and compares the scan maximum with the global threshold.

The true alignment is used only to evaluate the sufficient lower-bound power

```math
P_{D,true}
=Pr[Y_x(q_0)>\Gamma],
```

which satisfies

```math
P_D^{scan}\ge P_{D,true}.
```

This removes any possible interpretation that the guarantee criterion gives the receiver side information about event time.

---

## 2. Full-template threshold is now defined directly

The manuscript no longer defines `Gamma_infty` only by writing an unqualified limit of finite-template thresholds.

It first defines the full-template stationary Gaussian process

```math
Cov[Z_\infty(q),Z_\infty(q')]
=R_\infty(|q-q'|),
\qquad
R_\infty(y)=(1+y)e^{-y},
```

and then defines

```math
\Gamma_\infty(\ell,\alpha)
=\inf\left\{u:
Pr\left[\sup_{0\le q\le\ell}Z_\infty(q)>u\right]\le\alpha
\right\}.
```

The connection to the finite-template process is now stated separately.

For normalized templates

```math
\hat h_x(v)
=\frac{v e^{-v}1_{[0,x]}(v)}{\|v e^{-v}1_{[0,x]}\|_2},
```

```math
\hat h_\infty(v)
=\frac{v e^{-v}1_{[0,\infty)}(v)}{\|v e^{-v}1_{[0,\infty)}\|_2},
```

we have

```math
\|\hat h_x-\hat h_\infty\|_2\to0.
```

Their autocovariances obey the uniform bound

```math
\boxed{
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
}
```

Thus, on every fixed compact search interval, the finite-template Gaussian scans converge to the full-template scan at the covariance level; threshold convergence follows under the same ordinary supremum-quantile continuity regularity already carried by Proposition 1.

This makes the role of `Gamma_infty` explicit and removes the presentation gap identified in the first post-revision audit.

---

## 3. Current remaining Paper A issues

After this cleanup, the conceptual / semantic major-revision items are closed.

Remaining before submission:

```text
1. exact-hard-window quantitative example / numerical presentation strategy;
2. deepest radar/sonar/ladar/synchronization closest-prior-art audit;
3. final citation/manuscript QA after those two items;
4. figures and journal formatting only after scientific closure.
```

The Step-49 Gaussian-extremes hard stop remains active. No Step 50 has been opened.
