# External-Style Referee Review — Applied Optics Draft Rev. 2

**Date:** 2026-08-13  
**Manuscript:** `PAPER_A_APPLIED_OPTICS_DRAFT.md`, Rev. 2  
**Review posture:** significance, detector relevance, and readability only; technical theorem already audited separately

## Recommendation

**MINOR-TO-MODERATE REVISION BEFORE EXTERNAL SUBMISSION.**

The Rev. 2 architecture is materially better than the theorem-first manuscript. The physical mechanism is now understandable from the first two figures, the continuum feasibility bracket is shown before the general crossover theorem, and the source-matched transfer family is explicitly identified as an existence construction.

I no longer see a major readability defect. The remaining risk is editorial significance: because the paper contains no experimental detector data and deliberately uses an idealized channel family, an *Applied Optics* editor must be convinced that the result changes how an optical measurement should be specified or qualified.

---

## 1. Figures — PASS

### Figure 1

The accumulated-SNR plot immediately shows the known-arrival advantage of the faster channel. The solid/dashed distinction means the result does not depend on color.

**PASS.**

### Figure 2

This is the strongest conceptual figure. At the same physical uncertainty `L=9 tau_f`, the fast covariance is essentially exhausted while the slow covariance remains substantial. A detector reader can now see the origin of the larger normalized search without needing a Gaussian-process argument first.

**PASS.**

### Figure 3

The revised figure correctly uses direction arrows:

```text
slow point = upper bound, exact PFA may lie below;
fast point = lower bound, exact PFA may lie above.
```

The required `alpha=.05` line lies strictly between them. The different marker shapes plus labels again avoid dependence on color.

**PASS.**

Do not replace this with a bar chart; bars would visually imply exact probabilities.

---

## 2. Manuscript order — PASS

The result order is now appropriate for an applications journal:

```text
mechanism
-> finite continuum witness
-> general theorem
-> interpretation.
```

This is preferable to proving the asymptotic theorem before showing that the phenomenon occurs at a finite and comprehensible scale.

**PASS.**

---

## 3. Dimensional mapping — PASS WITH ONE CAVEAT

The sentence

```text
if tau_f=10 microseconds, then tau_s=60 microseconds and L=90 microseconds
```

makes the scale-free result intelligible.

Keep the explicit qualification that this is an illustration only. Do not associate these numbers with HgCdTe, InSb, APDs, or another detector technology without a separate physical model.

**PASS.**

---

## 4. Remaining significance risk — practical meaning of L

The paper should say explicitly what a finite arrival-time uncertainty interval can represent in a real optical measurement. Examples include:

- trigger or synchronization jitter;
- an asynchronous transient expected somewhere inside a gated record;
- a prior time-of-flight/range gate in active optical ranging;
- a finite search window established by another sensor or timing system.

This does not turn the theorem into an experiment. It tells the reader why `L/tau` is an experimentally meaningful quantity rather than a purely mathematical search length.

**REQUIRED BEFORE SUBMISSION.**

---

## 5. Remaining framing risk — abstract opening

The phrase

> “Photodetector response time is usually treated as an intrinsic speed advantage”

is broader than the theorem and invites an unnecessary objection. Response time is indeed a detector property, but system-level engineers already know that bandwidth can interact with noise and processing.

Prefer an opening tied exactly to the controlled comparison:

> “With eventual event-specific sensitivity held fixed, a shorter photodetector response time accelerates known-arrival transient measurements. When arrival time is uncertain, however, it also enlarges the normalized timing search.”

This states the paper's own result rather than caricaturing conventional practice.

**REQUIRED COPYEDIT.**

---

## 6. Remaining framing risk — why alpha=0.05 and r=6?

The continuum witness uses

```math
alpha=0.05,
\qquad
r=6.
```

A reviewer may ask whether these are supposed to be representative detector values.

They are not. They are a transparent witness chosen so that the continuous-time upper and lower bounds separate cleanly without invoking rare-event or timing-grid numerics.

State this explicitly near the parameter choice:

> “The values are chosen for an analytically transparent finite-scale witness, not as a recommended false-alarm specification or a representative detector pair.”

This is especially important because a 5% global false-alarm probability is high for many sensing systems.

**REQUIRED BEFORE SUBMISSION.**

---

## 7. Physical channel interpretation

The paper now correctly calls `G_tau` an existence construction and notes that its impulse response can be nonnegative.

One extra sentence would help an optics audience:

> “Here `G_tau` is interpreted as the linear small-signal optical-to-electrical channel for the selected event; the construction isolates temporal response rather than a particular microscopic transport mechanism.”

This makes clear what input/output the transfer function connects.

**RECOMMENDED.**

---

## 8. Abstract length and journal form

The Rev. 2 abstract is approximately 93 words, consistent with the Optica style guide's approximately 100-word target.

The manuscript now follows the conventional Introduction / Model / Results / Discussion / Conclusion architecture. Figure callouts are ordered. Funding, Disclosures, and Data Availability sections are present as placeholders rather than fabricated statements.

**PASS FOR PRE-SUBMISSION DRAFT.**

---

## 9. Novelty/significance assessment

The paper is not persuasive if framed as a discovery of search penalties, correlation-dependent thresholds, or sensitivity-speed tradeoffs. Those are established.

It is potentially persuasive if framed as a detector-qualification result:

> Two detector channels can have deliberately equalized eventual event sensitivity yet still lack a detector-only ordering for an unknown-arrival task because detector response time controls both the evidence clock and the nuisance-search geometry.

The value is conceptual and operational: it identifies the additional task information needed before “faster” can be translated into “reaches this detection operating point sooner.”

I would not use novelty or priority language.

---

## 10. Final referee disposition after listed edits

After the three framing edits above:

```text
TECHNICAL SOUNDNESS: PASS from prior audit
READABILITY: PASS
FIGURE LOGIC: PASS
DETECTOR RELEVANCE: PASS WITH EXPLICIT PRACTICAL L INTERPRETATION
APPLIED OPTICS FIT: PLAUSIBLE
NOVELTY: NOT ESTABLISHED
EDITORIAL SIGNIFICANCE RISK: MODERATE, NOT FATAL
```

At that point I would stop internal rewriting and move to a real manuscript package / independent human-style review rather than further mathematical development.