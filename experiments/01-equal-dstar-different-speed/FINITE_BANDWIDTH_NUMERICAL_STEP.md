# Step 15 — Smooth-Band Numerical Validation and Crossover Trend

**Date:** 2026-08-11 14:18 EDT  
**Status:** NUMERICAL VALIDATION / CONDITIONAL / REFINEMENT. A smooth finite-information-band version of the Step-14 regularized timing scan is simulated directly as a correlated Gaussian process. Unlike the Step-13 hard-white-noise scan, the 99th-percentile search threshold is stable under practical timing-grid refinement within Monte Carlo uncertainty and agrees with the Rice/Euler-characteristic high-threshold prediction for the validation case. Rice-based crossover estimates move systematically toward smaller normalized timing uncertainty as the bandwidth parameter is increased. These crossover values are approximate and are **not** accepted as exact continuous-time phase-boundary values. No novelty claim.

---

## 1. Question

For finite bandwidth, can the now-smooth timing scan be evaluated with controlled numerical behavior, independently cross-checked against continuous Gaussian-process theory, and used to determine how the fast/slow crossover changes as the regularization is weakened?

Step 14 established the generic finite-second-moment structure but did not choose a specific numerical regularizer or compute `Gamma_kappa`.

This step makes one explicit choice and tests it.

---

## 2. Important model choice — Gaussian information-band regularization

The exact Step-14 brick-wall accessible-band model is not required for the first numerical validation. Instead use a smooth high-frequency information penalty with the same essential regularity property: finite second spectral moment.

For the finite dimensionless template

```math
h_x(v)=v e^{-v}1_{[0,x]}(v),
```

its Fourier transform is

```math
\boxed{
H_x(\nu)
=\frac{
1-e^{-(1+i\nu)x}[1+(1+i\nu)x]
}{(1+i\nu)^2}.
}
```

Define the regularized noise-weighted timing spectrum

```math
\boxed{
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2
\exp[-(\nu/\kappa)^2].
}
```

The Gaussian factor is **defined here as an explicit information/processing weighting**, not as an invertible common signal-and-noise low-pass. Therefore the Step-14 rejected-shortcut cancellation does not apply.

`kappa` is a dimensionless high-frequency information scale. This model is a smooth surrogate within the broader Step-14 finite-second-moment class; it is not claimed to be the unique physical bandwidth model.

---

## 3. Exact regularity of this numerical model

Normalize

```math
W_{x,\kappa}(\nu)
=\frac{J_{x,\kappa}(\nu)}
{\int J_{x,\kappa}(\nu')d\nu'}.
```

Then the timing covariance is

```math
R_{x,\kappa}(y)
=\int W_{x,\kappa}(\nu)e^{i\nu y}d\nu.
```

All moments exist. In particular,

```math
\boxed{
\sigma_\nu^2(x,\kappa)
=\frac{
\int \nu^2J_{x,\kappa}(\nu)d\nu
}{
\int J_{x,\kappa}(\nu)d\nu
}
<\infty.
}
```

Hence

```math
\boxed{
R_{x,\kappa}(y)
=1-\frac12\sigma_\nu^2y^2+o(y^2).
}
```

The Step-13 `|y|` cusp is absent for every finite `kappa`.

---

## 4. Finite-SNR normalization used for the validation family

Let

```math
H_\infty(\nu)=\frac1{(1+i\nu)^2}.
```

Define the fraction of regularized eventual squared SNR captured by finite `x` as

```math
\boxed{
\mathcal R_\kappa^2(x)
=
\frac{
\int |H_x(\nu)|^2e^{-(\nu/\kappa)^2}d\nu
}{
\int |H_\infty(\nu)|^2e^{-(\nu/\kappa)^2}d\nu
}.
}
```

Normalize each family member to the same regularized eventual SNR amplitude `rho_0`, so

```math
\rho_{x,\kappa}
=\rho_0\mathcal R_\kappa(x).
```

This preserves the equal-eventual-SNR comparison within the chosen regularized model.

---

## 5. Continuous high-threshold cross-check

