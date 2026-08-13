# Novelty-first screening log — 2026-08-13

This file records candidate photodetector gedanken directions screened after Experiments 01 and 02. The purpose is to prevent repeated investment in ideas already covered by mature detector, spectroscopy, or signal-processing literature.

## 1. Joint optical-response / noise hidden-state counting

Question: if optical transfer-function poles and intrinsic noise Lorentzians do not match, what minimum internal state dimension is required?

Result: useful detector corollary, but classical stochastic realization/spectral-factorization theory already treats minimal state-space realization from deterministic transfer functions and stochastic spectra. Older photoconductor literature also compares lifetime inferred from GR noise with direct pulsed response.

Disposition: **do not open as a theory experiment.** A response pole plus two intrinsic GR Lorentzians rules out a one-state model, but this is a systems-identification consistency check, not new theory.

## 2. Diffusion-length breakdown of D* area normalization

Initial intuition: spatial carrier diffusion might correlate GR fluctuations and invalidate the conventional `sqrt(A)` area normalization when detector dimensions approach diffusion length.

Correction: diffusion alone conserves total carrier number. For a closed/uniformly weighted linear detector,

```math
\partial_t\delta n=D\nabla^2\delta n-\delta n/\tau+\xi
```

integrates to a total-number mode in which the diffusion term vanishes. Diffusion by itself is therefore insufficient to break extensive GR-noise scaling. Geometry matters through surfaces, contacts, extraction, nonuniform weighting, or carrier loss across boundaries.

HgCdTe/SPRITE literature already treats diffusion, geometry, lifetime and spatial response.

Disposition: **candidate falsified in its naive form.**

## 3. Zero-bias detection through noise only

Question: can an unbiased photoconductor detect illumination with zero mean current solely because illumination changes resistance and fluctuation noise?

Physics: yes in principle. At thermal equilibrium the open-circuit Johnson voltage PSD is `4kTR`, while the short-circuit current PSD is `4kT/R`. If illumination changes `R`, the variance can change even at zero mean current.

But Johnson-noise thermometry/radiometry and thermal-noise detector readout are longstanding fields.

Disposition: **good teaching example; not opened as research theory.**

## 4. Surface-versus-bulk 1/f noise from geometry scaling

Question: can two HgCdTe geometries with different surface/volume ratios distinguish surface/interface fluctuators from bulk Hooge-like noise through scaling alone?

This is experimentally useful but lies close to established Hooge/McWhorter and spatial noise-localization methods. HgCdTe models already include localized 1/f, GR, dislocation, interface and diffusion noise sources.

Disposition: **diagnostic idea, insufficient novelty for theory branch.**

## 5. HgCdTe e-APD near-deterministic avalanche multiplication

Question: how can a random impact-ionization process have excess-noise factor near `F=1`?

Prior art is extensive. Dead-space / age-dependent branching-process theory has long shown that the finite energy-build-up distance introduces order and suppresses excess noise. Current HgCdTe Monte Carlo work explicitly models the same mechanism, along with strongly electron-dominated impact ionization.

A live research discrepancy remains in the dependence of excess noise on junction geometry / field inhomogeneity, but resolving it requires detailed transport simulation or experiment.

Disposition: **active research area, but not a simple untouched gedanken theorem.**

## 6. Does a 1.06-um lifetime measurement equal the lifetime relevant to LWIR detection?

This remains a useful measurement-validity question.

Established facts:

- HgCdTe transient lifetime work uses ~10-ns 1.06-um YAG pulses.
- At high excess-carrier density, decay becomes nonexponential and injection-dependent.
- Recent mid-IR PL work also finds strong injection/surface dependence of extracted lifetime.

A one-population memoryless recombination model has a simple closure: once two preparations have the same post-thermalization carrier-density state, their subsequent decay cannot depend on pump photon energy. Persistent pump-energy dependence under matched post-thermalization conditions therefore implies an omitted state or spatial degree of freedom.

Potential omitted physics includes absorption-depth weighting, surfaces, traps, hot carriers, carrier multiplication, and nonlinear injection.

### Carrier-multiplication caveat

A 1.06-um photon has much more energy than a LWIR HgCdTe bandgap. HgCdTe impact-ionization models place electron threshold energies close to the gap, so a hot photoelectron is energetically capable of secondary pair creation. However, whether this occurs appreciably before phonon cooling at low field depends on microscopic scattering rates.

No primary source found in this screening establishes appreciable single-photon carrier multiplication in bulk HgCdTe from a 1.06-um lifetime pump under the relevant low-field conditions.

Therefore **do not assume carrier multiplication**. It remains an experimental caveat.

Disposition: **measurement-validity question remains open/useful, but no theory novelty established.**

## Research rule

The early-screening method is working. Do not create a manuscript or large theory branch merely because a result is physically interesting.

Require at least one of the following before opening a new major experiment:

1. a device-physics consequence not reducible to a standard characterization method;
2. a clean contradiction/falsification criterion not already standard in the literature;
3. a quantitatively testable prediction for HgCdTe that differs from existing models;
4. a genuine gap exposed by direct comparison with primary prior art.
