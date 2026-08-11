# Step 20 — Finite Speed Ratio and Double Preference Reversal versus Readout Bandwidth

**Date:** 2026-08-11 16:12 EDT  
**Status:** DERIVED / NUMERICAL COUNTEREXAMPLE / CONDITIONAL. The fixed-physics bandwidth sweep from Step 19 is extended from the large-speed-ratio asymptote to a genuinely finite detector-speed ratio. With one shared physical information bandwidth, the slower detector has a low-band accessible-SNR advantage, the faster detector can win at intermediate bandwidth, and the slower detector can win again at high bandwidth because the fast detector pays the larger unknown-time search burden. An explicit `r=2` finite-duration Rice calculation exhibits two preference reversals as bandwidth is swept. The two switch values survive a frequency-quadrature refinement test. This is a counterexample to any assumption that bandwidth can change the preferred detector at most once. Exact Palm-corrected switch locations remain open. No novelty claim.

---

## 1. Question

Step 19 showed that, in the large-speed-ratio/full-fast-template limit, fixing the underlying detector signal and noise while sweeping readout bandwidth produces a finite optimum for the maximum tolerable unknown-arrival interval.

The next question is stricter:

> At finite speed ratio, where the same physical bandwidth changes both detectors' accessible SNR and timing-search covariance simultaneously, does the finite-bandwidth structure survive, and can the preferred detector reverse more than once as bandwidth is swept?

The answer within the present smooth Gaussian information-band / high-threshold Rice model is **yes**.

---

## 2. Fixed-physics finite-`r` model

Retain the controlled time-scaled detector family from Step 09, normalized so that the two detectors have the same **unregularized full-band eventual known-time SNR**

```math
\rho_{full}.
```

Let

```math
r=\frac{\tau_s}{\tau_f}>1.
```

Impose one common physical information-band scale

```math
\Omega_B.
```

Define the fast detector's dimensionless bandwidth

```math
\boxed{\kappa_f=\Omega_B\tau_f,}
```

so the slow detector sees

```math
\boxed{\kappa_s=\Omega_B\tau_s=r\kappa_f.}
```

Unlike Step 18, do **not** renormalize either detector after bandwidth is imposed.

For the full template, define the Step-19 accessible squared-SNR fraction

```math
F(\kappa)
=\frac{I_0(\kappa)}{\pi/2},
```

where

```math
I_0(\kappa)
=\int_{-\infty}^{\infty}
\frac{e^{-(\nu/\kappa)^2}}
{(1+\nu^2)^2}\,d\nu.
```

Then the accessible eventual SNRs are

```math
\boxed{
\rho_{\infty,f}(\kappa_f)
=\rho_{full}\sqrt{F(\kappa_f)},
}
```

```math
\boxed{
\rho_{\infty,s}(\kappa_f)
=\rho_{full}\sqrt{F(r\kappa_f)}.
}
```

Because `F` is strictly increasing,

```math
\boxed{
\rho_{\infty,s}>\rho_{\infty,f}
\quad\text{for every finite }\kappa_f.
}
```

This asymmetry is not inserted by hand. It follows from applying one physical bandwidth to two time-scaled signals whose unbandlimited total SNRs were normalized equal.

---

## 3. Narrow-band asymptote — the slower detector gets an SNR head start

From Step 19,

```math
F(\kappa)
\sim\frac{2\kappa}{\sqrt\pi}
\qquad(\kappa\ll1).
```

Therefore

```math
\frac{\rho_{\infty,s}}
{\rho_{\infty,f}}
=
\sqrt{\frac{F(r\kappa_f)}{F(\kappa_f)}}
\to\boxed{\sqrt r}.
```

So at sufficiently narrow common readout bandwidth, the slower detector can have a substantial accessible-SNR advantage even though the two detectors have equal unbandlimited eventual SNR.

This gives a natural low-band ordering:

```text
very narrow bandwidth
    -> neither detector feasible
slightly wider bandwidth
    -> slow detector becomes feasible first
```

The slow detector's known-time feasibility onset occurs at roughly `1/r` of the fast detector's `kappa_f` scale in the narrow-band limit.

---

## 4. Exact finite-duration quantities used for the finite-`r` calculation

For finite dimensionless decision duration `x`, retain

```math
h_x(v)=v e^{-v}1_{[0,x]}(v)
```

with transform

```math
H_x(\nu)
=\frac{1-e^{-(1+i\nu)x}[1+(1+i\nu)x]}
{(1+i\nu)^2}.
```

For detector `i` with dimensionless bandwidth `kappa_i`, define

