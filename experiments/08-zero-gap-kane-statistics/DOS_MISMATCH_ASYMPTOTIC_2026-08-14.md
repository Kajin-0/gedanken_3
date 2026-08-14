# Zero-Gap DOS-Mismatch Asymptotic

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** GENERAL ASYMPTOTIC THEOREM / HGCDTE IS ONE SPECIAL CASE / NOVELTY NOT ESTABLISHED

## 1. General zero-gap problem

Consider a clean zero-gap system with a conduction-side density of states

```math
g_e(E)=A E^a,
\qquad E>0,
```

and a valence-hole density of states

```math
g_h(E)=B E^b,
\qquad E>0,
```

with

```math
a,b>-1.
```

There is no extrinsic charge. The chemical potential `mu(T)` is set by intrinsic neutrality

```math
n(\mu,T)=p(\mu,T).
```

Define

```math
\eta=\frac{\mu}{kT}.
```

The exact carrier densities are

```math
n=A(kT)^{a+1}I_a(\eta),
```

```math
p=B(kT)^{b+1}I_b(-\eta),
```

where

```math
I_s(\eta)=\int_0^\infty\frac{x^s}{1+e^{x-\eta}}dx.
```

## 2. Matched exponents: `a=b`

If `a=b`, all explicit temperature powers cancel from neutrality:

```math
A I_a(\eta)=B I_a(-\eta).
```

Therefore

```math
\boxed{\eta\to\eta_0=\text{constant}}
```

as `T->0`, with `eta_0` set by `A/B`.

Consequently

```math
\boxed{n=p\propto T^{a+1}.}
```

The particle-hole symmetric case `A=B` has `eta_0=0`.

A symmetric 3-D massless Dirac cone has `a=b=2`, hence `n~T^3`.

## 3. Mismatched exponents: `a>b`

If `a>b`, the conduction-side thermal phase space `T^(a+1)` vanishes faster than the hole-side phase space `T^(b+1)` at fixed `eta`.

Neutrality therefore requires

```math
\eta\to+\infty.
```

The electrons become degenerate relative to `kT`, while holes are Boltzmann suppressed.

Use

```math
I_a(\eta)\simeq\frac{\eta^{a+1}}{a+1}
```

at leading order and

```math
I_b(-\eta)\simeq\Gamma(b+1)e^{-\eta}.
```

Neutrality gives

```math
\boxed{
\eta^{a+1}e^\eta
\simeq
\frac{(a+1)B\Gamma(b+1)}{A}
(kT)^{b-a}.
}
```

Define

```math
Q(T)=\frac{(a+1)B\Gamma(b+1)}{A}
(kT)^{b-a}.
```

Then the leading closed solution is

```math
\boxed{
\eta(T)
\simeq
(a+1)
W\left[
\frac{Q(T)^{1/(a+1)}}{a+1}
\right].
}
```

The common carrier density is

```math
\boxed{
n=p
\simeq
A(a+1)^a(kT)^{a+1}
W^{a+1}\left[
\frac{Q(T)^{1/(a+1)}}{a+1}
\right].
}
```

Since `Q~T^{-(a-b)}`,

```math
\boxed{
\eta(T)\sim(a-b)\ln(T_0/T)
}
```

up to `ln ln` corrections, and

```math
\boxed{
n=p\sim
T^{a+1}[\ln(T_0/T)]^{a+1}.}
```

## 4. Mirror case: `b>a`

If the valence DOS exponent is larger,

```math
\eta\to-\infty.
```

The hole side becomes degenerate and the electron side Boltzmann suppressed.

The mirror result is

```math
\boxed{
n=p\sim
T^{b+1}[\ln(T_0/T)]^{b+1}.}
```

Thus the larger DOS exponent controls the algebraic power, while exponent mismatch creates the logarithmic enhancement.

## 5. Compact general rule

Let

```math
s_{max}=\max(a,b).
```

Then for unequal exponents,

