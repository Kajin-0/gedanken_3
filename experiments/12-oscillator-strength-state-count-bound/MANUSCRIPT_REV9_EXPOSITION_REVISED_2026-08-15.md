# Thermal quasiparticle population bound from direct interband spectral weight under finite optical-velocity capacity

**Anonymous manuscript — Rev9 exposition revision — 2026-08-15**

## Abstract

Low thermal carrier population and strong low-energy optical coupling are competing requirements in direct interband absorbers. Their relation is often evaluated only after a density of states and a recombination model have been chosen. We derive a finite-temperature inequality that precedes those choices.

The construction isolates direct transitions that cross the chemical potential: an electron begins in an exact one-body state below \(\mu\) and ends in an exact state above \(\mu\). The corresponding conductivity, \(\sigma_1^{\rm cross}(\omega)\), therefore retains only the optical response whose initial and final occupations can be tied directly to the thermal electron-hole excitation population. Exact Fermi statistics and Kubo-Greenwood response first give a thermally weighted optical-strength inequality.

A second ingredient is needed because one degenerate energy shell could otherwise couple to many partner states. The **optical-velocity capacity** is the largest selected velocity-operator singular value available from any one exact degenerate shell; it limits how much selected optical strength one shell can supply without increasing the dimension of the optically active one-body support. Introducing the basis-invariant per-shell capacity \(v_{\mathcal B}^{\rm cap}\) and the support ranks of the selected coupling blocks yields

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

In words, a specified amount of thermally weighted direct cross-\(\mu\) optical spectral weight requires a minimum thermal population in the one-body subspaces that carry that response, provided the optical strength available per shell is finite.

Here \(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}\) is the equilibrium thermal population of the one-body optical-support subspaces selected by \(\mathcal B\). A nonzero macroscopic density floor requires the per-shell capacity to remain uniformly bounded along the thermodynamic sequence. This condition is not merely formal. For the standard first-order \(8\times8\) Kane Hamiltonian used for HgCdTe, \(v_{\mathcal B}^{\rm cap}\le\sqrt{3/2}\,v_K\) for every window, giving a microscopic upper-bound scale near \(1.3\times10^6\ \mathrm{m/s}\) from measured Kane velocities. An end-to-end calculation in a second-order eight-band HgCdTe \(k\cdot p\) model gives \(v_{\mathcal B}^{\rm cap}\simeq1.02\times10^6\ \mathrm{m/s}\) and bound/reference ratios ranging from \(0.032\) for \(E_g\le E_{cv}\le1.5E_g\) to \(0.118\) for a broad direct-transition validation window through \(0.5\ \mathrm{eV}\).

Because the thermal kernel tends to \(2k_BT\) at low photon energy, finite low-energy integrated direct spectral weight cannot coexist with vanishing active thermal quasiparticle population when the capacity is bounded uniformly both in system size and along the low-energy window sequence. Mirror-symmetric equal-mass parabolic bands saturate the active-subspace bound within the stated ideal optical model. Independent Dirac checks recover one half of the exact thermal population in neutral two-dimensional massless Dirac systems, two thirds in three dimensions, and \(0.7947\) for a three-dimensional massive-Dirac model at a \(10\ \mu\mathrm m\), \(300\ \mathrm K\) gap. The result is an equilibrium quasiparticle state-count constraint, not a universal dark-current or detectivity limit.

---

## I. Introduction

An interband photodetector requires electronic states that couple strongly to the optical field while remaining sparsely thermally populated. In the infrared, where useful photon energies can be only a few \(k_BT\), this tension is severe. Detector material criteria commonly compare useful absorption with a modeled thermal-generation process, for example through \(\alpha/G_{\rm th}\) [1]. The present question is deliberately upstream of a recombination or transport model. It asks what equilibrium one-body population is already required by the surviving direct optical response itself.

A more primitive question can therefore be asked before those model choices:

> If an equilibrium independent-quasiparticle material retains a specified amount of low-energy direct interband optical spectral weight, how small can the thermal population of the electronic states carrying that response be?

Several established theories constrain pieces of this problem. Semiconductor phase-space filling calculates how electron and hole occupations bleach optical transitions [9,10]. Optical \(f\)-sum rules constrain conductivity moments through all-electron or kinetic quantities [11]. Quantum-geometric optical sums relate other response moments to Wannier spread and quantum metric [12]. In semiconductor lasers, reducing valence-band mass and electron-hole density-of-states asymmetry has long been recognized as a route to reducing the injected carrier density required for transparency and gain [13].

Two canonical equilibrium relations lie nearby but constrain different objects. The van Roosbroeck-Shockley detailed-balance relation obtains radiative electron-hole recombination from optical absorption [2]. Fluctuation-dissipation theory relates dissipative response to equilibrium fluctuations of the conjugate observable [3]. Neither relation by itself gives the one-body state-count inequality derived below. The former targets radiative event rates; the latter targets response fluctuations rather than a minimum thermally excited quasiparticle population.

The present question is the inverse equilibrium problem. We ask whether surviving cross-chemical-potential optical spectral weight itself enforces a minimum thermal electron-hole excitation population when the selected optical velocity strength available from any one degenerate energy shell is finite. The phrase **cross-chemical-potential** will mean a direct one-body transition whose initial state lies below \(\mu\) and whose final state lies above \(\mu\). This partition is chosen because the upper-state electron occupation and lower-state hole occupation are precisely the thermal excitations that can be bounded from Fermi statistics.

The logical chain has three steps, and each step closes a different loophole. First, we need a transition-level statement: an exact Fermi-Dirac inequality relates the population difference of one transition crossing the chemical potential to the thermal occupation of its upper state and the thermal hole occupation of its lower state. Second, a transition-level inequality is not yet a measurable spectral statement, so Kubo-Greenwood converts it into a frequency-integrated response inequality. Third, summing over transitions can reuse the same state many times. A singular-value/rank bound closes that state-reuse loophole by limiting the selected optical strength available from one exact energy eigenspace relative to the number of optically active one-body directions in that eigenspace.

One ideal case will serve as a running intuition anchor. Consider an effective two-band direct-gap model with equal electron and hole masses, intrinsic \(\mu\) at midgap, vertical one-to-one transitions, and a constant interband velocity matrix element. Every selected transition is then mirror symmetric about \(\mu\), and every selected one-body direction spends the same optical-velocity resource. Section V shows that this model exactly saturates the active-subspace inequality for any selected direct-transition window. The general derivation below asks what remains true after mirror symmetry, simple dispersion, equal degeneracy, and one-to-one pairing are all removed.

The theorem is formulated for any measurable positive-frequency window. It does not assume parabolic or Dirac dispersion, equal degeneracy, Bloch momentum, translational invariance, or one-to-one transition counting. Static one-body disorder is allowed if exact eigenstates are used.

The scope is narrower than a detector-performance theorem. The result constrains **integrated** direct spectral weight, not an arbitrarily high peak response in a vanishingly narrow line. Equilibrium quasiparticle population is not identical to dark current: localization can suppress transport, and collection time need not equal recombination lifetime. Neutral excitons can carry low-energy oscillator strength without being free charge. The theorem therefore supplies a necessary electronic-state-count condition for direct independent-quasiparticle absorbers, not a universal limit on \(D^*\), dark current, thermal generation, or finite-bandwidth noise.

---

## II. Cross-chemical-potential transitions and a pointwise Fermi bound

The first step isolates the local statistical cost of a single direct transition. We do this before introducing any spectral integral because the global theorem ultimately inherits its thermal factor from this one-transition Fermi constraint.

