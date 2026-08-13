# Agent recovery entrypoint

Read [`AGENTS.md`](AGENTS.md) first for scientific-integrity rules.

## Current project state

### Experiment 01 — CLOSED as a publication path

`experiments/01-equal-dstar-different-speed/`

The original theorem is mathematically valid, but the central unknown-arrival search mechanism is established acquisition/detection theory. The device-engineer manuscript Rev. 5 is therefore:

```text
DO NOT SUBMIT AS A FULL RESEARCH ARTICLE.
```

This is a novelty disposition, not a mathematical retraction.

Read, in order:

1. `experiments/01-equal-dstar-different-speed/INFORMATION_SPECTRUM_STOP_2026-08-13.md`
2. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
3. `experiments/01-equal-dstar-different-speed/REV5_REJECTION_AND_RESEARCH_DISPOSITION_2026-08-13.md`
4. `experiments/01-equal-dstar-different-speed/PHOTOCONDUCTOR_INFORMATION_BANDWIDTH_2026-08-13.md`
5. `experiments/01-equal-dstar-different-speed/PHYSICAL_NOISE_COUPLING_2026-08-13.md`
6. `experiments/01-equal-dstar-different-speed/MIXED_NOISE_FINITE_PULSE_2026-08-13.md`
7. `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md` only as preserved theorem history.

### Experiment 01 final reduction

For measured complex responsivity `R(f)` and output-noise PSD `S_n(f)`,

```math
W(f)=|R(f)|^2/S_n(f)=1/NEP^2(f)
```

in consistent input-power units. For optical-event spectrum `P(f)`, all of the explored optimal linear-Gaussian timing quantities follow from

```math
I_P(f)=|P(f)|^2W(f).
```

- matched-filter SNR is its zeroth moment;
- arrival-time Fisher information is its second moment;
- unknown-arrival correlation is its normalized Fourier transform.

These are classical optimum-filter quantities. Do not rename them as new metrics.

The useful photoconductor interpretation retained from the branch is

```math
\tau_{info}=\tau/\sqrt{1+S_{GR,0}/S_W},
```

showing that responsivity bandwidth and optimally whitened information bandwidth can differ when GR noise shares the carrier-lifetime pole with the signal. Novelty is not established.

## Hard stops

- Do not resume Rev. 5 polishing or submission production.
- Do not claim the unknown-arrival timing-cell penalty, RMS/effective bandwidth, `W(f)`, or `tau_info` as novel.
- The Step-13–49 Gaussian-extremes branch remains hard-stopped. Do not create Step 50 by default.
- Do not revive invalid historical finite-grid/Palm claims.
- Never reference this research repository inside a manuscript intended for publication.

## Next research rule

Start a new photodetector gedanken experiment from a microscopic/device-physics premise, not from acquisition theory. Perform a prior-art audit early, before manuscript construction. If the result reduces to a known detector or signal-processing identity, document the closure and move on rather than forcing novelty.