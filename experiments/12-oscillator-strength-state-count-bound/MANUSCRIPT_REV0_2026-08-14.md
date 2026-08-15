# Thermal population cost of direct interband optical spectral weight

**Anonymous manuscript — Rev0 — 2026-08-14**

## Abstract

Strong low-energy optical absorption and low equilibrium carrier population are competing requirements in interband photodetectors, but their relation is usually evaluated only after a particular density of states, band structure, and recombination model have been chosen. Here we derive a finite-temperature inequality that removes the density-of-states model from this first comparison. For exact independent-quasiparticle states below and above the chemical potential, we show that the direct cross-chemical-potential optical spectral weight in any chosen frequency window is bounded by a thermally weighted per-state velocity-matrix resource. If the selected optical matrix strength carried by any single upper or lower state is at most \(v_{*,\mathcal B}^2\), then

\[
 n_e+n_h\ge
 \frac{2}{\pi e^2v_{*,\mathcal B}^2}
 \int_{\mathcal B}
 \frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
 {\exp[\hbar\omega/(2k_BT)]-1}\,d\omega .
\]

For an intrinsic absorber, the right-hand side divided by two bounds the equilibrium electron or hole density separately. The thermal kernel approaches \(2k_BT\) as the transition energy tends to zero, so a fixed amount of low-energy direct interband spectral weight cannot coexist with a vanishing thermal quasiparticle population unless the microscopic optical velocity resource also changes. The inequality is exact for mirror-symmetric parabolic conduction and valence bands with equal masses and remains quantitatively tight in dispersive Dirac models: it recovers one half of the exact thermal population for neutral two-dimensional massless Dirac fermions, two thirds in three dimensions, and \(0.7947\) for a three-dimensional massive-Dirac model at a 10-µm, 300-K gap. The result is a necessary equilibrium population constraint, not a universal dark-current or detectivity limit; neutral excitons, indirect absorption, many-body spectral functions, and carrier-transport kinetics lie outside its present scope.

---

## I. Introduction

A photon detector requires two properties that often pull in opposite directions. The electronic system must couple strongly enough to the optical field to absorb useful radiation, while equilibrium electronic excitations must be sufficiently sparse that dark generation, occupation fluctuations, and transport do not overwhelm the signal. In infrared detectors this competition is especially severe because the useful photon energy can be only a few \(k_BT\).

The standard detector-level treatment begins after a material model has already supplied an absorption coefficient and a thermal generation rate. In this language, the classic infrared-detector material criterion compares useful absorption with thermal generation through quantities such as \(\alpha/G_{\rm th}\) [1]. That construction is operationally valuable, but it does not ask a more primitive question: **does the existence of a specified amount of low-energy interband oscillator strength itself require a minimum equilibrium population of the electronic states that carry it?**

Several established bodies of theory bear directly on this question without answering it in this form. Semiconductor phase-space filling computes how specified carrier occupations bleach optical transitions [2,3]. Optical \(f\)-sum rules constrain frequency-integrated conductivity by all-electron or kinetic quantities [4]. Quantum-geometric optical sum rules connect other conductivity moments to Wannier spread and quantum metric [5]. In semiconductor lasers, light and more symmetric conduction and valence bands have long been recognized as a route to reducing the injected carrier density required for transparency and gain [6]. These results all motivate the present question, but they do not provide a density-of-states-independent inverse bound from surviving equilibrium interband spectral weight to thermally excited carrier population.

Here we derive such an inequality for independent quasiparticles. The central observation is elementary at the level of a single transition: for two Fermi-occupied states on opposite sides of the chemical potential, a large absorption population difference cannot be maintained arbitrarily close to the chemical potential without thermally occupying the upper state or emptying the lower state. The nontrivial global step is to show that an electronic state cannot evade this cost by contributing oscillator strength to arbitrarily many transitions. The total selected squared velocity-matrix strength attached to each upper or lower state provides the necessary microscopic resource constraint.

The resulting theorem has four useful properties. First, it is formulated for an arbitrary optical-frequency window and does not require a globally bounded continuum velocity. Second, it does not assume a density of states, effective mass, Bloch momentum, equal band degeneracy, or one-to-one transition counting. Third, it survives static one-particle disorder when stated in exact eigenstates. Fourth, it has nontrivial equality and near-equality realizations in familiar semiconductor models.

