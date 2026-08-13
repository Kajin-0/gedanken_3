# Current State — Experiment 06: SRH Event Provenance

**Date:** 2026-08-13  
**Status:** CLOSED AS DEVICE/PUBLICATION PATH / IDEAL OBSERVABILITY RESULT RETAINED / PRIOR ART OCCUPIES CORE ARCHITECTURE

Read first: `00_PRIOR_ART_STOP.md`, then `FIRST_PRINCIPLES.md`.

## Retained result

For a planar depleted diode,

```math
Q_e=q(1-x/d),
\qquad
Q_h=qx/d,
\qquad
Q_e+Q_h=q.
```

A photon launches electron and hole simultaneously. One ideal SRH generation center produces the complementary carrier pulses through sequential trap transitions with exponential dwell times. In noiseless continuous-time carrier-resolved observation the isolated lineages are distinguishable.

Finite timing resolution gives same-trap leakage

```math
R_{same}
=g[(1-e^{-r_e\delta t})+(1-e^{-r_h\delta t})]
\simeq r_e r_h\delta t.
```

For many traps,

```math
R_{cross}\simeq2\delta t[G^2-\sum_a g_a^2].
```

The complementary fractional Ramo charges provide a depth-consistency fingerprint; for unrelated uniformly distributed trap depths, a charge-complement tolerance `epsilon` accepts fraction `2epsilon-epsilon^2`.

These are conditional calculations, not a new detector architecture.

## Decisive prior art

Hitachi US 6,455,872 (filed 2000, granted 2002) claims a photodetector with separate electrometers for the two opposite-polarity photocarriers and a comparator. The specification explicitly allows the comparator to require **both** electron and hole outputs to identify a photon and reject spurious one-sided events.

Maione et al., Phys. Rev. B 83, 155309 (2011), DOI `10.1103/PhysRevB.83.155309`, model the individual electron/hole trap capture/emission terminal-current pulses and their correlations.

Therefore adding SRH kinetics plus a coincidence window to a two-carrier detector is not a strong novelty basis.

## Feasibility note

Raw fractional-Ramo readout simultaneously requires very high bandwidth and sub-electron charge information. Ordinary avalanche gain is not a clean rescue because impact ionization creates counter-carriers that can manufacture the missing opposite-carrier response.

## Disposition

```text
ideal SRH/photon lineage distinction: RETAIN
finite-resolution leakage formulas: RETAIN
Ramo charge fingerprint: RETAIN
separate electron/hole coincidence architecture: PRIOR ART
carrier-selective avalanche rescue: DO NOT PURSUE BY DEFAULT
paper construction: DO NOT BEGIN
```

Move to a new microscopic detector premise.