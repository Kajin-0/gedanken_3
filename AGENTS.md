# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Step 01 established scalar-`D*` insufficiency. Step 02 established the known-waveform matched-filter SNR functional. Step 03 established that unknown arrival time alone does not break equivalence for identical complete `D*(f)` under ideal full-observation Gaussian conditions, while a fixed finite observation window can because magnitude `D*(f)` discards phase/latency. Stop before latency-compensated dispersion analysis. No generalized replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`

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

For deterministic finite-energy optical waveform `p(t)`, complete LTI transfer `G(f)`, and additive stationary output noise with two-sided PSD `S_n(f)`,

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

For

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

This is valid for known timing, full observation, LTI response, additive stationary noise, and maximization over linear filters.

---

## 6. Step 03 — unknown timing versus finite observation

### Unknown arrival time

Define

```math
K_i(f)=\frac{G_i(f)P(f)}{\sqrt{S_{n,i}(f)}}.
```

Equal complete `D*(f)` gives equal `|K_i(f)|^2`.

For stationary Gaussian noise, unlimited observation, exact detector knowledge, and unrestricted matched-filter delay search, both the signal mean versus trial delay and the noise covariance of the search statistic depend only on the Fourier transform of `|K_i(f)|^2`.

**DERIVED / CONDITIONAL:** unknown arrival time alone does not break the ideal detectability equivalence of detectors with identical complete `D*(f)`.

### Finite fixed observation window

Use

```math
G_A(f)=1,
\qquad
G_B(f)=e^{-i2\pi f\Delta},
```

with identical white output-noise PSD `N`.

Then

```math
D_A^*(f)=D_B^*(f)=\sqrt{A/N}
```

for every frequency.

Record only `W=[0,T]`. For a finite-energy pulse lying inside the window for detector A, choose `Delta>T`, so detector B's delayed response lies outside the window.

For white noise,

```math
\rho_{i,W}^2=\frac1N\int_0^T|s_i(t)|^2dt.
```

Thus

```math
\rho_{A,W}^2>0,
\qquad
\rho_{B,W}^2=0.
```

Therefore

```math
\boxed{
D_A^*(f)=D_B^*(f)\ \forall f
\not\Rightarrow
\rho_{A,W}=\rho_{B,W}
}
```

under a fixed finite observation window.

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` discards transfer-function phase/latency, and finite time truncation can make that discarded information affect detectability.

Critical qualification: if the window can be shifted to compensate a known pure delay, this specific counterexample disappears. Do not promote latency itself to an intrinsic sensitivity penalty.

---

## 7. Current scientific frontier

The surviving hierarchy is:

```text
single reference D*
-> insufficient for arbitrary temporal signals

complete magnitude D*(f)
-> sufficient for the restricted known-waveform/full-observation maximum-linear-SNR problem
-> still sufficient for ideal unknown-arrival matched-filter search in stationary Gaussian noise
-> insufficient for a fixed finite observation window because phase/temporal placement can matter
```

The first missing information exposed beyond complete magnitude `D*(f)` is the complex temporal response together with the measurement protocol.

Do **not** yet claim that a full complex transfer function is universally sufficient.

---

## 8. Scope boundary — do not silently generalize

Do not yet claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- a new scalar detector-performance metric;
- that latency alone is a fundamental sensitivity loss;
- that nontrivial phase/dispersion matters after latency compensation (not yet shown);
- sufficiency of complex `G(f)` plus PSD under arbitrary nonlinear/nonstationary protocols;
- novelty.

Signal-dependent shot noise, saturation, dead time, nonlinear response, nonstationary noise, and globally optimal non-Gaussian decision theory remain untouched.

---

## 9. Single next question — DO NOT ANSWER UNTIL PROMPTED

> After compensating any known overall latency, can two detectors with identical complete `D*(f)` still have different finite-window detectability because of nontrivial transfer-function phase or temporal dispersion?

This is the next test because it determines whether Step 03 is merely a clock-alignment counterexample or evidence that the full complex temporal response is genuinely needed for finite-time detector comparison.