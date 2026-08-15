# Thermal population cost of direct interband optical spectral weight

**Anonymous manuscript — Rev6 — 2026-08-14**

## Abstract

Low thermal carrier population and strong low-energy optical coupling are competing requirements in direct interband absorbers, but their relation is usually evaluated only after a density of states and recombination model have been chosen. We derive a finite-temperature inequality that precedes those choices. For exact independent-quasiparticle states below and above the chemical potential, let \(\sigma_1^{\rm cross}(\omega)\) denote the direct optical conductivity from transitions crossing the chemical potential in an arbitrary positive-frequency window \(\mathcal B\). Exact Fermi statistics and Kubo-Greenwood response give a thermally weighted optical-strength inequality. Introducing a basis-invariant per-shell optical-velocity capacity \(v_{\mathcal B}^{\rm cap}\) and the support ranks of the selected coupling blocks yields

\[
\boxed{
\frac{2}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega
\le
n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}
\le n_e+n_h .
}
\]

Here \(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}\) is the equilibrium thermal population of the one-body optical-support subspaces selected by \(\mathcal B\). Because the thermal kernel tends to \(2k_BT\) at low photon energy, fixed low-energy **integrated** direct spectral weight cannot coexist with vanishing active thermal quasiparticle population at fixed \(v_{\mathcal B}^{\rm cap}\). Mirror-symmetric equal-mass parabolic bands exactly saturate the active-subspace bound for every spectral window in the ideal one-to-one model; the total-population bound is saturated when the full direct spectrum is selected. Independent Dirac checks recover one half of the exact thermal population in neutral two-dimensional massless Dirac systems, two thirds in three dimensions, and \(0.7947\) for a three-dimensional massive-Dirac model at a 10-µm, 300-K gap. The result is an equilibrium quasiparticle state-count constraint, not a universal dark-current or detectivity limit.

---

## I. Introduction

An interband photodetector requires electronic states that couple strongly to the optical field while remaining sparsely thermally populated. In the infrared, where useful photon energies can be only a few \(k_BT\), this tension is severe. Conventional detector theory generally evaluates it only after a material-specific model has supplied an absorption coefficient, density of states, thermal generation rate, recombination law, and transport model. A classic example is the infrared-detector material criterion based on useful absorption relative to thermal generation, such as \(\alpha/G_{\rm th}\) [1].

A more primitive question can be asked before those model choices:

> If an equilibrium independent-quasiparticle material retains a specified amount of low-energy direct interband optical spectral weight, how small can the thermal population of the electronic states carrying that response be?

Several established theories constrain pieces of this problem. Semiconductor phase-space filling calculates how electron and hole occupations bleach optical transitions [2,3]. Optical \(f\)-sum rules constrain conductivity moments through all-electron or kinetic quantities [4]. Quantum-geometric optical sums relate other response moments to Wannier spread and quantum metric [5]. In semiconductor lasers, reducing valence-band mass and electron-hole density-of-states asymmetry has long been recognized as a route to reducing the injected carrier density required for transparency and gain [6].

The present question is the inverse equilibrium problem. We ask whether surviving cross-Fermi optical spectral weight itself enforces a minimum thermal electron-hole excitation population when the selected optical velocity strength available from any one degenerate energy shell is finite.

The derivation has three steps. First, an exact Fermi-Dirac inequality relates the population difference of one transition crossing the chemical potential to the thermal occupation of its upper state and the thermal hole occupation of its lower state. Second, Kubo-Greenwood converts that local relation into a frequency-integrated response inequality. Third, a singular-value/rank bound prevents one energy eigenspace from supplying unlimited selected optical weight without a corresponding number of optically active one-body degrees of freedom.

The theorem is formulated for any measurable positive-frequency window. It does not assume parabolic or Dirac dispersion, equal degeneracy, Bloch momentum, translational invariance, or one-to-one transition counting. Static one-body disorder is allowed if exact eigenstates are used.

The scope is narrower than a detector-performance theorem. The result constrains **integrated** direct spectral weight, not an arbitrarily high peak response in a vanishingly narrow line. Equilibrium quasiparticle population is not identical to dark current: localization can suppress transport, and collection time need not equal recombination lifetime. Neutral excitons can carry low-energy oscillator strength without being free charge. The theorem therefore supplies a necessary electronic-state-count condition for direct independent-quasiparticle absorbers, not a universal limit on \(D^*\), dark current, thermal generation, or finite-bandwidth noise.

