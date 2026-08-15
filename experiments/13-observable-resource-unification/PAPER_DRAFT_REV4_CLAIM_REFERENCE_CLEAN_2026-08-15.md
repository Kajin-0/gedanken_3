# Spectral geometry of photodetection: optical state-count bounds, selectivity, and internal observability

**Unified manuscript — Rev. 4 (claim/reference-clean scientific draft)**  
**Date:** 2026-08-15  
**Status:** novelty-gate revision; not yet typeset for submission

---

## Abstract

Direct optical response constrains more than absorption alone: under a finite microscopic coupling capacity it can certify a minimum population of the one-body states that carry that response. We derive an equilibrium bound in which the selected direct cross-chemical-potential conductivity over an arbitrary frequency window lower-bounds the thermally occupied electron-plus-hole endpoint population through a basis-invariant exact-shell velocity capacity. We then show that this inverse bound is one realization of a more general detector relation. On a physically declared admissible domain, the strongest allowed response relative to the actual activity-ensemble average is exactly the reciprocal of the fraction of total activity certified by a maximum-capacity inversion. The maximally mixed limit gives a stable-rank task-selectivity relation; a rank-one coherent detector gives the full nonuniform coherence dimension `N_eff=1/sum_j w_j^2`. For dispersive bands, the optical population-bound tightness decomposes into Fermi asymmetry, shell-to-global capacity utilization, and inverse shell response selectivity. A production-resolution second-order eight-band HgCdTe calculation gives factors `0.3068` and `0.5726`, whose product `0.1757` reproduces the broad-window active-population tightness. Within the BIA-neglecting validation model the active exact-shell velocity blocks are singular-value isotropic by fixed-k `PT` symmetry; that exact isotropy is not asserted for full zincblende HgCdTe. Finally, we formulate terminal observability using channel-specific positive effects. Under independent conservative one-final-sink lineages, ideal endpoint counting can force zero interpixel cross-noise even with internal photon recycling, whereas finite-transit Shockley–Ramo motion can lift the source-channel null at finite frequency while preserving zero integrated charge for an internally created and recombined pair. The results connect inverse material inference, task/coherence selectivity, and terminal observability without proposing a replacement scalar figure of merit.

---

# I. Introduction

Photodetectors are commonly compared using scalar figures such as responsivity, quantum efficiency, noise-equivalent power, specific detectivity, bandwidth, dark current, or timing jitter. These quantities remain indispensable when the measurement protocol is specified. They are not, however, complete descriptions of how a detector couples arbitrary signal tasks, microscopic excitation channels, or internal dynamics to its terminals. Task-based imaging theory has long used matrices and information kernels rather than one scalar [1,2]; quantum photodetector theory represents measurement outcomes by positive effects and explicitly treats architecture-dependent performance tradeoffs [3,4]; semiconductor detector theory likewise distinguishes carrier fluctuations from the current induced through the terminal coupling problem [5,6].

We therefore do not propose a new generic measurement formalism. The narrower question is whether several photodetector limits that arise in different physical settings can be connected quantitatively once the full coupling map is retained.

The physical center of the present work is an inverse semiconductor theorem. For equilibrium independent quasiparticles, consider only direct optical transitions whose endpoints straddle the chemical potential. We show that finite selected optical conductivity cannot be supported by arbitrarily few thermally occupied endpoint states if the selected exact-shell velocity blocks have finite operator capacity. The resulting bound is upstream of recombination kinetics: it constrains the equilibrium one-body population required to carry a selected optical response, not dark current, generation rate, or detectivity. It is therefore distinct from the classic infrared material criterion `alpha/G_th` [7], semiconductor absorption/recombination detailed balance [8], and fluctuation-dissipation identities [9]. It is also distinct in response moment and target quantity from optical sum rules [10-14] and recent optical-response/quantum-geometry bounds [15,16].

Once this material theorem is expressed on an endpoint-lifted positive operator space, a broader structure becomes visible. A detector stage has a physically allowed maximum response per direction and an actual ensemble-average response. Their ratio is a forward selectivity. The same ratio is the reciprocal of how tightly the observed response can certify the ensemble's total activity when only the maximum per-direction capacity is retained. In a rank-one coherent detector this reproduces the effective coherence dimension `N_eff`; in the thermal semiconductor theorem it becomes the exact reciprocal of the optical velocity-capacity tightness. A shell-resolved form then identifies whether looseness comes from within-shell singular-value concentration or simply from shell-to-shell variation in absolute coupling strength.

A second information loss occurs downstream. Photon recycling can move an excitation between detector pixels without guaranteeing that the internal exchange appears in terminal noise. Photon recycling and mean optical crosstalk in HgCdTe photodiodes are established [17-20], as is the need for a proper Shockley–Ramo/corpuscular treatment of generation-recombination noise [5,6]. We show that, under a conservative independent-lineage final-sink model, the source terminal can be exactly null to a recycled lineage even while mean crosstalk and internal population correlations are nonzero. Finite-transit Shockley–Ramo current changes the terminal map and can lift that null at finite frequency.

