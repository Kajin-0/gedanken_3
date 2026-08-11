# Step 18 — Same Physical Readout Bandwidth and Electronics-Limited Crossover

**Date:** 2026-08-11 15:22 EDT  
**Status:** DERIVED / ASYMPTOTIC / NEGATIVE RESULT / REFINEMENT. Both detectors are now constrained by the same physical information-band scale `Omega_B`, so `kappa_f=Omega_B tau_f` and `kappa_s=Omega_B tau_s` differ. The large-speed-ratio fast-feasibility-edge law survives when the slow channel is itself well resolved relative to the electronics (`kappa_s -> infinity`, or more generally `ell_crit(kappa_f)/r -> 0`). In the high-threshold Rice limit the physical crossover changes continuously from an electronics-limited scale `~1/Omega_B` to an intrinsic-detector scale `~tau_f`. Under the deliberately equal-accessible-eventual-SNR normalization used here, changing bandwidth shifts the fast/slow boundary monotonically but does **not** produce an interior optimal bandwidth. A real bandwidth optimum remains open because changing physical bandwidth would ordinarily also change eventual SNR. No novelty claim.

---

## 1. Question

Steps 14–17 compared a similarity-preserving family with the same dimensionless timing bandwidth

```math
\kappa=\Omega_B\tau
```

for every detector. That required the physical bandwidth to scale as `1/tau`.

Now impose a more literal shared readout:

```math
\boxed{\Omega_{B,f}=\Omega_{B,s}=\Omega_B.}
```

Then

```math
\boxed{\kappa_f=\Omega_B\tau_f,}
```

```math
\boxed{\kappa_s=\Omega_B\tau_s=r\kappa_f,}
```

where

```math
r=\tau_s/\tau_f>1.
```

Question:

> Does the large-`r` crossover law survive, and can the common electronics bandwidth itself change or optimize which detector wins?

---

## 2. Controlled comparison used in this step

Retain the Step-15 Gaussian information weighting as the explicit finite-band surrogate,

```math
J_{x,\kappa}(\nu)
=|H_x(\nu)|^2e^{-(\nu/\kappa)^2},
```

but now evaluate the two detectors at different `kappa_f` and `kappa_s` set by the same physical `Omega_B`.

To isolate timing/search effects, normalize the two detector/readout combinations to the same **accessible eventual matched-filter SNR**

```math
\rho_{\infty,f}=\rho_{\infty,s}=\rho_0.
```

This is an important assumption. It is not the same as taking one fixed physical detector and sweeping its electronics bandwidth while leaving its signal and noise amplitudes unchanged.

Under this controlled normalization,

```math
T_{D,f}
=\tau_f X_D\!\left(\rho_0,\alpha,\beta,
\frac{L}{\tau_f},\kappa_f\right),
```

```math
T_{D,s}
=\tau_s X_D\!\left(\rho_0,\alpha,\beta,
\frac{L}{\tau_s},\kappa_s\right).
```

There is no longer one universal dimensionless `kappa` shared by the pair.

---

## 3. Finite-`r` crossover identity with common physical bandwidth

At equal physical decision time write

```math
x_s=x,
\qquad
x_f=rx.
```

Also write

```math
\ell_s=\ell,
\qquad
\ell_f=r\ell.
```

The signal margins are now

```math
u_s
=\rho_0\mathcal R_{\kappa_s}(x)-\Phi^{-1}(\beta),
```

```math
u_f
=\rho_0\mathcal R_{\kappa_f}(rx)-\Phi^{-1}(\beta).
```

For the smooth Palm formulation from Step 16, let `sigma_s,sigma_f` be the finite-scan derivative standard deviations and `C_s,C_f` the corresponding Palm correction factors. Then the exact smooth-process crossover identity is still

```math
\boxed{
\frac{[\alpha-Q(u_f)]e^{u_f^2/2}}
{\sigma_f C_f}
=
r
\frac{[\alpha-Q(u_s)]e^{u_s^2/2}}
{\sigma_s C_s},
}
```

but the two sides are evaluated at

```math
\kappa_f=\Omega_B\tau_f,
\qquad
\kappa_s=r\kappa_f.
```