```math
I_{0,i}(x)
=\int |H_x(\nu)|^2
 e^{-(\nu/\kappa_i)^2}d\nu,
```

```math
I_{2,i}(x)
=\int \nu^2|H_x(\nu)|^2
 e^{-(\nu/\kappa_i)^2}d\nu.
```

The fixed-physics finite-duration SNR is

```math
\boxed{
\rho_i(x)
=\rho_{full}
\sqrt{\frac{I_{0,i}(x)}{\pi/2}},
}
```

and the smooth timing-scan derivative standard deviation is

```math
\boxed{
\sigma_i(x)
=\sqrt{\frac{I_{2,i}(x)}{I_{0,i}(x)}}.
}
```

For normalized search interval `ell_i`, the high-threshold Rice/EC threshold `Gamma_i` is defined by

```math
\boxed{
\alpha
=Q(\Gamma_i)
+\ell_i\frac{\sigma_i(x)}{2\pi}
 e^{-\Gamma_i^2/2}.
}
```

The earliest dimensionless decision duration solves

```math
\boxed{
\rho_i(x)-\Gamma_i(x,\ell_i)-\Phi^{-1}(\beta)=0.
}
```

For a fixed physical arrival-time uncertainty `L`, define

```math
\Lambda\equiv\frac{L}{\tau_f}.
```

Then

```math
\ell_f=\Lambda,
\qquad
\ell_s=\frac{\Lambda}{r}.
```

If the dimensionless detection times are `x_f` and `x_s`, the physical decision times in fast-detector units are

```math
\boxed{
\frac{T_f}{\tau_f}=x_f,
\qquad
\frac{T_s}{\tau_f}=r x_s.
}
```

The preference statistic is therefore

```math
\boxed{
\Delta_T(\kappa_f)
=x_f-rx_s.
}
```

`Delta_T<0` means fast wins; `Delta_T>0` means slow wins.

---

## 5. Explicit finite-`r` counterexample

Use the same fixed-physics calibration introduced in Step 19:

```text
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90
```

Choose a genuinely finite speed ratio

```math
\boxed{r=2}
```

and a fixed physical timing uncertainty

```math
\boxed{
\Lambda=\frac{L}{\tau_f}=0.895.
}
```

Thus

```text
fast search interval: ell_f = 0.895
slow search interval: ell_s = 0.4475
```

and the same physical bandwidth gives

```text
kappa_s = 2 kappa_f.
```

Direct finite-duration Rice solutions give:

```text
kappa_f    T_f/tau_f      T_s/tau_f      preference
-----------------------------------------------------
20         infeasible      7.56822         slow only
25          8.02316        7.61341         slow
30          6.81840        7.65936         fast
80          7.09937        8.03871         fast
120         7.93053        8.26231         fast
140         9.11095        8.35794         slow
160        infeasible      8.44554         slow only
```

Therefore the preference sequence with increasing common readout bandwidth is

```math
\boxed{
\text{slow}
\;\longrightarrow\;
\text{fast}
\;\longrightarrow\;
\text{slow}.
}
```

This is the first explicit finite-speed-ratio demonstration of **two detector-preference reversals produced solely by sweeping the common readout bandwidth** within the present task model.

---

## 6. Two finite-band switch points

Solving

```math
T_f(\kappa_f)=T_s(\kappa_f)
```

with both detectors finite gives

```math
\boxed{
\kappa_{\times,1}
\approx25.4898402,
}
```

and

```math
\boxed{
\kappa_{\times,2}
\approx130.1945883.
}
```

At the lower switch,

```text
T_f/tau_f ~= 7.6179243
T_s/tau_f ~= 7.6179246
```

and at the upper switch,

```text
T_f/tau_f ~= 8.3121644
T_s/tau_f ~= 8.3121644.
```

Thus both reversals occur while **both detectors are feasible**. They are not merely labels attached to a feasibility onset.

---

## 7. Numerical convergence check

The finite-duration spectral integrals were evaluated directly on a symmetric frequency grid.

Using spacing

```text
dnu = 0.02
```

gives

```text
kappa_cross_1 = 25.4898401969
kappa_cross_2 = 130.194588321
```

while halving the spacing to

```text
dnu = 0.01
```

gives

```text
kappa_cross_1 = 25.4898401826
kappa_cross_2 = 130.194588861
```

The changes are approximately

```text
1.4e-8
5.4e-7
```

respectively.

**NUMERICAL VALIDATION:** the two-switch structure is not a frequency-quadrature artifact at the reported precision of the Rice calculation.

The reproducible implementation is stored in

```text
numerics/finite_r_bandwidth_reversal.py
```

---

## 8. Why two reversals occur