The staged detector chain can be represented schematically as

```math
\mathcal H_{task}
\xrightarrow{M_{opt}}
\mathcal H_{exc}
\xrightarrow{M_{dyn}}
\mathcal H_{int}
\xrightarrow{M_{ro}(\omega)}
\mathcal H_{term}.
```

The maps in these spaces are physically different. The unity developed here is therefore not one universal matrix. It is the spectral geometry of the physically relevant map at the stage being interrogated: its spectral edge controls a capacity, its distribution of singular values controls directional selectivity, and its null space controls observability.

---

# II. Direct optical response bounds thermal endpoint population

## A. Exact Fermi endpoint inequality

Work first in finite volume with exact one-particle eigenstates. Let `|v>` and `|c>` satisfy

```math
E_v<\mu<E_c,
```

and define

```math
E_{cv}=E_c-E_v>0,
```

```math
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
```

and

```math
D_{cv}=f(E_v)-f(E_c).
```

The equilibrium Fermi occupations satisfy

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le
p_c+h_v.
}
\tag{1}
```

Equality occurs exactly when the two endpoint excitation energies are mirror symmetric about the chemical potential,

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
\tag{2}
```

Equation (1) is the statistical step of the theorem. The Bose-like denominator is not an assumed bosonic population; it is the optimized relation between two fermionic endpoint occupations at fixed transition energy.

## B. Selected cross-chemical-potential Kubo conductivity

For a physical velocity polarization `i`, define

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

Restrict the conductivity to selected direct transitions whose endpoints straddle `mu`. Using the positive-frequency Kubo-Greenwood convention,

```math
\boxed{
\sigma_1^{cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
}
\tag{3}
```

For any measurable positive-frequency window `B`, define

```math
\boxed{
K_T(E)=\frac{E}{e^{E/(2k_BT)}-1}.
}
\tag{4}
```

Multiplying Eq. (1) by the squared velocity matrix element and using Eq. (3) gives

```math
\boxed{
\mathcal R_B(T)
\ge
\mathcal L_B(T)
\equiv
\frac{2}{\pi e^2}
\int_BK_T(\hbar\omega)
\sigma_1^{cross}(\omega)d\omega.
}
\tag{5}
```

`R_B` is the exact thermally weighted squared-velocity strength of the selected transitions. No density of states, parabolic approximation, recombination model, or one-to-one transition pairing has entered Eq. (5).

The conductivity in Eq. (3) is a selected microscopic contribution. A measured total optical conductivity can also contain same-side-of-`mu` transitions, intraband response, phonon-assisted processes, excitons, or other channels and cannot be inserted into Eq. (5) without an appropriate decomposition or isolation of the selected contribution.

## C. Basis-invariant exact-shell capacity

A pairwise maximum `max|v_cv|` is not sufficient in a degenerate multiband problem because basis rotations inside an exact eigenspace redistribute individual matrix elements. Let `P_epsilon` project onto the complete exact eigenspace at energy `epsilon`.

For an upper endpoint shell define

```math
Q^-_{\epsilon_c,B}
=\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in B}}
P_{\epsilon_v},
```

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,B}.
\tag{6}
```

For a lower endpoint shell define

```math
Q^+_{\epsilon_v,B}
=\sum_{\substack{\epsilon_c>\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in B}}
P_{\epsilon_c},
```

```math
B_{\epsilon_v,B}
=Q^+_{\epsilon_v,B}\hat v_iP_{\epsilon_v}.
\tag{7}
```

The physically declared capacity domain is fixed by the cross-`mu` endpoint condition, the selected window `B`, the chosen velocity polarization, and exact-energy-shell basis freedom. Define

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
\tag{8}
```

The domain in Eq. (8) is part of the theorem. It cannot be enlarged by adding unrelated high-coupling states after the response is known.

For any selected finite-rank block `M`,

```math
Tr(MM^\dagger)
\le
\|M\|_{op}^2rank(M).
\tag{9}
```

Define the optically active thermal endpoint populations

```math
\boxed{
n_{e,B}^{act}
=\frac1V
\sum_{\epsilon_c>\mu}f(\epsilon_c)
rank(A_{\epsilon_c,B}),
}
\tag{10}
```

```math
\boxed{
n_{h,B}^{act}
=\frac1V
\sum_{\epsilon_v<\mu}[1-f(\epsilon_v)]
rank(B_{\epsilon_v,B}).
}
\tag{11}
```

Combining Eqs. (5), (8), and (9) yields

```math
\boxed{
 n_e+n_h
 \ge
 n_{e,B}^{act}+n_{h,B}^{act}
 \ge
 \frac{2}{\pi e^2(v_B^{cap})^2}
 \int_B
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
\tag{12}
```

Equation (12) is the principal physical theorem. It bounds equilibrium one-body endpoint population, not a recombination rate. The distinction from semiconductor detailed balance [8], fluctuation-dissipation theory [9], and infrared generation-based criteria [7] is therefore fundamental rather than notational.

