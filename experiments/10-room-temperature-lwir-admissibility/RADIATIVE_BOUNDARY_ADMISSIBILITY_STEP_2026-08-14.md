# Experiment 10 — External Radiative Boundary Floor and Direct-Auger Admissibility Ratio

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **EXTERNAL OPTICAL-BOUNDARY INVARIANT DERIVED / TASK-ABSORPTANCE-ONLY MATCHING SHOWN INSUFFICIENT / PHOTON-RECYCLING DISTINCTION MADE EXPLICIT / DIRECT-AUGER-TO-RADIATIVE ACTIVATION PARITY DERIVED / NOVELTY NOT ESTABLISHED**

## 1. Question for this step

Previous steps reduced the direct Auger event rate of the controlled finite-gap massive-Dirac family to the schematic matched-area form

```math
G_A^{area}
\sim
\mathcal I_A
v^{-4}
\exp[-(\Delta+K_{th})/(k_BT)]
```

in the weak-screening, smooth-threshold-matrix limit, with

```math
\Delta=E_g/2,
```

and with the finite-asymmetry threshold approximately

```math
K_{th}\sim E_g\mathcal A_m^{-1/3}
```

for weak scalar particle-hole asymmetry.

This step asks:

> What is the unavoidable optical/radiative event floor to which this direct Auger rate should be compared when two detectors are required to have the same useful optical response?

The answer requires a correction to the original matching condition: matching only the useful scene absorptance is not enough.

---

## 2. Full external optical boundary is the correct object

Let `mu` denote a complete external optical channel, including frequency, direction, polarization, and whichever external port the mode belongs to.

Let

```math
\mathcal A_\mu
```

be the absorptance of the complete detector structure for incoming channel `mu`.

For a linear passive reciprocal structure, modal Kirchhoff reciprocity gives equality between absorption from an incoming mode and thermal emission into the corresponding reversed mode.

Therefore, for detector temperature `T_d`, the mean escaping thermal-photon rate is fixed by the complete mode-resolved external absorptance:

```math
\boxed{
\Phi_{em}^{ext}(T_d)
=\int_{\mathcal M_{ext}}d\mu\;
\mathcal A_\mu\,n_B(\omega_\mu,T_d)\,\Gamma_\mu.
}
```

Here `Gamma_mu dmu` is the incident-mode flux measure and

```math
n_B(\omega,T)=\frac{1}{e^{\hbar\omega/(k_BT)}-1}.
```

For an arbitrary external radiation field with modal occupation `n_mu^env`,

```math
\boxed{
\Phi_{abs}^{ext}
=\int_{\mathcal M_{ext}}d\mu\;
\mathcal A_\mu\,n_\mu^{env}\,\Gamma_\mu.
}
```

Thus, if two reciprocal detectors have the same

```text
complete external channel set;
mode-resolved absorptance A_mu over that set;
detector temperature;
and external modal occupation,
```

then both their external photon absorption rate and their escaping thermal-emission rate are identical, regardless of absorber chemistry.

This is the relevant **external optical-boundary invariance**.

It is a direct consequence of established Kirchhoff/detailed-balance physics, not a novelty claim.

---

## 3. Correction to the founding matching condition

The founding Gedanken experiment initially required equal

```text
useful absorptance spectrum;
accepted scene etendue;
optical environment.
```

That is not sufficient to fix the total external radiative exchange.

Counterexample:

```text
Detector A and Detector B have identical front-side absorptance over the accepted scene cone.
Detector A has a perfectly reflecting rear optical boundary.
Detector B has an additional transmitting/emitting substrate-side port.
```

The two detectors have identical task absorptance but different total external emissive mode counts and therefore different thermal-radiative exchange.

Hence the theorem-grade comparison must strengthen the optical matching condition to

```math
\boxed{
\mathcal A_\mu^{(A)}=\mathcal A_\mu^{(B)}
\quad\text{for every external optical reservoir/channel relevant to carrier exchange.}
}
```

Useful scene coupling remains a subset of this complete boundary condition.

---

## 4. Planar far-field form

For a planar detector exchanging propagating radiation with external half-space modes, use one polarization per term. The blackbody photon radiance per photon energy per polarization is

```math
L_{\gamma,p}(E,T)
=\frac{E^2}{h^3c^2}
\frac{1}{e^{E/(k_BT)}-1}.
```

Therefore

