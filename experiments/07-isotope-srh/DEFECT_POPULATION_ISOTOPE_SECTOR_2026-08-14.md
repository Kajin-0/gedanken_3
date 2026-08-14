# Defect-Population Isotope Sector: Quenched vs Annealed Mercury Vacancies

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT HARMONIC IDENTITY / ENSEMBLE DEPENDENCE EXPOSED / GENERIC DEFECT THERMODYNAMICS HAS PRIOR ART

## 1. Why capture kinetics are not the whole isotope problem

When electron capture is rate-limiting, a reduced SRH rate has the structure

```math
R_{SRH}\propto N_V C_n,
```

up to occupancy/control factors.

Therefore

```math
\boxed{
S_{SRH}\simeq S_{N_V}+S_{C_n}
}
```

when the vacancy population itself is allowed to respond to isotope mass.

The previous Experiment-07 derivations primarily analyzed `S_Cn`. This file isolates `S_NV`.

## 2. Harmonic vibrational free energy

For one harmonic mode

```math
F_\nu
=\frac12\hbar\omega_\nu
+kT\ln\left(1-e^{-\beta\hbar\omega_\nu}\right)
=kT\ln\left[2\sinh\left(\frac{\beta\hbar\omega_\nu}{2}\right)\right].
```

Differentiate with respect to log frequency:

```math
\boxed{
\frac{\partial F_\nu}{\partial\ln\omega_\nu}
=\frac{\hbar\omega_\nu}{2}
\coth\left(\frac{\beta\hbar\omega_\nu}{2}\right)
\equiv U_\nu.
}
```

`U_nu` is the thermal mean energy of the harmonic oscillator, including zero-point energy.

For elemental isotope mass `M_a`, define modal mass participation

```math
p_{\nu a}
\equiv
-2\frac{\partial\ln\omega_\nu}{\partial\ln M_a}.
```

Then

```math
\boxed{
\frac{\partial F_{vib}}{\partial\ln M_a}
=-\frac12\sum_\nu p_{\nu a}U_\nu.
}
```

## 3. Defect-formation free energy

Let `Delta G_f` be the complete defect-formation free energy for the reaction that creates a mercury vacancy, including the appropriate atomic reservoir chemical potential.

To leading Born-Oppenheimer order, static electronic energies do not depend explicitly on nuclear isotope mass. The harmonic mass derivative is therefore

```math
\boxed{
\frac{\partial\Delta G_f^{vib}}{\partial\ln M_a}
=-\frac12
\Delta\left[\sum_\nu p_{\nu a}U_\nu\right],
}
```

where `Delta[...]` means defective crystal minus pristine crystal plus the reservoir contribution with the correct reaction stoichiometry.

For an equilibrium dilute defect concentration

```math
N_V\propto e^{-\beta\Delta G_f},
```

so

```math
\boxed{
S_{N_V,a}
\equiv\frac{\partial\ln N_V}{\partial\ln M_a}
=\frac{\beta}{2}
\Delta\left[\sum_\nu p_{\nu a}U_\nu\right].
}
```

The sign depends on how vacancy formation redistributes the isotope-participating vibrational spectrum.

## 4. Classical-limit cancellation

For `beta hbar omega << 1`,

```math
U_\nu
=kT+\frac{(\hbar\omega_\nu)^2}{12kT}+O[(\hbar\omega/kT)^4].
```

The leading classical term gives

```math
S_{N_V,a}^{cl}
=\frac12\Delta\sum_\nu p_{\nu a}.
```

For a consistently balanced formation reaction including the elemental reservoir, the classical mass factors cancel. Equivalently, the total modal participation count associated with a conserved atomic species balances across the reaction.

Hence the leading equilibrium isotope effect on defect formation vanishes in the classical limit:

```math
\boxed{S_{N_V,a}\to0\quad\text{classically}.}
```

The first quantum correction is

```math
\boxed{
S_{N_V,a}
\simeq
\frac{1}{24(kT)^2}
\Delta\left[
\sum_\nu p_{\nu a}(\hbar\omega_\nu)^2
\right]
}
```