---

# III. Endpoint-lifted spectral geometry and inverse certification

Equation (12) can be expressed as a positive activity pairing. This exposes a relation to forward detector selectivity.

## A. General admissible-domain reciprocity

Let `D` be a physically declared admissible domain for one detector stage, with projector `P_D`. Let

```math
G_D=P_DGP_D\succeq0,
```

```math
\lambda_D=\lambda_{max}(G_D)>0,
```

and let

```math
X\succeq0,
\qquad supp(X)\subseteq D,
\qquad TrX>0.
```

The actual ensemble-average response per unit activity is

```math
\bar q_X
=\frac{Tr(G_DX)}{TrX}.
\tag{13}
```

Define the strongest admissible response relative to that ensemble average,

```math
\boxed{
\mathcal S_{X|D}
=\frac{\lambda_D}{\bar q_X}
=\frac{\lambda_DTrX}{Tr(G_DX)}.
}
\tag{14}
```

The capacity inversion of the response certifies

```math
N_{cap}=rac{Tr(G_DX)}{\lambda_D},
```

so the certified fraction of the true activity is

```math
\boxed{
\tau_{X|D}
=\frac{Tr(G_DX)}{\lambda_DTrX}.
}
\tag{15}
```

Therefore

```math
\boxed{
\mathcal S_{X|D}\tau_{X|D}=1.
}
\tag{16}
```

Equation (16) is algebraically a normalized spectral-capacity identity; no novelty is claimed for the linear algebra. Its detector content is that Eq. (14) and Eq. (15) answer two independently meaningful questions about the same physical map: forward selectivity relative to the actual ensemble and inverse certification of the ensemble's total activity.

The direction attaining `lambda_D` need not be appreciably occupied in `X`. This is precisely why a maximum-capacity inverse bound can be loose.

If `Tr(G_DX)=0`, the activity lies in the observable null on its support and the certified fraction is zero.

## B. Endpoint-lifted thermal specialization

For the optical theorem construct

```math
\boxed{
G_B
=\bigoplus_{\epsilon_c>\mu}
A_{\epsilon_c,B}A_{\epsilon_c,B}^\dagger
\oplus
\bigoplus_{\epsilon_v<\mu}
B_{\epsilon_v,B}^\dagger B_{\epsilon_v,B}.
}
\tag{17}
```

The two sectors are both retained because Eq. (12) bounds electron-plus-hole endpoint population. Let `P_a^{act}` project onto the support of each endpoint block and define

```math
\boxed{
X_B^{act}
=\bigoplus_{\epsilon_c>\mu}
f(\epsilon_c)P_{\epsilon_c}^{act}
\oplus
\bigoplus_{\epsilon_v<\mu}
[1-f(\epsilon_v)]P_{\epsilon_v}^{act}.
}
\tag{18}
```

Then

```math
TrX_B^{act}/V=n_B^{act},
\qquad
Tr(G_BX_B^{act})/V=\mathcal R_B,
\tag{19}
```

and

```math
\lambda_{max}(G_B)=(v_B^{cap})^2.
\tag{20}
```

Thus

```math
\boxed{
\mathcal S_{th,B}^{act}
=\frac{(v_B^{cap})^2n_B^{act}}{\mathcal R_B},
}
\tag{21}
```

```math
\boxed{
\tau_{cap}^{act}
=\frac{\mathcal R_B}{(v_B^{cap})^2n_B^{act}},
}
\tag{22}
```

and

```math
\boxed{
\mathcal S_{th,B}^{act}\tau_{cap}^{act}=1.
}
\tag{23}
```

The observable conductivity step introduces the independent factor

```math
\boxed{
\eta_F=\mathcal L_B/\mathcal R_B\le1,
}
\tag{24}
```

so

```math
\boxed{
\tau_{obs}^{act}
=\eta_F\tau_{cap}^{act},
\qquad
\mathcal S_{th,B}^{act}\tau_{obs}^{act}=\eta_F.
}
\tag{25}
```

Equation (23) is the inverse-resource interpretation of the same spectral geometry used below in forward detector selectivity.

---

# IV. Forward selectivity: task and coherence limits

## A. Uniform task ensemble and stable rank

Let `D` be a `d`-dimensional task subspace and choose the uniform activity `X=I_D`. Define

```math
T=TrG_D,
\qquad
r_{st}=T/\lambda_D.
\tag{26}
```

Equation (16) becomes

```math
\boxed{
\mathcal S_{mix}=d/r_{st},
\qquad
\tau_{mix}=r_{st}/d.
}
\tag{27}
```

The equal-trace isotropic comparator is

```math
G_{iso}=(T/d)I_D.
```

The maximum task response advantage is

```math
\boxed{
\mathcal A_{max}
=\frac{\lambda_D}{T/d}
=d/r_{st}
=\mathcal S_{mix}.
}
\tag{28}
```

