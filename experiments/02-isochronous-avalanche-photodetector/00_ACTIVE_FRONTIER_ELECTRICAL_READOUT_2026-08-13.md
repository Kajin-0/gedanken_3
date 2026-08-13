# Active frontier — electrical readout architecture

**Date:** 2026-08-13  
**Read first:** `ELECTRICAL_READOUT_EQUIVALENCE_2026-08-13.md`, then `THREE_STATE_COUPLED_MODE_SURROGATE_2026-08-13.md`.

Latest result: independent electrical segmentation exposes the section coordinate, so calibrated per-section timestamp offsets remove the same between-section conditional-mean variance as ideal optical precompensation. Segmented readout is therefore not a clean demonstration of passive isochronous timing.

The leading implementation is now a **single/common-output distributed or traveling-wave avalanche detector**. Its electrical propagation delay must be included in the exact depth-map condition. Near-end electrical propagation can shorten the required optical path; far-end propagation generally lengthens it. If the forward device is matched, reversing optical propagation gives the exact residual slope `dm_r/dx=-2/v_g`, independent of deterministic electrical delay.

Next hard step: compare lumped common-output, segmented calibrated, and traveling-wave common-output architectures on timing, capacitance, avalanche/readout physics, and resource cost before full Maxwell/TCAD work.

Novelty remains unestablished. Do not draft a paper or use priority language.
