# Rev. 5 rejection and research disposition

**Date:** 2026-08-13  
**Status:** REV. 5 DO NOT SUBMIT / NOVELTY RISK CONFIRMED / PHYSICAL EXTENSION CONTINUES ONLY AS A NEW QUESTION

## Decision

The hostile review of `paper_a_device_engineer_rev5` is not treated as authoritative, but its central novelty objection survives independent checking.

**Rev. 5 should not be submitted as a full research article in its present scientific form.**

The reason is not a mathematical failure. The reason is that the core unknown-arrival mechanism — a shorter correlation time producing more effectively resolvable timing trials and therefore a larger global false-alarm threshold — is established acquisition/detection theory. The existing Paper-A theorem is a rigorous detector-facing specialization, but that is not presently enough to support a strong novelty claim.

The original derivation remains useful as a controlled result and as a route to deeper detector questions. It is not deleted.

## Review disposition

### 1. `Unknown arrival + more timing cells` novelty objection

**Disposition: SUBSTANTIALLY VALID / POTENTIALLY FATAL TO REV. 5 AS A RESEARCH ARTICLE.**

Independent literature checking confirms longstanding prior work on matched-filter banks, unknown arrival/delay, global false alarms, acquisition dwell/search size, and timing correlation. The manuscript already cited part of this literature, but the paper's central theorem still sits too close to that established logic.

The acquisition penalty itself must not be presented as the contribution.

### 2. Contrived pole-zero detector family

**Disposition: VALID FOR REV. 5 MAIN CONSTRUCTION, BUT TECHNICALLY AVOIDABLE.**

A fully conventional replacement model has now been derived using:

- one common exponential optical pulse;
- standard first-order detector transfer functions;
- common downstream white-noise PSD;
- physically linked detector responsivities;
- equal eventual matched-filter SNR.

This eliminates the event-matched detector zero. However, removing the contrivance does not by itself solve the novelty problem.

### 3. Sufficient guarantee vs exact finite-time scan power

**Disposition: VALID CLAIM BOUNDARY; `INTELLECTUALLY DISHONEST` CHARACTERIZATION REJECTED.**

Paper A proves a crossover in a sufficient guarantee time, not in the exact first finite solution of the complete signal-present scan-power equation. The manuscript explicitly states this. The title says `guarantee detection`, not `optimal detection latency`.

This remains an important limitation and should not be blurred in any future use of the result.

### 4. Continuous search creates the reversal

**Disposition: FALSE AS A FATAL OBJECTION.**

The effect survives a finite discrete correlator bank.

For the conventional first-order physical witness described below, use six timing hypotheses

```text
0, 1.5, 3.0, 4.5, 6.0, 7.5   [in units of tau_f]
```

and the same threshold budget

```text
rho0 = 3.5
alpha = .05
beta = .90
c = rho0 - Phi^{-1}(beta) = 2.2184484344553996.
```

High-accuracy six-variate Gaussian CDF evaluation gives

```text
P_FA,fast  = 0.0662240
P_FA,slow  = 0.0358007
```

at the same threshold.

Therefore

```math
P_{FA,slow}<0.05<P_{FA,fast}
```

already for a finite six-correlator bank. The continuum is useful for clean one-sided analytic bounds; it is not what creates the ordering separation.

## Conventional first-order physical witness

Use one common unit-area exponential optical pulse with

```math
\tau_p=\tau_f,
```

and first-order detector transfer functions

```math
G_\tau(s)=\frac{R_{dc}}{1+s\tau}.
```

Choose

```math
\tau_s=10\tau_f.
```

For downstream white noise `N`, eventual matched-filter SNR is

```math
\rho_\infty^2=\frac{R_{dc}^2}{2N(\tau_p+\tau)}.
```

Set

```math
\frac{R_s}{R_f}
=\sqrt{\frac{\tau_p+\tau_s}{\tau_p+\tau_f}}
=\sqrt{\frac{11}{2}}
\approx2.34520788,
```

so the two conventional first-order channels have exactly equal eventual matched-filter SNR for the same optical pulse.