At fixed trace, selectivity cannot improve every direction. At least one orthogonal task satisfies

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{mix}}{d-1},
}
\tag{29}
```

or

```math
\boxed{
\mathcal L_{task}
\ge
\frac{\mathcal S_{mix}-1}{d-1}.
}
\tag{30}
```

The bound is tight when the remaining `d-1` eigenvalues are equal.

This task-space statement belongs to the established tradition of task-based detector/image assessment [1,2]. Its role here is to give the forward meaning of the same concentration factor. The separate transient unknown-arrival construction that motivated this work equalizes eventual event-specific matched-filter SNR for one selected waveform and adds a continuous correlated timing search; it is not assumed to be an equal-trace problem.

## B. Coherent bright-state detector

Consider a microscopic excited manifold with

```math
|B\rangle
=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
\qquad
\sum_jw_j=1.
\tag{31}
```

The photon-created state is

```math
\rho_\gamma=|B\rangle\langle B|,
```

while the population-matched incoherent internal state is

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
\tag{32}
```

Population-diagonal observables cannot distinguish the two. Let

```math
G_D=\Pi_B=|B\rangle\langle B|.
```

Then

```math
Tr(\Pi_B\rho_\gamma)=1,
```

```math
Tr(\Pi_B\rho_D)=\sum_jw_j^2.
\tag{33}
```

Applying Eq. (16) to `X=rho_D`,

```math
\boxed{
\mathcal S_{\rho_D|D}
=\frac1{\sum_jw_j^2}
\equiv N_{eff},
}
\tag{34}
```

```math
\boxed{
\tau_{\rho_D|D}=1/N_{eff}.
}
\tag{35}
```

The inverse participation form itself is familiar in coherence/collective-state physics [21-24]. The useful point here is its exact identification with the same forward/inverse response-capacity ratio that becomes Eq. (23) in the thermal semiconductor problem.

For this particular rank-one projector, there is also an independent quantum-measurement statement: any yes/no effect with unit acceptance of `|B>` must contain `|B>` as a unit-eigenvalue eigenvector, so the bright projector minimizes the accepted probability of `rho_D` under that unit-signal constraint. Thus `N_eff` is the actual conditional rejection factor in this construction, not merely a response ratio.

The result does not imply that coherence alone solves detector dark count. Dephasing, extraction, reverse injection, and finite-density kinetics remain separate resources [3,24-28].

---

# V. Dispersive decomposition of optical population-bound tightness

The global thermal reciprocity in Eq. (23) gives the average capacity slack but not its microscopic origin.

Index selected endpoint shells by `a`. Define

```math
\lambda_a=\|M_a\|_{op}^2,
```

```math
r_a=rank(M_a),
```

```math
r_{st,a}
=\frac{Tr(M_aM_a^\dagger)}{\lambda_a},
```

and the local active response-selectivity factor

```math
\boxed{
\mathcal S_a^{act}=r_a/r_{st,a}.
}
\tag{36}
```

Let

```math
\boxed{
c_a=\lambda_a/(v_B^{cap})^2}
\tag{37}
```

be the shell utilization of the global capacity, and let

```math
\boxed{
w_a^{act}=p_ar_a/\sum_bp_br_b}
\tag{38}
```

be the normalized thermal active-population weight.

Then

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
\tag{39}
```

Equivalently,

```math
\boxed{
\mathcal S_{th,B}^{act}
=
\left[
\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}
\right]^{-1}.
}
\tag{40}
```

The actual observable tightness is

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
\tag{41}
```

Equation (41) separates three distinct physical sources of looseness:

```text
thermal/Fermi asymmetry:                eta_F;
shell-to-global capacity mismatch:      c_a;
within-shell singular concentration:    1/S_a^act.
```

This decomposition is the principal new cross-branch diagnostic produced by the unified formulation. It is not an optical sum rule; it resolves the tightness of the independent-quasiparticle population theorem itself.

---

# VI. Production eight-band HgCdTe validation

We evaluate Eqs. (39)-(41) in the same second-order bulk eight-band Kane validation used for the 300-K, 10-um-class HgCdTe population theorem. The model follows the bulk constant-parameter limit of Novik et al. [29], uses the empirical gap relation of Laurenti et al. [30], and evaluates the physical velocity from the analytic derivative of the Hamiltonian. The standard HgCdTe Kane energy scale and magneto-optical velocity are consistent with the parameter range used here [29,31,32].

For the broad selected window

```text
E_g <= Delta E <= 0.5 eV,
```

the production quadrature gives

```text
mu                            = 0.1354615 eV
n_ref                         = 1.0051405e17 cm^-3
R_B                           = 3.9874202e28 cm^-3 (m/s)^2
L_B                           = 1.2234865e28 cm^-3 (m/s)^2
n_B^act                       = 6.7241114e16 cm^-3
v_B^cap                       = 1.01764e6 m/s.
```

Therefore

```math
\boxed{
\eta_F=0.30684,
\qquad
\tau_{cap}^{act}=0.57262,
\qquad
\tau_{obs}^{act}=0.17570.
}
\tag{42}
```

The factorization closes numerically,

