# Step 45 — Witness-Time Margin Scan Before Continuum Certification

**Date:** 2026-08-12 18:41 EDT  
**Status:** PAIRED NUMERICAL WITNESS SCAN / NEGATIVE RESULT / REFINEMENT / OPEN. Step 44 produced a genuine 95% finite-grid statistical certificate at the fast rough endpoint, but with only `4.22e-5 alpha` margin, while the old conservative timing-grid allowance is `0.002 alpha`. Before attempting a difficult continuum discretization theorem, this step tests whether slightly shifting the common witness time `X` creates a materially larger proof margin. A common-random-number scan shows that increasing `X` does reduce the fast rough-endpoint long-cluster mean, but only at the `~1e-3–2e-3 alpha` level before the slow rough-endpoint lower bound approaches feasibility. Thus witness redesign alone does not create a comfortable margin: `X=7.5` preserves a large slow margin but gains only `~0.0016 alpha`, still smaller than the old grid allowance; `X=7.7` gains about `~0.0020 alpha`, but the slow lower bound falls to only `~1.013 alpha`. The natural next target is therefore continuum timing-grid bias itself rather than further witness-time tuning. No novelty claim.

---

## 1. Why scan `X` with common random numbers

Absolute occupation-Palm estimates have Monte Carlo standard error of order `1e-2 alpha` in modest pilot runs, while the witness-time effect being sought is only a few `1e-3 alpha`. Independent runs cannot resolve that difference efficiently.

For the fast rough endpoint, keep fixed

```text
Lambda = 0.895
Delta  = 0.15
L0     = 0.02
kappa  = infinity
```

and generate candidate `X` values from the **same**:

- spectral white-noise realization;
- lower-level Palm uniform variate;
- selected occupation time.

For each `X`, the marginal field and Palm-conditioned sample remain correct. Therefore the paired difference estimator satisfies

```math
E[\widehat U(X)-\widehat U(X_0)]
=U(X)-U(X_0),
```

with substantially reduced variance.

The baseline is

```text
X0 = 7.16.
```

This scan is a witness-design diagnostic, not a replacement for the Step-44 certificate.

---

## 2. Broad pilot: increasing `X` only weakly moves the fast endpoint

A `20000`-path common-random-number scan on timing spacing about `.0015` gives:

```text
X       mean/alpha     change from X=7.16 / alpha     paired SE / alpha
------------------------------------------------------------------------
6.80    0.99783               +0.00480                   0.00133
7.00    0.99569               +0.00266                   0.00132
7.16    0.99303                0                         --
7.30    0.99229               -0.00074                   0.00109
7.50    0.99199               -0.00104                   0.00105
7.70    0.99196               -0.00107                   0.00099
```

The absolute means in this modest scan should not be compared directly with the Step-44 `200000`-path estimate; only the paired changes are informative here.

**REFINEMENT:** the fast endpoint is already close to its large-`X` saturation regime. Moving the witness time by several tenths changes the false-alarm upper moment by only a few `1e-3 alpha`.

---

## 3. Higher-statistics paired check at the useful upper end

A separate `50000`-path paired run with the same construction compares only

```text
X = 7.16, 7.50, 7.70.
```

It gives

```text
X       mean/alpha     change from 7.16 / alpha     paired SE / alpha
-----------------------------------------------------------------------
7.16    0.998787                0                        --
7.50    0.997212             -0.001575                 0.000789
7.70    0.996781             -0.002006                 0.000735
```

Thus the central paired gain is approximately

```math
\boxed{\Delta U_f(7.50)/\alpha\approx-0.0016}
```

and

```math
\boxed{\Delta U_f(7.70)/\alpha\approx-0.0020.}
```

These are numerical paired estimates, not finite-sample confidence certificates for the differences.

---

## 4. Slow rough-endpoint cost of moving the witness

The common witness must still leave the slow detector infeasible at the same physical time. A separate rough-endpoint cluster-moment pilot with `30000` paths gives:

