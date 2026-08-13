# Prior-art audit — Experiment 02

**Date:** 2026-08-13
**Disposition:** SURVIVES FIRST SCREEN / NOVELTY NOT ESTABLISHED

## Clearly occupied territory

1. **Absorption/generation position causes APD/SPAD timing jitter.**
   - Rosset et al., *Nuclear Instruments and Methods A* 977, 164346 (2020), DOI 10.1016/j.nima.2020.164346, models random photogeneration position, drift/diffusion, avalanche stochasticity, and timing jitter in SAM-APDs.
   - Waveguide and CMOS SPAD work likewise treats transport time from the photogeneration point to the high-field region as a jitter source.

2. **Waveguide/nanophotonic structures can break the ordinary PDE-versus-jitter thickness tradeoff.**
   - Ma et al., *Nature Communications* 8, 1204 (2017), DOI 10.1038/s41467-017-00733-y, uses nanostructured light trapping to enhance absorption in a thin Si SPAD while retaining low jitter.
   - Yanikgonul et al., *Optics Express* 26, 15232–15246 (2018), DOI 10.1364/OE.26.015232, simulates waveguide SPAD PDE and timing jitter.

3. **Traveling-wave photodetectors already use velocity matching.**
   - Shi, Liu, and Liu, *Journal of Lightwave Technology* 22, 1583–1590 (2004), DOI 10.1109/JLT.2004.829230, models traveling-wave avalanche photodetectors including optical/microwave velocity mismatch, propagation loss, boundary reflection, carrier transport, and multiplication response.
   - This established velocity matching concerns optical propagation versus distributed electrical/microwave output propagation for RF bandwidth.

4. **Position-dependent timing compensation exists in other detector contexts.**
   - Position-sensitive APDs have post-measurement timing-offset corrections.
   - PMT/MCP and charged-particle timing detectors use isochronous electron-transport geometries.
   - Recent SPAD patents seek more uniform avalanche-to-contact propagation distances.

## Specific gap being tested

The present hypothesis is narrower:

> Deliberately correlate optical propagation delay to the photon-absorption site with the internal carrier transit delay from that site to the avalanche-trigger region, so their sum is independent of absorption position.

Working condition:

```math
\frac{d}{dx}[t_o(x)+t_c(x)+t_e(x)+\mu_a(x)]=0.
```

The distinguishing term is `t_c(x)`: the internal carrier-to-avalanche trigger delay.

Standard traveling-wave velocity matching is recovered as a special case when internal carrier delay is position independent. Experiment 02 asks whether a detector can be geometrically or optically engineered so a position-dependent internal carrier delay cancels the optical arrival delay and therefore suppresses single-photon absorption-position jitter.

## Search result as of 2026-08-13

Targeted journal and patent searches have not yet located an APD/SPAD explicitly designed around this optical-delay/internal-carrier-delay cancellation condition.

This is only an absence in the searched literature. It is **not** proof of novelty or priority.

## Search terms already used

- isochronous avalanche photodiode absorption position
- carrier transit compensation optical propagation photodiode
- waveguide APD timing jitter absorption position multiplication region
- position-dependent carrier transit compensation SPAD
- graded/sloped/tilted multiplication region APD timing
- grazing-incidence APD timing jitter
- waveguide SPAD optical path length timing jitter
- patents combining optical propagation delay, carrier transit, avalanche photodiodes

## Closest conceptual precedents

- optical/electrical velocity matching in traveling-wave photodiodes;
- isochronous charged-particle/electron optics;
- nanophotonic redistribution of SPAD absorption;
- spatial timing correction/calibration in position-sensitive APDs.

None found so far combines these specifically to cancel absorption-position carrier transit jitter intrinsically inside an APD/SPAD.

## Current novelty status

```text
Possible device-design synthesis: YES
Novelty established: NO
Priority language authorized: NO
Paper drafting authorized: NO
Further derivation/feasibility work: YES
```