```math
\boxed{
n_i(T)
\sim
T^{s_{max}+1}
[\ln(T_0/T)]^{s_{max}+1}
}
```

at zero gap, under the clean noninteracting power-law-DOS assumptions.

For equal exponents the logarithm is absent:

```math
\boxed{
n_i(T)\sim T^{a+1}.}
```

## 6. HgCdTe specialization

At the massless-Kane point:

```text
conduction cone: g_e(E) ~ E^2      -> a=2
heavy-hole reservoir: g_h(E) ~ E^(1/2) -> b=1/2
```

with the light-hole cone supplying only a subleading hole population once `eta>>1`.

Therefore

```math
\boxed{
n_i(T)\sim T^3[\ln(T_0/T)]^3.}
```

The coefficient and exact Lambert-W argument reduce to the expression in `FIRST_PRINCIPLES_ZERO_GAP_2026-08-14.md`.

## 7. Chemical-potential scaling

An important subtlety is

```math
\eta=\mu/(kT)\to\infty
```

while

```math
\mu=kT\eta\to0.
```

Thus the intrinsic chemical potential approaches the zero-gap node in absolute energy as `T->0`, but it approaches from the conduction side by an ever-increasing number of thermal energies.

This is why the electron gas is asymptotically degenerate in the dimensionless sense without retaining a finite zero-temperature carrier density.

## 8. Flat-band singularity

An exactly flat valence band is not described by a finite power-law DOS `E^b` in an unbounded continuum. It contains a macroscopically large state count concentrated at one energy and requires a lattice/momentum cutoff.

Therefore the ideal spectroscopic Kane model with a perfectly flat heavy-hole band is insufficient to determine thermodynamic intrinsic carrier concentration by itself.

Any finite heavy-hole curvature converts the flat band into the `b=1/2` reservoir above and restores a well-defined continuum thermodynamic limit.

Hence a term that is negligible for low-energy optical dispersion can be leading-order for charge neutrality.

## 9. Detector-language interpretation

The standard activated semiconductor picture assumes a finite gap and nondegenerate carriers. At a genuine zero-gap point the activation exponential disappears.

The remaining thermal carrier floor is set by:

1. nodal DOS exponents;
2. DOS prefactor asymmetry;
3. the charge-neutrality shift of the chemical potential.

For a detector model this means that simply extending a positive-gap formula to arbitrarily long cutoff wavelength can give the wrong asymptotic carrier statistics even if the fitted formula was highly accurate over ordinary LWIR compositions.

## 10. Prior-art status

The ingredients are established:

- chemical potential follows charge neutrality;
- power-law DOS controls thermodynamic scaling in nodal semimetals;
- Schmit and later HgCdTe work solve Kane carrier concentration numerically;
- massless Kane bands and the flat heavy-hole band are established.

A targeted search did not identify this exact general Lambert-W DOS-mismatch asymptotic or its HgCdTe `T^3 log^3 T` specialization.

That does not establish novelty. The theorem is mathematically elementary once the asymptotic regimes are chosen, and may exist in other semimetal contexts under different terminology.

## 11. Adversarial risk

A skeptical reviewer can argue:

> This is a useful asymptotic analysis of charge neutrality between two standard power-law densities of states. The logarithm follows directly from balancing a degenerate power-law population against a Boltzmann tail. The HgCdTe specialization applies this generic result to an already-known Kane band structure.

That criticism is substantial.

## 12. Next gate

The only way Experiment 08 should remain a frontier is if the zero-gap asymptotic produces a detector consequence not already contained in classic HgCdTe `n_i` calculations.

Next test:

- compare the exact Kane zero-gap limit against the widely used Hansen-Schmit fitted `n_i` law;
- prove whether any fit proportional to `E_g^(3/4)` can be uniformly valid as `E_g->0`;
- determine the practical gap/cutoff domain where the asymptotic mismatch becomes order unity;
- then adversarially assess whether that is merely a domain-of-validity correction or a publishable theoretical result.
