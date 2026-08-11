# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Five logical steps completed. The frontier is now operational deadline detection: Step 05 derived the exact finite-record maximum linear SNR and the normalized SNR-squared accumulation curve `eta(T)=rho_T^2/rho_infinity^2`. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`
6. `experiments/01-equal-dstar-different-speed/SNR_ACCUMULATION_STEP.md`

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

equal low-frequency/reference `D*` does not guarantee equal SNR for a 1 Hz optical tone. Explicitly,

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
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df.
}
```

With

```math
D^*(f)=\frac{\sqrt A|G(f)|}{\sqrt{S_n(f)}},
```

```math
\boxed{
\rho_\infty^2
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Thus complete magnitude `D*(f)` is sufficient for this restricted known-waveform/full-observation maximum-linear-SNR problem.

---

## 6. Step 03 — unknown timing and finite observation

### Unknown arrival time

For stationary Gaussian noise, exact detector knowledge, unlimited observation, and unrestricted matched-filter delay search, identical complete `D*(f)` produces the same matched-filter search statistics.

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

Its nonlinear group delay cannot be removed by any constant time shift. For a compact output pulse in A, B develops a nonzero tail while preserving total energy exactly.

Therefore

```math
\boxed{
\max_\delta\rho_{B,T}^2<\rho_{A,T}^2
}
```

for equal-duration windows even after arbitrary constant alignment.

**DERIVED / COUNTEREXAMPLE:** complete magnitude `D*(f)` can be insufficient for finite-time detection because nonlinear phase / temporal dispersion controls when recoverable SNR appears.

---

## 8. Step 05 — exact SNR accumulation

For output `y=s+n` observed only on `[0,T]`, let `C_T` be the additive-noise covariance operator restricted to that record.

The exact maximum linear SNR available by the deadline is

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
}
```

Define

```math
\boxed{
\eta(T)=\frac{\rho_T^2}{\rho_\infty^2}.
}
```

`eta(T)` is the fraction of eventual matched-filter **SNR squared** accessible by deadline `T`; the SNR-amplitude fraction is `sqrt(eta)`.

For nested records,

```math
0\le\eta(T)\le1,
```

and `eta(T)` is nondecreasing.

For white output noise `N`,

```math
\boxed{
\eta(T)
=\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
}
```

For the minimal exponential waveform

```math
s_\tau(t)=S_0e^{-t/\tau}u(t),
```

```math
\boxed{
\eta_\tau(T)=1-e^{-2T/\tau}.
}
```

At `T=1 us`:

```text
tau_A = 1 ns -> eta_A ~ 1

tau_B = 1 s  -> eta_B ~ 2e-6
```

This is a normalized timing comparison against each detector's own eventual SNR, not automatically an absolute SNR comparison.

For a selected squared-SNR fraction `q`,

```math
T_q=\inf\{T:\eta(T)\ge q\}
```

and for the exponential example

```math
T_q=-\frac{\tau}{2}\ln(1-q).
```

Important colored-noise caution: restriction to a finite record and infinite-record whitening do not generally commute. Use `C_T^{-1}` for the exact finite-window result.

---

## 9. Current scientific frontier

The surviving hierarchy is:

```text
single reference D*
-> insufficient for arbitrary temporal signals

complete magnitude D*(f)
-> sufficient for known-waveform/full-observation maximum linear SNR
-> sufficient for ideal full-observation unknown-arrival Gaussian matched filtering
-> insufficient for finite-window measurement

nonlinear phase / temporal dispersion
-> can alter temporal SNR accumulation even at equal complete D*(f)

finite-record performance
-> total eventual detectability: rho_infinity
-> SNR-access dynamics: eta(T)=rho_T^2/rho_infinity^2
```

The current open issue is operational detection probability by a deadline, not construction of a new scalar metric.

---

## 10. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- `eta(T)` is a universal detector-only replacement for `D*`;
- phase dispersion is always harmful;
- full complex `G(f)` plus PSD is sufficient under every possible protocol;
- novelty.

Signal-dependent shot noise, saturation, dead time, nonlinear response, nonstationary noise, and globally optimal non-Gaussian decision theory remain untouched.

---

## 11. Single next question — DO NOT ANSWER UNTIL PROMPTED

> At a fixed false-alarm probability, how does finite-time `rho_T` translate into actual probability of detecting the optical event by deadline `T`, and can two detectors with equal asymptotic SNR have sharply different deadline detection probabilities?

This is the next logical test because Step 05 has quantified SNR accumulation but has not yet converted it into an operational detection probability.