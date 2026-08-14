# Natural-Hg pilot — transient discrimination matrix

**Date:** 2026-08-14  
**Status:** PILOT DESIGN / NO ISOTOPE PROCUREMENT

## Exact model ambiguity

For sequential captures `a=C1*n`, `b=C2*n`, `r=b/a`, the normalized unfilled charge is

```math
U(t)=1-\bar N_e(t)/2
=c_1e^{-at}+c_2e^{-bt},
```

with

```math
c_1=\frac{2r-1}{2(r-1)},
\qquad
c_2=-\frac{1}{2(r-1)}.
```

For

```math
\boxed{r<1/2}
```

both coefficients are positive and sum to one. The sequential two-capture transient is therefore **exactly identical** to a positive mixture of two independent one-step capture populations. Mean filling data alone cannot distinguish those mechanisms.

At `r=1/2`, `c1=0` and the transient is exactly single exponential.

For `r>1/2`, one coefficient is negative, so the ideal sequential transient lies outside the positive-mixture family and is distinguishable in principle. The distinguishing shape becomes weak again for `r >> 1` as the second capture becomes effectively instantaneous.

This is a structural identifiability result, not an SNR result.

## Numerical scale

With normalized ideal data sampled over four decades in pulse duration, the best positive-mixture fit has zero residual for `r<1/2` by exact algebra. For `r>1/2`, representative RMS departures are approximately:

```text
r       RMS departure from best positive mixture
0.51       0.05%
0.55       0.25%
0.60       0.45%
0.80       1.04%
1          1.39%
2          1.90%
5          1.67%
10         1.23%
20         0.81%
50         0.42%
100        0.24%
```

These values are an optimistic reduced-order guide. Real distributed electrostatics, overlapping traps and pulse distortion increase model flexibility and reduce discriminating power.

## Interpretation rule

A resolved second rate can still be useful as an internal density reference even if the mean curve cannot prove that it is the second charge transition of the same Hg vacancy. But it must be a physically stable rate, not an arbitrary component of a distributed profile.

Promote a second rate to an internal reference only if:

1. it is reproducible across sister devices;
2. its ratio to the target rate is stable across filling biases while the common time scale changes;
3. it persists over temperature in a way consistent with a discrete trap transition;
4. emission DLTS / Laplace-DLTS or another independent spectrum assigns the target and reference transitions;
5. a continuum/distributed-profile model is not equally adequate without stable discrete rates.

Do not claim a same-defect negative-U sequence from mean filling shape alone.

## Pilot acquisition matrix

### Stage A — scouting

Use 1-2 devices to locate the electron-capture window.

- Sweep filling-pulse duration over as wide a logarithmic range as the instrument permits, initially targeting at least 5-6 decades.
- Locate the main transition region and any shoulder/plateau.
- Choose the final pulse window so it spans at least `~0.01` to `~100` times the dominant fitted capture time when practical.

### Stage B — paired natural-Hg pilot

Use the previously defined ~10 independent adjacent sister pairs, with roughly 3-5 devices per coupon.

For every analytical device:

- at least 25 logarithmically spaced fill durations across ~4 decades around the dominant capture transition;
- at least 3 filling conditions/biases chosen empirically so the common filling time changes by factors of order several;
- at least 3 temperatures in the usable electron-capture/emission window after the actual trap is located;
- repeated full sweeps sufficient to make random transient noise smaller than the pair-level systematic target.

The filling biases need not correspond to accurately known minority density during this pilot. Their purpose is to test whether candidate rate ratios remain invariant while the common rate scale changes.

## Model hierarchy

Fit all data with increasing physical complexity:

```text
M0: one effective capture rate
M1: positive mixture / distributed one-step capture
M2: two discrete positive trap populations with shared bias scaling
M3: sequential two-capture negative-U model
```

Do not promote `M3` merely because it lowers residuals. Require stable parameters across bias and temperature and compare against `M1/M2`.

For a genuine common-density pair of discrete capture processes,

```math
\lambda_i=C_i n,
\qquad
\lambda_j=C_j n,
```

so

```math
\lambda_i/\lambda_j=C_i/C_j
```

should remain invariant when the fill strength changes.

## Pilot decision tree

```text
A. No stable second rate:
   keep original q_fit = (Cn,B/Cn,A)(nB/nA) problem;
   use external density correction / pair-floor gate.

B. Stable second rate, but no physical assignment:
   use it as a diagnostic of electrostatic reproducibility only;
   do not use it to claim isotope-dependent V_Hg capture.

C. Stable discrete reference + target V_Hg assignment:
   use isotope double ratio to cancel common n_fill;
   this materially strengthens Experiment 07.

D. Stable same-defect negative-U sequential signature independently established:
   use C2/C1 shape ratio as an additional density-independent closure;
   this is a bonus, not required for the experiment.
```

## Current bottom line

The natural-Hg pilot now tests both the original pair reproducibility and whether the material provides its own internal density reference. It remains the correct next physical gate before enriched Hg is purchased.
