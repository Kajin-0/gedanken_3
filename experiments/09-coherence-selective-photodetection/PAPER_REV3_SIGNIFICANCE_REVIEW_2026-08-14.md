# Final significance review — Experiment 09 Paper Rev. 3

**Date:** 2026-08-14  
**Manuscript:** `PAPER_DRAFT_REV3_2026-08-14.md`  
**Review posture:** skeptical editor/referee assessing whether the surviving result warrants a concise theory paper  
**Disposition:** **PROCEED TO FIGURES AND JOURNAL-FACING PREPARATION / NO FATAL TECHNICAL DEFECT IDENTIFIED / NOVELTY STILL NOT ESTABLISHED / SIGNIFICANCE PLAUSIBLE ONLY UNDER NARROW CLAIM**

---

# 1. What Rev. 3 now claims

Rev. 3 no longer claims any of the following as new:

```text
coherent collective photodetectors;
bright/dark-state detector manifolds;
static 1/N projection of incoherent noise;
local-dephasing bright/dark transfer;
collective-versus-decoherence scaling regimes;
generic detector thermodynamic tradeoffs.
```

Those are appropriately assigned to established literature.

The surviving paper claim is narrower:

> In a coherence-selective detector with extensive independent internal local-generation processes, choose the measurement gate by a prescribed conditional internal signal-collection efficiency. If useful bright extraction and local dephasing scale with detector size and the counted coupling per microscopic state is bounded, the accepted internal-dark burden has a constrained scaling structure that produces a piecewise scalable-efficiency ceiling.

The central result is

```math
\eta_{sc}
=
\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta,
\end{cases}
```

under `0<=alpha<=1` from the bounded-local-coupling resource assumption.

The detailed gate/dark-burden laws provide the proof and approach to this ceiling.

---

# 2. Why this is not killed by Young et al. 2020

Young, Sarovar, and Leonard already propose coherently interacting nanoscale detector elements and derive conditions for high/ideal performance. Their ideal-efficiency condition explicitly includes the requirement that relaxation processes not couple dark states back into the optically active manifold.

That precedent is extremely close and should remain prominent.

However, the screened paper does not answer the present question:

```text
What accepted internal-dark burden results when dark-to-bright isolation is violated,
when the gate is selected by a required collection efficiency,
and when useful/decohering rates scale with system size?
```

Rev. 3 is therefore best viewed as a **quantitative failure/scalability theory for one ideal condition in an established coherent detector architecture**, not as an independent architecture proposal.

That is a legitimate scientific niche.

---

# 3. Why this is not killed by Bassler et al. 2026

Bassler, Lyne, and Cuerda derive large-`N` scaling regimes in Dicke superradiance under local dephasing and spontaneous emission. They clearly own the broad statement that competition between collective dynamics and local decoherence creates different large-system scaling sectors.

Rev. 3 survives only because its observable and operational constraint are different:

```text
Bassler et al.:
    collective emission observables / many-body coherence scaling;

Experiment 09:
    minimum gate fixed by detector collection efficiency
    -> integrated number of accepted internally generated local events.
```

The resulting bounded-coupling no-go and scalable-efficiency ceiling are detector-specific consequences, not a claim of new Dicke scaling theory.

The manuscript should continue to use “scaling laws,” “scalability boundary,” or “efficiency ceiling” rather than presenting the result as a new thermodynamic or many-body phase transition.

---

# 4. Technical status

I find no new algebraic contradiction in the following chain:

1. exact permutation-symmetric one-body equations;
2. exact one-event signal/local-dark collection kernels;
3. explicit independent-particle Poisson lift for extensive local generation;
4. minimum gate selected by fixed `eta`;
5. `kappa_N~N^alpha`, `gamma_N~N^beta` asymptotic classification;
6. positive-matrix trace bound giving `alpha<=1` under bounded local counted coupling;
7. resulting scalable-efficiency ceiling;
8. corrected gated reverse-injection scaling.

The critical balanced boundary should continue to be claimed at scaling level (`Theta` with logarithms) rather than as a precision finite-`N` Lambert-W approximation.

---

# 5. Strongest detector consequence

The most useful physical statement is not the full five-row table. It is:

> **Under bounded counted coupling per microscopic state, any fixed operating point that strictly requires slow dark-manifold recycling incurs at least an `O(N)` accepted local-dark burden.**

This creates the ceiling:

```text
extraction scaling wins:
    any fixed eta<1 can remain scalable;

balanced rate scaling:
    scalable efficiency is limited by the fast branching fraction;

dephasing scaling wins:
    no fixed positive efficiency can remain scalable.
```

