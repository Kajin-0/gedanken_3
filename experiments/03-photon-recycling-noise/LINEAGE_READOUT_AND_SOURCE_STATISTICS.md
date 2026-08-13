# Lineage readout and source-statistics boundary

**Date:** 2026-08-13
**Status:** GENERAL SHOT-NOISE ORGANIZATION / CLASSICAL MATHEMATICS / DEVICE INTERPRETATION

## 1. One excitation lineage, many possible terminal observables

Let independent generation events of source class `s` occur as a stationary Poisson process of rate `lambda_s`.

Each generated excitation follows a random internal history — transport, recombination, photon recycling, extraction, branching — and produces a vector terminal-current waveform

```math
h^{(s)}(t)=(h_1^{(s)}(t),...,h_N^{(s)}(t)).
```

Let `H_i(omega)` be its Fourier transform.

Classical Poisson shot-noise / Campbell theory gives the centered output cross-spectral matrix

```math
\boxed{
S_{ij}(\omega)
=\sum_s\lambda_s
\mathbb E[H_i^{(s)}(\omega)H_j^{(s)*}(\omega)].
}
```

This equation is the clean readout criterion for Experiment 03.

Photon exchange can exist internally without appearing in terminal cross-noise. What matters is whether one **measured excitation lineage** contributes jointly to more than one terminal waveform.

## 2. Endpoint-counting photodiode

If one lineage ends in exactly one collection channel `F`, and the readout counts only that final extraction event,

```math
H_i(\omega)=q e^{-i\omega T}\mathbf 1_{F=i}.
```

For `i != j`,

```math
H_iH_j^*=0
```

for every lineage, hence

```math
\boxed{S_{ij}(\omega)=0.}
```

This is the same exact cancellation described in `EXTRACTION_CURRENT_CANCELLATION.md`.

The detector can still have nonzero **mean** optical crosstalk because source excitations are routed to different final pixels. Mean crosstalk and passive count correlation are different observables.

## 3. Occupancy-sensitive photoconductor

If terminal current is proportional to carrier occupancy while the excitation resides in a pixel,

```math
h_i(t)=g_i\mathbf 1_{X(t)=i},
```

then one recycled lineage can contribute first to one pixel and later to another. Generally

```math
\mathbb E[H_iH_j^*]\ne0,
```

so the exchange cross-spectrum survives.

The symmetric two-pixel birth/death/exchange result in `CURRENT_STATE.md` is one exactly solvable example.

## 4. Shockley-Ramo junction readout

For a junction detector, carrier motion induces current before endpoint collection. A schematic single-carrier contribution is

```math
i_i(t)=q\,\mathbf v(t)\cdot\mathbf E_{w,i}[\mathbf r(t)],
```

with pixel weighting field `E_w,i`.

A single carrier trajectory can therefore contribute waveform components to more than one electrode if weighting fields overlap or if a recycled lineage occupies more than one spatial region.

The endpoint-counting cancellation is not generally valid for such a waveform observable. A distributed transport / Shockley-Ramo model is required.

## 5. Branching or gain device

In a SPAD, an avalanche in pixel A is already recorded while avalanche luminescence can trigger an additional avalanche in pixel B. One primary lineage therefore produces multiple measured descendants.

The vector waveform has joint support, so cross-correlation is expected. This is why passive dark-event timing correlations measure SPAD optical crosstalk without contradicting the conservative-routing no-go theorem.

## 6. General readout lesson

```text
internal coupling is not enough

terminal cross-noise requires
one stochastic lineage -> joint terminal waveform
```

The following mechanisms can create joint waveform support:

- occupancy/conductance readout;
- Shockley-Ramo induced current during transit;
- branching or avalanche gain;
- electrical/capacitive readout mixing;
- correlated external generation.

Exclusive final routing of independent Poisson excitations does not.

## 7. Non-Poisson source statistics

The extraction-current cancellation also relies on Poisson generation.

Let one stationary input point process have mean event rate `lambda` and event-rate PSD `S_in(omega)`. Independently assign each event to one exclusive final output with probability `p_i`.

For the output count processes,

```math
\boxed{
S_{ii}^{out}(\omega)
=p_i\lambda+p_i^2[S_{in}(\omega)-\lambda],
}
```

and for `i != j`,

```math
\boxed{
S_{ij}^{out}(\omega)
=p_i p_j[S_{in}(\omega)-\lambda].
}
```

Therefore:

```text
Poisson source:      S_in=lambda -> zero inter-output cross-spectrum
super-Poisson source:            -> positive inherited correlation
sub-Poisson source:              -> negative inherited correlation
```

For long count windows with source Fano factor `F`,

```math
\operatorname{Cov}(N_i,N_j)
=p_i p_j\,\mathbb E[N](F-1).
```

This is standard thinning of a point process, not a new detector theorem.

## 8. Infrared-background consequence

Thermal optical radiation is not perfectly Poisson. Bose photon bunching produces excess noise and can correlate detector outputs when they share optical modes. Classical infrared photon-noise theory already includes this effect.

Thus a positive passive inter-pixel correlation in a background-limited infrared array can arise from the incident field itself and must not be attributed to photon recycling without controls.

The exchange model's negative spectral component is potentially more discriminating, but electrical mixing, feedback, or other coupled dynamics can also produce negative cross-spectra.

## 9. Current Experiment-03 claim boundary

Do not claim that passive cross-noise universally measures photon recycling.

A correct detector-specific statement is:

> Photon recycling is visible in passive terminal cross-noise only to the extent that the source statistics and terminal impulse response preserve joint information from the same excitation lineage.

The next physically important task is to determine that impulse response for a real HgCdTe device class rather than assume that carrier-population noise equals terminal-current noise.