# Thermal population cost of direct interband optical spectral weight

**Anonymous manuscript — Rev2 — 2026-08-14**

## Abstract

Low thermal carrier population and strong low-energy optical coupling are competing requirements in direct interband absorbers, but their relation is usually evaluated only after a density of states and recombination model have been chosen. We derive a finite-temperature inequality that precedes those model choices. For exact independent-quasiparticle states below and above the chemical potential, the direct cross-chemical-potential conductivity in any optical-frequency window \(\mathcal B\) obeys

\[
\frac{2}{\pi e^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega
\le
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h),
\]

where \(\mathcal R_{\mathcal B}\) is the thermally occupied optical-velocity strength and \(u_{\mathcal B}\) is a basis-invariant optical-velocity resource defined independently within each degenerate energy eigenspace. The kernel approaches \(2k_BT\) at low photon energy. Thus fixed low-energy **integrated** direct spectral weight cannot coexist with vanishing thermal quasiparticle population at fixed \(u_{\mathcal B}\). Mirror-symmetric equal-mass parabolic bands exactly saturate the bound at all temperatures. The bound recovers one half of the exact thermal population in neutral two-dimensional massless Dirac systems, two thirds in three dimensions, and \(0.7947\) for a three-dimensional massive-Dirac model at a 10-µm, 300-K gap. The result is a necessary equilibrium quasiparticle-population constraint, not a universal dark-current or detectivity limit; neutral excitons, indirect absorption, many-body spectral functions, transport kinetics, and unconstrained photonic path enhancement require additional physics.

---

## I. Introduction

An interband photodetector requires electronic states that couple strongly to the optical field while remaining sparsely thermally populated. In the infrared, where the useful photon energy can be only a few \(k_BT\), this tension is especially severe. Conventional detector theory usually evaluates it only after a material-specific model has supplied an absorption coefficient, carrier density, recombination rate, and transport law. A classic example is the infrared-detector material criterion based on useful absorption relative to thermal generation, such as \(\alpha/G_{\rm th}\) [1].

A more primitive question can be asked before a density of states or recombination mechanism is selected:

> If an equilibrium material retains a specified amount of low-energy direct interband optical spectral weight, how small can the thermal population of the electronic states carrying that response be?

Several established theories constrain pieces of this problem. Semiconductor phase-space filling calculates how electron and hole occupations bleach optical transitions [2,3]. Optical \(f\)-sum rules constrain conductivity moments through all-electron or kinetic quantities [4]. Quantum-geometric optical sums relate other response moments to Wannier spread and quantum metric [5]. In semiconductor lasers, reducing valence-band mass and electron-hole density-of-states asymmetry has long been recognized as a route to reducing the injected carrier density required for transparency and gain [6].

The present question is an inverse equilibrium problem. We ask whether a finite surviving cross-Fermi optical spectral weight itself enforces a minimum thermal electron-hole excitation population when the optical velocity strength available from any one degenerate energy eigenspace is finite.

The derivation has two steps. First, an exact Fermi-Dirac inequality relates the population difference of one transition crossing the chemical potential to the thermal occupation of its upper state and the thermal hole occupation of its lower state. Second, a state cannot evade that local cost by coupling to arbitrarily many optical partners: all selected transitions leaving a fixed degenerate energy shell share a finite velocity-matrix resource. Kubo-Greenwood converts the resulting statewise inequality into a spectral-response bound.

The theorem is formulated for any measurable positive-frequency window. It therefore does not require a globally bounded continuum velocity. It does not assume parabolic or Dirac dispersion, equal band degeneracy, Bloch momentum, translational invariance, or one-to-one transition counting. Static one-body disorder is allowed if exact eigenstates are used.

The scope is deliberately narrower than a detector-performance theorem. The result constrains **integrated optical spectral weight**, not an arbitrarily high peak response in a vanishingly narrow line. Equilibrium quasiparticle population is also not identical to dark current: localization can suppress transport, and collection time need not equal recombination lifetime. Neutral excitons can carry low-energy optical oscillator strength without being free charge. The theorem is therefore a necessary electronic-state-count constraint for direct independent-quasiparticle absorbers, not a universal limit on \(D^*\), dark current, or finite-bandwidth noise.

---

## II. Cross-\(\mu\) optical transitions

Consider an equilibrium independent-particle Hamiltonian in finite volume \(V\) with chemical potential \(\mu\). Let \(v\) label exact one-particle eigenstates below \(\mu\) and \(c\) exact states above it,

\[
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0.
\tag{1}
\]