---

## II. Cross-\(\mu\) optical transitions and the pointwise Fermi bound

Consider an equilibrium independent-particle Hamiltonian in a finite normalization volume \(V\) with chemical potential \(\mu\). Let \(v\) label exact one-particle eigenstates below \(\mu\), and \(c\) exact states above it,

\[
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0.
\tag{1}
\]

Spin, valley, orbital, finite-volume, and static-disorder multiplicities are included in the state labels. The thermodynamic limit is taken only after the finite-system inequalities are established. In two dimensions the same derivation uses sample area in place of \(V\) and sheet conductivity in place of bulk conductivity.

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

For one physical velocity/current polarization \(i\), write

\[
v_{cv}=\langle c|\hat v_i|v\rangle.
\tag{4}
\]

The positive-frequency conductivity contributed only by transitions crossing \(\mu\) is

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

Transitions whose initial and final states lie on the same side of \(\mu\), phonon-assisted processes, and neutral collective optical excitations are not included in Eq. (5).

Set

\[
a=e^{-(E_c-\mu)/(k_BT)},
\qquad
b=e^{-(\mu-E_v)/(k_BT)}.
\tag{6}
\]

Then \(ab=e^{-E_{cv}/(k_BT)}\equiv z\), and

\[
D_{cv}=\frac{1-z}{(1+a)(1+b)},
\qquad
p_c+h_v=\frac{a+b+2z}{(1+a)(1+b)}.
\tag{7}
\]

At fixed transition energy, the arithmetic-geometric mean inequality gives \(a+b\ge2\sqrt{ab}\). Therefore

\[
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v .
}
\tag{8}
\]

Equality holds if and only if

\[
E_c-\mu=\mu-E_v=\frac{E_{cv}}{2}.
\tag{9}
\]

Thus the least thermally populated realization of a crossing transition of fixed energy places its two states symmetrically about the chemical potential. The Bose-like denominator in Eq. (8) is not an assumed bosonic occupation; it emerges from optimizing two Fermi occupations.

---

## III. Arbitrary-window theorem hierarchy

Let \(\mathcal B\) be any measurable set of positive angular frequencies and define

\[
\mathcal T_{\mathcal B}
=\{(c,v):E_{cv}/\hbar\in\mathcal B\}.
\tag{10}
\]

For a chosen exact eigenbasis define selected row and column strengths

\[
R_c(\mathcal B)
=\sum_{v:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2,
\qquad
C_v(\mathcal B)
=\sum_{c:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2.
\tag{11}
\]

The thermally weighted selected velocity strength is

\[
\boxed{
\mathcal R_{\mathcal B}(T)
=\frac1V\left[
\sum_cp_cR_c(\mathcal B)
+\sum_vh_vC_v(\mathcal B)
\right].
}
\tag{12}
\]

Although individual row and column strengths can redistribute under rotations inside an exactly degenerate eigenspace, Eq. (12) is invariant because all states in that eigenspace have the same Fermi occupation.

Define

\[
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
\tag{13}
\]

Multiplying Eq. (8) by \(|v_{cv}|^2\), summing over \(\mathcal T_{\mathcal B}\), and using Eq. (5) gives the first theorem.

### Theorem 1: thermal optical velocity-strength inequality

\[
\boxed{
\mathcal R_{\mathcal B}(T)
\ge
\frac{2}{\pi e^2}
\int_{\mathcal B}
K_T(\hbar\omega)
\sigma_1^{\rm cross}(\omega)\,d\omega .
}
\tag{14}
\]

Equation (14) contains no maximum-velocity or density-of-states approximation.

### A. Basis-invariant shell optical-velocity capacity

Let \(P_\epsilon\) project onto the complete exact eigenspace at one-particle energy \(\epsilon\). For an upper shell \(\epsilon_c>\mu\), define

\[
Q^-_{\epsilon_c,\mathcal B}
=\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_v},
\qquad
A_{\epsilon_c,\mathcal B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,\mathcal B}.
\tag{15}
\]

For a lower shell \(\epsilon_v<\mu\), define

\[
Q^+_{\epsilon_v,\mathcal B}
=\sum_{\substack{\epsilon_c>\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_c},
\qquad
B_{\epsilon_v,\mathcal B}
=Q^+_{\epsilon_v,\mathcal B}\hat v_iP_{\epsilon_v}.
\tag{16}
\]

Define the basis-invariant selected optical-velocity capacity

\[
\boxed{
\left(v_{\mathcal B}^{\rm cap}\right)^2
=
\max\!\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,\mathcal B}\|_{\rm op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,\mathcal B}\|_{\rm op}^2
\right].
}
\tag{17}
\]

