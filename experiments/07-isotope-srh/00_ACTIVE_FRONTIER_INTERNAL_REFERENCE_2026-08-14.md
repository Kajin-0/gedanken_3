# Experiment 07 active frontier — internal reference

**Date:** 2026-08-14

Read first:

1. `PILOT_TRANSIENT_DISCRIMINATION_2026-08-14.md`
2. `NEGATIVE_U_INTERNAL_REFERENCE_SCREEN_2026-08-14.md`
3. `NATURAL_HG_PILOT_GATE_2026-08-14.md`
4. `ELECTROSTATIC_DEGENERACY_AND_CALIBRATION_2026-08-14.md`

The unresolved metrology problem is

```math
q_{fit}=(C_{n,B}/C_{n,A})(n_B/n_A).
```

A second resolved electron-capture rate in the same filling population can cancel the common minority-density scale:

```math
D_{ij}=\ln[(\lambda_i/\lambda_j)_B/(\lambda_i/\lambda_j)_A]
=\Delta_I\ln C_i-\Delta_I\ln C_j.
```

A same-defect negative-U version is possible only conditionally. For sequential captures `a=C1*n`, `b=C2*n`, `r=b/a`,

```math
\bar N_e(t)=2-\frac{2b-a}{b-a}e^{-at}+\frac{a}{b-a}e^{-bt}.
```

The shape contains `C2/C1`, independent of `n`, but there is a stronger structural ambiguity:

```math
U(t)=1-\bar N_e/2=c_1e^{-at}+c_2e^{-bt}.
```

For `r<1/2`, both coefficients are positive. The sequential transient is therefore exactly identical to an ordinary positive mixture of two one-step capture populations. At `r=1/2` it is exactly single exponential. For `r>1/2` it is distinguishable from a positive mixture in principle, but the signature vanishes again as `r>>1`.

Thus **mean filling shape alone cannot establish a same-defect negative-U mechanism over a large part of parameter space**. A second rate is useful as an internal density reference only after bias/temperature stability plus independent trap assignment show that it is a real discrete capture process.

The detector-relevant Hg-vacancy SRH theory also does not establish that the operating recombination loop exposes both electron-capture transitions simultaneously. Do not equate the existence of two Hg-vacancy acceptor levels with two observable SRH electron filling rates.

Current disposition:

```text
same-defect two-rate self-calibration: CONDITIONAL BONUS, NOT BASELINE
co-located discrete electron reference trap: USE IF ACTUALLY RESOLVED/ASSIGNED
10-pair natural-Hg sister pilot: NEXT PHYSICAL GATE
custom injection-DLTS: FALLBACK ONLY
isotope procurement: NOT YET
paper drafting: DO NOT BEGIN
```

The natural-Hg pilot now has two jobs:

1. bound the false isotope-like pair shift to the existing ~0.3-0.5% target;
2. search over multi-decade fill times, several fill biases and temperatures for a physically stable second electron rate.

If no stable second rate is found, retain external minority-density calibration. Do not force a negative-U fit.
