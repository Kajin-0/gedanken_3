# Step 19 — Fixed-Physics Bandwidth Sweep and a Genuine Finite Readout Optimum

**Date:** 2026-08-11 15:33 EDT  
**Status:** DERIVED / ASYMPTOTIC / NUMERICAL SPOT CHECK / REFINEMENT. The equal-accessible-SNR normalization from Step 18 is removed. The underlying full-band detector signal amplitude and white-noise level are held fixed while the accessible readout information bandwidth is varied. In the large-speed-ratio/full-fast-template limit, the maximum tolerable unknown-arrival interval has a genuine finite optimum bandwidth in the high-threshold Rice model. The reason is asymptotic: finite-band SNR loss decays as `1/kappa^2`, while the reduction in timing-search curvature is larger, `1/kappa`. Thus a slight reduction from infinite bandwidth improves unknown-time performance before narrower bandwidth eventually loses too much SNR. A Palm spot check supports that the optimum is not merely a first-order Rice artifact, but the exact Palm-optimal bandwidth has not been solved. No uniqueness or novelty claim.

---

## 1. Question

Step 18 deliberately renormalized every electronics bandwidth to the same accessible eventual matched-filter SNR. Under that artificial normalization, narrowing bandwidth only reduced timing-search complexity, so no finite optimum appeared.

Now remove that normalization.

Hold fixed:

- the physical detector signal amplitude;
- the underlying white output-noise level;
- the detector time constant `tau_f`;
- the task `(alpha,beta)`.

Vary only the accessible physical information-band scale `Omega_B`.

Question:

> Does the competition between lost accessible SNR and reduced timing-search complexity produce a genuine finite readout bandwidth optimum?

For the large-speed-ratio full-fast-template branch of the Gaussian information-band model, the answer is **yes**.

---

## 2. Fixed-physics full-template model

Retain the full fast-detector dimensionless template

```math
H_\infty(\nu)=\frac{1}{(1+i\nu)^2}
```

and the Step-15 Gaussian information weighting

```math
e^{-(\nu/\kappa)^2},
\qquad
\kappa=\Omega_B\tau_f.
```

Unlike Step 18, do **not** renormalize the accessible SNR when `kappa` changes.

Let

```math
\rho_{full}
```

be the eventual known-time matched-filter SNR with the information-band penalty removed (`kappa -> infinity`).

Define

```math
I_0(\kappa)
=\int_{-\infty}^{\infty}
\frac{e^{-(\nu/\kappa)^2}}
{(1+\nu^2)^2}\,d\nu,
```

```math
I_2(\kappa)
=\int_{-\infty}^{\infty}
\frac{\nu^2e^{-(\nu/\kappa)^2}}
{(1+\nu^2)^2}\,d\nu.
```

Since

```math
I_0(\infty)=\frac{\pi}{2},
```

the fraction of eventual squared SNR that remains accessible is

```math
\boxed{
F(\kappa)=\frac{I_0(\kappa)}{\pi/2}.
}
```

Therefore

```math
\boxed{
\rho_\infty(\kappa)
=\rho_{full}\sqrt{F(\kappa)}.
}
```

The timing-derivative standard deviation of the normalized full-template scan is

```math
\boxed{
\sigma^2(\kappa)=\frac{I_2(\kappa)}{I_0(\kappa)}.
}
```

Thus changing bandwidth now changes **both** the available signal separation and the unknown-time search geometry.

---

## 3. Exact closed forms for the Gaussian weighting

Let

```math
q=\frac{1}{\kappa},
\qquad
E(q)=e^{q^2}\operatorname{erfc}(q).
```

Using the standard Gaussian integral over `(nu^2+a^2)^-1` and differentiating with respect to `a`, one obtains

```math
\boxed{
I_0
=\pi E(q)\left(\frac12-q^2\right)
+\sqrt\pi\,q,
}
```

and

```math
\boxed{
I_2
=\pi E(q)\left(\frac12+q^2\right)
-\sqrt\pi\,q.
}
```

These are exact for the chosen smooth information-band model.

`F(kappa)` increases continuously from zero to one as bandwidth grows because the integrand in `I_0` increases pointwise with `kappa`.

---

