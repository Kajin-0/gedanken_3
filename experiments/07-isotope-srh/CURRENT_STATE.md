# Current State — Experiment 07: Isotope-Tuned SRH Capture in HgCdTe

**Date:** 2026-08-13  
**Status:** ACTIVE PROVISIONAL / SINGLE-PHONON THRESHOLD LEVER IDENTIFIED / NOVELTY NOT ESTABLISHED

## Question

Can isotopic mass engineering change HgCdTe dark generation by moving a mercury-vacancy carrier-capture channel across a one-phonon kinematic threshold, while leaving the electronic chemistry approximately unchanged?

This is narrower than generic "phonon engineering suppresses SRH." A micron-scale phononic crystal is not the target: the relevant HgCdTe lattice modes are THz and require essentially atomic-scale control.

## Prior-art boundary

Established and not claimed as new:

- isotope substitution shifts semiconductor phonon frequencies approximately through mass scaling and can alter electron-phonon physics;
- nonradiative defect capture depends sensitively on defect vibrational modes;
- HgCdTe mercury vacancies can capture holes by acoustic-phonon cascades or single optical-phonon emission;
- in narrow-gap (~40 meV) HgCdTe, published calculations find both electron and hole capture by mercury-vacancy states can proceed through single optical-phonon emission and can make SRH recombination lifetime-limiting at 4.2 and 77 K for sufficient vacancy density.

Targeted searching has not yet found isotope-engineered HgCdTe SRH/dark-current measurements. This absence is not proof of novelty.

Key adjacent papers:

- Kozlov et al., Photonics 9, 887 (2022), DOI 10.3390/photonics9120887.
- Kozlov et al., JETP 165, 840-847 (2024), DOI 10.31857/S0044451024060117.
- Kozlov et al., Semicond. Sci. Technol. 40, 035007 (2025), DOI 10.1088/1361-6641/ada9ce.
- modern first-principles multiphonon-capture theory, e.g. Phys. Rev. B 111, 045201 and 115202 (2025).

## Generic isotope result

To leading Born-Oppenheimer order, isotope substitution changes nuclear masses but not the electronic potential-energy surfaces.

For a harmonic configuration coordinate,

```math
omega=sqrt(K/M_eff),
```

while the reorganization energy

```math
lambda=K Delta R^2/2
```

is mass-independent.

Therefore the classical high-temperature Marcus-type capture exponent is mass-independent. Generic isotope leverage exists only through quantum vibrational corrections, zero-point shifts, mode mixing/renormalization, and secondary electronic renormalization.

For a low-temperature single-mode Franck-Condon model,

```math
S=lambda/(hbar omega),
N=Delta E/(hbar omega).
```

A strong near-activationless transition changes only weakly under a few-percent frequency shift. Large isotope leverage in this generic model requires an already exponentially weak Franck-Condon transition.

## HgCdTe-specific threshold exception

HgCdTe vacancy binding energies are reported in the approximate 10-20 meV range, close to acoustic cutoffs and optical-phonon energies.

For acoustic one-phonon capture of a thermal carrier with kinetic energy E into a bound state of ionization energy Eb,

```math
E+Eb <= hbar omega_max.
```

Define

```math
Delta = hbar omega_max - Eb.
```

For a 3-D Maxwell-Boltzmann carrier distribution, the fraction of carriers with `E<Delta` is

```math
F(Delta)=erf(sqrt(u))-(2/sqrt(pi))*sqrt(u)*exp(-u),
qquad u=Delta/(kT).
```

Near threshold,

```math
boxed: F ~ (4/(3 sqrt(pi))) [Delta/(kT)]^(3/2).
```

Thus the capture phase space can be far more isotope-sensitive than the generic multiphonon exponent when `Eb` lies close to a phonon cutoff. If isotope substitution moves `hbar omega_max` below `Eb`, that one-phonon channel closes.

For a nearly dispersionless optical phonon, energy conservation instead selects approximately

```math
E*=hbar omega_op-Eb.
```

The channel exists only for `E*>=0`; a minimal 3-D carrier phase-space factor scales as

```math
sqrt(E*) exp[-E*/(kT)].
```

Again, an isotope shift can switch the channel on/off only near resonance.

## Correct isotope scale

Using standard atomic weights as the natural-material reference and the most generous stable-isotope endpoints:

```text
HgTe-like mode:
  all-light vs natural  ~ +2.36% frequency
  all-heavy vs natural  ~ -0.89%
  full light-to-heavy span ~3.29%

CdTe-like mode:
  all-light vs natural  ~ +3.05%
  all-heavy vs natural  ~ -1.26%
  full light-to-heavy span ~4.36%
```

Therefore engineering ordinary natural material toward the heaviest isotopes moves a 10-20 meV phonon by only roughly 0.1-0.25 meV. A large dark-current effect requires a capture channel already lying within that narrow energy window of a phonon threshold/resonance.

## First numerical stress

At 77 K (`kT ~ 6.64 meV`) with the literature HgTe-like LA cutoff `10.56 meV`, a simple heavy-isotope scaling gives about `10.47 meV`.

The threshold phase-space model therefore predicts strong relative sensitivity only for vacancy binding energies very near the cutoff. Farther from threshold the isotope effect rapidly falls to a modest perturbation.

The companion script `numerics/isotope_threshold.py` prints the exact reduced-mass frequency shifts and acoustic/optical threshold stress sweeps.

## Main risks / kill conditions

1. **Bypass pathways:** excited-state cascades, other acoustic branches, optical phonons, multiphonon capture, or another carrier-capture step may bypass the shifted threshold.
2. **Wrong bottleneck:** changing one capture coefficient does little if the opposite carrier capture controls the SRH cycle.
3. **Alloy/defect-energy spread:** if the distribution of vacancy binding energies is much broader than the isotope-induced phonon shift, an ensemble device will smear the threshold.
4. **Bandgap confounder:** isotope-dependent zero-point electron-phonon renormalization can shift electronic energies; any dark-current comparison must separate this from a pure capture-coefficient effect.
5. **Practical enrichment:** natural-to-heavy frequency shifts are only ~1%, much smaller than the full isotope-endpoint span.

## Next hard step

Build the minimal two-step SRH cycle with isotope-dependent `C_n(M)` and `C_p(M)` from one-phonon kinematics plus explicit alternative channels. Determine whether any realistic vacancy-energy/phonon-energy region gives a >2x lifetime or dark-generation change after:

- both electron and hole capture are included;
- at least one isotope-insensitive bypass channel is allowed;
- a finite distribution of defect binding energies is convolved in.

If a >2x effect requires sub-0.1-meV fine tuning or an unrealistically narrow defect-energy distribution, close the engineering path and retain isotope substitution only as a spectroscopy/diagnostic proposal.

Do not claim novelty or begin manuscript construction.