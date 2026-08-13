# Detector-Facing Paper Architecture — Task-Dependent Fast/Slow Ordering

**Date:** 2026-08-12  
**Status:** CONSOLIDATION / PAPER ARCHITECTURE / NOVELTY NOT ESTABLISHED / MATHEMATICAL COMPANION SEPARATED. The forty-nine-step Gaussian-extremes closure branch is finished and must not be restarted by default. This document compresses the surviving detector/detection-theory result into a short paper architecture. The novelty burden is placed only on the complete equal-eventual-SNR, unknown-arrival ranking-reversal construction identified as a possible synthesis contribution in `PRIOR_ART_AUDIT_DETECTOR_TASK_REVERSAL.md`.

---

## 1. Paper thesis

The paper should **not** claim that conventional specific detectivity `D*` is newly shown to be incomplete for pulsed detection. That is established prior art.

The paper should **not** propose a new scalar sensitivity-speed product.

The paper should **not** claim that faster detectors are generally worse.

The paper-level thesis is narrower:

> **Under a specified global-false-alarm, unknown-arrival matched-filter scanning protocol, equal eventual matched-filter sensitivity does not define a detector-only fast/slow ordering. In a controlled time-scaled photodetector family, shortening the detector time scale accelerates evidence accumulation but also shortens the timing-search correlation length. These competing effects produce a task-dependent fast/slow detection-time boundary, including at least one fast-to-slow crossover under the stated assumptions.**

This is a **task/protocol theorem and counterexample to detector-only ordering**, not a universal theorem about detector speed.

---

## 2. Recommended title

Primary working title:

> **Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity**

Descriptive subtitle if the target journal permits one:

> **Unknown arrival time can reverse fast/slow detection ranking under a global false-alarm constraint**

Avoid titles such as:

```text
Why faster photodetectors are worse
A new detectivity metric
The fundamental speed-sensitivity limit
Beyond D*: a universal metric
```

because the repo does not support those claims.

---

## 3. Abstract skeleton

The abstract should contain only four logical moves.

### Sentence 1 — established context

Conventional specific detectivity is useful for stationary/reference-condition sensitivity, while pulsed detection and sensitivity-bandwidth tradeoffs are already known to require temporal/spectral information.

### Sentence 2 — actual question

Ask whether two detector channels with the **same eventual matched-filter SNR** but different response times are nevertheless ordered for a finite-time task when event arrival is unknown.

### Sentence 3 — main result

For a controlled time-scaled Gaussian family, derive

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
}
```

and show that the fast member wins at known/low timing uncertainty, while the larger normalized timing-search burden can produce at least one fast-to-slow crossover and a slow-only feasibility region.

### Sentence 4 — scope

State explicitly that the result is protocol- and task-specific: it does not imply that slower photodetectors are generally superior and does not introduce a universal replacement for `D*`.

No Pickands, Palm, Rice, or endpoint-certificate material belongs in the abstract.

---

## 4. Main-text structure

Target a short conceptual/theoretical paper: approximately **5 main sections**, with the central mathematics visible and the specialized closure material removed.

### Section I — What detector metric is being asked to do?

Purpose: frame the problem without pretending the first ingredients are new.

Keep only three points:

1. Scalar `D*` is a reference sensitivity measure and does not by itself specify arbitrary pulse detection; cite Jones and modern characterization literature as prior art.
2. For a known deterministic waveform under the restricted full-observation stationary-Gaussian problem, the optimal SNR can be written as a spectral overlap involving `D*(f)`; present this as background/derivation, not novelty.
3. The paper asks a different question: **does equal eventual sensitivity order two detectors for a finite-deadline, unknown-arrival decision task?**

The all-pass finite-window counterexample can be reduced to one paragraph or a short appendix. It is conceptually useful but is not the novelty-bearing result.

End Section I with the controlled comparison:

```math
\rho_{f,\infty}=\rho_{s,\infty}=\rho_0,
\qquad
\tau_f<\tau_s.
```

The construction deliberately removes eventual-SNR advantage so that temporal scaling itself is isolated.

---

### Section II — Controlled equal-eventual-SNR detector family

Use the Step-11 family because it is analytically clean:

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

with normalization chosen so that

```math
\rho_{\tau,\infty}=\rho_0
```

for every `tau`.

Define

```math
x=t/\tau.
```

The finite-time squared-SNR fraction is

```math
\boxed{
\eta(x)=1-e^{-2x}(1+2x+2x^2),
}
```

hence

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
}
```