```math
0.30684\times0.57262=0.17570.
\tag{43}
```

and the global thermal capacity selectivity is

```math
\boxed{
\mathcal S_{th,B}^{act}
=1/0.57262
\simeq1.746.
}
\tag{44}
```

The lower bound remains approximately `11.8%` of the full cross-`mu` reference population and `17.6%` of the selected active population.

## A. Why the active shell selectivity is exactly unity in the validation model

Every thermally important selected active shell satisfies

```math
\mathcal S_a^{act}=1
```

to machine precision; the maximum observed deviation is approximately `4e-14`.

This is symmetry enforced in the present model. The second-order Kane Hamiltonian used here omits explicit bulk-inversion-asymmetry/Dresselhaus terms. Within that approximation, inversion `P` and spinful time reversal `T` give an antiunitary

```math
\Theta=PT,
```

which leaves each bulk `k` fixed and satisfies `Theta^2=-1`. Generic endpoint shells are therefore twofold `Theta` doublets. Velocity is odd under `P` and odd under `T`, hence even under `PT`. In `Theta`-adapted bases, the velocity block between two doublets has quaternionic form

```math
\boxed{
M=
\begin{pmatrix}
a&b\\-b^*&a^*\end{pmatrix},
}
\tag{45}
```

so

```math
MM^\dagger=(|a|^2+|b|^2)I_2.
\tag{46}
```

The two nonzero singular values are equal. Concatenating selected partner doublets preserves Eq. (46), forcing `S_a^act=1` for the generic active endpoint blocks in this BIA-neglecting model.

Real HgCdTe has zincblende bulk inversion asymmetry. More complete eight-band models can include BIA terms [33], which can lift the exact fixed-k doublet/quaternionic relation. We therefore do **not** claim that real HgCdTe has universally isotropic active shell blocks. The population theorem itself does not rely on inversion symmetry; a BIA-inclusive calculation would simply require recomputation of the capacity, ranks, and shell factors.

Within the current validation model, Eq. (42) can therefore be interpreted particularly cleanly:

```text
within-shell singular anisotropy:     no contribution;
between-shell capacity variation:     0.57262;
Fermi/Kubo asymmetry:                  0.30684;
observable active tightness:           0.17570.
```

This explains the realistic theorem slack rather than merely reporting it.

---

# VII. Internal photon recycling and channel-specific observability

The preceding sections concern task or optical coupling. Downstream, the relevant question is whether an internal stochastic process survives the readout map.

## A. Terminal effects and cross-channel overlaps

At fixed angular frequency, let the internal innovation vector have positive spectral covariance

```math
\Sigma(\omega)\succeq0
```

and let

```math
\mathbf y=M(\omega)\boldsymbol\xi.
```

Then

```math
S_y=M\Sigma M^\dagger.
\tag{47}
```

For terminal `i`, define the positive channel effect

```math
\boxed{
G_i(\omega)
=M^\dagger|i\rangle\langle i|M
\succeq0.
}
\tag{48}
```

so

```math
\boxed{
S_{ii}=Tr[G_i(\omega)\Sigma].
}
\tag{49}
```

For channels `i` and `j`, define

```math
\boxed{
C_{ij}(\omega)
=M^\dagger|j\rangle\langle i|M,
}
\tag{50}
```

which need not be positive. Then

```math
\boxed{
S_{ij}=Tr(C_{ij}\Sigma).
}
\tag{51}
```

Whitening `Sigma` gives the usual spectral-coherence bound

```math
\boxed{
|S_{ij}|^2\le S_{ii}S_{jj}.
}
\tag{52}
```

If a positive internal sector `X` is null to channel `i`,

```math
Tr(G_iX)=0,
\tag{53}
```

then its cross contribution with every other channel is forced to vanish. Cross-noise requires joint visibility of the same internal sector.

## B. Conservative internal exchange can be strong

For two identical carrier reservoirs with local non-transfer relaxation `gamma`, conservative exchange rate `k`, and stationary mean population `m`, the internal occupancy cross-spectrum is

```math
\boxed{
S_{x,12}(\omega)
=m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
}
\tag{54}
```

It changes sign at

```math
\boxed{
\omega_x=\sqrt{\gamma(\gamma+2k)}.
}
\tag{55}
```

The internal populations are therefore dynamically correlated even though the equal-time cross covariance vanishes.

## C. Endpoint-counting null

Now assume:

```text
(i) Poisson primary generation;
(ii) independent noninteracting complete lineages;
(iii) one final sink per lineage;
(iv) the measurement records only the final sink event;
(v) no branching/gain that creates multiple recorded descendants;
(vi) no shared electronic coupling between channels.
```

A conservative lineage that begins in pixel A and ultimately exits through pixel B has ideal endpoint waveform

```math
\mathbf H_{A\to B}^{end}(\omega)
=g_B(\omega)\mathbf e_B.
\tag{56}
```

The lineage lies in the A-channel null. Independent marking, thinning, random displacement, and superposition of Poisson lineages therefore produce independent final-sink streams [34,35]. Consequently

