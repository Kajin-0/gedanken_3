# Experiment 10 — Founding Gedanken Model

**Date:** 2026-08-14  
**Mode:** analytical/theoretical only

## 1. Minimal question

Take a target long-wavelength infrared cutoff and operating temperature,

```math
\lambda_c=10\ \mu\mathrm{m},
\qquad
T=300\ \mathrm{K}.
```

Can an unknown passive semiconductor `X` be designed, at the level of its electronic structure, so that its intrinsic detector performance is comparable to the best physically admissible HgCdTe reference while retaining a finite useful response speed?

The first objective is **not** to search a materials database. It is to determine what a material would have to be.

## 2. Fixed gap

For an interband cutoff,

```math
E_g=\frac{hc}{\lambda_c}.
```

At 10 um,

```math
E_g\approx 0.12398\ \mathrm{eV}.
```

At 300 K,

```math
k_B T\approx 0.02585\ \mathrm{eV},
\qquad
E_g/(k_B T)\approx 4.80.
```

Therefore changing chemistry while retaining the same 10-um cutoff does not change the dominant Boltzmann gap factor. Any intrinsic advantage must arise from other parts of the electronic structure or from changing which generation pathways are kinematically available.

## 3. Reference-matching conditions

The first comparison should remove trivial optical and geometric advantages. Require `H` and `X` to have the same:

```text
cutoff energy;
operating temperature;
detector area;
accepted optical etendue;
incident optical field;
external absorptance spectrum over the task band;
and required temporal response.
```

These conditions may later be relaxed one at a time, but not before the matched problem is understood.

## 4. Why an absorption constraint is mandatory

A material with arbitrarily low density of states can trivially reduce thermal carrier population if it is also allowed to become an arbitrarily weak absorber. That is not a useful detector improvement.

The true optimization is constrained:

```math
\text{minimize internal fluctuation/generation cost}
```

subject to

```math
A(\omega)\ge A_0(\omega)
```

and a temporal requirement such as

```math
f_{3\mathrm{dB}}\ge f_0.
```

The central theoretical tension is therefore between

```text
thermodynamic DOS,
interband optical oscillator strength,
nonradiative phase space,
and response time.
```

## 5. First two dispersion classes

### A. Parabolic two-band comparator

Use

```math
E_c(k)=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
```

```math
E_v(k)=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h}.
```

The usual nondegenerate intrinsic-density estimate is

```math
n_i=\sqrt{N_cN_v}\exp[-E_g/(2k_BT)].
```

This is useful as a controlled finite-gap comparator only where its statistical and parabolic assumptions remain valid.

### B. Massive-Dirac/Kane comparator

Use

```math
E_\pm(k)=\pm\sqrt{\Delta^2+(\hbar vk)^2},
\qquad
\Delta=E_g/2.
```

Its exact 3-D density of states per included degeneracy factor is proportional to

```math
g(E)\propto
\frac{|E|\sqrt{E^2-\Delta^2}}
{\hbar^3v^3},
\qquad |E|\ge\Delta.
```

Near the edge,

```math
m_D=\frac{E_g}{2v^2}.
```

At fixed finite `E_g`, increasing `v` therefore lowers the near-edge DOS scale. Whether this produces a detector advantage after the absorption constraint is imposed is the first open problem.

## 6. Exact-statistics caution inherited from Experiment 08

Experiment 08 proved that substituting

```math
m_D=E_g/(2v^2)
```

into a nondegenerate parabolic formula and then sending `E_g -> 0` gives the wrong limit. The exact Kane neutrality problem has a finite zero-gap carrier density in the reduced model.

Experiment 10 is deliberately a **finite-gap, room-temperature** problem. Nevertheless, exact Fermi-Dirac integrals should replace Maxwell-Boltzmann approximations whenever the latter materially affect the result.

Do not use Experiment 10 as a pretext to reopen the closed zero-gap novelty path.

## 7. Radiative floor before nonradiative detail

If two reciprocal detectors have the same external absorptance spectrum and optical environment, Kirchhoff/detailed-balance physics tightly constrains their unavoidable radiative exchange with that environment.

A possible theorem target is therefore:

> Under matched absorptance, temperature, etendue, and optical environment, identify which parts of the detector fluctuation floor are material-independent and which can still be reduced by changing electronic dispersion.

This statement must be derived with a precise detector/noise model before it is promoted to a theorem.

## 8. Add Auger only after the matched optical problem

For a clean narrow-gap material, intrinsic Auger generation/recombination is an obvious room-temperature obstacle. The rate is controlled not only by carrier density but by matrix elements and simultaneous energy/momentum conservation.

Schematically,

```math
R_A\propto
\int |M|^2
f_1f_2(1-f_3)(1-f_4)
\delta(E_1+E_2-E_3-E_4)
\delta(\mathbf k_1+\mathbf k_2-\mathbf k_3-\mathbf k_4-\mathbf G)
d\Gamma.
```

Thus there are two qualitatively different routes to small Auger generation:

```text
reduce thermal carrier population;
reduce or close the allowed Auger phase space.
```

The second route is a dispersion problem, not merely a lifetime parameter.

## 9. Why bandwidth belongs in the theorem

A detector can often suppress a noise rate by making an internal process arbitrarily slow. That does not establish useful detectability.

Any eventual admissibility result should therefore contain a response constraint such as

```math
\tau_{det}\le\tau_0
```

or

```math
f_{3\mathrm{dB}}\ge f_0.
```

This is inherited conceptually from Experiment 01: scalar asymptotic sensitivity does not completely order detectors with different temporal response.

## 10. Possible final mathematical object

The desired endpoint is an admissible set of electronic-structure parameters or functions,

```math
\mathcal A(T,\lambda_c,A_0,f_0)
```

such that membership implies the material can, in principle, reach a specified intrinsic detector-quality threshold.

A schematic parameterized version might involve

```math
\{E_g,\ g_v,\ m_e^*,\ m_h^*,\ v_{cv},\Delta_{SO},\epsilon,\text{Auger phase-space data},\ldots\}.
```

The actual theorem should eliminate phenomenological parameters wherever a more primitive band-structure relation is available.

## 11. First hard stop

Do not proceed directly to T2SLs, 2-D materials, quantum dots, or a list of candidate compounds.

First answer:

> For two matched finite-gap absorbers, one parabolic and one massive-Dirac, can lower thermodynamic DOS coexist with the same useful absorptance without an exact compensating cost?

If the answer is no, derive the invariant/no-go. If yes, quantify the surviving degree of freedom. Only then add Auger phase-space constraints.