This establishes the intuitive side of the competition:

```text
smaller tau -> evidence is accumulated earlier in physical time.
```

Then define the unknown-arrival interval `L`, allowed global false-alarm probability `alpha`, and required true-alignment detection probability `beta`.

For the finite matched-filter scan, introduce the exact dimensionless covariance

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}dv
}{
\int_0^x v^2e^{-2v}dv
},
\qquad 0\le y<x,
}
```

with `R_x(y)=0` for `y>=x`.

The key physical scaling is

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

Thus smaller `tau` also compresses the timing-search correlation length.

End Section II with one sentence:

> Speed changes **both** the rate at which signal evidence is accumulated and the statistical geometry of the unknown-arrival search.

That is the mechanism the rest of the paper formalizes.

---

### Section III — Detection time is a task surface, not a detector scalar

Define the dimensionless timing-search length

```math
\ell=L/\tau.
```

Let

```math
\Gamma(x,\ell,\alpha)
```

be the exact `(1-alpha)` quantile of the supremum of the normalized Gaussian timing scan over `[0,ell]`.

The true-alignment decision margin is

```math
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
```

Define

```math
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\left\{
x>0:
M(x;\ell,\rho_0,\alpha)
\ge\Phi^{-1}(\beta)
\right\}.
```

Then the central scaling relation is

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

This equation should be visually prominent. It contains the entire detector/task tension:

```text
smaller tau
-> multiplies the decision-time scale downward

but

smaller tau
-> increases L/tau
-> enlarges the normalized timing-search problem.
```

Also retain the Step-11 result that, for one fixed detector in this family, the decision margin increases with integration duration. Therefore the cross-detector reversal is **not** caused by one detector using a self-suboptimal integration time.

---

### Section IV — Central theorem: task-dependent fast/slow reversal

This is the novelty-bearing center of the paper.

#### Theorem / Proposition — Equal-eventual-SNR task reversal

Consider two members of the family with

```math
\tau_f<\tau_s,
\qquad
r=\tau_s/\tau_f>1,
```

and equal eventual SNR `rho_0`. Define timing uncertainty in slow-detector units,

```math
\ell=L/\tau_s.
```

Then

```math
T_{D,f}
=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}
=r\tau_f X_D(\rho_0,\alpha,\beta,\ell).
```

Hence the preference boundary is

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)
=0.
}
```

Under the continuity/divergence assumptions stated explicitly in Step 12:

```text
L=0:
    fast detector reaches the required decision first;

as L approaches the fast detector's feasibility boundary:
    fast detection time diverges while the slow detector remains feasible;

therefore:
    at least one finite fast-to-slow crossover exists.
```

Define

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)
<\rho_0-\Phi^{-1}(\beta)\}.
```

Then

```math
\boxed{L_{crit}(\tau)=\tau\ell_{crit}.}
```

So, for equal eventual SNR,

```math
L_{crit,s}/L_{crit,f}=\tau_s/\tau_f=r.
```

This gives the exact feasibility partition:

```text
small L:
    both feasible, fast wins;

intermediate L:
    both feasible, with at least one fast/slow crossover;

larger L:
    slow-only feasibility is possible;

still larger L:
    neither is feasible.