The result is intentionally narrower than a detector-performance theorem. It bounds equilibrium quasiparticle population. Localized states can satisfy the optical inequality while producing little dc dark current, and a depleted photovoltaic detector can have fast collection despite a long recombination lifetime. Neutral excitons can carry low-energy optical strength without being free charge at all. These distinctions are part of the result's scope rather than corrections to be hidden after the fact.

---

## II. Direct cross-μ optical transitions

Consider an independent single-particle Hamiltonian in equilibrium at temperature \(T\) and chemical potential \(\mu\). Let \(v\) label exact one-particle states below the chemical potential and \(c\) exact states above it,

\[
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0 .
\tag{1}
\]

No translational symmetry is assumed. Spin, valley, orbital, finite-volume, and static-disorder multiplicities are included explicitly in the state labels.

Define

\[
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
\qquad
D_{cv}=f(E_v)-f(E_c),
\tag{2}
\]

where

\[
f(E)=\frac{1}{e^{(E-\mu)/(k_BT)}+1}.
\tag{3}
\]

Here \(p_c\) is the thermal occupation of an upper state and \(h_v\) is the thermal hole occupation of a lower state.

For one Cartesian polarization \(i\), let

\[
v_{cv}=\langle c|\hat v_i|v\rangle.
\tag{4}
\]

We define \(\sigma_1^{\rm cross}(\omega)\) to be only the positive-frequency Kubo-Greenwood conductivity from transitions crossing \(\mu\),

\[
\sigma_1^{\rm cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
\tag{5}
\]

This restriction matters at finite temperature. Optical transitions whose initial and final states both lie below \(\mu\), or both above it, are not part of the stronger half-transition-energy bound derived below. For an ordinary intrinsic direct-gap semiconductor near its absorption edge, Eq. (5) is the relevant band-to-band contribution.

---

## III. A pointwise Fermi lemma

The thermal population cost begins with a single crossing transition.

Define

\[
a=e^{-(E_c-\mu)/(k_BT)},
\qquad
b=e^{-(\mu-E_v)/(k_BT)}.
\tag{6}
\]

Then

\[
ab=e^{-E_{cv}/(k_BT)}\equiv z,
\tag{7}
\]

and direct algebra gives

\[
D_{cv}=\frac{1-z}{(1+a)(1+b)},
\tag{8}
\]

\[
p_c+h_v=\frac{a+b+2z}{(1+a)(1+b)}.
\tag{9}
\]

At fixed transition energy, \(ab=z\), and the arithmetic-geometric mean inequality gives

\[
a+b\ge 2\sqrt z.
\tag{10}
\]

Substituting Eq. (10) into Eq. (9) yields

\[
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v .
}
\tag{11}
\]

Equality holds if and only if

\[
E_c-\mu=\mu-E_v=\frac{E_{cv}}{2}.
\tag{12}
\]

Equation (11) is the local origin of the theorem. For a transition of fixed energy, the least thermally costly placement of the two states is mirror symmetry about the chemical potential. The denominator has a Bose-like form, but no bosonic occupation has been assumed: it results from optimizing two Fermi occupations constrained to opposite sides of \(\mu\).

---

## IV. Arbitrary-window spectral-weight theorem

### A. Selected transition graph

Let \(\mathcal B\) be any measurable set of positive angular frequencies. It may be contiguous or disjoint. Define the selected transition set

\[
\mathcal T_{\mathcal B}
=
\left\{(c,v):\frac{E_{cv}}{\hbar}\in\mathcal B\right\}.
\tag{13}
\]

For each upper state define the selected row velocity strength

\[
R_c(\mathcal B)
=
\sum_{v:(c,v)\in\mathcal T_{\mathcal B}}
|v_{cv}|^2,
\tag{14}
\]

and for each lower state

\[
C_v(\mathcal B)
=
\sum_{c:(c,v)\in\mathcal T_{\mathcal B}}
|v_{cv}|^2.
\tag{15}
\]

The thermally weighted selected velocity-strength density is

\[
\mathcal R_{\mathcal B}(T)
=
\frac{1}{V}
\left[
\sum_c p_c R_c(\mathcal B)
+
\sum_v h_v C_v(\mathcal B)
\right].
\tag{16}
\]

This quantity contains no maximum-velocity approximation.

### B. Thermal optical velocity-strength inequality

