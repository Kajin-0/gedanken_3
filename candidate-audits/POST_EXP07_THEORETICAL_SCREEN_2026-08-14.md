# Post-Experiment-07 theoretical candidate screen

**Date:** 2026-08-14  
**Constraint:** analytical/theoretical research only  
**Status:** no Experiment 08 opened yet

Experiment 07 is closed by default as a novelty path. The following successor premises were screened against strong prior art before opening a new branch.

## 1. Metastable activation-barrier photodetector — STOP

Premise:

A detector sits in a metastable state with barrier `E_b`. Thermal escape creates dark counts while a photon lowers or crosses the barrier. Ask whether a universal dark-count / photon-detection tradeoff follows from Kramers activation.

Reason for stop:

This is already central to superconducting nanowire and Josephson threshold-detector theory. Established models treat photon counts and thermally activated dark counts as competing escapes from metastable states, including vortex crossings, thermal phase slips, and nonequilibrium Josephson threshold detection.

Potential identities such as an Arrhenius signal/dark-rate ratio reduce to standard activated-rate / statistical-decision theory.

Do not open Experiment 08 on this premise.

## 2. Detector reset / Landauer irreversibility — STOP

Premise:

Ask whether every reusable photodetector must dissipate a minimum energy per registered photon because its memory/output state must be reset.

Reason for stop:

Thermodynamic costs of measurement, information erasure, finite-time reset, and quantum-metrology precision are established through Landauer and quantum-information thermodynamics. The generic lower-bound problem is already much broader than photodetection.

A detector-specific application would be an example, not a new fundamental principle.

Do not open Experiment 08 on this premise.

## 3. Sub-Poisson dark current as a detectivity resource — STOP

Premise:

Can interactions or exclusion make dark events sub-Poissonian while leaving useful photoresponse unchanged, producing a fundamental detectivity gain beyond the usual shot-noise model?

Reason for stop:

Shot-noise suppression from correlated transport is established in semiconductor and avalanche photodiodes. APD theory explicitly allows effective excess-noise factors below naive Poisson expectations because of temporal correlations. Generation-recombination shot-noise suppression and Coulomb/transport correlation effects are also established adjacent physics.

Therefore `F<1` for dark-event counts is not a new detector principle. Any performance benefit must be analyzed within established full noise statistics rather than presented as a new fundamental resource.

Do not open Experiment 08 on this premise.

## 4. Experiment-07 analytical correction retained

A new no-go was derived during the transition:

For one-phonon capture with

```math
\Delta=E_{ph}-\varepsilon,
```

threshold proximity does **not** imply isotope sensitivity because electronic zero-point/electron-phonon renormalization can co-move with the phonon.

For a minimal common mass scaling

```math
E_{ph}=P M^{-1/2},
\qquad
\varepsilon=\varepsilon_\infty+Z M^{-1/2},
```

```math
\Delta=-\varepsilon_\infty+(P-Z)M^{-1/2}.
```

Thus `Z=P` makes the detuning isotope-independent even arbitrarily near threshold.

Controlling note:
`experiments/07-isotope-srh/THRESHOLD_PROXIMITY_ISOTOPE_NO_GO_2026-08-14.md`.

This reinforces the closure of Experiment 07 rather than reopening it.

## 5. Current search rule for Experiment 08

Do not open a branch for:

- metastable threshold escape;
- detector reset / Landauer cost;
- generic sub-Poisson shot-noise suppression;
- another isotope/capture parameterization;
- another readout/provenance side channel.

The next premise should alter a deeper photodetection constraint and survive comparison against:

- detailed balance / Kirchhoff / fluctuation-dissipation;
- quantum measurement thermodynamics;
- standard shot-noise and mesoscopic-transport theory;
- optimum filtering and acquisition theory;
- Shockley-Ramo and avalanche theory;
- established coherent/quantum photodetection.

No Experiment 08 has been opened yet. This is intentional.