```math
\boxed{
\Phi_{em}^{ext}
=\sum_p\int dE\int d\Omega\,
\cos\theta\,
\mathcal A_p(E,\Omega)
\frac{E^2}{h^3c^2}
\frac{1}{e^{E/(k_BT_d)}-1}.
}
```

The absorbed background rate is the same integral with the external-mode occupation replacing the detector Planck occupation.

For a blackbody enclosure at the same temperature as the detector,

```math
\boxed{
\Phi_{abs}^{ext}=\Phi_{em}^{ext}\equiv\Phi_0.
}
```

The mean net optical pair flux vanishes, but the bidirectional stochastic event traffic does not:

```math
\boxed{
\mathcal T_{opt}^{eq}=2\Phi_0.
}
```

---

## 5. Ideal 10-um / 300-K radiative benchmark

For an ideal planar absorber with

```math
\mathcal A(E)=\Theta(E-E_g)
```

for both polarizations over one hemisphere,

```math
\boxed{
\Phi_0
=\frac{2\pi(k_BT)^3}{h^3c^2}
I_2(x_g),
}
```

where

```math
x_g=\frac{E_g}{k_BT},
```

and

```math
I_2(x_g)
=\int_{x_g}^{\infty}
\frac{x^2dx}{e^x-1}.
```

At

```text
T = 300 K
lambda_c = 10 um
x_g = 4.795922925
```

numerical evaluation gives

```text
I_2 = 0.286823524
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A cm^-2
```

and therefore the equilibrium two-way external optical event traffic is

```math
\boxed{
2\Phi_0=9.79555\times10^{17}\ \mathrm{cm^{-2}s^{-1}}.
}
```

This reproduces the previously estimated room-temperature 10-um ideal radiative dark-current scale.

At the cutoff itself,

```math
n_B(E_g,300\,\mathrm K)=0.0083322.
```

Since all accepted interband photons have `E >= E_g`, Bose bunching changes the variance-to-mean factor of any single fully accepted thermal mode by less than about `0.84%` relative to a Poisson event approximation. The exact mode statistics can be retained when required, but the mean-flux theorem above does not use a Poisson approximation.

---

## 6. Photon recycling: what is and is not invariant

The **internal radiative recombination event rate is not fixed** by external absorptance.

In the simplest recycling picture, let `p_esc` be the probability that an internally emitted photon escapes before being reabsorbed. Then schematically

```math
\Phi_{em}^{ext}=p_{esc}R_{rad}^{int}.
```

At fixed external thermal emission,

```math
R_{rad}^{int}=\Phi_{em}^{ext}/p_{esc}
```

can vary strongly as the escape probability changes.

This is why a bulk quantity such as

```math
Bn_i^2d
```

is not the invariant denominator required by the present detector comparison.

For the active-carrier number, an internal radiative recombination followed by reabsorption removes a pair and then recreates a pair. In the coarse-grained limit where photon-recycling flight/reabsorption times are short compared with the detector measurement timescale, those internal cycles do not constitute an irreversible carrier-number loss. The irreversible optical events are coupling to external optical reservoirs: external photon absorption and final photon escape/loss.

Therefore the present boundary theorem applies directly to the low-frequency/coarse-grained carrier-number problem.

At bandwidths comparable to photon dwell/recycling rates, the internal recombination-reabsorption sequence can contribute additional dynamical fluctuations. That is a separate finite-bandwidth correction and is not claimed to be fixed by external absorptance alone.

This distinction is consistent with explicit HgCdTe photon-transport calculations showing strong photon-recycling modification of the role of radiative recombination.

---

## 7. Replace the provisional Xi_nr by an event-traffic ratio

Define the total direct-Auger event traffic per detector area as

```math
\mathcal T_A
=G_A^{gen}+R_A^{rec}.
```

Define the irreversible external optical event traffic

```math
\mathcal T_{opt}
=\Phi_{abs}^{ext}+\Phi_{em}^{ext}.
```

Then define

```math
\boxed{
\Xi_A^{ext}
=\frac{\mathcal T_A}{\mathcal T_{opt}}.
}
```

This replaces the earlier ambiguous quantity that added a bulk radiative rate to a background rate.

At full thermal equilibrium,

```math
G_A^{gen}=R_A^{rec}=G_A,
```

