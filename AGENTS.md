# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Six logical steps completed. The frontier is now unknown-time monitoring: Step 06 mapped finite-time matched-filter SNR to fixed-false-alarm detection probability and showed that equal eventual SNR can coexist with radically unequal deadline detection probability. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`
6. `experiments/01-equal-dstar-different-speed/SNR_ACCUMULATION_STEP.md`
7. `experiments/01-equal-dstar-different-speed/DEADLINE_DETECTION_PROBABILITY_STEP.md`

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

Its nonlinear group delay cannot be removed by a constant time shift. For a compact output pulse in A, B develops a nonzero tail while preserving total energy exactly.

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

For white output noise,

```math
\boxed{
\eta(T)=
\frac{\int_0^T|s(t)|^2dt}
{\int_0^\infty|s(t)|^2dt}.
}
```

For the minimal exponential output

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

Important colored-noise caution: finite-window covariance restriction and infinite-record whitening do not generally commute. Use `C_T^{-1}` for the exact finite-window result.

---

## 9. Step 06 — operational detection probability by deadline

For the simple finite-record Gaussian hypotheses

```math
H_0:y_T=n_T,
```

```math
H_1:y_T=s_T+n_T,
```

with known signal waveform/timing/amplitude and the same covariance under both hypotheses, the normalized Neyman-Pearson statistic obeys

```math
z_T|H_0\sim\mathcal N(0,1),
```

```math
z_T|H_1\sim\mathcal N(\rho_T,1).
```

At per-decision false-alarm probability `alpha`,

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-\Phi^{-1}(1-\alpha)
\right].
}
```

For equal eventual SNR

```math
\rho_{A,\infty}=\rho_{B,\infty}=6,
```

with the original exponential `tau_A=1 ns`, `tau_B=1 s`, deadline `T=1 us`, and `P_FA=1e-6`:

```text
P_D,A ~ 0.89372
P_D,B ~ 1.043e-6
```

while both approach the same `P_D,infinity ~ 0.89372` as `T->infinity`.

**DERIVED / CONDITIONAL:** equal total eventual detectability can coexist with radically unequal deadline detection probability solely because SNR accumulates on different time scales.

For target `P_D=beta`,

```math
\rho_T\ge\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta),
```

so

```math
\eta_{req}=
\left[
\frac{\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta)}
{\rho_\infty}
\right]^2.
```

For the exponential accumulation law,

```math
T_{\alpha,\beta}
=-\frac{\tau}{2}\ln(1-\eta_{req})
```

when the requested operating point is asymptotically feasible.

This is one known-time fixed-deadline decision; it does not include unknown-time search or repeated/sequential looks.

---

## 10. Current scientific frontier

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

fixed-deadline Gaussian decision
-> P_D(T;alpha)=Phi[rho_infinity sqrt(eta(T))-Phi^{-1}(1-alpha)]
```

The current open issue is how an **unknown event time within a monitoring interval** changes the false-alarm threshold because the experiment must search many correlated candidate arrival times.

---

## 11. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- `eta(T)` is a universal detector-only replacement for `D*`;
- phase dispersion is always harmful;
- `rho_infinity` and `eta(T)` suffice outside the stated Gaussian simple-hypothesis protocol;
- full complex `G(f)` plus PSD is sufficient under every possible protocol;
- novelty.

Signal-dependent shot noise, unknown amplitudes/phases, repeated or sequential looks, saturation, dead time, nonlinear response, nonstationary noise, and globally optimal non-Gaussian decision theory remain untouched.

---

## 12. Single next question — DO NOT ANSWER UNTIL PROMPTED

> If the optical event may occur at an unknown time within a monitoring interval, how does the requirement to search over many possible arrival times change the false-alarm threshold and the advantage conferred by rapid SNR accumulation?

This is the next logical step because Step 06 used one known-time decision and therefore did not include the trials factor / correlated-search threshold created by unknown event time.