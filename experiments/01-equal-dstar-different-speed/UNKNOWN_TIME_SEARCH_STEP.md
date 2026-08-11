# Step 07 — Unknown Arrival Time and the Search Penalty

**Date:** 2026-08-11 12:38 EDT  
**Status:** DERIVED for the simplest exact max-scan model with `M` independent candidate arrival slots in additive Gaussian noise. Unknown timing raises the global false-alarm threshold. Rapid SNR accumulation remains beneficial, but a larger number of resolvable timing trials creates an opposing look-elsewhere penalty. No continuous-time effective-trials theory or universal detector metric is claimed.

---

## 1. Question

If the optical event may occur at an unknown time within a monitoring interval, how does searching over many possible arrival times change the false-alarm threshold and the advantage conferred by rapid SNR accumulation?

The purpose is to add the **smallest exact timing-search problem** to Step 06 without jumping immediately to a continuous correlated Gaussian-process theory.

---

## 2. Simplest exact unknown-time model

Assume the monitoring interval contains `M` candidate arrival slots that are sufficiently separated that their normalized matched-filter outputs are independent under noise.

Let

```math
z_k,
\qquad k=1,\ldots,M,
```

be the normalized matched-filter output for candidate slot `k`.

Under noise only,

```math
z_k|H_0\sim\mathcal N(0,1)
```

independently.

If an event occurs in one particular slot `j`, assume

```math
z_j|H_1\sim\mathcal N(\rho_T,1),
```

while the other slots remain standard normal.

Here

```math
\rho_T
=\rho_\infty\sqrt{\eta(T)}
```

is the finite-time SNR amplitude available for the signal template associated with one candidate event.

Use the simplest scan rule

```math
Z_{\max}=\max_{1\le k\le M}z_k
```

and declare an event when

```math
Z_{\max}>\gamma.
```

This is an exact max-scan / GLRT-style model for the stated independent slots. It is **not** claimed to be the universally optimal composite-hypothesis test for every prior on unknown arrival time.

---

## 3. Exact global false-alarm threshold

Under `H_0`,

```math
P(Z_{\max}\le\gamma|H_0)
=\Phi(\gamma)^M.
```

Therefore the global false-alarm probability for the whole timing search is

```math
P_{FA,global}
=1-\Phi(\gamma)^M.
```

Set the allowed global false-alarm probability to

```math
P_{FA,global}=\alpha.
```

Then the exact threshold is

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

For small `alpha/M`,

```math
1-(1-\alpha)^{1/M}\approx\frac{\alpha}{M},
```

so approximately

```math
\gamma_{M,\alpha}
\approx\Phi^{-1}\!\left(1-\frac{\alpha}{M}\right).
```

At very small tail probability the leading asymptotic behavior is only logarithmic in the number of trials,

```math
\gamma_{M,\alpha}
\sim\sqrt{2\ln(M/\alpha)}
```

up to the standard Gaussian-tail logarithmic corrections.

Thus timing uncertainty does not multiply the required SNR by `M`; it raises the required sigma threshold slowly, approximately as `sqrt(log M)`.

---

## 4. Detection probability of the true event slot

For an event in slot `j`, the probability that the **correct signal-bearing slot itself** crosses the globally calibrated threshold is

```math
P_{D,true}
=P(z_j>\gamma_{M,\alpha}|H_1).
```

Hence

```math
\boxed{
P_{D,true}(T;M,\alpha)
=\Phi\!\left[
\rho_T-\gamma_{M,\alpha}
\right].
}
```

Using the accumulation curve,

```math
\boxed{
P_{D,true}(T;M,\alpha)
=\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-
\Phi^{-1}\!\left((1-\alpha)^{1/M}\right)
\right].
}
```

This is the direct unknown-time analogue of the Step-06 known-time relation.

The probability that the **global max test rejects `H_0` somewhere** under `H_1` is

```math
\boxed{
P_{D,global}
=1-
\Phi(\gamma_{M,\alpha}-\rho_T)
\Phi(\gamma_{M,\alpha})^{M-1}.
}
```

