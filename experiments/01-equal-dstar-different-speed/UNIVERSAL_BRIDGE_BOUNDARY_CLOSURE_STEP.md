# Step 31 — Universal-Crossover Bridge Through the Finite-r High-Band Boundary

**Date:** 2026-08-11 21:17 EDT  
**Status:** NUMERICAL CLOSURE / REFINEMENT / CONDITIONAL / OPEN. Step 30 reduced the difficult small-`chi` fast-channel finite-band correction to the canonical Brownian-minus-parabola crossover function `F(mu)`. This step inserts that bridge into the finite-`r` boundary surrogate, then calibrates only the residual finite-`u` offset against the existing exact Palm boundary points and the direct occupation-time rough endpoint. The resulting central bridge has one shallow maximum near `kappa_f~95` and is strictly decreasing on the sampled/densely interpolated interval `kappa_f>=100`, approaching `Lambda_infinity~0.90513` from above. For the original horizontal slice `Lambda=0.895`, this removes the last numerically plausible bounded high-band re-entrant pocket: the corrected boundary never approaches that slice after the validated lower crossing. This is a numerical closure for the stated calibration, not a theorem-level interval enclosure and not a global statement for all `Lambda` or detector models. No novelty claim.

---

## 1. Question

Steps 21–23 established that the old Rice second switch near `kappa_f~130` is not a continuous-Palm switch and that

```math
\Lambda_\times(\infty)\approx0.905\pm0.004.
```

Step 22 mapped the finite-band Palm boundary through `kappa_f=200`, while Step 30 supplied a reusable continuum bridge for the small-`chi` fast channel.

The remaining question is whether the high-band boundary can dip again below the old task slice

```math
\Lambda=0.895
```

and return to the rough endpoint, producing a bounded re-entrant slow-preferred pocket.

---

## 2. Finite-u tangent boundary with the universal fast bridge

Use the Step-26 finite-`u` tangent approximation for the admissible normalized search length,

```math
\ell_{tan}
=\frac{\alpha-Q(u)}
{(\sqrt b/\sqrt2)\,H\,\phi(u)}.
```

For the fast channel in the small-`chi` sector, replace the old fixed `C_H` approximation by the Step-30 crossover

```math
\boxed{
H_f(\chi_f,\zeta_f)
=H_{mix,f}(\chi_f)
-\chi_f^{2/3}\,\mathcal F(\mu_f),
}
```

with

```math
\mu_f=\sqrt2\,\zeta_f\chi_f^{1/3}.
```

For the slow channel, `mu_s` is already large throughout the high-band region, so the fixed-`chi` Bessel/paired correction from Steps 27–28 is used.

Solving the common-time equality

```math
\ell_f(X,\kappa_f)
=r\ell_s(X/r,r\kappa_f)
```

gives a **shape surrogate** for `Lambda_cross(kappa_f)`.

This tangent construction is not used as an absolute finite-`alpha` boundary because Step 23 already showed a percent-level finite-threshold offset between the tangent asymptotic and the exact occupation/Palm boundary.

---

## 3. Universal-bridge tangent shape

Representative values of the Step-30/26 coupled tangent surrogate are

```text
kappa_f      Lambda_tan
-----------------------
60           0.88255
80           0.88497
100          0.88604
130          0.88675
160          0.88702
200          0.88715
300          0.88714
500          0.88693
1000         0.88660
2000         0.88633
5000         0.88609
10000        0.88595
infinity      0.88564
```

The universal fast crossover removes the premature fixed-`chi` asymptotic approximation. The remaining absolute discrepancy is primarily the known finite-`u` rare-event correction.

---

## 4. Palm/occupation anchoring of the finite-u discrepancy

Use the existing Step-22 Palm anchors

```text
kappa_f      Lambda_Palm
------------------------
60           ~0.9098
100          ~0.9103
200          ~0.9099
```

and the Step-23 direct rough endpoint

```math
\Lambda_\infty^{occ}=0.90513
```

for the central bridge.

Define

```math
\delta(\kappa)
=\Lambda_{exact}(\kappa)-\Lambda_{tan}(\kappa).
```

The endpoint discrepancy is

```math
\delta_\infty
=0.90513-0.88564
=0.01949.
```

The Palm-minus-tangent discrepancies at `kappa=60,100,200` decrease smoothly toward this endpoint. A minimal two-parameter relaxation law

```math
\boxed{
\delta(\kappa)
=\delta_\infty+A\kappa^{-p}
}
```

fitted only to those three Palm anchors gives