Consider an equilibrium independent-particle Hamiltonian in a finite normalization volume \(V\) with chemical potential \(\mu\). We separate exact one-particle states by which side of \(\mu\) they occupy at zero temperature: \(v\) labels a state below \(\mu\), and \(c\) labels a state above it,

\[
E_v<\mu<E_c,
\qquad
E_{cv}=E_c-E_v>0.
\tag{1}
\]

Equation (1) defines the crossing pair whose thermal electron and hole occupations will be compared with its optical population difference.

Spin, valley, orbital, finite-volume, and static-disorder multiplicities are included in the state labels. For compact notation we assume that no selected positive-frequency transition has an endpoint exactly at \(\mu\). If such a state occurs, its contribution is defined by the continuous \(\mu\to\mu\pm0\) limiting prescription. The thermodynamic limit is taken only after the finite-system inequalities are established. In two dimensions the same derivation uses sample area in place of \(V\) and sheet conductivity in place of bulk conductivity.

For a crossing pair, the relevant thermal quantities have direct meanings. The upper-state electron occupation is \(p_c\); the missing lower-state electron, or hole occupation, is \(h_v\). Their difference in one-body occupation controls the available absorption strength. Define

\[
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
\tag{2}
\]

and

\[
D_{cv}=f(E_v)-f(E_c),
\tag{3}
\]

with

\[
f(E)=\frac{1}{e^{(E-\mu)/(k_BT)}+1}.
\tag{4}
\]

Thus \(D_{cv}\) is the Pauli population difference available to drive the direct transition, whereas \(p_c+h_v\) counts the thermal electron-hole excitation associated with its two endpoints.

Optical strength also requires a matrix element. For one physical velocity/current polarization \(i\), write

\[
v_{cv}=\langle c|\hat v_i|v\rangle.
\tag{5}
\]

Before using the full measured conductivity, we isolate the part whose transitions actually cross \(\mu\). This **cross-\(\mu\) conductivity** is the optical spectral weight for precisely the one-body transitions to which the pointwise Fermi inequality applies. The positive-frequency conductivity contributed only by transitions crossing \(\mu\) is

\[
\boxed{
\sigma_1^{\rm cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
}
\tag{6}
\]

Equation (6) is therefore not the total optical conductivity in general; it is the direct response carried by transitions whose two endpoints straddle the chemical potential.

Transitions whose initial and final states lie on the same side of \(\mu\), phonon-assisted processes, and neutral collective optical excitations are not included in Eq. (6).

The next algebraic step asks a specific optimization question: for a fixed transition energy \(E_{cv}\), how small can the endpoint thermal population \(p_c+h_v\) be while retaining the Fermi population difference \(D_{cv}\)? To expose that symmetry, set

\[
a=e^{-(E_c-\mu)/(k_BT)},
\qquad
b=e^{-(\mu-E_v)/(k_BT)}.
\tag{7}
\]

Then \(ab=e^{-E_{cv}/(k_BT)}\equiv z\), and

\[
D_{cv}=\frac{1-z}{(1+a)(1+b)},
\qquad
p_c+h_v=\frac{a+b+2z}{(1+a)(1+b)}.
\tag{8}
\]

At fixed transition energy, \(ab\) is fixed. The arithmetic-geometric mean inequality gives \(a+b\ge2\sqrt{ab}\), so the thermal endpoint population is minimized when the two activation energies are equal. Therefore

\[
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le p_c+h_v .
}
\tag{9}
\]

Equation (9) says that a crossing transition with a specified surviving Fermi population difference cannot be supported by arbitrarily small thermal occupation of its two endpoint states.

Equality holds if and only if

\[
E_c-\mu=\mu-E_v=\frac{E_{cv}}{2}.
\tag{10}
\]

Equation (10) identifies the transition-level optimum: the least thermally costly placement of fixed-energy endpoints is mirror symmetry about the chemical potential. This is the first place where the equal-mass parabolic intuition anchor appears. In that ideal model, every vertical transition satisfies Eq. (10), so the pointwise statistical step is saturated everywhere in the selected spectrum.

The Bose-like denominator in Eq. (9) is not an assumed bosonic occupation. It emerges from optimizing two Fermi occupations.

---

## III. Arbitrary-window theorem hierarchy

The pointwise result is not yet enough because an optical experiment selects a range of transition frequencies and sums over many states. This section first converts Eq. (9) into a windowed optical-strength inequality and then prevents repeated use of the same degenerate shell from making the summed optical response arbitrarily large.

A spectral window should select transitions by their energy difference, without assuming momentum conservation, a band label, or one-to-one pairing. Let \(\mathcal B\) be any measurable set of positive angular frequencies and define

\[
\mathcal T_{\mathcal B}
=\{(c,v):E_{cv}/\hbar\in\mathcal B\}.
\tag{11}
\]

Equation (11) is simply the graph of all cross-\(\mu\) direct transitions whose frequencies lie in the selected optical window.

For bookkeeping, we next ask how much selected squared velocity strength is attached to each upper or lower state. For a chosen exact eigenbasis define

\[
R_c(\mathcal B)
=\sum_{v:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2,
\tag{12}
\]

\[
C_v(\mathcal B)
=\sum_{c:(c,v)\in\mathcal T_{\mathcal B}}|v_{cv}|^2.
\tag{13}
\]

These row and column sums expose state reuse explicitly: one state may contribute optical strength through many selected partners.

The first global quantity combines that selected velocity strength with the thermal cost of the state on which it resides. It is a thermally weighted optical-strength resource, not yet a particle count. Define

\[
\boxed{
\mathcal R_{\mathcal B}(T)
=\frac1V\left[
\sum_cp_cR_c(\mathcal B)
+\sum_vh_vC_v(\mathcal B)
\right].
}
\tag{14}
\]

Equation (14) counts the selected squared optical velocity attached to thermally occupied upper electrons and lower holes, per normalization volume.

Although individual row and column strengths can redistribute under rotations inside an exactly degenerate eigenspace, Eq. (14) is invariant because all states in that eigenspace have the same Fermi occupation.

The pointwise Fermi inequality contributes an energy-dependent conversion factor when it is inserted into Kubo-Greenwood. We name that factor the **thermal kernel** because it weights each optical transition according to the minimum Fermi occupation cost allowed at its energy:

\[
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
\tag{15}
\]

This kernel is not introduced phenomenologically; it is the exact energy factor inherited from Eq. (9).

The reason for the next step is to turn the statewise statistical statement into a spectral-response statement that can be integrated over an arbitrary optical window. Multiplying Eq. (9) by \(|v_{cv}|^2\), summing over \(\mathcal T_{\mathcal B}\), and using Eq. (6) gives the first theorem,

\[
\boxed{
\mathcal R_{\mathcal B}(T)
\ge
\frac{2}{\pi e^2}
\int_{\mathcal B}
K_T(\hbar\omega)
\sigma_1^{\rm cross}(\omega)\,d\omega .
}
\tag{16}
\]

Equation (16) says that the thermally weighted selected velocity strength must be at least as large as the measured cross-\(\mu\) optical spectral weight after the exact Fermi thermal kernel is applied.

Equation (16) contains no maximum-velocity or density-of-states approximation. The remaining problem is different: \(\mathcal R_{\mathcal B}\) is a velocity-weighted quantity, whereas the desired theorem is a population bound. We therefore need to limit how much selected velocity strength one energy shell can carry.

### A. Basis-invariant shell optical-velocity capacity

A transition-by-transition maximum \(\max|v_{cv}|\) is not sufficient in a degenerate multiband problem. A whole degenerate shell can couple coherently to several partner directions, and the physically meaningful bound must be invariant under basis rotations inside that shell. The **optical-velocity capacity** is introduced to quantify the maximum selected velocity strength that one exact energy shell can supply after all such internal superpositions are allowed.

Let \(P_\epsilon\) project onto the complete exact eigenspace at one-particle energy \(\epsilon\). For an upper shell \(\epsilon_c>\mu\), the first object selects all lower-shell partners that lie in the chosen optical window:

\[
Q^-_{\epsilon_c,\mathcal B}
=\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_v}.
\tag{17}
\]

