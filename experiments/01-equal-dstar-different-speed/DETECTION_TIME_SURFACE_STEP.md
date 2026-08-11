# Step 10 — Task-Level Detection-Time Surface

**Date:** 2026-08-11 13:18 EDT  
**Status:** DEFINED / DERIVED for the same finite-deadline Gaussian max-scan framework used in Steps 06–09. The compact task-level object is a minimum decision-delay surface in `(P_FA, P_D, L)`, built from the exact finite-record SNR and the exact finite-record timing-search threshold. A rational by-deadline envelope is introduced so additional available data can never hurt: the detector may always use a shorter filter. This is a task descriptor, not a universal detector-only replacement for `D*`, and no novelty claim is made.

---

## 1. Question

Is there a compact task-level description — preferably a surface rather than a scalar — that retains both

```text
finite-time SNR accumulation
```

and

```text
unknown-arrival-time search uncertainty
```

without discarding the detector-response information exposed in Steps 01–09?

The desired object should answer an operational question:

> Given an allowed global false-alarm probability, a required probability of detection, and an interval over which the event time is unknown, what is the shortest post-event decision delay the detector can support?

---

## 2. Fix the task protocol

Let an optical event have unknown arrival time

```math
\tau_0\in[0,L],
```

where `L` is the physical monitoring interval over which arrival time is uncertain.

For a candidate event time `tau`, allow a post-candidate filter duration

```math
0<t\le T,
```

where `T` is the maximum decision delay the task permits.

The output segment available for that candidate is

```math
y_{\tau,t}(u)=y(\tau+u),
\qquad 0\le u\le t.
```

For the specified detector, optical waveform, and noise model, let

```math
s_t
```

be the true detector output restricted to `[0,t]`, and let

```math
C_t
```

be the corresponding restricted noise covariance operator.

The finite-record optimal linear filter is

```math
\boxed{
q_t=C_t^{-1}s_t.
}
```

Its known-time matched-filter SNR amplitude is

```math
\boxed{
\rho_t^2
=\langle s_t,C_t^{-1}s_t\rangle.
}
```

This is the Step-05 finite-time SNR, now indexed by the **chosen filter duration** `t` rather than automatically by the maximum allowed deadline `T`.

---

## 3. Exact unknown-time scan for that same filter duration

Translate the same finite-duration filter across every candidate event time:

```math
z_t(\tau)
=
\frac{
\langle q_t,y_{\tau,t}\rangle
}{\rho_t}.
```

Under noise only,

```math
E[z_t(\tau)]=0,
\qquad
\operatorname{Var}[z_t(\tau)]=1.
```

For stationary noise, the exact scan covariance is the Step-09 finite-deadline result

```math
\boxed{
r_t(\Delta)
=
\frac{
\int |Q_t(f)|^2S_n(f)e^{i2\pi f\Delta}df
}{
\int |Q_t(f)|^2S_n(f)df
},
}
```

where `Q_t(f)` is the transform of `q_t`.

Thus the same finite-duration measurement determines both

```text
signal separation -> rho_t
```

and

```text
search correlation -> r_t(Delta).
```

No independent bandwidth or trial-count approximation has been inserted.

---

## 4. Exact global false-alarm threshold

For monitoring interval `[0,L]`, define the scan maximum

```math
Z_{t,L}
=\sup_{0\le\tau\le L}z_t(\tau).
```

For an allowed **global** false-alarm probability

```math
P_{FA}=\alpha,
```

define the exact threshold

```math
\boxed{
\gamma_t(L,\alpha)
=
F^{-1}_{Z_{t,L}|H_0}(1-\alpha),
}
```

meaning

```math
P_{H_0}\!\left[Z_{t,L}>\gamma_t(L,\alpha)\right]
=\alpha.
```

The threshold is a functional of the full finite-duration scan covariance `r_t`, the monitoring interval `L`, and the false-alarm requirement.

