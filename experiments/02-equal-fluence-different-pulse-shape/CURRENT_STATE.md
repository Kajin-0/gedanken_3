# Current State — Experiment 02: Equal Fluence, Different Pulse Shape

**Date:** 2026-08-13
**Status:** ACTIVE / FIRST NONTRIVIAL CONSEQUENCE ESTABLISHED / EARLY PRIOR-ART AUDIT IN PROGRESS

## Starting question

Two optical pulses deposit exactly the same number of absorbed photons into the same HgCdTe photoconductor.

- Pulse A is short and intense.
- Pulse B is weak and spread out.

Must the detector produce the same total electrical response?

This is intentionally a device-physics question. Do not turn it into a signal-processing/acquisition problem.

## Step 1 — linear benchmark

Let `n(t)` denote a spatially uniform excess carrier density and `G(t)` the absorbed pair-generation rate density. Start with

```math
\frac{dn}{dt}=G(t)-\frac{n}{\tau},
```

with `n(-infinity)=n(+infinity)=0`.

Integrating the rate equation over the complete transient gives

```math
0=\int G(t)dt-\frac{1}{\tau}\int n(t)dt,
```

hence

```math
\boxed{
\int n(t)dt
=\tau\int G(t)dt.
}
```

Under fixed bias and approximately constant mobility, excess photoconductive current is proportional to `n(t)`, so the integrated electrical response is proportional to `integral n dt`.

Therefore, in the linear single-lifetime model:

```text
same absorbed fluence => same integrated detector response
```

independent of temporal pulse shape.

This is the baseline reciprocity statement.

## Step 2 — minimal nonlinear recombination

Add a cubic high-injection recombination term as the simplest Auger-like model:

```math
\frac{dn}{dt}
=G(t)-\frac{n}{\tau}-Cn^3,
\qquad C>0.
```

Integrating over the complete transient gives the exact identity

```math
\boxed{
\int n(t)dt
=\tau\left[
\int G(t)dt
-C\int n^3(t)dt
\right].
}
```

Thus equal absorbed fluence no longer guarantees equal integrated response. The response also depends on the carrier-density history through `integral n^3 dt`.

A pulse that drives a larger transient carrier density can lose more carriers to Auger recombination before they contribute to the time-integrated conductivity.

This is the first nontrivial consequence.

## Exact impulsive limit

For an ideal instantaneous injection producing

```math
n(0^+)=n_0
```

followed by

```math
\frac{dn}{dt}=-\frac{n}{\tau}-Cn^3,
```

the integrated carrier response is exactly

```math
\boxed{
A(n_0)
\equiv\int_0^\infty n(t)dt
=\sqrt{\frac{\tau}{C}}
\arctan\!\left(n_0\sqrt{C\tau}\right).
}
```

Define

```math
z=n_0\sqrt{C\tau}.
```

Relative to the linear prediction `tau n0`,

```math
\boxed{
\frac{A}{\tau n_0}
=\frac{\arctan z}{z}.
}
```

Representative values:

```text
z = 0.1  -> 0.9967 of linear response
z = 1    -> 0.7854
z = 3    -> 0.4163
z = 10   -> 0.1471
```

At weak injection,

```math
A=\tau n_0-\frac{C\tau^2n_0^3}{3}+O(n_0^5).
```

In the formal strong-injection limit of this minimal model,

```math
\boxed{
A\to\frac{\pi}{2}\sqrt{\frac{\tau}{C}}.
}
```

So the integrated carrier response saturates even though the initially injected carrier density continues to increase. Real devices will acquire additional physics before an arbitrarily large-injection limit is reached; this is a mathematical property of the minimal SRH-like-linear + cubic-Auger model, not a claim of unlimited physical validity.

## Physical meaning

The same total absorbed photon number can produce different total electrical charge if recombination is nonlinear in carrier density.

The simplest predicted ordering is:

```text
short/high-density pulse -> more nonlinear recombination -> smaller integrated response
long/low-density pulse   -> closer to linear reciprocity -> larger integrated response
```

for otherwise identical absorbed fluence.

## Early prior-art result

The underlying high-injection physics is definitely not new.

Established HgCdTe work includes:

- Bartoli et al., J. Appl. Phys. 45, 2150–2154 (1974), DOI 10.1063/1.1663561: high-flux n-HgCdTe photoconductivity saturation attributed to Auger recombination; photoconductivity scales approximately as flux^(1/3) and response time as flux^(-2/3) in the high-flux regime.
- 0.1 eV HgCdTe photoconductor work in Infrared Physics 17, 127–135 (1977): performance and GR noise described by Auger theory.
- High-excess-carrier transient HgCdTe lifetime measurements report departures from exponential decay and injection-dependent lifetime.
- Absolute-linearity measurements of HgCdTe PCs show response nonlinearity depends on irradiance, not merely total radiant power.

A targeted search has not yet located the exact fixed-fluence integrated-response identity above as the central result, but novelty is **not established**. The result may be a simple reformulation of known nonlinear recombination / saturation physics.

## Claim boundary

Do not claim:

- that Auger saturation in HgCdTe is new;
- that equal-fluence pulse-shape dependence is yet novel;
- that the cubic model is a complete HgCdTe Auger-1 model;
- that spatial diffusion, sweepout, heating, mobility changes, trapping, radiative recombination, or contacts are negligible in a real device.

## Next question

The next step is narrow:

> For two finite pulses with the same absorbed fluence, can we prove a useful ordering of the integrated response as one pulse is temporally spread relative to the other, and does that ordering survive a more realistic HgCdTe recombination law?

Do not proceed to manuscript construction. Prior art remains an early gate.