This pair corresponds to the pairwise responsivity-speed exponent

```math
g=\frac{\ln\sqrt{11/2}}{\ln 10}\approx0.37018<1/2.
```

Thus the faster channel has the intrinsic known-arrival evidence advantage in the physically linked scaling family.

For `rho0=3.5`, `alpha=.05`, `beta=.90`, the required known-arrival accumulated squared-SNR fraction is

```text
0.6990895796463652.
```

Independent numerical integration gives the first crossings

```text
fast:  t = 1.80519795247 tau_f
slow:  t = 7.53280266002 tau_f.
```

So fast wins strongly at known arrival.

The full-template timing covariance is

```math
R_\tau(\Delta)
=\frac{\tau_p e^{-|\Delta|/\tau_p}
-\tau e^{-|\Delta|/\tau}}
{\tau_p-\tau}.
```

For the fast matched-timescale channel,

```math
R_f(\Delta)=(1+|\Delta|/\tau_f)e^{-|\Delta|/\tau_f}.
```

At

```math
L=7.5\tau_f,
```

the slow Rice upper bound is

```text
P_FA,slow <= 0.0454867946313 < .05,
```

while a six-point Slepian/equicorrelation lower bound for the fast channel is

```text
P_FA,fast >= 0.0561848873819 > .05.
```

Thus the same slow-only guarantee-feasibility separation exists without the pole-zero detector construction.

## Why this does not rescue Rev. 5 by itself

Radiation-detector and signal-processing literature already contains extensive optimum-filter treatments with:

- arbitrary pulse shapes;
- occurrence-time estimation;
- colored noise;
- series and parallel noise sources with different transfer paths;
- finite processing windows;
- shaping-time / resolution / rate tradeoffs.

Therefore a new paper cannot claim novelty merely because it restores physical noise paths or replaces the detector with a standard first-order response.

## Physical extension that remains worth investigating

The useful exact result is the mixed-noise information spectrum

```math
\mathcal I_\tau(f)
=\frac{|P(f)|^2|G_\tau(f)|^2}
{N_{in}|G_\tau(f)|^2+N_{out}}.
```

If all relevant noise follows the same invertible transfer function as the signal (`N_out=0`), then

```math
\mathcal I_\tau(f)=|P(f)|^2/N_{in}
```

and the detector response cancels completely from ideal full-record optimal detection.

For a first-order detector and exponential optical pulse, define

```math
\lambda_\tau=N_{in}R_{dc}^2/N_{out},
\qquad
\tau_I=\frac{\tau}{\sqrt{1+\lambda_\tau}}.
```

Then

```math
\mathcal I_\tau(\omega)
=I_0
\frac{1}
{(1+\omega^2\tau_p^2)(1+\omega^2\tau_I^2)},
```

and

```math
R_\tau(\Delta)
=\frac{\tau_p e^{-|\Delta|/\tau_p}
-\tau_I e^{-|\Delta|/\tau_I}}
{\tau_p-\tau_I}.
```

This identifies an information time `tau_I` that can differ from raw detector response time `tau`.

This is physically useful, but **novelty is not established**. Optimum-filter literature already treats the more general principle that signal and different noise sources must be weighted through their transfer functions.

## Current research decision

1. Freeze Rev. 5 as a clear pedagogical manuscript / internal derivation, **not a submission candidate**.
2. Do not spend more effort polishing its typography, title, or theorem proof.
3. Preserve the physically conventional first-order witness because it answers the `unphysical detector` and `continuum artifact` objections.
4. Continue only if a narrower detector-physics question emerges that is demonstrably absent from prior optimum-filter/timing literature.
5. Any future manuscript must state acquisition-search penalties as prior art rather than as the scientific advance.
6. The research repository must never be cited or mentioned in any manuscript.

## Best next question

The most useful next question is not `does the crossover survive?` — it does in a conventional model.

It is:

> Is there a detector-specific, experimentally measurable relation between raw response time, noise-source placement, and the optimally whitened timing-information scale that is not already contained in classical optimum-filter theory?

Until that novelty question is answered positively, do not prepare another submission draft.