The corresponding projected optical coupling block is

\[
A_{\epsilon_c,\mathcal B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,\mathcal B}.
\tag{18}
\]

Equations (17) and (18) collect every selected lower partner of one exact upper energy shell into a single basis-independent operator block.

For a lower shell \(\epsilon_v<\mu\), define the analogous selected upper partner space

\[
Q^+_{\epsilon_v,\mathcal B}
=\sum_{\substack{\epsilon_c>\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in\mathcal B}}
P_{\epsilon_c},
\tag{19}
\]

and the corresponding lower-shell coupling block

\[
B_{\epsilon_v,\mathcal B}
=Q^+_{\epsilon_v,\mathcal B}\hat v_iP_{\epsilon_v}.
\tag{20}
\]

The capacity is then the largest squared operator norm of any selected upper- or lower-shell block:

\[
\boxed{
\left(v_{\mathcal B}^{\rm cap}\right)^2
=
\max\!\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,\mathcal B}\|_{\rm op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,\mathcal B}\|_{\rm op}^2
\right].
}
\tag{21}
\]

Equation (21) is the maximum selected optical-velocity strength available from one exact degenerate shell after all allowed superpositions within that shell are included. It is the resource that prevents a single shell from carrying unlimited selected spectral weight.

The operator norms maximize only over superpositions inside one exactly degenerate energy eigenspace; states at distinct energies are not coherently mixed. This restriction is essential to the physical meaning of the shell construction.

All inequalities up to this point are finite-system statements. A finite-system bound does not automatically produce a nonzero macroscopic density floor: the per-shell capacity could, in principle, grow with system size. For a thermodynamic sequence \(V_j\to\infty\) and fixed spectral window \(\mathcal B\), a nonzero density floor therefore requires the explicit uniform-capacity hypothesis

\[
\boxed{
\bar v_{\mathcal B}^{\rm cap}
\equiv
\limsup_{j\to\infty}v_{\mathcal B,V_j}^{\rm cap}<\infty.
}
\tag{22}
\]

Equation (22) says that the optical strength available from any one selected shell must remain bounded as the system becomes macroscopic; finite capacity at every finite \(V\) is not enough if that capacity itself diverges with \(V\).

Under Eq. (22), the density inequalities below survive the thermodynamic limit with \(v_{\mathcal B}^{\rm cap}\) replaced by \(\bar v_{\mathcal B}^{\rm cap}\). For readability we retain the shorter symbol \(v_{\mathcal B}^{\rm cap}\) when no ambiguity arises.

In the equal-mass parabolic intuition anchor, this capacity step is also saturated: each selected one-to-one block has nonzero singular values equal to the same \(v_0\). The general operator definition in Eq. (21) is what remains when that simple pairing structure is absent.

### B. Optically active thermal population

The capacity bounds optical strength per active one-body direction, so the proof next needs to count how many independent directions actually support the selected coupling. The relevant quantity is not an oscillator-strength-weighted participation ratio. It is the exact support dimension of each selected coupling block, weighted by the thermal occupation of its parent shell.

Define the selected support ranks

\[
r^+_{\epsilon_c,\mathcal B}
=\operatorname{rank}A_{\epsilon_c,\mathcal B},
\qquad
r^-_{\epsilon_v,\mathcal B}
=\operatorname{rank}B_{\epsilon_v,\mathcal B}.
\tag{23}
\]

Equation (23) counts the number of independent upper- or lower-shell directions on which the selected optical block has nonzero support.

All ranks are finite-system ranks before the thermodynamic limit and are invariant under unitary changes of basis within an exact degenerate shell.

The corresponding **optically active thermal populations** count those support dimensions with their equilibrium Fermi weights. Define

\[
\boxed{
n_{e,\mathcal B}^{\rm act}
=\frac1V
\sum_{\epsilon_c>\mu}f(\epsilon_c)r^+_{\epsilon_c,\mathcal B},
}
\tag{24}
\]

\[
\boxed{
n_{h,\mathcal B}^{\rm act}
=\frac1V
\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]r^-_{\epsilon_v,\mathcal B}.
}
\tag{25}
\]

Equations (24) and (25) are the thermal electron and hole populations carried by the one-body support subspaces that participate in the selected optical window.

These quantities count the support dimension of the selected optical coupling blocks, weighted by thermal occupation. They are not oscillator-strength-weighted participation ratios. Because exact rank changes discontinuously when a singular value passes through zero, \(n_{\mathcal B}^{\rm act}\) is a mathematical support-dimension construct rather than a robust experimentally inferred “number of participating carriers.” The total-population corollary below does not require that interpretation.

Since each selected rank is at most the dimension of its parent eigenspace,

\[
n_{e,\mathcal B}^{\rm act}\le n_e,
\qquad
n_{h,\mathcal B}^{\rm act}\le n_h,
\tag{26}
\]

where \(n_e=V^{-1}\sum_cp_c\) and \(n_h=V^{-1}\sum_vh_v\).

Equation (26) says only that restricting to optically active support cannot create more thermal population than exists in the full upper- and lower-\(\mu\) excitation spaces.

The final algebraic step closes the state-reuse loophole quantitatively. Regrouping Eq. (14) by exact energy shell gives traces of \(AA^\dagger\) and \(B^\dagger B\). For any operator \(X\),

\[
\operatorname{Tr}(XX^\dagger)
\le
\|X\|_{\rm op}^2\operatorname{rank}X.
\tag{27}
\]

Equation (27) states that the total squared coupling in a block cannot exceed its largest singular-value squared times the number of nonzero singular directions.

Applying Eq. (27) shell by shell therefore gives

\[
\boxed{
\mathcal R_{\mathcal B}(T)
\le
\left(v_{\mathcal B}^{\rm cap}\right)^2
\left(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act}\right).
}
\tag{28}
\]

Equation (28) converts the thermally weighted velocity-strength resource into a population quantity: finite optical-velocity capacity limits how much selected response each thermally occupied active direction can carry.

Combining the lower bound on \(\mathcal R_{\mathcal B}\) from Eq. (16) with the upper bound from Eq. (28) gives the central result,

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
\tag{29}
\]

Equation (29) says that surviving direct cross-\(\mu\) optical spectral weight imposes a minimum equilibrium thermal population on the one-body subspaces carrying that response, and the full thermal excitation population can only be larger.

For an intrinsic neutral semiconductor, one additional condition is required before the two-sided population can be reduced to a one-species density. The chemical potential must lie in a gap so that the lower/upper-\(\mu\) partition coincides with the valence/conduction manifolds. Under that condition charge neutrality gives \(n_e=n_h\equiv n_{\rm th}\), and Eq. (29) implies

