# One-Phonon Mass Sensitivity and Laplace Closure

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** CORRECTED SINGLE-PHONON MODEL / GENERAL SPECTRAL IDENTITIES DERIVED / NOVELTY NOT ESTABLISHED

## 1. Why the previous sign-crossing formula was incomplete

The earlier reduced model retained only thermal carrier phase space,

```math
C\propto \sqrt{\Delta}\,e^{-\Delta/(kT)},
```

and therefore missed two isotope-dependent factors inherent to a quantized phonon transition:

1. the electron-phonon matrix element;
2. the phonon Bose occupation factor.

These terms materially shift the isotope-sensitivity zero at temperatures where `kT` is not negligible compared with the optical-phonon energy.

## 2. Diatomic optical-coordinate scaling

For a relative optical coordinate with reduced mass `mu` and isotope-independent harmonic force constant `K`,

```math
\omega=\sqrt{K/\mu}.
```

Define the elemental isotope participation

```math
\alpha\equiv-\frac{\partial\ln\omega}{\partial\ln M}>0.
```

For a linear electronic coupling to the relative displacement, the one-phonon matrix element contains the zero-point displacement,

```math
|g|^2\propto\frac{1}{\mu\omega}.
```

Since `omega ~ mu^(-1/2)`,

```math
\boxed{|g|^2\propto\omega}
```

for this reduced model, and hence

```math
\boxed{
\frac{\partial\ln |g|^2}{\partial\ln M}=-\alpha.
}
```

For an HgTe-like relative mode,

```math
\alpha_{Hg}=\frac12\frac{M_{Te}}{M_{Hg}+M_{Te}},
```

which is about `0.1944` at natural atomic weights.

## 3. Sharp one-optical-phonon capture model

Take

```math
C(M,T)
\propto |g|^2 [N_\omega(T)+1]
\sqrt{\Delta}\,e^{-\Delta/(kT)},
```

with

```math
N_\omega=\frac{1}{e^{\hbar\omega/(kT)}-1},
\qquad
\Delta=\hbar\omega-E,
```

where `E` is the electronic energy release required by the defect transition and `Delta>0` is the carrier kinetic energy selected by one-phonon emission.

Let

```math
x=\frac{\hbar\omega}{kT},
\qquad
\epsilon\equiv\frac{dE}{d\ln M}.
```

Then

```math
\frac{d\Delta}{d\ln M}=-\alpha\hbar\omega-\epsilon.
```

The complete logarithmic mass sensitivity in this reduced model is

```math
\boxed{
S_C
\equiv\frac{d\ln C}{d\ln M}
=-\alpha
+\alpha xN_\omega
+(-\alpha\hbar\omega-\epsilon)
\left(\frac{1}{2\Delta}-\frac{1}{kT}\right).
}
```

This separates:

```text
matrix-element term        -alpha
Bose-factor term           +alpha x N
energy-selection term      (d Delta/d ln M)[1/(2Delta)-1/(kT)]
```

Any isotope-induced electronic-level shift enters explicitly through `epsilon`.

## 4. Pure phonon-mass limit

If the electronic separation is held fixed (`epsilon=0`),

```math
\boxed{
S_C
=\alpha\left[
-1+x(N_\omega+1)-\frac{\hbar\omega}{2\Delta}
\right].
}
```

The sign change therefore occurs at

```math
\boxed{
\Delta_\times
=\frac{\hbar\omega}
{2[x(N_\omega+1)-1]}.
}
```

This replaces the earlier incomplete estimate `Delta_x=kT/2`.

For `hbar omega=17.73 meV` at `77 K`,

```text
kT ~= 6.635 meV
x ~= 2.672
N ~= 0.0742
Delta_x ~= 4.74 meV
```

rather than `kT/2 ~= 3.32 meV`.

Physical interpretation:

- near threshold, heavier isotope lowers `omega`, closes phase space, and strongly decreases capture;
- far enough above threshold, the lower selected carrier kinetic energy can increase the thermally occupied carrier population and overcome the weaker quantized coupling;
- the isotope effect can therefore reverse sign without changing the underlying defect species.

## 5. Natural Hg -> 204Hg reduced-order scale

For an HgTe-like `143 cm^-1` mode and Te held natural, reduced-mass scaling gives approximately

```text
omega(204Hg)/omega(natural Hg) = 0.996745
hbar omega: 17.7297 -> 17.6720 meV
phonon-energy shift ~= -0.0577 meV
```

In the **sharp**, fixed-electronic-level model at 77 K, representative heavy/natural capture ratios are approximately

```text
Delta_nat = 0.10 meV -> 0.65
Delta_nat = 0.20 meV -> 0.85
Delta_nat = 0.50 meV -> 0.95
Delta_nat = 1.00 meV -> 0.98
Delta_nat = 2.00 meV -> 0.99
Delta_nat = 5.00 meV -> ~1.000
```

The very large effect is confined to an extremely near-threshold transition.

## 6. Finite broadening

Represent defect/phonon energy dispersion by a Gaussian convolution of standard deviation `sigma`:

```math
F_\sigma(\Delta,T)
=\int_0^\infty dE\;\sqrt{E}\,e^{-E/(kT)}
\frac{e^{-(E-\Delta)^2/(2\sigma^2)}}{\sqrt{2\pi}\sigma}.
```

