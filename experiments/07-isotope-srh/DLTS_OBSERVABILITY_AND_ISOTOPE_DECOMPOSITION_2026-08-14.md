# DLTS Observability and Isotope Decomposition

**Date:** 2026-08-14
**Status:** DIRECT-CAPTURE ROUTE PASSES FIRST OBSERVABILITY GATE / TEMPERATURE SIGN TEST RESTRICTED TO NEAR-THRESHOLD CASE / NOVELTY NOT ESTABLISHED

## 1. Separate capture from emission

For a hole trap,

```math
e_p(T,M)=C_p(T,M)N_v(T,M)\exp[-E_a(M)/(kT)].
```

Therefore between two isotope states,

```math
\Delta\ln e_p=\Delta\ln C_p+\Delta\ln N_v-\Delta E_a/(kT).
```

Ordinary Arrhenius DLTS cannot by itself identify whether an isotope shift changed the microscopic capture coefficient or the electronic trap/band-edge energy. This is especially dangerous when `C_p(T)` is itself strongly temperature dependent.

The primary Experiment-07 observable should therefore be **direct filling kinetics**, with emission DLTS retained as a second, independent channel.

For a simple filling transient,

```math
A(t_p)=A_\infty[1-\exp(-C_p p t_p)].
```

Then

```math
\tau_c=(C_p p)^{-1}.
```

Measure `p` independently by C-V/Hall or the appropriate device electrostatics, and infer `C_p` from the full pulse-length dependence.

## 2. Capture-time scale is feasible

Modern HgCdTe DLTS reports a vacancy-like hole capture-cross-section range roughly `sigma_p=1e-16` to `4e-15 cm^2`. Older n-HgCdTe DLTS reported about `1e-16 cm^2` for a major electron trap. These are experimental scales, not asserted to be the exact narrow-gap V_Hg transition targeted here.

Using the commonly used HgCdTe heavy-hole mass `m_h*=0.65m0`, the 77-K thermal velocity is about `7.34e6 cm/s`, giving

```text
sigma=1e-16 cm^2   -> C ~7.34e-10 cm^3/s
sigma=1e-15 cm^2   -> C ~7.34e-9  cm^3/s
sigma=4e-15 cm^2   -> C ~2.94e-8  cm^3/s
```

Representative filling times at 77 K are:

```text
p=1e13 cm^-3:  tau_c ~136 us, 13.6 us, 3.41 us
p=1e14 cm^-3:  tau_c ~13.6 us, 1.36 us, 0.341 us
p=1e15 cm^-3:  tau_c ~1.36 us, 0.136 us, 0.034 us
```

Thus the useful parameter space naturally reaches tens of nanoseconds through hundreds of microseconds. Carrier density can be used as a tuning variable rather than accepting one fixed capture time.

DLTS filling-pulse methods for direct capture-cross-section determination are established; very short filling pulses are a known practical complication, not a new concept.

## 3. Sensitivity of the filling curve

Let `x=C_p p t_p`. Then

```math
\frac{\partial(A/A_\infty)}{\partial\ln C_p}=x e^{-x}.
```

This is maximized at `x=1`:

```math
\boxed{\max \partial(A/A_\infty)/\partial\ln C_p=e^{-1}=0.368.}
```

Therefore, near the optimal filling time:

```text
1% change in C_p -> ~0.368% of full transient amplitude
2% change in C_p -> ~0.736%
5% change in C_p -> ~1.84%
```

A single-point 5-sigma detection of a 2% capture-coefficient contrast with independent equal noise would require about 0.10% repeatability in normalized transient amplitude. The preferred experiment fits multiple filling times jointly and should outperform this deliberately conservative single-point comparison.

## 4. Emission windows are not the primary limitation

Using the standard emission form with `m_h*=0.65m0` and illustrative `sigma=1e-15 cm^2`, a nominal measurement window from `1` to `1e6 s^-1` is reached at approximately:

```text
E_a=10 meV -> 6.4 to 17.8 K
E_a=20 meV -> 11.9 to 30.6 K
E_a=40 meV -> 22.3 to 53.3 K
E_a=89 meV -> 46.4 to 103 K
```

These are only scale estimates because the temperature dependence of `C_p` is the quantity under test. They show that shallow narrow-gap traps are not automatically outside transient-spectroscopy timescales; they move the useful experiment to lower temperature.

