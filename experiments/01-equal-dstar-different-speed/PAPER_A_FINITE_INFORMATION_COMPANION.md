# Paper A numerical companion — finite-information continuum validation

**Date:** 2026-08-12  
**Status:** EXISTING VALIDATED RESULT CONSOLIDATED / SMOOTH FINITE-INFORMATION MODEL / NOT THE EXACT HARD-WINDOW PAPER A QUANTITATIVE EXAMPLE / NO NOVELTY CLAIM

This note extracts the strongest already-completed continuum numerical result from Steps 14–17 into a compact form suitable for Paper A discussion.

Its purpose is narrow:

> show that the fast/slow search-penalty mechanism survives a smooth finite-information timing model and produces a quantitatively stable crossover that is not an artifact of independent timing slots or the invalid Step-13 rough timing grid.

It does **not** replace the exact hard-window Paper A model and does not close the remaining request for a robust exact-hard-window quantitative example.

---

## 1. Why this companion exists

The exact finite hard-window template

```math
h_x(v)=v e^{-v}1_{[0,x]}(v)
```

has a covariance cusp at zero for every finite `x`. Step 13 showed that ordinary grid maxima then converge too slowly for its reported `ell~49` crossover to be trusted.

Step 14 introduced a genuine finite-information regularization rather than an invertible common low-pass. Step 15 validated the resulting smooth correlated timing process against direct Monte Carlo. Step 16 then used the exact continuous upcrossing-Palm identity to evaluate `alpha=10^-6` rare events efficiently.

Those results are already part of the repository history. This file only consolidates them for the Paper A narrative.

---

## 2. Smooth finite-information model

Use

```math
H_x(\nu)
=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}
{(1+i\nu)^2}
```

and the Gaussian information weighting

```math
\boxed{
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}.
}
```

This weighting is an explicit limitation on accessible timing information. It is not an invertible noiseless filter applied identically to signal and noise.

For every finite `kappa`, the normalized timing process is differentiable and has finite derivative variance

```math
\sigma_\nu^2(x,\kappa)
=\frac{\int \nu^2J_{x,\kappa}(\nu)d\nu}
{\int J_{x,\kappa}(\nu)d\nu}.
```

The equal-eventual-SNR comparison is retained within this regularized model.

---

## 3. Rare-event validation task

Step 16 used

```text
rho_0 = 6.2
r = tau_s/tau_f = 1.2
alpha = 1e-6
beta = 0.90
kappa = 8
```

with

```math
z_\beta=\Phi^{-1}(0.90).
```

The first-order continuous Rice/Euler-characteristic crossover was

```text
ell_s^Rice = 0.571441752
ell_f^Rice = r ell_s = 0.685730102
```

with finite integration durations

```text
x_s = 4.473364397
x_f = 5.368037276
```

and available thresholds

```text
u_s = 4.895464822
u_f = 4.913100340.
```

These `x` values are finite; this is not a calculation in which the integration duration itself has numerically diverged.

---

## 4. Exact continuous false-alarm identity used for correction

For the differentiable stationary Gaussian timing process, Step 16 used

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right],
}
```

where

```math
\lambda_u
=\ell\frac{\sigma_\nu}{2\pi}e^{-u^2/2}
```

is the exact Rice mean upcrossing count and `E_up` denotes the Palm law of a randomly selected level-`u` upcrossing.

This identity shows explicitly why the first-order Rice expression

```math
Q(u)+\lambda_u
```

is an upper bound here: it overcounts multiple excursions and endpoint/upcrossing overlap.

The Palm sampler forces a continuous upcrossing and therefore does not estimate the rare event by waiting for a `10^-6` maximum to occur in brute-force paths.

---

## 5. Palm check at the Rice crossover

Using `5000` Palm paths for each channel, Step 16 found:

### Slow channel

```text
Rice target alpha           = 1.0000000e-6
Palm P_FA                    = 9.9949037e-7
Monte Carlo standard error  = 2.04e-10
fraction N_u^+ > 1          ~= 8e-4
endpoint-overlap fraction   ~= 6e-4
```

### Fast channel

```text
Rice target alpha           = 1.0000000e-6
Palm P_FA                    = 9.9922753e-7
Monte Carlo standard error  = 2.70e-10
fraction N_u^+ > 1          ~= 8e-4
endpoint-overlap fraction   ~= 1e-3
```

Thus the Rice false-alarm probabilities were high by only approximately

```text
slow: 0.051%
fast: 0.077%.
```

The corresponding threshold corrections were only of order `1e-4` Gaussian-threshold units.

---

## 6. Palm-corrected crossover

Propagating the continuous false-alarm correction through the finite-time guarantee equations moved the crossover from

```text
ell_s^Rice = 0.571441752
```

to

```math
\boxed{
\ell_s^{Palm}\approx0.5721.
}
```

The Step-16 numerical summary was

```text
ell_s^Palm ~= 0.5721 +/- 0.001
```

including conservative allowance for local-grid, finite-period, and first-order propagation effects.

The displacement from the Rice result was therefore

```text
Delta ell_s ~= 0.00066
relative shift ~= 0.12%.
```

A direct reevaluation near `ell_s=0.57210` gave a Palm-corrected crossover residual consistent with zero within propagated uncertainty.

---

## 7. Grid/refinement context

Step 15 had already checked the smooth `kappa=8` timing process by direct correlated Gaussian Monte Carlo at two timing resolutions. At its `alpha=.01` validation points, the `delta=.05` and `.025` maximum thresholds overlapped within bootstrap tail uncertainty and agreed with the continuous Rice prediction. No Step-13-like systematic upward grid drift was observed.

Step 16 then repeated the Palm correction with local timing steps

```text
0.01, 0.005, 0.0025
```

and found no rough-grid continuum drift. The grid is used only to count the rare secondary crossings / endpoint corrections around a continuously imposed Palm upcrossing.

---

## 8. What this result establishes

For the tested finite-information model:

```text
- the actual correlated timing process is used;
- no independent timing-slot approximation is used;
- alpha=1e-6 false alarm is evaluated through a continuous upcrossing-Palm identity;
- the crossover survives the exact rare-event correction;
- the corrected crossover differs from Rice by only about 0.12%;
- the integration durations at the crossover are finite (x_s~4.47, x_f~5.37).
```

This is strong evidence that the search-geometry mechanism itself is not created by the invalid Step-13 grid discretization.

---

## 9. What this result does NOT establish

It does not establish:

```text
- the exact hard-window Paper A crossover location;
- an exact signal-present scan-power crossover;
- a universal finite-information kernel;
- practical hardware bandwidth recommendations;
- crossover uniqueness;
- novelty.
```

The Gaussian information weighting is a controlled smooth surrogate. It should be presented, if used in Paper A, as a **robustness / continuum-validation companion**, not as numerical evaluation of the exact hard-window theorem.

---

## 10. Paper A use

The defensible manuscript-level statement is:

> A smooth finite-information extension of the same time-scaled search problem has already been evaluated directly at `alpha=10^-6` using continuous upcrossing-Palm rare-event sampling. For `rho_0=6.2`, `beta=.90`, `r=1.2`, and `kappa=8`, the corrected crossover is `ell_s~=0.5721 +/- .001`, only about `0.12%` from the continuous Rice prediction. This supports the mechanism's robustness to finite timing information but is not substituted for the exact hard-window phase boundary.

The exact hard-window quantitative example remains a separate numerical presentation task.
