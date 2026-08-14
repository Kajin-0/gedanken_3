# Zero-Gap Kane Pair-Fluctuation Asymptotic

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** RETAIN AS TECHNICAL EXTENSION / GENERAL DEGENERATE GR-FLUCTUATION THEORY IS ESTABLISHED / DOES NOT REOPEN EXPERIMENT 08

## 1. Question

Experiment 08 found that a zero-gap Kane HgCdTe model can have a substantial equilibrium carrier density while the intrinsic chemical potential lies several `kT` inside the conduction cone.

Does the equilibrium electron-hole pair-number variance remain Poisson-like and therefore scale directly with the mean carrier density?

No. Degeneracy suppresses the electronic compressibility.

## 2. Neutral-pair thermodynamic susceptibility

Let `n=p` at intrinsic equilibrium. Consider a neutral pair fluctuation

```math
\delta n=\delta p=\delta N/V.
```

Let the independent electron and hole susceptibilities be

```math
\chi_e=\frac{\partial n}{\partial\mu_e},
\qquad
\chi_h=\frac{\partial p}{\partial\mu_h}.
```

The free-energy curvature along the neutral-pair coordinate is

```math
\frac{\partial^2 f}{\partial n_{pair}^2}
=\chi_e^{-1}+\chi_h^{-1}.
```

Therefore the effective pair susceptibility is the harmonic combination

```math
\boxed{
\chi_{pair}
=\frac{\chi_e\chi_h}{\chi_e+\chi_h}.
}
```

The equilibrium pair-number variance in volume `V` is

```math
\boxed{
\operatorname{Var}N_{pair}
=kT V\chi_{pair}.
}
```

Define single-species compressibility/Fano factors

```math
F_e=\frac{kT\chi_e}{n},
\qquad
F_h=\frac{kT\chi_h}{p}.
```

For `n=p`,

```math
\boxed{
F_{pair}
\equiv\frac{\operatorname{Var}N_{pair}}{nV}
=\frac{F_eF_h}{F_e+F_h}.
}
```

In the nondegenerate intrinsic limit `F_e=F_h=1`, giving

```math
\boxed{F_{pair}=1/2.}
```

This is the familiar harmonic-mean form of intrinsic generation-recombination number fluctuations.

## 3. Zero-gap Kane electron factor

At `E_g=0`, the massless conduction cone has

```math
n=A I_2(\eta),
\qquad
A=\frac{(kT)^3}{\pi^2\hbar^3v^3},
```

where

```math
\eta=\mu/(kT).
```

Using

```math
\frac{d I_2}{d\eta}=2I_1,
```

```math
\boxed{
F_e=\frac{2I_1(\eta)}{I_2(\eta)}.
}
```

For `eta>>1`,

```math
I_2\simeq\eta^3/3+\pi^2\eta/3,
```

```math
I_1\simeq\eta^2/2+\pi^2/6,
```

so

```math
\boxed{F_e\simeq3/\eta}
```

at leading order.

Thus the mean electron number can be large while the incremental thermodynamic number variance is strongly sub-Poissonian.

## 4. Heavy-hole factor

In the low-temperature zero-gap asymptotic from Experiment 08, the heavy-hole population that balances the degenerate cone is exponentially small per available state but multiplied by a large DOS reservoir.

The holes themselves remain approximately Boltzmann distributed with respect to their quasi-Fermi coordinate, so

```math
\boxed{F_h\to1.}
```

The light-hole contribution is asymptotically subleading once `eta>>1`.

## 5. Representative 77-K zero-gap result

Using the same reduced model as Experiment 08:

```text
v = 1.07e6 m/s
m_hh = 0.5 m0
T = 77 K
eta ~= 5.308
n ~= 5.70e15 cm^-3
```

one obtains approximately

```text
F_e ~= 0.467
F_h ~= 0.998
```

and therefore

```math
\boxed{F_{pair}\simeq0.318.}
```

Compared with the classical intrinsic value `1/2`, the equilibrium neutral-pair variance per mean carrier is suppressed by about 36 percent.

This does not mean the total detector GR noise is reduced by exactly 36 percent, because the dynamic noise spectrum also depends on the recombination/generation kinetic matrix and terminal transduction.

## 6. Low-temperature asymptotic

Experiment 08 found

```math
\eta\simeq3W(\mathcal C T^{-1/2})
```

and

```math
n\simeq
\frac{9(kT)^3}{\pi^2\hbar^3v^3}W^3.
```

Since

```math
F_e\simeq3/\eta\simeq1/W,
```

and `F_h->1`,

```math
F_{pair}
=\frac{F_eF_h}{F_e+F_h}
\simeq\frac{1}{W+1}
\sim\frac1W.
```

Hence

```math
\boxed{
F_{pair}\sim\frac1{\ln(T_0/T)}.
}
```

The pair-variance density becomes

```math
\boxed{
\frac{\operatorname{Var}N_{pair}}V
=nF_{pair}
\sim
T^3[\ln(T_0/T)]^2.
}
```

Thus the zero-gap mean carrier density scales as `T^3 ln^3`, while the equilibrium neutral-pair fluctuation variance loses one logarithmic factor through Fermi compressibility.

## 7. Physical interpretation

At zero gap, heavy-hole DOS asymmetry pushes the intrinsic chemical potential into the conduction cone by many thermal energies. The electron population is therefore degenerate in the dimensionless sense.

Pauli filling makes adding/removing another electron progressively harder, so

```math
kT\partial n/\partial\mu < n.
```

The hole reservoir remains approximately classical. Since a neutral generation-recombination event must fluctuate electrons and holes together, the stiffer electron subsystem controls the pair susceptibility through the harmonic combination.

Therefore:

```text
large mean intrinsic carrier density
!=
Poissonian pair-number fluctuation amplitude.
```

## 8. Prior-art boundary

This is not a new general fluctuation principle.

K. M. van Vliet, Phys. Rev. 110, 50 (1958), derived the spontaneous carrier-fluctuation spectral-density matrix from irreversible thermodynamics and explicitly states that the closed-form theory is valid for both nondegenerate and degenerate semiconductors. The paper also establishes agreement between the Einstein relation and the extended generation-recombination variance theorem.

Later bipolar Langevin/master-equation GR-noise theory treats electron and hole fluctuations jointly and warns that monopolar approximations fail when minority-carrier fluctuations matter.

Therefore the present result is only the **massless-Kane specialization** of established degenerate-semiconductor fluctuation thermodynamics.

## 9. Disposition

```text
zero-gap mean-vs-variance distinction: RETAIN
F_pair ~ T^3 ln^2 variance scaling: RETAIN AS KANE ASYMPTOTIC
new GR-noise theorem: NO
Experiment 08 novelty status: REMAINS CLOSED
```

Do not infer a full terminal-noise PSD from this equilibrium variance alone. Any frequency-dependent GR-noise prediction requires the transition-rate/relaxation matrix and readout transfer function.