## 4. Known-time feasibility threshold

Let

```math
z_\beta=\Phi^{-1}(\beta),
```

and

```math
\gamma_\alpha=\Phi^{-1}(1-\alpha).
```

Even with known event time, the task requires

```math
\rho_\infty(\kappa)
>\rho_{req},
```

where

```math
\boxed{
\rho_{req}=\gamma_\alpha+z_\beta.
}
```

If

```math
\rho_{full}\le\rho_{req},
```

then no bandwidth can make the task feasible.

If instead

```math
\rho_{full}>\rho_{req},
```

there is a unique finite bandwidth threshold `kappa_min` satisfying

```math
\boxed{
\rho_{full}\sqrt{F(\kappa_{min})}
=\rho_{req}.
}
```

For `kappa <= kappa_min`, the detector cannot tolerate any positive unknown-arrival search interval at the requested `(alpha,beta)`.

This already removes the Step-18 monotonic narrow-band preference: sufficiently narrow electronics now destroys the task through SNR loss.

---

## 5. Large-speed-ratio crossover / feasibility objective

Retain the Step-18 large-speed-ratio condition so the slow detector approaches known-time operation and the fast detector uses its full accessible template.

Define the available threshold margin

```math
\boxed{
u(\kappa)
=\rho_{full}\sqrt{F(\kappa)}-z_\beta.
}
```

For `u(kappa) > gamma_alpha`, the isolated-excursion Rice feasibility length of the fast full-template scan is

```math
\boxed{
\ell_{crit}^{Rice}(\kappa)
=
\frac{
2\pi[\alpha-Q(u(\kappa))]
 e^{u(\kappa)^2/2}
}{\sigma(\kappa)}.
}
```

The corresponding physical large-`r` fast/slow crossover is

```math
\boxed{
L_\times^{Rice}(\Omega_B)
\sim
\tau_f\,
\ell_{crit}^{Rice}(\Omega_B\tau_f).
}
```

The bandwidth-optimization question is therefore precise:

```math
\boxed{
\kappa_{opt}
\in\arg\max_{\kappa>0}
\ell_{crit}^{Rice}(\kappa).
}
```

This optimizes the amount of physical arrival-time uncertainty for which the fast detector remains preferable on the large-speed-ratio branch. It is **not** yet claimed to optimize every possible detection objective.

---

## 6. Narrow-band limit — SNR loss wins

For

```math
\kappa\ll1,
```

the information band is narrow compared with the detector's natural timing scale. Expanding around `nu=0` gives

```math
I_0(\kappa)
=\sqrt\pi\,\kappa
[1-\kappa^2+O(\kappa^4)],
```

so

```math
\boxed{
F(\kappa)
\sim\frac{2\kappa}{\sqrt\pi}.
}
```

Hence

```math
\boxed{
\rho_\infty(\kappa)
\sim
\rho_{full}
\sqrt{\frac{2\kappa}{\sqrt\pi}}
\to0.
}
```

Meanwhile

```math
\boxed{
\sigma(\kappa)
\sim\frac{\kappa}{\sqrt2}.
}
```

The reduced search curvature cannot rescue the task because the available SNR itself vanishes. Therefore sufficiently narrow bandwidth is infeasible.

---

## 7. Wide-band limit — the key asymptotic imbalance

Let

```math
q=1/\kappa.
```

The exact integrals give

```math
F(\kappa)
=1-q^2+
\frac{8}{3\sqrt\pi}q^3
+O(q^4),
```

so

```math
\boxed{
\rho_\infty(\kappa)
=\rho_{full}
\left[
1-\frac{1}{2\kappa^2}
+O(\kappa^{-3})
\right].
}
```

The SNR penalty from finite bandwidth is therefore only second order in `1/kappa`.

But

```math
\sigma^2(\kappa)
=1-\frac{4}{\sqrt\pi\kappa}
+O(\kappa^{-2}),
```

so

```math
\boxed{
\sigma(\kappa)
=1-\frac{2}{\sqrt\pi\kappa}
+O(\kappa^{-2}).
}
```

The reduction in timing-search curvature is **first order** in `1/kappa`.

Define

```math
G(u)
=2\pi[\alpha-Q(u)]e^{u^2/2}.
```