and

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0,
```

so exactly

```math
\boxed{
\Xi_A^{ext}=\frac{G_A}{\Phi_0}.
}
```

A natural direct-channel admissibility criterion is therefore

```math
\boxed{
\Xi_A^{ext}\le1
\quad\Longleftrightarrow\quad
G_A^{area}\le\Phi_0.
}
```

Interpretation:

```text
the equilibrium direct-Auger event traffic contributes no more carrier-number transition traffic than the unavoidable external optical exchange imposed by the matched boundary.
```

This does not yet include SRH, phonon-assisted Auger, heavy-hole channels, contacts, or readout noise.

---

## 8. Exact radiative denominator versus direct-Auger activation

The preceding direct-Auger calculation gives, in the weak-screening smooth-matrix limit,

```math
G_A^{area}
\sim
\mathcal I_A
v^{-4}
\left(\frac{k_BT}{\Delta}\right)^3
\exp[-(\Delta+K_{th})/(k_BT)],
```

with interaction/screening factors left in `mathcal I_A`.

The exact ideal radiative denominator is

```math
\Phi_0
=\frac{2\pi(k_BT)^3}{h^3c^2}
I_2(2\Delta/k_BT).
```

Thus

```math
\boxed{
\Xi_A^{ext}
\propto
\mathcal P_A
v^{-4}
\frac{\exp[-(\Delta+K_{th})/(k_BT)]}
{I_2(2\Delta/k_BT)},
}
```

where `mathcal P_A` contains the remaining dimensional interaction, optical-depth, dielectric, spinor, exchange, and numerical factors.

For `E_g/k_BT >> 1`,

```math
I_2(x_g)
\simeq
(x_g^2+2x_g+2)e^{-x_g}.
```

At the present `x_g=4.7959`, this Boltzmann-tail approximation differs from the exact `I_2` by only about `0.34%`.

Using `x_g=2Delta/(k_BT)`, the exponential part of the ratio becomes

```math
\boxed{
\Xi_A^{ext}
\propto_{exp}
\exp[-(K_{th}-\Delta)/(k_BT)].
}
```

This produces a clean **activation-parity line**:

```math
\boxed{
K_{th}=\Delta=E_g/2.
}
```

If

```math
K_{th}>E_g/2,
```

then direct Auger is exponentially more suppressed with temperature than the unavoidable radiative boundary floor. If

```math
K_{th}<E_g/2,
```

it is exponentially less suppressed and must be defeated by algebraic/matrix-element factors instead.

This comparison concerns only the thermal exponential. It does not by itself guarantee `Xi_A <= 1` because the interaction prefactor can still be large.

---

## 9. Scalar-asymmetry model automatically lies on the favorable side of activation parity while both edge curvatures remain positive

For the scalar asymmetry model

```math
E_\pm=Dk^2\pm\sqrt{\Delta^2+(\hbar vk)^2},
```

the normalized asymmetry is

```math
\mathcal A_m=2|\beta|,
\qquad
\beta=D\Delta/(\hbar^2v^2).
```

Positive electron and hole edge curvatures require

```math
|\beta|<1/2.
```

On the strong-asymmetry boundary branch,

```math
q_{th}=|\beta|^{-1/2},
```

and

```math
\frac{K_{th}}{\Delta}
=\sqrt{1+|\beta|^{-1}}.
```

The minimum threshold in the entire positive-curvature model occurs as `|beta| -> 1/2`, giving

```math
\boxed{
K_{th}\ge\sqrt3\,\Delta
=0.866025\,E_g.
}
```

Therefore

```math
\boxed{
K_{th}-\Delta
\ge(\sqrt3-1)\Delta>0.
}
```

So every member of this controlled positive-curvature scalar-asymmetry family lies on the favorable side of the radiative activation-parity line.

At 10 um / 300 K,

```math
\frac{(\sqrt3-1)\Delta}{k_BT}
=1.7555,
```

so the weakest possible direct-Auger/radiative exponential factor within this reduced family is approximately

```math
\boxed{e^{-1.7555}=0.173.}
```

Again, this is an exponential comparison only, not a full rate bound.

---

## 10. Symmetry leverage relative to the radiative floor at the fixed target

For the exact scalar-asymmetry thresholds already derived at `10 um / 300 K`, define only the exponential ratio

```math
\mathcal E_{A/rad}
=\exp[-(K_{th}-E_g/2)/(k_BT)].
```

Then

```text
A_m       K_th/kBT      E_A/rad
0.40        5.873       3.10e-2
0.20        7.536       5.87e-3
0.10        9.470       8.49e-4
0.08476    10.000       4.99e-4
0.04       12.848       2.89e-5
0.02       16.273       9.42e-7
0.01       20.675       1.15e-8
```

Thus the previously chosen `10 k_BT` direct-threshold witness does more than make the absolute Auger tail small: relative to the unavoidable 300-K radiative boundary floor, it carries an additional thermal factor of about

```math
\boxed{5.0\times10^{-4}}
```

before the favorable `v^-4` factor and before unresolved interaction prefactors are applied.

---

## 11. What has actually been established

```text
DERIVED:
    complete external mode-resolved absorptance, not useful front-side absorptance alone, is the optical object that fixes thermal emission;

