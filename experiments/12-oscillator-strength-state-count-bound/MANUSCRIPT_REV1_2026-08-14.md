# Thermal population cost of direct interband optical spectral weight

**Anonymous manuscript — Rev1 — 2026-08-14**

## Abstract

Low thermal carrier population and strong low-energy optical coupling are competing requirements in direct interband photodetectors, but their relation is usually evaluated only after a density of states and recombination model have been chosen. We derive a finite-temperature inequality that precedes those model choices. For exact independent-quasiparticle states below and above the chemical potential, the direct cross-chemical-potential conductivity in any optical-frequency window \(\mathcal B\) obeys

\[
rac{2}{\pi e^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega
\le
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h),
\]

where \(\mathcal R_{\mathcal B}\) is the thermally occupied optical-velocity strength and \(u_{\mathcal B}\) is a basis-invariant per-energy-shell optical-velocity resource. The kernel approaches \(2k_BT\) at low photon energy; consequently, fixed low-energy direct interband spectral weight cannot coexist with vanishing thermal quasiparticle population at fixed \(u_{\mathcal B}\). Mirror-symmetric equal-mass parabolic bands exactly saturate the bound at all temperatures. It also recovers one half of the exact thermal population in neutral two-dimensional massless Dirac systems, two thirds in three dimensions, and \(0.7947\) for a three-dimensional massive-Dirac model at a 10-µm, 300-K gap. The result is a necessary equilibrium quasiparticle-population constraint, not a universal dark-current or detectivity limit; neutral excitons, indirect absorption, many-body spectral functions, and transport kinetics require additional physics.

---

## I. Introduction

An interband photodetector requires electronic states that couple strongly to the optical field while remaining sparsely thermally populated. In the infrared, where the useful photon energy can be only a few \(k_BT\), this tension is particularly severe. Conventional detector theory usually evaluates it only after a material-specific model has supplied an absorption coefficient, carrier density, recombination rate, and transport law. A classic example is the infrared-detector material criterion based on the ratio of useful absorption to thermal generation, \(\alpha/G_{\rm th}\) [1].

A more primitive question can be asked before a density of states or recombination mechanism is selected:

> If a material retains a specified amount of low-energy direct interband optical spectral weight at equilibrium, how small can the equilibrium population of the electronic states carrying that optical response be?

Several established theories constrain parts of this problem. Semiconductor phase-space filling calculates how electron and hole occupations reduce optical oscillator strength [2,3]. Optical \(f\)-sum rules constrain integrated conductivity through all-electron or kinetic quantities [4]. Quantum-geometric sum rules relate other optical moments to Wannier spread and quantum metric [5]. In semiconductor lasers, reducing valence-band mass and electron-hole density-of-states asymmetry has long been recognized as a route to lowering the carrier density required for transparency and gain [6]. These results establish the relevant physical ingredients and design intuition. They do not, however, directly give an inverse finite-temperature inequality from surviving equilibrium cross-Fermi optical spectral weight to thermally excited electron-hole population without inserting a density-of-states model.

Here we derive such an inequality for independent quasiparticles. The local ingredient is an exact Fermi-Dirac inequality for one transition crossing the chemical potential. The global ingredient is a finite optical-velocity-strength budget per degenerate energy eigenspace: one electronic state cannot supply unlimited squared current-matrix strength to arbitrarily many transitions. Kubo-Greenwood then converts the statewise inequality into a measurable optical spectral functional.

The result is formulated for an arbitrary positive-frequency window and therefore does not require a globally bounded continuum velocity operator. It does not assume parabolic or Dirac dispersion, equal band degeneracy, Bloch momentum, translational invariance, or one-to-one transitions. Static one-body disorder is allowed if exact eigenstates are used. The result has exact equality realizations in mirror-symmetric parabolic bands and remains quantitatively nontrivial in dispersive Dirac systems.

The scope is deliberately narrower than a detector-performance bound. Equilibrium quasiparticle population is not identical to dark current; localization can suppress transport, and collection time need not equal recombination lifetime. Neutral excitons can carry low-energy oscillator strength without being free charge. The theorem therefore provides a necessary electronic-state-count constraint for direct independent-quasiparticle absorbers, not a universal limit on \(D^*\), dark current, or noise.