\[
\boxed{
n_{\rm th}
\ge
\frac{1}{\pi e^2\left(v_{\mathcal B}^{\rm cap}\right)^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega .
}
\tag{30}
\]

Equation (30) is the one-species intrinsic-gap corollary: under the stated gap and neutrality conditions, the same optical integral directly lower-bounds the intrinsic thermal electron density, with an equal hole density.

Equation (29), rather than Eq. (30), is the general statement when \(\mu\) lies inside a nominal band. A global all-frequency statement is a special case only when the corresponding global selected shell capacity is finite. A bounded physical velocity operator is sufficient but not necessary; a selected cross-band block can remain bounded even if unrelated high-energy or intraband velocities do not. For macroscopic density statements, the uniform condition in Eq. (22) is essential: finite capacity at each finite \(V\) is not enough if that capacity itself diverges with system size.

---

## IV. Low-energy consequence

The central inequality is windowed, so the low-energy question must be posed with explicit control of how the window, its integrated spectral weight, and the capacity behave together. This section makes those quantifiers explicit; it does not infer a low-energy floor from the transition energy alone.

The thermal kernel has the expansion

\[
K_T(E)=2k_BT-\frac{E}{2}+O(E^2/k_BT).
\tag{31}
\]

Equation (31) shows why the low-energy limit is nontrivial: the kernel approaches the finite value \(2k_BT\) rather than vanishing with the photon energy.

To state the limit without exchanging hidden quantifiers, consider a sequence of windows \(\mathcal B_m\). The first requirement is that the entire selected window move to low transition energy,

\[
E_m\equiv\sup_{\omega\in\mathcal B_m}\hbar\omega\longrightarrow0.
\tag{32}
\]

Equation (32) specifies the low-energy limit itself; it says nothing yet about how much useful optical spectral weight survives.

The second requirement is that the selected integrated cross-\(\mu\) spectral weight remain nonzero,

\[
W_m\equiv
\int_{\mathcal B_m}\sigma_1^{\rm cross}(\omega)d\omega
\longrightarrow W_0>0.
\tag{33}
\]

Equation (33) is essential because a peak response can remain large while its integrated weight vanishes if the useful bandwidth collapses.

The third requirement controls the optical resource over both limits. The capacity must remain uniformly bounded not only as \(V\to\infty\) for each window, but also across the entire moving-window sequence:

\[
\boxed{
v_*\equiv
\sup_m\left[
\limsup_{V\to\infty}v_{\mathcal B_m,V}^{\rm cap}
\right]<\infty.
}
\tag{34}
\]

Equation (34) excludes an escape in which progressively lower-energy windows are supported by an optical-velocity capacity that itself diverges.

Because \(K_T(E)\to2k_BT\) uniformly on a shrinking low-energy window, Eq. (29) then gives the nonzero floor

\[
\boxed{
\liminf_{m\to\infty}
\left(n_{e,\mathcal B_m}^{\rm act}+n_{h,\mathcal B_m}^{\rm act}\right)
\ge
\frac{4k_BT}{\pi e^2v_*^2}W_0>0.
}
\tag{35}
\]

Equation (35) says that low transition energy, finite nonvanishing integrated direct cross-\(\mu\) spectral weight, and a uniformly bounded per-shell optical capacity cannot coexist with a vanishing active thermal population within the stated independent-quasiparticle direct-transition class.

The total excitation population is at least as large. The integrated-weight condition is essential: a requirement only on the peak conductivity of a line whose useful bandwidth tends to zero does not impose a finite population floor because its integrated spectral weight can vanish.

The conclusion is therefore conditional and precise. Lowering transition energy together with finite integrated direct cross-\(\mu\) spectral weight and a capacity uniformly bounded over both system size and the moving-window sequence forbids the active thermal population from vanishing. Band engineering may evade the floor by increasing the capacity itself, by allowing the integrated selected spectral weight to shrink, or by leaving the independent-quasiparticle direct-transition class.

The equal-mass parabolic intuition anchor realizes the opposite extreme: it does not evade any hypothesis and instead saturates the statistical and capacity steps. The next section verifies that equality explicitly before testing less symmetric models.

---

## V. Equality and quantitative validation

The theorem is exact but resource-conditioned, so validation must answer two separate questions. First, can the inequality be tight rather than merely formal? Second, does it remain quantitatively nontrivial when the ideal symmetry assumptions are relaxed? The parabolic and Dirac families address the first question analytically, while the HgCdTe calculations anchor the capacity and full bound in a realistic narrow-gap multiband model.

### A. Mirror-symmetric parabolic direct bands

We begin with the running intuition anchor because it exposes where equality can occur in every proof step. Consider ideal three-dimensional direct-gap bands

\[
E_c(k)=\frac{E_g}{2}+\frac{\hbar^2k^2}{2m_e},
\qquad
E_v(k)=-\frac{E_g}{2}-\frac{\hbar^2k^2}{2m_h},
\tag{36}
\]

with vertical transitions and a constant one-to-one optical velocity matrix element \(|v_{cv}|=v_0\).

Equation (36) provides a transparent test family: mass symmetry controls mirror symmetry about \(\mu\), while the one-to-one constant matrix element removes any ambiguity in the per-shell optical capacity.

For \(m_e=m_h\), intrinsic neutrality gives \(\mu=0\), and every vertical transition is mirror symmetric. For any selected direct-transition window \(\mathcal B\), the pointwise Fermi inequality saturates and every selected shell coupling block has all nonzero singular values equal to \(v_0\). Hence

\[
\boxed{
(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act})_{\rm bound}
=
(n_{e,\mathcal B}^{\rm act}+n_{h,\mathcal B}^{\rm act})_{\rm exact}
}
\tag{37}
\]

at all temperatures within this ideal model.

Equation (37) shows that the active-subspace theorem can be exactly saturated in every selected spectral window; the inequality is not intrinsically loose.

The **total-population** inequality in Eq. (29) is exactly saturated only when the selected window covers the full relevant direct spectrum of this ideal effective two-band optical model. For a partial window, thermally occupied states outside the selected optical graph make \(n_e+n_h\) strictly larger than the active population. No claim is made that parabolic bands with a constant interband matrix element define an ultraviolet-complete semiconductor Hamiltonian over an unbounded spectrum. The finite-window equality construction is the physically local statement.

To see how asymmetry degrades tightness, take unequal masses. In the nondegenerate limit, using the global direct spectrum gives

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
\tag{38}
\]

Equation (38) quantifies the loss of tightness caused by electron-hole mass asymmetry: the bound is exact at equal mass and decreases continuously as the two density-of-states scales separate.

At \(E_g/k_BT=4.7959\), exact finite-temperature evaluation gives total-population ratios \(0.9161\), \(0.6455\), and \(0.4379\) for \(m_h/m_e=2,5,\) and \(10\), respectively. The equal-mass global model remains exactly saturated. The favorable role of reducing electron-hole asymmetry is established semiconductor-optics physics [13]. The point here is the inverse spectral-weight inequality and its equality structure.

### B. Dirac systems

The parabolic family proves exact saturation is possible, but it does not test a qualitatively different dispersion. Dirac models provide an independent check in which the optical matrix structure and density of states differ substantially from the parabolic case.

For neutral two-dimensional massless Dirac quasiparticles, the two-dimensional form of the theorem uses sample area and sheet conductivity. Exact finite-temperature interband sheet conductivity [14,15] inserted into the global theorem gives

\[
n_e^{\rm bound}
=\frac{\pi}{12}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
\qquad
n_e^{\rm exact}
=\frac{\pi}{6}
\left(\frac{k_BT}{\hbar v_F}\right)^2.
\tag{39}
\]