Thus the Step-17 algebraic structure survives; the earlier similarity reduction does not.

---

## 4. Large-`r` limit — condition needed

A subtlety appears immediately.

At a candidate fast-feasibility-edge crossover,

```math
\ell_s
=\frac{L}{\tau_s}
\sim
\frac{\ell_{crit}(\kappa_f)}{r}.
```

Therefore the slow detector approaches a known-arrival-time problem only if

```math
\boxed{
\frac{\ell_{crit}(\kappa_f)}{r}\to0.
}
```

For fixed `tau_f` and fixed physical `Omega_B`, `kappa_f` is fixed and this condition holds automatically as `r->infinity`.

In the electronics-limited regime derived below,

```math
\ell_{crit}(\kappa_f)\propto1/\kappa_f,
```

so the same condition becomes approximately

```math
r\kappa_f=\kappa_s\to\infty.
```

Hence:

**REFINEMENT:** under common physical bandwidth, `r->infinity` by itself is not enough to justify the Step-17 known-time-slow argument if `kappa_f` is simultaneously allowed to collapse like `1/r`. The clean large-`r` law requires the slow detector to span many electronics correlation times, equivalently `kappa_s` large enough that `ell_s` becomes negligible.

For the original `tau_f=1 ns`, `tau_s=1 s` pair, this condition is overwhelmingly satisfied for any ordinary MHz-or-higher readout information scale.

---

## 5. Exact large-`r` law with fixed physical electronics

Assume the condition above and track the same fast-to-slow branch.

Then

```math
\ell_s\to0,
```

so the slow detector approaches its known-time decision duration, while

```math
x_f=rx_s\to\infty.
```

The fast detector therefore uses its full accessible template at its own fixed

```math
\kappa_f=\Omega_B\tau_f.
```

Define

```math
u_\infty
\equiv
\rho_0-\Phi^{-1}(\beta)
```

and define the fast detector's exact full-template normalized feasibility edge by

```math
\boxed{
\Gamma_{\infty,\kappa_f}
(\ell_{crit}(\kappa_f),\alpha)
=u_\infty.
}
```

Then the Step-17 result generalizes directly:

```math
\boxed{
\frac{L_\times}{\tau_f}
\to
\ell_{crit}(\kappa_f),
}
```

or

```math
\boxed{
L_\times
\to
\tau_f\,
\ell_{crit}(\Omega_B\tau_f).
}
```

**DERIVED / CONDITIONAL:** the large-speed-ratio law survives a common physical readout bandwidth. The only leading-order bandwidth dependence enters through the fast detector's dimensionless electronics bandwidth `Omega_B tau_f`.

---

## 6. Full-template timing bandwidth in the Gaussian regularizer

For the full fast template,

```math
H_\infty(\nu)=\frac1{(1+i\nu)^2},
```

so the regularized timing spectrum is proportional to

```math
\frac{e^{-(\nu/\kappa)^2}}
{(1+\nu^2)^2}.
```

Its derivative variance is

```math
\boxed{
\sigma_\infty^2(\kappa)
=
\frac{
\int_{-\infty}^{\infty}
\frac{\nu^2e^{-(\nu/\kappa)^2}}
{(1+\nu^2)^2}\,d\nu
}{
\int_{-\infty}^{\infty}
\frac{e^{-(\nu/\kappa)^2}}
{(1+\nu^2)^2}\,d\nu
}.
}
```

This function is strictly increasing with `kappa`.

To see this, write

```math
s=\kappa^{-2}
```

and normalize

```math
p_s(\nu)
\propto
\frac{e^{-s\nu^2}}{(1+\nu^2)^2}.
```

Then

```math
\sigma_\infty^2=E_s[\nu^2]
```

and

```math
\boxed{
\frac{d}{ds}\sigma_\infty^2
=-\operatorname{Var}_s(\nu^2)<0.
}
```

Since `ds/dkappa<0`,

```math
\boxed{
\frac{d}{d\kappa}\sigma_\infty^2(\kappa)>0.
}
```

