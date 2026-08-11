# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Step 01 established a scalar-`D*` insufficiency counterexample. Step 02 established the known-waveform matched-filter SNR functional. Stop before unknown-timing / finite-window analysis. No generalized replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, invalidations, and unresolved branches.

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

- **DEFINED** — a convention or model definition.
- **ASSUMED** — an idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — a physically consistent construction sufficient to disprove a claimed implication.
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

## 4. Step 01 — scalar D* is insufficient

Interpret the quoted equality as equality at a low-frequency/reference condition. Use equal area `A`, equal low-frequency responsivity `R0`, equal additive white output-noise density `n0`, and first-order temporal responses

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i}.
```

Then

```math
D_{A,0}^*=D_{B,0}^*=\frac{\sqrt A R_0}{n_0}.
```

For the same 1 Hz optical tone and same estimator bandwidth,

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.
```

**DERIVED / COUNTEREXAMPLE:** equal reference-condition scalar `D*` does not guarantee equal SNR for every optical signal.

Critical qualification: this is not `fast is always better`. If dominant noise is filtered by the same temporal pole, signal and noise attenuation can cancel.

---

## 5. Step 02 — known-waveform optimal SNR

For a deterministic finite-energy optical waveform `p(t)` with Fourier transform `P(f)`, complete LTI optical-to-output transfer `G(f)`, and additive zero-mean stationary output noise with two-sided PSD `S_n(f)`, the output signal spectrum is

```math
S(f)=G(f)P(f).
```

For any linear measurement filter `Q(f)`,

```math
\mathrm{SNR}_Q^2
=\frac{
\left|\int Q^*(f)S(f)df\right|^2
}{
\int |Q(f)|^2S_n(f)df
}.
```

Cauchy-Schwarz gives

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int_{-\infty}^{\infty}\frac{|S(f)|^2}{S_n(f)}df
}
```

with

```math
\boxed{
Q_{\mathrm{opt}}(f)\propto\frac{S(f)}{S_n(f)}.
}
```

Therefore

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

For frequency-resolved detectivity

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

this becomes

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

All displayed integrals use a two-sided PSD convention.

---

## 6. Current scientific frontier

**DERIVED / CONDITIONAL:** in the known-waveform, LTI, additive-stationary-noise limit, maximum linear-filter SNR is determined by the spectral overlap

```math
|P(f)|^2\times\frac{|G(f)|^2}{S_n(f)}.
```

The detector contribution is the ratio

```math
|G(f)|^2/S_n(f),
```

not response time, bandwidth, responsivity, or noise PSD separately.

A single scalar `D*` is only local information and cannot generally determine broadband-waveform SNR.

This formulation automatically preserves the Step-01 cancellation: if the same transfer magnitude multiplies signal and dominant noise, it can cancel in `|G|^2/S_n`; if dominant additive noise enters after the signal pole, it does not.

---

## 7. Scope boundary — do not silently generalize

The Step-02 result assumes:

```text
known deterministic waveform including timing
finite signal energy
linear time-invariant detector/readout
additive signal-independent stationary noise
two-sided PSD convention
full observation / enough delay to realize matched filter
maximization over linear filters
positive noise PSD over signal support
```

Gaussianity is not required for maximum linear SNR. It is required for the stronger standard optimal known-signal Gaussian detection interpretation.

Do not yet claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- a new scalar detector-performance metric;
- that frequency-resolved `D*(f)` remains sufficient with unknown timing or finite observation windows;
- novelty.

---

## 8. Single next question — DO NOT ANSWER UNTIL PROMPTED

> If two detectors have the same complete magnitude function `D*(f)` at every frequency, can they nevertheless differ in detectability once the optical event has an unknown arrival time or the observation window is finite?

This is the next test because the matched-filter/full-observation derivation discarded phase/timing/window constraints while retaining only the spectral signal-to-noise magnitude weighting.
