# Post-Experiment-11 Theoretical Premise Screen 2 — 2026-08-14

**Scope:** analytical/theoretical only  
**Purpose:** preserve rejected premises before opening Experiment 12.  
**Disposition:** **TEN ADDITIONAL CANDIDATES REJECTED / EXPERIMENT 12 NOT OPENED**

This file continues `POST_EXP11_THEORETICAL_SCREEN_2026-08-14.md`.

---

## Candidate 8 — optically allowed but thermally protected transition

Premise: engineer a useful photon transition whose optical matrix element is large while the reverse dark-generation pathway is suppressed by symmetry, momentum, or a larger thermal activation energy.

Disposition: **REJECT.** Infrared heterostructure detector architectures already exploit asymmetric barriers/selection rules so photoresponse energy and dark-current activation energy need not coincide. The broad premise is established band/transition engineering rather than a new detector principle.

---

## Candidate 9 — photon-momentum tagging of signal carriers

Premise: photoexcited carriers inherit photon momentum or a directional momentum-space signature, while thermal carriers are approximately isotropic; momentum-selective collection could discriminate signal from dark carriers.

Disposition: **REJECT.** Photon-drag infrared detection is longstanding, and momentum-space carrier-separation photodetectors have explicitly been proposed to combine useful optical absorption with reduced dark current. No new invariant emerged.

---

## Candidate 10 — electron-hole coincidence as a leakage discriminator

Premise: one absorbed photon creates an electron and a hole in the same microscopic event, whereas important contact/surface leakage mechanisms can inject only one carrier species. Independently sensing both signs could reject unpaired leakage.

First consequence: coincidence can reject single-carrier leakage but intrinsic thermal generation also creates neutral electron-hole pairs and therefore survives the discriminator.

Disposition: **REJECT.** Event-topology/surface discrimination in single-pair-sensitive semiconductor detectors is established, and pair coincidence cannot lower the fundamental intrinsic pair-generation floor.

Screening rule retained:

```text
charge sign / pair multiplicity / event neutrality alone cannot distinguish a photon-created pair from an intrinsic thermally created pair.
```

---

## Candidate 11 — bound-exciton LWIR state

Premise: use a bound exciton with

```math
h\nu=E_g-E_b
```

so the useful optical transition lies below the free-carrier gap, while thermal free carriers still nominally cost `E_g`; subsequently dissociate the exciton into terminal charge.

Disposition: **REJECT.** Excitonic photodetection and field/phonon-assisted exciton dissociation are established design spaces. More fundamentally, a dissociation pathway efficient for the photoexcited exciton is also available to thermally occupied excitons, so an `E_g` dark activation advantage does not follow automatically.

---

## Candidate 12 — phononic bandgap blocks dark generation

Premise: useful photon absorption is direct but a dominant dark transition requires a phonon; suppress the required lattice mode with a phononic bandgap.

Disposition: **REJECT.** Suppression of phonon scattering in mid-IR detectors is established, and phoxonic-crystal detector concepts explicitly engineer phononic gaps to reduce dark current. Broad premise is occupied.

---

## Candidate 13 — bandgap inhomogeneity creates an exponential dark-current penalty

Premise: useful absorption/cutoff changes relatively smoothly with local `E_g`, whereas dark generation contains factors such as

```math
g\sim e^{-aE_g}.
```

Therefore disorder gives Jensen amplification

```math
\langle e^{-aE_g}\rangle
\ge e^{-a\langle E_g\rangle},
```

and finite-area devices may become rare-low-gap-region dominated.

Disposition: **REJECT.** HgCdTe literature already treats composition inhomogeneity as a major source of cutoff and dark-current degradation. The Jensen/extreme-value step is generic exponential-disorder statistics layered onto known MCT physics.

---

## Candidate 14 — low DOS versus Pauli saturation capacity

Premise: reducing the number of optically addressable electronic states suppresses equilibrium thermal carriers but also lowers the number of photoexcitations that can be stored before Pauli blocking bleaches absorption.

Minimal finite-state model gives both dark occupation and saturation capacity proportional to the number of available transitions, so reducing DOS/active volume does not independently improve their ratio.

Disposition: **REJECT.** This is ordinary state filling / saturable-absorber physics, with no specifically photodetector invariant surviving.

---

## Candidate 15 — collection-field / speed versus tunneling dark current

Premise: a larger collection field or smaller depletion width shortens carrier transit time but increases TAT/BTBT leakage.

Disposition: **REJECT.** This leakage-bandwidth conflict is established in high-speed Ge p-i-n photodiodes and narrow-gap/APD design. It is a standard field-engineering tradeoff.

---

## Candidate 16 — correlated electron-hole Ramo shot-noise spectrum

Premise: each photon creates correlated electron and hole current impulses, so terminal current noise need not equal a naive sum of independent `2qI` shot-noise terms, especially at finite frequency.

Disposition: **REJECT.** Generation-recombination noise with Ramo/corpuscular methods, pair correlations, and sub-full-shot-noise factors is mature semiconductor detector theory.

---

## Candidate 17 — spectral-temporal nonseparability

Premise: the absorption coefficient `alpha(lambda)` determines the carrier birth-depth distribution, while drift/diffusion determine transit time. Therefore a photodiode generally has a wavelength-dependent impulse response rather than a separable response

```math
R(\lambda)H(\omega).
```

Disposition: **REJECT.** Classical high-speed p-i-n transient-response theory already includes absorption-depth distributions, diffusion from neutral layers, and wavelength-dependent bandwidth/impulse response. No new invariant emerges from the nonseparability itself.

---

# Overall disposition

```text
Candidates 8-17: REJECTED.
Experiment 12 remains unopened.
```

## Updated screening lesson

Repeated failures now show a strong pattern. A premise is unlikely to survive if it contains only:

```text
one equilibrium occupation law
+
one generic response/conservation theorem.
```

Future candidates should require at least two specifically semiconductor-photodetection constraints whose composition produces a nontrivial result not already recognized as a standard device tradeoff.