```math
\boxed{
S_{AB}^{end}(\omega)=0
}
\tag{57}
```

for every frequency in the ideal endpoint model, despite nonzero mean recycling/crosstalk and nonzero internal occupancy correlations.

This result uses old stochastic-process mathematics; the detector-specific point is the distinction between conservative internal routing and final-sink terminal observability.

## D. Finite-transit Shockley–Ramo lifting of the source-channel null

A real junction can respond to carrier motion before final collection. Let `phi_i(r)` be the weighting potential of terminal `i`. For an electron-hole pair,

```math
\boxed{
 i_i(t)
 =e\frac{d}{dt}
 [\phi_i(\mathbf r_e(t))-\phi_i(\mathbf r_h(t))].
}
\tag{58}
```

The use of Shockley–Ramo coupling for detector impulse response and generation-recombination noise is established [5,6].

If a pair is created internally at one point and later recombines internally at a common point, the endpoint weighting-potential separation vanishes at both ends. Therefore

```math
\boxed{
Q_i^{rec}=\int i_i(t)dt=0
}
\tag{59}
```

for every electrode.

For

```math
H_i(\omega)=\int i_i(t)e^{-i\omega t}dt,
```

integration by parts gives

```math
\boxed{
H_i^{rec}(\omega)
=i\omega e
\int\Delta\phi_i(t)e^{-i\omega t}dt.
}
\tag{60}
```

Thus

```math
H_i^{rec}(0)=0,
\tag{61}
```

while an individual finite-transit trajectory can have nonzero finite-frequency support.

For the same A-to-B conservative recycling lineage,

```math
\mathbf H_{A\to B}^{Ramo}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}
\tag{62}
```

is a minimal localized-weighting-field representation. The A-channel null present in Eq. (56) can therefore be lifted for nonzero frequency. Once the lineage is visible to both channels, a nonzero cross contribution is permitted by Eq. (52).

This does not guarantee an experimentally nonzero ensemble cross-spectrum: symmetry, opposing lineages, weighting-field cancellation, and electronics may still suppress the overlap. The derived boundary is narrower:

```text
final-sink-only conservative readout
    -> one-lineage/one-terminal support and zero cross-noise;

finite-transit Ramo readout
    -> internally recombined source segment has zero DC area
       but can acquire finite-frequency terminal support.
```

The result is compatible with, rather than a replacement for, established photon-recycling models in HgCdTe photodiodes [17-20].

---

# VIII. Discussion

The common structure can be stated without introducing a new detector metric.

For a physically declared domain, the spectral edge `lambda_D` is the maximum admissible response per direction. The actual ensemble-average response is `Tr(G_DX)/TrX`. Their ratio is a forward selectivity. The inverse ratio is the fraction of total activity certified by the measured response when only the maximum capacity is used. Stable rank appears when the activity ensemble is maximally mixed; `N_eff` appears when the effect is a rank-one bright projector and the activity is a population-matched incoherent state; the thermal optical capacity tightness appears when the activity is the equilibrium endpoint population.

The principal semiconductor theorem contains an additional independent statistical step. The selected conductivity functional `L_B` is lower than the exact thermally weighted velocity strength `R_B` by the Fermi factor `eta_F`. The capacity step then relates `R_B` to the active endpoint population. The full observable tightness therefore factorizes into statistical and spectral contributions, and Eq. (41) resolves the latter shell by shell.

This perspective is complementary to established optical sum rules. Conventional and generalized sum rules constrain conductivity moments through charge density, kinetic energy, or Hamiltonian derivatives [10-14]; recent works connect optical moments to topology or quantum geometry [15,16]. Here the target is the equilibrium population of the one-body cross-`mu` endpoint support and the controlling microscopic resource is a selected exact-shell velocity capacity.

The downstream readout result illustrates a different kind of information loss. Internal recycling can be present yet be null to one terminal under a final-sink map. The readout operator, not the existence of the internal process, determines observability. This is consistent with classical GR-noise/Ramo theory [5,6] but produces a specific conditional statement for conservative photon-recycling lineages.

Several limitations should be kept explicit:

```text
- Eq. (12) requires a selected direct cross-mu conductivity contribution;
- the theorem is independent-quasiparticle and does not include arbitrary excitonic,
  phonon-assisted, or many-body optical response;
- it is an equilibrium population bound, not a dark-current or D* theorem;
- N_eff is an ideal coherent-state discrimination result and requires preserved/extractable coherence;
- the exact HgCdTe shell isotropy is a symmetry property of the BIA-neglecting validation model;
- endpoint Poisson cancellation fails for branching, correlated generation,
  interactions, or common electronics;
- finite-frequency Ramo support allows but does not guarantee an ensemble cross-spectrum.
```

The scientific contribution is therefore not that positive operators or singular values are new. It is the detector-specific cross-closure: an inverse optical state-count theorem, its relation to forward selectivity, its shell-resolved material diagnosis, and a downstream channel-null criterion for internal observability.

---

