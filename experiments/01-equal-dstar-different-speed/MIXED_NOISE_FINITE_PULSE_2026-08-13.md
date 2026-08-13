# Finite optical pulse + mixed detector noise

**Date:** 2026-08-13  
**Status:** EXACT FULL-RECORD INFORMATION RESULT / PHYSICAL BRIDGE TO PAPER A

## 1. Model

Use a finite-energy exponential optical event with unit area,

```math
p(t)=\frac{1}{\tau_p}e^{-t/\tau_p}u(t),
```

so, in angular frequency,

```math
|P(\omega)|^2
=\frac{1}{1+\omega^2\tau_p^2}.
```

Let the detector be first order,

```math
G_\tau(i\omega)
=\frac{R_{dc}(\tau)}{1+i\omega\tau}.
```

Include two independent white-noise sources:

1. `N_in`: noise entering before the detector response and therefore shaped by `G_tau` exactly like the optical signal;
2. `N_out`: additive noise entering after the detector response.

The output-noise PSD is

```math
S_{n,\tau}(\omega)
=N_{in}|G_\tau|^2+N_{out}.
```

---

## 2. Exact whitened information spectrum

The matched-filter information density is

```math
\mathcal I_\tau(\omega)
=\frac{|P(\omega)|^2|G_\tau(\omega)|^2}
{N_{in}|G_\tau(\omega)|^2+N_{out}}.
```

Define the dimensionless low-frequency common-path/output-noise ratio

```math
\boxed{
\lambda_\tau
=\frac{N_{in}R_{dc}^2(\tau)}{N_{out}}.
}
```

Then define an **effective detector information time**

```math
\boxed{
\tau_I(\tau)
=\frac{\tau}{\sqrt{1+\lambda_\tau}}.
}
```

Direct reduction gives

```math
\boxed{
\mathcal I_\tau(\omega)
=I_0(\tau)
\frac{1}
{(1+\omega^2\tau_p^2)(1+\omega^2\tau_I^2)},
}
```

where

```math
\boxed{
I_0(\tau)
=\frac{1}{N_{in}+N_{out}/R_{dc}^2(\tau)}.
}
```

Thus the complete signal/noise problem factorizes into two information time scales:

- the optical-event time `tau_p`;
- the detector/noise information time `tau_I`, which is generally **not equal** to the raw detector response time `tau`.

This distinction is physically important. The response time seen on an oscilloscope and the time scale that controls the optimally whitened detection statistic need not be the same.

---

## 3. Exact eventual matched-filter SNR

Using

```math
\rho_\infty^2
=\frac{1}{2\pi}\int_{-\infty}^{\infty}
\mathcal I_\tau(\omega)d\omega,
```

and

```math
\frac{1}{2\pi}\int_{-\infty}^{\infty}
\frac{d\omega}
{(1+\omega^2a^2)(1+\omega^2b^2)}
=\frac{1}{2(a+b)},
```

one obtains

```math
\boxed{
\rho_\infty^2(\tau)
=\frac{I_0(\tau)}{2(\tau_p+\tau_I(\tau))}.
}
```

Equivalently,

```math
\boxed{
\rho_\infty^2
=\frac{R_{dc}^2}
{2N_{out}(1+\lambda_\tau)
\left(\tau_p+\tau/\sqrt{1+\lambda_\tau}\right)}.
}
```

### Common-path limit

As `N_out -> 0`,

```math
I_0\to1/N_{in},
\qquad
\tau_I\to0,
```

and therefore

```math
\boxed{
\rho_\infty^2
\to\frac{1}{2N_{in}\tau_p},
}
```

independent of detector responsivity and detector response time.

This is the finite-pulse version of the common-path cancellation theorem and avoids the infinite-bandwidth singularity of an ideal delta pulse.

### Output-noise limit

As `N_in -> 0`,

```math
\tau_I\to\tau,
```

so

```math
\boxed{
\rho_\infty^2
\to\frac{R_{dc}^2}
{2N_{out}(\tau_p+\tau)}.
}
```

For `tau_p << tau`, this reduces to the short-pulse scaling

