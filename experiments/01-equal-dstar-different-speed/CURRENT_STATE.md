# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-13 10:58 EDT  
**Status:** **REV. 5 IS NOT A SUBMISSION CANDIDATE. THE ORIGINAL THEOREM REMAINS MATHEMATICALLY SOUND, BUT ITS CENTRAL ACQUISITION MECHANISM IS TOO CLOSE TO ESTABLISHED PRIOR ART TO CARRY A FULL RESEARCH ARTICLE. ACTIVE WORK IS NOW A NOVELTY-FIRST PHYSICAL-NOISE EXTENSION.**

The Step-13–49 Gaussian-extremes branch remains hard-stopped. Do not create Step 50 by default.

## Read next

1. `REV5_REJECTION_AND_RESEARCH_DISPOSITION_2026-08-13.md` — current publication/research decision
2. `PHYSICAL_NOISE_COUPLING_2026-08-13.md` — exact common-path cancellation and mixed-noise result
3. `RESPONSIVITY_SPEED_SCALING_2026-08-13.md` — exact responsivity-speed phase diagram
4. `MIXED_NOISE_FINITE_PULSE_2026-08-13.md` — finite optical pulse + mixed-noise information spectrum
5. `PAPER_A_DRAFT.md` — preserved original theorem
6. `PAPER_A_FINAL_ADVERSARIAL_QA_2026-08-12.md` — historical theorem QA
7. `PROGRESS_LOG.md`

Do not resume by polishing the old manuscript.

---

# Publication decision

The device-engineer rewrite, Rev. 5, successfully made the original thought experiment understandable, but a subsequent hostile novelty review exposed the decisive issue:

> The unknown-arrival search penalty itself — shorter timing correlation, more effectively resolvable timing hypotheses, and a higher global false-alarm threshold — is established acquisition/detection theory.

Independent checks of radar/communications and radiation-detector timing literature support that criticism.

Therefore:

```text
REV. 5: DO NOT SUBMIT AS A FULL RESEARCH ARTICLE.
```

This is a novelty disposition, not a mathematical retraction.

The original theorem remains a valid controlled result and a useful pedagogical derivation.

---

# Original theorem — preserved claim boundary

Paper A established a crossover in a **sufficient batch guarantee time** for an equal-eventual-SNR detector family under unknown arrival time.

It did not establish:

- exact finite-time full-scan detection-time crossover;
- online/sequential optimality;
- crossover uniqueness;
- universal slow-detector superiority;
- equality with conventional scalar `D*`;
- novelty or priority.

The original continuum witness remains correct:

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

This historical result should not be promoted as a new acquisition principle.

---

# Conventional first-order replacement witness

The `unphysical pole-zero detector` criticism has been answered technically, although this does not rescue novelty.

Use one common exponential optical pulse with

```math
\tau_p=\tau_f,
```

and standard first-order detector transfer functions

```math
G_\tau(s)=\frac{R_{dc}}{1+s\tau}.
```

Take

```math
\tau_s=10\tau_f.
```

With the same downstream white-noise PSD `N`, the eventual matched-filter SNR is

```math
\rho_\infty^2
=\frac{R_{dc}^2}{2N(\tau_p+\tau)}.
```

Choose

```math
\frac{R_s}{R_f}
=\sqrt{\frac{11}{2}}
\approx2.34520788,
```

so both conventional first-order channels have exactly equal eventual matched-filter SNR for the same optical pulse.

For

```text
rho0 = 3.5
alpha = .05
beta = .90
```

the known-arrival first crossings are

```text
fast:  1.80519795247 tau_f
slow:  7.53280266002 tau_f
```

so fast wins strongly at known arrival.

At

```math
L=7.5\tau_f,
```

the continuous one-sided bounds are

```text
slow Rice upper bound = 0.0454867946313 < .05
fast six-point Slepian lower bound = 0.0561848873819 > .05
```

and a direct six-variate Gaussian calculation on six timing hypotheses gives

```text
P_FA,fast = 0.0662240
P_FA,slow = 0.0358007.
```

Thus the slow-only separation survives a **finite six-correlator bank**. It is not an artifact of a continuous supremum.

---

# Physical noise-coupling result

The active physical insight is that detector response time is not automatically the task-relevant time scale after optimal noise weighting.

Let the optical signal pass through detector transfer `G_tau(f)`.

If all relevant noise enters before and passes through exactly the same invertible transfer function,

