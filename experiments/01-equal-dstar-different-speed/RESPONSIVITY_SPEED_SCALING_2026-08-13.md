# Responsivity--speed scaling extension

**Date:** 2026-08-13  
**Status:** EXACT KNOWN-ARRIVAL RESULT / PHYSICAL LINKAGE EXTENSION

## 1. Minimal physically linked first-order model

Take a detector with first-order small-signal transfer function

```math
G_\tau(s)=\frac{R_{dc}(\tau)}{1+s\tau},
```

where `tau` is the response time and `R_dc(tau)` is the DC responsivity.

For an optical pulse short compared with the detector response time, use the impulsive limit. The electrical signal is then

```math
s_\tau(t)
=\frac{R_{dc}(\tau)}{\tau}e^{-t/\tau}u(t).
```

Assume, for this step only, additive white **post-response** output noise

```math
E[n(t)n(t')]=N\delta(t-t').
```

This is the opposite limiting case from the common-path cancellation model. It makes the responsivity--speed linkage explicit before the two noise paths are combined.

Parameterize the responsivity scaling by

```math
\boxed{
R_{dc}(\tau)
=R_r\left(\frac{\tau}{\tau_r}\right)^g,
}
```

where `g` is a dimensionless responsivity--lifetime exponent.

---

## 2. Finite-time matched-filter evidence

The accumulated known-arrival matched-filter SNR is

```math
\rho^2(t;\tau)
=\frac{1}{N}\int_0^t s_\tau^2(u)du.
```

Therefore

```math
\boxed{
\rho^2(t;\tau)
=C\tau^{2g-1}
\left(1-e^{-2t/\tau}\right),
}
```

where

```math
C=\frac{R_r^2}{2N\tau_r^{2g}}
```

under the chosen units.

The eventual SNR is

```math
\boxed{
\rho_\infty(\tau)
\propto \tau^{g-1/2}.
}
```

Thus `g=1/2` is the exact boundary between increasing and decreasing eventual sensitivity with response time.

---

## 3. Exact fast/slow evidence ratio

Let

```math
\tau_s=r\tau_f,
\qquad r>1.
```

At one common physical integration time `t`,

```math
\boxed{
\frac{\rho_s^2(t)}{\rho_f^2(t)}
=r^{2g-1}
\frac{1-e^{-2t/(r\tau_f)}}
{1-e^{-2t/\tau_f}}.
}
```

Define

```math
q_r(t)
=\frac{1-e^{-2t/(r\tau_f)}}
{1-e^{-2t/\tau_f}}.
```

For every `r>1`, `q_r(t)` increases strictly with `t` from

```math
\lim_{t\to0^+}q_r(t)=1/r
```

to

```math
\lim_{t\to\infty}q_r(t)=1.
```

A compact proof uses

```math
a=e^{-2t/(r\tau_f)},
\qquad e^{-2t/\tau_f}=a^r,
```

so

```math
q_r=\frac{1-a}{1-a^r}.
```

Then

```math
\frac{dq_r}{da}
=\frac{-1+r a^{r-1}-(r-1)a^r}
{(1-a^r)^2}<0
```

for `0<a<1`, because

```math
r a^{r-1}-(r-1)a^r<1.
```

Since `a` decreases with `t`, `q_r(t)` increases strictly.

Therefore the slow/fast squared-SNR ratio itself increases monotonically with physical integration time.

Its limiting values are

```math
\boxed{
\lim_{t\to0^+}
\frac{\rho_s^2}{\rho_f^2}
=r^{2g-2},
}
```

and

```math
\boxed{
\lim_{t\to\infty}
\frac{\rho_s^2}{\rho_f^2}
=r^{2g-1}.
}
```

---

## 4. Exact phase diagram

These two limits plus monotonicity give a complete known-arrival ordering classification.

### Regime I: `g<1/2`

```math
r^{2g-2}<r^{2g-1}<1.
```

Hence

