# Experiment 09 — Journal strategy after Rev. 3

**Date:** 2026-08-14  
**Status:** FIRST TARGET SELECTED / JOURNAL FIT IS A STRATEGY DECISION, NOT A SCIENTIFIC CLAIM

## Recommended first target

### Physical Review A — Regular Article

Current PRA scope explicitly includes:

```text
quantum science;
quantum technologies;
quantum hardware, engineering and technologies;
quantum sensing;
open quantum systems and decoherence;
quantum thermodynamics;
quantum optics and coherent light-matter interfaces.
```

Experiment 09 is a theoretical open-system/quantum-detector paper rather than a material-specific device proposal. Its closest literature is already concentrated in PRA/quantum-optics/open-system venues, including Young et al. 2018 and Shammah et al. 2017.

The most natural requested PRA section is therefore:

```text
A-3E Quantum Technologies
```

because the object is a detector/hardware scalability theorem. Secondary editorial fits are A-1E Fundamental Concepts (open quantum systems/decoherence) and A-8E Quantum Optics.

### Article type

Use a **Regular Article**, not a PRA Letter by default.

Reason:

- PRA Regular Articles have no length limit and may still be concise.
- PRA Letters are limited to 4500 words and are intended for important results whose current interest/significance justifies accelerated handling.
- Experiment 09 has a coherent narrow theorem but novelty remains unestablished and the model is abstract. Compressing it into a Letter would increase the editorial-significance burden without scientific benefit.

A short Regular Article is therefore the more defensible first submission architecture.

---

## Fallback

### Physical Review Applied — Regular Article

PRApplied is clearly in scope for:

```text
device physics;
optics/optoelectronics/photonics;
quantum information science and technology.
```

Its acceptance criterion emphasizes fresh insight into **applications-based physical phenomena**. Experiment 09 currently lacks a concrete material implementation, so this criterion creates a larger editorial risk than PRA.

PRApplied becomes more attractive if a later revision adds a physically grounded detector realization without requiring experimental work.

---

## Aspirational / not recommended first

### PRX Quantum

In scope, including open quantum systems, quantum hardware, quantum thermodynamics, and photon detectors, but explicitly highly selective and aimed at exceptional advances/connections/capabilities/insights with broad impact.

Current Experiment-09 significance does not justify choosing this bar as the first submission strategy.

### Quantum Science and Technology

Also in scope for quantum engineering/sensing and theory, but highly selective; published work is expected to be essential reading for a subfield and of broader lasting impact.

Again, not the best first target for the current model-specific theorem.

---

## Manuscript architecture consequence

Prepare a PRA-oriented Rev. 4 as a concise Regular Article.

### Main text

1. Introduction — established coherent detector architecture; Young 2020 and Bassler 2026 made central.
2. Minimal detector model and exact two-rate kernel.
3. Extensive internal-event count lift and fixed-efficiency task.
4. Main scalable-efficiency theorem under bounded local coupling.
5. Compact rate-scaling table / physical interpretation.
6. Gated reverse-injection floor as a secondary result.
7. Discussion / limitations / relationship to prior work.
8. Conclusion.

### Appendices

A. Exact finite-N solution.
B. Asymptotic rate-scaling coefficients.
C. Critical balanced logarithmic boundary.
D. Bounded-local-coupling matrix proof.
E. Gated reverse-injection derivation.

The paper must stand alone without Supplemental Material. Numerical scripts remain available for reproducibility.

---

## Claim discipline

Do not call the result:

```text
fundamental limit;
new quantum detector architecture;
new decoherence phase transition;
quantum advantage;
universal photodetector bound.
```

The narrow contribution remains:

> an efficiency-selected scaling theory for accepted internally generated local events when dark-to-bright isolation is imperfect in a coherence-selective detector, together with a bounded-microscopic-coupling ceiling on scalable internal collection efficiency.

---

## Next action

Create `PAPER_DRAFT_REV4_PRA_2026-08-14.md`, then audit its references and generate/QA the three theory figures before LaTeX rendering.