Spin, valley, orbital, finite-volume, and static-disorder multiplicities are included in the state labels. The thermodynamic limit may be taken after the finite-volume inequalities are established.

Define

\[
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
\qquad
D_{cv}=f(E_v)-f(E_c),
\tag{2}
\]

with

\[
f(E)=\frac{1}{e^{(E-\mu)/(k_BT)}+1}.
\tag{3}
\]

For one physical current/velocity polarization \(i\), write

\[
v_{cv}=\langle c|\hat v_i|v\rangle.
\tag{4}
\]

The direct positive-frequency conductivity contributed only by transitions crossing \(\mu\) is

\[
\boxed{
\sigma_1^{\rm cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
}
\tag{5}
\]

Thermally activated transitions whose initial and final states both lie below \(\mu\), or both above it, obey a weaker detailed-balance relation and are not included in Eq. (5).

### A. Pointwise Fermi lemma

Set

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

and

\[
D_{cv}=\frac{1-z}{(1+a)(1+b)},
\qquad
p_c+h_v=\frac{a+b+2z}{(1+a)(1+b)}.
\tag{8}
\]

At fixed transition energy \(ab=z\), the arithmetic-geometric mean inequality gives \(a+b\ge2\sqrt{ab}\). Hence

\[
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v .
}
\tag{9}
\]

Equality holds if and only if

\[
E_c-\mu=\mu-E_v=\frac{E_{cv}}{2}.
\tag{10}
\]

For a transition of fixed energy, mirror placement about the chemical potential is therefore the least thermally costly configuration. The Bose-like denominator in Eq. (9) is not an assumed boson occupation; it emerges from optimizing two Fermi occupations.

---

## III. Arbitrary-window theorem hierarchy

Let \(\mathcal B\) be any measurable set of positive angular frequencies and define

\[
\mathcal T_{\mathcal B}
=
\{(c,v):E_{cv}/\hbar\in\mathcal B\}.
\tag{11}
\]

For a chosen exact eigenbasis, define selected row and column strengths

\[
R_c(\mathcal B)
=
\sum_{v:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2,
\tag{12}
\]

\[
C_v(\mathcal B)
=
\sum_{c:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2.
\tag{13}
\]

Although individual row or column strengths can redistribute under a basis rotation inside an exactly degenerate eigenspace, the thermally weighted sum

\[
\boxed{
\mathcal R_{\mathcal B}(T)
=
\frac{1}{V}
\left[
\sum_c p_cR_c(\mathcal B)
+
\sum_v h_vC_v(\mathcal B)
\right]
}
\tag{14}
\]

is invariant because all states within a degenerate eigenspace have the same Fermi occupation.

Define

\[
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
\tag{15}
\]

Multiplying Eq. (9) by \(|v_{cv}|^2\), summing over \(\mathcal T_{\mathcal B}\), and using Eq. (5) gives the first result.

### Theorem 1: thermal optical velocity-strength inequality

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
\tag{16}
\]

Equation (16) contains no maximum-velocity or density-of-states approximation.

### A. Basis-invariant shell resource

Let \(P_\epsilon\) project onto the complete exact eigenspace of one-particle energy \(\epsilon\). For an upper energy \(\epsilon_c>\mu\), define the lower endpoint projector selected by \(\mathcal B\),

\[
Q^-_{\epsilon_c,\mathcal B}
=
\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_v},
\tag{17}
\]

and

\[
A_{\epsilon_c,\mathcal B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,\mathcal B}.
\tag{18}
\]

For a lower energy \(\epsilon_v<\mu\), define

\[
Q^+_{\epsilon_v,\mathcal B}
=
\sum_{\substack{\epsilon_c>\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_c},
\tag{19}
\]

\[
B_{\epsilon_v,\mathcal B}
=Q^+_{\epsilon_v,\mathcal B}\hat v_iP_{\epsilon_v}.
\tag{20}
\]

The invariant optical-velocity resource is

\[
\boxed{
u_{\mathcal B}^2
=
\max\!\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,\mathcal B}\|_{\rm op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,\mathcal B}\|_{\rm op}^2
\right].
}
\tag{21}
\]

In Eq. (21), the symbol is the Latin \(u_{\mathcal B}\), not a Greek frequency variable. The operator norms maximize only over arbitrary superpositions inside a single degenerate energy eigenspace, so the definition is invariant under the actual eigenbasis freedom without coherently mixing states at different energies.

Every selected row and column strength is at most \(u_{\mathcal B}^2\). Therefore

\[
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h),
\tag{22}
\]

where

\[
n_e=\frac{1}{V}\sum_cp_c,
\qquad
n_h=\frac{1}{V}\sum_vh_v.
\tag{23}
\]