This statement is simple enough to be useful outside the derivation and specific enough not to duplicate generic coherence/decoherence theory.

---

# 6. Thermodynamic supporting result

The corrected efficiency-gated reverse-injection law strengthens the manuscript's honesty:

```text
fast branch:        O(1) reverse burden at fixed affinity;
balanced boundary:  O(log N);
strict slow branch: O(N).
```

This prevents the paper from falsely claiming a free asymptotic advantage while also correcting the earlier overstatement that any collective forward enhancement automatically forces a `kT ln N` affinity increase in the gated detector.

The thermodynamic section should remain secondary.

---

# 7. Main editorial risks that remain

## A. Model abstraction

The independent-particle lift is an ideal low-density kinetic limit. No concrete semiconductor/exciton architecture is demonstrated to realize it together with the required coherent bright state and collective extractor.

This limits the paper's reach but does not invalidate a Gedanken/theory article if stated clearly.

## B. Mathematical simplicity

Once the model is specified, the asymptotic exponents are not extraordinarily difficult to derive. The paper's significance rests on the detector formulation and resource interpretation, not mathematical sophistication.

## C. Novelty remains unproven

The focused searches are strong enough to justify writing, not priority language. A deeper citation-network/patent search could still find a closer theorem.

## D. Same-mode optical background

The mechanism does not suppress same-mode background photons. The title/abstract must remain explicitly about **internal** dark counts/events.

---

# 8. Recommended paper format

A concise theory paper is now justified.

Recommended main-text structure:

```text
1. Introduction / closest architecture and exact narrow question
2. Minimal model and exact kernel
3. Fixed-efficiency extensive local-generation task
4. Main scalable-efficiency theorem + bounded-coupling no-go
5. Supporting scaling laws and reverse-injection floor
6. Discussion / prior art / limitations
7. Conclusion
```

Use appendices/supplement for:

- full finite-`N` kernel algebra;
- asymptotic coefficients in every alpha/beta sector;
- critical Lambert-W boundary derivation;
- general covariance and parallel detailed-balance derivations.

---

# 9. Figure gate

Figures are now scientifically justified.

Recommended set:

### Figure 1 — Gedanken detector and two clocks

Show:

```text
coherent photon bright state
vs local internal event;
bright extraction kappa_N;
local dephasing gamma_N;
fast counted route;
slow dark-manifold recycling route.
```

### Figure 2 — exact finite-N scaling verification

Log-log exact `mu_loc,N` versus `N` for representative rate sectors, with asymptotic slopes:

```text
alpha>beta:        -alpha
balanced below:    -s
balanced above:    2-s
alpha<beta:        2-alpha.
```

Include one balanced-boundary curve if legible.

### Figure 3 — scalable-efficiency ceiling / regime map

A simple `(alpha-beta, eta)` conceptual map showing:

```text
alpha>beta: eta_sc=1;
alpha=beta: eta_sc=q0;
alpha<beta: eta_sc=0.
```

Use the detailed power-law table as an inset or companion panel rather than making the reader reconstruct the headline theorem from equations alone.

---

# 10. Journal-level assessment

At this stage I would not target a broad high-impact general-physics journal. The result is too model-specific and the closest prior art too strong.

Plausible eventual homes are journals receptive to concise theoretical quantum-detector / applied quantum optics work. Journal selection should be done only after figures and a final citation-production audit.

---

# 11. Final disposition

```text
MATHEMATICAL CONSISTENCY: PASS AT CURRENT AUDIT LEVEL
MODEL CLAIM SCOPE: PASS
FAILED REV. 0 CLAIMS: NOT REVIVED
YOUNG 2020 PRIOR ART: EXPLICITLY INCORPORATED
BASSLER 2026 PRIOR ART: EXPLICITLY INCORPORATED
SCALABLE-EFFICIENCY THEOREM: RETAIN
BOUNDED-COUPLING NO-GO: RETAIN
GATED REVERSE-INJECTION RESULT: RETAIN AS SUPPORTING
SAME-MODE BACKGROUND LIMITATION: RETAIN PROMINENTLY
NOVELTY: NOT ESTABLISHED
SIGNIFICANCE: PLAUSIBLE FOR CONCISE THEORY PAPER
NEXT: FIGURES + FINAL CITATION AUDIT + JOURNAL-FACING REVISION
```

**Do not open Experiment 10.** Rev. 3 has crossed the threshold where manuscript production is now the rational next use of effort.
