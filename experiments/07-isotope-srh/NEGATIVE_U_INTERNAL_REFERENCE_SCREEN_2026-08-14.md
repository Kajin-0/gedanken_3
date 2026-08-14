# Negative-U internal-reference screen

**Date:** 2026-08-14  
**Status:** CONDITIONAL BONUS OBSERVABLE / DOES NOT REPLACE NATURAL-Hg PILOT

## Idea

If one mercury vacancy could be driven through two sequential electron captures

```text
V0 --a=C1*n--> V- --b=C2*n--> V2-
```

then the unknown minority-electron density `n` multiplies both rates. The ratio

```math
r=b/a=C2/C1
```

is therefore independent of the common carrier-density scale.

Starting from `P0(0)=1`,

```math
P0=e^{-at},
```

```math
P1=\frac{a}{b-a}(e^{-at}-e^{-bt}),
```

and the mean number of captured electrons is

```math
\boxed{
\bar N_e(t)
=2-\frac{2b-a}{b-a}e^{-at}
+\frac{a}{b-a}e^{-bt}.
}
```

For `a=b`,

```math
\bar N_e=2-(2+at)e^{-at}.
```

Thus a common change in `n` shifts the transient horizontally, while a change in `C2/C1` changes its shape.

## Exact degeneracies / bad regimes

The shape is not always informative.

For

```math
r=b/a=1/2,
```

the first exponential cancels exactly and

```math
\boxed{\bar N_e/2=1-e^{-(a/2)t}.}
```

The nominal two-step process is therefore exactly indistinguishable from a single exponential in the mean-charge transient.

As `r -> infinity`, the second capture becomes effectively instantaneous after the first; the intermediate state has negligible occupancy and the transient again approaches a single exponential.

This is especially relevant to a negative-U defect because thermodynamic stabilization of the doubly occupied state can make the intermediate one-electron state difficult to observe. Negative-U DLTS in other semiconductors shows that short filling pulses / low-temperature preparation can sometimes expose the hidden first acceptor transition, but this must not be assumed for HgCdTe.

## Optimistic Fisher screen

Companion script: `numerics/negative_u_two_capture_identifiability.py`.

Assumptions:

- 25 filling times spanning `a*t=0.01...100`;
- independent 0.5% RMS noise per normalized point;
- unknown baseline, saturation amplitude, and common time scale `a`;
- the sequential two-capture model is assumed correct.

Representative one-sweep precision on `ln(r)`:

```text
r=b/a     sigma_ln(r)     RMS departure from best single exponential
0.05        0.0266                   6.85%
0.10        0.0260                   4.84%
0.20        0.0295                   2.54%
0.30        0.0341                   1.30%
0.50        0.0456                   0.00%   [exact single-exponential shape]
0.80        0.0705                   0.85%
1.0         0.0944                   1.13%
2.0         0.2767                   1.49%
3.0         0.1947                   1.42%
5.0         0.1469                   1.17%
10          0.1580                   0.74%
20          0.2307                   0.39%
50          0.5347                   0.12%
```

For a 2% isotope-induced change in `r`, a 5-sigma measurement under these optimistic assumptions requires only tens of repeated sweeps for `r << 1`, but roughly `10^3` or more sweeps over much of the `r > 1` range. Systematic transient-shape errors would dominate before such averaging became useful.

The important qualitative result is therefore:

```text
slow second capture (r << 1): intermediate occupancy visible -> ratio potentially useful
fast second capture (r >> 1): intermediate occupancy suppressed -> internal ratio poorly useful
```

## HgCdTe charge-state correction

Do not assume that the detector-relevant SRH cycle necessarily traverses `V0 -> V- -> V2-` by two successive electron captures.

Hg vacancies are double acceptors with neutral, singly charged, and doubly charged states. Modern narrow-gap HgCdTe capture theory treats electron capture by vacancy acceptor states and finds electron capture to be slower than hole capture, governing the SRH rate. The 2025 calculation explicitly presents electron-capture results for a singly charged double acceptor `A2^-1`.

The experimentally established negative-U state ordering shows that the intermediate vacancy state can be hidden in thermal measurements and photogenerated in optical measurements. This establishes that two charge transitions exist, but not that both electron-capture rates are simultaneously observable in the same p-type SRH operating cycle.

Therefore the two-electron internal-reference concept is an **optional spectroscopy experiment**, not the baseline way to remove the `C_n n_fill` degeneracy.

## Prior-art boundary

Established and not novel:

- negative-U defects and sequential two-electron charge transitions;
- short-pulse / Laplace-DLTS recovery of hidden first acceptor transitions in negative-U defects (e.g. carbon vacancies in 4H-SiC);
- Hg-vacancy negative-U behavior and two acceptor levels in HgCdTe.

Experiment 07 does not claim the two-step transient theory as new.

## Current disposition

```text
same-defect two-rate ratio as universal self-calibration: REJECT
same-defect two-rate ratio if experimentally resolved: RETAIN AS BONUS
arbitrary second electron trap as internal reference: RETAIN IF PRESENT AND CHARACTERIZED
10-pair natural-Hg sister pilot: REMAINS BASELINE GATE
custom injection-DLTS architecture: FALLBACK ONLY
```

## Natural-Hg pilot addition

Before isotope procurement, the natural-Hg pilot should explicitly search for multi-rate electron filling:

1. acquire normalized filling curves over at least 3-4 decades of pulse duration;
2. test single-exponential, distributed-profile, and sequential two-capture fits;
3. vary filling bias and temperature;
4. if a stable density-independent two-rate shape is found, evaluate it as an internal reference;
5. if not, do not force the negative-U interpretation; retain the external minority-density calibration gate.

The internal-reference route replaces the existing pilot only after an actual narrow-gap HgCdTe transient demonstrates that the required second rate is observable.
