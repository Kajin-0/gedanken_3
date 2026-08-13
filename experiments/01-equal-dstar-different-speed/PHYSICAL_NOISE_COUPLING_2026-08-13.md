# Physical noise coupling extension

**Date:** 2026-08-13  
**Status:** FIRST-PRINCIPLES EXTENSION / SEPARATE FROM STEP-13--49 HARD STOP

## Question

Paper A deliberately imposed equal event-specific eventual matched-filter SNR with additive output white noise. The natural next question is what survives when signal, response time, responsivity, and detector noise are physically linked rather than normalized independently.

The first useful distinction is **where the noise enters relative to the detector transfer function**.

---

## 1. Common-path noise: detector response cancels

Let one optical event have spectrum

```math
P(f)e^{-i2\pi f\theta},
```

where `theta` is the unknown arrival time. Let the detector transfer function be `G_tau(f)`.

Suppose the signal and a stationary white input-noise process pass through the same linear detector channel:

```math
Y(f)
=G_\tau(f)P(f)e^{-i2\pi f\theta}
+G_\tau(f)W(f),
```

with

```math
S_W(f)=N_{in}.
```

The output-noise PSD is therefore

```math
S_{n,\tau}(f)=N_{in}|G_\tau(f)|^2.
```

For full-record optimal matched filtering, the frequency-resolved information density is

```math
\mathcal I_\tau(f)
=\frac{|G_\tau(f)P(f)|^2}
{N_{in}|G_\tau(f)|^2}
=\boxed{\frac{|P(f)|^2}{N_{in}}},
```

wherever `G_tau(f)` is nonzero.

Hence

```math
\boxed{
\rho_{\infty}^2
=\int \mathcal I_\tau(f)df
=\frac{1}{N_{in}}\int|P(f)|^2df
}
```

is independent of detector response time.

The normalized timing-scan covariance is likewise determined by

```math
R(\Delta)
=\frac{\int \mathcal I_\tau(f)e^{i2\pi f\Delta}df}
{\int \mathcal I_\tau(f)df},
```

so it is also independent of `G_tau`.

### Consequence

If **all relevant noise is shaped by exactly the same invertible detector response as the signal**, then under ideal full-record optimal processing the detector time constant carries no detection information by itself.

The response slows the observed waveform, but it slows the noise in precisely the compensating way. Whitening removes both together.

This is a genuine boundary of Paper A: the task-dependent timing-search mechanism requires some detector-dependent change in the whitened information spectrum. It cannot arise merely from applying the same invertible filter to both signal and all noise.

This statement assumes no zeros that destroy information in the signal band, ideal continuous observation, and no additional measurement constraints. Finite records, noninvertible filtering, digitizer bandwidth, or downstream noise can reintroduce detector dependence.

---

## 2. Mixed noise: only the non-common-path component survives the cancellation

Now add a second stationary noise source after the detector transfer function:

```math
Y(f)
=G_\tau(f)P(f)e^{-i2\pi f\theta}
+G_\tau(f)W_{in}(f)
+W_{out}(f),
```

with independent white PSDs

```math
S_{in}=N_{in},
\qquad
S_{out}=N_{out}.
```

Then

```math
S_{n,\tau}(f)
=N_{in}|G_\tau(f)|^2+N_{out}.
```

The information spectrum becomes

```math
\boxed{
\mathcal I_\tau(f)
=\frac{|P(f)|^2|G_\tau(f)|^2}
{N_{in}|G_\tau(f)|^2+N_{out}}
=\frac{|P(f)|^2}
{N_{in}+N_{out}/|G_\tau(f)|^2}.
}
```

This equation is the central result of this extension.

It shows that detector response affects optimal detection only through the portion of the noise that is **not transformed in the same way as the signal**.

Limits:

```math
N_{out}=0
\quad\Longrightarrow\quad
\mathcal I_\tau(f)=|P(f)|^2/N_{in},
```

so detector response cancels completely.

Conversely,

```math
N_{in}=0
\quad\Longrightarrow\quad
\mathcal I_\tau(f)=|P(f)|^2|G_\tau(f)|^2/N_{out},
```

so detector gain and bandwidth enter maximally.

For intermediate mixtures, response-time dependence turns on continuously with the non-common-path noise fraction.

---

## 3. Deeper interpretation

The physically relevant object is not response time alone and not a scalar sensitivity number. For an optimal linear Gaussian detection task it is the **whitened information spectrum**

```math
\boxed{
\mathcal I_\tau(f)
=\frac{|S_\tau(f)|^2}{S_{n,\tau}(f)}.
}
```

It determines both

```math
\rho_\infty^2=\int\mathcal I_\tau(f)df
```

and the timing-search covariance through its normalized Fourier transform.

Thus a detector time constant matters only insofar as changing it changes `mathcal I_tau(f)` after signal and noise are treated together.

This gives a sharper physical boundary for Paper A:

- **common-path noise only:** detector response can cancel from the ideal full-record task;
- **non-common-path/output noise present:** detector response changes the information spectrum and can change both evidence accumulation and search geometry;
- **real detectors:** the result depends on the mixture of photon/background noise, internal carrier noise, Johnson noise, readout noise, and bandwidth limits, because those sources need not share one transfer path.

---

## 4. What this establishes

Established:

1. A detector response-time crossover is **not universal** once physical noise coupling is restored.
2. There is an exact cancellation limit in which detector response time disappears from the full-record matched-filter information spectrum.
3. A mixed pre-/post-response noise model gives a simple interpolation between detector-invariant and detector-dependent regimes.
4. The natural systems-level quantity is `mathcal I_tau(f)`, not `tau` alone.

Not yet established:

- whether a realistic detector model lies near the common-path or output-noise-dominated limit;
- whether Paper A's fast-to-slow guarantee-time crossover survives for a particular HgCdTe, InSb, APD, photoconductor, or photodiode noise budget;
- the finite-window exact-scan ordering in the mixed-noise model.

The next useful step is to introduce a physically linked responsivity--response-time law and determine how the known-arrival evidence ordering changes before adding the unknown-arrival search.