This quantity can count an unrelated noise crossing in a wrong slot as a rejection while a weak true slot remains below threshold. For assessing whether the optical event itself generated a threshold crossing, `P_{D,true}` is therefore the cleaner quantity. At very small global `alpha`, the two differ negligibly for a readily detected signal but can differ materially when the true signal is extremely weak.

---

## 5. Numerical search penalty

Take the same global false-alarm requirement as Step 06,

```math
\alpha=10^{-6}.
```

For a known event time (`M=1`),

```math
\gamma_{1,\alpha}
=\Phi^{-1}(0.999999)
\approx4.753424.
```

For one million independent candidate arrival times,

```math
M=10^6,
```

```math
\boxed{
\gamma_{10^6,10^{-6}}
\approx7.03449.
}
```

Thus a million-fold increase in the number of independent timing hypotheses raises the threshold by about

```text
7.03449 - 4.75342 = 2.28107 sigma.
```

This is substantial but far smaller than a factor of `10^6` in required SNR.

---

## 6. Return to the equal-eventual-SNR fast/slow example

Retain the Step-06 normalization

```math
\rho_{A,\infty}=\rho_{B,\infty}=6,
```

with

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s},
```

and the exponential accumulation law

```math
\eta_\tau(T)=1-e^{-2T/\tau}.
```

At

```math
T=1\ \mu\mathrm{s},
```

```math
\rho_{A,T}\approx6,
```

while

```math
\rho_{B,T}\approx0.0084853.
```

Now impose the much harder unknown-time search with

```math
M=10^6,
\qquad
\alpha=10^{-6}.
```

The common scan threshold is

```math
\gamma\approx7.03449.
```

Therefore the true-slot crossing probabilities are

```math
\boxed{
P_{D,true,A}
=\Phi(6-7.03449)
\approx0.15045,
}
```

and

```math
\boxed{
P_{D,true,B}
=\Phi(0.0084853-7.03449)
\approx1.06\times10^{-12}.
}
```

For comparison, in Step 06 with known event time (`M=1`), detector A had approximately

```text
P_D,A ~= 0.89372.
```

Thus unknown timing can strongly reduce absolute detection probability even when essentially all of the detector's eventual SNR has already accumulated.

For detector B, the global max test would still reject noise-only with probability of order `10^-6` under such a weak signal, but that is dominated by accidental crossings in the other searched slots rather than by the true event slot.

---

## 7. Search uncertainty creates an opposing speed effect

For a fixed number of searched hypotheses `M`, the threshold is common to both detectors and

```math
P_{D,true}
```

remains strictly increasing with the accumulated SNR `rho_T`. Rapid SNR accumulation therefore remains beneficial.

However, a faster/narrower temporal response can in some protocols resolve more distinct arrival times inside a fixed monitoring duration. If this produces a larger effective number of independent timing trials,

```math
M_A>M_B,
```

then the faster detector also faces the higher threshold

```math
\gamma_{M_A,\alpha}>\gamma_{M_B,\alpha}.
```

Therefore speed can produce two competing effects:

```text
rapid SNR accumulation
    -> increases rho_T and helps deadline detection

more resolvable arrival-time hypotheses
    -> increases search threshold and hurts detection