# IX. Conclusion

A selected direct optical response in an equilibrium semiconductor cannot be supported by arbitrarily few thermally populated one-body endpoint states when the exact-shell optical velocity blocks have finite capacity. The resulting lower bound, Eq. (12), is the principal physical theorem of this work.

Expressing that theorem on an endpoint-lifted positive activity space reveals a broader reciprocity. On any physically declared admissible domain,

```math
\boxed{
\frac{\lambda_D}{Tr(G_DX)/TrX}
\times
\frac{Tr(G_DX)}{\lambda_DTrX}
=1.
}
\tag{63}
```

The first factor is the maximum admissible response relative to the actual ensemble average; the second is the fraction of total activity certified by a maximum-capacity inversion. The maximally mixed limit gives stable-rank task selectivity, while the rank-one coherent specialization gives the full nonuniform `N_eff` rejection factor.

For dispersive semiconductor bands, Eq. (39) resolves the capacity tightness into within-shell selectivity and shell-to-global capacity utilization, with the independent Fermi/Kubo factor multiplying afterward. In the production BIA-neglecting eight-band HgCdTe validation, the selected active shells are singular-value isotropic by `PT` symmetry; the broad active-bound tightness `0.1757` is therefore explained by `0.5726` shell-capacity utilization and `0.3068` Fermi/Kubo efficiency rather than by within-shell bright-state concentration.

Finally, a downstream detector stage has its own positive terminal observability effects. Conservative photon recycling can be exactly null to a source terminal under ideal final-sink counting, while finite-transit Shockley–Ramo motion can lift that null at finite frequency despite zero integrated induced charge for an internally created and recombined pair.

The common result is not a replacement scalar for specific detectivity, responsivity, or noise. It is a spectral accounting principle for determining what a detector preferentially measures, what microscopic activity its measured response can certify, and what internal dynamics its readout can hide.

---

# References

[1] H. H. Barrett, J. L. Denny, R. F. Wagner, and K. J. Myers, “Objective assessment of image quality. II. Fisher information, Fourier crosstalk, and figures of merit for task performance,” *J. Opt. Soc. Am. A* **12**, 834–852 (1995), doi:10.1364/JOSAA.12.000834.

[2] E. Clarkson and F. Shen, “Fisher information and surrogate figures of merit for the task-based assessment of image quality,” *J. Opt. Soc. Am. A* **27**, 2313–2326 (2010), doi:10.1364/JOSAA.27.002313.

[3] S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Phys. Rev. A* **98**, 063835 (2018), doi:10.1103/PhysRevA.98.063835.

[4] H. Xu, F. Xu, T. Theurer, D. Egloff, Z.-W. Liu, N. Yu, M. B. Plenio, and L. Zhang, “Experimental Quantification of Coherence of a Tunable Quantum Detector,” *Phys. Rev. Lett.* **125**, 060404 (2020), doi:10.1103/PhysRevLett.125.060404.

[5] W. Dąbrowski, “Transport equations and Ramo's theorem: Applications to the impulse response of a semiconductor detector and to the generation-recombination noise in a semiconductor junction,” *Prog. Quantum Electron.* **13**, 233–266 (1989), doi:10.1016/0079-6727(89)90004-9.

[6] W. Dąbrowski, “Comments on the collective and corpuscular approach of generation-recombination noise in a p-n junction,” *Solid-State Electron.* **30**, 205–208 (1987), doi:10.1016/0038-1101(87)90150-X.

[7] J. Piotrowski and W. Gawron, *Infrared Phys. Technol.* **38**, 63 (1997), doi:10.1016/S1350-4495(96)00030-8.

[8] W. van Roosbroeck and W. Shockley, “Photon-Radiative Recombination of Electrons and Holes in Germanium,” *Phys. Rev.* **94**, 1558–1560 (1954), doi:10.1103/PhysRev.94.1558.

[9] H. B. Callen and T. A. Welton, *Phys. Rev.* **83**, 34 (1951), doi:10.1103/PhysRev.83.34.

[10] H. Watanabe and M. Oshikawa, *Phys. Rev. B* **102**, 165137 (2020), doi:10.1103/PhysRevB.102.165137.

[11] L. F. Cárdenas-Castillo, S. Zhang, F. L. Freire, Jr., D. Kochan, and W. Chen, *Phys. Rev. B* **110**, 075203 (2024), doi:10.1103/PhysRevB.110.075203.

[12] M. Bethkenhagen *et al.*, *Phys. Rev. Research* **2**, 023260 (2020), doi:10.1103/PhysRevResearch.2.023260.

[13] V. P. Gusynin and S. G. Sharapov, *Phys. Rev. B* **73**, 245411 (2006), doi:10.1103/PhysRevB.73.245411.

[14] V. P. Gusynin, S. G. Sharapov, and J. P. Carbotte, *Phys. Rev. B* **75**, 165407 (2007), doi:10.1103/PhysRevB.75.165407.