For a differentiable unit-variance stationary Gaussian timing scan, the exact mean upcrossing density is

```math
\nu_u^+
=\frac{\sigma_\nu}{2\pi}e^{-u^2/2}.
```

For a high threshold over dimensionless search length `ell`, use the standard first-order Euler-characteristic / rare-excursion approximation

```math
\boxed{
\alpha
\approx
Q(u)
+
\ell\frac{\sigma_\nu}{2\pi}e^{-u^2/2}.
}
```

Call the solution `Gamma_Rice(x,ell,alpha,kappa)`.

This is not declared exact. Its purpose here is to provide an independent continuous-time prediction against which the direct correlated-process Monte Carlo can be checked.

---

## 6. Direct correlated Gaussian simulation

A periodic stationary Gaussian process is synthesized by FFT with spectral eigenvalues proportional to

```math
J_{x,\kappa}(\nu).
```

The synthesis period is chosen much longer than the search interval. The maximum over the desired interval is then measured directly.

No independent timing slots or `M_eff` are introduced.

The implementation is stored in

```text
numerics/regularized_scan_mc.py
```

and includes:

- spectral synthesis of the correlated process;
- timing-grid control;
- period/padding control;
- bootstrap confidence intervals for the threshold quantile;
- Rice/Euler-characteristic threshold calculation;
- Rice-based dimensionless detection-time and crossover utilities.

---

## 7. Validation task

Retain the deliberately moderate Step-13 method-validation operating point:

```text
rho_0 = 5
r = tau_s/tau_f = 1.2
alpha = 0.01
beta = 0.90
```

Choose

```text
kappa = 8.
```

The Rice-based crossover calculation for this regularized model places the provisional switch at

```math
\ell_s^{Rice}\approx54.7489.
```

At that provisional boundary the corresponding dimensionless filter durations are

```text
slow: x_s ~= 3.78390
fast: x_f ~= 4.54068
```

and the continuous Rice thresholds are

```text
slow Gamma_Rice ~= 3.66373
fast Gamma_Rice ~= 3.70181.
```

These numbers define the points at which the numerical threshold solver is tested. They do **not** prove that `ell=54.7489` is the exact crossover.

---

## 8. Timing-grid convergence check

Direct correlated Monte Carlo was performed at two timing resolutions.

### Slow-detector scan point

For `x_s ~=3.78390`, `ell_s ~=54.7489`, `kappa=8`:

```text
delta = 0.05
paths = 15000
MC 99% threshold ~= 3.6401
bootstrap 95% interval ~= [3.5967, 3.6821]

Rice/EC prediction ~= 3.6637
```

and

```text
delta = 0.025
paths = 12000
MC 99% threshold ~= 3.6470
bootstrap 95% interval ~= [3.5924, 3.7012]

Rice/EC prediction ~= 3.6637
```

### Fast-detector scan point

For `x_f ~=4.54068`, `ell_f=r ell_s ~=65.6986`, `kappa=8`:

```text
delta = 0.05
paths = 15000
MC 99% threshold ~= 3.7041
bootstrap 95% interval ~= [3.6480, 3.7530]

Rice/EC prediction ~= 3.7018
```

and

```text
delta = 0.025
paths = 12000
MC 99% threshold ~= 3.6649
bootstrap 95% interval ~= [3.6325, 3.7017]

Rice/EC prediction ~= 3.7018
```

The fast `delta=0.025` point lands near the upper edge of its bootstrap interval rather than exactly on the Rice value; the tail uncertainty is still substantial at only `12000` paths.

The scientifically relevant observation is that:

```text
1. the two grid resolutions overlap within tail uncertainty;
2. both are compatible with the continuous Rice prediction;
3. there is no systematic upward drift like Step 13's rough process.
```

Therefore the finite-`kappa` regularization has removed the dominant grid-to-continuum pathology seen in Step 13.

---

## 9. Period / wraparound check

For the slow validation point at `delta=0.05`, enlarging the spectral-synthesis period from approximately

```text
P ~= 204.8
```

to

```text
P ~= 409.6
```