It is **not** determined by sample count.

---

## 5. True-time event-attributable detection probability

At the correct candidate time `tau=tau_0`, the normalized statistic has

```math
z_t(\tau_0)|H_1
\sim
\mathcal N(\rho_t,1)
```

under the same simple known-waveform, known-amplitude, additive-Gaussian assumptions as Step 06.

Therefore the probability that the **true event alignment itself** crosses the globally calibrated unknown-time threshold is

```math
\boxed{
P_{D,true}(t;L,\alpha)
=
\Phi\!\left[
\rho_t-\gamma_t(L,\alpha)
\right].
}
```

Define the task margin

```math
\boxed{
m(t;L,\alpha)
\equiv
\rho_t-\gamma_t(L,\alpha).
}
```

Then simply

```math
\boxed{
P_{D,true}(t;L,\alpha)=\Phi[m(t;L,\alpha)].
}
```

This is the compact combination of SNR accumulation and search uncertainty for the simple max-scan true-time criterion.

---

## 6. Important point: the raw margin need not improve monotonically with filter duration

For known event time, the threshold is independent of filter duration:

```math
\gamma_t(0,\alpha)=\Phi^{-1}(1-\alpha),
```

while `rho_t` is nondecreasing. Therefore longer usable records cannot reduce the known-time matched-filter margin.

For unknown event time, however,

```math
\gamma_t(L,\alpha)
```

can change with `t` because changing the finite-duration filter changes the timing-search covariance and hence the global threshold.

Therefore the raw use-all-data quantity

```math
m(t;L,\alpha)
```

is **not guaranteed to be monotone in `t`**.

This is consistent with Step 09: more accumulated SNR can be offset by a larger search penalty.

---

## 7. Rational by-deadline envelope

A physical measurement with maximum allowed delay `T` is not forced to use all `T` seconds of data. It may always ignore later samples and use any shorter filter duration

```math
0<t\le T.
```

Therefore define the best achievable event-attributable margin **by deadline `T`** as

```math
\boxed{
m^*(T;L,\alpha)
=
\sup_{0<t\le T}
\left[
\rho_t-\gamma_t(L,\alpha)
\right].
}
```

The corresponding best true-time crossing probability available by the deadline is

```math
\boxed{
P_{D,true}^*(T;L,\alpha)
=
\Phi\!\left[m^*(T;L,\alpha)\right].
}
```

Because the admissible set of filter durations grows with `T`,

```math
\boxed{
T_2>T_1
\quad\Rightarrow\quad
m^*(T_2;L,\alpha)
\ge
m^*(T_1;L,\alpha).
}
```

Thus the **optimized by-deadline performance is nondecreasing**, even though the raw margin of a forced use-all-data filter need not be.

This distinction is essential.

---

## 8. Define the detection-time surface

Let the required event-attributable detection probability be

```math
P_D=\beta.
```

Since

```math
\Phi^{-1}(\beta)
```

is the required Gaussian decision margin, define

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=
\inf\left\{
T>0:
 m^*(T;L,\alpha)
\ge
\Phi^{-1}(\beta)
\right\}.
}
```

Equivalently, because `m^*` is the supremum over all shorter durations,

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=
\inf\left\{
t>0:
\rho_t-\gamma_t(L,\alpha)
\ge
\Phi^{-1}(\beta)
\right\}.
}
```

If no filter duration satisfies the requested operating point, define

```math
\boxed{
\mathcal T_D=\infty.
}
```

This is the proposed **task-level detection-time surface**.

Its arguments have immediate operational meaning:

```text
alpha  -> allowed global false-alarm probability
beta   -> required event-attributable detection probability
L      -> interval over which event arrival time is unknown
```

and its value is

```text
minimum post-event decision delay.
```

---

## 9. Feasibility and an optimal filter duration

Define the best margin obtainable with any finite filter duration