when the high-temperature expansion is valid.

Thus equilibrium defect isotope fractionation is a quantum vibrational effect rather than a generic classical mass effect.

## 5. Low-temperature limit

For `beta hbar omega >> 1`,

```math
U_\nu\to\frac12\hbar\omega_\nu,
```

and

```math
\boxed{
S_{N_V,a}
\to
\frac{\beta}{4}
\Delta\left[
\sum_\nu p_{\nu a}\hbar\omega_\nu
\right].
}
```

The isotope sensitivity of the equilibrium defect concentration is then controlled by the change in mass-participating zero-point energy upon defect formation.

## 6. Quenched versus annealed defect ensembles

This exposes a necessary theoretical distinction.

### Quenched-defect ensemble

The number of mercury vacancies is fixed independently of the isotope perturbation:

```math
S_{N_V}=0.
```

If electron capture controls SRH,

```math
\boxed{S_{SRH}^{quenched}\simeq S_{C_n}.}
```

This is the appropriate mathematical limit when defects are treated as externally specified structural disorder.

### Annealed/equilibrated-defect ensemble

Vacancies equilibrate with the atomic reservoir at the isotope-dependent formation free energy:

```math
N_V(M,T)\propto e^{-\beta\Delta G_f(M,T)}.
```

Then

```math
\boxed{
S_{SRH}^{annealed}
\simeq S_{C_n}+S_{N_V}.
}
```

Therefore there is no unique 'SRH isotope coefficient' without specifying which defect ensemble is meant.

This is a quenched-versus-annealed statistical-mechanics distinction, not a new physical principle.

## 7. Order-of-magnitude quantum scale

At 77 K,

```text
kT ~ 6.64 meV.
```

HgCdTe optical phonon energies in the narrow-gap capture problem are roughly `15-20 meV`, so `hbar omega/kT` is order `2-3`, not a classical small parameter.

For a representative `17.7 meV` mode,

```math
U=\hbar\omega(N+1/2)\approx10.2\ \text{meV}
```

at 77 K.

A natural-Hg -> 204Hg log-frequency shift of order `-0.00325` changes the free energy of one fully Hg-participating mode by an energy scale of order

```text
|delta F| ~ U |delta ln omega| ~ 0.03 meV.
```

Relative to `kT~6.64 meV`, one uncompensated local-mode contribution corresponds to a defect-concentration change of order `0.5%`.

This is only a scale illustration. Formation free energies contain differences among many modes plus the reservoir, and substantial cancellation is expected.

## 8. Consequence for Experiment 07

A theoretical isotope prediction for total mercury-vacancy-limited SRH recombination requires two distinct calculations if the defect population is annealed:

```text
capture sector:
    isotope derivative of C_n

formation sector:
    isotope derivative of Delta G_f and therefore N_V
```

The 2024/2025 HgCdTe capture papers specify/assume vacancy populations when calculating recombination. Their capture calculation alone therefore cannot determine the annealed total isotope coefficient.

In the quenched-defect ensemble this complication disappears and the previous capture-only theory is sufficient.

## 9. Prior-art boundary

Vibrational contributions to point-defect formation free energies are established finite-temperature defect thermodynamics. Harmonic phonon calculations of defective and pristine cells, including zero-point and entropy terms, are standard.

Do not claim this framework as novel.

The retained Experiment-07 value is conceptual bookkeeping: it prevents a capture isotope coefficient from being silently identified with the total SRH isotope coefficient when defect populations are allowed to equilibrate.

## 10. Next theoretical gate

The active question is now whether Experiment 07 contains any genuinely new HgCdTe-specific theorem beyond:

1. established isotope-sensitive nonradiative capture physics;
2. generic control/convexity identities;
3. generic Laplace/cumulant identities;
4. generic isotope-mode rank/chain-rule closures;
5. generic vibrational defect thermodynamics.

Perform an adversarial novelty audit before adding further model complexity. If the remaining result is only a straightforward isotope perturbation of Kozlov et al.'s established Hg-vacancy capture calculation, close Experiment 07 as a research-novelty path and retain the analytical identities as useful notes.
