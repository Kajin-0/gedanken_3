# Experiment 12 — response to extreme adversarial re-review of Rev8

**Date:** 2026-08-15  
**Disposition:** **CENTRAL THEOREM UNCHANGED / TWO SUBSTANTIVE REVIEW ITEMS FIXED / REV9 CREATED**

## Review verdict received

The supplied review found no major defect in the central hierarchy and rated Rev8 minor-to-moderate revision before PRB submission. The two mandatory issues were:

1. the intrinsic `n_e=n_h=n_th` corollary was stated too generally once the realistic HgCdTe example placed `mu` inside the nominal conduction manifold;
2. the second-order HgCdTe calculation did not document sufficiently clearly that the numerical `v_B^cap` is the projected-block operator norm/singular value required by the theorem.

Additional requested refinements were numerical reproducibility, replacement of `exact` by `reference/model` for the truncated k.p calculation, more transparent abstract wording about the 0.5-eV window, and a selected-window k-range/branch diagnostic.

## Rev9 corrections

### Intrinsic-gap corollary domain

The manuscript now states that

```math
n_e=n_h=n_th
```

follows only for an intrinsic neutral semiconductor whose chemical potential lies in a gap so that the lower/upper-`mu` partition coincides with the valence/conduction manifolds. The general theorem remains Eq. (main) when `mu` lies inside a nominal band.

The HgCdTe example explicitly uses the general cross-`mu` hierarchy. Its numerically converged cross-`mu` reference population is

```text
1.005141e17 cm^-3
```

while conventional conduction-electron plus valence-hole counting gives

```text
1.010043e17 cm^-3,
```

a 0.485% difference.

### Projected-block capacity implemented exactly

The numerical script now documents and prints the actual capacity construction:

```text
for each k:
  diagonalize H(k);
  group exact model-degenerate energy eigenspaces;
  collect all opposite-side partner eigenspaces in the selected transition-energy window;
  construct the full projected velocity block;
  take its largest singular value;
maximize over shells and k.
```

Because the homogeneous bulk velocity operator conserves crystal momentum, the full operator is block diagonal in k, so the bulk specialization is

```math
v_B^cap = ess sup_{k,lambda} s_max[P_{lambda k} v_x(k) Q_{lambda k,B}],
```

including the analogous lower-shell blocks.

This is not a pairwise `max |v_cv|` approximation.

For the `Eg..0.5 eV` window:

```text
projected-block v_B^cap = 1.015611e6 m/s
largest individual |v_cv| = 0.868123e6 m/s
capacity / pairwise max = 1.169892
```

Using the pairwise maximum would under-estimate the denominator and overstate the population lower bound by 36.9%. Thus the distinction raised by the reviewer is numerically material, and the production calculation uses the correct theorem quantity.

### Degeneracy and k-domain diagnostics

At fixed quadrature, varying the degeneracy-clustering tolerance from `1e-10` to `1e-5 eV` leaves the broad-window capacity unchanged to reported precision.

Maximum selected momentum:

```text
Eg..1.5Eg : 0.149 nm^-1
Eg..2Eg   : 0.240 nm^-1
Eg..3Eg   : 0.415 nm^-1
Eg..0.5eV : 0.583 nm^-1
```

In the broad window, the selected transitions connect the four Gamma8-derived branches to the Gamma6-derived pair. The two Gamma7-derived split-off branches do not enter the selected set on the sampled domain.

### Reproducibility equations added

Rev9 now writes explicitly:

```math
n_mu^ref = sum_n int_K d^3k/(2pi)^3 [f_nk Theta(E_nk-mu)+(1-f_nk)Theta(mu-E_nk)]
```

and the direct thermally weighted transition sum used to form the bound, plus the projected-block singular-value capacity prescription.

The production quadrature is stated: Gauss-Legendre in `k` and `cos(theta)`, uniform azimuth, bounded k domains, and `1e-7 eV` degeneracy grouping.

### Terminology and presentation

The second-order k.p denominator is now `reference` / `numerically converged reference`, not `exact`. Table II uses `Bound/reference`.

The abstract reports the realistic-window range rather than advertising only 0.5 eV:

```text
0.032 for Eg..1.5Eg
through
0.118 for a broad direct-transition validation window through 0.5 eV.
```

The conclusion notes that `v_B^cap` changes very little across those windows; the increasing tightness is driven predominantly by accumulation of cross-mu spectral weight.

Appendix A explicitly invokes the intrinsic-gap corollary before interpreting the result as an intrinsic electron column.

## Scientific disposition

```text
CENTRAL THEOREM: UNCHANGED
REV8 COROLLARY DOMAIN DEFECT: FIXED
PROJECTED-BLOCK CAPACITY REPRODUCIBILITY: FIXED
REALISTIC HgCdTe BOUND/REFERENCE RATIOS: UNCHANGED
NOVELTY: NOT ESTABLISHED
```

Next step should be another hostile review of Rev9, not additional theory by default.