---

## II. Cross-μ optical transitions and the pointwise Fermi bound

Consider an equilibrium independent-particle Hamiltonian in finite volume \(V\) with chemical potential \(\mu\). Let \(v\) label exact one-particle eigenstates below \(\mu\) and \(c\) exact states above it,

\[
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0.
\tag{1}
\]

The finite-volume formulation makes degeneracies explicit; the thermodynamic limit may be taken after the inequalities are established. Spin, valley, orbital, and static-disorder multiplicities are included in the state labels.

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

For a physical velocity/current polarization \(i\), write

\[
v_{cv}=\langle c|\hat v_i|v\rangle.
\tag{4}
\]

The direct positive-frequency conductivity contributed by transitions crossing \(\mu\) is

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

The restriction to cross-\(\mu\) transitions is essential. Thermally activated transitions entirely below or entirely above the chemical potential obey a weaker detailed-balance relation and are not included in Eq. (5).

### A. Pointwise Fermi lemma

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

and

\[
D_{cv}=\frac{1-z}{(1+a)(1+b)},
\tag{8}
\]

\[
p_c+h_v=\frac{a+b+2z}{(1+a)(1+b)}.
\tag{9}
\]

At fixed transition energy \(ab=z\), and \(a+b\ge2\sqrt{ab}\). Therefore

\[
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v .
}
\tag{10}
\]

Equality holds if and only if

\[
E_c-\mu=\mu-E_v=\frac{E_{cv}}{2}.
\tag{11}
\]

Thus, for a transition of fixed energy, the least thermally costly placement of the participating fermion states is mirror symmetry about the chemical potential. The Bose-like denominator in Eq. (10) is not an assumed boson occupation; it follows from optimizing the two Fermi occupations.

---

## III. Arbitrary-window thermal optical inequality

Let \(\mathcal B\) be any measurable set of positive angular frequencies. Define the selected transition set

\[
\mathcal T_{\mathcal B}
=
\left\{(c,v):E_{cv}/\hbar\in\mathcal B\right\}.
\tag{12}
\]

For a chosen exact eigenbasis, define selected row and column strengths

\[
R_c(\mathcal B)
=
\sum_{v:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2,
\tag{13}
\]

\[
C_v(\mathcal B)
=
\sum_{c:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2.
\tag{14}
\]

Although individual \(R_c\) and \(C_v\) can redistribute under rotations within an exactly degenerate eigenspace, the thermally weighted sum

\[
\mathcal R_{\mathcal B}(T)
=
\frac{1}{V}
\left[
\sum_c p_cR_c(\mathcal B)
+
\sum_v h_vC_v(\mathcal B)
\right]
\tag{15}
\]

is invariant because all states in a degenerate eigenspace have the same Fermi occupation.

Define the thermal kernel

\[
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
\tag{16}
\]

Multiplying Eq. (10) by \(|v_{cv}|^2\), summing over \(\mathcal T_{\mathcal B}\), and using Eq. (5) gives the first theorem.

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
\tag{17}
\]

Equation (17) contains no maximum-velocity or density-of-states approximation.

### A. Basis-invariant optical-velocity resource

To convert Eq. (17) to a population bound, the optical strength available from one thermally occupied state must be bounded without introducing a basis ambiguity inside exact degeneracies.

Let \(P_\epsilon\) be the projector onto the complete eigenspace of one-particle energy \(\epsilon\). For an upper energy \(\epsilon_c>\mu\), define

\[
Q^-_{\epsilon_c,\mathcal B}
=
\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_v},
\tag{18}
\]

\[
A_{\epsilon_c,\mathcal B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,\mathcal B}.
\tag{19}
\]

For a lower energy \(\epsilon_v<\mu\), define analogously

