# Experiment 07 — Threshold proximity does not imply isotope leverage

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only

## 1. Capture model

For a reduced one-optical-phonon capture channel,

```math
r(M,T)=A(M)\Delta(M)^\nu\exp[-\Delta(M)/(kT)],
```

with simple 3-D phase-space exponent `nu=1/2` and

```math
\Delta(M)=E_{ph}(M)-\varepsilon(M).
```

Here `E_ph=hbar omega` is the participating phonon energy and `epsilon` is the relevant electronic band-to-defect transition energy.

The isotope elasticity is

```math
\boxed{
\frac{\partial\ln r}{\partial\ln M}
=\frac{\partial\ln A}{\partial\ln M}
+\left(\frac{\nu}{\Delta}-\frac1{kT}\right)
\frac{\partial\Delta}{\partial\ln M}.
}
```

The threshold factor can be large when `Delta -> 0`, but only multiplies the isotope derivative of the **detuning**, not the phonon derivative alone.

## 2. Phonon/electronic co-motion

Isotope substitution does not change the Born-Oppenheimer electronic potential at fixed nuclear coordinates to leading order, but observed electronic levels acquire zero-point/electron-phonon renormalization. A minimal harmonic mass-scaling model is

```math
E_{ph}(M)=P M^{-1/2},
```

```math
\varepsilon(M)=\varepsilon_\infty+Z M^{-1/2}.
```

Then

```math
\boxed{
\Delta(M)=-\varepsilon_\infty+(P-Z)M^{-1/2}.
}
```

The isotope leverage is governed by the mismatch `P-Z`, not by the phonon energy `P` alone.

If

```math
Z=P,
```

then

```math
\boxed{
\partial\Delta/\partial M=0
}
```

exactly even if `Delta` is arbitrarily close to zero.

Thus a one-phonon threshold can be spectrally near resonance while being isotope-insensitive because the electronic transition co-moves with the phonon under isotope substitution.

## 3. Formal independence theorem

At reference mass `M0`, write

```math
\Delta(M)=-\varepsilon_\infty+D M^{-1/2},
\qquad D=P-Z.
```

Then

```math
\Delta_0=-\varepsilon_\infty+D M_0^{-1/2},
```

and

```math
s_0\equiv
\left.\frac{\partial\Delta}{\partial\ln M}\right|_{M_0}
=-\frac12D M_0^{-1/2}.
```

Given any finite target pair `(Delta_0,s_0)`, choose

```math
D=-2s_0 M_0^{1/2},
```

and

```math
\varepsilon_\infty=-2s_0-\Delta_0.
```

Therefore

```math
\boxed{
\Delta_0\ \text{places no universal constraint on}\
\partial\Delta/\partial\ln M.
}
```

Threshold proximity and isotope sensitivity are mathematically independent once the electronic transition is allowed its physically expected isotope-dependent zero-point renormalization.

## 4. Co-motion parameter

Define

```math
\chi
=\frac{\partial\varepsilon/\partial\ln M}
{\partial E_{ph}/\partial\ln M}.
```

Then

```math
\boxed{
\frac{\partial\Delta}{\partial\ln M}
=\frac{\partial E_{ph}}{\partial\ln M}(1-\chi).
}
```

Hence

```math
\boxed{
\frac{\partial\ln r}{\partial\ln M}
=\frac{\partial\ln A}{\partial\ln M}
+\left(\frac{\nu}{\Delta}-\frac1{kT}\right)
\frac{\partial E_{ph}}{\partial\ln M}(1-\chi).
}
```

Interpretation:

```text
chi = 0   : electronic level fixed; naive phonon-only isotope picture.
chi = 1   : exact co-motion; detuning isotope leverage vanishes.
chi < 0   : electronic shift opposes phonon shift; detuning leverage is enhanced.
chi > 1   : electronic shift overcompensates phonon shift; isotope response reverses sign.
```

Thus even the **sign** of the threshold isotope response is not fixed by harmonic phonon mass scaling alone.

## 5. Finite-isotope form

For isotope states A and B,

```math
\delta\Delta
=\delta E_{ph}-\delta\varepsilon.
```

The exact reduced-model rate ratio is

```math
\ln(r_B/r_A)
=\ln(A_B/A_A)
+\nu\ln(\Delta_B/\Delta_A)
-\delta\Delta/(kT).
```

If

```math
\delta\varepsilon=\delta E_{ph}
```

and the prefactor is isotope-independent, then

```math
\boxed{r_B/r_A=1}
```

regardless of how small `Delta` is.

## 6. Prior-art boundary

Semiconductor isotope effects on band energies from zero-point/electron-phonon renormalization are established. First-principles work shows that such shifts are material-, band-, phonon-mode-, and many-body-dependent; there is no universal coefficient tying an electronic transition shift to the corresponding phonon-frequency shift.

Large isotope effects on defect nonradiative dynamics are also established experimentally, including isotope-induced changes of local vibrational modes that suppress decay in silicon T centers. These examples demonstrate that large effects are possible; they do not provide a universal lower bound.

The theorem here should therefore be treated as a no-go / clarification, not a novelty claim without a dedicated audit.

## 7. Consequence for Experiment 07

The original intuition

```text
near one-phonon threshold + isotope phonon shift -> large isotope effect
```

is incomplete.

The correct statement is

```text
near one-phonon threshold
+ nonzero phonon/electronic detuning mismatch under isotope substitution
+ sufficiently weak bypass channels
-> potentially large isotope effect.
```

Without microscopic knowledge or a bound on the electronic isotope shift, mass scaling alone cannot guarantee any nonzero isotope effect.

## 8. Next theoretical question

Can general electron-phonon theory place a useful upper bound on `|chi-1|`, or on the differential band-to-defect isotope shift, using only equilibrium quantities such as phonon frequencies, zero-point band-gap renormalization, and defect localization? If no such model-independent bound exists, the universal analytical path for Experiment 07 should be closed and only material-specific first-principles calculation remains.