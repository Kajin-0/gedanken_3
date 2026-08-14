# Experiment 08 — Zero-Gap Kane Carrier Statistics

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** PROVISIONAL / EXACT ZERO-GAP ASYMPTOTIC DERIVED / CLASSIC KANE CARRIER-CONCENTRATION PRIOR ART IS STRONG / NOVELTY NOT ESTABLISHED

## 1. Gedanken premise

In narrow-gap HgCdTe the Kane edge electron mass scales approximately with the gap,

```math
m_e^*\sim\frac{E_g}{2v^2}.
```

If this edge mass is substituted into the ordinary nondegenerate parabolic intrinsic-carrier formula,

```math
n_i\propto(m_e m_h)^{3/4}T^{3/2}e^{-E_g/(2kT)},
```

then

```math
n_i\propto E_g^{3/4}
```

as `E_g -> 0+`, apparently predicting `n_i -> 0`.

But gapless HgCdTe at the topological transition has massless Kane cones crossed by a heavy-hole band. It should not become thermally empty merely because the *edge curvature mass* vanishes.

Question:

> What is the correct intrinsic carrier concentration as `E_g -> 0`, and exactly where does the conventional parabolic/nondegenerate detector formula lose self-consistency?

## 2. Strong prior-art boundary

Do not claim the general Kane carrier-concentration problem as new.

- Schmit (J. Appl. Phys. 41, 2876, 1970; DOI 10.1063/1.1659330) already calculated intrinsic carrier concentration by imposing electron-hole neutrality with nonparabolic Kane electrons and a heavy-hole valence band.
- Nemirovsky and Finkman (J. Appl. Phys. 50, 8107, 1979; DOI 10.1063/1.325950) measured and modeled intrinsic concentration.
- Hansen and Schmit (1983) produced the widely used fitted expression proportional to `E_g^(3/4) T^(3/2) exp[-E_g/(2kT)]`, stated for `E_g>0`.
- Later Kane-based formulas explicitly include nonparabolicity and degeneracy.
- Modern HgCdTe work experimentally establishes the massless-Kane gap closure and nearly universal velocity near the topological transition.

The possible contribution here is therefore only an **analytical zero-gap asymptotic / validity theorem**, not a new numerical carrier model.

## 3. Minimal thermodynamic Kane model

Take energy zero at the heavy-hole/light-hole valence maximum and positive gap `E_g`.

Use the positive-gap simplified Kane dispersions

```math
E_c(p)=\frac{E_g}{2}+\sqrt{\left(\frac{E_g}{2}\right)^2+v^2p^2},
```

```math
E_{lh}(p)=\frac{E_g}{2}-\sqrt{\left(\frac{E_g}{2}\right)^2+v^2p^2}.
```

Thus `E_c(0)=E_g` and `E_lh(0)=0`.

Retain the small heavy-hole curvature that is neglected in the ideal spectroscopic massless-Kane model:

```math
E_{hh}(p)=-\frac{p^2}{2m_{hh}}.
```

This curvature is essential for thermodynamic state counting.

The 2016 massless-Kane HgCdTe paper explicitly describes the ideal heavy-hole band as flat and discusses `m_hh~0.5m0` when assessing the neglected quadratic term. The present model deliberately reinstates that term.

## 4. Exact Kane densities of states

For conduction energy `E>=E_g`,

```math
p(E)=\frac{\sqrt{E(E-E_g)}}{v}.
```

With Kramers/spin degeneracy two,

```math
\boxed{
g_c(E)
=\frac{(2E-E_g)\sqrt{E(E-E_g)}}
{2\pi^2\hbar^3v^3}.
}
```

For light-hole energy `-epsilon`, `epsilon>=0`,

```math
\boxed{
g_{lh}(\epsilon)
=\frac{(2\epsilon+E_g)\sqrt{\epsilon(\epsilon+E_g)}}
{2\pi^2\hbar^3v^3}.
}
```

For the parabolic heavy-hole band,

```math
\boxed{
g_{hh}(\epsilon)
=\frac1{2\pi^2}
\left(\frac{2m_{hh}}{\hbar^2}\right)^{3/2}
\sqrt{\epsilon}.
}
```

## 5. Dimensionless exact neutrality equation

Define

```math
\gamma=\frac{E_g}{kT},
\qquad
\eta=\frac{\mu}{kT},
```

and

```math
A_0=\frac{(kT)^3}{2\pi^2\hbar^3v^3},
\qquad
\Lambda=\left(\frac{2m_{hh}v^2}{kT}\right)^{3/2}.
```

Then

```math
n=A_0J_c(\gamma,\eta),
```

where

```math
J_c=
\int_\gamma^\infty
\frac{(2z-\gamma)\sqrt{z(z-\gamma)}}
{1+e^{z-\eta}}dz.
```

The light-hole density is

```math
p_{lh}=A_0J_{lh}(\gamma,\eta),
```

with

```math
J_{lh}=\int_0^\infty
\frac{(2z+\gamma)\sqrt{z(z+\gamma)}}
{1+e^{z+\eta}}dz.
```