\[
Q^+_{\epsilon_v,\mathcal B}
=
\sum_{\substack{\epsilon_c>\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_c},
\tag{20}
\]

\[
B_{\epsilon_v,\mathcal B}
=Q^+_{\epsilon_v,\mathcal B}\hat v_iP_{\epsilon_v}.
\tag{21}
\]

The basis-invariant selected velocity resource is

\[
\boxed{
u_{\mathcal B}^2
=
\max\!\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,\mathcal B}\|_{\rm op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,\mathcal B}\|_{\rm op}^2
\right].
}
\tag{22}
\]

The operator norms maximize only over arbitrary superpositions *within the same degenerate energy eigenspace*. They do not introduce unphysical coherent mixing between equilibrium states at different energies.

Every selected row or column strength is bounded by \(u_{\mathcal B}^2\). Hence

\[
\mathcal R_{\mathcal B}(T)
\le
u_{\mathcal B}^2(n_e+n_h),
\tag{23}
\]

where

\[
n_e=\frac{1}{V}\sum_cp_c,
\qquad
n_h=\frac{1}{V}\sum_vh_v.
\tag{24}
\]

Combining Eqs. (17) and (23) gives the population theorem.

### Theorem 2: windowed thermal quasiparticle-population bound

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
\tag{25}
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
\tag{26}
\]

The windowed formulation avoids any need for a globally bounded continuum velocity. If the full physical velocity operator has a finite norm, the projectors in Eqs. (19) and (21) immediately give \(u_{\mathcal B}\le\|\hat v_i\|_{\rm op}\). In a bounded orthonormal Wannier representation, a further ultraviolet ceiling follows from hopping range and strength.

---

## IV. Low-energy limit and physical interpretation

The thermal kernel obeys

\[
K_T(E)=2k_BT-\frac{E}{2}+O(E^2/k_BT).
\tag{27}
\]

Thus if a useful direct optical window is shifted toward zero transition energy while both its integrated cross-\(\mu\) conductivity and \(u_{\mathcal B}\) remain fixed,

\[
\boxed{
n_e+n_h
\gtrsim
\frac{4k_BT}{\pi e^2u_{\mathcal B}^2}
\int_{\mathcal B}\sigma_1^{\rm cross}(\omega)d\omega .
}
\tag{28}
\]

For an intrinsic absorber the right side is divided by two.

Equation (28) is the principal qualitative result. Within the independent-quasiparticle direct-transition class, lowering the useful photon energy does not by itself provide a route to simultaneously finite optical spectral weight and vanishing equilibrium free-charge population. The escape resource is explicit: more selected optical velocity strength must be concentrated into each thermally occupiable energy shell, or the detector must leave the theorem class.

The theorem does not state that light effective masses are universally optimal. It states a more primitive resource relation between surviving optical response, equilibrium Fermi population, and the optical matrix strength available from each energy eigenspace.

---

## V. Equality and quantitative validation

### A. Mirror-symmetric parabolic direct bands

Consider the textbook three-dimensional direct-gap model

\[
E_c(k)=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
\qquad
E_v(k)=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h},
\tag{29}
\]

with vertical transitions and a constant one-to-one optical velocity matrix element \(|v_{cv}|=v_0\).

For \(m_e=m_h\), intrinsic neutrality gives \(\mu=0\), and every vertical transition is mirror symmetric,

\[
E_c(k)-\mu=\mu-E_v(k).
\tag{30}
\]

Equation (10) therefore saturates at every \(k\). The selected energy-shell optical block also has norm \(u_{\mathcal B}=v_0\). Consequently

\[
\boxed{
(n_e+n_h)_{\rm bound}
=(n_e+n_h)_{\rm exact}
}
\tag{31}
\]

for a window containing the full direct continuum, at **all temperatures**.

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
\tag{32}
\]

This factor is exactly unity for mirror-symmetric masses and decreases continuously with mass asymmetry. At \(E_g/k_BT=4.7959\), exact finite-temperature integration gives \(0.9161\), \(0.6455\), and \(0.4379\) for \(m_h/m_e=2,5,\) and \(10\), respectively.

The qualitative benefit of reducing conduction/valence density-of-states asymmetry is established semiconductor-laser physics [6]; Eq. (32) is used here as a tightness test and equality interpretation, not as a novelty claim.

