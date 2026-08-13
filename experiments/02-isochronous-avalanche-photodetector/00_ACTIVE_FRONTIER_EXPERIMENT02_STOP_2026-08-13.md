# Active frontier — Experiment 02 dominance stop

**Date:** 2026-08-13  
**Controlling result:** `FIXED_DEPTH_WAVEGUIDE_DOMINANCE_STOP_2026-08-13.md`

## Disposition

Experiment 02 is now **closed as the default publication/device-optimization path**.

The exact conditional-mean timing condition remains valid, but the current APD/SPAD implementation is dominated by a simpler strong comparator once waveguide geometry is allowed:

```text
fixed shallow absorption depth
+ longitudinal waveguide absorption
+ optional standard traveling-wave optical/electrical velocity matching.
```

On the existing reduced-order benchmark, a single fixed 200-nm absorber near the multiplication region gives about `5.74 ps RMS` for a 40-um optical length, versus about `8.37 ps RMS` for the optimized three-state transverse-depth ladder. It still clears the historical 30% gate without electrical velocity matching for lengths up to approximately `1.98 mm`.

The mapped architecture therefore adds state-transfer and/or heterointerface complexity without establishing a timing advantage over the strong waveguide comparator.

## Preserve

- `Var(T)=Var[m(X)]+E[Var(T|X)]`;
- `m(X)=constant` as the exact mean-delay cancellation condition;
- `d_opt(x)=C-E[t_c(Z)|X=x]` as the optimal deterministic delay map;
- forward/reverse derivations and finite-ladder mathematics as valid conditional analyses;
- the correction that geometric isochrony and minimum total RMS need not coincide.

## Do not continue by default

- no five/six-state optical rescue;
- no full Maxwell/TCAD optimization of the migrating depth map;
- no manuscript construction;
- no novelty or priority language.

## Reopen only if

A physically motivated constraint defeats the fixed-depth waveguide comparator, such as mandatory thick absorption volume for power/energy handling, unavailable electrical velocity matching with necessarily millimeter-scale absorption, or a material system where fixed-depth localization is intrinsically unavailable.

Otherwise start a new microscopic photodetector gedanken experiment and perform the same early strong-comparator/prior-art audit before building a manuscript.