Multiply Eq. (11) by \(|v_{cv}|^2\), sum only over \(\mathcal T_{\mathcal B}\), and use Eq. (5). Defining

\[
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1},
\tag{17}
\]

we obtain

\[
\boxed{
\mathcal R_{\mathcal B}(T)
\ge
\frac{2}{\pi e^2}
\int_{\mathcal B}
K_T(\hbar\omega)
\sigma_1^{\rm cross}(\omega)
\,d\omega .
}
\tag{18}
\]

Equation (18) is the most assumption-light form of the result. It states that thermally weighted velocity strength carried by upper-state electrons and lower-state holes must be at least as large as a finite-temperature optical spectral-weight functional.

### C. Carrier-population corollary

Define the largest selected velocity strength attached to any one state,

\[
\boxed{
v_{*,\mathcal B}^2
=
\max\left[
\sup_c R_c(\mathcal B),
\sup_v C_v(\mathcal B)
\right].
}
\tag{19}
\]

The thermal electron and hole densities are

\[
n_e=\frac{1}{V}\sum_c p_c,
\qquad
n_h=\frac{1}{V}\sum_v h_v.
\tag{20}
\]

By construction,

\[
\mathcal R_{\mathcal B}(T)
\le
v_{*,\mathcal B}^2(n_e+n_h).
\tag{21}
\]

Combining Eqs. (18) and (21) gives

\[
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2v_{*,\mathcal B}^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega .
}
\tag{22}
\]

For an intrinsic charge-neutral absorber, \(n_e=n_h\equiv n_{\rm th}\),

\[
\boxed{
n_{\rm th}
\ge
\frac{1}{\pi e^2v_{*,\mathcal B}^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega .
}
\tag{23}
\]

The windowed form is important. A continuum velocity operator can be unbounded at arbitrarily high energy, but Eq. (23) requires only the velocity-matrix resource inside the useful optical window.

---

## V. Microscopic interpretation of the velocity resource

The quantity \(v_{*,\mathcal B}\) is not a universal speed limit or a fitted detector parameter. It is the selected squared optical velocity strength that one electronic state can contribute.

Completeness gives, for any upper state,

\[
R_c(\mathcal B)
\le
\sum_n|\langle c|\hat v_i|n\rangle|^2
=
\langle c|\hat v_i^2|c\rangle,
\tag{24}
\]

and analogously

\[
C_v(\mathcal B)
\le
\langle v|\hat v_i^2|v\rangle.
\tag{25}
\]

Thus \(v_{*,\mathcal B}^2\) can be bounded by the largest relevant one-body velocity second moment. In an orthonormal localized/Wannier Hamiltonian

\[
H(\mathbf k)=\sum_R H_R e^{i\mathbf k\cdot R},
\tag{26}
\]

the velocity operator satisfies the further conditional lattice bound

\[
\|\hat v_i\|
\le
\frac{1}{\hbar}
\sum_R |R_i|\|H_R\|,
\tag{27}
\]

so the ability to evade Eq. (23) by increasing optical velocity ultimately consumes an ultraviolet hopping-range/strength resource.

The ordinary Thomas-Reiche-Kuhn or effective-mass sum rule does not provide a positive, material-independent numerical replacement for \(v_{*,\mathcal B}\) in a generic multiband crystal: remote-band contributions enter effective-mass identities with signs and energy denominators. Equation (23) should therefore be understood as a resource-conditioned inequality, not a chemistry-independent number.

---

## VI. Low-energy limit

The thermal kernel in Eq. (17) has the expansion

\[
K_T(E)
=2k_BT-\frac{E}{2}+O\!\left(\frac{E^2}{k_BT}\right).
\tag{28}
\]

Therefore, if a useful optical window is pushed toward zero transition energy while its integrated cross-\(\mu\) spectral weight and \(v_{*,\mathcal B}\) remain fixed,

\[
\boxed{
n_e+n_h
\gtrsim
\frac{4k_BT}{\pi e^2v_{*,\mathcal B}^2}
\int_{\mathcal B}
\sigma_1^{\rm cross}(\omega)d\omega .
}
\tag{29}
\]

For an intrinsic absorber,

\[
\boxed{
n_{\rm th}
\gtrsim
\frac{2k_BT}{\pi e^2v_{*,\mathcal B}^2}
\int_{\mathcal B}
\sigma_1^{\rm cross}(\omega)d\omega .
}
\tag{30}
\]

This is the main qualitative consequence: within the stated quasiparticle class, reducing the useful direct-interband photon energy cannot by itself make the equilibrium charge population vanish if a finite amount of intrinsic optical spectral weight must be retained. The escape variable is explicit: the optical velocity strength available per thermally occupiable state must also increase, or the detector must leave the theorem class.

---

## VII. Equality and validation

### A. Flat resonant manifolds

The simplest equality construction contains equal-dimensional conduction and valence manifolds separated by a single transition energy, with the chemical potential at their midpoint. If every nonzero singular value of the interband velocity block equals \(v_{*,\mathcal B}\), all inequalities above saturate. This construction motivated the theorem but is not required by it.

### B. Three-dimensional parabolic direct bands

Consider

\[
E_c(k)=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
\qquad
E_v(k)=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h},
\tag{31}
\]

