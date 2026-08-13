# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `agent/noise-coupling-study`  
**Active experiment:** `experiments/02-isochronous-avalanche-photodetector/`

Read first:

1. `experiments/02-isochronous-avalanche-photodetector/CURRENT_STATE.md`
2. `experiments/02-isochronous-avalanche-photodetector/PROGRESS_LOG.md`
3. `experiments/02-isochronous-avalanche-photodetector/REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md`
4. `experiments/02-isochronous-avalanche-photodetector/OPTIMAL_DELAY_MAP.md`
5. `experiments/02-isochronous-avalanche-photodetector/RESIDUAL_JITTER_FLOOR.md`
6. `experiments/02-isochronous-avalanche-photodetector/DIMENSIONLESS_FEASIBILITY_BOUND.md`
7. `experiments/02-isochronous-avalanche-photodetector/PRIOR_ART_AUDIT_2026-08-13.md`

Before material writes, fetch the live target and exact blob SHA. Preserve failed and corrected paths. Update `CURRENT_STATE.md`, `PROGRESS_LOG.md`, `agent.md`, and this file when the research frontier changes.

Do not use novelty or priority language without a dedicated prior-art audit.

## Experiment 02 — controlling result

For absorption coordinate `X`,

```math
Var(T)=Var[m(X)]+E[Var(T|X)],
```

where

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

The target is to make the position-dependent conditional mean constant. For a joint absorption distribution `p(x,z)`, the optimum deterministic optical delay is

```math
d_opt(x)=C-E[t_c(Z)|X=x]
```

with other position-dependent mean delays included when required.

The active hypothesis is specifically **transverse absorption-depth compensation**, not ordinary longitudinal traveling-wave velocity matching.

### First reduced-order device surrogate

Current scale:

```text
d=2 um
v0=5e4 m/s
vg=7.5e7 m/s
T0=40 ps
L=3 mm
Pe=100
local depth RMS=100 nm
avalanche RMS=5 ps
electronics RMS=2 ps
optical RMS=1 ps
```

Results:

```text
direct control       12.645 ps RMS
forward matched       7.460 ps RMS
decorrelated control 16.253 ps RMS
reverse anti-match   21.741 ps RMS
```

A one-million-event first-passage Monte Carlo reproduces these values. The forward/direct reduction is about `41.0%`, so this reduced-order parameter point passes the selected 20–30% feasibility gate.

At the same auxiliary assumptions, the 30% gate allows avalanche RMS up to about `8.34 ps` at `Pe=100`; `Pe=20` cannot reach 30% even with zero avalanche jitter.

### Important correction

Do not claim that the minimum total jitter must occur exactly at the geometric mean-delay match. In the present reduced-order velocity sweep, exact mean-delay cancellation is at `v/v0=1`, while the total-jitter minimum shifts to about `v/v0=1.2815` because residual transport variance also changes with drift speed.

The stronger causal signature is the forward/reverse asymmetry.

### Next step

Construct a finite **discrete optical-depth ladder** approximating the continuous optimal delay map. Determine the minimum number of localized absorbing sections and the depth/delay tolerances required to retain the 20–30% improvement and forward/reverse signature.

Do not begin manuscript construction yet. Novelty remains unestablished.

## Experiment 01 — closed publication path

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 is **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. The theorem remains mathematically valid, but the unknown-arrival mechanism and optimum-filter information-spectrum formulation reduce to established theory.

Do not reopen the Step-13–49 proof chain or manuscript polishing. Do not present `|R|^2/S_n`, `1/NEP^2`, RMS/effective timing bandwidth, or the unknown-arrival timing-cell penalty as new metrics.