```

A fast-only feasibility region is excluded in this constructed family.

#### Required qualification in theorem statement

The theorem must say that the existence result is conditional on the standard continuity/extreme-value properties used in Step 12. Do not hide this qualification in supplemental text.

No claim of crossover uniqueness should appear.

---

### Section V — Interpretation and limits

The discussion should return immediately to photodetectors.

Core interpretation:

```text
Detector speed is not merely a bandwidth/signal-rise-time parameter once arrival time is uncertain.
It also rescales the nuisance-parameter search.
```

Then state what the theorem does and does not say.

It **does say**:

- equal eventual matched-filter sensitivity does not produce a detector-only ordering for the stated finite-time task;
- the task has a dimensionless search parameter `L/tau`;
- faster response can lose its early-evidence advantage when the global search burden is large enough;
- detector comparison therefore requires the measurement protocol and timing uncertainty, not only a device scalar.

It **does not say**:

- slower detectors are generally better;
- the chosen scan is Bayes/minimax/sequentially optimal among all unknown-arrival decision rules;
- a new universal sensitivity-speed metric has been found;
- the crossover is unique;
- the result automatically extends to nonlinear response, signal-dependent noise, dead time, saturation, unknown amplitude/phase, or nonstationarity.

End with the practical message:

> Detector specifications can rank devices only relative to a specified measurement task. Under timing uncertainty, the relevant task variables include not only eventual sensitivity and response time, but also the size of the arrival-time search and the allowed global false-alarm probability.

---

## 5. Figure plan

Keep the main paper to **three figures maximum**.

### Figure 1 — Thought experiment and competing effects

Two equal-eventual-SNR detector responses with `tau_f<tau_s`.

Left: normalized signal accumulation versus physical time.

Right: corresponding timing-scan covariance versus physical lag, showing the fast detector's narrower correlation length.

One visual should communicate:

```text
fast -> earlier evidence
fast -> more timing-search resolution
```

No extreme `1 ns` versus `1 s` hardware implication should be attached to the illustration.

### Figure 2 — Dimensionless detection-time surface

Plot or schematic of

```math
T_D/\tau=X_D(\rho_0,\alpha,\beta,L/\tau).
```

Show how one detector comparison corresponds to evaluating the same task surface at two different normalized search lengths, `ell` and `r ell`.

This is the conceptual centerpiece and should replace many of the specialized numerical plots generated in Steps 13–49.

### Figure 3 — Task-regime diagram

A clean regime schematic or numerically validated phase diagram:

```text
fast preferred
    -> crossover boundary
slow preferred while both feasible
    -> slow-only feasible
    -> neither feasible.
