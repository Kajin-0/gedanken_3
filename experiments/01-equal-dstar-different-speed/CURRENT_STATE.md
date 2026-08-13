# Current State — Experiment 01: Equal sensitivity, different speed

**Date:** 2026-08-13
**Status:** **SCIENTIFICALLY CLOSED AS A PUBLICATION PATH.** The mathematical results are preserved, but the research-article novelty case failed independent prior-art review.

## Final decision

```text
Paper A / Rev. 5: DO NOT SUBMIT AS A FULL RESEARCH ARTICLE.
Original theorem: mathematically valid.
Pedagogical/device interpretation: useful.
Novelty: not established.
```

The decisive issue is not a discovered mathematical error. The central unknown-arrival mechanism — shorter timing correlation, more effectively resolvable timing hypotheses, and a higher global false-alarm threshold — is established acquisition/detection theory. Optimum timing with arbitrary stationary detector noise, finite sampled processing, and RMS/effective timing bandwidth are also established prior art.

Read next:

1. `INFORMATION_SPECTRUM_STOP_2026-08-13.md` — final closure
2. `REV5_REJECTION_AND_RESEARCH_DISPOSITION_2026-08-13.md` — hostile-review adjudication
3. `PHOTOCONDUCTOR_INFORMATION_BANDWIDTH_2026-08-13.md` — retained device interpretation
4. `PHYSICAL_NOISE_COUPLING_2026-08-13.md`
5. `MIXED_NOISE_FINITE_PULSE_2026-08-13.md`
6. `PAPER_A_DRAFT.md` — preserved theorem history

## Final general reduction

For measured complex responsivity `R(f)` and output-noise PSD `S_n(f)`, define

```math
W(f)=\frac{|R(f)|^2}{S_n(f)}.
```

In consistent optical-input units,

```math
W(f)=1/NEP^2(f).
```

For optical-event spectrum `P(f)`,

```math
I_P(f)=|P(f)|^2W(f).
```

Then

```math
\rho_\infty^2=\int I_P(f)df,
```

```math
J_\theta=(2\pi)^2\int f^2I_P(f)df,
```

and

```math
C(\Delta)=
\frac{\int I_P(f)e^{i2\pi f\Delta}df}
{\int I_P(f)df}.
```

Thus the project’s matched-filter SNR, timing Fisher information, and unknown-arrival covariance are the zeroth moment, second moment, and normalized Fourier transform of the same classical optimum-filter information spectrum.

Do not rename these quantities as new detector metrics.

## Retained photoconductor result

For a single-pole photoconductor with GR-noise plateau `S_GR,0` and white Johnson/readout floor `S_W`,

```math
\boxed{\tau_{info}=\frac{\tau}{\sqrt{1+S_{GR,0}/S_W}}.}
```

This gives a useful physical warning:

```text
raw responsivity -3 dB bandwidth != optimally whitened timing bandwidth in general.
```

When GR noise shares the carrier-lifetime pole with the signal, part of that pole cancels under optimal whitening. A real HgCdTe scale check showed that the correction can be large. This is a useful detector interpretation, not an established new optimum-filter principle.

## Historical theorem retained

The original sufficient-guarantee-time theorem and its continuum witness remain mathematically valid. It proves a crossover for a controlled equal-eventual-SNR family, not exact finite-time scan latency and not universal slow-detector superiority.

A conventional first-order finite-pulse replacement construction also reproduces the slow-only guarantee-feasibility separation, including for a finite six-correlator timing bank. This answered the physical-model and continuum-only criticisms but did not rescue novelty.

## Hard stops

- Step-13–49 Gaussian-extremes work remains hard-stopped; do not create Step 50 by default.
- Do not resume Rev. 5 manuscript polishing.
- Do not claim the timing-cell search penalty, RMS/effective bandwidth, `W(f)`, or `tau_info` as novel.
- Never reference the research repository inside a publication manuscript.

## Next move

Start a new photodetector gedanken experiment from a microscopic/device-physics premise. Perform the prior-art audit near the beginning, not after manuscript construction.