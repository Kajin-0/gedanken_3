# Step 06 — Detection Probability by a Deadline

**Date:** 2026-08-11 12:30 EDT  
**Status:** DERIVED under explicit simple-hypothesis additive-Gaussian assumptions. Finite-time matched-filter SNR maps exactly to the fixed-false-alarm probability of detection. Equal asymptotic SNR can coexist with radically different deadline detection probabilities when SNR accumulation differs. No universal replacement metric is claimed.

---

## 1. Question

At fixed false-alarm probability, how does the finite-time matched-filter SNR `rho_T` translate into actual probability of detecting the optical event by deadline `T`, and can two detectors with equal asymptotic SNR have sharply different deadline detection probabilities?

This step keeps the observation deadline fixed and makes one binary decision at that deadline. It is not yet a sequential/repeated-look detection problem.

---

## 2. Minimal Gaussian detection problem

On the finite record `[0,T]`, test

```math
H_0:\quad y_T=n_T,
```

against

```math
H_1:\quad y_T=s_T+n_T,
```

where:

- `s_T` is the known deterministic detector output for the specified optical event restricted to `[0,T]`;
- `n_T` is zero-mean Gaussian additive noise;
- the same positive-definite covariance operator `C_T` applies under both hypotheses;
- event timing, waveform, sign/phase, and amplitude are known for this simple-hypothesis test.

From Step 05,

```math
\boxed{
\rho_T^2=\langle s_T,C_T^{-1}s_T\rangle.
}
```

---

## 3. Neyman-Pearson statistic

For equal Gaussian covariance under `H_0` and `H_1`, the log-likelihood ratio is monotone in

```math
r_T=\langle s_T,C_T^{-1}y_T\rangle.
```

The statistic has

```math
E[r_T|H_0]=0,
```

```math
E[r_T|H_1]=\rho_T^2,
```

and under either hypothesis

```math
\operatorname{Var}(r_T)=\rho_T^2.
```

Normalize by

```math
z_T=\frac{r_T}{\rho_T}.
```

Then

```math
\boxed{
z_T|H_0\sim\mathcal N(0,1),
}
```

```math
\boxed{
z_T|H_1\sim\mathcal N(\rho_T,1).
}
```

Thus the finite-time matched-filter SNR amplitude `rho_T` is exactly the separation, in noise-standard-deviation units, between the two decision distributions.

---

## 4. Fixed false-alarm probability

Let the allowed false-alarm probability per decision be

```math
P_{FA}=\alpha.
```

Decide `H_1` when

```math
z_T>\gamma_\alpha,
```

where

```math
\boxed{
\gamma_\alpha=\Phi^{-1}(1-\alpha)
}
```

and `Phi` is the standard normal CDF.

The corresponding probability of detection is

```math
P_D(T;\alpha)
=P(z_T>\gamma_\alpha|H_1).
```

Therefore

```math
\boxed{
P_D(T;\alpha)
=\Phi\!\left(\rho_T-\gamma_\alpha\right)
}
```

or equivalently

```math
\boxed{
P_D(T;\alpha)
=Q\!\left(\gamma_\alpha-\rho_T\right).
}
```

This is the exact ROC relation for the stated simple Gaussian problem.

---

## 5. Insert the SNR-accumulation curve

Step 05 defined

```math
\eta(T)=\frac{\rho_T^2}{\rho_\infty^2}.
```

Hence

```math
\rho_T=\rho_\infty\sqrt{\eta(T)}.
```

The deadline detection probability becomes

```math
\boxed{
P_D(T;\alpha)
=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-\Phi^{-1}(1-\alpha)
\right].
}
```

Thus, within this restricted detection problem, the two quantities separated in Step 05 have a direct operational interpretation:

```text
rho_infinity -> eventual separation of signal/noise decision distributions
eta(T)       -> fraction of squared separation available by deadline T
```

A detector can have excellent eventual detectability and still be nearly useless at an early deadline if `eta(T)` is small.

---

## 6. Explicit equal-asymptotic-SNR example

Normalize the original fast and slow exponential detector examples so they have exactly the same full-observation SNR amplitude

```math
\rho_{A,\infty}=\rho_{B,\infty}=6.
```