Equation (39) shows that the theorem recovers one half of the exact thermal electron areal density in neutral two-dimensional massless Dirac systems. The corresponding global ratio is \(2/3\) for an isotropic three-dimensional massless Dirac cone [16].

For the gapped three-dimensional massive-Dirac dispersion

\[
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2},
\tag{40}
\]

using the finite-temperature conductivity and exact carrier density [16,17] gives

\[
\boxed{
\frac{(n_e+n_h)_{\rm bound}}
{(n_e+n_h)_{\rm exact}}
=0.794684
}
\tag{41}
\]

at \(2\Delta/k_BT=4.7959\), corresponding to a \(10\ \mu\mathrm m\) gap at \(300\ \mathrm K\).

Equation (41) shows that the bound remains quantitatively strong in a gapped three-dimensional Dirac model at a representative LWIR thermal scale.

| Model | Bound/exact |
|---|---:|
| 2-D neutral massless Dirac | 0.5000 |
| 3-D massless Dirac | 0.6667 |
| 3-D massive Dirac, \(\Delta/k_BT=2.398\) | 0.7947 |
| 3-D parabolic, \(m_h/m_e=2\) | 0.9161 |
| 3-D parabolic, \(m_h=m_e\) | 1.0000 |

**Table I.** Representative tightness checks for the global total-population corollary.

For the massive-Dirac family the ratio approaches unity as \(\Delta/k_BT\) increases, consistent with increasing concentration of thermally active optical states near mirror-symmetric band edges.

### C. HgCdTe \(8\times8\) Kane-model capacity

The preceding checks use models in which the optical resource is analytically transparent. The theorem, however, treats \(v_{\mathcal B}^{\rm cap}\) as an independent microscopic input, so its physical scale and thermodynamic boundedness must also be demonstrated in a realistic multiband narrow-gap Hamiltonian.

A useful test is the standard first-order \(8\times8\) Kane Hamiltonian used for bulk HgCdTe optical calculations [4]. In this model the velocity operator is linear and bounded, which lets us derive a size-independent capacity ceiling directly from the microscopic Hamiltonian. Write its \(x\)-polarized velocity operator as

\[
\hat v_x
=\frac{1}{\hbar}\frac{\partial H_K}{\partial k_x}
=v_KM_x.
\tag{42}
\]

Equation (42) separates the material-scale Kane velocity \(v_K\) from the dimensionless matrix structure that determines the operator norm.

In the published Kane basis, \(M_x\) separates into two weighted-star blocks. In either block the squared couplings sum to

\[
\frac34+\frac14+\frac12=\frac32,
\tag{43}
\]

so the nonzero eigenvalues of \(M_x\) are \(\pm\sqrt{3/2}\) (twofold).

Equation (43) fixes the exact first-order matrix norm rather than estimating it from a single pairwise transition.

Hence

\[
\boxed{
\|\hat v_x\|_{\rm op}
=\sqrt{\frac32}\,v_K,
\qquad
v_{\mathcal B}^{\rm cap}\le\sqrt{\frac32}\,v_K
}
\tag{44}
\]

for every selected optical window.

Equation (44) supplies a microscopic, volume-independent upper bound on the selected per-shell capacity in the first-order Kane model. Because the right-hand side is independent of volume and wave vector, it automatically satisfies the uniform thermodynamic hypothesis in Eq. (22) within this model.

Using the conventional Kane energy \(E_P=2m_0P^2/\hbar^2\) and \(v_K^2=E_P/(3m_0)\), Eq. (44) can also be written

\[
\boxed{
v_{\mathcal B}^{\rm cap}
\le\frac{P}{\hbar}
=\sqrt{\frac{E_P}{2m_0}}.
}
\tag{45}
\]

Equation (45) expresses the same first-order capacity ceiling in the standard Kane matrix-element notation.

HgCdTe magneto-optical measurements find an approximately composition- and temperature-independent \(v_K=(1.07\pm0.05)\times10^6\ \mathrm{m/s}\) near the topological transition, consistent with the standard \(E_P\simeq18.8\ \mathrm{eV}\) [5]. Equation (44) therefore supplies a first-order upper bound of about \(1.31\times10^6\ \mathrm{m/s}\) from the measured central velocity, or \(1.286\times10^6\ \mathrm{m/s}\) from \(E_P=18.8\ \mathrm{eV}\). It is not an assertion that every selected optical window attains that global operator norm. Thus the velocity-capacity resource is not merely formal in a standard narrow-gap multiband Hamiltonian.

The exact coefficient in Eq. (44) belongs to the first-order Kane model. Higher-order \(8\times8\ k\cdot p\) terms add \(k\)-dependent contributions to the velocity operator. On a finite spectral window within a bounded momentum domain where the \(k\cdot p\) expansion is used, those terms still define a finite microscopic selected capacity, but they do not preserve the first-order \(\sqrt{3/2}\) ceiling [6,8].

### D. Second-order HgCdTe bound/reference test

The first-order calculation proves that a realistic multiband model can satisfy the capacity hypothesis, but it does not test the complete population inequality. We therefore next evaluate the capacity, thermally weighted optical sum, and cross-\(\mu\) reference population together in a second-order eight-band model. This is the end-to-end significance test of the theorem in a strongly asymmetric narrow-gap system.

We use the bulk constant-parameter limit of the second-order eight-band model of Novik et al. [6]. For a representative \(300\ \mathrm K\), \(10\ \mu\mathrm m\) gap (\(E_g=0.123984\ \mathrm{eV}\)), the empirical gap relation used in that model gives \(x=0.17973\) [6,7]. We linearly interpolate the remote-band parameters between the HgTe and CdTe endpoints tabulated in Ref. 6, giving \(\Delta=1.04945\ \mathrm{eV}\), \(F=-0.01618\), \(\gamma_1=3.6273\), \(\gamma_2=0.3598\), and \(\gamma_3=1.0717\), with \(E_P=18.8\ \mathrm{eV}\). This interpolation is a representative modeling choice, not a claim of a unique measured \(300\ \mathrm K\) parameter set.

The carrier integral is restricted to \(|k|\le2.0\ \mathrm{nm^{-1}}\). Conventional charge neutrality, evaluated between the two \(\Gamma_6\)-derived branches and the six \(\Gamma_8/\Gamma_7\)-derived branches of the model, gives a chemical potential \(11.5\ \mathrm{meV}\) above the nominal \(\Gamma_6\) edge, reflecting the large valence/heavy-hole density of states. Because \(\mu\) therefore lies inside the nominal conduction manifold, the theorem's cross-\(\mu\) population is not mathematically identical to conventional conduction-electron plus valence-hole counting.

The numerically converged cross-\(\mu\) reference population is

\[
\boxed{
(n_e+n_h)_{\rm ref}=1.005\times10^{17}\ \mathrm{cm^{-3}}.
}
\tag{46}
\]

Equation (46) is the denominator appropriate to the general cross-\(\mu\) theorem for this model, not an “exact” material carrier density.

The conventional electron-plus-hole total is \(1.010\times10^{17}\ \mathrm{cm^{-3}}\), a \(0.5\%\) difference. Accordingly, the HgCdTe calculation tests the general hierarchy in Eq. (29), not the intrinsic-gap corollary in Eq. (30).

