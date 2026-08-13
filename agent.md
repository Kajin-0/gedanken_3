# Agent recovery entrypoint

The canonical scientific-integrity instructions are in [`AGENTS.md`](AGENTS.md). Read that file first.

## Active project

The active experiment is:

`experiments/01-equal-dstar-different-speed/`

The current Paper-A technical core has passed the repository's final internal adversarial QA. The authoritative recovery order is:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md`
3. `experiments/01-equal-dstar-different-speed/PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md`
4. `experiments/01-equal-dstar-different-speed/PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
5. `experiments/01-equal-dstar-different-speed/PAPER_A_CLOSEST_PRIOR_ART_AUDIT_2026-08-12.md`
6. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`

Do not resume from memory or a prior chat summary when live repository state is available.

## Hard constraints for the next agent

- The Step-13–49 Gaussian-extremes branch is **hard-stopped**. Do not create Step 50 by default.
- Do not revive the invalid Step-13 `ell~49` grid crossover, the invalid Step-20 upper Rice switch, raw Step-27 tiny-`chi` values, or Step-44 as continuum truth.
- Paper A now concerns a **batch sufficient guarantee time** `T_G`, not an exact online latency and not the exact first solution of the full signal-present scan-power equation.
- Equal eventual matched-filter SNR is event-specific and is **not** the same assumption as equal scalar `D*`.
- The controlling quantitative example is the continuum Rice/Slepian feasibility bracket at `rho0=3.5`, `alpha=.05`, `beta=.90`, `tau_s/tau_f=6`, with `L=9 tau_f=1.5 tau_s`.
- Novelty remains **unestablished**. Classical acquisition, optical-CDMA acquisition, direct-detection ladar acquisition, and pulse-width/range-resolution tradeoffs are prior art. No `first`, `novel`, or priority language is authorized.

## Current next phase

Do not reopen theory unless a genuinely new defect is found. The natural next work is external-style manuscript preparation/review: figures, journal-format rendering, an independent referee pass, and journal-specific citation checks.
