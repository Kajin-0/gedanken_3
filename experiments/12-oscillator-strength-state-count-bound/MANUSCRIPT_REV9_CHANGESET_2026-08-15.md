# Experiment 12 — PRB Rev9 changeset

**Date:** 2026-08-15

Rev9 is a surgical response to the supplied extreme adversarial review of Rev8. The central finite-volume theorem is unchanged.

## Changes from Rev8

1. Qualified the intrinsic-neutral corollary: `n_e=n_h=n_th` is asserted only when `mu` lies in a gap and the cross-`mu` partition coincides with valence/conduction manifolds.
2. The realistic HgCdTe example explicitly uses the general cross-`mu` hierarchy because its charge-neutral `mu` lies 11.477 meV above the nominal Gamma6 edge.
3. Renamed the numerical HgCdTe denominator from `exact` to `reference` / `numerically converged reference`.
4. Added explicit formulas for the cross-`mu` reference population and thermally weighted direct-transition sum.
5. Added the bulk specialization of the theorem capacity as an essential supremum of largest singular values of full projected velocity blocks.
6. Stated quadrature and degeneracy-grouping conventions.
7. Added a numerical diagnostic showing the SVD capacity is `1.015611e6 m/s`, while the largest pairwise matrix element is only `0.868123e6 m/s`; pairwise substitution would overstate the population lower bound by 36.9%.
8. Added selected-window maximum momentum to the HgCdTe validation table: 0.149, 0.240, 0.415, and 0.583 nm^-1.
9. Added branch-selection diagnostic: the broad selected set contains Gamma8-derived -> Gamma6-derived transitions; the Gamma7-derived split-off pair does not enter.
10. Added degeneracy-clustering-tolerance robustness (`1e-10` to `1e-5 eV`, unchanged capacity to reported precision at fixed quadrature).
11. Reframed the abstract to report the realistic bound/reference range `0.032 -> 0.118` and call 0.5 eV a broad direct-transition validation window.
12. Added the physical interpretation that the capacity remains nearly constant across the realistic windows, so the improved bound comes predominantly from accumulated cross-mu spectral weight.
13. Appendix A now explicitly invokes the intrinsic-gap corollary before converting to an intrinsic electron column.

## Local QA-passed artifacts

```text
experiment12_prb_rev9.tex
SHA-256 da4d929d77d817e48c6661d61ffcdcaac82a8503b9594a8dafcca27e838c0f7b

experiment12_prb_rev9.pdf
SHA-256 849e0653b6007c35a92967e812ab584ede70914714c2315bf849839701232e0b

kane_8band_tightness_rev9.py
SHA-256 5b26fa0a1da8bebaf8a225313e21474f4a74a698ce0180ae26ba35d55dd2b28b
```

The repository's `numerics/kane_8band_tightness.py` has been updated to include the Rev9 projected-block, pairwise, momentum-support, and degeneracy-tolerance diagnostics.

## Disposition

```text
REV9 SCIENCE: READY FOR ANOTHER HOSTILE REVIEW
CENTRAL THEOREM: UNCHANGED
NO NEW DETECTOR-PERFORMANCE CLAIMS
NOVELTY: NOT ESTABLISHED
```