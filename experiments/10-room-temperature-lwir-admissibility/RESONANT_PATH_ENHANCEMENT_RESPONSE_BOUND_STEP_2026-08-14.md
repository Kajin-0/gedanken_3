# Experiment 10 — Resonant Path Enhancement Versus Temporal Response

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **ONE-PORT TCMT RESPONSE/LOSS BOUND DERIVED / FINITE RESPONSE ALONE DOES NOT RESTORE A UNIVERSAL CARRIER-COLUMN FLOOR / NEW ELECTROMAGNETIC PARTICIPATION RESOURCE IDENTIFIED / BROADBAND THICKNESS-BANDWIDTH LIMITS ARE PRIOR ART / NOVELTY NOT ESTABLISHED**

## 1. Why this step is necessary

The current Experiment-10 theorem gives, for a controlled single-pass absorber whose useful absorption is dominated by the active finite-gap massive-Dirac pair,

```math
\Sigma_c\ge C/v_{adm}^2,
```

where `v_adm` incorporates the microscopic hopping ceiling and spectator-band Auger-closure ceiling.

But the physical-thickness step

```math
d=\zeta/\alpha_D
```

is not valid for an arbitrary resonant or slow-light structure. A weakly absorbing thin material can be critically coupled to a cavity and reach high or perfect external absorptance because the field samples it repeatedly.

This step asks:

> Does a finite detector temporal-response requirement by itself prevent arbitrarily large resonant path enhancement and restore a universal lower bound on physical active-carrier sheet density?

Start with the simplest one-port, single-resonance temporal coupled-mode theory (TCMT). This is deliberately not yet a general passive electromagnetic bound.

---

## 2. One-port resonator

Use the standard TCMT normalization in which

```math
U=|a|^2
```

is stored modal energy and

```math
P_\pm=|s_\pm|^2
```

are input/output powers.

For resonance frequency `omega_0`, external leakage rate `gamma_e`, and internal absorption rate `gamma_i`, write

```math
\boxed{
\dot a
=(i\omega_0-\gamma_e-\gamma_i)a
+\sqrt{2\gamma_e}\,s_+.
}
```

For a one-port system with direct reflection phase `pi`,

```math
s_-=-s_++\sqrt{2\gamma_e}\,a.
```

This is standard temporal coupled-mode theory and not a novelty claim.

For monochromatic detuning

```math
\delta\omega=\omega-\omega_0,
```

the absorptance is

```math
\boxed{
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\delta\omega)^2+(\gamma_e+\gamma_i)^2}.
}
```

At resonance,

```math
\boxed{
A_0
=\frac{4\gamma_e\gamma_i}
{(\gamma_e+\gamma_i)^2}.
}
```

Perfect absorption requires critical coupling

```math
\boxed{\gamma_e=\gamma_i.}
```

All of these facts are established photonic-resonator physics.

---

## 3. Define an unambiguous optical response time

The cavity **field-envelope** response has pole

```math
\gamma_{tot}=\gamma_e+\gamma_i.
```

Define

```math
\boxed{
\tau_{opt}
\equiv\frac{1}{\gamma_e+\gamma_i}.
}
```

This is the amplitude-envelope time constant and also the small-signal pole scale for modulation of the absorbed power about a resonantly driven steady state.

The energy ringdown time is smaller by a factor of two:

```math
\tau_U=\frac{1}{2(\gamma_e+\gamma_i)}.
```

These conventions must not be mixed.

At critical coupling,

```math
\tau_{opt}=\frac{1}{2\gamma_i},
```

and the optical absorption spectrum has angular-frequency FWHM

```math
\Delta\omega_{FWHM}=4\gamma_i.
```

Therefore

```math
\tau_{opt}\Delta\omega_{FWHM}=2,
```

while

```math
\tau_U\Delta\omega_{FWHM}=1.
```

This elementary lifetime/linewidth relation is established and not novel.

---

## 4. General target absorptance, not only A=1

Let

```math
x=\gamma_e/\gamma_i.
```