The operator norms maximize only over superpositions inside one exactly degenerate energy eigenspace; states at distinct energies are not coherently mixed.

### B. Basis-invariant optically active thermal population

Define the selected support ranks

\[
r^+_{\epsilon_c,\mathcal B}
=\operatorname{rank}A_{\epsilon_c,\mathcal B},
\qquad
r^-_{\epsilon_v,\mathcal B}
=\operatorname{rank}B_{\epsilon_v,\mathcal B}.
\tag{18}
\]

All ranks in Eqs. (18)–(20) are finite-system ranks before the thermodynamic limit. They are invariant under arbitrary unitary changes of basis within an exact degenerate shell.

Define the corresponding thermal populations

\[
\boxed{
n_{e,\mathcal B}^{\rm act}
=\frac1V
\sum_{\epsilon_c>\mu}f(\epsilon_c)r^+_{\epsilon_c,\mathcal B},
}
\tag{19}
\]

\[
\boxed{
n_{h,\mathcal B}^{\rm act}
=\frac1V
\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]r^-_{\epsilon_v,\mathcal B}.
}
\tag{20}
\]

These quantities count the support dimension of the selected optical coupling blocks, weighted by thermal occupation. They are not oscillator-strength-weighted participation ratios. Since each selected rank is at most the dimension of its parent eigenspace,

\[
n_{e,\mathcal B}^{\rm act}\le n_e,
\qquad
n_{h,\mathcal B}^{\rm act}\le n_h,
\tag{21}
\]

where \(n_e=V^{-1}\sum_cp_c\) and \(n_h=V^{-1}\sum_vh_v\).

Regrouping Eq. (12) by exact energy shell gives traces of \(AA^\dagger\) and \(B^\dagger B\). For any operator \(X\),

\[
\operatorname{Tr}(XX^\dagger)
\le
\|X\|_{\rm op}^2\operatorname{rank}X.
\tag{22}
\]

Therefore

\[
\boxed{
\mathcal R_{\mathcal B}(T)
\le
\left(v_{\mathcal B}^{\rm cap}\right)^2
\left(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}\right).
}
\tag{23}
\]

### Theorem 2: windowed optically active thermal-population bound

Combining Eqs. (14) and (23),

\[
\boxed{
n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}
\ge
\frac{2}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega .
}
\tag{24}
\]

Together with Eq. (21),

\[
\boxed{
n_e+n_h
\ge
n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}
\ge
\frac{2}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega .
}
\tag{25}
\]

For an intrinsic neutral absorber, \(n_e=n_h\equiv n_{\rm th}\), Eq. (25) implies

\[
\boxed{
n_{\rm th}
\ge
\frac{1}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega .
}
\tag{26}
\]

A global all-frequency statement is a special case only when the corresponding global selected shell capacity is finite. A bounded physical velocity operator is sufficient but not necessary; a selected cross-band block can remain bounded even if unrelated high-energy or intraband velocities do not.

---

## IV. Low-energy consequence

The thermal kernel has the expansion

\[
K_T(E)=2k_BT-\frac{E}{2}+O(E^2/k_BT).
\tag{27}
\]

Thus if a useful direct optical window is shifted toward zero transition energy while its **integrated** cross-\(\mu\) conductivity and \(v_{\mathcal B}^{\rm cap}\) remain finite,

\[
\boxed{
n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}
\gtrsim
\frac{4k_BT}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}\sigma_1^{\rm cross}(\omega)d\omega .
}
\tag{28}
\]

The total excitation population is at least as large. The integrated-weight condition is essential: a requirement only on the peak conductivity of a line whose useful bandwidth tends to zero does not impose a finite population floor because its integrated spectral weight can vanish.