```math
\boxed{
\rho_f(t)>\rho_s(t)
\quad\text{for every finite }t>0.
}
```

The faster detector has both the larger early evidence rate and larger eventual SNR.

### Regime II: `g=1/2`

The eventual SNRs are equal:

```math
\rho_{\infty,f}=\rho_{\infty,s}.
```

For every finite time,

```math
\boxed{\rho_f(t)>\rho_s(t),}
```

with equality approached only as `t->infinity`.

This is precisely the **equal-eventual-SNR first-order normalization used in the Paper-A robustness corollary**. In transfer-function language, Paper A's amplitude scaling `A_tau proportional tau^{-1/2}` corresponds to

```math
R_{dc}(\tau)=A_\tau\tau\propto\sqrt\tau,
```

so Paper A sits exactly at the critical exponent

```math
\boxed{g=1/2.}
```

### Regime III: `1/2<g<1`

At early times,

```math
r^{2g-2}<1,
```

so fast initially has more evidence.

Eventually,

```math
r^{2g-1}>1,
```

so slow has more total available evidence.

Because the ratio is strictly increasing, there is **exactly one known-arrival evidence crossover**:

```math
\boxed{
\exists!\ t_\times>0:
\rho_f(t_\times)=\rho_s(t_\times).
}
```

It is determined implicitly by

```math
r^{2g-1}
\left(1-e^{-2t_\times/(r\tau_f)}\right)
=1-e^{-2t_\times/\tau_f}.
```

For example, `r=6`, `g=3/4` gives

```math
t_\times\approx1.4656\tau_f.
```

This crossover exists even with perfectly known arrival time. Unknown-arrival search is not required to create it.

### Regime IV: `g=1`

The early-time evidence rates are equal in the `t->0` limit, but for every finite `t>0`,

```math
\boxed{\rho_s(t)>\rho_f(t).}
```

The slower detector dominates thereafter.

A simple photoconductive-gain scaling `R_dc proportional tau` falls in this idealized class if transit time and output white-noise level are held fixed. Real photoconductor noise also changes with lifetime, so this is a scaling illustration, not a complete device model.

### Regime V: `g>1`

```math
\boxed{\rho_s(t)>\rho_f(t)}
```

from the outset; the slower detector has both greater early and eventual evidence.

---

## 5. Physical interpretation

The exponent `g` separates three logically distinct mechanisms:

- response speed controls how quickly one detector-time unit passes;
- responsivity scaling controls signal amplitude as `tau` changes;
- noise placement controls whether that amplitude/bandwidth change survives whitening.

The Paper-A equal-eventual-SNR construction is therefore not an arbitrary isolated point in this family. It is the exact **critical boundary `g=1/2`** between fast-eventual and slow-eventual sensitivity under white post-response noise.

At this boundary, faster response retains the strongest possible known-arrival finite-time advantage while removing eventual SNR as a confounding variable. The unknown-arrival timing search can then overturn that otherwise strict finite-time preference.

For `1/2<g<1`, a slower detector already gains an eventual-sensitivity advantage, so an unknown-arrival search penalty is no longer the sole mechanism capable of producing a reversal.

---

## 6. What this establishes

Established exactly for the stated first-order/short-pulse/output-white-noise model:

1. `g=1/2` is a critical responsivity--speed exponent.
2. Paper A's equal-eventual-SNR normalization corresponds exactly to this boundary.
3. `g<1/2`: fast dominates known-arrival accumulated SNR at all finite times.
4. `1/2<g<1`: there is exactly one known-arrival evidence crossover.
5. `g>=1`: slow dominates known-arrival evidence for every finite time (strictly for `t>0`).

Not yet included:

- common-path detector noise;
- finite optical pulse duration comparable with `tau`;
- colored/readout noise;
- unknown-arrival global-threshold ordering in the general `g` family.

The next step is to combine this responsivity law with the common-path/output-noise mixture from `PHYSICAL_NOISE_COUPLING_2026-08-13.md`.