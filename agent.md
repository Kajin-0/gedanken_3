# Agent recovery entrypoint

Read [`AGENTS.md`](AGENTS.md) first for scientific-integrity rules.

## Experiment 01 — CLOSED

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 is **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. The theorem is mathematically valid, but the unknown-arrival search mechanism and optimum-filter information-spectrum reformulation are established prior art.

Read `experiments/01-equal-dstar-different-speed/INFORMATION_SPECTRUM_STOP_2026-08-13.md` first if revisited. Do not reopen Step 13–49 or manuscript polishing.

## Experiment 02 — EARLY STOP

`experiments/02-equal-fluence-different-pulse-shape/`

Equal-fluence pulse-shape dependence under nonlinear recombination was derived exactly, including the general two-pulse sign identity, but the central method is established excitation-correlation spectroscopy. See that experiment's `CURRENT_STATE.md`.

Do not build a theory manuscript from Experiment 02.

## Experiment 03 — ACTIVE

`experiments/03-photon-recycling-noise/`

### Revised question

Do not assume that internal photon-recycling exchange must appear in terminal current noise.

The correct question is:

> **When does photon recycling survive the detector readout as inter-pixel noise, and when does the readout erase it?**

Read in order:

1. `experiments/03-photon-recycling-noise/CURRENT_STATE.md`
2. `experiments/03-photon-recycling-noise/EXTRACTION_CURRENT_CANCELLATION.md`
3. `experiments/03-photon-recycling-noise/LINEAGE_READOUT_AND_SOURCE_STATISTICS.md`
4. `experiments/03-photon-recycling-noise/READOUT_INTERPOLATION.md`
5. `experiments/03-photon-recycling-noise/TERMINAL_CURRENT_CLOSURE.md`
6. `experiments/03-photon-recycling-noise/ARRAY_GRAPH_CLOSURE.md`
7. `experiments/03-photon-recycling-noise/FEASIBILITY_AND_DIFFUSION_DISCRIMINANT.md`
8. `experiments/03-photon-recycling-noise/RADIATIVE_RATE_AND_TIME_DOMAIN.md`

### Internal exchange result

For identical carrier reservoirs with local non-transfer rate `gamma`, conservative exchange rate `k`, and mean population `m`,

```math
S_{x,12}(\omega)
=m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
```

It is positive at low frequency, negative at high frequency, and crosses at

```math
\omega_x=\sqrt{\gamma(\gamma+2k)}.
```

General exchange-noise sign reversal is prior art in other systems; do not claim it as new.

### Deterministic/occupancy closure

Steady neighboring/self crosstalk for a localized source is

```math
c=k/(\gamma+k).
```

For an occupancy-sensitive observable,

```math
\frac{S_{12}}{S_{11}}
=c\frac{\omega_x^2-\omega^2}{\omega_x^2+\omega^2},
```

with

```math
\omega_x^2=\gamma^2(1+c)/(1-c).
```

Thus independently measured `gamma` and `c` predict the full normalized intrinsic spectrum with no free shape parameter.

### Critical no-go result — ideal endpoint counting

Split local loss into extraction `Gamma_e` plus other loss. If terminal current counts only final extraction events,

```math
j_e=\Gamma_e x+\zeta_e,
```

where the same extraction shot-noise event enters the state equation with sign `-zeta_e`.

The state/output correlation cancels the population contribution exactly:

```math
\boxed{S_{j_e}(\omega)=\Gamma_e m I.}
```

Therefore ideal extraction streams are white and mutually uncorrelated even though internal populations are exchange-correlated.

This is exact beyond the Langevin approximation under independent Poisson generation and independent one-for-one routing: each excitation is Poisson-marked by one final sink and delay, so final sink streams are independent Poisson processes.

A Gillespie simulation in `numerics/extraction_current_cancellation_gillespie.py` verifies nonzero sign-changing internal cross-noise and zero extraction cross-noise in the same event-level realization.

### Counterintuitive consequence

```text
mean optical crosstalk can be nonzero
while passive endpoint-count cross-noise is exactly zero.
```

This is ordinary Poisson thinning/routing mathematics, not new queueing theory.

### Device-class boundary

```text
photoconductor / occupancy-sensitive current
    -> internal recycling cross-spectrum can be visible

ideal endpoint-counting photodiode
    -> conservative exchange cross-spectrum can vanish exactly

real junction photodiode
    -> requires Shockley-Ramo / transport impulse response

SPAD / branching gain
    -> one event creates additional measured descendants, so crosstalk correlations are expected
```

SPAD passive crosstalk correlation is prior art.

### General lineage criterion

For independent Poisson generation, if one excitation lineage produces random vector terminal waveform `H_i(omega)`,

```math
S_{ij}(\omega)=\sum_s\lambda_s E[H_i^{(s)}H_j^{(s)*}].
```

Internal coupling becomes terminal cross-noise only when one measured lineage contributes jointly to more than one terminal waveform.

### Source-statistics caveat

Exclusive endpoint routing is uncorrelated only for Poisson generation. For source event-rate PSD `S_in` and routing probabilities `p_i`,

```math
S_{ij}^{out}=p_ip_j[S_{in}-\lambda],\qquad i\ne j.
```

Thermal photon bunching can therefore create positive detector-output correlation independent of recycling. This is classical photon-noise theory.

### Toy readout interpolation

For

```math
I=gx+qj_e,
```

```math
\boxed{
S_I=g(g+q\Gamma_e)S_x+q^2\Gamma_e mI.
}
```

`g=0` gives endpoint-counting cancellation; nonzero occupancy sensitivity restores the cross-spectrum.

### Photon-recycling factorization

Fast photon transfer gives

```math
k_{ij}=\Gamma_r p_{ij},
```

so a radiative origin requires

```math
k_{ij}/p_{ij}=\Gamma_r
```

across pixel pairs when one source population is adequate. This is a possible detector-specific spatial closure, novelty not established.

### Current novelty status

```text
exchange-noise mathematics: old
Poisson-output cancellation mathematics: old
thermal photon-output correlations: old
SPAD passive crosstalk correlations: old
HgCdTe deterministic photon recycling/crosstalk: old

HgCdTe readout-observable boundary and passive photoconductor application:
    potentially useful / novelty NOT established
```

Do not build a manuscript yet.

## Next step

Determine whether a **realistic HgCdTe photoconductor test structure** gives a quantitatively measurable photon-recycling cross-spectrum after Johnson/readout noise, and whether optical controls can separate it from thermal photon correlations, electrical mixing, and carrier diffusion.

For photovoltaic pixels, do not return to the simple occupancy model; use an explicit Shockley-Ramo/transport readout before making terminal-noise claims.

## Global research rule

Continue novelty-first screening. Do not force publication from a mathematically interesting result already covered by adjacent fields. Never reference this research repository inside a publication manuscript.