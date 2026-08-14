# Experiment 08 — Zero-Gap Kane Statistics Novelty Stop

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** CLOSE AS DEFAULT NOVELTY PATH / RETAIN ZERO-GAP ASYMPTOTICS AND VALIDITY CORRECTIONS

## 1. What was established

The reduced thermodynamic Kane model gives an exact intrinsic-neutrality equation through the positive-gap to zero-gap crossover.

At `E_g=0`, with massless electron/light-hole cones and finite parabolic heavy-hole curvature,

```math
2[I_2(\eta)-I_2(-\eta)]
=\Lambda I_{1/2}(-\eta),
```

where

```math
\eta=\mu/(kT),
\qquad
\Lambda=(2m_{hh}v^2/kT)^{3/2}.
```

For representative HgCdTe scales `v=1.07e6 m/s`, `m_hh=0.5m0`, `T=77 K`, the reduced model gives

```text
eta ~= 5.308
mu ~= 35.22 meV
n_i(Eg=0) ~= 5.70e15 cm^-3.
```

Thus at fixed `T>0`, the exact reduced Kane limit is finite while the naive edge-parabolic formula tends to zero as `E_g^(3/4)`.

## 2. Noncommuting-limit result

The edge mass

```math
m_e^*=E_g/(2v^2)
```

is derived by expanding the Kane dispersion for kinetic energies much smaller than `E_g`.

Therefore taking `E_g->0` at fixed `T` after substituting this mass into a Maxwell-Boltzmann parabolic formula is mathematically inconsistent.

In the reduced model,

```math
\boxed{
\lim_{E_g\to0+}n_i^{parabolic}=0
\ne
\lim_{E_g\to0+}n_i^{Kane}=n_0(T)>0.
}
```

## 3. Hard boundary of the simplest parabolic/nondegenerate construction

The parabolic intrinsic Fermi level reaches the conduction edge when

```math
\boxed{
\frac{E_g^*}{kT}
=\frac32 W\left(\frac{4m_{hh}v^2}{3kT}\right).
}
```

For `T=77 K`, `m_hh=0.5m0`, `v=1.07e6 m/s`,

```text
E_g^* ~=48.7 meV.
```

Below this, the simple nondegenerate parabolic intrinsic-Fermi construction predicts its own chemical potential inside the conduction band and is formally self-inconsistent.

This boundary does **not** apply to full Kane calculations or empirical fits that already encode nonparabolicity/degeneracy.

## 4. Zero-gap asymptotic

For `T->0`, `eta>>1` and

```math
\eta^3e^\eta
\simeq
3\sqrt{\pi/2}
(m_{hh}v^2/kT)^{3/2}.
```

Hence

```math
\boxed{
\eta\simeq
3W\left[
\frac13
\left(3\sqrt{\pi/2}
(m_{hh}v^2/kT)^{3/2}\right)^{1/3}
\right].
}
```

and

```math
\boxed{
n_0(T)\sim T^3[\ln(T_0/T)]^3}
```

up to Lambert-W / `ln ln` corrections.

The logarithm arises because a large heavy-hole reservoir pushes the reduced intrinsic chemical potential into the conduction cone while the absolute chemical potential still tends to zero.

## 5. Generic DOS-mismatch theorem

For zero-gap power-law densities of states

```math
g_e(E)=AE^a,
\qquad
g_h(E)=BE^b,
```

if `a>b`,

```math
\eta\simeq(a+1)
W\left[
\frac1{a+1}
\left(
\frac{(a+1)B\Gamma(b+1)}{A}(kT)^{b-a}
\right)^{1/(a+1)}
\right]
```

and

```math
n_i\sim T^{a+1}[\ln(T_0/T)]^{a+1}.
```

For `b>a`, the mirror result holds; for `a=b`, `eta` tends to a constant and the logarithm disappears.

HgCdTe has `a=2` for the massless Kane cone and `b=1/2` for a parabolic heavy-hole reservoir.

