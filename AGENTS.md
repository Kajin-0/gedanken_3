# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active branch:** `agent/noise-coupling-study`

Before material writes, fetch the live target and exact blob SHA. Preserve failed, corrected, and negative paths. Do not use novelty or priority language without a dedicated prior-art audit.

## Read first

1. `agent.md`
2. `experiments/02-isochronous-avalanche-photodetector/00_ACTIVE_FRONTIER_EXPERIMENT02_STOP_2026-08-13.md`
3. `experiments/02-isochronous-avalanche-photodetector/FIXED_DEPTH_WAVEGUIDE_DOMINANCE_STOP_2026-08-13.md`
4. `experiments/01-equal-dstar-different-speed/INFORMATION_SPECTRUM_STOP_2026-08-13.md`

The older Experiment-02 `CURRENT_STATE.md` and `PROGRESS_LOG.md` preserve the derivation history but are superseded for frontier recovery by the dated stop pointer above.

## Experiment 02 — CLOSED default path

The exact timing decomposition remains valid:

```math
Var(T)=Var[m(X)]+E[Var(T|X)],
```

with

```math
m(X)=t_o(X)+t_c(X)+t_e(X)+\mu_a(X).
```

The position-dependent mean term vanishes for `m(X)=constant`, and the deterministic optimal delay map is

```math
d_opt(x)=C-E[t_c(Z)|X=x]
```

with other mean delays included as needed.

However, the proposed transverse absorption-depth migration is dominated for the present APD/SPAD timing objective once waveguide geometry is admitted. The strong comparator is:

```text
fixed shallow absorption depth
+ longitudinal waveguide absorption
+ optional ordinary optical/electrical velocity matching.
```

On the same reduced-order benchmark, a fixed 200-nm absorber adjacent to the multiplication side gives about `5.74 ps RMS` for a 40-um absorption length, versus about `8.37 ps RMS` for the optimized three-state transverse-depth ladder. Without electrical velocity matching it still clears the historical 30% gate to roughly `1.98 mm` absorption length.

Therefore:

```text
exact isochronous identity: RETAIN
finite-ladder/forward-reverse analyses: RETAIN AS CONDITIONAL RESULTS
migrating depth-map APD/SPAD publication path: CLOSE
five/six-state rescue: DO NOT PURSUE
full Maxwell/TCAD optimization of migrating map: DO NOT PURSUE BY DEFAULT
novelty/priority: NOT ESTABLISHED
```

Reopen only if a real physical constraint defeats the fixed-depth waveguide comparator, such as mandatory thick absorption volume for power/energy handling, necessarily multi-millimeter absorption with unavailable velocity matching, or a material system where fixed-depth localization is intrinsically unavailable.

## Experiment 01 — CLOSED publication path

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 remains **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. Its mathematical theorem remains valid, but the unknown-arrival mechanism and optimum-filter information-spectrum formulation reduce to established acquisition/optimum-filter theory.

Do not reopen Step 13–49, Rev. 5 polishing, or attempts to rename `|R|^2/S_n`, `1/NEP^2`, RMS/effective bandwidth, or the timing-cell penalty as new metrics.

## Next-experiment protocol

Start from a microscopic/device-physics premise. Before a long derivation chain:

1. identify the strongest established detector architecture that might remove the proposed problem;
2. compare it quantitatively on the same resource assumptions;
3. run a focused journal/patent audit;
4. stop early if the comparator dominates or the result reduces to established theory;
5. only after surviving those gates build detailed simulation or manuscript structure.