### B. Dirac models

The theorem remains nontrivial for strongly nonparabolic dispersions. For neutral two-dimensional massless Dirac quasiparticles, the exact interband sheet conductivity [7,8] yields

\[
n_e^{\rm bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\qquad
n_e^{\rm exact}
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\tag{33}
\]

so the bound recovers exactly one half of the thermal electron population. For an isotropic three-dimensional massless Dirac cone, the ratio is \(2/3\) [9].

For a gapped three-dimensional massive-Dirac model,

\[
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\tag{34}
\]

using the finite-temperature optical conductivity and exact carrier density gives the ratios listed in Table I [9,10]. At

\[
\frac{2\Delta}{k_BT}=4.7959,
\tag{35}
\]

corresponding to a 10-µm gap at 300 K,

\[
\boxed{
\frac{(n_e+n_h)_{\rm bound}}
{(n_e+n_h)_{\rm exact}}
=0.794684 .
}
\tag{36}
\]

**Table I.** Tightness of the thermal population bound in representative dispersive models.

| Model | Bound / exact thermal population |
|---|---:|
| 2-D neutral massless Dirac | 0.5000 |
| 3-D massless Dirac | 0.6667 |
| 3-D massive Dirac, \(\Delta/k_BT=2.398\) | 0.7947 |
| 3-D parabolic, \(m_h/m_e=2\), \(E_g/k_BT=4.796\) | 0.9161 |
| 3-D parabolic, \(m_h=m_e\) | 1.0000 |

For the massive-Dirac family, the ratio approaches unity as \(\Delta/k_BT\) increases. This trend is consistent with the equality condition: thermally relevant upper and lower states become increasingly localized near mirror-symmetric band edges.

---

## VI. Relation to established theory

### A. Phase-space filling

Phase-space-filling theory calculates how specified electron and hole occupations bleach semiconductor optical transitions [2,3]. The present result uses the same Fermi exclusion physics in the inverse direction, but the global inequality additionally constrains state reuse: one upper or lower energy eigenspace cannot supply unlimited optical velocity strength to arbitrarily many selected transitions. Equation (25) therefore converts surviving equilibrium spectral weight into a lower thermal-population cost without selecting a density-of-states model.

### B. Optical sum rules

Conventional and generalized \(f\)-sum rules constrain optical moments by total charge density, kinetic energy, or Hamiltonian derivatives [4]. Quantum-geometric sums use other frequency moments to access Wannier spread or quantum metric [5]. Equation (25) instead employs the finite-temperature kernel

\[
\frac{E}{e^{E/(2k_BT)}-1}
\tag{37}
\]

and bounds thermally excited upper-state electrons and lower-state holes. It is therefore complementary to standard sum rules rather than a replacement for them.

### C. Low-carrier band engineering

The physical intuition that lighter and more symmetric electron/hole bands can reduce the carrier density required for an optical task is old. Yablonovitch and Kane showed that lowering the valence-band effective mass can reduce the carrier density and threshold current required for semiconductor lasing [6]. The exact parabolic equality in Eq. (31) is consistent with this established intuition, while Eq. (25) is a different equilibrium inverse constraint that does not assume a parabolic density of states.

### D. Infrared detector material figures of merit

The classic infrared figure of merit based on \(\alpha/G_{\rm th}\) directly compares absorption with thermal generation [1]. Equation (25) lies upstream of a generation model: it constrains the equilibrium population of states required to carry the optical response. There is no universal conversion from that population to a dark-generation rate, because the recombination lifetime that fixes equilibrium turnover need not equal the detector collection or response time. Thus Eq. (25) is a necessary state-count condition, not a replacement for \(\alpha/G_{\rm th}\).

---

## VII. Scope and escape routes

The theorem applies to direct independent-quasiparticle transitions crossing the chemical potential. Several important detector classes lie outside this scope.

**Neutral excitons and collective states.** A bound exciton can carry low-energy optical oscillator strength below the free electron-hole continuum while remaining electrically neutral. Photocurrent then requires a separate dissociation process. Such a detector evades a theorem formulated in terms of free quasiparticle population.

**Indirect transitions.** Phonon-assisted absorption requires a joint electron-phonon matrix element rather than the direct one-body velocity graph in Eq. (5).

**Many-body broadening.** Static one-body disorder does not invalidate the proof if exact eigenstates are used. Interaction-generated spectral functions and phenomenological lifetime broadening require a many-body generalization.

**Localization and terminal current.** Localized optically active states still obey Eq. (25), but can contribute weakly to dc transport. The theorem therefore does not imply a universal dark-current lower bound.

**Finite-bandwidth noise.** A related inequality can be written for the sum of independent Fermi occupation variances, but the distribution of that fluctuation power over frequency depends on kinetics. No universal readout-band noise floor follows from Eq. (25).

**Photonic enhancement.** Equation (25) constrains intrinsic electronic conductivity. Converting external absorptance into material conductivity depends on the optical architecture. Resonant or slow-light path enhancement introduces additional electromagnetic resources.

These are not merely caveats: they identify concrete ways in which a detector can leave the direct independent-quasiparticle class and therefore avoid the particular population cost derived here.

---

## VIII. Conclusion

For an equilibrium independent-quasiparticle absorber, direct optical transitions that cross the chemical potential obey the hierarchy

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
\tag{38}
\]

