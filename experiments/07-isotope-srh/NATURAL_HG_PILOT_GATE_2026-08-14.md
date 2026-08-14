# Natural-Hg pilot gate before isotope procurement

**Date:** 2026-08-14
**Status:** CHEAP PRE-ISOTOPE FALSIFICATION EXPERIMENT DEFINED / 10-PAIR FIRST PILOT RECOMMENDED / MINORITY-DENSITY SYSTEMATIC REMAINS HARD GATE

## 1. Purpose

Experiment 07 now predicts a plausible Hg-only electron-capture contrast of order 1-5% only if the target mercury-vacancy electron transition lies sufficiently close to a one-optical-phonon condition. Before buying enriched Hg or building a custom injection structure, measure how large a false isotope-like capture shift appears in ordinary natural-Hg material processed in the exact proposed way.

This pilot tests the metrology and fabrication floor without isotope cost or isotope-physics interpretation.

## 2. Sister-pair design

Use adjacent/interleaved coupons from one wafer. All coupons receive the same natural-Hg anneal and then the same randomized common MIS/junction fabrication batch.

Artificially label one member of each adjacent pair A and the other B, blinded during fitting.

For each device:
- identify the same electron trap;
- measure normalized filling curves over at least 8-10 pulse durations around the capture time;
- repeat at several filling biases;
- fit the horizontal registration factor `q_fit` exactly as planned for the isotope experiment;
- record C-V/Hall/Eg and any available injection-current monitor.

Multiple devices on one coupon estimate within-coupon fabrication/readout scatter. The independent replicate is the coupon pair.

## 3. Random-effects quantity of interest

For pair `j` and filling bias `b`, define

`r_jb = ln(q_fit,jb)`.

Organize it as

`r_jb = a_j + c_jb + epsilon_jb`.

Interpretation:
- `a_j`: dangerous pair-specific common multiplicative shift; this is indistinguishable from an isotope `C_n` effect if it occurs in the real experiment;
- `c_jb`: bias-dependent mismatch from changing electrostatic/profile shape;
- `epsilon_jb`: repeat/device fit noise.

The primary pilot output is the RMS of `a_j` after all corrections, not merely the pooled transient-fit precision.

## 4. Confidence gate

If `s_obs` is the observed RMS of the independent pair-level common shifts from `N` pairs, then for a normal random-effects planning model the one-sided 95% upper confidence bound on the true pair scatter is

`sigma_pair,95 = s_obs sqrt[(N-1)/chi2_(0.05,N-1)]`.

For a hoped-for 2% isotope effect, allocate about one quarter of that signal to the common density/fabrication systematic:

`target sigma_pair,95 < 0.5%`.

Minimum pair counts needed to establish that bound are approximately:

```text
observed pair RMS 0.20% -> 5 pairs
0.30% -> 10 pairs
0.35% -> 17 pairs
0.40% -> 36 pairs
```

If the observed scatter itself is >=0.5%, no finite amount of replication can establish a true RMS below 0.5% without changing the process; the experiment needs a better common-mode calibration or a larger predicted isotope signal.

Companion: `numerics/natural_hg_pilot_gate.py`.

## 5. Recommended first pilot

Start with **10 adjacent natural-Hg sister pairs**.

A practical device nesting target is roughly 3-5 nominally identical capacitors/junctions per coupon, but these devices are not independent material replicates.

At N=10:

```text
observed pair RMS 0.20% -> 95% upper sigma ~0.329%
0.30% -> ~0.494%
0.40% -> ~0.658%
0.50% -> ~0.823%
1.00% -> ~1.645%
```

Thus a 10-pair pilot sharply distinguishes a genuinely sub-percent process from a percent-scale one.

## 6. Bias-invariance gate

A false `q_fit` caused by a nonuniform filling-profile change should generally depend on filling bias/depletion geometry, whereas a microscopic multiplicative `C_n` change should produce the same horizontal scale factor for every bias that addresses the same trap and carrier-energy distribution.

Therefore require:

`q_fit(b1) ~= q_fit(b2) ~= q_fit(b3)`

within the target systematic budget.

This does not remove a pure uniform carrier-density rescaling, which remains exactly degenerate with `C_n`. It only detects the profile-shape component.

## 7. Common-density gate

The pilot must also test whether available C-V/Hall/Eg/current corrections reduce the residual common change in effective minority electron density below about 0.5% for a 2% target signal.

If they do not, there are only two credible rescues:

1. identify a second co-located electron trap that provides an internal density reference;
2. build an injection-DLTS-style controlled minority-carrier structure.

Do not respond by averaging more devices: a common carrier-density bias is systematic.

## 8. Cheap decision tree

```text
10-pair natural-Hg pilot:

pair RMS <=~0.3% and bias-invariant q_fit:
    PASS metrology floor; isotope experiment remains credible.

pair RMS ~0.3-0.5%:
    marginal; improve density correction and/or increase pairs.

pair RMS ~0.5-1%:
    a 5% isotope effect may remain testable, 1-2% effect is weak.

pair RMS >~1%:
    STOP isotope procurement unless an internal reference or controlled-injection method removes the common scale.
```

## 9. Scientific value of a null pilot

Failure of this pilot is useful. It means the current Hg-isotope hypothesis cannot be tested cleanly with ordinary post-anneal sister-device DLTS at the predicted contrast. That should close the practical Experiment-07 route rather than motivate increasingly elaborate fitting.

Novelty remains unestablished. No manuscript construction.