For reproducibility, let \(E_{n\mathbf k}\) and \(|n\mathbf k\rangle\) denote the eight eigenpairs and \(f_{n\mathbf k}=f(E_{n\mathbf k})\). The first numerical object is the reference thermal population itself. It counts Fermi-occupied exact states above \(\mu\) and holes below \(\mu\) throughout the stated bounded momentum domain \(\mathcal K\):

\[
\boxed{
n_\mu^{\rm ref}
=\sum_n\int_{\mathcal K}\frac{d^3k}{(2\pi)^3}
\left[
f_{n\mathbf k}\Theta(E_{n\mathbf k}-\mu)
+(1-f_{n\mathbf k})\Theta(\mu-E_{n\mathbf k})
\right].
}
\tag{47}
\]

Equation (47) makes explicit that the reference population follows the theorem's exact lower/upper-\(\mu\) partition rather than a nominal band-label partition.

The second numerical object is the thermally weighted transition sum that corresponds directly to the optical integral in Eq. (29). Evaluating it before any linewidth broadening avoids introducing a phenomenological lineshape into the theorem test:

\[
\boxed{
S_{\mathcal B}
=\sum_{nm}\int_{\mathcal K}\frac{d^3k}{(2\pi)^3}
(f_{n\mathbf k}-f_{m\mathbf k})|v^x_{mn}(\mathbf k)|^2
\frac{\chi_{\mathcal B}(E_{m\mathbf k}-E_{n\mathbf k})}
{e^{(E_{m\mathbf k}-E_{n\mathbf k})/(2k_BT)}-1}.
}
\tag{48}
\]

The sum in Eq. (48) is restricted to \(E_{n\mathbf k}<\mu<E_{m\mathbf k}\). The population lower bound is \(2S_{\mathcal B}/(v_{\mathcal B}^{\rm cap})^2\). Equation (48) is therefore the direct transition-sum implementation of the thermally weighted cross-\(\mu\) optical numerator.

The third numerical object is the capacity itself. This distinction is important: the theorem requires the largest singular value of the **full projected block**, not the largest individual pairwise matrix element. At each \(\mathbf k\), complete degenerate eigenspaces are grouped, all opposite-side partner eigenspaces satisfying the window criterion are assembled, and the largest singular value of the full projected block \(P_{\lambda\mathbf k}v_xQ_{\lambda\mathbf k,\mathcal B}\) and its lower-shell counterpart is computed. Translational invariance makes the full bulk operator block diagonal in \(\mathbf k\), so

\[
\boxed{
v_{\mathcal B}^{\rm cap}
=\operatorname*{ess\,sup}_{\mathbf k,\lambda}
 s_{\max}\!\left[P_{\lambda\mathbf k}v_x(\mathbf k)Q_{\lambda\mathbf k,\mathcal B}\right],
}
\tag{49}
\]

with the maximum also taken over the corresponding lower-shell blocks.

Equation (49) is the bulk specialization of the same projected-shell operator norm defined abstractly in Eq. (21); it is not a pairwise \(\max|v_{cv}|\) approximation.

The production calculation uses Gauss-Legendre quadrature in \(k\) and \(\cos\theta\), uniform azimuthal quadrature, and a \(10^{-7}\ \mathrm{eV}\) degeneracy-clustering tolerance for the model's exact twofold degeneracies.

| Window | \(v_{\mathcal B}^{\rm cap}\) (\(10^6\ \mathrm{m/s}\)) | Bound/reference | \(k_{\rm sel,max}\) (\(\mathrm{nm^{-1}}\)) |
|---|---:|---:|---:|
| \(E_g\)–\(1.5E_g\) | 1.017 | 0.0320 | 0.149 |
| \(E_g\)–\(2E_g\) | 1.017 | 0.0749 | 0.240 |
| \(E_g\)–\(3E_g\) | 1.015 | 0.1110 | 0.415 |
| \(E_g\)–\(0.5\ \mathrm{eV}\) | 1.016 | 0.1180 | 0.583 |

**Table II.** Second-order eight-band HgCdTe test at \(300\ \mathrm K\) and \(E_g=0.123984\ \mathrm{eV}\). The last column gives the largest momentum at which a selected cross-\(\mu\) transition occurs in the numerical quadrature.

Table II evaluates both the selected-shell capacity and the thermally weighted optical sum. The capacity stays nearly constant while the bound tightens as additional cross-\(\mu\) spectral weight is accumulated. Over the broad direct-transition validation window \(E_g\le E_{cv}\le0.5\ \mathrm{eV}\) we obtain

\[
\boxed{
v_{\mathcal B}^{\rm cap}\simeq1.02\times10^6\ \mathrm{m/s},
\qquad
\frac{(n_e+n_h)_{\rm bound}}{(n_e+n_h)_{\rm ref}}
\simeq0.118.
}
\tag{50}
\]

Equation (50) says that, over this broad validation window, the theorem recovers about \(11.8\%\) of the numerically converged cross-\(\mu\) reference population while using the full projected-block capacity required by the theorem.

The corresponding lower bound is \(1.19\times10^{16}\ \mathrm{cm^{-3}}\). Thus the heavy-hole and multiband asymmetry substantially loosen the constraint relative to the ideal parabolic and Dirac checks, but the bound remains order \(10^{-1}\) rather than numerically negligible. The \(0.5\ \mathrm{eV}\) interval is a model-validation window, not a proposed detector operating bandwidth.

The broad-window projected-block singular value is \(1.0156\times10^6\ \mathrm{m/s}\), whereas the largest individual pairwise matrix element is only \(0.8681\times10^6\ \mathrm{m/s}\). Replacing the projected-block norm by a pairwise maximum would therefore overstate the population lower bound by about \(37\%\). This numerical difference is why the basis-invariant block capacity is required rather than a simpler pairwise velocity maximum.

Varying the degeneracy-clustering tolerance from \(10^{-10}\) to \(10^{-5}\ \mathrm{eV}\) leaves the capacity unchanged to the reported precision at fixed quadrature. The selected \(0.5\ \mathrm{eV}\) window samples only \(|k|\le0.583\ \mathrm{nm^{-1}}\). The selected transitions connect the \(\Gamma_8\)-derived branches to the \(\Gamma_6\)-derived pair, while the \(\Gamma_7\)-derived split-off pair does not enter the selected set over this domain. Increasing the carrier cutoff from \(1.5\) to \(2.0\ \mathrm{nm^{-1}}\) changes the cross-\(\mu\) reference population by less than \(1\%\); denser radial/angular quadrature and optical-domain variations change the broad-window ratio only at the few-\(10^{-4}\) level.

These are convergence and branch-selection diagnostics inside the bounded-domain \(k\cdot p\) model. They are not a claim that the continuum expansion is valid to arbitrary momentum.

---

## VI. Relation to established theory

This section locates the result relative to established response and semiconductor theory. The purpose is not to reclassify known ingredients as new, but to identify the specific logical object bounded by Eq. (29).

### A. Phase-space filling

Phase-space filling provides the closest transition-level intuition. Semiconductor phase-space-filling theory computes how specified carrier occupations reduce optical absorption [9,10]. Equation (29) uses the same exclusion physics in the inverse direction.

The global step is not merely transitionwise inversion. The selected shell operator norm and support rank close the possibility that one thermally occupiable energy eigenspace supplies unlimited optical weight through many partners. Thus the theorem is a windowed state-count statement built from familiar Pauli blocking, not a claim that Pauli blocking itself is new.

### B. Optical sum rules

