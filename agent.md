# Agent recovery entrypoint

Read [`AGENTS.md`](AGENTS.md) first for scientific-integrity rules.

## Experiment 04 — EARLY STOP

`experiments/04-nonreciprocal-photodetector/`

Read first:

1. `experiments/04-nonreciprocal-photodetector/CURRENT_STATE.md`
2. `experiments/04-nonreciprocal-photodetector/FIRST_PRINCIPLES_TRACE_BOUND.md`

Question: can nonreciprocity let a detector absorb a desired optical mode strongly while radiatively emitting weakly enough to reduce intrinsic dark current/noise?

For passive linear external channels with scattering matrix `S`,

```math
A_{in}=I-S^\dagger S,
\qquad
E_{out}=I-SS^\dagger,
```

so

```math
\boxed{Tr(A_{in})=Tr(E_{out}).}
```

Directional absorptivity and emissivity can differ, but total channel-integrated absorption and emission are equal.

If `K` orthogonal signal modes must each be perfectly absorbed,

```math
\sum_i e_i=\sum_j a_j\ge K.
```

An ideal reciprocal mode-selective detector that absorbs only those `K` modes attains the same lower bound. Therefore passive nonreciprocity can redirect emitted photons but does not beat the ideal reciprocal comparator on total radiative coupling or accepted-mode thermal photon noise.

Active/time-modulated escape routes are established photonic-refrigeration/energy-conversion problems and must count pump work; do not treat them as free detector sensitivity.

Disposition:

```text
passive nonreciprocal intrinsic-sensitivity path: CLOSED EARLY
trace bound: RETAIN
paper construction: DO NOT BEGIN
novelty: NOT ESTABLISHED
```

Reopen only if a physically unavoidable detector constraint defeats the reciprocal mode-selective comparator while leaving a nonreciprocal implementation viable.

## Experiment 02 — CLOSED

`experiments/02-isochronous-avalanche-photodetector/`

The conditional-mean timing mathematics remains valid, but fixed shallow waveguide absorption plus ordinary traveling-wave engineering dominates the migrating-depth device concept. Do not resume full Maxwell/TCAD optimization by default.

## Experiment 01 — CLOSED

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 remains **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. The theorem is mathematically valid, but the central acquisition/information-spectrum mechanisms are established theory. Do not reopen Step 13–49.

## Next research rule

For every new photodetector gedanken experiment, identify the strongest existing measurement, architecture, thermodynamic bound, or reciprocity argument first. If it already removes the proposed advantage, document the stop before growing the derivation.