changed the 99th-percentile estimate by only about `0.01` in a smaller `8000`-path diagnostic run, well inside the Monte Carlo tail uncertainty at this stage.

No evidence was found that periodic wraparound controls the reported threshold comparison.

---

## 10. Rice-based crossover trend with bandwidth

Having validated that the smooth finite-`kappa` process behaves numerically in the expected continuous class, use the Rice/Euler-characteristic approximation to make a **trend study**, not an exact phase diagram.

For the same

```text
rho_0 = 5
r = 1.2
alpha = 0.01
beta = 0.90
```

the approximate slow-detector normalized crossover is:

```text
kappa      ell_cross^Rice
  2          75.56
  4          61.58
  8          54.75
 16          51.43
 32          49.89
```

Thus, within this regularized model and approximation,

```math
\boxed{
\kappa\uparrow
\quad\Rightarrow\quad
\ell_\times\downarrow
}
```

over the tested range.

Interpretation: restoring more high-frequency timing information increases the fast detector's normalized timing-search burden, so the slower detector becomes preferable at a smaller physical uncertainty measured in slow-detector units.

The values approach the neighborhood in which the Step-13 rough-grid calculation was drifting, but **this does not rehabilitate the rejected `ell~49` result**. The rough continuous limit is singular and has not been computed exactly.

---

## 11. What is established versus approximate

### ESTABLISHED / NUMERICALLY VALIDATED

- The chosen finite-`kappa` Gaussian information-band scan is smooth and has finite timing curvature.
- Direct simulation uses the actual correlated Gaussian process, not independent trials.
- For `kappa=8`, the 99th-percentile threshold is stable between `delta=0.05` and `0.025` within Monte Carlo tail uncertainty.
- The direct Monte Carlo thresholds are compatible with the independent Rice/Euler-characteristic continuous-time predictions at the validation points.
- Period doubling does not materially change the threshold at the present uncertainty level.
- The dominant Step-13 continuum-resolution failure is absent in this regularized test.

### CONDITIONAL / APPROXIMATE

- The tabulated crossover locations are Rice/Euler-characteristic approximations, not exact Monte Carlo phase-boundary values.
- The observed monotonic crossover trend with `kappa` is established only for the tested regularized model/parameters and approximation.
- No `kappa->infinity` extrapolation is accepted as the exact rough-white-noise crossover.

---

## 12. What failed or remains unresolved

- **NOT ATTEMPTED AS A CLAIM:** a full Monte Carlo solve of `Gamma_kappa(x,ell,alpha)` over every `x` needed for a statistically converged crossover surface would require substantially more tail sampling than the two-point validation here.
- The Step-13 `ell~49` fixed-grid estimate remains invalidated.
- No proof of crossover uniqueness.
- No rare-event importance sampler for `alpha=1e-6`.
- No exact result yet for the same fixed physical electronics bandwidth on unequal-`tau` detectors.
- The Gaussian information-band factor is one controlled regularization model, not a universal detector/readout law.
- No novelty claim.

---

## 13. First nontrivial consequence

**NUMERICAL VALIDATION / CONDITIONAL:** once the infinite-white-bandwidth cusp is regularized, the continuous correlated timing-search threshold becomes numerically well behaved: ordinary timing-grid refinement and Rice theory agree within controlled Monte Carlo uncertainty for the validation case.

The first bandwidth trend is also physically coherent:

```text
more accessible high-frequency timing information
    -> larger timing-search burden
    -> fast/slow switch occurs at smaller L/tau_s
```

for the tested equal-eventual-SNR family.

This provides the first controlled numerical evidence that the analytic task-regime mechanism survives finite-bandwidth regularization **and** can be approached numerically without an independent-trials approximation.

---

## 14. Stopping point

The finite-bandwidth numerical method is validated locally, but the crossover table is still Rice-based rather than fully Monte-Carlo solved.

### Single natural next question

> Can a rare-event / high-threshold numerical method be built for the smooth regularized scan so that `Gamma_kappa(x,ell,alpha)` and the crossover can be solved directly at detector-relevant false-alarm probabilities such as `alpha=10^-6`, and how different is that result from the Rice prediction?