The heavy-hole density is

```math
p_{hh}=A_0\Lambda I_{1/2}(-\eta),
```

where

```math
I_j(\eta)=\int_0^\infty\frac{y^j}{1+e^{y-\eta}}dy.
```

Intrinsic charge neutrality is therefore

```math
\boxed{
J_c(\gamma,\eta)
=J_{lh}(\gamma,\eta)
+\Lambda I_{1/2}(-\eta).
}
```

This reduced problem depends only on the two dimensionless control parameters `gamma=E_g/kT` and `Lambda`.

## 6. Exact zero-gap equation

At `E_g=0`, the electron and light-hole bands are conical:

```math
g_c(E)=g_{lh}(E)=\frac{E^2}{\pi^2\hbar^3v^3}.
```

The neutrality equation becomes

```math
\boxed{
2[I_2(\eta)-I_2(-\eta)]
=\Lambda I_{1/2}(-\eta).
}
```

The heavy-hole DOS breaks electron-hole symmetry and forces `eta>0`: the intrinsic chemical potential lies inside the conduction cone.

For representative HgCdTe scales

```text
v = 1.07e6 m/s
m_hh = 0.5 m0
T = 77 K
```

the exact reduced model gives

```text
eta = mu/(kT) ~= 5.308
mu ~= 35.22 meV
n0 ~= 5.70e15 cm^-3
```

with the hole density overwhelmingly heavy-hole-like in this model.

Thus at fixed nonzero temperature,

```math
\boxed{
\lim_{E_g\to0+}n_i(E_g,T)=n_0(T)>0.
}
```

## 7. Noncommuting parabolic/zero-gap limit

The ordinary edge-parabolic approximation gives

```math
m_e^*=\frac{E_g}{2v^2}.
```

Substitution into the nondegenerate formula gives

```math
n_i^{par}\propto E_g^{3/4}e^{-E_g/(2kT)},
```

and hence

```math
\lim_{E_g\to0+}n_i^{par}=0.
```

Therefore

```math
\boxed{
\lim_{E_g\to0+}n_i^{par}(E_g,T)
\ne
\lim_{E_g\to0+}n_i^{Kane}(E_g,T)
}
```

for every fixed `T>0`.

The mathematical reason is simple: the edge-parabolic expansion assumes occupied kinetic energies much smaller than `E_g`. Taking `E_g->0` at fixed `T` violates the expansion that generated `m_e^*` before the limit is reached.

## 8. Hard self-consistency boundary of the nondegenerate parabolic formula

For parabolic electron and heavy-hole bands, the intrinsic Fermi level is

```math
\mu_i^{par}
=\frac{E_g}{2}
+\frac{3kT}{4}\ln\left(\frac{m_{hh}}{m_e}\right).
```

The nondegenerate conduction-band treatment becomes internally impossible once this predicted `mu_i` reaches the conduction edge `E_g`.

Using

```math
m_e=\frac{E_g}{2v^2},
```

and defining `y=E_g/(kT)`, the boundary obeys

```math
y=\frac32\ln\left(\frac{2m_{hh}v^2}{ykT}\right).
```

Hence

```math
\boxed{
y_*
=\frac32
W\left(\frac{4m_{hh}v^2}{3kT}\right).
}
```

For `T=77 K`, `v=1.07e6 m/s`, `m_hh=0.5m0`,

```text
y_* ~= 7.342
E_g,* ~= 48.72 meV.
```

Thus below about `49 meV` in this reduced model, the simplest nondegenerate parabolic intrinsic-Fermi construction predicts its own Fermi level inside the conduction band and is formally self-inconsistent.

This is not a statement that all Kane-based empirical `n_i` formulas fail at 49 meV. It is specifically the self-consistency boundary of the **edge-parabolic/nondegenerate derivation**.

## 9. Zero-gap low-temperature asymptotic

At zero gap and low temperature, `Lambda>>1`, so `eta>>1`.

Use

```math
I_2(\eta)\simeq\frac{\eta^3}{3}+\frac{\pi^2\eta}{3},
```

```math
I_2(-\eta)\ll I_2(\eta),
```

and

```math
I_{1/2}(-\eta)\simeq\Gamma(3/2)e^{-\eta}
=\frac{\sqrt\pi}{2}e^{-\eta}.
```

Keeping the leading cubic term gives

```math
\boxed{
\eta^3e^\eta
\simeq
3\sqrt{\frac\pi2}
\left(\frac{m_{hh}v^2}{kT}\right)^{3/2}.
}
```

Define

```math
C(T)=3\sqrt{\frac\pi2}
\left(\frac{m_{hh}v^2}{kT}\right)^{3/2}.
```

Then

```math
\boxed{
\eta(T)\simeq
3W\left(\frac{C(T)^{1/3}}{3}\right).
}
```

The leading electron density is

```math
n_0(T)
\simeq
\frac{(kT)^3}{3\pi^2\hbar^3v^3}\eta^3.
```

Therefore

