# Current State — Experiment 06: SRH Event Provenance

**Date:** 2026-08-13  
**Status:** ACTIVE PROVISIONAL / IDEAL DISTINGUISHABILITY DERIVED / PRACTICAL READOUT AND GAIN CONFLICT OPEN / NOVELTY NOT ESTABLISHED

## Core result

In a planar depleted diode with weighting potential `phi_w=x/d`, a photon-generated pair at depth `x` produces simultaneous electron and hole Ramo currents with complementary integrated charges

```math
Q_e=q(1-x/d),
\qquad
Q_h=qx/d,
\qquad
Q_e+Q_h=q.
```

An SRH generation center produces the same net pair through sequential trap transitions

```text
empty -> filled + mobile hole      rate r_h
filled -> empty + mobile electron  rate r_e.
```

The full-cycle rate is

```math
g=r_e r_h/(r_e+r_h).
```

With ideal continuous-time carrier-resolved observation, photon launch-time difference is exactly zero while an SRH pair has continuous exponential separation. Ideal classification error is therefore zero under the isolated-lineage model.

For finite timing resolution `delta_t`, same-trap unresolved leakage scales as

```math
R_same
=g[(1-e^{-r_e delta_t})+(1-e^{-r_h delta_t})]
\simeq r_e r_h delta_t.
```

For many traps with rates `g_a` and `G=sum g_a`, cross-trap accidental electron/hole coincidences scale as

```math
R_cross\simeq2delta_t[G^2-sum g_a^2].
```

The complementary induced charges provide a depth/lineage fingerprint. A charge gate `|Q_e+Q_h-q|<epsilon q` accepts a fraction `2epsilon-epsilon^2` of unrelated uniformly distributed trap-depth pairs.

See `FIRST_PRINCIPLES.md`.

## Prior art

Do not claim the trap pulse sequence itself as new. Maione et al., Phys. Rev. B 83, 155309 (2011), DOI `10.1103/PhysRevB.83.155309`, explicitly model terminal current pulses from electron/hole trap capture and emission.

Photo/dark APD discrimination from multiplication-history pulse-height statistics is also established (Williams et al., IEEE JEDS 1, 99-110, 2013, DOI `10.1109/JEDS.2013.2263196`). Generic coincidence dark-noise rejection and single-e-h-pair charge resolution are established adjacent techniques.

No exact prior-art match to the complementary-Ramo SRH provenance veto in one linear photodiode has been found in the targeted search. This is not proof of novelty.

## Severe feasibility scale

For illustrative HgCdTe values `d=2 um`, `v_e=1e7 cm/s`, `v_h=3e6 cm/s`, single-carrier Ramo currents are only about `8 nA` and `2.4 nA` with maximum transit times about `20 ps` and `67 ps`.

A passive equilibrated charge input has `sigma_Q=sqrt(kTC)`. At 77 K, `q^2/(kT)=24.15 aF`; high photon acceptance requires resolving fractional charges much smaller than `q`, making ordinary fast electrical readout extremely difficult.

This is not a universal quantum limit; active/cryogenic charge amplification changes the measurement model.

## Avalanche rescue problem

A two-sided structure with separate electron and hole multiplication regions is structurally plausible and dual-carrier multiplication APDs already exist. But ordinary avalanche gain creates counter-carriers. An electron avalanche with gain `M_e` creates order `M_e-1` secondary holes. If each has probability `p_h` of reaching/triggering the opposite side,

```math
P_false,h=1-(1-p_h)^(M_e-1).
```

High gain therefore tends to manufacture the missing coincidence and erase the SRH provenance unless avalanche-generated counter-carriers are locally blocked/collected.

Naive two-sided ordinary avalanche coincidence is rejected. A carrier-selective, locally isolated gain architecture remains open but spends substantial additional device complexity.

## Next hard question

Before designing such a gain architecture, audit whether carrier-selective dual-sided multiplication/collection already exists and whether it can suppress counter-carrier feedback without blocking desired primary carriers. If the required isolation is simply another known coincidence-detector architecture, close Experiment 06 rather than forcing novelty.