# Step 09 — Can Search Penalty Reverse a Faster Detector's Finite-Time Advantage?

**Date:** 2026-08-11 13:01 EDT  
**Status:** DERIVED / CONDITIONAL. A clean time-scaled detector family shows that rapid SNR accumulation is not guaranteed to dominate unknown-arrival-time search penalty. Under standard convergence of the finite-deadline scan to its full-template scan, the slower detector can have higher detection probability at a finite deadline even while the faster detector still has strictly more accumulated SNR. A naive direct comparison of Step-05 `eta(T)` with Step-08 full-observation `f_rms` is invalid and is explicitly corrected here. No universal replacement metric or novelty claim.

---

## 1. Question

Given two effects

```text
finite-time SNR accumulation -> eta(T)
continuous-time unknown-arrival search penalty -> timing-scan covariance / threshold
```

can the broader/faster detector's larger search penalty actually reverse the finite-time detection ranking, or is faster SNR accumulation guaranteed to win?

---

## 2. First correction: eta(T) and full-observation f_rms cannot be combined naively

Step 05 defined the finite-deadline SNR from data available only by time `T`:

```math
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
```

Step 08 defined `f_rms` from the **full-observation** noise-whitened template.

Those are not automatically the same measurement statistic.

For an unknown-arrival scan that must decide using only `T` seconds after each candidate arrival, the actual scan filter is the finite-deadline optimal filter

```math
q_T=C_T^{-1}s_T,
```

not the infinite-record matched filter.

Therefore it would be inconsistent to use

```text
finite-window rho_T from Step 05
+
full-observation f_rms from Step 08
```

as though they belonged to one exact detection protocol.

This invalidates that naive shortcut, but not Steps 05 or 08 individually.

---

## 3. Exact finite-deadline scan covariance

Let the noise be stationary on the full monitoring record. For each candidate arrival time `tau`, translate the same finite-deadline filter `q_T` and form the normalized scan statistic

```math
z_T(\tau)
=\frac{
\int_0^T q_T^*(u)y(\tau+u)du
}{
\rho_T
}.
```

Under noise only,

```math
E[z_T]=0,
\qquad
\operatorname{Var}(z_T)=1.
```

Let

```math
Q_T(f)=\int_0^T q_T(t)e^{-i2\pi ft}dt.
```

Then the exact stationary noise-only covariance of the finite-deadline timing scan is

```math
\boxed{
r_T(\Delta)
=
\frac{
\int |Q_T(f)|^2S_n(f)e^{i2\pi f\Delta}df
}{
\int |Q_T(f)|^2S_n(f)df
}.
}
```

Because `q_T=C_T^{-1}s_T`, the denominator equals `rho_T^2`.

For white output noise `N`,

```math
q_T(t)\propto s_T(t),
```

so

```math
\boxed{
r_T(\Delta)
=
\frac{
\int |S_T(f)|^2e^{i2\pi f\Delta}df
}{
\int |S_T(f)|^2df
},
}
```

where `S_T` is the transform of the signal truncated to the actual deadline record.

Thus finite-deadline SNR accumulation and finite-deadline search penalty are coupled through the same restricted measurement problem.

---

## 4. Hard-deadline regularity warning

Even if the underlying detector response is smooth, hard truncation at `T` can make the finite template discontinuous at the record boundary whenever `s(T) != 0`.

Then the finite-template spectrum can have a slow high-frequency tail and its spectral second moment may diverge. Consequently the Step-08 differentiable-process Rice formula based on `f_rms` need not apply directly to the hard-deadline scan.

This is not a failure of the search problem; the exact covariance `r_T(Delta)` remains well defined. It means only that a physical bandwidth limit, smoother observation weighting, or a non-differentiable Gaussian-extreme-value treatment is needed before reducing the scan to a curvature parameter.

Therefore no ranking claim below relies on inserting the Step-08 full-template `f_rms` into a hard finite-window formula.

---

## 5. A smooth causal time-scaled detector family with equal eventual SNR

Use the same finite-energy optical event for every detector,

```math
p(t)=e^{-bt}u(t),
\qquad b>0,
```

whose Laplace transform is

```math
P(s)=\frac1{s+b}.
```