The sweep passes through three qualitatively different regimes.

### Regime A — narrow electronics

The slow detector captures more of its total matched-filter energy because

```math
\kappa_s=r\kappa_f.
```

In the narrow-band limit its accessible eventual SNR advantage approaches `sqrt(r)`. Slow becomes feasible first and is initially preferred.

### Regime B — intermediate electronics

The fast detector has recovered enough accessible SNR that its shorter intrinsic response dominates the physical decision time.

For the explicit example,

```text
25.49 < kappa_f < 130.19
```

is a connected fast-preferred bandwidth window under the Rice model.

### Regime C — wide electronics

Both detectors have nearly recovered their equal full-band SNR, so the low-band SNR asymmetry disappears.

But the faster detector resolves more timing structure over the same physical unknown-arrival interval and pays the larger search burden. For the chosen `Lambda=0.895`, that eventually restores the slow detector's advantage.

Thus the bandwidth sweep can change which physical effect controls the task:

```text
low bandwidth:
    accessible-SNR asymmetry favors slow

intermediate bandwidth:
    response-time advantage favors fast

high bandwidth:
    unknown-time search burden favors slow
```

---

## 9. Relation to the Step-19 finite optimum

Step 19 showed, in the large-`r` limit, that the maximum fast-preferred timing uncertainty as a function of bandwidth rises from zero, reaches a finite maximum, and then falls slightly toward its infinite-band value.

The finite-`r` double reversal above is the corresponding two-dimensional manifestation.

At fixed

```math
\Lambda=0.895,
```

the horizontal task line intersects the finite-`r` fast/slow boundary twice.

Therefore the finite-`r` task boundary is **nonmonotone in bandwidth** for this example. Under ordinary continuity, this also implies a finite-band maximum of the fast-preferred timing-uncertainty boundary.

**REFINEMENT:** the finite-bandwidth optimum is not merely an artifact of sending `r -> infinity`; a nonmonotone bandwidth dependence survives already at `r=2` in the finite-duration Rice calculation.

---

## 10. Illustrative physical bandwidth translation

If, purely for scale, one sets

```text
tau_f = 1 ns
```

and defines

```math
f_B=\frac{\Omega_B}{2\pi},
```

then

```text
kappa_cross_1 ~= 25.48984 -> f_B ~= 4.057 GHz
kappa_cross_2 ~=130.19459 -> f_B ~=20.721 GHz.
```

These are **not** circuit `-3 dB` bandwidth recommendations. `f_B` remains the Gaussian information-band scale of the controlled surrogate.

---

## 11. Scope and unresolved exactness

### ESTABLISHED WITHIN THE FINITE-DURATION RICE MODEL

- A common physical bandwidth gives the slower detector greater accessible eventual SNR at every finite bandwidth in the equal-full-band-SNR time-scaled family.
- The narrow-band accessible-SNR ratio tends to `sqrt(r)`.
- At finite `r=2`, a fixed task can exhibit two preference reversals as bandwidth is swept.
- The two reported Rice switch points survive a factor-of-two frequency-grid refinement.
- The finite-`r` fast/slow boundary can therefore be nonmonotone in bandwidth.

### OPEN / NOT CLAIMED

- The exact Palm-corrected switch values have not yet been computed.
- Step 17 showed that Rice accuracy becomes nonuniform for finite hard windows as `kappa` grows, so the upper switch is especially deserving of a Palm check.
- No claim that every `r`, `Lambda`, `rho_full`, `alpha`, or `beta` exhibits two switches.
- No proof that there are at most two reversals.
- No claim that the Gaussian information-band surrogate is a literal electronics transfer function.
- No hardware-optimal bandwidth claim.
- No novelty claim.

---

## 12. First nontrivial consequence

**NUMERICAL COUNTEREXAMPLE / CONDITIONAL:** readout bandwidth is not merely a monotonic nuisance parameter that moves one fast/slow boundary. Even for only a factor-of-two detector speed difference, the preferred detector can switch twice as the same physical bandwidth is increased:

```math
\boxed{
\text{slow}\to\text{fast}\to\text{slow}.
}
```

That means detector selection cannot, in general, be ordered independently of the readout bandwidth and the allowed arrival-time uncertainty, even after the underlying full-band detector SNRs have been matched.

---

## 13. Stopping point

The multiple-reversal phenomenon is established at the finite-duration Rice level and numerically converged with respect to the spectral quadrature used here.

### Single natural next question

> Does the exact continuous Palm correction preserve both finite-`r` bandwidth reversals, especially the high-bandwidth switch where finite-window Rice accuracy is least uniform, and how far do the two switch points move?