The left inequality follows only from Fermi statistics and Kubo-Greenwood response. The right inequality introduces the basis-invariant optical velocity resource available from one degenerate energy shell. Together they provide a density-of-states-independent lower bound on equilibrium electron-hole excitation population.

The bound is exactly saturated by mirror-symmetric equal-mass parabolic bands and remains quantitatively substantial in mass-asymmetric parabolic and Dirac models. Because the thermal kernel approaches \(2k_BT\) at low transition energy, finite low-energy direct interband spectral weight carries a finite thermal population cost unless the microscopic optical-velocity resource also increases.

The result should be interpreted as a necessary electronic-state-count condition, not a universal detector-performance limit. Recombination, transport, localization, excitons, indirect processes, and photonic enhancement provide additional independent resources. Within its stated class, however, the inequality isolates an optical-statistical tradeoff that is normally hidden after a particular density of states and recombination model have already been assumed.

---

## Appendix A. Single-pass LWIR illustration

For a weak-loss homogeneous absorber,

\[
\alpha(\omega)\simeq
\frac{\sigma_1^{\rm cross}(\omega)}{n_b\epsilon_0c}.
\tag{A1}
\]

Take \(T=300\) K, a 10-µm absorption edge, \(n_b=3.5\), and require single-pass absorptance \(A\ge0.90\) over \(\mathcal B=[\omega_g,1.1\omega_g]\). Beer-Lambert optical depth then requires \(\alpha d\ge-\ln0.1\). Exact integration of Eq. (26) gives the illustrative intrinsic electron-column bounds

| \(u_{\mathcal B}\) (m/s) | Minimum electron column (cm\(^{-2}\)) |
|---:|---:|
| \(5.0\times10^5\) | \(3.66\times10^{12}\) |
| \(1.0\times10^6\) | \(9.15\times10^{11}\) |
| \(1.07\times10^6\) | \(7.99\times10^{11}\) |
| \(2.0\times10^6\) | \(2.29\times10^{11}\) |
| \(3.0\times10^6\) | \(1.02\times10^{11}\) |

These numbers are not a universal detector floor. Resonant/path-enhanced structures can reduce the amount of active material needed for a given external absorptance by spending separate photonic resources.

---

## Appendix B. Secondary fluctuation statement

For one crossing transition, Fermi algebra also gives

\[
D_{cv}
\le
\sinh\!\left(\frac{E_{cv}}{2k_BT}\right)
\left[p_c(1-p_c)+h_v(1-h_v)\right].
\tag{B1}
\]

Summing with the same optical resource gives a lower bound on the sum of independent grand-canonical one-body occupation variances. This is an integrated equilibrium fluctuation statement, not a finite-bandwidth detector-noise theorem, because kinetics determine how the variance is distributed in frequency.

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
