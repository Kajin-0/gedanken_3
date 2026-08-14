# Repeated Hg-Isotope Crossover and Temperature Sign Test

**Date:** 2026-08-14
**Status:** EXPERIMENT-07 FRONTIER / HGCdTe-SPECIFIC MECHANISM TEST / NOVELTY NOT ESTABLISHED

## 1. Five-step isotope modulation

Use one thin HgCdTe specimen and alternate Hg isotope ambient:

```text
A B A B A
A = natural Hg
B = enriched 204Hg
```

Let `y_j=ln(tau_j)`. Define

```math
C_5=(-y_1+4y_2-6y_3+4y_4-y_5)/8.
```

For a perfect alternating isotope state, `C_5` returns the B-minus-A lifetime shift. Its weights annihilate any drift polynomial through cubic order in cycle number:

```math
sum_j w_j j^p=0,\quad p=0,1,2,3.
```

For independent equal measurement variance `sigma_y^2`,

```math
Var(C_5)=(35/32)sigma_y^2.
```

This is lower than the three-point ABA variance `(3/2)sigma_y^2` while rejecting much higher-order smooth anneal drift.

Apply the same contrast to the measured Raman phonon frequency:

```math
C_omega=(-ln omega_1+4ln omega_2-6ln omega_3+4ln omega_4-ln omega_5)/8.
```

Then, if lifetime responds locally to that phonon coordinate plus smooth drift,

```math
K_Hg ~= C_5/C_omega.
```

The ratio does not require complete isotope exchange or equal B-state uptake; the measured Raman modulation is the calibration. A natural-Hg AAAAA control with the same contrast measures residual non-smooth anneal curvature/systematics.

For a target reversible lifetime contrast `|C_5|=2%`, 5-sigma detection from independent lifetime measurement noise alone requires approximately

```text
single-measurement log-lifetime sigma < 0.38%.
```

For 1% contrast the corresponding value is ~0.19%.

## 2. Isotope uptake must be measured, not assumed

Hg radiotracer work in epitaxial CdxHg1-xTe reports two diffusion components and substantially reduced surface tracer incorporation in epitaxial material. Therefore the earlier ideal constant-surface exchange fraction is only a feasibility upper estimate.

Required order:

```text
1. isotope anneal
2. SIMS on sacrificial sister piece
3. Raman on the actual lifetime specimen
4. only then interpret lifetime
```

The independent isotope perturbation variable is `C_omega`, not vapor isotope fraction or an assumed diffusion profile.

## 3. Temperature sign test for one optical phonon

For the minimal single-optical-phonon phase-space model

```math
r \propto sqrt(Delta) exp[-Delta/(kT)],
\qquad Delta=hbar omega-E_b,
```

an SRH-dominated lifetime has

```math
K_omega(T)=d ln tau/d ln omega
=hbar omega[1/(kT)-1/(2Delta)].
```

Hence the isotope effect changes sign at

```math
kT_x=2Delta.
```

Thus a measured reversible Hg-isotope lifetime contrast that crosses zero versus temperature directly estimates

```math
Delta=kT_x/2.
```

Examples for the simple spontaneous-emission limit:

```text
Delta=0.5 meV -> T_x=11.6 K
Delta=1.0 meV -> T_x=23.2 K
Delta=2.0 meV -> T_x=46.4 K
Delta=3.0 meV -> T_x=69.6 K
```

Including the optical-phonon stimulated-emission factor `n_B+1` shifts the upper examples only modestly for a ~17.7 meV mode; the exact crossover satisfies

```math
kT_x=2Delta[n_B(omega,T_x)+1].
```

The acoustic-cutoff model does not generically predict this same sign reversal because lowering the cutoff monotonically reduces the fraction of carriers eligible for one-acoustic-phonon capture.

Therefore temperature dependence can distinguish a sharp optical-phonon threshold from a simple acoustic-cutoff picture and from many isotope-independent anneal drifts.

## 4. Prior-art boundary update

General isotope substitution as a defect-identification tool is established. In 2026, a silicon T-center study demonstrated a >5x isotope-dependent excited-state lifetime and linked it to an isotope-shifted local vibrational mode suppressing nonradiative decay. Therefore Experiment 07 cannot claim the general principle of isotope-controlled nonradiative lifetime as new.

The remaining target is narrow and HgCdTe-specific:

```text
reversible Hg-isotope perturbation
+ measured HgTe-like Raman shift
+ SRH-dominated lifetime response
+ predicted temperature/phonon-branch behavior
-> test of the proposed single-optical-phonon mercury-vacancy capture mechanism.
```

## 5. Next kill test

Before any expensive isotope program:

1. precondition a thin HgCdTe layer under repeated natural-Hg anneals until Raman, Eg, Hall/vacancy proxy and lifetime stabilize;
2. demonstrate measurable Hg isotope uptake by SIMS/Raman;
3. execute at least ABA, preferably ABABA, on the same specimen;
4. measure lifetime at multiple temperatures spanning a predicted crossover region;
5. reject the mechanism if lifetime does not reversibly track the Raman isotope shift or if the inferred response is explainable by Eg/vacancy changes.

No manuscript construction or novelty claim is authorized.