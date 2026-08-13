# Agent recovery entrypoint

Read [`AGENTS.md`](AGENTS.md) first for scientific-integrity rules.

## Current research disposition

### Experiment 02 — CLOSED as the default publication/device-optimization path

`experiments/02-isochronous-avalanche-photodetector/`

Read first:

1. `experiments/02-isochronous-avalanche-photodetector/00_ACTIVE_FRONTIER_EXPERIMENT02_STOP_2026-08-13.md`
2. `experiments/02-isochronous-avalanche-photodetector/FIXED_DEPTH_WAVEGUIDE_DOMINANCE_STOP_2026-08-13.md`
3. `experiments/02-isochronous-avalanche-photodetector/READOUT_SIDE_INFORMATION_NO_GO_2026-08-13.md`
4. `experiments/02-isochronous-avalanche-photodetector/COMMON_OUTPUT_ARCHITECTURE_RESULT_2026-08-13.md`
5. `experiments/02-isochronous-avalanche-photodetector/CONTINUOUS_COMMON_JUNCTION_GEOMETRY_2026-08-13.md`
6. `experiments/02-isochronous-avalanche-photodetector/THREE_STATE_COUPLED_MODE_SURROGATE_2026-08-13.md`
7. `experiments/02-isochronous-avalanche-photodetector/DISCRETE_DEPTH_LADDER_2026-08-13.md`
8. `experiments/02-isochronous-avalanche-photodetector/REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md`
9. `experiments/02-isochronous-avalanche-photodetector/OPTIMAL_DELAY_MAP.md`

## What remains valid

For absorption coordinate `X`,

```math
Var(T)=Var[m(X)]+E[Var(T|X)],
```

with

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

The position-dependent conditional-mean term vanishes when

```math
m(X)=constant.
```

For a Maxwell-derived joint absorption distribution, the optimum deterministic delay map is

```math
d_opt(x)=C-E[t_c(Z)|X=x]
```

with other position-dependent mean delays included as required.

The finite ladder, forward/reverse controls, reduced-order Monte Carlo, and correction that geometric isochrony need not coincide with minimum total RMS remain valid **conditional analyses**.

## Why Experiment 02 stopped

Once the device architecture admitted waveguide absorption and distributed/common electrical readout, a stronger established comparator became unavoidable:

```text
fixed shallow absorption depth
+ longitudinal waveguide absorption
+ optional ordinary traveling-wave optical/electrical velocity matching.
```

This separates the two problems instead of correlating them. Waveguide APDs already use propagation along the optical guide to obtain high responsivity while keeping carrier transit thickness small; traveling-wave photodetectors/APDs already treat the remaining longitudinal velocity mismatch.

On the existing reduced-order benchmark, one fixed 200-nm absorber adjacent to the multiplication side gives approximately

```text
5.74 ps RMS at 40-um absorption length
```

under the same Pe=100, 5-ps avalanche, 2-ps electronics, and 1-ps optical assumptions, compared with approximately

```text
8.37 ps RMS
```

for the optimized three-state transverse-depth ladder.

Without any electrical velocity matching, that fixed-depth comparator still clears the historical 30% gate until the optical absorption length reaches roughly `1.98 mm`.

Therefore the migrating depth map adds transfer-fidelity and/or heterointerface complexity without establishing a timing advantage over the strong comparator.

Do not rescue the path by adding five/six depth states or by beginning full Maxwell/TCAD optimization.

## Reopen conditions

Only reopen Experiment 02 if a physically motivated constraint defeats the fixed-depth waveguide comparator, e.g. mandatory thick absorber volume for a non-efficiency resource, necessarily multi-millimeter absorption with unavailable electrical velocity matching, or a material system where fixed-depth localization is intrinsically impossible but depth migration is practical.

Novelty and priority remain unestablished. Do not draft a paper from Experiment 02.

### Experiment 01 — also closed publication path

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 remains **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. Its theorem is mathematically valid, but the unknown-arrival mechanism and optimum-filter information-spectrum formulation reduce to established theory. Do not reopen Step 13–49 or manuscript polishing.

## Next research rule

Start the next photodetector gedanken experiment from a microscopic/device-physics premise. Before building a large derivation chain, identify the strongest established architecture/control that could make the proposed mechanism unnecessary. If that comparator wins, document the stop early rather than engineering around it.