Thus increasing accessible physical timing bandwidth always increases the fast full-template timing-search curvature in this normalized model.

---

## 7. High-threshold Rice form

In the isolated-excursion approximation, define the task constant

```math
\boxed{
\mathcal C(\rho_0,\alpha,\beta)
=2\pi
[\alpha-Q(u_\infty)]
e^{u_\infty^2/2}.
}
```

Then

```math
\boxed{
\ell_{crit}^{Rice}(\kappa_f)
=\frac{\mathcal C}{\sigma_\infty(\kappa_f)},
}
```

and therefore

```math
\boxed{
L_\times^{Rice}
\sim
\tau_f
\frac{\mathcal C}
{\sigma_\infty(\Omega_B\tau_f)}.
}
```

Because `sigma_infinity(kappa)` increases monotonically, the normalized equal-`rho_0` crossover decreases monotonically with physical electronics bandwidth.

---

## 8. Two asymptotic physical regimes

### Electronics-limited fast channel: `Omega_B tau_f << 1`

For small `kappa`, the full-template factor is nearly constant across the narrow information band, so

```math
\sigma_\infty^2(\kappa)
=\frac{\kappa^2}{2}+O(\kappa^4),
```

or

```math
\boxed{
\sigma_\infty(\kappa)
\sim\frac{\kappa}{\sqrt2}.
}
```

Hence

```math
\boxed{
L_\times^{Rice}
\sim
\frac{\sqrt2\,\mathcal C}{\Omega_B}.
}
```

The intrinsic `tau_f` cancels.

**FIRST NONTRIVIAL CONSEQUENCE:** once the fast detector is substantially faster than the accessible electronics, making the detector still faster no longer moves the crossover at leading order. The task boundary is set by the readout timing scale `1/Omega_B`.

### Detector-limited / wide-readout channel: `Omega_B tau_f >> 1`

Without the Gaussian penalty,

```math
\int_{-\infty}^{\infty}\frac{d\nu}{(1+\nu^2)^2}
=\frac\pi2,
```

and

```math
\int_{-\infty}^{\infty}
\frac{\nu^2d\nu}{(1+\nu^2)^2}
=\frac\pi2.
```

Therefore

```math
\boxed{
\sigma_\infty(\kappa)\to1,
}
```

so

```math
\boxed{
L_\times^{Rice}
\to
\mathcal C\,\tau_f.
}
```

The electronics no longer limits timing information; the intrinsic fast-detector time scale sets the crossover.

---

## 9. Illustrative numbers for the original `1 ns` versus `1 s` pair

Use **only** the Step-16 validation task

```text
rho_0 = 6.2
alpha = 1e-6
beta = 0.90
```

for which

```text
u_infinity ~= 4.918448434
C ~= 0.634410768.
```

For `tau_f=1 ns`, define the convenient information-band frequency

```math
f_B=\Omega_B/(2\pi).
```

The large-`r` Rice crossover for the Gaussian information-band model is approximately

```text
f_B          kappa_f          L_cross^Rice
1 MHz        0.00628          142.8 ns
10 MHz       0.0628            14.34 ns
100 MHz      0.628              1.802 ns
1 GHz        6.283              0.747 ns
10 GHz       62.83              0.646 ns
infinite     infinity            0.634 ns
```

These are **illustrative task/model values**, not hardware recommendations or real photodetector predictions. `f_B` is the scale parameter of the Gaussian information weighting, not automatically a circuit `-3 dB` bandwidth.

The useful structural result is the transition

```text
narrow electronics -> L_cross set mainly by 1/Omega_B
wide electronics   -> L_cross set mainly by tau_f.
```

---

## 10. Does bandwidth optimize which detector wins?

Within the deliberately normalized equal-accessible-eventual-SNR comparison, no interior optimum appears in the large-`r` limit.

Since

```math
\sigma_\infty(\kappa)
```

is strictly increasing,

```math
L_\times^{Rice}
\propto1/\sigma_\infty(\Omega_B\tau_f)
```

is strictly decreasing with `Omega_B`.

Thus reducing timing bandwidth pushes the fast-to-slow crossover to larger arrival-time uncertainty: the fast detector wins over a larger task region because the electronics removes timing-search degrees of freedom.