Define a stable causal detector/readout family

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}.
```

Then the detector output for the same optical event is exactly

```math
\boxed{
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
}
```

Assume equal white output-noise PSD `N`.

Since

```math
\int_0^\infty t^2e^{-2t/\tau}dt
=\frac{\tau^3}{4},
```

choose

```math
\boxed{
A_\tau
=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
}
```

so every member has exactly the same full-observation matched-filter SNR

```math
\boxed{
\rho_{\tau,\infty}=\rho_0.
}
```

Thus any ranking difference below is not caused by unequal eventual known-time SNR.

---

## 6. Faster members accumulate SNR strictly earlier

For this family, write

```math
x=\frac{T}{\tau}.
```

In white noise,

```math
\eta_\tau(T)
=\frac{\int_0^T t^2e^{-2t/\tau}dt}
{\int_0^\infty t^2e^{-2t/\tau}dt}.
```

The integral gives

```math
\boxed{
\eta_\tau(T)
=1-e^{-2x}(1+2x+2x^2).
}
```

For two response scales

```math
\tau_f<\tau_s,
```

one has, for every finite `T>0`,

```math
\boxed{
\eta_f(T)>\eta_s(T).
}
```

Hence

```math
\boxed{
\rho_{f,T}>\rho_{s,T}
}
```

for every finite deadline, while both approach the same `rho_0` as `T->infinity`.

The faster member therefore has a genuine finite-time SNR advantage at every finite deadline.

---

## 7. Full-observation timing-search covariance scales exactly with tau

The output spectrum is

```math
S_\tau(f)
=\frac{A_\tau}{(1/\tau+i2\pi f)^2}.
```

For full-observation matched filtering in white noise, the normalized timing-scan covariance can be evaluated analytically:

```math
\boxed{
r_\tau(\Delta)
=
\left(1+\frac{|\Delta|}{\tau}\right)
\exp\!\left(-\frac{|\Delta|}{\tau}\right).
}
```

Thus

```math
r_\tau(\Delta)=r_1(\Delta/\tau).
```

Equivalently, the noise-only scan process satisfies the distributional scaling

```math
\boxed{
z_\tau(t)\overset{d}=z_1(t/\tau).
}
```

Search a physical monitoring interval of duration `L`. Then

```math
\sup_{0\le t\le L} z_\tau(t)
\overset{d}=
\sup_{0\le u\le L/\tau} z_1(u).
```

Therefore if `tau_f<tau_s`, the faster detector searches a strictly longer interval in normalized timing coordinates.

Define the exact full-template global threshold by

```math
P\!\left[
\sup_{0\le t\le L}z_\tau(t)>\gamma_\tau^\infty(L,\alpha)
\right]
=\alpha.
```

Because the supremum over a longer nested interval is stochastically no smaller,

```math
\boxed{
\gamma_f^\infty(L,\alpha)
\ge
\gamma_s^\infty(L,\alpha).
}
```

For a nondegenerate continuous Gaussian process and a nontrivial search interval, the inequality is strict for ordinary false-alarm quantiles:

```math
\boxed{
\delta\gamma_\infty
\equiv
\gamma_f^\infty-\gamma_s^\infty
>0.
}
```

This threshold ordering is exact and does not require the Rice high-threshold approximation.

For this family the Step-08 local width is also finite and equals

```math
f_{\mathrm{rms}}=\frac{1}{2\pi\tau},
```

but that fact is not needed for the exact stochastic-ordering argument.

---

## 8. Conditional reversal theorem for a finite deadline

Let

```math
\gamma_{i,T}(L,\alpha)
```

be the exact global threshold of the **actual finite-deadline scan** for detector `i`.

Assume the physically standard convergence condition

```math
\gamma_{i,T}(L,\alpha)
\longrightarrow
\gamma_i^\infty(L,\alpha)
\qquad (T\to\infty),
```

which follows when the finite-deadline translated filter/process converges sufficiently regularly to the full-template scan.

Define the finite-deadline SNR advantage

```math
\Delta\rho_T
=\rho_{f,T}-\rho_{s,T}.
```

From Section 6,

```math
\Delta\rho_T>0
```

for every finite `T`, but

```math
\boxed{
\Delta\rho_T\to0
\qquad (T\to\infty).
}
```

Define the search-threshold difference

```math
\Delta\gamma_T
=\gamma_{f,T}-\gamma_{s,T}.
```

By the convergence assumption and Section 7,

```math
\boxed{
\Delta\gamma_T
\to\delta\gamma_\infty>0.
}
```

Therefore there exists a finite `T_0` such that for sufficiently large finite `T>T_0`,

```math
\boxed{
0<\Delta\rho_T<\Delta\gamma_T.
}
```

The true-time Gaussian crossing margin is

```math
m_i(T)
=\rho_{i,T}-\gamma_{i,T}.
```

Hence

```math
m_f-m_s
=\Delta\rho_T-\Delta\gamma_T<0,
```

so

```math
\boxed{
P_{D,true,f}(T)<P_{D,true,s}(T)
}
```

because the Gaussian CDF is monotone.

Yet simultaneously

```math
\boxed{
\rho_{f,T}>\rho_{s,T}.
}
```

This is the desired ranking reversal.

---

## 9. Interpretation

**DERIVED / CONDITIONAL:** faster SNR accumulation is not guaranteed to dominate unknown-arrival-time search penalty.

Within the stated time-scaled Gaussian max-scan family, the faster detector can still have **more usable SNR by the deadline** while having **lower detection probability at the same global false-alarm requirement**, because its finer timing resolution forces a larger search threshold.

The mechanism is mathematically transparent:

```text
fast SNR advantage:
Delta rho_T > 0 but -> 0 as T grows

