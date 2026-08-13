# Experiment 06 — PRIOR-ART STOP

**Date:** 2026-08-13
**Status:** DEVICE/PUBLICATION PATH CLOSED / IDEAL FORMULAS RETAINED

The ideal SRH-versus-photon lineage calculation remains valid: a photon launches electron and hole simultaneously, whereas one SRH generation center produces complementary carrier pulses through sequential trap transitions. Retain the finite-window leakage, many-trap accidental-coincidence, and complementary-Ramo-charge formulas in `FIRST_PRINCIPLES.md`.

The central detector architecture is not available as a novelty claim. Hitachi US 6,455,872 (filed 2000, granted 2002) claims a photoabsorptive region, separate electrometers for opposite-polarity carriers, and a comparator. Its specification explicitly states that the threshold may require both electrometers to respond, indicating both an electron and a hole from an incident photon and rejecting spurious one-sided events.

Maione et al., Phys. Rev. B 83, 155309 (2011), DOI 10.1103/PhysRevB.83.155309, separately model individual terminal-current pulses from electron/hole trap capture and emission and their correlations.

Thus the combination

```text
separate electron/hole detection
+ stochastic trap pulse sequence
+ coincidence/consistency test
```

is too occupied to support the proposed device/publication direction. Adding a timing window is not enough to rescue novelty.

Naive dual-sided avalanche gain is also not a clean escape because impact ionization creates counter-carriers that can manufacture the missing opposite-side response.

Disposition:

```text
ideal lineage distinction: RETAIN
finite timing leakage formulas: RETAIN
Ramo charge fingerprint: RETAIN
separate e/h coincidence architecture: PRIOR ART
avalanche rescue: DO NOT PURSUE BY DEFAULT
paper construction: DO NOT BEGIN
```

Move to a new microscopic detector premise.