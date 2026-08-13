# External-Style Referee Review — Applied Optics Draft

**Date:** 2026-08-13  
**Manuscript:** `PAPER_A_APPLIED_OPTICS_DRAFT.md`  
**Review posture:** skeptical optics/detector reviewer, not continuation of the derivation

## Recommendation

**MAJOR REVISION FOR PRESENTATION AND SIGNIFICANCE; NO FATAL TECHNICAL DEFECT IDENTIFIED.**

The manuscript contains a logically coherent result and a much stronger continuum witness than the earlier grid-based calculations. I do not see a reason to reopen the Step-13–49 Gaussian-extremes branch. The main publication risk is whether the result is sufficiently detector-relevant and distinct from classical acquisition theory to justify a full research article.

---

## 1. What I think the paper actually contributes

The strongest defensible contribution is:

> In a controlled causal detector-channel family with equal event-specific eventual matched-filter SNR, changing the detector response time rescales both the finite-time evidence clock and the normalized unknown-arrival search. Under one global-false-alarm batch protocol this produces a sufficient-guarantee-time ordering that is fast-favored at known arrival but becomes slow-only feasible at larger physical timing uncertainty.

That is narrower than:

- “`D*` is incomplete”;
- “speed and sensitivity trade off”;
- “unknown arrival creates a search penalty”;
- “matched-filter thresholds depend on correlation”; or
- “acquisition time depends on search size.”

All of those are already known.

The manuscript now mostly respects this boundary.

---

## 2. Strongest part — the continuum witness

The new witness is the paper's most convincing result:

```math
\rho_0=3.5,
\quad
\alpha=0.05,
\quad
\beta=0.90,
\quad
r=6,
```

and

```math
L=9\tau_f=1.5\tau_s.
```

At this same physical timing uncertainty,

```math
P_{FA,s}\le0.0336428<0.05<0.0624701\le P_{FA,f}.
```

This avoids the rough finite-window grid pathology entirely.

The slow result is a genuine continuous-time upper bound from the endpoint event plus Rice mean upcrossings. The fast result is a genuine lower bound because a seven-point sampled maximum is contained in the continuous supremum, and Slepian comparison lower-bounds that sampled exceedance probability by the equicorrelated comparison process.

This should be presented as a **result**, not buried as validation.

---

## 3. Major concern — the detector family is deliberately source-matched

The transfer function

```math
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2}
```

cancels the pole of the selected optical event

```math
P(s)=1/(s+b).
```

This is mathematically legitimate for an existence construction, but an optics reviewer can reasonably ask:

> Why should this be called a photodetector result rather than a deliberately engineered linear-channel counterexample?

The manuscript must answer this directly.

Required presentation:

1. State that the theorem is an **existence counterexample to detector-only ranking**, not a generic model of HgCdTe, InSb, photodiodes, APDs, etc.
2. Keep the nonnegative impulse-response observation `b>=1/tau_f`; it materially improves physical plausibility.
3. Explain that the purpose of the pole-zero choice is to hold the optical input fixed while producing an exactly time-scaled output family whose eventual matched-filter SNR can be equalized analytically.
4. Do not imply that real detector responsivity and noise can be varied independently without physical constraints.

If this is not stated prominently, the paper will look over-engineered.

---

## 4. Major concern — equal eventual SNR is not equal D*

The paper originated from an equal-`D*` thought experiment, but the theorem does not compare equal-`D*` detectors. It compares channels with equal **event-specific eventual matched-filter SNR**.

This is scientifically cleaner, but the distinction must remain explicit from the title/abstract onward.

I would remove any implication that the theorem itself proves something about two equal-conventional-`D*` detectors. The Introduction can motivate why task-level metrics are needed, but the formal result is an equal-`rho_0` construction.

The Applied Optics draft now handles this substantially better than the older manuscript.

---

## 5. Major concern — practical relevance needs one dimensional mapping

The theory is scale-free. That is useful mathematically but makes the result look abstract.

The continuum witness should immediately be translated once into dimensional language. For example:

```text
If tau_f = 10 microseconds,
then tau_s = 60 microseconds
and the witness occurs at L = 90 microseconds.
```

Equivalently, any common scale can be used. This must be labeled an illustration, not a claim about a particular material system.

This single sentence would make `L/tau` much easier for detector readers to interpret.

---

## 6. Major concern — the manuscript still reads too much like a theorem note

Applied Optics asks for applications-centered research with enough detail for reproducibility. The draft is much improved, but Sections 3.1–3.2 still lead with mathematical machinery.

Recommended narrative order inside Results:

1. **Physical mechanism:** fast accumulates evidence sooner but searches more timing structure.
2. **Concrete continuum witness:** show a finite physical regime where slow is feasible and fast is not.
3. **General theorem:** show that this is not an isolated point and prove at least one crossover.

