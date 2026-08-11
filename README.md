# Gedanken 3 — Photodetector Performance Thought Experiments

This repository develops photodetector thought experiments from first principles, one logical step at a time.

The project is deliberately non-teleological: it does not begin by assuming that a conventional detector metric is inadequate or that a replacement metric must exist. Each step should establish only what follows from the stated assumptions, preserve counterexamples, and stop at the first genuinely new consequence.

## Active experiment

`experiments/01-equal-dstar-different-speed/`

Starting question:

> Two hypothetical photodetectors have equal conventional specific detectivity, `D*_A = D*_B`, but vastly different response times (`tau_A = 1 ns`, `tau_B = 1 s`). Does equal `D*` imply equal ability to detect an arbitrary optical signal?

## Research discipline

- State the exact observable and measurement protocol before comparing SNR.
- Treat `D*` as condition-dependent unless frequency, wavelength, area, bandwidth, bias, temperature, and responsivity convention are explicit.
- Separate detector signal transfer from detector/readout noise transfer.
- Prefer counterexamples and minimal models over broad claims.
- Record assumptions, invalidations, and unresolved branches.
- Do not claim novelty from internal derivations alone.

Read `AGENTS.md` first when recovering project context.