```math
\boxed{
m_{\max}(L,\alpha)
=
\sup_{t>0}
\left[
\rho_t-\gamma_t(L,\alpha)
\right].
}
```

Then the requested operating point is feasible under this true-time max-scan criterion iff

```math
\boxed{
m_{\max}(L,\alpha)
\ge
\Phi^{-1}(\beta).
}
```

If the supremum is attained, define a task-optimal filter duration

```math
\boxed{
t_{\mathrm{opt}}(L,\alpha)
\in
\operatorname*{arg\,max}_{t>0}
\left[
\rho_t-\gamma_t(L,\alpha)
\right].
}
```

This possibility is absent from the simplest known-time problem, where the threshold does not grow with timing-search resolution and longer observations ordinarily just accumulate more SNR.

In the unknown-time problem, an interior `t_opt` is possible in principle because the useful-SNR and search-complexity terms can compete.

No claim is made here that a finite interior optimum occurs for every detector.

---

## 10. Monotonic task properties

The surface has several exact ordering properties under the stated nested-search protocol.

### Harder detection requirement

If

```math
\beta_2>\beta_1,
```

then

```math
\boxed{
\mathcal T_D(\alpha,\beta_2,L)
\ge
\mathcal T_D(\alpha,\beta_1,L).
}
```

### Stricter false-alarm requirement

If

```math
\alpha_2<\alpha_1,
```

then the required scan threshold is no smaller, so

```math
\boxed{
\mathcal T_D(\alpha_2,\beta,L)
\ge
\mathcal T_D(\alpha_1,\beta,L).
}
```

### Larger arrival-time uncertainty interval

For nested monitoring intervals

```math
L_2>L_1,
```

the noise-only supremum is taken over a larger set, so

```math
\gamma_t(L_2,\alpha)
\ge
\gamma_t(L_1,\alpha).
```

Hence

```math
\boxed{
\mathcal T_D(\alpha,\beta,L_2)
\ge
\mathcal T_D(\alpha,\beta,L_1).
}
```

Thus the surface responds in the physically expected directions without requiring a scalar speed metric.

---

## 11. Earlier steps appear as limiting cases

### Known event time

With only one known timing hypothesis,

```math
\gamma_t=\Phi^{-1}(1-\alpha),
```

independent of `t`. Therefore

```math
\boxed{
\mathcal T_D
=
\inf\left\{
t:
\rho_t
\ge
\Phi^{-1}(1-\alpha)+\Phi^{-1}(\beta)
\right\},
}
```

which recovers Step 06.

### `M` independent candidate times

If the scan consists of `M` independent timing hypotheses,

```math
\gamma_t
=\Phi^{-1}\!\left[(1-\alpha)^{1/M}\right],
```

which recovers Step 07.

### Continuous correlated timing search

For a real continuous scan,

```math
\gamma_t(L,\alpha)
```

is the quantile of the supremum of the Gaussian process with covariance `r_t(Delta)`, exactly retaining the Step-08/09 correlation structure.

Thus the detection-time surface is not a new approximation layered on top of the previous derivations; it is a compact way of packaging them into one task question.

---

## 12. Why this is not another D* replacement

The surface cannot be evaluated from one scalar detector number.

It requires, at each candidate filter duration `t`,

```math
\rho_t^2
=\langle s_t,C_t^{-1}s_t\rangle
```

and

```math
r_t(\Delta)
```

or equivalent information sufficient to obtain the global threshold `gamma_t(L,alpha)`.

Those quantities retain the detector's complex temporal response, the optical waveform, the noise covariance, and the timing-search protocol.

Therefore

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
}
```

is explicitly a **task-level performance surface**, not an intrinsic material/device scalar.

It answers a different question from conventional `D*`:

```text
D*:
How strong is small-signal sensitivity under specified spectral/bandwidth conditions?

