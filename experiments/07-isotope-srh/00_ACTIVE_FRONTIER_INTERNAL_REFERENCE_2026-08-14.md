# Experiment 07 active frontier — internal reference

**Date:** 2026-08-14

Read `NEGATIVE_U_INTERNAL_REFERENCE_SCREEN_2026-08-14.md` and `NATURAL_HG_PILOT_GATE_2026-08-14.md` first.

The unresolved metrology problem is the exact degeneracy

```math
q_{fit}=(C_{n,B}/C_{n,A})(n_B/n_A).
```

A second resolved electron capture rate in the same depletion region would cancel the common minority-density scale. For two traps,

```math
D_{ij}=\ln[(\lambda_i/\lambda_j)_B/(\lambda_i/\lambda_j)_A]
=\Delta_I\ln C_i-\Delta_I\ln C_j.
```

A more ambitious same-defect version uses two sequential electron captures of a negative-U double acceptor. The mean captured charge is

```math
\bar N_e(t)=2-\frac{2b-a}{b-a}e^{-at}+\frac{a}{b-a}e^{-bt},
```

with `a=C1*n`, `b=C2*n`; its shape depends on `b/a=C2/C1` and is density-independent.

However this is **conditional only**:

- Hg vacancies are negative-U double acceptors and the intermediate charge state can be hidden in thermal measurements.
- Short-pulse/Laplace-DLTS can reveal hidden first acceptor transitions in other negative-U defects, proving feasibility in principle but not in HgCdTe.
- The sequential transient is exactly a single exponential for `b/a=1/2` and approaches a single exponential for `b/a >> 1`.
- The detector-relevant Hg-vacancy SRH calculation does not establish that the operating cycle traverses both electron-capture transitions in a way that makes both rates observable.

Therefore:

```text
same-defect two-rate self-calibration: CONDITIONAL BONUS, NOT BASELINE
arbitrary co-located electron reference trap: useful if naturally resolved
10-pair natural-Hg sister pilot: remains next physical gate
custom injection-DLTS: fallback only
```

The natural-Hg pilot must add an explicit multi-rate search: filling curves over 3-4 decades, several fill biases and temperatures, with single-rate, distributed-profile and sequential two-rate comparisons. If a stable density-independent second electron rate is actually observed, promote the internal reference. If not, continue with external minority-density calibration and do not force a negative-U interpretation.

No isotope procurement and no paper drafting yet.