But this is **not a free physical optimization**, because this step renormalized every bandwidth choice to the same accessible eventual SNR `rho_0`.

For an actual fixed detector/readout chain, reducing bandwidth generally changes

```text
available signal energy,
noise covariance,
eventual SNR,
and finite-time accumulation
```

simultaneously.

**NEGATIVE RESULT / QUALIFICATION:** there is no interior bandwidth optimum in the present equal-`rho_0` large-`r` comparison. A genuine physical optimum cannot be inferred until `rho_infinity(Omega_B)` is allowed to change with the electronics.

---

## 11. Large-`r` path dependence

The phrase `r -> infinity` must now be qualified.

### Path A — hold `tau_f` and `Omega_B` fixed, make the slow detector slower

Then

```math
\kappa_f=\Omega_B\tau_f
```

is fixed and

```math
\kappa_s=r\kappa_f\to\infty.
```

The clean law

```math
L_\times\to\tau_f\ell_{crit}(\kappa_f)
```

holds.

### Path B — hold `tau_s` and `Omega_B` fixed, make the fast detector arbitrarily fast

Then

```math
\kappa_f=\frac{\kappa_s}{r}\to0.
```

The fast channel becomes electronics-limited. Its own feasibility scale tends to `~1/Omega_B`, rather than continuing to collapse with `tau_f`.

If `kappa_s` is also large, the same fast-edge law remains self-consistent and gives the electronics-limited result above. If `kappa_s` is not large, the slow detector does not approach known-time operation and the simple one-edge asymptote is insufficient.

**REFINEMENT:** extreme detector-speed ratio and extreme detector-speed advantage are not synonymous once a common electronics timescale exists.

---

## 12. What has been established

- **DERIVED:** with common physical bandwidth, the finite-`r` Palm/Rice crossover identity survives but uses `kappa_f != kappa_s`.
- **DERIVED / CONDITIONAL:** if `ell_crit(kappa_f)/r -> 0` (in particular for fixed `tau_f,Omega_B` and `r->infinity`), then

```math
L_\times\to\tau_f\ell_{crit}(\Omega_B\tau_f).
```

- **DERIVED:** for the full-template Gaussian information-band model, `sigma_infinity(kappa)` is strictly increasing with bandwidth.
- **DERIVED / HIGH-THRESHOLD:** the physical crossover interpolates between

```math
L_\times\sim\sqrt2\mathcal C/\Omega_B
```

for electronics-limited timing and

```math
L_\times\sim\mathcal C\tau_f
```

for detector-limited timing.
- **DERIVED:** an intrinsic detector can become so fast that common electronics, not `tau_f`, sets the task crossover.
- **NEGATIVE RESULT / QUALIFICATION:** no interior bandwidth optimum exists under the equal-accessible-eventual-SNR normalization; a genuine physical optimum remains open.

---

## 13. What has not been established

- No bandwidth optimum for a fixed physical detector with `rho_infinity(Omega_B)` allowed to vary.
- No exact Palm correction to the full fixed-physical-bandwidth phase surface over all `Omega_B`.
- No simple large-`r` one-edge law when `kappa_s` remains finite enough that the slow channel is not near known-time operation.
- No claim that the Gaussian information weighting is a literal circuit transfer function or that `f_B` is a `-3 dB` bandwidth.
- No proof of crossover uniqueness for all fixed-bandwidth parameter choices.
- No universal detector ranking, universal replacement metric, or novelty claim.

---

## 14. Stopping point

The shared-electronics problem reveals a new physical scale hierarchy:

```text
intrinsic detector time tau_f
versus
electronics information time 1/Omega_B.
```

The fast/slow task boundary is controlled by whichever limitation prevents the fast channel from providing arbitrarily fine useful timing information.

### Single natural next question

> If the physical detector signal and noise amplitudes are now held fixed while `Omega_B` is varied—so that reducing bandwidth can also reduce eventual SNR—does the competition between SNR loss and timing-search relief produce a genuine finite optimal readout bandwidth for unknown-time detection?