HgCdTe DLTS has already been demonstrated in a 96-meV-gap material at 30 K with both electron and hole trapping parameters attributed to a possible common SRH center. This is strong enabling prior art, not novelty.

## 5. The optical-phonon temperature sign test has a hidden filling constraint

For the minimal single-optical-phonon model,

```math
C_p\propto\sqrt{\Delta}\exp[-\Delta/(kT)],
\qquad \Delta=\hbar\omega-E_b,
```

and

```math
K_C=\frac{\partial\ln C_p}{\partial\ln\omega}
=\hbar\omega[1/(2\Delta)-1/(kT)].
```

The simple sign crossover is `kT_x=2Delta`.

However the trap must remain fillable at `T_x`. Using `hbar omega=17.73 meV`, the implied activation scale is `E_a~hbar omega-Delta`. The ratio of thermal emission to filling capture is approximately

```math
\frac{e_p}{C_p p}=\frac{N_v e^{-E_a/(kT)}}{p},
```

independent of the absolute capture coefficient.

Representative values at the predicted crossover are:

```text
Delta=0.5 meV, T_x=11.6 K:
  p=1e14 -> essentially complete filling

Delta=1.0 meV, T_x=23.2 K:
  p=1e15 -> ~94% equilibrium filling

Delta=2.0 meV, T_x~47 K:
  p=1e16 -> only ~37% filling

Delta=3.0 meV, T_x~74 K:
  p=1e16 -> only ~6% filling
```

Therefore the dramatic temperature sign-reversal test is self-consistent mainly for a genuinely near-threshold optical channel, roughly `Delta <= 1 meV` at modest injection. For larger detuning, Experiment 07 should measure the low-temperature isotope dependence of `C_p(T)` rather than chase the crossover into a regime where emission empties the trap.

## 6. Measurement hierarchy

The preferred decomposition is now:

```text
A. direct filling kinetics
   -> C_p(T,M) or C_n(T,M)

B. emission DLTS / Laplace-DLTS
   -> e_p(T,M), trap spectrum, E_a-like information

C. C-V / Hall
   -> carrier density and depletion width

D. DLTS amplitude
   -> trap concentration N_t

E. Raman
   -> actual isotope-induced phonon shift

F. SIMS on sacrificial material
   -> isotope depth profile
```

Then use

```math
\Delta E_a
=-kT[\Delta\ln e_p-\Delta\ln C_p-\Delta\ln N_v]
```

as a consistency check rather than folding electronic and phononic isotope effects into one apparent Arrhenius intercept.

## 7. Prior-art boundary

Established:

- DLTS in narrow-gap HgCdTe, including electron and hole capture at a possible common SRH center (Polla & Jones, Solid State Communications 36, 809-812, 1980, DOI 10.1016/0038-1098(80)90017-4).
- HgCdTe trap capture-cross-section extraction by DLTS.
- direct capture-cross-section extraction from filling-pulse dependence.
- temperature-dependent capture coefficients and the danger of interpreting Arrhenius intercepts as fixed cross sections.
- general isotope-dependent nonradiative defect dynamics.

A targeted search has not found an isotope-dependent HgCdTe DLTS capture-coefficient experiment. Absence from this search is not proof of novelty.

## 8. Current disposition

```text
total-lifetime isotope experiment: REJECTED
thin isotope layer + direct DLTS capture coefficient: RETAIN
capture-time feasibility: PASS
ordinary Arrhenius intercept as isotope observable: REJECT
optical-phonon sign crossover: RETAIN ONLY FOR Delta ~<=1 meV
low-T C_p(T) isotope comparison: LEADING MECHANISM TEST
novelty: NOT ESTABLISHED
paper drafting: DO NOT BEGIN
```

## Next hard step

Determine the smallest experimentally resolvable isotope change in `C_p(T)` after realistic uncertainty in carrier density, pulse calibration, trap nonuniformity and device-to-device processing is included. Then compare that floor with the broadened/bypass one-phonon model's predicted natural-Hg -> 204Hg capture-coefficient contrast.

If the predicted contrast falls below realistic direct-capture metrology, close Experiment 07. If a 1-5% reversible `C_p` contrast survives, proceed to a concrete shallow-junction test structure.