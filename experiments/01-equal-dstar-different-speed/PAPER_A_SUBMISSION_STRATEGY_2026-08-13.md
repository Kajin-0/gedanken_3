# Paper A — Submission Strategy

**Date:** 2026-08-13  
**Status:** EXTERNAL-PAPER PHASE / JOURNAL FIT AND MANUSCRIPT ARCHITECTURE

## Recommended first target

### 1. Applied Optics — recommended first submission

Current journal scope is explicitly applications-centered optics and includes optical devices, sensors, detectors, information processing, sensing, and optical technology. The journal asks research articles to connect science or technology to practical applications and to provide enough detail for reproducibility.

Paper A fits this readership because its object is not an abstract Gaussian-process theorem in isolation. It asks how photodetector response time changes a specified optical detection task under a global false-alarm constraint.

There is also substantial historical precedent inside *Applied Optics* for nearby topics:

- R. C. Jones, pulse/energy detectivity lineage in JOSA;
- B. N. Edwards, short-pulse photodiode detection, *Appl. Opt.* 5, 1423–1425 (1966);
- A. Goutzoulis, D. Casasent, and B. V. K. Vijaya Kumar, detector effects on time-integrating correlator performance, *Appl. Opt.* 24, 1224–1236 (1985);
- C. R. Doering and P. M. Harvey, optimal SNR and detector time constant in digital phase-lock amplifiers, *Appl. Opt.* 26, 633–642 (1987);
- R. L. Denningham, R. D. Griffin, and J. N. Lee, optical matched filter with constant-false-alarm detection, *Appl. Opt.* 30, 181–182 (1991);
- A. B. Milstein et al., direct-detection ladar acquisition in a range window, *Appl. Opt.* 47, 296–311 (2008).

These references narrow the novelty claim but strengthen journal fit.

### 2. Journal of Applied Physics — strong fallback

JAP explicitly publishes significant new experimental **and theoretical** applied-physics results and includes devices, sensors, photonics, and electronics. It is a good fallback if the manuscript is framed more as a general detector/device-physics result and less as an optical detection-system result.

Risk: the paper may be judged more signal-detection-theory than applied-device physics unless the detector realization and physical interpretation remain prominent.

### 3. Physical Review Applied — aspirational target, not recommended first

PRApplied includes device physics, optics, optoelectronics, photonics, and photonic devices, but its stated criteria require fresh insight plus a significant, authoritative contribution of substantial interest.

The present paper has a rigorous result but still carries two scope limitations:

- novelty of the detector-scaling synthesis is not established;
- the theorem is for a sufficient guarantee time, not the exact full signal-present scan detection time.

Those limitations make an editorial rejection substantially more likely than at Applied Optics.

### 4. Optics Express — technically in scope but weaker strategic fit

Optics Express covers photodetectors and all aspects of optics/photonics, but the paper is a compact conceptual/theoretical result rather than a broad photonics innovation. Applied Optics provides a more natural applications-and-detection readership.

---

## Applied Optics preparation constraints

From the current Optica Publishing Group style guide:

- abstract should be approximately 100 words;
- conventional article structure is preferred: Introduction, Method, Results, Discussion, Conclusion;
- figures must be called out in order and should stand on their own;
- figure identity must not rely on color alone;
- references are numbered in order of appearance;
- the submission checklist requires **Disclosures** and **Data Availability** statements;
- Word or LaTeX is accepted; visual template matching is optional at initial submission.

Paper A should therefore be rewritten around the application and result rather than around the historical derivation sequence.

---

## Recommended manuscript architecture

### 1. Introduction

Keep only four logical moves:

1. `D*` is useful but not a complete arbitrary-transient task metric; this is old.
2. Unknown-delay/global-false-alarm acquisition is mature; this is also old.
3. The remaining narrow question is whether changing detector response time can change task ordering when eventual event-specific matched-filter SNR is deliberately equalized.
4. State the answer and the exact claim boundary: sufficient batch guarantee time, not exact full-scan detection time.

Do not spend introduction space proving that scalar `D*` is incomplete.

### 2. Model and decision protocol

Combine current Sections II and III into one compact methods/model section:

- common optical event;
- causal detector existence construction;
- white-noise convention;
- equal eventual SNR normalization;
- finite-time evidence fraction `eta(x)`;
- timing covariance `R_x`;
- batch record `L+t`;
- global threshold and `P_D^scan >= P_D,true`;
- definition of `T_G`.

### 3. Results

This should become the center of the paper:

#### 3.1 Response time enters twice

Show:

```math
T_G=\tau X_G(\rho_0,\alpha,\beta,L/\tau).
```

Explain that `tau` multiplies the evidence clock and divides the nuisance-domain size.

#### 3.2 Feasibility partition and crossover theorem

Present only the minimum proof needed for:

- fast preference at `L=0`;
- fast-only feasibility impossible;
- fast boundary occurs first;
- `T_G,f -> infinity` while slow remains feasible;
- at least one crossover by continuity.

Move supporting covariance-limit detail to an appendix/supplement if page pressure develops.

#### 3.3 Continuum quantitative witness

Make this the main numerical/analytic result:

```text
rho0 = 3.5
alpha = 0.05
beta = 0.90
r = 6
L = 9 tau_f = 1.5 tau_s
```

with

```math
P_{FA,s}\le0.0336428<0.05<0.0624701\le P_{FA,f}.
```

Emphasize that the slow bound is continuous-time Rice + union bound and the fast bound is continuous-time Slepian via a finite sampled subset. No hard-window grid extrapolation enters this witness.

### 4. Discussion

Organize around interpretation rather than caveat accumulation:

- task-level versus detector-only ranking;
- why this is not a new `D* x bandwidth` metric;
- relationship to classical acquisition theory;
- what equal eventual event SNR does and does not mean;
- model limitations;
- practical implication: specify detector temporal response together with the acquisition task when transient arrival is uncertain.

### 5. Conclusion

One paragraph. Restate the two-clock mechanism and continuum witness. Explicitly leave exact scan-power ordering open.

---

## Recommended figure set

Use three main figures. Avoid a schematic curve whose exact shape has not been computed.

### Figure 1 — Evidence accumulation versus detector time scale

Plot `sqrt(eta(t/tau))` versus physical `t/tau_f` for fast and slow (`r=6`).

Purpose: establish the unambiguous known-arrival advantage of the faster channel.

### Figure 2 — Same physical uncertainty, different normalized search geometry

Plot the full-template covariance in physical time,

```math
R_\tau(\Delta)=\left(1+|\Delta|/\tau\right)e^{-|\Delta|/\tau},
```

for the fast and slow channels, with the same physical `L=9 tau_f` indicated.

Purpose: show visually why the faster channel presents more effectively distinct timing opportunities over the same physical interval.

### Figure 3 — Continuum feasibility bracket

Show the required `alpha=0.05` horizontal level together with:

```math
P_{FA,s}\le0.0336428,
\qquad
P_{FA,f}\ge0.0624701.
```

Use inequality arrows/markers rather than presenting either bound as the exact probability.

Purpose: give the reader one immediate, finite-scale result proving the channels occupy opposite feasibility regimes.

The theorem supplies crossover existence between the known-time fast-preferred regime and the finite-`L` slow-only regime; no fabricated numerical `T_G(L)` curve is needed.

---

## Title recommendation

Current title is accurate but long:

> Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR

Recommended Applied Optics title:

> **Task-dependent photodetector ordering under unknown arrival time**

Alternative, more explicit:

> **Response-time reversal in an equal-SNR photodetector acquisition task**

The first is safer because “reversal” can be misread as an exact full-scan theorem.

---

## Submission claim

The paper should make exactly this contribution claim:

> For a controlled causal photodetector family with equal event-specific eventual matched-filter SNR, detector response time rescales both finite-time evidence accumulation and the normalized unknown-arrival search. Under a global-false-alarm batch protocol this produces task-dependent sufficient-guarantee-time ordering, including at least one fast-to-slow crossover and a finite slow-only feasibility regime.

Do not claim:

- equal `D*` in the theorem;
- a universal response-time ranking;
- exact full-scan detection-time reversal;
- crossover uniqueness;
- a new sensitivity-bandwidth metric;
- novelty or priority.

---

## Current recommendation

**Prepare Applied Optics first.**

The manuscript is scientifically mature enough for external-style preparation. The next bottleneck is whether an independent optics reviewer finds the result sufficiently useful and distinct after the classical acquisition literature is made explicit.