[15] Y. Onishi and L. Fu, “Fundamental Bound on Topological Gap,” *Phys. Rev. X* **14**, 011052 (2024), doi:10.1103/PhysRevX.14.011052.

[16] D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury, “Low-energy optical absorption in correlated insulators: Projected sum rules and the role of quantum geometry,” *Phys. Rev. B* **112**, 075116 (2025).

[17] K. Jóźwikowski, M. Kopytko, and A. Rogalski, “Numerical estimations of carrier generation-recombination processes and photon recycling effect in 3-μm n-on-p HgCdTe photodiodes,” *Opt. Eng.* **50**, 061003 (2011), doi:10.1117/1.3572167.

[18] K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon-recycling analysis of HgCdTe heterostructure photodiodes, *J. Electron. Mater.* **41**, 2766–2774 (2012), doi:10.1007/s11664-012-2093-7.

[19] A. Jóźwikowska and K. Jóźwikowski, “Numerical estimation of photon reabsorption process and optical crosstalk in arrays of HgCdTe photodiodes,” *Opt. Quantum Electron.* **51**, 85 (2019), doi:10.1007/s11082-019-1781-4.

[20] M. Kopytko *et al.*, “Photon recycling effect in small pixel p-i-n HgCdTe long wavelength infrared photodiodes,” *Infrared Phys. Technol.* **97**, 38–42 (2019), doi:10.1016/j.infrared.2018.12.015.

[21] C. W. Helstrom, *Quantum Detection and Estimation Theory* (Academic Press, New York, 1976).

[22] R. J. Glauber, “The Quantum Theory of Optical Coherence,” *Phys. Rev.* **130**, 2529 (1963), doi:10.1103/PhysRev.130.2529.

[23] R. H. Dicke, “Coherence in Spontaneous Radiation Processes,” *Phys. Rev.* **93**, 99 (1954), doi:10.1103/PhysRev.93.99.

[24] M. O. Scully and A. A. Svidzinsky, “The Super of Superradiance,” *Science* **325**, 1510–1511 (2009), doi:10.1126/science.1178417.

[25] V. May and O. Kühn, *Charge and Energy Transfer Dynamics in Molecular Systems*, 3rd ed. (Wiley-VCH, 2011).

[26] H. Haug and A.-P. Jauho, *Quantum Kinetics in Transport and Optics of Semiconductors*, 2nd ed. (Springer, 2008).

[27] C. W. Gardiner and P. Zoller, *Quantum Noise*, 3rd ed. (Springer, 2004).

[28] M. Esposito, U. Harbola, and S. Mukamel, “Nonequilibrium fluctuations, fluctuation theorems, and counting statistics in quantum systems,” *Rev. Mod. Phys.* **81**, 1665 (2009), doi:10.1103/RevModPhys.81.1665.

[29] E. G. Novik, A. Pfeuffer-Jeschke, T. Jungwirth, V. Latussek, C. R. Becker, G. Landwehr, H. Buhmann, and L. W. Molenkamp, *Phys. Rev. B* **72**, 035321 (2005), doi:10.1103/PhysRevB.72.035321.

[30] J. P. Laurenti, J. Camassel, A. Bouhemadou, B. Toulouse, R. Legros, and A. Lusson, *J. Appl. Phys.* **67**, 6454 (1990), doi:10.1063/1.345119.

[31] F. Teppe *et al.*, *Nat. Commun.* **7**, 12576 (2016), doi:10.1038/ncomms12576.

[32] P. Man and D. S. Pan, *Phys. Rev. B* **44**, 8745 (1991), doi:10.1103/PhysRevB.44.8745.

[33] X. Cartoixà, D. Z.-Y. Ting, and T. C. McGill, eight-band zincblende modeling with bulk-inversion-asymmetry terms, associated publication and arXiv:cond-mat/0212394. **[Production note: verify final journal citation before submission.]**

[34] A. Mirasol, Poisson output theorem for the `M/G/∞` queue, *Operations Research* **11**, 282 (1963), doi:10.1287/opre.11.2.282.

[35] J. M. Harrison and A. J. Lemoine, open networks of infinite-server queues, *J. Appl. Prob.* **18** (1981), doi:10.2307/3213306.

[36] D. Huang, J.-I. Chyi, and H. Morkoç, *Phys. Rev. B* **42**, 5147 (1990), doi:10.1103/PhysRevB.42.5147.

[37] N. H. Kwong, G. Rupper, and R. Binder, *Phys. Rev. B* **79**, 155205 (2009), doi:10.1103/PhysRevB.79.155205.

[38] E. Yablonovitch and E. O. Kane, *J. Lightwave Technol.* **4**, 504 (1986), doi:10.1109/JLT.1986.1074751.

---

**Rev. 4 production boundary.** All claims are now written to the narrow novelty boundary established by the extreme Rev. 3 audit. One bibliography item, Ref. 33, still requires exact journal-level verification. Before typesetting, perform a final reference verification pass, replace Ref. 33, and re-review the scientific text for claim/reference alignment. No new theory should be added by default unless that review uncovers a concrete gap.