```math
\boxed{
n_0(T)
\simeq
\frac{9(kT)^3}{\pi^2\hbar^3v^3}
W^3\left(\frac{C(T)^{1/3}}{3}\right).
}
```

Since the Lambert-W argument scales as `T^(-1/2)`,

```math
\boxed{
n_0(T)\sim T^3[\ln(T_0/T)]^3}
```

up to the standard `ln ln` corrections as `T->0`.

The zero-gap carrier density therefore vanishes algebraically/logarithmically as `T->0`, not by activated `exp[-E_g/(2kT)]` behavior.

## 10. Why the logarithm appears

A pure symmetric 3-D Dirac cone at charge neutrality has `mu=0` and thermally excited carrier density proportional to `T^3`.

HgCdTe is not symmetric because of the heavy-hole reservoir. Its DOS is much larger than the conical light-hole DOS. Charge neutrality therefore pushes `mu/kT=eta` positive.

At low temperature the heavy-hole holes are Boltzmann-suppressed by `e^{-eta}`, while the degenerate cone electron density scales as `eta^3`. Balancing them produces

```math
eta^3e^eta\propto T^{-3/2},
```

and hence the Lambert-W/logarithmic enhancement.

## 11. Small heavy-hole curvature is thermodynamically singular

The spectroscopic simplified Kane model treats the heavy-hole band as perfectly flat. In an unbounded continuum model this gives an ill-defined/infinite state count.

For thermodynamics one must therefore retain either

1. finite heavy-hole curvature, or
2. a finite Brillouin-zone/remote-band cutoff.

With finite parabolic curvature, `m_hh` enters

```math
\Lambda\propto m_{hh}^{3/2}.
```

At 77 K in the reduced model,

```text
m_hh=0.3m0 -> n0 ~4.44e15 cm^-3
m_hh=0.5m0 -> n0 ~5.70e15 cm^-3
m_hh=0.8m0 -> n0 ~7.11e15 cm^-3.
```

Thus the quadratic heavy-hole term can be negligible for the optical Landau-level dispersion yet leading-order for thermodynamic charge neutrality. The order in which the flat-band and thermodynamic limits are taken matters.

## 12. Numerical crossover at 77 K

For the representative reduced model:

```text
Eg(meV)    exact Kane n_i (cm^-3)    naive parabolic n_i    exact/parabolic
100        3.02e13                    2.69e13                1.12
50         7.87e14                    6.92e14                1.14
30         2.17e15                    2.13e15                1.02
20         3.19e15                    3.34e15                0.96
10         4.39e15                    4.21e15                1.04
5          5.03e15                    3.65e15                1.38
2          5.43e15                    2.30e15                2.36
1          5.57e15                    1.48e15                3.77
0          5.70e15                    0                       divergent ratio
```

The parabolic formula can accidentally remain numerically close over part of the crossover even after its assumptions are degrading; its eventual zero-gap trend is nevertheless qualitatively wrong.

## 13. Conditional detector consequence

Any equilibrium dark mechanism whose leading carrier-statistics factor contains `n_i` or `n_i^2` cannot be extrapolated to zero gap using the standard activated parabolic expression.

Within the reduced zero-gap statistics alone:

```text
factor proportional to n_i    -> ~ T^3 W^3
factor proportional to n_i^2  -> ~ T^6 W^6
```

before the independent temperature dependence of capture coefficients, mobility, Auger coefficients, tunneling, defects, etc. is included.

Do not promote these factors to complete dark-current laws without modeling those independent kinetics.

The radiative equilibrium floor must also respect optical detailed balance and should be treated separately.

## 14. Adversarial novelty status

Strong prior art exists:

- exact/numerical Kane-model intrinsic carrier concentration has been studied since at least 1970;
- later formulas explicitly correct for nonparabolicity and degeneracy;
- heavy-hole DOS in HgCdTe has itself been studied in detail;
- massless Kane fermions and the gap-closing transition are established modern HgCdTe physics.

The targeted search has not yet located the particular zero-gap Lambert-W asymptotic or the explicit noncommuting-limit/self-consistency theorem above.

That absence is not proof of novelty. A skeptical reviewer may still reasonably describe the result as an analytical asymptotic of equations already solved numerically decades ago.

## 15. Current disposition

```text
zero-gap paradox: RESOLVED
exact reduced Kane neutrality: RETAIN
noncommuting parabolic limit: RETAIN
parabolic self-consistency boundary: RETAIN
Lambert-W zero-gap asymptotic: RETAIN PROVISIONALLY
thermodynamic importance of finite heavy-hole curvature: RETAIN PROVISIONALLY
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

## 16. Next theoretical gate

Generalize the zero-gap asymptotic to arbitrary nodal electron DOS `g_e(E)~E^a` competing with a valence reservoir `g_h(E)~E^b`.

Determine whether the HgCdTe `T^3 log^3 T` law is merely one instance of a generic DOS-mismatch theorem. If so, perform an immediate prior-art audit; if the general theorem is standard, close Experiment 08 as a novelty path while retaining the HgCdTe validity correction.

Companion calculation: `numerics/zero_gap_kane_statistics.py`.