DERIVED:
    at fixed complete external optical boundary and detector temperature, external thermal-emission rate is chemistry-independent;

DERIVED:
    at fixed external environment and complete absorptance, background photon absorption is chemistry-independent;

CORRECTED:
    internal bulk radiative recombination rate is not the invariant comparator because photon recycling changes internal event count;

DEFINED:
    Xi_A^ext = total direct-Auger event traffic / irreversible external optical event traffic;

DERIVED AT EQUILIBRIUM:
    Xi_A^ext = G_A/Phi_0;

DERIVED:
    direct-Auger versus radiative thermal-exponent parity occurs at K_th = E_g/2;

DERIVED IN SCALAR-ASYMMETRY MODEL:
    positive electron/hole edge curvatures imply K_th >= sqrt(3) Delta > Delta, so the direct channel is always thermally steeper than the radiative boundary floor;

NUMERICAL BENCHMARK:
    ideal 10-um / 300-K hemispherical step absorber has Phi_0 = 4.89777e17 cm^-2 s^-1 and q Phi_0 = 0.078471 A/cm^2.
```

---

## 12. What has not been established

```text
Xi_A^ext <= 1 for any real material;
a universal bound on the direct-Auger interaction prefactor;
a full finite-bandwidth photon-recycling noise theorem;
heavy-hole / third-band Auger suppression;
phonon-assisted, Umklapp, disorder-assisted, or plasmon-assisted channels;
SRH suppression;
contact/readout noise;
that matching useful scene absorptance alone fixes the radiative floor;
novelty of the combined admissibility framework.
```

---

## 13. Prior-art boundary

The radiative ingredients are established:

```text
van Roosbroeck & Shockley, Phys. Rev. 94, 1558 (1954), DOI 10.1103/PhysRev.94.1558:
    thermal radiative recombination related to absorption by detailed balance;

U. Rau, Phys. Rev. B 76, 085303 (2007), DOI 10.1103/PhysRevB.76.085303:
    rigorous spectral/angular reciprocity between photovoltaic response and luminescent emission;

D. A. B. Miller et al., PNAS 114, 4336-4341 (2017), DOI 10.1073/pnas.1701606114:
    modal Kirchhoff laws for reciprocal thermal emitters;

A. Rogalski, M. Kopytko, P. Martyniuk, Appl. Opt. 57, D11-D19 (2018), DOI 10.1364/AO.57.000D11:
    explicit HgCdTe photon-transport calculations showing strong photon-recycling modification of radiative recombination influence.
```

Therefore neither detailed balance, Kirchhoff reciprocity, radiative dark-current formulas, nor photon recycling is available as a novelty claim.

Possible surviving contribution remains the detector-specific joint construction

```text
complete optical-boundary floor
+ exact finite-gap matched-absorptance carrier scaling
+ microscopic velocity resource
+ symmetry-controlled direct-Auger threshold
+ thresholded direct-Auger rate
-> explicit nonradiative-to-unavoidable-optical admissibility ratio.
```

Novelty remains unestablished.

---

## 14. Next question

The radiative side is now fixed at the boundary level. The direct two-band Auger side is also factored as far as useful without a full multiband model.

The next intrinsic spoiler is therefore not another detailed-balance manipulation. It is the first **extra-band escape from the two-band Auger protection**:

> Add the minimal third band, especially a heavy-hole-like reservoir, and determine whether an additional Auger channel can remain open even when the active conduction/valence pair has large `v` and excellent particle-hole symmetry. Can one derive an energy/mass/velocity separation condition that preserves `Xi_A^ext <= 1` parametrically?

Do not rank materials yet. Begin with exact kinematics of the minimal three-band model before inserting empirical lifetimes.