fast search penalty:
Delta gamma_T -> positive constant for fixed L and alpha
```

Eventually the threshold gap must dominate the shrinking SNR gap.

This is not a contradiction with Step 03. Step 03's equivalence required identical complete `D*(f)` and hence identical timing-search covariance. The present scaled family has equal **integrated asymptotic SNR** but different SNR-weighted spectra and therefore different timing-search processes.

---

## 10. Rice-regime illustration only — not the proof

For the full template of this family,

```math
f_{\mathrm{rms}}=\frac1{2\pi\tau}.
```

At high threshold, Step 08 gives the approximation

```math
\alpha
\approx
Q(u)+\frac{L}{2\pi\tau}e^{-u^2/2}.
```

As an illustration, not as the rigorous finite-deadline proof, take

```text
tau_f = 1 ns
tau_s = 1 s
L = 100 s
alpha = 1e-6
```

which gives the full-template Rice thresholds approximately

```text
u_f ~ 8.638
u_s ~ 5.760.
```

The large threshold difference shows that the search penalty can be several sigma for an extreme temporal-scale ratio even though both detectors can be normalized to the same eventual SNR.

Do not combine these full-template threshold numbers with a hard finite-window `eta(T)` as an exact finite-deadline probability; Section 2 explains why that shortcut is invalid.

---

## 11. What has been established

- **REFINEMENT / CORRECTION:** Step-05 `eta(T)` and Step-08 full-observation `f_rms` cannot be inserted independently into one finite-deadline search formula without deriving the finite-deadline scan covariance.
- **DERIVED:** the exact finite-deadline scan covariance is determined by the translated finite-window optimal filter `q_T`, not the full template.
- **DERIVED:** a stable causal time-scaled family can have exactly equal eventual matched-filter SNR while the faster member has strictly larger finite-time SNR at every finite deadline.
- **DERIVED:** for that family's full-observation scan, `r_tau(Delta)=(1+|Delta|/tau)exp(-|Delta|/tau)` and the faster member has a strictly larger unknown-time search threshold over the same physical monitoring duration.
- **DERIVED / CONDITIONAL:** if finite-deadline scan thresholds converge to their full-template limits, a finite-deadline ranking reversal must occur: the faster detector can have larger `rho_T` but smaller unknown-time detection probability.
- **DERIVED:** no broad theorem that rapid SNR accumulation must always dominate search complexity can hold under these assumptions.

---

## 12. What has not been established

- No exact closed-form finite-deadline supremum threshold `gamma_{tau,T}` for the constructed family.
- No universal deadline `T_0`; it depends on waveform, detector, noise, monitoring duration, and false-alarm requirement.
- No claim that search penalty reverses rankings in ordinary photodetector operating regimes; the result is an existence/conditional result.
- No claim that `eta(T)`, `f_rms`, or a two-number pair is a universal replacement for `D*`.
- No Bayes-optimal arrival-time test, sequential stopping, unknown amplitude/phase, shot-noise, nonlinear, saturation, dead-time, or nonstationary treatment.
- No novelty claim.

---

## 13. Stopping point

The project has now established that speed and sensitivity cannot be reduced to a monotonic one-dimensional tradeoff once finite deadlines and unknown arrival time are both present: more rapid SNR acquisition can be offset, and in a controlled family ultimately reversed, by the statistical price of resolving more possible event times.

### Single natural next question

> Is there a compact task-level description — perhaps a detection-time surface in `(P_FA, P_D, L)` rather than a scalar figure of merit — that contains both SNR accumulation and timing-search uncertainty without discarding the detector response information exposed in Steps 01–09?