Use

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s},
```

and the Step-05 accumulation law

```math
\eta_\tau(T)=1-e^{-2T/\tau}.
```

At

```math
T=1\ \mu\mathrm{s},
```

```math
\eta_A\approx1,
```

while

```math
\eta_B\approx1.999998\times10^{-6}.
```

Therefore

```math
\rho_{A,T}\approx6,
```

```math
\rho_{B,T}
=6\sqrt{\eta_B}
\approx0.0084853.
```

Now choose a stringent per-decision false-alarm probability

```math
\alpha=10^{-6}.
```

The Gaussian threshold is

```math
\gamma_\alpha
=\Phi^{-1}(0.999999)
\approx4.753424.
```

Detector A then has

```math
\boxed{
P_{D,A}(1\ \mu\mathrm{s})
\approx0.89372.
}
```

Detector B has

```math
\boxed{
P_{D,B}(1\ \mu\mathrm{s})
\approx1.043\times10^{-6}.
}
```

Thus detector B is only negligibly above the false-alarm floor at this deadline, even though by construction its **eventual** SNR is exactly the same as detector A's.

As `T->infinity`, both converge to

```math
P_{D,\infty}
=\Phi(6-4.753424)
\approx0.89372.
```

So the finite-time difference is not caused by unequal eventual sensitivity; it is caused solely by unequal SNR-acquisition dynamics.

---

## 7. Required accumulated SNR for a target detection probability

Let the desired detection probability be

```math
P_D=\beta.
```

From

```math
\beta
=\Phi(\rho_T-\gamma_\alpha),
```

one needs

```math
\boxed{
\rho_T
\ge
\gamma_\alpha+\Phi^{-1}(\beta).
}
```

Using `rho_T=rho_infinity sqrt(eta)`, the required squared-SNR availability is

```math
\boxed{
\eta(T)
\ge
\eta_{req}
=
\left[
\frac{\gamma_\alpha+\Phi^{-1}(\beta)}
{\rho_\infty}
\right]^2.
}
```

This is feasible only if the detector's eventual SNR is large enough to reach the requested `(alpha,beta)` operating point.

For the one-pole exponential accumulation law,

```math
1-e^{-2T/\tau}\ge\eta_{req},
```

so the earliest deadline satisfying the target is

```math
\boxed{
T_{\alpha,\beta}
=
-\frac{\tau}{2}
\ln(1-\eta_{req})
}
```

whenever `0<eta_req<1`.

This is an operational detection-time result tied directly to specified false-alarm and detection probabilities, not an arbitrary rise-time convention.

---

## 8. First nontrivial consequence

**DERIVED / CONDITIONAL:** in the known-signal, fixed-deadline, additive-Gaussian problem,

```math
\boxed{
P_D(T;\alpha)
=
\Phi\!\left[
\rho_\infty\sqrt{\eta(T)}
-\Phi^{-1}(1-\alpha)
\right].
}
```

Therefore two detectors with exactly equal asymptotic matched-filter SNR can have drastically different probability of detection at the same deadline and false-alarm probability if their SNR-accumulation curves differ.

The original fast-versus-slow distinction has now acquired a direct decision-theoretic meaning:

> speed can matter not by changing how much total detectability exists, but by changing whether enough of that detectability has arrived before the decision deadline.

This remains a task/protocol-dependent statement, not a universal ranking of fast and slow detectors.

---

## 9. Critical qualifications

This result assumes a single known-time simple-hypothesis decision with Gaussian additive noise and equal covariance under both hypotheses.

It does **not** yet include:

- unknown signal amplitude, sign, phase, or waveform;
- a search over many possible event times;
- repeated or sequential looks before the deadline;
- trials-factor / look-elsewhere corrections;
- signal-dependent shot noise changing the covariance under `H_1`;
- nonlinear response, saturation, dead time, or nonstationary noise.

For unknown timing or repeated monitoring, `alpha` must be defined for the full search/decision protocol rather than for one isolated matched-filter sample.

---

## 10. What has been established

- **DERIVED:** finite-time matched-filter SNR `rho_T` is the Gaussian decision-distribution separation in standard-deviation units.
- **DERIVED:** at per-decision false-alarm probability `alpha`, `P_D=Phi(rho_T-Phi^{-1}(1-alpha))`.
- **DERIVED:** substituting `rho_T=rho_infinity sqrt(eta(T))` gives the exact deadline detection law for the stated model.
- **DERIVED / EXAMPLE:** equal asymptotic SNR `rho_infinity=6` with `tau_A=1 ns`, `tau_B=1 s`, `T=1 us`, and `P_FA=1e-6` gives approximately `P_D,A=0.89372` and `P_D,B=1.043e-6`.
- **DERIVED:** a target `(P_FA,P_D)` translates into a required accumulated `eta(T)` and, for the exponential model, an explicit detection deadline proportional to `tau`.

---

## 11. What has not been established

- No universal detector ranking independent of waveform and decision protocol.
- No universal scalar replacement for `D*`.
- No claim that `rho_infinity` and `eta(T)` suffice outside this simple Gaussian setting.
- No unknown-time search or sequential-detection result.
- No signal-dependent shot-noise, nonlinear, saturation, dead-time, or nonstationary treatment.
- No novelty claim.

---

## 12. Stopping point

The SNR-accumulation curve now has a direct operational detection-probability interpretation. Do not generalize beyond the stated Gaussian simple-hypothesis model in this file.

### Single natural next question

> If the optical event may occur at an unknown time within a monitoring interval, how does the requirement to search over many possible arrival times change the false-alarm threshold and the advantage conferred by rapid SNR accumulation?