If the full-band task is strictly feasible,

```math
u_\infty
=\rho_{full}-z_\beta
>\gamma_\alpha,
```

then

```math
G(u(\kappa))
=G(u_\infty)+O(\kappa^{-2}).
```

Therefore

```math
\boxed{
\ell_{crit}^{Rice}(\kappa)
=
\ell_{crit}^{Rice}(\infty)
\left[
1+\frac{2}{\sqrt\pi\kappa}
+O(\kappa^{-2})
\right].
}
```

This is the central Step-19 asymptotic result.

For sufficiently large but finite bandwidth,

```math
\boxed{
\ell_{crit}^{Rice}(\kappa)
>
\ell_{crit}^{Rice}(\infty).
}
```

So **infinite bandwidth is not optimal** for this unknown-time objective.

---

## 8. Existence of a genuine finite optimum

Assume

```math
\rho_{full}>\rho_{req}.
```

Then:

1. at `kappa=kappa_min`, the positive-search feasibility length is zero;
2. `ell_crit(kappa)` is continuous for `kappa>kappa_min`;
3. for all sufficiently large finite `kappa`, the wide-band expansion gives

```math
\ell_{crit}(\kappa)
>\ell_{crit}(\infty);
```

4. as `kappa -> infinity`, `ell_crit(kappa)` approaches the lower finite limit `ell_crit(infinity)`.

Therefore the continuous function must attain at least one maximum at finite `kappa`:

```math
\boxed{
0<\kappa_{opt}<\infty.
}
```

**DERIVED / CONDITIONAL:** within the chosen fixed-physics Gaussian information-band model and high-threshold Rice objective, a genuine finite readout-bandwidth optimum necessarily exists whenever the full-band detector has strictly more SNR than the known-time task requires.

No uniqueness claim is made.

---

## 9. Physical interpretation

Near infinite bandwidth, narrowing the readout slightly has two competing effects:

```text
BAD:
accessible SNR decreases
    ~ O(1/kappa^2)

GOOD:
timing-search curvature decreases
    ~ O(1/kappa)
```

The search-complexity benefit initially wins because it is asymptotically larger.

At stronger narrowing, however, the accumulated SNR loss eventually dominates and the task becomes impossible even for known timing.

Therefore the optimum is not an arbitrary engineering compromise inserted by hand. It emerges from the different asymptotic rates at which information-bandwidth truncation affects:

```text
signal separation
versus
timing-search multiplicity.
```

---

## 10. Numerical example tied to the Step-16 validation point

To maintain continuity with Step 16, choose the fixed physical full-band SNR so that the accessible SNR at

```text
kappa = 8
```

is exactly the earlier value

```text
rho_infinity(8) = 6.2.
```

For the Gaussian information band,

```text
F(8) ~= 0.9869810583,
```

so this corresponds to the fixed unbandlimited physical SNR

```math
\boxed{
\rho_{full}\approx6.2407571.
}
```

Retain

```text
alpha = 1e-6
beta  = 0.90.
```

The known-time required SNR is

```text
rho_req ~= 6.0349759.
```

The resulting bandwidth threshold is

```text
kappa_min ~= 3.14545.
```

Rice optimization gives

```text
kappa_opt ~= 42.23
ell_crit^Rice(kappa_opt) ~= 0.90083.
```

The infinite-band result is

```text
ell_crit^Rice(infinity) ~= 0.88906.
```

Thus the finite optimum improves the tolerable normalized arrival uncertainty by about

```text
1.32%
```

relative to infinite bandwidth.

At the optimum,

```text
rho_infinity(kappa_opt) ~= 6.23907
sigma(kappa_opt)        ~= 0.97402.
```

Almost all eventual SNR has already been recovered, while the timing-search curvature is still measurably below its infinite-band value.

For the illustrative

```text
tau_f = 1 ns,
```

and writing

```math
f_B=\Omega_B/(2\pi),
```

this model corresponds to

```text
known-time feasibility onset:  f_B ~= 0.501 GHz
finite optimum:                f_B ~= 6.72 GHz
L_cross at optimum:            ~= 0.901 ns
infinite-band L_cross:          ~= 0.889 ns.
```

