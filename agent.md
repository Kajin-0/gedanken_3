# Agent recovery entrypoint

The canonical scientific-integrity instructions are in [`AGENTS.md`](AGENTS.md). Read that file first.

## Active project

The active experiment is:

`experiments/01-equal-dstar-different-speed/`

Paper A's theorem-level technical core has passed internal adversarial QA. The active manuscript has now been rewritten specifically so that a photodetector/device engineer can understand the physical result from the title, abstract, introduction, and conclusion without first learning Gaussian-process terminology.

Read in this order:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PAPER_A_DRAFT.md` — authoritative audited theorem manuscript
3. `experiments/01-equal-dstar-different-speed/PAPER_A_APPLIED_OPTICS_DRAFT.md` — journal-facing technical draft
4. `experiments/01-equal-dstar-different-speed/PAPER_A_FIRST_ORDER_ROBUSTNESS_2026-08-13.md`
5. `experiments/01-equal-dstar-different-speed/PAPER_A_FULL_SCAN_VALIDATION_2026-08-13.md`
6. `experiments/01-equal-dstar-different-speed/PAPER_A_FULL_SCAN_VALIDATION_ADDENDUM_2026-08-13.md`
7. `experiments/01-equal-dstar-different-speed/PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md`
8. `experiments/01-equal-dstar-different-speed/PAPER_A_QUANTITATIVE_REGIME_WITNESS_2026-08-12.md`
9. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`

Do not resume from memory or a prior chat summary when live repository state is available.

## Hard scientific constraints

- The Step-13–49 Gaussian-extremes branch is **hard-stopped**. Do not create Step 50 by default.
- Do not revive the invalid Step-13 `ell~49` grid crossover, the invalid Step-20 upper Rice switch, raw Step-27 tiny-`chi` values, or Step-44 as continuum truth.
- Paper A concerns a **batch sufficient guarantee time** `T_G`, not exact online latency and not the exact first solution of the full signal-present scan-power equation.
- Equal eventual matched-filter SNR is event-specific and is **not** the same assumption as equal scalar `D*`.
- The controlling quantitative result is the continuum Rice/Slepian feasibility bracket at

```text
rho0 = 3.5
alpha = .05
beta = .90
tau_s/tau_f = 6
L = 9 tau_f = 1.5 tau_s
```

with

```math
P_{FA,s}\le0.0336428<0.05<0.0624701\le P_{FA,f}.
```

- `alpha=.05` and `r=6` are proof-friendly witness values, **not** recommended operating specifications or claimed representative detector values.
- Novelty remains **unestablished**. Classical acquisition, optical-CDMA acquisition, direct-detection ladar acquisition, sensitivity-bandwidth combinations, and pulse-width/range-resolution tradeoffs are prior art. No `first`, `novel`, or priority language is authorized.

## Manuscript communication constraints

These are now hard requirements, not optional style preferences:

- **Never mention or cite the research repository in the paper.** The repository is an internal research/documentation tool, not a manuscript reference.
- Do not put a GitHub URL, repository path, branch name, or repository archive instruction in the manuscript or Data Availability statement.
- If a Data Availability section is required, use a neutral statement such as: no experimental data were collected; numerical values follow from the equations and simulation procedures in the manuscript; supporting code/calculation files are available from the corresponding author upon reasonable request.
- A detector/device engineer should understand the physical question and result by reading only the title, abstract, first page, and conclusion.
- The paper should lead with the original gedanken experiment, not with `D*`, Gaussian-process terminology, acquisition-theory jargon, or theorem notation.
- The core physical picture must remain explicit:

```text
known arrival:
    faster detector -> signal evidence arrives sooner -> fast wins

unknown arrival:
    faster detector -> narrower timing signature
                    -> more distinct timing trials in the same physical window
                    -> higher threshold for the same whole-window false-alarm rate

competition:
    the timing-search penalty can outweigh the speed advantage
```

