# Prior-art audit — Experiment 02

**Date:** 2026-08-13
**Disposition:** SURVIVES EXPANDED SCREEN / NARROWED TO TRANSVERSE DEPTH COMPENSATION / NOVELTY NOT ESTABLISHED

## Clearly occupied territory

1. **Absorption/generation position causes APD/SPAD timing jitter.**
   - Rosset et al., *Nuclear Instruments and Methods A* 977, 164346 (2020), DOI 10.1016/j.nima.2020.164346, models random photogeneration position, drift/diffusion, avalanche stochasticity, and timing jitter in SAM-APDs.
   - Modern SPAD reviews and models likewise treat transport time from the photogeneration point to the high-field region as a timing-jitter source.

2. **Waveguide/nanophotonic structures can break the ordinary PDE-versus-jitter thickness tradeoff.**
   - Ma et al., *Nature Communications* 8, 628 (2017), DOI 10.1038/s41467-017-00733-y, uses nanostructured light trapping to enhance absorption in a thin Si SPAD while retaining low jitter.
   - Yanikgonul et al. model waveguide SPAD PDE and timing jitter.

3. **Traveling-wave photodetectors already use velocity matching.**
   - Shi, Liu, and Liu, *Journal of Lightwave Technology* 22, 1583–1590 (2004), DOI 10.1109/JLT.2004.829230, models traveling-wave avalanche photodetectors including optical/microwave velocity mismatch, carrier transport, multiplication response, propagation loss, and reflections.
   - Classical distributed photodetectors can cancel longitudinal optical-position delay against electrical propagation delay when optical and microwave velocities are matched.

4. **Lateral waveguide APD building blocks are established.**
   - Liu et al., *Micromachines* 13, 649 (2022), DOI 10.3390/mi13050649, demonstrate a waveguide Ge/Si APD with lateral multiplication region and carrier-transit-limited bandwidth.
   - Pang et al., *Optics Letters* 47, 4463–4466 (2022), DOI 10.1364/OL.466206, demonstrate another lateral Ge/Si waveguide APD.
   - Xue et al., *Nature Communications* 17, 3730 (2026), DOI 10.1038/s41467-026-70461-9, demonstrate a high-GBP lateral Si-Ge APD with a tapered optical input and rear DBR; the reported multiplication geometry is not longitudinally depth-compensated.

5. **Position-dependent carrier transit has been engineered before.**
   - US6239422B1, *Variable electrode traveling wave metal-semiconductor-metal waveguide photodetector* (priority 1998/1999 era), uses exponentially tapered electrode geometry. Carrier transit time varies with longitudinal position, but the stated design objective is optical-power/current-density and field/bandwidth management; the taper is not presented as optical-arrival/internal-carrier-delay cancellation for event timing.

6. **APD absorber transit time has been optimized structurally.**
   - US7557387B2 / US20070200141A1 (priority 2004), optimizes depleted and neutral absorber thicknesses to minimize carrier-transit response delay at fixed total absorber thickness. It does not correlate optical propagation delay with absorption depth.

7. **Modern NIR SPAD patents explicitly recognize absorption-position timing uncertainty.**
   - US20240063321A1 describes large NIR absorption depth as a timing-jitter problem and uses lateral waveguide/segmented SPAD regions to control PDE and jitter. The strategy partitions/reduces the spatial timing problem rather than equalizing optical and carrier delays.

8. **Position-dependent timing compensation exists in other detector contexts.**
   - Position-sensitive APDs can use post-measurement timing-offset corrections.
   - PMT/MCP and charged-particle timing detectors use isochronous electron-transport geometries.
   - Some SPAD patents seek more uniform carrier path or avalanche-to-contact propagation distances.

## Critical narrowing after the expanded audit

A generic longitudinal condition

```math
\frac{d}{dx}[t_o+t_c+t_e+\mu_a]=0
```

is too close to generalized traveling-wave delay matching to support a distinct research claim by itself.

Therefore the active hypothesis is now specifically **transverse absorption-depth compensation**:

> Map physical absorption depth onto optical propagation time so that deeper/later internal carrier transit is compensated by earlier optical arrival, making the conditional mean avalanche-trigger timestamp independent of absorption depth.

For a designed mean depth `z_bar(x)` and constant velocities,

```math
t(x)=x/v_g+[d-z_bar(x)]/v_c,
```

with exact compensation at

```math
\boxed{dz_bar/dx=v_c/v_g.}
```

This transverse carrier-depth term is not removed merely by matching optical propagation to electrical/microwave output propagation.

## Optical feasibility precedent

Three-dimensional integrated photonics has demonstrated adiabatic vertical optical-mode transfer over several micrometers using sub-millimeter taper lengths. Thus slowly moving an optical mode through a few micrometers of depth over a millimeter-scale path is not obviously forbidden by mode-conversion physics. Simultaneously maintaining controlled useful absorption and a narrow conditional absorption-depth distribution remains an open device-design problem.

## Search result as of 2026-08-13

Targeted journal and patent searches have not yet located an APD/SPAD explicitly designed to make optical propagation delay compensate **transverse absorption-depth-dependent carrier transit to the avalanche region**.

This is only an absence in the searched literature. It is **not** proof of novelty or priority.

## Search terms already used

- isochronous avalanche photodiode absorption position
- carrier transit compensation optical propagation photodiode
- waveguide APD timing jitter absorption position multiplication region
- position-dependent carrier transit compensation SPAD
- graded/sloped/tilted multiplication region APD timing
- grazing-incidence APD timing jitter
- waveguide SPAD optical path length timing jitter
- absorption depth optical delay avalanche photodiode timing compensation
- patents combining optical propagation delay, carrier transit, avalanche photodiodes

## Current novelty status

```text
Possible device-design synthesis: YES
Distinct hypothesis after narrowing: YES
Novelty established: NO
Priority language authorized: NO
Paper drafting authorized: NO
Further feasibility + prior-art work: YES
```