with vertical direct transitions and a constant one-to-one matrix element \(|v_{cv}|=v_0\). Then \(v_{*,\mathcal B}=v_0\) for a window containing the direct continuum.

When \(m_e=m_h\), intrinsic neutrality gives \(\mu=0\), and every vertical transition obeys

\[
E_c(k)-\mu=\mu-E_v(k).
\tag{32}
\]

Consequently both the pointwise Fermi lemma and the selected velocity-strength ceiling saturate for every \(k\), giving

\[
\boxed{
(n_e+n_h)_{\rm bound}
=(n_e+n_h)_{\rm exact}
}
\tag{33}
\]

at all temperatures.

For unequal masses in the nondegenerate limit,

\[
\boxed{
\frac{(n_e+n_h)_{\rm bound}}
{(n_e+n_h)_{\rm exact}}
=
\left[
\frac{4m_em_h}{(m_e+m_h)^2}
\right]^{3/4}
\le1 .
}
\tag{34}
\]

Thus the theorem's looseness is controlled directly by electron-hole asymmetry in this textbook model. At \(E_g/k_BT=4.7959\), corresponding to a 10-µm transition at 300 K, exact Fermi-Dirac evaluation gives ratios \(0.9161\), \(0.6455\), and \(0.4379\) for \(m_h/m_e=2,5,\) and \(10\), respectively, while the equal-mass case remains exactly unity.

### C. Dirac systems

The inequality also remains nontrivial away from parabolic bands. For neutral two-dimensional massless Dirac quasiparticles, using the exact finite-temperature interband sheet conductivity gives

