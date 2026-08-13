# Split-pulse step

**Date:** 2026-08-13
**Status:** EXACT RESULT IN THE MINIMAL LINEAR + CUBIC-RECOMBINATION MODEL

Use

```math
dn/dt=-n/\tau-Cn^3,
```

and let total absorbed impulsive injection be `N`. Compare one impulse `N` with two impulses `q=N/2` separated by `Delta`.

Define

```math
k=\sqrt{C\tau},\qquad K=\sqrt{\tau/C},\qquad \phi(n)=\arctan(kn).
```

The carrier area accumulated while freely decaying from `n_a` to `n_b` is

```math
A(n_a\to n_b)=K[\phi(n_a)-\phi(n_b)].
```

After the first half-pulse, the residual density before the second is

```math
r(\Delta)=
\frac{q e^{-\Delta/\tau}}
{\sqrt{1+C\tau q^2(1-e^{-2\Delta/\tau})}}.
```

Hence the exact total two-pulse area is

```math
\boxed{
A_2(\Delta)=K[\phi(q)-\phi(r)+\phi(r+q)].
}
```

At `Delta=0`, `r=q` and

```math
A_2(0)=A(N).
```

As `Delta -> infinity`, `r -> 0` and

```math
A_2(\infty)=2A(N/2).
```

Now

```math
\frac{dA_2}{dr}=Kk\left[-\frac{1}{1+k^2r^2}
+\frac{1}{1+k^2(r+q)^2}\right]<0,
```

while `dr/dDelta<0`. Therefore

```math
\boxed{dA_2/d\Delta>0.}
```

**For the same total absorbed fluence, separating two equal subpulses strictly increases the integrated photoconductive response.**

For `m` fully separated equal subpulses,

```math
\boxed{
A_m=m\sqrt{\tau/C}\,
\arctan\left(\frac{N\sqrt{C\tau}}{m}\right).
}
```

`A_m` increases with `m` and approaches

```math
\lim_{m\to\infty}A_m=\tau N,
```

the linear-recombination value.

## Physical meaning

```text
same absorbed photons
+ more temporal concentration
-> higher peak carrier density
-> stronger nonlinear recombination
-> smaller integrated conductivity.
```

This is a device-level memory of pulse shape even when total absorbed photon number is fixed.

## Prior-art caution

High-flux HgCdTe saturation and injection-dependent Auger lifetime are old results. The exact split-pulse ordering has not yet been established as novel.

Some HgCdTe focal-plane-array reciprocity-failure measurements report the opposite sign at fixed fluence (greater response at higher flux), where trapping/persistence-type mechanisms are implicated. The sign of the effect may therefore be mechanistically useful, but this is only a hypothesis at present.

## Next question

Determine whether the split-pulse ordering follows for a general recombination law

```math
R(n)=a n+b n^2+c n^3
```

from convexity alone, rather than from the special cubic/arctangent solution.