### Theorem 2: windowed thermal population bound

Combining Eqs. (16) and (22),

\[
\boxed{
n_e+n_h
\ge
\frac{2}{\pi e^2u_{\mathcal B}^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega .
}
\tag{24}
\]

For an intrinsic charge-neutral absorber, \(n_e=n_h\equiv n_{\rm th}\),

\[
\boxed{
n_{\rm th}
\ge
\frac{1}{\pi e^2u_{\mathcal B}^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
\,d\omega .
}
\tag{25}
\]

A global bound is a special case only when the corresponding all-frequency shell resource remains finite. If the physical velocity operator itself is bounded, projector contraction gives \(u_{\mathcal B}\le\|\hat v_i\|_{\rm op}\); bounded Wannier/tight-binding models can supply a further microscopic hopping ceiling.

---

## IV. Low-energy consequence

The thermal kernel has the expansion

\[
K_T(E)=2k_BT-\frac{E}{2}+O(E^2/k_BT).
\tag{26}
\]

Thus, if a useful direct optical window is shifted toward zero energy while its **integrated** cross-\(\mu\) conductivity and \(u_{\mathcal B}\) remain finite,

\[
\boxed{
n_e+n_h
\gtrsim
\frac{4k_BT}{\pi e^2u_{\mathcal B}^2}
\int_{\mathcal B}\sigma_1^{\rm cross}(\omega)d\omega .
}
\tag{27}
\]

The intrinsic bound is half the right-hand side.

The integrated-weight condition is essential. A requirement only on the peak conductivity of a line whose useful bandwidth tends to zero does not produce a finite population bound, because its integrated spectral weight can vanish. Equation (27) concerns finite oscillator strength over a specified useful spectral window.

Within that scope, lowering the useful direct transition energy alone cannot yield simultaneously finite optical spectral weight and vanishing equilibrium free-charge population. The escape variable is explicit: more selected optical velocity strength must be concentrated into each thermally occupiable energy shell, or the absorber must leave the theorem class.

---

## V. Equality and validation

### A. Mirror-symmetric parabolic bands

Consider the ideal three-dimensional direct-gap model

\[
E_c(k)=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
\qquad
E_v(k)=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h},
\tag{28}
\]

with vertical transitions and a constant one-to-one optical velocity matrix element \(|v_{cv}|=v_0\).

When \(m_e=m_h\), intrinsic neutrality gives \(\mu=0\), and every vertical transition is mirror symmetric about the chemical potential. The pointwise Fermi bound therefore saturates at every \(k\). The corresponding selected energy-shell block has \(u_{\mathcal B}=v_0\), so the population bound is exact within this ideal model:

\[
\boxed{
(n_e+n_h)_{\rm bound}
=(n_e+n_h)_{\rm exact}
}
\tag{29}
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
\tag{30}
\]

At \(E_g/k_BT=4.7959\), exact finite-temperature evaluation gives ratios \(0.9161\), \(0.6455\), and \(0.4379\) for \(m_h/m_e=2,5,\) and \(10\), respectively. The equal-mass model remains exactly saturated.

This equality construction is an ideal effective model, not a claim that a real semiconductor remains parabolic with constant matrix element to arbitrarily high energy. Its role is to show that the inequality is tight and to identify mirror electron-hole structure as its equality condition. The favorable role of reducing conduction/valence asymmetry is itself established semiconductor-optics physics [6].

### B. Dirac systems

For neutral two-dimensional massless Dirac quasiparticles, the exact finite-temperature interband sheet conductivity [7,8] gives

\[
n_e^{\rm bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\qquad
n_e^{\rm exact}
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\tag{31}
\]

so the theorem recovers one half of the exact thermal electron population. The corresponding ratio is \(2/3\) for an isotropic three-dimensional massless Dirac cone [9].

For the gapped three-dimensional massive-Dirac dispersion

\[
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\tag{32}
\]

using the exact finite-temperature conductivity and carrier density [9,10] gives

\[
\boxed{
\frac{(n_e+n_h)_{\rm bound}}
{(n_e+n_h)_{\rm exact}}
=0.794684
}
\tag{33}
\]

at \(2\Delta/k_BT=4.7959\), corresponding to a 10-µm gap at 300 K.

| Model | Bound / exact thermal population |
|---|---:|
| 2-D neutral massless Dirac | 0.5000 |
| 3-D massless Dirac | 0.6667 |
| 3-D massive Dirac, \(\Delta/k_BT=2.398\) | 0.7947 |
| 3-D parabolic, \(m_h/m_e=2\), \(E_g/k_BT=4.796\) | 0.9161 |
| 3-D parabolic, \(m_h=m_e\) | 1.0000 |

For the massive-Dirac family the ratio approaches unity as \(\Delta/k_BT\) increases, consistent with increasing concentration of the thermally active optical states near mirror-symmetric band edges.

---

## VI. Relation to established theory

### A. Phase-space filling

Semiconductor phase-space-filling theory computes how specified carrier occupations reduce optical absorption [2,3]. Equation (24) uses the same exclusion physics in the inverse direction, but the global statement also closes the state-reuse loophole through the finite selected optical strength of each degenerate energy shell. The resulting inequality does not require a chosen density of states.

### B. Optical sum rules

Conventional and generalized \(f\)-sum rules constrain conductivity moments through total charge density, kinetic energy, or Hamiltonian derivatives [4]. Quantum-geometric sums use different frequency moments to access Wannier spread or quantum metric [5]. Equation (24) instead uses the finite-temperature kernel

\[
\frac{E}{e^{E/(2k_BT)}-1}
\tag{34}
\]

and bounds thermally excited upper-state electrons and lower-state holes. It is complementary to, rather than a replacement for, standard sum rules.

### C. Low-carrier optical band engineering

The physical intuition that lighter and more symmetric electron-hole bands can reduce carrier requirements is old. Yablonovitch and Kane showed that lowering valence-band effective mass can reduce the injected carrier density and threshold current required for semiconductor lasing [6]. The parabolic equality structure above is consistent with that established direction. The candidate contribution here is the equilibrium inverse spectral-weight inequality, not the design slogan that symmetric bands are favorable.

### D. Infrared detector criteria

The classic infrared material criterion \(\alpha/G_{\rm th}\) directly compares useful absorption with thermal generation [1]. Equation (24) lies upstream of a generation model: it constrains the equilibrium population of the states needed to carry the optical response. There is no universal conversion from this population to a generation rate because recombination lifetime and detector collection/response time need not coincide. The present result is therefore a necessary state-count condition, not a replacement for \(\alpha/G_{\rm th}\).

---

## VII. Scope and escape routes

**Neutral excitons and collective states.** A bound exciton can carry low-energy optical oscillator strength below the free electron-hole continuum while remaining electrically neutral. Photocurrent then requires a separate dissociation step. Such systems lie outside a theorem formulated in terms of independent free quasiparticle population.

**Indirect transitions.** Phonon-assisted absorption requires a joint electron-phonon transition amplitude rather than the direct one-body velocity graph in Eq. (5).

**Many-body broadening.** Static one-body disorder is allowed if exact eigenstates are used. Interaction-generated spectral functions and phenomenological lifetime broadening require a many-body generalization.

**Localization and terminal current.** Localized optically active states still obey the population inequality but may contribute weakly to dc transport. No universal dark-current floor follows from Eq. (24).

**Finite-bandwidth noise.** A related inequality exists for the sum of independent Fermi occupation variances, but kinetics determine how that variance is distributed in frequency. No universal readout-band noise floor follows.

**Photonic enhancement.** Equation (24) constrains intrinsic electronic conductivity. Translating it to external absorptance depends on optical architecture. Resonant, antenna, or slow-light enhancement spends additional electromagnetic resources.

**Vanishing useful bandwidth.** The theorem constrains spectral weight. A peak-only detector requirement with arbitrarily small useful bandwidth can have arbitrarily small integrated weight and therefore an arbitrarily weak population bound.

These escape routes identify concrete ways to leave the direct independent-quasiparticle class or to change the optical resource being constrained.

---

## VIII. Conclusion

Direct cross-chemical-potential optical transitions in an equilibrium independent-quasiparticle system obey

\[
\boxed{
\frac{2}{\pi e^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega
\le
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h).
}
\tag{35}
\]

Here \(u_{\mathcal B}\) is defined invariantly by the largest selected optical-coupling operator norm within any exact degenerate upper or lower energy eigenspace. The left inequality follows directly from Fermi statistics and Kubo-Greenwood response; the right converts the thermally weighted optical resource into a state-count bound.

The theorem is exactly saturated by mirror-symmetric equal-mass parabolic bands in the ideal two-band model and remains quantitatively substantial in mass-asymmetric parabolic and Dirac systems. Its low-energy limit shows that finite integrated direct optical spectral weight carries a finite thermal quasiparticle population cost at fixed optical velocity resource.

This is not a universal photodetector-performance limit. Recombination, collection, localization, neutral excitons, indirect absorption, many-body dynamics, useful spectral bandwidth, and photonic enhancement introduce independent resources. Within the stated direct independent-quasiparticle class, however, the inequality isolates an optical-statistical constraint that is normally hidden after a specific density of states and recombination model have already been assumed.

---

## Appendix A. Single-pass 10-µm illustration

For a weak-loss homogeneous absorber,

\[
\alpha(\omega)\simeq
\frac{\sigma_1^{\rm cross}(\omega)}{n_b\epsilon_0c}.
\tag{A1}
\]

At 300 K, take a 10-µm absorption edge, \(n_b=3.5\), and require single-pass absorptance \(A\ge0.90\) over \(\mathcal B=[\omega_g,1.1\omega_g]\). Exact integration of Eq. (25) gives the illustrative intrinsic electron-column bounds

| \(u_{\mathcal B}\) (m/s) | Minimum electron column (cm\(^{-2}\)) |
|---:|---:|
| \(5.0\times10^5\) | \(3.66\times10^{12}\) |
| \(1.0\times10^6\) | \(9.15\times10^{11}\) |
| \(1.07\times10^6\) | \(7.99\times10^{11}\) |
| \(2.0\times10^6\) | \(2.29\times10^{11}\) |
| \(3.0\times10^6\) | \(1.02\times10^{11}\) |

These values are only a material-dominant single-pass illustration. Unconstrained photonic path enhancement changes the conversion from external absorptance to intrinsic material spectral weight.

---

## Appendix B. Secondary occupation-fluctuation corollary

For one crossing transition,

\[
D_{cv}
\le
\sinh\!\left(\frac{E_{cv}}{2k_BT}\right)
\left[p_c(1-p_c)+h_v(1-h_v)\right].
\tag{B1}
\]

Summing with the same selected optical resource yields a lower bound on the total independent-Fermi one-body occupation variance. The statement is frequency integrated; a finite-bandwidth noise bound requires kinetic information and is not claimed here.

---

## References

[1] J. Piotrowski and W. Gawron, “Ultimate performance of infrared photodetectors and figure of merit of detector material,” *Infrared Physics & Technology* **38**, 63–68 (1997), DOI `10.1016/S1350-4495(96)00030-8`.

[2] D. Huang, J.-I. Chyi, and H. Morkoç, “Carrier effects on the excitonic absorption in GaAs quantum-well structures: Phase-space filling,” *Physical Review B* **42**, 5147 (1990), DOI `10.1103/PhysRevB.42.5147`.

[3] N. H. Kwong, G. Rupper, and R. Binder, “Self-consistent T-matrix theory of semiconductor light-absorption and luminescence,” *Physical Review B* **79**, 155205 (2009), DOI `10.1103/PhysRevB.79.155205`.

[4] H. Watanabe and M. Oshikawa, “Generalized f-sum rules and Kohn formulas on nonlinear conductivities,” *Physical Review B* **102**, 165137 (2020), DOI `10.1103/PhysRevB.102.165137`.

[5] L. F. Cárdenas-Castillo, S. Zhang, F. L. Freire Jr., D. Kochan, and W. Chen, “Detecting the spread of valence-band Wannier functions by optical sum rules,” *Physical Review B* **110**, 075203 (2024), DOI `10.1103/PhysRevB.110.075203`.

[6] E. Yablonovitch and E. O. Kane, “Reduction of lasing threshold current density by the lowering of valence band effective mass,” *Journal of Lightwave Technology* **4**, 504–506 (1986), DOI `10.1109/JLT.1986.1074751`.

[7] V. P. Gusynin and S. G. Sharapov, “Transport of Dirac quasiparticles in graphene: Hall and optical conductivities,” *Physical Review B* **73**, 245411 (2006), DOI `10.1103/PhysRevB.73.245411`.

[8] V. P. Gusynin, S. G. Sharapov, and J. P. Carbotte, “Sum rules for the optical and Hall conductivity in graphene,” *Physical Review B* **75**, 165407 (2007), DOI `10.1103/PhysRevB.75.165407`.

[9] C. J. Tabert, J. P. Carbotte, and E. J. Nicol, “Optical and transport properties in three-dimensional Dirac and Weyl semimetals,” *Physical Review B* **93**, 085426 (2016); Erratum *Physical Review B* **94**, 039901 (2016), DOI `10.1103/PhysRevB.93.085426`.

[10] C. J. Tabert and J. P. Carbotte, “Optical conductivity of Weyl semimetals and signatures of the gapped semimetal phase transition,” *Physical Review B* **93**, 085442 (2016), DOI `10.1103/PhysRevB.93.085442`.