```math
\rho_\infty^2\propto R_{dc}^2/\tau
```

used in the responsivity--speed exponent analysis.

---

## 4. Exact timing-scan covariance

The full-template timing covariance is the normalized inverse Fourier transform of `mathcal I_tau`.

For

```math
\tau_p\ne\tau_I,
```

partial fractions give

```math
\boxed{
R_\tau(\Delta)
=\frac{
\tau_p e^{-|\Delta|/\tau_p}
-\tau_I e^{-|\Delta|/\tau_I}
}{\tau_p-\tau_I}.
}
```

This is normalized so that

```math
R_\tau(0)=1.
```

When the two information time scales become equal,

```math
\tau_I\to\tau_p,
```

L'Hopital's rule gives

```math
\boxed{
R_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau_p}\right)
 e^{-|\Delta|/\tau_p}.
}
```

This is exactly the Matérn-3/2 / Gamma(2)-template covariance used as the full-template process in Paper A.

### Important interpretation

The Paper-A covariance is therefore not merely an arbitrary convenient Gaussian process. It appears exactly as the **equal-information-timescale limit** of a first-order optical pulse + first-order detector + mixed-noise model.

The equality condition is

```math
\boxed{
\tau_I=\tau_p
\quad\Longleftrightarrow\quad
\lambda_\tau
=\left(\frac{\tau}{\tau_p}\right)^2-1.
}
```

This requires `tau >= tau_p`.

For one channel, that condition defines a physically interpretable parameter manifold on which the optimal timing-scan covariance is exactly Paper A's analytic covariance.

It does **not** by itself prove that an entire fast/slow Paper-A scaling family can be realized with one fixed optical pulse and one fixed noise budget; the required `lambda_tau` generally changes with detector parameters. The significance is narrower: the covariance shape itself has a direct mixed-noise first-order realization.

---

## 5. Noise-path limits of the timing covariance

### Common-path dominated

As `N_out -> 0`, `tau_I -> 0`, and

```math
R_\tau(\Delta)
\to e^{-|\Delta|/\tau_p}.
```

The detector time constant disappears. The timing-search geometry is set only by the optical event.

### Output-noise dominated

As `N_in -> 0`, `tau_I -> tau`, and

```math
R_\tau(\Delta)
=\frac{
\tau_p e^{-|\Delta|/\tau_p}
-\tau e^{-|\Delta|/\tau}
}{\tau_p-\tau}.
```

Now detector response time directly reshapes the whitened timing scan.

Thus the transition from detector-invariant to detector-dependent search geometry is continuous and controlled by the physically meaningful ratio `lambda_tau`.

---

## 6. New conceptual picture

The physically relevant time scales are now:

```text
optical event:       tau_p
raw detector speed:  tau
information speed:   tau_I = tau/sqrt(1+lambda_tau)
```

The raw detector response time is not, in general, the timing correlation scale seen by an optimal detector.

The same noise partition also controls the available eventual SNR through

```math
rho_infinity^2 = I_0/[2(tau_p+tau_I)].
```

So physical detector comparison requires both:

1. the amplitude factor `I_0`, which describes how much whitened information is available;
2. the information time `tau_I`, which describes how that information is distributed in frequency/time and therefore how large an unknown-arrival search appears.

This is a direct physical extension of Paper A's abstract task surface.

---

## 7. What this establishes

Established exactly for the finite exponential pulse, first-order detector, and two-white-noise-path model:

1. the whitened information spectrum factorizes into optical and detector/noise Lorentzians;
2. the detector enters through an effective information time `tau_I`, not raw `tau` alone;
3. the common-path limit removes detector response from both eventual SNR and timing covariance;
4. the output-noise limit restores direct detector-response dependence;
5. Paper A's full-template covariance `(1+|Delta|/tau)e^{-|Delta|/tau}` is the exact equal-information-timescale limit of this physically linked model.

The next question is whether two channels with physically linked `R_dc(tau)` and a common fixed noise budget can still exhibit the Paper-A unknown-arrival guarantee-time reversal, and in what region of `(g, N_in/N_out, tau_p)` that occurs.