```

If numerical curves are used, regenerate them from a validated continuum calculation. **Do not reuse the invalidated Step-13 rough-grid crossover or the Step-44 knife-edge as the primary evidence.**

The theorem itself establishes the qualitative regime sequence without requiring a visually precise knife-edge endpoint.

---

## 6. What belongs in appendices versus the separate companion

### Main-paper appendix material

Only short derivations directly needed to make the central theorem self-contained:

- normalization giving equal eventual SNR;
- derivation of `eta(x)`;
- derivation of `R_x(y)`;
- proof that the one-detector margin increases with filter duration;
- proof of the feasibility partition and crossover existence;
- optional one-page all-pass finite-window counterexample.

### Separate technical companion / repository track

Steps 13–49 should **not** be compressed into the main paper. They form a different mathematical project:

```text
rough hard-window Gaussian extrema
finite information bandwidth
Rice/Palm corrections
Pickands and Brownian-parabola limits
excursion-cluster estimators
Cameron-Martin threshold translation
finite-grid concentration
Brownian bridge/discrete-Pickands correction
exact-covariance grid-transfer diagnostics.
```

Their role is robustness/stress testing of a difficult continuous-search witness, not the conceptual foundation of the detector theorem.

A paper can cite a technical companion or repository note for these checks without forcing a detector reader through them.

---

## 7. Prior-art placement in the paper

The Introduction should proactively concede the established ingredients.

### Cite as prior art, not discoveries

- Jones 1960: pulse/energy detectivity derived from frequency-dependent detector sensitivity.
- Garcia & Dereniak and modern detector-characterization literature: speed/bandwidth is a separate detector attribute; sensitivity-speed products already exist.
- Vio/Andreani, Morras et al., Croce et al.: unknown-location matched-filter searches have correlated-peak/global-false-alarm penalties controlled by template correlation/effective trial rate.
- Standard all-pass/system theory: phase can change temporal placement while preserving magnitude response.

### Novelty burden

Only this complete synthesis remains a possible contribution:

```text
equal eventual matched-filter SNR
+ detector time-scale change
+ one fixed physical unknown-arrival interval
+ one global false-alarm requirement
+ finite-time evidence accumulation
+ time-scale-dependent search correlation
-> explicit fast/slow task boundary and reversal.
```

Use wording such as:

```text
"We study..."
"We construct..."
"We show within this family..."
"To our knowledge" only after a deeper literature audit.
```

Do not use `novel`, `first`, or `previously unknown` based on the present focused audit.

---

## 8. What the paper should omit entirely

Do not put the following in the detector-facing main narrative unless a reviewer explicitly asks:

- Step-13 `ell~49` estimate;
- the invalidated upper Rice switch;
- generalized Pickands crossover details;
- coupling coefficient corrections;
- Step-27 raw tiny-chi values;
- micro-upcrossing failure analysis;
- `R~1.56` finite-u tangent amplitude issue;
- occupation-Palm concentration machinery;
- `L0=.02` truncation engineering;
- Step-44 finite-grid endpoint knife-edge;
- witness retuning at `X=7.5–7.7`;
- discrete-Pickands numerical correction tables;
- exact-covariance grid-transfer Monte Carlo tables.

These are important research records and technical stress tests, but they are not the shortest path by which a photodetector reader understands the result.

---

## 9. Publication claim ladder

Use the following hierarchy when drafting.

### Safe / established

```text
Scalar reference D* is not a complete description of arbitrary temporal detection.
```

But cite prior art immediately.

### Derived in this project

```text
For the controlled equal-eventual-SNR family,
T_D=tau X_D(rho0,alpha,beta,L/tau).
```

### Strongest theorem-level result to foreground

```text
Under the stated global-PFA scan and continuity/extreme-value assumptions,
there is at least one finite fast-to-slow detection-time crossover as physical timing uncertainty increases, and a slow-only feasibility region is possible while fast-only feasibility is excluded in the equal-eventual-SNR scaled family.
```

### Possible contribution, not yet novelty claim

```text
Applying this construction explicitly to photodetector temporal-response comparison and using it to show that equal eventual sensitivity does not define a task-independent fast/slow ordering.
```

---

## 10. Recommended paper length and emphasis

A detector-facing manuscript should be short enough that the central result cannot be lost:

```text
Introduction / prior art                  ~1 page
Controlled detector family               ~1 page
Detection-time surface                    ~1 page
Task-reversal theorem + regime structure  ~1–1.5 pages
Discussion / limitations                  ~1 page
Appendices                                as needed
```

The paper should read as a **thought experiment sharpened into a task theorem**, not as a probability-theory paper with a photodetector example attached.

---

## 11. Architecture disposition

The project is now cleanly divided:

```text
Paper A / main detector result:
    Steps 01–12
    + prior-art audit
    + task-reversal theorem

Technical companion:
    Steps 13–49
    + failed paths
    + continuous-time false-alarm stress tests
    + specialized Gaussian-extreme closure work.
```

The next drafting step should stay inside Paper A.

### Single next question

> Can the central theorem, abstract, and opening two pages now be drafted in publication-style language from this architecture, while preserving the explicit novelty and scope restrictions above?
