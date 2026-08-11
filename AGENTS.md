# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Eight logical steps completed. The frontier is now whether the benefit of rapid SNR accumulation can ever be reversed by the larger continuous-time search penalty associated with a broader SNR-weighted timing spectrum. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. `experiments/01-equal-dstar-different-speed/MATCHED_FILTER_SNR_STEP.md`
4. `experiments/01-equal-dstar-different-speed/FINITE_WINDOW_PHASE_STEP.md`
5. `experiments/01-equal-dstar-different-speed/LATENCY_COMPENSATED_DISPERSION_STEP.md`
6. `experiments/01-equal-dstar-different-speed/SNR_ACCUMULATION_STEP.md`
7. `experiments/01-equal-dstar-different-speed/DEADLINE_DETECTION_PROBABILITY_STEP.md`
8. `experiments/01-equal-dstar-different-speed/UNKNOWN_TIME_SEARCH_STEP.md`
9. `experiments/01-equal-dstar-different-speed/CONTINUOUS_TIME_SEARCH_CORRELATION_STEP.md`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, counterexamples, cancellations, negative results, refinements, invalidations, and unresolved branches.

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
8. append or consolidate a timestamped entry in `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides snapshots and recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — physically consistent construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior conditional statement without invalidating the prior restricted result.
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

### Step 01 — scalar reference D* is insufficient

A physically allowed one-pole + additive-output-noise construction gives unequal tone SNR despite equal reference `D*`.

**Do not infer:** `fast is always better`; filtering of dominant noise can cancel signal attenuation.

### Step 02 — known-waveform full-observation SNR

```math
\boxed{
\rho_\infty^2
=\int |P(f)|^2\frac{|G(f)|^2}{S_n(f)}df
=\frac1A\int |P(f)|^2D^{*2}(f)df.
}
```

Complete magnitude `D*(f)` is sufficient for this restricted full-observation maximum-linear-SNR problem.

### Step 03 — unknown timing alone is not enough; finite truncation is

Under stationary Gaussian full observation, identical complete `D*(f)` gives identical matched-filter timing-search statistics.

A finite fixed window can break the equivalence because magnitude `D*(f)` discards temporal phase/placement.

### Step 04 — pure-delay loophole removed

A causal all-pass phase factor preserves complete magnitude `D*(f)` and total infinite-time SNR while changing finite-window SNR even after arbitrary constant latency compensation.

### Step 05 — exact finite-time SNR accumulation

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle,
}
```

```math
\boxed{
\eta(T)=\rho_T^2/\rho_\infty^2.
}
```

For white-noise exponential output,

```math
\eta_\tau(T)=1-e^{-2T/\tau}.
```

This separates eventual detectability from rate of access to that detectability.

### Step 06 — fixed-deadline detection probability

For the known-time Gaussian decision,

```math
\boxed{
P_D(T;\alpha)=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}-
\Phi^{-1}(1-\alpha)
\right].
}
```

Equal eventual SNR can coexist with radically unequal detection probability at an early deadline.

### Step 07 — independent-slot unknown-time search penalty

For `M` independent candidate arrival slots scanned by their maximum,

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Unknown timing consumes additional SNR margin through the global search threshold.

**Critical warning:** `M` is not the number of digital samples in a real continuous search.

### Step 08 — continuous-time search correlation

Define

```math
K(f)=\frac{G(f)P(f)}{\sqrt{S_n(f)}},
```

```math
W(f)=\frac{|K(f)|^2}{\int|K(f')|^2df'}.
```

The normalized stationary matched-filter timing-scan covariance is

```math
\boxed{
r(\Delta)=\int W(f)e^{i2\pi f\Delta}df.
}
```

For a fixed optical waveform,

```math
\boxed{
W(f)=
\frac{|P(f)|^2D^{*2}(f)}
{\int |P(f')|^2D^{*2}(f')df'}.
}
```

Hence higher sampling rate alone does not change the trials penalty.

If

```math
\int f^2W(f)df<\infty,
```

define

```math
\boxed{
f_{\mathrm{rms}}^2=\int f^2W(f)df.
}
```

Then

```math
\boxed{
-r''(0)=(2\pi)^2f_{\mathrm{rms}}^2,
}
```

```math
\boxed{
\tau_{\mathrm{curv}}=1/(2\pi f_{\mathrm{rms}}).
}
```

For a differentiable unit-variance Gaussian scan, Rice's exact mean upcrossing density is

```math
\boxed{
\nu_u^+=f_{\mathrm{rms}}e^{-u^2/2}.
}
```

A forced high-threshold independent-trials representation gives

```math
M_{\mathrm{eff}}(u)
\sim\sqrt{2\pi}\,uL f_{\mathrm{rms}},
```

so there is no universal threshold-independent effective `M`.

**REFINEMENT OF STEP 07:** for the same waveform, identical complete magnitude `D*(f)` gives identical full-observation scan covariance and search penalty. Phase-only differences do not increase the timing trials factor. A speed-related search penalty appears only if the SNR-weighted magnitude spectrum broadens or changes.

**REGULARITY WARNING:** the ideal abrupt exponential used in Steps 05–07 has divergent second spectral moment in ideal white noise. Its SNR-accumulation results remain valid, but the differentiable Rice crossing formula requires physical high-frequency regularization or a smoother waveform.

---

## 5. Current scientific frontier

The present physically meaningful ingredients are:

```text
rho_infinity
    total eventual matched-filter separation

eta(T)
    fraction of squared separation accessible by deadline

r(Delta)
    full continuous timing-search covariance

f_rms / tau_curv
    local timing-correlation scale when second moment exists

nu_u^+
    exact mean Gaussian threshold-upcrossing density
```

The next unresolved question is whether the larger search penalty associated with broader useful SNR bandwidth can ever outweigh faster SNR accumulation strongly enough to reverse a finite-time detector ranking.

---

## 6. Scope boundary — do not silently generalize

Do not claim:

- faster is universally better;
- slower is universally worse;
- a universal speed-detectivity tradeoff;
- `eta(T)` or `f_rms` is a universal detector-only replacement for `D*`;
- sample count is an effective trials count;
- `f_rms` alone determines arbitrary correlated-search extrema; the full `r(Delta)` can matter;
- the max scan is universally optimal for every arrival-time prior;
- full complex `G(f)` plus PSD is sufficient under every protocol;
- novelty.

Signal-dependent shot noise, unknown amplitudes/phases, repeated/sequential stopping, saturation, dead time, nonlinear response, nonstationary noise, and globally optimal non-Gaussian decision theory remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Given the two competing effects now identified — SNR accumulation `eta(T)` and continuous-time search width `f_rms` — can one construct two detectors with equal asymptotic SNR for which the faster detector's larger search penalty actually reverses the finite-time detection ranking, or is rapid SNR accumulation guaranteed to dominate under some broad conditions?
