# Agent recovery entrypoint

Read [`AGENTS.md`](AGENTS.md) first for scientific-integrity rules.

## Active research frontier

`experiments/02-isochronous-avalanche-photodetector/`

Experiment 02 asks whether optical propagation delay can be deliberately correlated with **transverse photon absorption depth** so that optical delay cancels the depth-dependent carrier transit time to an APD/SPAD avalanche region.

Read in this order:

1. `experiments/02-isochronous-avalanche-photodetector/CURRENT_STATE.md`
2. `experiments/02-isochronous-avalanche-photodetector/PROGRESS_LOG.md`
3. `experiments/02-isochronous-avalanche-photodetector/REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md`
4. `experiments/02-isochronous-avalanche-photodetector/OPTIMAL_DELAY_MAP.md`
5. `experiments/02-isochronous-avalanche-photodetector/RESIDUAL_JITTER_FLOOR.md`
6. `experiments/02-isochronous-avalanche-photodetector/DIMENSIONLESS_FEASIBILITY_BOUND.md`
7. `experiments/02-isochronous-avalanche-photodetector/DIRECTION_REVERSAL_TEST.md`
8. `experiments/02-isochronous-avalanche-photodetector/FORWARD_REVERSE_ATTENUATION_BOUND.md`
9. `experiments/02-isochronous-avalanche-photodetector/DEPTH_MAPPING_IMPLEMENTATION.md`
10. `experiments/02-isochronous-avalanche-photodetector/REALISTIC_TARGET_INGAAS.md`
11. `experiments/02-isochronous-avalanche-photodetector/MULTIPLICATION_REGION_REQUIREMENT.md`
12. `experiments/02-isochronous-avalanche-photodetector/PRIOR_ART_AUDIT_2026-08-13.md`

## Current result

For absorption coordinate `X`, the exact depth-position timing decomposition is

```math
Var(T)=Var[m(X)]+E[Var(T|X)],
```

where

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

The targeted position-dependent mean term vanishes exactly when

```math
m(X)=constant.
```

For a Maxwell-derived joint absorption distribution `p(x,z)`, the optimum deterministic optical delay is

```math
\boxed{d_opt(x)=C-E[t_c(Z)|X=x]}
```

with electrical propagation and mean avalanche delay included in the conditional mean when necessary.

The hypothesis is **not** generic longitudinal traveling-wave velocity matching. It is specifically transverse absorption-depth compensation.

## First combined device surrogate

At the current InGaAs/InP scale

```text
d=2 um
v0=5e4 m/s
vg=7.5e7 m/s
T0=40 ps
L=3 mm
```

with

```text
Pe=100
sigma_perp=100 nm
avalanche RMS=5 ps
electronics RMS=2 ps
optical RMS=1 ps
```

the reduced-order analytic model predicts

```text
direct depth-sensitive control  12.645 ps RMS
forward matched                   7.460 ps RMS
decorrelated same-marginal       16.253 ps RMS
reverse anti-matched             21.741 ps RMS
```

A `N=1,000,000` first-passage Monte Carlo gives `12.650`, `7.464`, `16.265`, and `21.744 ps RMS`, respectively.

Thus the forward/direct reduction is about

```text
41.0%
```

and the first combined surrogate passes the selected 20–30% practical go gate in this restricted parameter region.

At the same local-depth/electronics/optical assumptions, the maximum avalanche RMS compatible with >=30% improvement is approximately

```text
Pe=30  -> 4.35 ps
Pe=50  -> 6.92 ps
Pe=75  -> 7.89 ps
Pe=100 -> 8.34 ps
Pe=200 -> 8.96 ps
```

`Pe=20` cannot reach 30% even with zero avalanche jitter.

## Important correction

Do not state that the **minimum total jitter** must occur exactly at the geometric isochronous bias.

The geometric condition nulls the position-dependent conditional-mean slope. Residual diffusion/local-depth variance can change with field, so the total variance minimum can shift.

For the current reduced-order model with locally fixed `D`, the exact mean-delay match is at

```text
v/v0=1
```

while the total-jitter minimum occurs at approximately

```text
v/v0=1.2815.
```

The strongest causal discriminator remains the predicted **forward/reverse timing asymmetry**, not the exact location of the RMS minimum.

## Current next step

Construct a finite **discrete optical-depth ladder** approximating

```math
d_opt(x)=C-E[t_c(Z)|X=x]
```

with a small number of depth-localized absorbing sections and explicit optical delay increments.

Determine:

1. minimum section count needed to retain most of the continuous-map benefit;
2. section-depth and delay-error tolerances;
3. whether the forward/reverse signature remains above the 20–30% gate.

Do not begin a paper before this constructive implementation test and continued prior-art checking.

## Experiment 01 — closed publication path

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 is **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. Its theorem is mathematically valid, but the unknown-arrival search mechanism and optimum-filter information-spectrum formulation reduce to established acquisition/optimum-filter theory.

Read `experiments/01-equal-dstar-different-speed/INFORMATION_SPECTRUM_STOP_2026-08-13.md` if Experiment 01 is revisited.

Do not reopen Step 13–49, Rev. 5 polishing, or attempts to rename RMS/effective bandwidth, `|R|^2/S_n`, `1/NEP^2`, or the timing-cell penalty as new metrics.

## Hard rules

- Novelty remains unestablished for Experiment 02; no priority language is authorized.
- Do not conflate transverse depth compensation with ordinary traveling-wave velocity matching.
- Do not claim zero-jitter detection; only one identifiable conditional-mean depth term is targeted.
- Preserve failed and corrected paths.
- Kill a device realization if realistic diffusion, absorption localization, avalanche buildup, or implementation error eliminates the material timing benefit.
- Never reference this research repository inside a publication manuscript.