These are dimensionless-model translations, **not** hardware bandwidth recommendations or literal circuit `-3 dB` values.

---

## 11. Palm spot check — the optimum is not obviously a Rice artifact

Because the optimum is shallow, a direct rare-event sanity check was made using the Step-16 upcrossing Palm method on the full-template process.

At the Rice optimum candidate (`kappa ~=42.23`) with `10000` Palm paths and a local correction grid near `0.0025`, the Rice feasibility length produced

```text
P_FA ~= 9.9284e-7
```

instead of exactly `1e-6`. The implied Palm factor was approximately

```text
C_up ~= 0.9889,
```

which raises the fixed-threshold feasibility length from

```text
0.90083
```

to approximately

```text
0.91097.
```

For the unregularized full-template limit, the analogous `10000`-path Palm check gave approximately

```text
C_up ~= 0.9779
```

and raises the Rice feasibility length from

```text
0.88906
```

to approximately

```text
0.90915.
```

Thus the finite-band candidate remains about `0.2%` above the infinite-band value after this correction.

**NUMERICAL SPOT CHECK / QUALIFICATION:** this supports the existence of the finite optimum beyond first-order Rice theory, but it is not an exact Palm optimization. Secondary crossings are still counted on a fine grid, the finite-band candidate was not re-optimized under the Palm correction, and the remaining difference is small. Do not quote an exact Palm-optimal bandwidth yet.

---

## 12. What Step 19 establishes

- **MODEL CHANGE:** physical signal and noise amplitudes are fixed while readout bandwidth varies; accessible eventual SNR is no longer renormalized.
- **DERIVED:** accessible eventual SNR is `rho_full sqrt(F(kappa))` and tends to zero for narrow bandwidth.
- **DERIVED:** a finite minimum bandwidth is required before the requested `(alpha,beta)` task is feasible even for known timing.
- **DERIVED:** finite-band SNR loss is `O(kappa^-2)` near wide bandwidth, while the timing-curvature reduction is `O(kappa^-1)`.
- **DERIVED / CONDITIONAL:** in the large-`r`, full-fast-template, isolated-excursion Rice problem, infinite bandwidth is suboptimal and at least one finite `kappa_opt` must exist whenever the full-band detector is strictly task-feasible.
- **NUMERICAL EXAMPLE:** the Step-16-calibrated task gives `kappa_opt ~=42.23`, about a `1.32%` Rice improvement over infinite bandwidth.
- **NUMERICAL SPOT CHECK:** Palm rare-event corrections preserve the finite-candidate-over-infinite ordering in the tested calculation, but an exact Palm optimum has not been solved.

---

## 13. What is not established

- No uniqueness of `kappa_opt` for arbitrary tasks or bandwidth models.
- No claim that the Gaussian information weighting is a literal electronics transfer function.
- No claim that `6.72 GHz` is a recommended circuit bandwidth.
- No proof yet that the exact Palm/global-supremum optimum must be finite for all strictly feasible parameter choices.
- No statement that the bandwidth maximizing crossover `L_cross` also minimizes detection time for every fixed `L`.
- No result yet for finite speed ratio with both detectors' accessible SNR changing simultaneously under one physical bandwidth.
- No novelty claim.

---

## 14. First nontrivial consequence

**DERIVED / CONDITIONAL:** once real SNR loss is restored, unknown-time detection can possess a genuine finite readout-bandwidth optimum. The optimum arises because near the wide-band limit

```math
\boxed{
\text{search-complexity benefit from narrowing}
\sim O(1/\kappa)
}
```

while

```math
\boxed{
\text{SNR penalty from narrowing}
\sim O(1/\kappa^2).
}
```

Narrowing slightly from infinite bandwidth therefore helps first; narrowing too far eventually destroys detectability.

---

## 15. Stopping point

The existence of a finite optimum is established for the large-speed-ratio/full-template high-threshold objective in the chosen smooth information-band model, with a Palm spot check supporting the ordering.

### Single natural next question

> Does the finite optimum survive when the speed ratio is finite and the same physical bandwidth simultaneously changes **both detectors'** accessible SNR and timing-search covariance, and can that produce multiple preference reversals as bandwidth is swept?