Then

```math
C\propto \omega(N_\omega+1)F_\sigma.
```

For the same natural-Hg -> 204Hg shift at 77 K, the reduced-order model gives at `Delta_nat=0`:

```text
sigma = 0.10 meV -> C_heavy/C_nat ~ 0.49
sigma = 0.20 meV -> ~0.72
sigma = 0.47 meV -> ~0.88
sigma = 1.00 meV -> ~0.94
```

At `sigma=0.47 meV`, representative ratios are approximately

```text
Delta_nat = 0.0 meV -> 0.876
Delta_nat = 0.1 meV -> 0.890
Delta_nat = 0.2 meV -> 0.903
Delta_nat = 0.5 meV -> 0.936
Delta_nat = 1.0 meV -> 0.970
Delta_nat = 2.0 meV -> 0.991
```

These are parameterized theory results, not predictions for real HgCdTe. The capture spectral width is not established by this model.

## 7. General positive spectral-kernel representation

The previous equations are only one special model. A much more general result follows if the capture coefficient can be written as

```math
C(\beta)
=A[N_\omega(\beta)+1]Z(\beta),
\qquad
\beta\equiv\frac1{kT},
```

where

```math
Z(\beta)=\int_0^\infty \Phi(E)e^{-\beta E}\,dE,
```

and `Phi(E)>=0` is a temperature-independent capture spectral kernel containing the carrier density of states, spectral broadening, and energy-dependent transition strength.

Define the normalized capture-energy distribution

```math
P_\beta(E)=\frac{\Phi(E)e^{-\beta E}}{Z(\beta)}.
```

Then

```math
\boxed{
\frac{d}{d\beta}
\ln\frac{C}{N_\omega+1}
=-\langle E\rangle_\beta.
}
```

and

```math
\boxed{
\frac{d^2}{d\beta^2}
\ln\frac{C}{N_\omega+1}
=\operatorname{Var}_\beta(E)\ge0.
}
```

Thus the Bose-corrected log capture coefficient is **convex in inverse temperature** for any fixed positive spectral kernel.

More generally,

```math
\boxed{
\frac{d^m\ln Z}{d\beta^m}
=(-1)^m\kappa_m(E),
}
```

where `kappa_m` is the `m`th cumulant of the capture-weighted carrier energy.

This gives an exact hierarchy:

```text
first derivative  -> mean capture energy
second derivative -> capture-energy variance
third derivative  -> minus third cumulant
...
```

## 8. Consequence for isotope contrast

For two isotope states `A` and `B`, define the Bose-corrected log contrast

```math
\mathcal R(\beta)
=\ln\frac{C_B}{C_A}
-\ln\frac{N_B+1}{N_A+1}.
```

If the temperature-independent prefactor ratio `A_B/A_A` is constant, then

```math
\boxed{
\mathcal R'(\beta)
=-(\langle E\rangle_B-\langle E\rangle_A)
}
```

and

```math
\boxed{
\mathcal R''(\beta)
=\operatorname{Var}_B(E)-\operatorname{Var}_A(E).
}
```

For a perfectly sharp one-energy channel,

```math
\Phi_s(E)\propto\delta(E-\Delta_s),
```

so

```math
\mathcal R'(\beta)=-(\Delta_B-\Delta_A),
\qquad
\mathcal R''(\beta)=0.
```

Therefore exact linearity of the Bose-corrected isotope contrast in inverse temperature is a strong property of the sharp single-energy model. Curvature means that the isotope perturbation changes a broadened/multichannel capture spectrum or that the assumed temperature-independent kernel is incomplete.

## 9. What this does and does not establish

Established analytically:

1. the previous isotope sign-crossing formula was incomplete because it omitted matrix-element and Bose factors;
2. the corrected sign crossing can shift substantially at 77 K;
3. finite broadening regularizes the near-threshold isotope response;
4. the temperature dependence of a positive capture kernel has an exact Laplace/cumulant structure;
5. a total SRH isotope response must still be filtered through the cycle-control weights derived in `THEORETICAL_ISOTOPE_CONTROL_SUM_RULE_2026-08-14.md`.

Not established:

- the actual Hg-vacancy capture spectral width;
- the actual isotope shift of the electronic vacancy-band separation;
- that one HgTe-like mode alone controls the electron capture;
- novelty of the mathematical Laplace/cumulant identities.

## 10. Prior-art boundary

General multiphonon and first-principles carrier-capture theories are mature and explicitly retain electron-phonon matrix elements and phonon-mode structure. Recent work also treats changes in phonon frequencies across capture states. A 2026 PRL demonstrates a large isotope-dependent nonradiative lifetime in a semiconductor defect through a shifted local vibrational mode.

Therefore do not claim the generic concept of isotope-sensitive nonradiative capture as new.

The remaining HgCdTe-specific theoretical opportunity is narrower: combine the published narrow-gap `V_Hg` electronic spectrum/capture theory with the exact isotope-control and spectral identities above to determine whether a robust, composition-dependent isotope signature follows without free fitting parameters.

Companion calculation: `numerics/one_phonon_isotope_theory.py`.