```text
X       slow lower/alpha     slow E[C]/alpha     SE[E(C)]/alpha
----------------------------------------------------------------
7.50       1.08933              1.09003              0.00537
7.70       1.01340              1.01396              0.00508
```

The quoted SE is for `E[C]`, not a rigorous confidence bound for the Paley-Zygmund lower ratio.

The trend is decisive even without precision boundary work:

- at `X=7.50`, slow infeasibility still has a broad numerical margin;
- by `X=7.70`, the slow lower estimate is only about `1.3%` above `alpha` and is already becoming another near-boundary object.

A broader `10000`-path scan places the slow rough-endpoint crossing near `X~7.8`.

---

## 5. Compare witness gain with the continuum-bias problem

Step 44's finite-grid statistical bound at `X=7.16` is

```text
P_fast^(finite-grid,95%)/alpha < 0.999957771.
```

Its certified margin is

```text
0.00004223 alpha.
```

The old conservative grid allowance is

```text
0.002 alpha.
```

If the paired central shift were transferred to the Step-44 bound solely as a design estimate:

```text
X=7.50:
    predicted extra fast margin ~0.0016 alpha
    still smaller than old 0.002 alpha grid allowance;

X=7.70:
    predicted extra fast margin ~0.0020 alpha
    only barely comparable to old grid allowance,
    while slow lower is already ~1.013 alpha.
```

This is intentionally **not** presented as a new confidence certificate, because the paired differences themselves have not been wrapped in a simultaneous finite-sample bound and the grid model changes slightly with `X`.

---

## 6. NEGATIVE RESULT — witness shifting does not buy a comfortable proof margin

There is no useful free margin hidden in `X`.

A moderate shift to `X~7.5` is safe for the slow detector but gains only about

```math
O(1.5\times10^{-3}\alpha),
```

which is insufficient to absorb the old `0.002 alpha` continuum allowance.

Pushing near `X~7.7` can gain roughly

```math
O(2\times10^{-3}\alpha),
```

but then the slow detector itself is close to its feasibility boundary.

Therefore the strategy

```text
move X until the old grid allowance becomes irrelevant
```

simply trades the fast continuum knife-edge for a slow decision-time knife-edge.

**NEGATIVE RESULT:** witness-time redesign alone is not a robust substitute for understanding the finite-grid-to-continuum error.

---

## 7. First nontrivial consequence

The most productive next step is now unambiguous:

```math
\boxed{\text{attack the timing-grid bias directly.}}
```

A small witness adjustment may later be useful once the continuum-bias scale is known, but there is no evidence that retuning `X` can remove the need for a discretization bound.

The continuum problem is also more structured after Steps 42–44 than it was in Step 34. The statistic is duration-truncated at `L0=.02`, and Step 43 already controls genuinely short successful clusters analytically. The grid error therefore comes from:

1. missed between-sample level-`u` maxima inside otherwise long lower-level components;
2. interpolation error in the lower-level component duration `L` for `L>=.02`.

Those two errors can be bounded separately instead of retaining the old undifferentiated `0.002 alpha` allowance.

---

## 8. Qualifications

- The paired `X` scans are numerical Monte Carlo diagnostics, not formal confidence statements.
- The slow values are numerical cluster-moment estimates, not rigorous lower-confidence bounds.
- Timing spacing in the witness scan is about `.0015`, chosen for efficient paired comparison; Step 44's certificate used about `.001`.
- No claim is made that `X=7.16` is mathematically optimal; only that moving toward the slow boundary does not create a robustly larger proof margin.
- No claim for other task parameters.

---

## 9. Stopping point

Witness-time tuning cannot comfortably absorb the existing continuum uncertainty before the slow detector approaches feasibility. The next logical target is a direct continuum discretization bound for the `L0=.02` duration-truncated fast cluster estimator.

### Single natural next question

> Can the finite-grid error be decomposed into a missed-between-sample-success term and a long-component duration-interpolation term, and can each be bounded sharply enough to replace the old undifferentiated `0.002 alpha` allowance?
