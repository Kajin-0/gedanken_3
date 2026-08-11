# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Four logical steps completed. The frontier is now finite-time SNR accumulation: Step 04 proved that complete magnitude `D*(f)` can fail under finite observation even after arbitrary constant latency compensation because nonlinear transfer phase redistributes signal energy in time. No generalized replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`

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

## 4. Step 01 — scalar D* insufficiency

Under equal area, equal low-frequency responsivity, equal additive white output noise, and first-order temporal responses,

```math
H_i(f)=\frac{1}{1+i2\pi f\tau_i},
```

equal low-frequency/reference `D*` does not guarantee equal SNR for a 1 Hz optical tone. The explicit example gives

```math
\mathrm{SNR}_A/\mathrm{SNR}_B\approx6.36.
```

**DERIVED / COUNTEREXAMPLE:** scalar reference `D*` is insufficient for arbitrary temporal signals.

Do not convert this into `fast is always better`; signal/noise filtering can cancel.

---

## 5. Step 02 — full-observation known-waveform SNR

For deterministic finite-energy optical waveform `p(t)`, LTI transfer `G(f)`, and additive stationary noise PSD `S_n(f)`,

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

With

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

```math
\boxed{
\mathrm{SNR}_{\max}^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Thus complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

---

## 6. Step 03 — unknown timing and finite observation

### Unknown arrival time

For stationary Gaussian noise, exact detector knowledge, unlimited observation, and unrestricted matched-filter delay search, identical complete `D*(f)` produces the same matched-filter search mean/covariance process.

**DERIVED / CONDITIONAL:** unknown arrival time alone does not break equivalence.

### Fixed finite window

A pure-delay pair has identical complete `D*(f)` but can place different fractions of the output inside a fixed record.

**DERIVED / COUNTEREXAMPLE:** finite time truncation can make phase/latency information discarded by magnitude `D*(f)` operationally relevant.

Critical qualification: a known pure delay can be removed by shifting the window.

---

## 7. Step 04 — latency-compensated dispersion

Use

```math
G_0(s)=\frac{b}{s+b},
```

```math
G_A(s)=G_0(s),
```

```math
G_B(s)=G_0(s)\frac{s-a}{s+a}.
```

The added factor is stable, causal, and all-pass, so with equal white output noise

```math
D_A^*(f)=D_B^*(f)
\qquad \forall f.
```

Its group delay

```math
\tau_g(\omega)=\frac{2a}{a^2+\omega^2}
```

is frequency dependent and cannot be removed by any constant latency shift.

Choose a physically regular modulation such that detector A outputs

```math
x(t)=\sin^2(\pi t/T),
\qquad 0\le t\le T,
```

zero otherwise. Detector B's all-pass output has a nonzero exponential tail for every `t>T` while preserving total signal energy exactly.

Therefore detector A captures all of its full matched-filter energy in one `T`-long window, whereas detector B cannot do so in **any** `T`-long window, even after arbitrary constant alignment:

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2.
}
```

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can be insufficient for finite-time detection because nonlinear phase / temporal dispersion controls the rate at which recoverable SNR appears in time.

This is not a pure clock-alignment artifact.

---

## 8. Current scientific frontier

The surviving hierarchy is:

```text
single reference D*
-> insufficient for arbitrary temporal signals

complete magnitude D*(f)
-> sufficient for known-waveform/full-observation maximum linear SNR
-> sufficient for ideal full-observation unknown-arrival Gaussian matched filtering
-> insufficient for finite-window measurement

pure delay
-> removable finite-window failure mechanism

nonlinear phase / temporal dispersion
-> finite-window failure survives arbitrary constant latency compensation
```

The current open issue is not whether phase can matter — that is now established. The next question is how to quantify **SNR accumulation versus available observation time** without prematurely inventing a universal scalar figure of merit.

---

## 9. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- a universal scalar replacement for `D*`;
- phase dispersion is always harmful;
- full complex `G(f)` plus PSD is sufficient under every possible protocol;
- novelty.

Signal-dependent shot noise, saturation, dead time, nonlinear response, nonstationary noise, and globally optimal non-Gaussian decision theory remain untouched.

---

## 10. Single next question — DO NOT ANSWER UNTIL PROMPTED

> For a finite observation time, what is the simplest exact quantity that measures how much of a detector's full matched-filter SNR has become available by a deadline `T`?

This returns directly to the original fast-versus-slow detector intuition while retaining the distinctions learned in Steps 01–04.