```

The second effect grows only logarithmically with the number of independent trials in this model, whereas `eta(T)` can change by orders of magnitude. In the extreme `1 ns` versus `1 s` example, the accumulation difference dominates the search penalty.

Do not infer from this that the fast detector always wins. The balance is protocol dependent.

---

## 8. Required accumulated SNR under timing uncertainty

For a desired probability that the true event slot crosses threshold,

```math
P_{D,true}=\beta,
```

one requires

```math
\boxed{
\rho_T
\ge
\gamma_{M,\alpha}
+
\Phi^{-1}(\beta).
}
```

Equivalently,

```math
\boxed{
\eta(T)
\ge
\left[
\frac{
\gamma_{M,\alpha}+\Phi^{-1}(\beta)
}{\rho_\infty}
\right]^2.
}
```

Thus unknown timing consumes part of the available asymptotic SNR budget before any finite-time accumulation issue is considered.

For example, with

```text
M = 1e6
alpha = 1e-6
beta = 0.90
```

one needs approximately

```math
\rho_T
\ge7.03449+1.28155
\approx8.31604.
```

A detector with `rho_infinity=6` cannot achieve this 90%-detection operating point under this particular search rule even with infinite observation of each event. The timing uncertainty itself has made the requested operating point infeasible at that signal strength.

---

## 9. Continuous-time search: explicit scope boundary

Real event time is usually continuous, and matched-filter outputs at nearby trial delays are correlated.

Then it is generally **incorrect** to set

```math
M = number of digital samples
```

and apply the independent-trials formula.

The exact global false-alarm threshold is determined by the distribution of the supremum of the matched-filter Gaussian process, whose covariance is set by the template/noise autocorrelation.

An `effective M` can sometimes summarize this approximately, but it is not universal and cannot be inferred from sampling rate alone.

This step therefore establishes the independent-slot search penalty exactly and leaves the correlated continuous-time problem open.

---

## 10. First nontrivial consequence

**DERIVED / CONDITIONAL:** unknown arrival time introduces a second resource requirement beyond finite-time SNR accumulation: **search complexity**.

For the exact independent-slot max scan,

```math
\boxed{
P_{D,true}
=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-
\gamma_{M,\alpha}
\right],
}
```

with

```math
\boxed{
\gamma_{M,\alpha}
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right].
}
```

Thus deadline detectability is governed by a competition between

```text
accumulated signal-to-noise separation
rho_infinity sqrt(eta(T))
```

and

```text
search threshold required by timing uncertainty
gamma_{M,alpha}.
```

The thought experiment therefore cannot reduce unknown-time performance to detector speed or `D*` alone.

---

## 11. What has been established

- **DERIVED:** for `M` independent Gaussian timing trials, the exact global false-alarm threshold is `gamma=Phi^{-1}[(1-alpha)^(1/M)]`.
- **DERIVED:** the true signal-slot crossing probability is `Phi[rho_T-gamma]`.
- **DERIVED:** substituting `rho_T=rho_infinity sqrt(eta(T))` separates SNR accumulation from timing-search penalty.
- **DERIVED / EXAMPLE:** at `alpha=1e-6`, increasing from one known timing hypothesis to `10^6` independent hypotheses raises the threshold from about `4.7534` to `7.0345` sigma.
- **DERIVED / EXAMPLE:** with equal `rho_infinity=6` and a `1 us` deadline, the `1 ns` exponential example has `P_D,true~0.15045` under `10^6` independent timing trials, whereas the `1 s` example has `P_D,true~1.06e-12`.
- **DERIVED:** a sufficiently large timing search can make a target `(alpha,beta)` infeasible even when the detector's known-time eventual SNR would have been adequate.
- **CONDITIONAL:** if faster temporal response increases the number of effectively independent arrival-time hypotheses, that creates an opposing threshold penalty; its exact size requires the correlation structure of the timing-search statistic.

---

## 12. What has not been established

- No exact continuous-time search threshold for correlated matched-filter outputs.
- No universal formula for effective number of timing trials.
- No proof that faster detectors always create more independent trials or that the search penalty can never reverse a ranking.
- No globally optimal composite-hypothesis test for arbitrary arrival-time priors; the max scan is the deliberately chosen simplest rule.
- No repeated/sequential stopping result.
- No signal-dependent shot noise, nonlinear response, saturation, dead time, nonstationary noise, or non-Gaussian decision theory.
- No universal scalar replacement for `D*`.
- No novelty claim.

---

## 13. Stopping point

The first unknown-time search consequence is established. Do not replace the independent-slot model by an uncontrolled `M = sample count` approximation.

### Single natural next question

> In a continuous-time matched-filter search, what determines the correlation time / effective number of statistically distinct arrival-time trials, and how is that quantity related to the detector's noise-whitened temporal response rather than to sampling rate alone?
