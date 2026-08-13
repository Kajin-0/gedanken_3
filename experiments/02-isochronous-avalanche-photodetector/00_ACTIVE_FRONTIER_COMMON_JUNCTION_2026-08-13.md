# Active frontier — continuous common-junction isochronous APD

**Date:** 2026-08-13

Read first:

1. `READOUT_SIDE_INFORMATION_NO_GO_2026-08-13.md`
2. `COMMON_OUTPUT_ARCHITECTURE_RESULT_2026-08-13.md`
3. `LINEAR_MODE_IMPULSE_RESPONSE_TEST_2026-08-13.md`
4. `CONTINUOUS_COMMON_JUNCTION_GEOMETRY_2026-08-13.md`
5. `THREE_STATE_COUPLED_MODE_SURROGATE_2026-08-13.md`
6. `DISCRETE_DEPTH_LADDER_2026-08-13.md`

## Latest disposition

**Negative result:** if detector section identity is available anywhere in section-specific electrical paths, calibrated electrical delays can remove the same section-dependent mean timing as the finite passive optical ladder. This remains true even if the branches are merged to one external output afterward.

Therefore independent segmented SPADs are rejected as the primary demonstration. A segmented-and-calibrated detector is now a required control, not a weak baseline.

The leading architecture is a **continuous/common electrical avalanche detector with distributed/traveling-wave readout**, so the transverse absorption coordinate is not separately exposed as an electrical timing label.

At the current N=3 surrogate, the historical 30% timing-improvement gate leaves about `3.51 ps RMS` total readout budget after the retained physical transport/avalanche terms. Exact near-end traveling-wave matching can shorten the former 3-mm optical-only device to `1.5-2.4 mm` for `ve/vg=1-4` while retaining the same forward depth-quantization term.

The integrated forward/reverse contrast is smaller when electrical propagation supplies part of the compensating delay; the old `2T0` reverse span applies only in the optical-delay-dominated limit.

A linear-mode short-pulse APD impulse response obeys the same law-of-total-variance timing decomposition as single-event timestamps. Therefore linear APD operation is the preferred first validation platform; Geiger quench/TDC complexity is deferred.

## Current constructive fork

Two one-junction optical implementations remain:

```text
A. uniform continuous absorber + optical field localized/migrated in depth
   advantage: clean carrier transport
   risk: difficult <=~100-175 nm absorption-depth localization

B. three thin absorbing sheets inside one continuous depleted junction
   advantage: easy narrow depth localization
   risk: heterointerface trapping / stochastic transfer delay
```

At current N=3 assumptions, a thin-sheet implementation has only a few-picosecond added interface-delay RMS budget (`~2.9 ps` if the local depth RMS is 100 nm) before the historical 30% gate is lost.

## Next hard step

Construct the simplest two competing Maxwell-to-transport cross-section surrogates:

1. uniform 2-um absorber with a vertically shifted/supermode-localized field;
2. three thin absorbing sheets with ideal grading, then add explicit interface-delay variance.

For each extract `p(x,z)`, conditional carrier mean/variance, forward/reverse normalized impulse-response variance, absorption efficiency, and the readout budget.

Kill either route if its realistic localization or transport penalty exceeds the already-derived timing surface.

Novelty and priority remain unestablished. Do not begin manuscript construction.