Optical sum rules also connect spectral weight to microscopic quantities, so the distinction in response moment and particle count matters. Conventional and generalized \(f\)-sum rules constrain conductivity moments through total charge density, kinetic energy, or Hamiltonian derivatives [11]. Quantum-geometric sums use different frequency moments to access Wannier spread or quantum metric [12]. Conductivity sum rules have also been used to infer electronic particle counts, for example the ionization degree of warm dense matter via the Thomas-Reiche-Kuhn sum rule [18].

Equation (29) instead uses the finite-temperature kernel in Eq. (15) and bounds thermal occupation of the optically active cross-\(\mu\) one-body subspaces. It is complementary to, rather than a replacement for, these established sum rules. The broad idea “conductivity spectral weight \(\rightarrow\) particle count” is therefore not a novelty claim here.

### C. Detailed balance and fluctuation-dissipation

The thermal kernel can invite comparison with other equilibrium response identities, but the target quantity is different. The van Roosbroeck-Shockley relation is the canonical semiconductor detailed-balance connection between optical absorption and radiative electron-hole recombination [2]. Its target is a radiative event-rate spectrum. Equations (29) and (30) instead bound the equilibrium one-body electron-hole population required to support a specified direct cross-\(\mu\) optical response, without converting that population into a recombination rate.

Likewise, fluctuation-dissipation theory relates dissipative linear response to equilibrium fluctuations of the conjugate observable [3]. The present inequality is not an FDT identity. It uses the statewise Fermi constraint in Eq. (9) plus a finite optical-coupling capacity to bound the thermal occupation of the underlying one-body support. These equilibrium relations therefore occupy adjacent but distinct logical levels.

### D. Low-carrier optical band engineering

The equality family has a familiar qualitative message, but that message predates the present theorem. The intuition that lighter and more symmetric electron-hole bands can reduce carrier requirements is old. Yablonovitch and Kane showed that lowering valence-band effective mass can reduce the injected carrier density and threshold current required for semiconductor lasing [13].

The parabolic equality family is consistent with that established direction. The candidate contribution here is the equilibrium inverse windowed spectral-weight inequality and its active-subspace state-count form, not the design slogan that symmetric bands are favorable.

### E. Infrared detector criteria

Infrared detector criteria commonly move one level further downstream by introducing a generation mechanism. The classic infrared material criterion \(\alpha/G_{\rm th}\) compares useful absorption with thermal generation [1]. Equations (29) and (30) lie upstream of any generation model: they constrain equilibrium populations of the states required to carry direct optical response.

There is no universal conversion from this population to a generation rate because recombination lifetime and detector collection/response time need not coincide. This is why Eq. (29) should not be read as a dark-current, generation-rate, or \(D^*\) theorem.

---

## VII. Scope and escape routes

The theorem is intentionally narrow. Each limitation below identifies either a physical mechanism outside the one-body direct-transition construction or a quantity that cannot be inferred from equilibrium state count alone.

**Neutral excitons and collective states.** A bound exciton can carry low-energy optical oscillator strength below the free electron-hole continuum while remaining electrically neutral. Photocurrent then requires a separate dissociation step. Such systems lie outside a theorem formulated in terms of independent free quasiparticle states. This does not mean excitonic absorbers are poor detectors; it means their optical response is not constrained by the present free-quasiparticle state-count theorem without an additional theory of dissociation.

**Indirect transitions.** Phonon-assisted absorption requires a joint electron-phonon transition amplitude rather than the direct one-body velocity graph in Eq. (6). The present \(\sigma_1^{\rm cross}\) therefore does not include indirect optical weight.

**Many-body broadening.** Static one-body disorder is allowed if exact eigenstates are used. Interaction-generated spectral functions and phenomenological lifetime broadening require a many-body generalization. The finite-width lines of an interacting spectral function should not be inserted into Eq. (6) as though they were exact one-body delta functions without that additional derivation.

**Localization and terminal current.** Localized optically active states still obey the population theorem but may contribute weakly to dc transport. No universal dark-current floor follows. The theorem counts equilibrium one-body excitation population, not terminal-current mobility or extraction probability.

**Finite-bandwidth noise.** A related inequality exists for independent-Fermi occupation variance, but kinetics determine how that variance is distributed in frequency. No universal readout-band noise floor follows. A population or variance bound does not by itself specify the detector's noise spectrum.

**Photonic enhancement.** The theorem constrains intrinsic electronic conductivity. Translating it to external absorptance depends on optical architecture; resonant, antenna, or slow-light enhancement spends additional electromagnetic resources. The theorem therefore does not prohibit a photonic structure from obtaining large external absorption from smaller intrinsic material spectral weight.

**Measured conductivity versus \(\sigma_1^{\rm cross}\).** The theorem does not apply to the full measured conductivity indiscriminately. Direct use of Eq. (29) requires either that the selected window be dominated by direct transitions crossing \(\mu\), so that \(\sigma_1\simeq\sigma_1^{\rm cross}\), or that a microscopic/spectral decomposition isolate the cross-\(\mu\) contribution from intraband, same-side interband, phonon-assisted, and excitonic response. This decomposition requirement is part of applying the theorem to experiment; it is not optional bookkeeping.

**Support-rank interpretation.** The active population is an exact support-dimension construct. An arbitrarily small but nonzero singular value changes the exact rank, so \(n_{\mathcal B}^{\rm act}\) should not be interpreted as a noise-robust experimental participation count. The total-population inequality remains valid independently of that interpretation.

**Vanishing useful bandwidth.** A peak-only detector requirement with arbitrarily small useful bandwidth can have arbitrarily small integrated spectral weight and therefore an arbitrarily weak population bound. The low-energy floor in Eq. (35) requires the nonvanishing integrated-weight condition in Eq. (33).

These escape routes delimit the theorem rather than weaken its internal statement. Within the direct independent-quasiparticle class, none of them changes Eq. (29); they identify situations in which the measured device response contains additional physics or resources not represented by its hypotheses.

---

## VIII. Conclusion

The argument can now be read as a sequence of three constrained conversions. The pointwise Fermi inequality converts surviving occupation difference into unavoidable endpoint thermal population. Kubo-Greenwood converts that local statement into a selected optical spectral-weight inequality. The projected-shell singular-value/rank bound then converts thermally weighted velocity strength into a count of thermally occupied optical-support dimensions.

For equilibrium independent quasiparticles, direct transitions crossing the chemical potential therefore obey the hierarchy in Eq. (29). The first inequality combines Fermi statistics, Kubo-Greenwood response, and a basis-invariant singular-value/rank capacity for each selected degenerate energy shell. The second states that the selected optical support subspaces are subsets of the full thermal excitation space.

Within the stated ideal optical model, mirror-symmetric equal-mass parabolic bands saturate the active-population inequality in any selected window. This equality case supplies the simplest physical picture of the theorem: mirror-symmetric endpoint placement minimizes the Fermi cost, while a one-to-one constant matrix element saturates the shell-capacity step. Mass-asymmetric parabolic and Dirac models then provide nontrivial independent checks away from that optimum.

The HgCdTe Kane examples further show that the optical-velocity capacity can be bounded by a standard microscopic multiband Hamiltonian. In the first-order \(8\times8\) model, \(v_{\mathcal B}^{\rm cap}\le\sqrt{3/2}\,v_K\) uniformly in system size. A second-order bounded-domain calculation evaluates the complete inequality and gives bound/reference ratios from \(3.2\%\) in the near-edge window to \(11.8\%\) over a broad direct-transition validation window. In that model the capacity changes little across the windows, so the tightening comes predominantly from accumulated cross-\(\mu\) spectral weight.

