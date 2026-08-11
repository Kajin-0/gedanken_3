# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Seven logical steps completed. The frontier is now continuous-time unknown-arrival search: Step 07 proved the exact independent-slot look-elsewhere penalty and showed that timing uncertainty raises the detection threshold while rapid SNR accumulation and search complexity can oppose one another. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`
6. `experiments/01-equal-dstar-different-speed/SNR_ACCUMULATION_STEP.md`
7. `experiments/01-equal-dstar-different-speed/DEADLINE_DETECTION_PROBABILITY_STEP.md`
8. `experiments/01-equal-dstar-different-speed/UNKNOWN_TIME_SEARCH_STEP.md`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, invalidations, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the current blob SHA before replacing an existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and explain why they changed;
6. make narrow edits where practical;
7. update `CURRENT_STATE.md` whenever the scientific frontier changes;
8. append a timestamped entry to `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — physically consistent construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **OPEN** — not established.
- **INVALIDATED** — shown false under its stated generality.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Original starting question

Two hypothetical detectors satisfy

```math
D_A^*=D_B^*
```

but have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Question:

> Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 4. Surviving logical chain

### Step 01 — scalar reference `D*` is insufficient

A physically allowed one-pole + additive-output-noise construction gives unequal tone SNR despite equal low-frequency/reference `D*`.

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36
```

for the stated 1 Hz example.

Do **not** turn this into `fast is always better`; signal/noise filtering can cancel.

### Step 02 — full-observation known-waveform SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int|P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing alone is not enough; finite truncation is

For ideal stationary-Gaussian full-observation matched-filter delay search, equal complete `D*(f)` gives identical search statistics.

A finite fixed window can break the equivalence because magnitude `D*(f)` discards phase/temporal placement.

### Step 04 — pure-delay loophole removed

A stable causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR but can redistribute signal energy into a tail. Even after arbitrary constant time alignment,

```math
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
```

Thus nonlinear phase/dispersion can matter in finite-time detection.

### Step 05 — exact SNR accumulation

For finite record `[0,T]`,

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
}
```

Define

```math
\boxed{
\eta(T)=\rho_T^2/\rho_\infty^2.
}
```

For white noise and exponential output,

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`, `tau_A=1 ns` gives `eta_A~1`, while `tau_B=1 s` gives `eta_B~2e-6`.

### Step 06 — operational deadline probability

For the simple known-time Gaussian decision,

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

For equal `rho_infinity=6`, `T=1 us`, and `P_FA=1e-6`, the fast and slow exponential examples give approximately

```text
0.89372 vs 1.043e-6
```

while sharing the same eventual detection probability.

### Step 07 — unknown-arrival-time search penalty

For `M` **independent** Gaussian timing hypotheses scanned by

```math
Z_{max}=\max_k z_k,
```

a global false-alarm requirement `alpha` gives the exact threshold

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

The probability that the true signal-bearing slot itself crosses threshold is

```math
\boxed{
P_{D,true}
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\gamma_{M,\alpha}
\right].
}
```

For `alpha=1e-6`:

```text
M=1       -> gamma ~ 4.75342 sigma
M=1e6     -> gamma ~ 7.03449 sigma
```

With `rho_infinity=6` and `T=1 us`:

```text
tau_A=1 ns -> P_D,true ~ 0.15045
tau_B=1 s  -> P_D,true ~ 1.06e-12
```

**DERIVED / CONDITIONAL:** unknown timing introduces a search-complexity threshold in addition to finite-time SNR accumulation.

If faster temporal response creates more effectively independent arrival-time hypotheses in a fixed monitoring interval, then two effects can oppose one another:

```text
faster SNR accumulation -> helps
larger timing trials factor -> hurts
```

For independent trials the threshold penalty grows only logarithmically,

```math
\gamma_{M,\alpha}\sim\sqrt{2\ln(M/\alpha)}
```

up to Gaussian-tail corrections.

---

## 5. Current scientific frontier

Do **not** set

```text
M = number of sampled data points
```

in a real continuous-time search.

Nearby matched-filter delays are correlated. The exact threshold is governed by the supremum distribution of the matched-filter Gaussian process, whose covariance is determined by the noise-whitened signal/template autocorrelation.

The next task is to identify the natural correlation time / effective number of statistically distinct arrival-time trials from that process, without prematurely inventing a universal scalar metric.

---

## 6. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- `eta(T)` is a universal detector-only replacement for `D*`;
- the independent-slot `M` is equal to sample count;
- a universal formula for effective timing trials already exists in this project;
- the max scan is the globally optimal composite-hypothesis detector for every arrival-time prior;
- full complex `G(f)` plus PSD is sufficient under every protocol;
- novelty.

Signal-dependent shot noise, unknown amplitudes/phases, repeated/sequential stopping, saturation, dead time, nonlinear response, nonstationary noise, and globally optimal non-Gaussian decision theory remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> In a continuous-time matched-filter search, what determines the correlation time / effective number of statistically distinct arrival-time trials, and how is that quantity related to the detector's noise-whitened temporal response rather than to sampling rate alone?

This is the next logical step because Step 07 isolates the search penalty exactly for independent slots but does not yet connect detector temporal response to the real continuous-time trials factor.