Detection-time surface:
How soon can this specified event be detected at the required global false-alarm and detection probabilities when its arrival time is uncertain over L?
```

Neither makes the other unnecessary.

---

## 13. Exact global-detection qualification

The simple surface above uses the probability that the **true event alignment itself** exceeds the global scan threshold.

The exact global rejection probability under `H_1` is

```math
P_{D,global}(t;\tau_0)
=
P_{H_1,\tau_0}\!\left[
\sup_{0\le\tau\le L}z_t(\tau)
>
\gamma_t(L,\alpha)
\right].
```

This depends not only on `rho_t` and the noise covariance but also on the full signal-induced mean shape of the scan away from the true alignment and on boundary conventions.

Since a true-alignment crossing necessarily causes global rejection,

```math
\boxed{
P_{D,global}
\ge
P_{D,true}
}
```

for the same threshold.

Thus the defined `mathcal T_D` is a clean event-attributable task surface and generally a conservative descriptor relative to global rejection probability.

A separate exact-global or localization surface can be defined later if the scientific question requires it.

---

## 14. First nontrivial consequence

**DEFINED / DERIVED:** a compact task-level description exists without collapsing detector dynamics into a scalar:

```math
\boxed{
\mathcal T_D(\alpha,\beta,L)
=
\inf\left\{
t>0:
\rho_t-\gamma_t(L,\alpha)
\ge
\Phi^{-1}(\beta)
\right\}.
}
```

with

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle
```

and `gamma_t` determined by the supremum distribution of the finite-duration timing scan built from the same optimal filter.

The detector is therefore summarized for a **specified task** not by one sensitivity-speed number, but by a surface that asks how much decision time is required as false-alarm tolerance, desired detection probability, and timing uncertainty are varied.

A further important consequence is that unknown-time detection can possess a task-optimal filter duration: more available data can always be ignored, so optimized by-deadline performance is monotone even when a forced use-all-data detector statistic is not.

---

## 15. What has been established

- **DEFINED:** the task margin `m(t;L,alpha)=rho_t-gamma_t(L,alpha)`.
- **DERIVED:** `P_D,true=Phi[m]` for the stated simple Gaussian max-scan criterion.
- **REFINEMENT:** a maximum decision delay `T` should optimize over all filter durations `t<=T`; forcing the filter to use the entire available record can create artificial nonmonotonicity.
- **DERIVED:** the optimized by-deadline margin `m*(T)` is nondecreasing.
- **DEFINED:** the detection-time surface `mathcal T_D(alpha,beta,L)` is the earliest filter duration for which the task margin reaches `Phi^{-1}(beta)`.
- **DERIVED:** the surface increases for stricter false-alarm requirements, higher required detection probability, and larger timing-uncertainty intervals under the nested protocol.
- **DERIVED:** known-time, independent-slot, and continuous correlated-search results from Steps 06–09 are recovered as special cases.
- **NON-CLAIM:** this is not a universal detector-only figure of merit or replacement for conventional `D*`.

---

## 16. What has not been established

- No claim that a finite interior `t_opt` occurs for every detector or practical photodetector task.
- No exact closed-form `gamma_t(L,alpha)` for arbitrary correlated finite-duration scans.
- No globally optimal Bayes composite-hypothesis test for arbitrary arrival-time priors.
- No exact localization-error surface.
- No unknown amplitude/phase, sequential stopping, signal-dependent shot noise, nonlinear response, saturation, dead time, or nonstationary treatment.
- No universal scalar replacement for `D*`.
- No novelty claim.

---

## 17. Stopping point

The task-level packaging problem is resolved without discarding the detector response information discovered in Steps 01–09.

### Single natural next question

> For the time-scaled equal-eventual-SNR family introduced in Step 09, does the full detection-time surface collapse onto a small set of dimensionless variables — in particular `T/tau`, `L/tau`, `rho_infinity`, `P_FA`, and `P_D` — and does that reveal a finite optimal integration/filter duration in any regime?