```text
A ~= 0.18206
p ~= 0.77501.
```

This fit is deliberately low dimensional: it is used to transport the already known finite-`u` offset, not to manufacture high-band structure.

**DEFINED / CONDITIONAL:** this Palm-anchored relaxation is an empirical finite-threshold bridge. It is not a proof of the exact correction law.

---

## 5. Palm-anchored high-band boundary

Combining

```math
\Lambda_{bridge}(\kappa)
=\Lambda_{tan}(\kappa)+\delta(\kappa)
```

with monotone PCHIP interpolation of the tangent table gives

```text
kappa_f      Lambda_bridge
--------------------------
60           0.90966
80           0.91056
100          0.91066
130          0.91042
160          0.91008
200          0.90964
250          0.90916
300          0.90882
400          0.90829
500          0.90790
750          0.90730
1000         0.90695
2000         0.90632
5000         0.90583
10000        0.90559
infinity      0.90513
```

A dense logarithmic scan of the interpolated bridge gives a single shallow maximum at approximately

```math
\boxed{
\kappa_f\approx94.9,
\qquad
\Lambda_{max}\approx0.91068.
}
```

and

```math
\boxed{
\frac{d\Lambda_{bridge}}{d\kappa_f}<0
\quad\text{through the sampled/interpolated central bridge for }\kappa_f\ge100.
}
```

Thus the Step-22 Palm maximum near `kappa_f~60–100` connects naturally to the Step-23 rough endpoint without a second high-band minimum and recovery.

---

## 6. Consequence for the original `Lambda=0.895` slice

The central rough endpoint is

```math
\Lambda_\infty\approx0.90513,
```

which is already

```math
0.01013
```

above the old task slice.

Even using the previously reported `~0.004` rough-endpoint uncertainty as a conservative one-step downward allowance gives roughly

```math
0.90513-0.004\approx0.9011>0.895.
```

The Palm-anchored bridge is higher still at all finite high-band points.

Therefore, within the numerical model/calibration now assembled,

```math
\boxed{
\Lambda=0.895:
\quad
\text{no bounded high-band slow-preferred re-entrant pocket is supported.}
}
```

The surviving one-dimensional topology for that task remains

```text
slow preferred at low bandwidth
-> one Palm-corrected switch near kappa_f~21.7
-> fast preferred thereafter through the rough endpoint.
```

**NUMERICAL CLOSURE:** this statement combines direct Palm checks, the Palm boundary map, the continuum-extrapolated universal crossover, and the direct rough endpoint. It is stronger than isolated point checks but is not a rigorous interval theorem.

---

## 7. What this does and does not close

### Numerically closed for the stated calibration

- The Step-20 high-band Rice switch is not restored by the corrected fast-channel crossover.
- The high-band boundary has one shallow maximum near `kappa_f~100`, then decreases toward the rough endpoint.
- The original `Lambda=0.895` slice does not cross the boundary again.

### Still open

- a theorem-level finite-`alpha` interval enclosure for `Lambda_cross(kappa_f)`;
- proof that the empirical finite-`u` discrepancy law `delta_infinity+A kappa^-p` has the assumed monotone relaxation;
- exclusion of multiple extrema for other task parameters or other horizontal `Lambda` slices;
- a certified global maximum location for the finite-`r` boundary;
- publication-grade error bounds for `F(mu)`;
- hardware interpretation;
- novelty.

---

## 8. First nontrivial consequence

The remaining high-band ambiguity was not caused by the small-`chi` fast detector once its Brownian-parabola crossover is treated correctly.

After replacing the premature fixed-`chi` asymptotic with the universal `F(mu)` bridge and anchoring only the finite-threshold offset to exact Palm/occupation results, the boundary becomes a one-hump curve:

```text
rise -> shallow maximum near kappa_f~100 -> monotone high-band descent -> rough endpoint.
```

For the original task, the apparent Rice `slow -> fast -> slow` topology is therefore not merely unsupported at a few points; it is numerically closed across the full high-band bridge.

---

## 9. Stopping point

The bounded high-band re-entrant pocket is numerically eliminated for the original `r=2`, `Lambda=0.895` calibration. The remaining issue is whether the empirical finite-`u` anchoring can itself be replaced by a certified rare-event correction.

### Single natural next question

> Can the finite-`u` Palm/occupation discrepancy between the tangent bridge and the exact boundary be derived or bounded directly, replacing the empirical `delta_infinity+A kappa^{-p}` anchoring with a certified interval enclosure for `Lambda_cross(kappa_f)`?