Within the stated theorem class, lowering the useful direct transition energy alone cannot produce simultaneously finite optical spectral weight and vanishing thermal population of the states carrying that response. The escape variable is explicit: more selected optical velocity strength must be concentrated into each optically active energy shell, or the absorber must leave the independent-quasiparticle direct-transition class.

---

## V. Equality and quantitative validation

### A. Mirror-symmetric parabolic direct bands

Consider ideal three-dimensional direct-gap bands

\[
E_c(k)=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
\qquad
E_v(k)=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h},
\tag{29}
\]

with vertical transitions and a constant one-to-one optical velocity matrix element \(|v_{cv}|=v_0\).

For \(m_e=m_h\), intrinsic neutrality gives \(\mu=0\), and every vertical transition is mirror symmetric. For any selected direct-transition window \(\mathcal B\), the pointwise Fermi inequality saturates and every selected shell coupling block has all nonzero singular values equal to \(v_0\). Hence

\[
\boxed{
(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act})_{\rm bound}
=
(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act})_{\rm exact}
}
\tag{30}
\]

at all temperatures within this ideal model.

The **total-population** inequality in Eq. (25) is exactly saturated only when the selected window covers the full relevant direct spectrum. For a partial window, thermally occupied states outside the selected optical graph make \(n_e+n_h\) strictly larger than the active population.

For unequal masses in the nondegenerate limit, using the global direct spectrum gives

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
\tag{31}
\]

At \(E_g/k_BT=4.7959\), exact finite-temperature evaluation gives total-population ratios \(0.9161\), \(0.6455\), and \(0.4379\) for \(m_h/m_e=2,5,\) and \(10\), respectively. The equal-mass global model remains exactly saturated. The favorable role of reducing electron-hole asymmetry is established semiconductor-optics physics [6]; the point here is the inverse spectral-weight inequality and its equality structure.

### B. Dirac systems

For neutral two-dimensional massless Dirac quasiparticles, the two-dimensional form of the theorem uses sample area and sheet conductivity. Exact finite-temperature interband sheet conductivity [7,8] inserted into the global theorem gives