```math
Y=G_\tau P + G_\tau W_{in},
```

then

```math
\boxed{
\mathcal I_\tau(f)
=\frac{|G_\tau P|^2}{N_{in}|G_\tau|^2}
=\frac{|P(f)|^2}{N_{in}}.
}
```

Therefore ideal full-record matched-filter SNR and timing covariance are independent of detector response time.

With additional downstream noise,

```math
Y=G_\tau P+G_\tau W_{in}+W_{out},
```

so

```math
\boxed{
\mathcal I_\tau(f)
=\frac{|P(f)|^2|G_\tau(f)|^2}
{N_{in}|G_\tau(f)|^2+N_{out}}.
}
```

Detector response matters only insofar as changing it changes this **whitened information spectrum**.

This principle is physically important but is not yet established as novel; optimum-filter literature already treats detector signals with different series/parallel noise transfer paths.

---

# Finite pulse + mixed noise: effective information time

For a unit-area exponential optical pulse

```math
p(t)=\frac{1}{\tau_p}e^{-t/\tau_p}u(t),
```

and first-order detector

```math
G_\tau(i\omega)=\frac{R_{dc}}{1+i\omega\tau},
```

with mixed white noise, define

```math
\lambda_\tau=\frac{N_{in}R_{dc}^2}{N_{out}},
```

and

```math
\boxed{
\tau_I=\frac{\tau}{\sqrt{1+\lambda_\tau}}.
}
```

Then

```math
\boxed{
\mathcal I_\tau(\omega)
=I_0
\frac{1}
{(1+\omega^2\tau_p^2)(1+\omega^2\tau_I^2)}.
}
```

The full-template timing covariance is

```math
\boxed{
R_\tau(\Delta)
=\frac{\tau_p e^{-|\Delta|/\tau_p}
-\tau_I e^{-|\Delta|/\tau_I}}
{\tau_p-\tau_I}.
}
```

At

```math
\tau_I=\tau_p,
```

this becomes

```math
\left(1+\frac{|\Delta|}{\tau_p}\right)e^{-|\Delta|/\tau_p},
```

which is exactly the Matérn-3/2 covariance used in the original Paper-A continuum proof.

Interpretation:

> raw detector response time `tau` and optimally whitened timing-information scale `tau_I` need not be the same quantity.

This is currently an **interesting physical mapping, not an established novelty claim**.

---

# Responsivity-speed scaling

For

```math
R_{dc}(\tau)\propto\tau^g
```

in the short-pulse/downstream-white-noise first-order model,

```math
\rho_\infty\propto\tau^{g-1/2}.
```

Exact known-arrival classification:

- `g<1/2`: fast dominates accumulated SNR at every finite time and eventually;
- `g=1/2`: eventual SNR equal; fast dominates every finite time;
- `1/2<g<1`: exactly one known-arrival evidence crossover;
- `g>=1`: slow dominates finite-time known-arrival evidence.

The original equal-eventual-SNR first-order normalization lies exactly at the critical boundary `g=1/2`.

---

# Prior-art boundary now known

Do not claim novelty for any of the following:

- unknown-arrival matched-filter search penalty;
- more timing resolution producing more global false-alarm opportunities;
- matched filtering in colored noise;
- whitening by the noise PSD;
- optimum timing filters for arbitrary pulse shapes;
- detector series/parallel noise sources with different transfer paths;
- shaping-time / noise / throughput tradeoffs;
- finite processing-window optimum filters.

Radiation-detector literature explicitly treats occurrence-time optimum filtering under arbitrary stationary noise and realistic series/parallel detector noise paths.

---

# Manuscript constraints

If a future manuscript emerges:

1. **Never cite or mention the research repository in the manuscript.**
2. Preserve device-engineer-readable title, abstract, opening, and conclusion.
3. State classical acquisition penalties and optimum-filter theory as prior art.
4. Do not revive the contrived pole-zero detector family as the main physical model.
5. Do not claim exact finite-time scan crossover unless it is actually proved.
6. Do not create a submission draft until novelty has been established against detector timing / optimum-filter literature.

---

# Current next question

Do not ask again whether the old crossover survives. It does, including in a conventional first-order finite-grid model.

The active research question is:

> **Is there a detector-specific, experimentally measurable relation between raw response time, physical noise-source placement, and the optimally whitened timing-information scale that is not already contained in classical optimum-filter theory?**

If the answer is no, close this experiment as a useful pedagogical result rather than force a publication.
