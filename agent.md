# Agent recovery entrypoint

Read [`AGENTS.md`](AGENTS.md) first for scientific-integrity rules.

## Experiment 01 — CLOSED

`experiments/01-equal-dstar-different-speed/`

Paper A / Rev. 5 is **DO NOT SUBMIT AS A FULL RESEARCH ARTICLE**. The theorem is mathematically valid, but the unknown-arrival search mechanism and the optimum-filter information-spectrum reformulation are established prior art.

Read `experiments/01-equal-dstar-different-speed/INFORMATION_SPECTRUM_STOP_2026-08-13.md` first if Experiment 01 is ever revisited.

Do not resume Rev. 5 polishing, Step 13–49 Gaussian-extremes work, or attempts to rename RMS/effective bandwidth, `|R|^2/S_n`, or the timing-cell penalty as new metrics.

## Experiment 02 — EARLY STOP

`experiments/02-equal-fluence-different-pulse-shape/`

Question: for the same total absorbed photons, can temporal concentration change the integrated photoconductive response through nonlinear recombination?

Exact results retained:

```math
\int n(t)dt=\tau\int G(t)dt
```

for linear recombination, while cubic recombination gives

```math
\int n(t)dt
=\tau[\int G(t)dt-C\int n^3(t)dt].
```

For an impulsive injection,

```math
A(n_0)=\sqrt{\tau/C}\arctan(n_0\sqrt{C\tau}).
```

For two equal pulses, increasing their separation strictly increases integrated response when effective lifetime decreases with carrier density.

The general sign identity is

```math
\frac{dA_2}{d\Delta}
=[\tau_{eff}(r+q)-\tau_{eff}(r)]r'(\Delta),
\qquad
\tau_{eff}(n)=n/R(n),\quad r'(\Delta)<0.
```

Read:

1. `experiments/02-equal-fluence-different-pulse-shape/CURRENT_STATE.md`
2. `experiments/02-equal-fluence-different-pulse-shape/GENERAL_SIGN_THEOREM.md`
3. `experiments/02-equal-fluence-different-pulse-shape/SPLIT_PULSE_STEP.md`
4. `experiments/02-equal-fluence-different-pulse-shape/PROGRESS_LOG.md`

### Why Experiment 02 stopped

Excitation-correlation spectroscopy already uses two variably delayed pulses and time-integrated photocurrent/photoluminescence to probe nonlinear recombination. Rojas-Gatjens et al., J. Phys. Chem. C (2023), DOI 10.1021/acs.jpcc.3c04755, explicitly model negative nonlinear photocurrent from `gamma n + Bn^2` and `gamma n + An^3` kinetics.

High-injection HgCdTe Auger saturation and injection-dependent lifetime are also longstanding results.

The compact sign theorem is useful, but not presently sufficient novelty for a theory paper. A HgCdTe-specific excitation-correlation experiment might be useful, but no experimental work is available here.

## Adjacent candidate screened and rejected before opening

A proposed `signal-response pole = GR-noise pole` closure test was checked against prior art. HgCdTe literature already ties the GR-noise Lorentzian corner to effective carrier lifetime, and multi-region models explicitly generate multiple GR Lorentzians for multiple lifetimes.

Treat this as a useful lab consistency check, not a new research direction.

## Research rule going forward

Continue **novelty-first screening**.

Prefer simple microscopic/device-physics questions whose first nontrivial consequence is not already a standard detector-characterization or ultrafast-spectroscopy method. Audit prior art before building a large theory or manuscript.

Never reference this research repository inside a publication manuscript.