At resonance,

```math
A_0=\frac{4x}{(1+x)^2}.
```

For a specified `0<A_0<=1`, there are under-coupled and over-coupled solutions related by `x -> 1/x`.

Define

```math
s=\sqrt{1-A_0}.
```

The over-coupled solution is

```math
x_+=\frac{1+s}{1-s}.
```

For a given allowed response time, the over-coupled branch minimizes the required internal material loss.

Since

```math
\tau_{opt}^{-1}=\gamma_i(1+x_+),
```

one obtains exactly

```math
\boxed{
2\gamma_i
=\frac{1-\sqrt{1-A_0}}{\tau_{opt}}.
}
```

Define

```math
\boxed{
g(A_0)=1-\sqrt{1-A_0}.}
```

Then a response requirement

```math
\tau_{opt}\le\tau_{max}
```

implies

```math
\boxed{
2\gamma_i\ge\frac{g(A_0)}{\tau_{max}}.
}
```

For perfect absorption, `g(1)=1`, recovering the critical-coupling result.

For the Experiment-10 witness `A_0=0.90`,

```text
g(0.90) = 0.68377223398.
```

---

## 5. Relate internal loss to active absorber amount

The active absorber contributes internal dissipated power

```math
P_{abs}=2\gamma_i U.
```

For active material absorption coefficient `alpha_D` and physical active thickness `d`, define the electromagnetic **sampling-rate resource**

```math
\boxed{
\Lambda_a
\equiv
\frac{P_{abs}}
{\alpha_D d\,U}
=\frac{2\gamma_i}{\alpha_D d}.
}
```

`Lambda_a` has units of inverse time.

It measures how rapidly one unit of stored optical energy samples a unit single-pass optical depth of the active absorber. It contains geometry, mode confinement, group velocity, standing-wave enhancement, and absorber participation.

This definition is exact at the operating point; treating `Lambda_a` as independent of absorber loss is an additional weak-loss/design assumption when using it parametrically.

Then

```math
\boxed{
2\gamma_i=\Lambda_a\alpha_Dd.
}
```

Combining with the temporal-response condition gives