\[
n_e^{\rm bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\qquad
n_e^{\rm exact}
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\tag{32}
\]

so the bound recovers one half of the exact thermal electron areal density. The corresponding global ratio is \(2/3\) for an isotropic three-dimensional massless Dirac cone [9].

For the gapped three-dimensional massive-Dirac dispersion

\[
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\tag{33}
\]

using the finite-temperature conductivity and exact carrier density [9,10] gives

\[
\boxed{
\frac{(n_e+n_h)_{\rm bound}}
{(n_e+n_h)_{\rm exact}}
=0.794684
}
\tag{34}
\]

at \(2\Delta/k_BT=4.7959\), corresponding to a 10-µm gap at 300 K.

| Model | Global bound / exact total thermal population |
|---|---:|
| 2-D neutral massless Dirac | 0.5000 |
| 3-D massless Dirac | 0.6667 |
| 3-D massive Dirac, \(\Delta/k_BT=2.398\) | 0.7947 |
| 3-D parabolic, \(m_h/m_e=2\), \(E_g/k_BT=4.796\) | 0.9161 |
| 3-D parabolic, \(m_h=m_e\) | 1.0000 |

For the massive-Dirac family the ratio approaches unity as \(\Delta/k_BT\) increases, consistent with increasing concentration of thermally active optical states near mirror-symmetric band edges.

---

## VI. Relation to established theory

### A. Phase-space filling

Semiconductor phase-space-filling theory computes how specified carrier occupations reduce optical absorption [2,3]. Equation (24) uses the same exclusion physics in the inverse direction. The global step is not merely transitionwise inversion: the selected shell operator norm and support rank close the possibility that one thermally occupiable energy eigenspace supplies unlimited optical weight through many partners.

### B. Optical sum rules

Conventional and generalized \(f\)-sum rules constrain conductivity moments through total charge density, kinetic energy, or Hamiltonian derivatives [4]. Quantum-geometric sums use different frequency moments to access Wannier spread or quantum metric [5]. Equations (24)–(26) instead use the finite-temperature kernel

\[
\frac{E}{e^{E/(2k_BT)}-1}
\tag{35}
\]

and bound thermal occupation of the optically active cross-\(\mu\) one-body subspaces. The result is complementary to standard sum rules.

### C. Low-carrier optical band engineering

The intuition that lighter and more symmetric electron-hole bands can reduce carrier requirements is old. Yablonovitch and Kane showed that lowering valence-band effective mass can reduce the injected carrier density and threshold current required for semiconductor lasing [6]. The parabolic equality family is consistent with that established direction. The candidate contribution here is the equilibrium inverse windowed spectral-weight inequality and its active-subspace state-count form, not the design slogan that symmetric bands are favorable.

### D. Infrared detector criteria

The classic infrared material criterion \(\alpha/G_{\rm th}\) compares useful absorption with thermal generation [1]. Equations (24)–(26) lie upstream of any generation model: they constrain equilibrium populations of the states required to carry direct optical response. There is no universal conversion from this population to a generation rate because recombination lifetime and detector collection/response time need not coincide.

---

## VII. Scope and escape routes

**Neutral excitons and collective states.** A bound exciton can carry low-energy optical oscillator strength below the free electron-hole continuum while remaining electrically neutral. Photocurrent then requires a separate dissociation step. Such systems lie outside a theorem formulated in terms of independent free quasiparticle states.

**Indirect transitions.** Phonon-assisted absorption requires a joint electron-phonon transition amplitude rather than the direct one-body velocity graph in Eq. (5).

**Many-body broadening.** Static one-body disorder is allowed if exact eigenstates are used. Interaction-generated spectral functions and phenomenological lifetime broadening require a many-body generalization.

**Localization and terminal current.** Localized optically active states still obey the population theorem but may contribute weakly to dc transport. No universal dark-current floor follows.

**Finite-bandwidth noise.** A related inequality exists for independent-Fermi occupation variance, but kinetics determine how that variance is distributed in frequency. No universal readout-band noise floor follows.

**Photonic enhancement.** The theorem constrains intrinsic electronic conductivity. Translating it to external absorptance depends on optical architecture; resonant, antenna, or slow-light enhancement spends additional electromagnetic resources.

**Vanishing useful bandwidth.** A peak-only detector requirement with arbitrarily small useful bandwidth can have arbitrarily small integrated spectral weight and therefore an arbitrarily weak population bound.

---

## VIII. Conclusion

For equilibrium independent quasiparticles, direct transitions crossing the chemical potential obey

\[
\boxed{
\frac{2}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega
\le
n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}
\le n_e+n_h .
}
\tag{36}
\]

The first inequality combines Fermi statistics, Kubo-Greenwood response, and a basis-invariant singular-value/rank capacity for each selected degenerate energy shell. The second states that the selected optical support subspaces are subsets of the full thermal excitation space.

The theorem is exactly saturated by mirror-symmetric equal-mass parabolic bands for the **active population in any spectral window**, and for the **total population when the full direct spectrum is selected**. It remains quantitatively substantial in mass-asymmetric parabolic and Dirac models. Its low-energy limit shows that finite integrated direct optical spectral weight carries a finite thermal quasiparticle population cost at fixed selected optical-velocity capacity.

This is not a universal photodetector-performance limit. Recombination, collection, localization, neutral excitons, indirect absorption, many-body dynamics, useful spectral bandwidth, and photonic enhancement introduce independent resources. Within the stated direct independent-quasiparticle class, however, the inequality isolates an optical-statistical state-count constraint without first choosing a density of states or recombination mechanism.

---

## Appendix A. Single-pass 10-µm illustration

For a weak-loss homogeneous absorber,

\[
\alpha(\omega)\simeq
\frac{\sigma_1^{\rm cross}(\omega)}{n_b\epsilon_0c}.
\tag{A1}
\]

At 300 K, take a 10-µm absorption edge, \(n_b=3.5\), and require single-pass absorptance \(A\ge0.90\) over \(\mathcal B=[\omega_g,1.1\omega_g]\). Exact thermal-kernel integration gives the following lower bounds on the total intrinsic electron column.

| \(v_{\mathcal B}^{\rm cap}\) (m/s) | Minimum intrinsic electron column (cm\(^{-2}\)) |
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

Summing with the same selected optical resource yields a lower bound on total independent-Fermi one-body occupation variance. The statement is frequency integrated; a finite-bandwidth noise bound requires kinetic information and is not claimed here.

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