The low-energy statement is therefore conditional on three controlled quantities: nonvanishing integrated direct cross-\(\mu\) spectral weight, a per-shell optical capacity uniformly bounded over both the thermodynamic and moving-window limits, and the independent-quasiparticle direct-transition description. It does **not** say that a small band gap alone forces a large carrier density, and it does **not** say that every optical absorber must pay this free-quasiparticle population cost.

This is not a universal photodetector-performance limit. Recombination, collection, localization, neutral excitons, indirect absorption, many-body dynamics, useful spectral bandwidth, and photonic enhancement introduce independent resources. Within the stated class, however, the inequality isolates an optical-statistical state-count constraint without first choosing a density of states or recombination mechanism.

---

## Appendix A. Single-pass \(10\ \mu\mathrm m\) illustration

This appendix translates intrinsic electronic conductivity into a deliberately idealized single-pass absorption requirement. The purpose is only to show the numerical scale of the population bound under a simple optical boundary condition; it is not a universal conversion from external detector absorptance to intrinsic spectral weight.

For a weak-loss homogeneous absorber,

\[
\alpha(\omega)\simeq
\frac{\sigma_1^{\rm cross}(\omega)}{n_b\epsilon_0c}.
\tag{A1}
\]

Equation (A1) supplies the weak-loss material relation used for the illustration; it does not include arbitrary resonant path enhancement or entrance-interface loss.

At \(300\ \mathrm K\), take a \(10\ \mu\mathrm m\) absorption edge, \(n_b=3.5\), and require an internal single-pass absorptance \(A_{\rm int}\ge0.90\) over \(\mathcal B=[1.02\omega_g,1.10\omega_g]\). Here “internal” means absorptance of the power admitted into the absorber, equivalently ideal antireflection or index-matched entrance coupling. Fresnel entrance loss is not included.

For the idealized intrinsic-gap model assumed in this appendix, the chemical potential lies in the gap and Eq. (30) applies. This additional condition is what permits the total two-sided thermal population bound to be interpreted as an intrinsic electron-column bound. Exact thermal-kernel integration then gives the lower bounds in Table III.

| \(v_{\mathcal B}^{\rm cap}\) (m/s) | Minimum intrinsic electron column (cm\(^{-2}\)) |
|---:|---:|
| \(5.0\times10^5\) | \(2.88\times10^{12}\) |
| \(1.0\times10^6\) | \(7.20\times10^{11}\) |
| \(1.07\times10^6\) | \(6.29\times10^{11}\) |
| \(2.0\times10^6\) | \(1.80\times10^{11}\) |
| \(3.0\times10^6\) | \(8.00\times10^{10}\) |

**Table III.** Single-pass illustrative intrinsic electron-column bounds.

These values are only a material-dominant single-pass illustration. Using the first-order Kane upper bound from Eq. (44), \(v_{\mathcal B}^{\rm cap}\le1.31\times10^6\ \mathrm{m/s}\), gives the conservative illustrative lower column \(\Sigma_e\ge4.19\times10^{11}\ \mathrm{cm^{-2}}\). This does not assert that real bulk HgCdTe exactly realizes the idealized optical model; it anchors the capacity scale to an actual multiband narrow-gap Hamiltonian. Unconstrained photonic path enhancement changes the conversion from external absorptance to intrinsic material spectral weight.

---

## Appendix B. Secondary occupation-fluctuation corollary

The main theorem is a population constraint, not a finite-bandwidth noise theorem. A related statewise inequality can nevertheless constrain the total independent-Fermi occupation variance before any kinetic model distributes that variance over frequency.

For one crossing transition,

\[
D_{cv}
\le
\sinh\!\left(\frac{E_{cv}}{2k_BT}\right)
\left[p_c(1-p_c)+h_v(1-h_v)\right].
\tag{B1}
\]

Equation (B1) relates the same crossing-transition population difference to the sum of the independent-Fermi occupation variances of its two endpoint states.

Summing with the same selected optical resource yields a lower bound on total independent-Fermi one-body occupation variance. The statement is frequency integrated; a finite-bandwidth noise bound requires kinetic information and is not claimed here.

---

## References

[1] J. Piotrowski and W. Gawron, *Infrared Phys. Technol.* **38**, 63 (1997), doi:`10.1016/S1350-4495(96)00030-8`.

[2] W. van Roosbroeck and W. Shockley, *Phys. Rev.* **94**, 1558 (1954), doi:`10.1103/PhysRev.94.1558`.

[3] H. B. Callen and T. A. Welton, *Phys. Rev.* **83**, 34 (1951), doi:`10.1103/PhysRev.83.34`.

[4] J. D. Malcolm and E. J. Nicol, *Phys. Rev. B* **92**, 035118 (2015), doi:`10.1103/PhysRevB.92.035118`.

[5] F. Teppe *et al.*, *Nat. Commun.* **7**, 12576 (2016), doi:`10.1038/ncomms12576`.

[6] E. G. Novik, A. Pfeuffer-Jeschke, T. Jungwirth, V. Latussek, C. R. Becker, G. Landwehr, H. Buhmann, and L. W. Molenkamp, *Phys. Rev. B* **72**, 035321 (2005), doi:`10.1103/PhysRevB.72.035321`.

[7] J. P. Laurenti, J. Camassel, A. Bouhemadou, B. Toulouse, R. Legros, and A. Lusson, *J. Appl. Phys.* **67**, 6454 (1990), doi:`10.1063/1.345119`.

[8] P. Man and D. S. Pan, *Phys. Rev. B* **44**, 8745 (1991), doi:`10.1103/PhysRevB.44.8745`.

[9] D. Huang, J.-I. Chyi, and H. Morkoç, *Phys. Rev. B* **42**, 5147 (1990), doi:`10.1103/PhysRevB.42.5147`.

[10] N. H. Kwong, G. Rupper, and R. Binder, *Phys. Rev. B* **79**, 155205 (2009), doi:`10.1103/PhysRevB.79.155205`.

[11] H. Watanabe and M. Oshikawa, *Phys. Rev. B* **102**, 165137 (2020), doi:`10.1103/PhysRevB.102.165137`.

[12] L. F. Cárdenas-Castillo, S. Zhang, F. L. Freire, Jr., D. Kochan, and W. Chen, *Phys. Rev. B* **110**, 075203 (2024), doi:`10.1103/PhysRevB.110.075203`.

[13] E. Yablonovitch and E. O. Kane, *J. Lightwave Technol.* **4**, 504 (1986), doi:`10.1109/JLT.1986.1074751`.

[14] V. P. Gusynin and S. G. Sharapov, *Phys. Rev. B* **73**, 245411 (2006), doi:`10.1103/PhysRevB.73.245411`.

[15] V. P. Gusynin, S. G. Sharapov, and J. P. Carbotte, *Phys. Rev. B* **75**, 165407 (2007), doi:`10.1103/PhysRevB.75.165407`.

[16] C. J. Tabert, J. P. Carbotte, and E. J. Nicol, *Phys. Rev. B* **93**, 085426 (2016); **94**, 039901(E) (2016), doi:`10.1103/PhysRevB.93.085426`.

[17] C. J. Tabert and J. P. Carbotte, *Phys. Rev. B* **93**, 085442 (2016), doi:`10.1103/PhysRevB.93.085442`.

[18] M. Bethkenhagen *et al.*, *Phys. Rev. Research* **2**, 023260 (2020), doi:`10.1103/PhysRevResearch.2.023260`.