## 6. Thermodynamic role of heavy-hole curvature

The simplified spectroscopic massless-Kane model treats the heavy-hole band as flat. In continuum thermodynamic state counting an exactly flat unbounded band is singular and requires a momentum cutoff.

Retaining finite heavy-hole curvature regularizes the intrinsic-neutrality problem. Thus the quadratic heavy-hole term can be negligible for low-energy magneto-optical dispersion yet leading-order for equilibrium carrier statistics.

This order-of-limits observation is retained as a conceptual result.

## 7. Practical comparison with Hansen-Schmit

The familiar Hansen-Schmit fitted law is proportional to

```math
E_g^{3/4}T^{3/2}e^{-E_g/(2kT)}
```

and is therefore asymptotically incompatible with the finite zero-gap Kane limit.

However, when the reduced exact model is compared along a 77-K Hansen gap/composition trajectory, the difference becomes large only extremely near zero gap:

```text
~10% departure: Eg ~5.25 meV  (lambda ~236 um)
~20% departure: Eg ~4.43 meV  (lambda ~280 um)
~50% departure: Eg ~2.99 meV  (lambda ~415 um)
2x departure:   Eg ~1.89 meV  (lambda ~656 um)
```

The exact numerical values depend on the reduced-model choices `v` and `m_hh`; these are scale comparisons, not universal thresholds.

Thus the asymptotic failure is mathematically real but lies far beyond ordinary MWIR/LWIR detector gaps at 77 K.

## 8. Strong prior art

The central computational problem is old and mature:

- J. L. Schmit, J. Appl. Phys. 41, 2876 (1970), already calculated `n_i` and the reduced Fermi energy by Kane-model electron-hole neutrality.
- Nemirovsky and Finkman, J. Appl. Phys. 50, 8107 (1979), measured and modeled intrinsic concentration.
- Hansen and Schmit (1983) gave the widely used analytical fit based on Kane calculations and measured heavy-hole mass.
- Yadava (1994) developed a Kane-based expression including nonparabolicity and degeneracy corrections.
- Bogoboyashchyy (2001) studied the heavy-hole density of states over broad HgCdTe composition/temperature ranges.
- Krishnamurthy, Berding and Yu, J. Electron. Mater. 35, 1369 (2006), performed full-band calculations of Fermi levels, intrinsic carrier densities, one-photon absorption, and recombination lifetimes; they explicitly found significant effects from nonparabolic and anisotropic valence bands.
- Modern massless-Kane work establishes the zero-gap conical/flat-band structure and universal velocity near the topological transition.

## 9. Adversarial disposition

A skeptical reviewer could reasonably say:

> The zero-gap asymptotic is a useful analytical limit of a Kane charge-neutrality problem whose numerical solution has been standard in HgCdTe for more than fifty years. The Lambert-W form and the explicit validity warning are pedagogically useful, but the practical detector correction becomes substantial only at gaps far smaller than conventional infrared-detector operation.

That criticism is currently correct.

## 10. Stop decision

```text
zero-gap Kane paradox: RESOLVED
Lambert-W asymptotic: RETAIN
DOS-mismatch theorem: RETAIN
parabolic self-consistency boundary: RETAIN
finite-heavy-hole thermodynamic regularization: RETAIN
major detector-theory novelty: NOT ESTABLISHED
Experiment 08 publication frontier: CLOSED BY DEFAULT
paper drafting: DO NOT BEGIN
```

Reopen only if a further consequence appears that changes a genuine detector-performance bound, rather than merely correcting an asymptotic carrier formula at sub-THz-scale gaps.

## 11. Controlling files

1. `00_NOVELTY_STOP_2026-08-14.md`
2. `FIRST_PRINCIPLES_ZERO_GAP_2026-08-14.md`
3. `DOS_MISMATCH_ASYMPTOTIC_2026-08-14.md`
4. `numerics/zero_gap_kane_statistics.py`

Next research step: return to theory-only premise generation and screen against the strongest prior theory immediately.