```math
\boxed{
\alpha_Dd
\ge
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

Thus finite response prevents arbitrarily small material optical depth **at fixed `Lambda_a`**.

---

## 6. Carrier-column consequence

The physical active electron sheet population is

```math
\Sigma_c=n_cd.
```

Hence

```math
\boxed{
\Sigma_c
\ge
\frac{n_c}{\alpha_D}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

For the active finite-gap Dirac pair at `mu=0`,

```math
\frac{n_c}{\alpha_D}
=\frac{B(T,E_g,r,n_b)}{v^2},
```

where

```math
\boxed{
B
=\frac{3n_bF_2(\Delta/k_BT)}
{\pi^2\alpha_{fs}Q(r,\Delta/k_BT)}
\frac{(k_BT)^3}{\hbar^3\omega}.
}
```

The earlier single-pass coefficient is

```math
C=\zeta B,
\qquad
\zeta=-\ln(1-A_{sp}).
```

Adding spectator hole states shifts `mu>0`, increasing `n_c` and reducing active-pair absorption, so under the same active-pair optical requirement

```math
\frac{n_c}{\alpha_D}\ge\frac{B}{v^2}.
```

Therefore

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

If electronic admissibility imposes

```math
v\le v_{adm}=\min(V_{hop},v_{spec}),
```

then

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

This is the resonant analogue of the earlier single-pass theorem.

---

## 7. The decisive no-go: response time alone does NOT restore universality

The preceding result still contains

```math
\Lambda_a.
```

TCMT by itself does not provide a material-independent upper bound on `Lambda_a`.

If a sequence of passive geometries could make

```math
\Lambda_a\to\infty
```

by concentrating more of the modal energy into an arbitrarily small active region, then

```math
\Sigma_c^{min}\to0
```

at fixed `A_0` and finite `tau_max` within the reduced TCMT description.

Therefore

```math
\boxed{
\text{finite temporal response alone does not restore a universal physical carrier-column lower bound.}
}
```

A universal photonic closure requires an additional electromagnetic resource limiting at least one of

```text
modal energy concentration;
absorber participation per physical thickness;
group/energy velocity;
resonator size;
material susceptibility;
number/density of resonances;
accepted optical bandwidth.
```

This is the central result of this step.

---

## 8. Simple ring/Fabry-type corollary

For a weak absorber segment of length `d` sampled once per optical circulation in a resonator of effective path length `L` and energy/group velocity `v_E`,

```math
2\gamma_i
\simeq
\alpha_Dd\frac{v_E}{L}.
```

Thus

```math
\boxed{\Lambda_a\simeq v_E/L.}
```

The temporal bound becomes

```math
\boxed{
\alpha_Dd
\gtrsim
g(A_0)\frac{L}{v_E\tau_{max}}.
}
```

and

```math
\boxed{
\Sigma_c
\gtrsim
\frac{B}{v_{adm}^2}
g(A_0)\frac{L}{v_E\tau_{max}}.
}
```

The path enhancement is therefore directly paid for by photon dwell time in this simple architecture.

For perfect absorption,

```math
\tau_{opt}\simeq\frac{L}{\alpha_Dd\,v_E}.
```

A smaller absorber optical depth requires proportionally longer cavity response.

This relation is elementary resonator physics and not novel.

---

## 9. Numerical scale: temporal response is a weak constraint at LWIR optical periods

For orientation only, take a simple resonator with one optical circulation length

```math
L=\lambda_0/n_b
```

and

```math
v_E\approx c/n_b.
```

Then

```math
L/v_E\approx\lambda_0/c.
```

At `lambda_0=10 um`,

```text
L/v_E = 33.36 fs.
```

For `A_0=0.90`,

```text
g(A_0)=0.68377.
```

Compared with the single-pass optical-depth requirement

```text
zeta=-ln(0.1)=2.30259,
```

the ratio of the resonant temporal lower bound to the original single-pass sheet bound is

```math
\boxed{
R_{res/sp}
=
\frac{g(A_0)}{\zeta}
\frac{L/v_E}{\tau_{max}}.
}
```

For the simple `L=lambda/n` example:

```text
tau_max = 0.1 ps  -> R = 9.91e-2
tau_max = 1 ps    -> R = 9.91e-3
tau_max = 10 ps   -> R = 9.91e-4
```

So even a 1-ps optical-response requirement still permits roughly a `100x` reduction of the single-pass carrier-column bound in this simple resonator model.

For a `v=1e6 m/s` active-pair witness whose single-pass column is `1.067e13 cm^-2`, the 1-ps ring-scale temporal bound would be only order

```text
1.06e11 cm^-2
```

before any spectator-band velocity ceiling is imposed.

This numerical illustration is architecture-specific, but it demonstrates an important scale separation: optical round-trip times at 10 um are tens of femtoseconds, much shorter than many detector-response targets. Finite response alone can therefore be a weak practical restriction on resonant path enhancement.

---

## 10. Broad-spectrum absorption changes the problem

A single high-Q resonance can evade physical absorber thickness only over a narrow optical band. If the founding detector comparison requires a **matched broad absorptance spectrum**, then many resonances or broadband impedance matching are required.

Passive absorber thickness-bandwidth tradeoffs are established prior art. In particular, Rozanov's 2000 causality/sum-rule result derives a lower bound on thickness versus absorption bandwidth for a metal-backed passive multilayer absorber:

```text
K. N. Rozanov,
"Ultimate thickness to bandwidth ratio of radar absorbers,"
IEEE Trans. Antennas Propag. 48, 1230-1234 (2000),
DOI 10.1109/8.884491.
```

Modern work has generalized or modified such sum rules under different boundary conditions. Therefore a broad passivity-based thickness-bandwidth theorem is not an available novelty claim.

However, Rozanov's original hypotheses do not automatically apply to every detector architecture, optical port topology, metasurface, or dispersive material. Experiment 10 must not silently import that bound as universal.

---

## 11. Direct photodetector prior art

Resonant-cavity-enhanced photodetectors have long been used specifically to decouple high quantum efficiency from absorber transit-time thickness.

Established work reports thin absorption regions with resonant field enhancement and tens-of-GHz bandwidths, including:

```text
S. Islam et al., "High-Speed Resonant Cavity Enhanced Schottky Photodiodes," Ultrafast Electronics and Optoelectronics (1997);
G. Ulu et al., "High-Speed Resonant Cavity Enhanced Photodiodes with Near-Unity Quantum Efficiency," 1999;
I. Kimukin, N. Biyikli, and E. Ozbay, "High-performance 1.55 um Resonant Cavity Enhanced Photodetector," OFC 2002.
```

The RCE-PD literature explicitly frames resonant enhancement as a route around the conventional absorber-thickness quantum-efficiency versus carrier-transit-bandwidth tradeoff.

Therefore neither

```text
cavities enhance absorption in thin photodetectors;
resonant enhancement trades optical linewidth/lifetime;
resonant photodetectors improve bandwidth-efficiency products
```

is a novelty claim.

---

## 12. What has actually been established

```text
DERIVED:
    exact one-port absorptance formula in the chosen TCMT convention;

DERIVED:
    for target peak absorptance A0 and envelope response tau_opt,
    the minimum internal loss is
    2 gamma_i = [1-sqrt(1-A0)]/tau_opt
    on the over-coupled branch;

DEFINED:
    Lambda_a = 2 gamma_i/(alpha_D d), the optical sampling-rate / participation resource;

DERIVED:
    Sigma_c >= (n_c/alpha_D) g(A0)/(Lambda_a tau_max);

DERIVED CONDITIONALLY:
    Sigma_c >= B g(A0)/(v_adm^2 Lambda_a tau_max)
    for the active Dirac pair plus the electronic admissibility ceiling;

DERIVED NO-GO:
    finite response alone is insufficient for a universal physical carrier-column floor because TCMT does not upper-bound Lambda_a;

DERIVED FOR SIMPLE CAVITY:
    Lambda_a ~ v_E/L and path enhancement is paid for by dwell time;

PRIOR-ART AUDIT:
    critical coupling, resonator linewidth/lifetime, RCE photodetectors, and passive absorber thickness-bandwidth bounds are established.
```

---

## 13. What is not established

```text
a universal upper bound on Lambda_a for arbitrary passive electromagnetic structures;
a general optical confinement bound using material susceptibility;
a detector-specific application of Rozanov/Bode-Fano bounds to the complete Experiment-10 optical boundary;
a finite-bandwidth theorem for arbitrary multi-resonant/metasurface absorbers;
a manuscript-level novelty claim.
```

---

## 14. Consequence for Experiment 10

The previous physical carrier-column theorem cannot be made universal merely by adding a finite response time.

The correct generalized structure is now

```math
\boxed{
\Sigma_c
\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}},
}
```

**conditional on an electromagnetic sampling-rate resource `Lambda_a`.**

Thus Experiment 10 now has two logically separate resource ceilings:

```text
electronic:
    v <= min(V_hop, v_spec);

photonic:
    Lambda_a <= Lambda_max
    or an equivalent bandwidth/thickness/confinement/passivity constraint.
```

Without both, no universal physical carrier-sheet floor follows.

---

## 15. Next action

The strongest next question is no longer another cavity calculation.

> Can `Lambda_a` be bounded from passivity, causality, material susceptibility, finite accepted optical bandwidth, and the complete external optical boundary strongly enough to yield a nontrivial detector-specific bound?

First audit known optical response bounds: Rozanov-type thickness-bandwidth sum rules, Bode-Fano matching limits, electromagnetic material-response bounds, and delay-bandwidth limits. If these already subsume the required resource, Experiment 10 should cite them rather than rederive them. If their hypotheses leave a detector-specific gap, formulate that gap precisely before doing more algebra.