- Terms such as Rice, Slepian, nuisance parameter/domain, composite alternative, covariance ordering, and Gaussian-process extrema belong in the derivation, not in the abstract or conclusion unless absolutely necessary.
- `T_G` must be explained in words before relying on the symbol: it is the additional observation time needed to certify a target detection probability while limiting false alarms over the entire unknown-arrival search. It is not detector rise time and not an exact real-time stopping latency.
- Preserve rigor underneath the simplified exposition. Do not simplify by silently strengthening the theorem into exact scan-time reversal.

## Current journal-facing framing

Current title for the device-engineer-readable render:

> **When a Faster Photodetector Can Take Longer to Guarantee Detection**

Preferred abstract-level message:

> If arrival time is known, faster wins. If arrival time is uncertain, a faster detector gives noise more distinct chances to imitate the signal over the same physical search window, so the global threshold must rise. With equal final SNR, that search penalty can become large enough for the slower detector to require less additional observation time to guarantee the same detection probability.

The journal-facing draft is deliberately separate from `PAPER_A_DRAFT.md`; do not overwrite the audited theorem manuscript merely to satisfy journal style.

Presentation choices:

- Introduction should begin with detector A fast / detector B slow and one unknown-arrival window.
- Explain covariance physically: near-one correlation means neighboring trial arrival times are almost the same trial; near-zero means another distinct chance for noise to mimic the pulse.
- Explain the finite witness physically before presenting Rice/Slepian mathematics: the slow detector's entire continuous search is bounded below the allowed false-alarm rate, while only seven separated fast-detector trials already exceed it.
- Explain the crossover theorem before the formal proof: fast wins at zero timing uncertainty; fast reaches its search-limited failure point first as `L` grows; continuity forces a crossing.
- Keep the full-scan Monte Carlo explicitly labeled as an asymptotic/full-template robustness check, not a finite-time crossover theorem.
- Keep the first-order detector corollary because it answers the objection that the effect is unique to the engineered double-pole construction.
- Do not add a numerical `T_G(L)` crossover curve unless a new scientific reason justifies reopening the finite-window rough-process problem.

## Rendered-manuscript status

The device-engineer rewrite has been compiled locally into a **14-page letter-size PDF** and visually inspected.

Current render disposition:

```text
LATEX COMPILE: PASS
CROSS-REFERENCES: PASS
NO OVERFULL/UNDERFULL BOXES: PASS
TITLE/ABSTRACT READABILITY: PASS
FIRST-PAGE PHYSICAL MOTIVATION: PASS
CONCLUSION READABILITY: PASS
REPOSITORY REFERENCES IN MANUSCRIPT: ZERO
FIGURE SEMANTICS: UNCHANGED
```

The three analytical figures remain unchanged. The rewrite is principally conceptual/expository; it does not alter the theorem, continuum witness, first-order robustness result, or full-scan numerical check.

## Citation audit corrections

The final rendered source must preserve the corrected bibliography:

1. **Croce et al. 2004** — correct APS author order/list:

```text
R. P. Croce; Th. Demma; M. Longo; S. Marano; V. Matta; V. Pierro; I. M. Pinto.
```

2. **Milstein et al. 2008** — correct Applied Optics author list:

```text
Adam B. Milstein; Leaf A. Jiang; Jane X. Luu; Eric L. Hines; Kenneth I. Schultz.
```

For final citation metadata, use `PAPER_A_REFERENCE_AUDIT_2026-08-13.md` and the rendered LaTeX/PDF over stale older bibliography text where they conflict.

## Remaining blockers before real submission

Do **not** invent these fields. They require author confirmation:

1. author name(s), affiliation(s), and corresponding-author email;
2. Funding statement;
3. Disclosures/conflicts statement;
4. final Data Availability wording, with **no repository reference**;
5. final cover-letter placeholders and not-under-consideration confirmation.

## Current next phase

Before doing more theory, judge the manuscript as a detector engineer would:

1. Can the title be understood without reading the paper?
2. Does the abstract state the physical mechanism without specialist detection-theory jargon?
3. Does page 1 recover the simplicity of the original gedanken experiment?
4. Does the conclusion say what a detector engineer should change in how they think about response time?
5. Only after those pass should further physical-noise extensions be considered for inclusion.