This reverses the current order of Sections 3.2 and 3.3.

For an optics audience, show the phenomenon first, then prove the general statement.

---

## 7. Figure requirements

I would consider the paper difficult to publish without figures. Three figures are sufficient.

### Figure 1 — accumulated evidence

Plot

```math
\sqrt{\eta(t/\tau)}
```

against physical `t/tau_f` for `tau_f` and `tau_s=6 tau_f`.

This makes the fast known-arrival advantage visually undeniable.

### Figure 2 — timing covariance over one physical uncertainty interval

Plot

```math
R_\tau(\Delta)
=\left(1+|\Delta|/\tau\right)e^{-|\Delta|/\tau}
```

for the same pair in physical lag units and indicate the common interval `L=9 tau_f`.

This should be the conceptual center of the paper: the fast detector resolves more timing structure across the same physical uncertainty interval.

### Figure 3 — feasibility bracket

Plot the required global PFA `alpha=0.05` and show only the one-sided statements

```math
P_{FA,s}\le0.0336428,
\qquad
P_{FA,f}\ge0.0624701.
```

Use arrows or inequality annotations. Do not plot either as an exact measured probability.

Do **not** include a smooth numerical `T_G(L)` crossover curve unless it is actually computed with justified continuum control.

---

## 8. Prior-art positioning — improved, but the novelty burden remains real

The manuscript now cites classical acquisition, optical CDMA, ladar, correlated matched-filter false alarms, and detector sensitivity-speed work.

That is necessary. It also makes the remaining contribution narrower.

A reviewer could still argue:

> This is a straightforward composition of known facts: temporal compression shortens correlation time; a larger normalized search raises a global threshold; therefore a speed ordering can reverse.

The best response is **not** to claim novelty more strongly. The best response is to make the exact detector-scaling theorem and the finite continuum bracket unusually transparent and useful.

The paper's value is likely conceptual clarification and task-level detector qualification, not a new branch of Gaussian-extreme-value theory.

---

## 9. Technical points checked

### 9.1 Equal-SNR normalization

For

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

```math
\int_0^\infty t^2e^{-2t/\tau}dt=\tau^3/4,
```

so

```math
A_\tau=2\rho_0\sqrt N/\tau^{3/2}
```

is correct under the stated covariance convention.

**PASS.**

### 9.2 Evidence fraction

```math
\eta(x)=1-e^{-2x}(1+2x+2x^2)
```

and

```math
\eta'(x)=4x^2e^{-2x}>0.
```

**PASS.**

### 9.3 Full-template covariance

```math
R_\infty(y)=(1+y)e^{-y}.
```

Near zero,

```math
R_\infty''(0)=-1,
```

which gives the stated Rice upcrossing intensity.

**PASS.**

### 9.4 Slow feasibility bound

A path with supremum above `c` either starts above `c` or has at least one upcrossing. Therefore

```math
P(\sup Z>c)
\le Q(c)+E[N_c^+]
```

is valid. With `ell=1.5` the stated numerical bound is below `0.05`.

**PASS.**

### 9.5 Fast infeasibility bound

Seven samples separated by `1.5` have off-diagonal covariance no greater than

```math
R_\infty(1.5).
```

The equicorrelated comparison vector therefore has larger covariance and a stochastically smaller maximum. Slepian yields the stated lower bound on fast-channel exceedance.

**PASS.**

### 9.6 Crossover claim

Fast wins at `L=0`; the fast guarantee time diverges at its physical feasibility boundary while the slow channel remains inside its feasible region. Under the stated continuity regularity, at least one crossing follows.

**PASS, existence only.**

---

## 10. Minor points

1. The Optica style guide suggests an abstract of approximately 100 words. The new abstract is close enough but should be counted after final copyediting.
2. Define `Q(c)=1-Phi(c)` at first use in Results.
3. Avoid switching between `T_wall` and `T_{wall}` styles.
4. Use one notation for the crossover: `L_x` or `L_\times`, not both.
5. Ensure every inequality in Figure 3 is visibly one-sided.
6. Add funding, disclosures, and data-availability statements before submission; placeholders are appropriate until author metadata are confirmed.
7. The title “Task-dependent photodetector ordering under unknown arrival time” is appropriately restrained and preferable to a title containing “reversal.”

---

## 11. Referee disposition

If submitted in the current journal-facing form **without figures and without a dimensional interpretation**, I would recommend major revision and could understand an editorial rejection for insufficient practical framing.

If the paper adds the three figures, moves the continuum witness ahead of the general crossover theorem in Results, and explicitly frames the transfer family as an existence construction, I would view the manuscript as technically sound and potentially appropriate for *Applied Optics*.

I would still not certify novelty from the present literature search.

### Next action

> Build the three figures, add one dimensional scale illustration, reorder Results so the continuum witness precedes the theorem, and then perform one fresh review focused solely on significance and readability.