\[
n_e^{\rm bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\tag{35}
\]

while the exact thermal electron density is

\[
n_e^{\rm exact}
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\tag{36}
\]

so the bound recovers one half of the exact population. The corresponding ratio is \(2/3\) for an isotropic three-dimensional massless Dirac cone.

For the finite-gap three-dimensional massive-Dirac dispersion

\[
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\tag{37}
\]

the exact finite-temperature conductivity and carrier density can both be evaluated directly [7]. At

\[
\frac{2\Delta}{k_BT}=4.7959,
\tag{38}
\]

the theorem gives

\[
\boxed{
\frac{(n_e+n_h)_{\rm bound}}
{(n_e+n_h)_{\rm exact}}
=0.794684 .
}
\tag{39}
\]

The ratio rises toward unity as \(\Delta/k_BT\) increases, consistent with the fact that the thermally relevant upper and lower states become increasingly concentrated around mirror-symmetric band edges.

| Model | Bound / exact thermal population |
|---|---:|
| 2-D neutral massless Dirac | 0.5000 |
| 3-D massless Dirac | 0.6667 |
| 3-D massive Dirac, \(\Delta/k_BT=2.398\) | 0.7947 |
| 3-D parabolic, \(m_h/m_e=2\), \(E_g/k_BT=4.796\) | 0.9161 |
| 3-D parabolic, \(m_h=m_e\) | 1.0000 |

These examples show that Eq. (22) is neither tied to a particular density of states nor generically parametrically loose.

---

## VIII. Relation to established optical and detector constraints

### A. Phase-space filling

Semiconductor phase-space-filling theory evaluates the reduction of absorption and oscillator strength caused by specified electron and hole occupations [2,3]. Equation (22) is naturally viewed as an inverse statement with an additional microscopic resource constraint: if a finite cross-\(\mu\) spectral weight survives at equilibrium, then the total thermal occupation cannot be made arbitrarily small because the squared velocity strength available from any one state is finite. The ingredients are familiar; the constraint is the global inverse composition.

### B. Optical sum rules

The conventional \(f\)-sum and its generalizations constrain conductivity moments through the density of all charged particles, kinetic energy, or derivatives of the Hamiltonian [4]. Quantum-geometric sums use other frequency moments to access Wannier spread or quantum metric [5]. Equation (22) instead weights only cross-\(\mu\) optical transitions by

\[
\frac{E}{e^{E/(2k_BT)}-1}
\tag{40}
\]

and constrains the density of thermally excited electrons and holes. It is therefore complementary to, rather than a replacement for, standard optical sum rules.

### C. Low-carrier optical band engineering

The favorable role of light and symmetric electron-hole bands is established semiconductor-optics physics. Yablonovitch and Kane showed that lowering the heavy valence-band mass can reduce the injected carrier density and threshold current required for semiconductor lasing [6]. Equation (34) recovers the same qualitative direction in an equilibrium absorption problem, but the band-design intuition itself is not a novelty claim here.

### D. Infrared detector material figures of merit

The classic infrared criterion \(\alpha/G_{\rm th}\) directly compares optical absorption with thermal generation [1]. Equation (22) addresses an upstream and weaker question: before specifying a recombination mechanism or generation lifetime, how small can the equilibrium population of the electronic states carrying the useful direct optical spectral weight be? The present theorem does not determine \(G_{\rm th}\) from \(n_{\rm th}\). In particular, no universal relation \(G_{\rm th}\ge n_{\rm th}/\tau_{\rm response}\) exists because recombination lifetime and collection/response time need not coincide.

---

## IX. Infrared-detector illustration

To give Eq. (23) a detector-scale interpretation without turning it into an external-optics theorem, consider a weak-loss homogeneous single-pass absorber with background refractive index \(n_b\), for which

\[
\alpha(\omega)\simeq
\frac{\sigma_1^{\rm cross}(\omega)}{n_b\epsilon_0c}.
\tag{41}
\]

Let a 300-K material have a 10-µm absorption edge and require \(A\ge0.90\) over the frequency interval \(\mathcal B=[\omega_g,1.1\omega_g]\). With Beer-Lambert optical depth \(	au=\alpha d\), the condition implies \(	au\ge-\ln0.1\) throughout the interval. Exact integration of the thermal kernel then gives the illustrative lower bounds

| \(v_{*,\mathcal B}\) (m/s) | Minimum intrinsic electron column (cm\(^{-2}\)) |
|---:|---:|
| \(5.0\times10^5\) | \(3.66\times10^{12}\) |
| \(1.0\times10^6\) | \(9.15\times10^{11}\) |
| \(1.07\times10^6\) | \(7.99\times10^{11}\) |
| \(2.0\times10^6\) | \(2.29\times10^{11}\) |
| \(3.0\times10^6\) | \(1.02\times10^{11}\) |

The example should be read only as a material-dominant single-pass corollary. Resonant cavities, antennas, slow-light structures, and other photonic path-enhancement mechanisms introduce additional electromagnetic resources and can reduce the physical material volume required for a specified external absorptance.

---

## X. Scope and escape routes

Equation (22) is deliberately not a universal theorem for all photon detectors.

**Neutral many-body excitations.** A bound exciton can carry strong optical oscillator strength below the free electron-hole continuum while remaining charge neutral. A detector using such a state requires a separate dissociation step. Excitonic absorption therefore lies outside a theorem stated in terms of free independent-quasiparticle population.

**Indirect absorption.** Phonon-assisted optical processes cannot in general be represented by the direct one-body velocity graph used in Eq. (5). They require a separate treatment of the joint electronic-lattice transition amplitude.

**Interaction-generated broadening.** Static one-body disorder is allowed if exact eigenstates are used. A phenomenological lifetime broadening of clean transitions is not equivalent to such a static Hamiltonian; a genuine many-body spectral-function formulation would be required.

**Localization and dark current.** Localized one-particle states still obey the population theorem because the proof does not require mobility. They may nevertheless couple only weakly to terminal transport. Equation (22) is therefore a necessary material-state-count condition, not a lower bound on dc dark current.

**Finite-bandwidth noise.** A related inequality can be written for the sum of independent Fermi occupation variances, but converting integrated equilibrium variance into noise in a specified readout band requires kinetics. No universal finite-bandwidth noise floor follows from Eq. (22) alone.

**External photonic enhancement.** The theorem constrains intrinsic electronic conductivity. Translating it to external absorptance requires an optical architecture. Arbitrary passive path enhancement cannot be eliminated without specifying additional photonic resources.

These escape routes are physically useful: they identify how a detector architecture must leave the independent direct-interband quasiparticle class if it is to evade the population cost in Eq. (22).

---

## XI. Conclusion

We have derived a finite-temperature inequality relating direct cross-chemical-potential optical spectral weight to equilibrium electron-hole excitation population in independent-quasiparticle absorbers. The result can be written as the hierarchy

\[
\boxed{
\frac{2}{\pi e^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}d\omega
\le
\mathcal R_{\mathcal B}(T)
\le
v_{*,\mathcal B}^2(n_e+n_h).
}
\tag{42}
\]

It is independent of an assumed density of states and remains valid for arbitrary dispersive multiband state reuse and static one-particle disorder. The bound is exactly saturated by mirror-symmetric equal-mass parabolic bands and remains quantitatively substantial in mass-asymmetric parabolic and Dirac models.

The low-energy limit gives the clearest physical statement: at fixed microscopic velocity-strength resource, finite direct optical spectral weight near zero transition energy carries a finite thermal quasiparticle-population cost proportional to \(T\). Lowering the band-to-band photon energy therefore does not, by itself, provide a route to simultaneously strong direct absorption and vanishing equilibrium charge population.

This is a necessary equilibrium population constraint, not a universal detector-performance limit. Dark generation, collection, finite-bandwidth noise, neutral excitons, indirect transitions, and photonic enhancement require additional physics. The value of the inequality is instead to isolate a model-independent electronic resource tradeoff that is normally hidden once a specific density of states and recombination mechanism have already been assumed.

---

## References

[1] J. Piotrowski and W. Gawron, “Ultimate performance of infrared photodetectors and figure of merit of detector material,” *Infrared Physics & Technology* **38**, 63–68 (1997). DOI: `10.1016/S1350-4495(96)00030-8`.

[2] D. Huang, J.-I. Chyi, and H. Morkoç, “Carrier effects on the excitonic absorption in GaAs quantum-well structures: Phase-space filling,” *Physical Review B* **42**, 5147–5153 (1990). DOI: `10.1103/PhysRevB.42.5147`.

[3] N. H. Kwong, G. Rupper, and R. Binder, “Self-consistent T-matrix theory of semiconductor light-absorption and luminescence,” *Physical Review B* **79**, 155205 (2009). DOI: `10.1103/PhysRevB.79.155205`.

[4] H. Watanabe and M. Oshikawa, “Generalized f-sum rules and Kohn formulas on nonlinear conductivities,” *Physical Review B* **102**, 165137 (2020). DOI: `10.1103/PhysRevB.102.165137`.

[5] L. F. Cárdenas-Castillo, S. Zhang, F. L. Freire Jr., D. Kochan, and W. Chen, “Detecting the spread of valence-band Wannier functions by optical sum rules,” *Physical Review B* **110**, 075203 (2024). DOI: `10.1103/PhysRevB.110.075203`.

[6] E. Yablonovitch and E. O. Kane, “Reduction of lasing threshold current density by the lowering of valence band effective mass,” *Journal of Lightwave Technology* **4**, 504–506 (1986). DOI: `10.1109/JLT.1986.1074751`.

[7] C. J. Tabert, J. P. Carbotte, and E. J. Nicol, “Optical and transport properties in three-dimensional Dirac and Weyl semimetals,” *Physical Review B* **93**, 085426 (2016); Erratum *Physical Review B* **94**, 039901 (2016). DOI: `10.1103/PhysRevB.93.085426`.

[8] V. P. Gusynin, S. G. Sharapov, and J. P. Carbotte, “Sum rules for the optical and Hall conductivity in graphene,” *Physical Review B* **75**, 165407 (2007). DOI: `10.1103/PhysRevB.75.165407`.

---

## Rev0 internal scope note

This draft intentionally avoids claiming:

```text
first-ever / universal photodetector theorem;
dark-current lower bound;
D* lower/upper bound;
finite-bandwidth noise floor;
applicability to excitonic or indirect absorbers.
```

The next step is an extreme adversarial manuscript review. Any theorem normalization, prior-art collision, or overclaim found there must be corrected before considering submission formatting.
