# Spectral geometry of photodetection: task selectivity, thermal state-count bounds, and hidden internal dynamics

**Unified manuscript — Rev. 0**  
**Date:** 2026-08-15  
**Status:** scientific-structure draft for hostile review; not submission formatted

---

## Abstract

Scalar photodetector figures of merit summarize selected operating conditions but do not retain the geometry of how a detector couples different optical tasks, microscopic excitations, and terminal observables. We develop a detector-specific spectral formulation that connects four questions usually treated separately. For a positive coupling or information operator `G` on a `d`-dimensional task space with fixed total strength `Tr G`, we show that the maximum task advantage over an equal-strength isotropic detector equals the coherent bright-state response advantage over a uniform incoherent excitation and is the reciprocal of the corresponding state-count capacity tightness. The same selectivity imposes a quantitative loss on at least one orthogonal task. We then derive a direct optical theorem in which cross-chemical-potential conductivity over an arbitrary frequency window gives a lower bound on the equilibrium population of the one-body states carrying that response, with a basis-invariant shell velocity capacity. For dispersive bands, the theorem tightness separates into Fermi asymmetry, shell-to-global capacity utilization, and inverse coherent selectivity. An eight-band 300-K HgCdTe calculation reconstructs the broad-window active-population tightness as approximately `0.571 x 0.308 = 0.176`; the active shell blocks are locally isotropic in this model, so coherence concentration does not cause the looseness. Finally, a complete-lineage shot-noise formulation shows that conservative photon recycling may be exactly invisible to ideal endpoint-counting cross-noise while reappearing at finite frequency through Shockley–Ramo carrier motion. These results identify which information is discarded when detector behavior is compressed to a scalar and which microscopic resources can still be inferred from measured response.

---

# I. Introduction

Photodetector performance is usually communicated through scalar quantities: responsivity, quantum efficiency, noise-equivalent power, specific detectivity, bandwidth, dark current, or timing jitter. These quantities are indispensable, but each refers to a restricted experiment. A scalar cannot in general preserve how detector response is distributed over signal waveforms, internal quantum states, transition channels, or readout observables.

This fact by itself is not new. Task-based imaging and detection theory has long represented performance with matrices or kernels rather than one scalar, quantum measurement theory describes detectors through positive operator-valued effects, and semiconductor detector theory distinguishes internal carrier fluctuations from the current induced at external electrodes. General quantum-photodetector frameworks likewise treat absorption, internal dynamics, amplification, and measurement as distinct stages. Our purpose is narrower. We ask whether several detector-specific limits that arose independently can be placed into one quantitative chain and whether doing so produces new relations among them.

The motivating examples are deliberately different.

First, two photodetector channels can be normalized to have the same eventual matched-filter sensitivity for a selected transient while differing in temporal response. When event arrival is known, the faster channel accumulates evidence sooner. When arrival is uncertain, the faster channel also creates a larger normalized timing-search region. A validated continuous-time construction shows that the ordering can reverse for a conservative global-false-alarm acquisition criterion. Thus eventual event-specific sensitivity does not fix finite-time task ordering.

Second, a photon can prepare a coherent superposition of microscopic excited states while internal dark generation prepares the same basis-state populations incoherently. A bright-state readout can distinguish the two even though energy and microscopic populations are identical. In the uniform `N`-state limit the ideal accepted-dark fraction is `1/N`.

Third, direct interband optical response itself carries information about equilibrium quasiparticle population. For transitions crossing the chemical potential, Fermi statistics and a bounded microscopic velocity block imply that finite optical spectral weight cannot be supported by arbitrarily few thermally populated one-body states. This gives a lower bound on thermal carrier population without assuming a density of states, parabolic dispersion, recombination law, or one-to-one transitions.

Fourth, an internal process need not remain visible at the terminals. Conservative photon recycling can produce dynamical carrier correlations and deterministic optical crosstalk while ideal final-extraction streams remain independent Poisson processes. A finite-transit junction changes this conclusion because carrier motion induces Shockley–Ramo current before the lineage reaches its final sink.

The central observation of this paper is that these are not merely four versions of the statement that “the readout matters.” Their quantitative structure is governed by the spectral geometry of the physical coupling map appropriate to the question being asked.

We first derive a fixed-strength spectral-concentration theorem. The same stable-rank factor controls maximum task advantage, coherent bright-state selectivity, and the reciprocal tightness of a state-count capacity bound. We then embed that geometry into the direct optical thermal-population theorem, extend it shell by shell to dispersive bands, and validate the decomposition in an eight-band HgCdTe model. Finally, we move from optical coupling to terminal readout and derive the corresponding lineage-observability boundary for photon recycling.

The operators used in these sections act on different physical spaces. We do **not** claim that one universal matrix is simultaneously a matched-filter kernel, a microscopic velocity block, and a terminal transfer matrix. The common object is instead a physical map `M` at a specified stage of the detector chain and its positive Gram/effect operator `G=M^dagger M` on the relevant input space. The scientific question determines which stage and which space are appropriate.

---

# II. Spectral concentration of a detector coupling map

## A. Positive response pairing

Let a linear detector stage map an input vector or fluctuation amplitude `x` to an observed amplitude

```math
y=Mx.
```

The associated quadratic response is

```math
\|y\|^2
=\langle x|M^\dagger M|x\rangle.
```

Define

```math
\boxed{G=M^\dagger M\succeq0.}
```

For a positive input state or covariance `X`, the corresponding average response is

```math
\boxed{Q_G[X]=Tr(GX).}
```

Let `G` act on a `d`-dimensional subspace, with eigenvalues

```math
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_d\ge0.
```

Define its total strength and stable rank

```math
T=TrG,
```

```math
\boxed{r_{st}=T/\lambda_1.}
```

The equal-total-strength isotropic comparator is

```math
\boxed{G_{iso}=\frac{T}{d}I.}
```

This comparator is not asserted to be physically realizable for every device class. It is the unique positive operator with the same trace that assigns identical quadratic response to every normalized direction in the chosen subspace.

## B. Best-task advantage

For a normalized pure task `|s>`,

```math
q_G(s)=\langle s|G|s\rangle.
```

The largest possible response is `lambda_1`, while the isotropic comparator gives `T/d`. Therefore

```math
\boxed{
\mathcal A_{max}
=\frac{\lambda_1}{T/d}
=\frac{d}{r_{st}}.
}
```

Spectral concentration therefore converts a fixed total response budget into task selectivity.

## C. Coherent versus incoherent response

Let the coherent signal be the brightest eigenstate

```math
\rho_B=|1\rangle\langle1|.
```

Compare it with a uniform incoherent excitation over the same microscopic parent space,

```math
\rho_D=I/d.
```

Then

```math
Q_G[\rho_B]=\lambda_1,
```

```math
Q_G[\rho_D]=T/d.
```

Hence the coherent-to-incoherent response ratio is

```math
\boxed{
\mathcal S_{coh}
=\frac{Q_G[\rho_B]}{Q_G[\rho_D]}
=\frac{d}{r_{st}}
=\mathcal A_{max}.
}
```

The same spectral concentration that gives a best-task advantage gives the same factor of coherent selectivity.

## D. Reciprocal state-count capacity

Suppose the same `d` microscopic states are populated incoherently with common weight `p`, and their total coupling-weighted response is

```math
R=pTrG=pT.
```

If only the per-state capacity `lambda_1` is used to infer how many states are required to carry `R`, the capacity estimate is

```math
N_{cap}=R/\lambda_1=pr_{st}.
```

The true parent-state population is

```math
N=pd.
```

Thus the state-count capacity tightness is

```math
\boxed{
\tau_{count}
=\frac{N_{cap}}{N}
=\frac{r_{st}}{d}.
}
```

Combining the preceding results,

```math
\boxed{
\mathcal A_{max}
=\mathcal S_{coh}
=\frac1{\tau_{count}}.
}
```

This identity is elementary once the quantities are written in terms of `G`. Its physical content here is that the three ratios arise from independent detector questions: task performance, coherent rejection of incoherent excitation, and inverse state counting.

## E. Selectivity requires a task penalty

Fixed trace also prevents spectral concentration from improving all tasks. Since

```math
\sum_{j=2}^d\lambda_j
=T-\lambda_1,
```

at least one orthogonal direction satisfies

```math
\lambda_d
\le
\frac{T-\lambda_1}{d-1}.
```

Using

```math
\mathcal S_{coh}=d\lambda_1/T,
```

we obtain

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{coh}}{d-1}.
}
```

The guaranteed fractional loss on at least one task is therefore

```math
\boxed{
\mathcal L_{task}
\ge
\frac{\mathcal S_{coh}-1}{d-1}.
}
```

This bound is tight when the remaining `d-1` eigenvalues are equal.

More generally, if two detector information operators have the same trace but are not identical, their difference is a nonzero Hermitian trace-zero operator and is therefore indefinite. There necessarily exist tasks with opposite detector orderings.

This provides the abstract geometric skeleton behind the transient-ordering example introduced above. The detailed unknown-arrival problem contains additional search-process structure and is not reduced to trace matching, but it illustrates the same principle: a scalar normalization does not preserve the task geometry of the detector.

---

# III. Coherence-selective photodetection as a concentrated endpoint

Consider `N` degenerate microscopic excited states `|j>` and one accepted optical mode that prepares

```math
|B\rangle
=\sum_{j=1}^N\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

with

```math
w_j\ge0,
\qquad
\sum_jw_j=1.
```

Conditioned on absorption, the material state is

```math
\rho_\gamma=|B\rangle\langle B|.
```

Construct an adversarial internal dark event with exactly the same microscopic populations but no coherence,

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Any observable diagonal in this basis gives the same expectation for the two states. The ideal bright projector

```math
\Pi_B=|B\rangle\langle B|
```

instead gives

```math
Tr(\Pi_B\rho_\gamma)=1,
```

```math
Tr(\Pi_B\rho_D)=\sum_jw_j^2.
```

Defining

```math
N_{eff}=\frac1{\sum_jw_j^2},
```

one has an ideal conditional rejection factor `N_eff`. In the uniform case,

```math
w_j=1/N,
```

so

```math
\boxed{
\eta_\gamma=1,
\qquad
\epsilon_D=1/N.
}
```

The uniform bright selector is precisely the rank-one endpoint of Sec. II:

```math
G=\Pi_B,
\qquad
T=1,
\qquad
r_{st}=1,
\qquad
d=N.
```

Therefore

```math
\mathcal S_{coh}=N,
\qquad
\tau_{count}=1/N.
```

The `N-1` orthogonal combinations are exactly dark to this readout. The detector has traded isotropic access to the microscopic manifold for maximal selectivity of one coherent direction.

This section concerns conditional state discrimination. It does not by itself establish a low dark-count detector. Dephasing, extraction, detailed balance, and finite-density kinetics remain independent physical constraints.

---

# IV. Direct optical response forces a minimum thermal state population

We now turn from an ideal coherent selector to an equilibrium semiconductor. Here the inverse problem is different: given direct optical response in a selected frequency window, how little thermal one-body population can support it?

## A. Cross-chemical-potential transitions

Work first in finite volume, with exact one-particle eigenstates. Let `mu` be the equilibrium chemical potential. We select direct optical transitions

```math
v\to c
```

with

```math
E_v<\mu<E_c
```

and transition frequency in a chosen window `B`.

For one such transition define

```math
E=E_c-E_v>0.
```

The Fermi occupations obey the exact inequality

```math
\boxed{
\frac{2(f_v-f_c)}{e^{E/(2k_BT)}-1}
\le
f_c+(1-f_v).
}
```

Equality occurs when the electron and hole excitation energies are mirror symmetric about the chemical potential.

This inequality is the thermal step that converts absorptive occupation difference into a lower requirement on electron-plus-hole population.

## B. Kubo-Greenwood form

For polarization `i`, the direct cross-`mu` contribution to the real optical conductivity may be written

```math
\sigma_1^{cross}(\omega)
=\frac{\pi e^2}{V\omega}
\sum_{v,c}^{cross}
(f_v-f_c)|v^i_{cv}|^2
\delta(E_c-E_v-\hbar\omega).
```

Define the thermal optical functional

```math
\boxed{
\mathcal L_B
=\frac{2}{\pi e^2}
\int_B
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}
d\omega.
}
```

After the frequency integral and the Fermi inequality,

```math
\mathcal L_B
\le
\mathcal R_B,
```

where `R_B` is the exact thermally weighted selected velocity strength.

## C. Basis-invariant shell capacity

Exact degeneracies require a basis-invariant definition. Let `P_epsilon` project onto the full eigenspace of energy `epsilon`. For an upper energy shell define the selected lower-space projector

```math
Q^-_{\epsilon_c,B}
=\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in B}}
P_{\epsilon_v}
```

and the selected velocity block

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,B}.
```

Similarly, for a lower shell,

```math
B_{\epsilon_v,B}
=Q^+_{\epsilon_v,B}\hat v_iP_{\epsilon_v}.
```

Define

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

This maximizes only within exact energy shells and therefore does not introduce unphysical coherent superpositions of different equilibrium energies.

For every selected block,

```math
Tr(MM^\dagger)
\le
\|M\|_{op}^2rank(M).
```

Define the optically active thermal populations

```math
n_{e,B}^{act}
=\frac1V
\sum_{\epsilon_c>\mu}
f(\epsilon_c)rank(A_{\epsilon_c,B}),
```

```math
n_{h,B}^{act}
=\frac1V
\sum_{\epsilon_v<\mu}
[1-f(\epsilon_v)]rank(B_{\epsilon_v,B}).
```

Then

```math
\mathcal R_B
\le
(v_B^{cap})^2
(n_{e,B}^{act}+n_{h,B}^{act}).
```

Combining the two steps gives the central material theorem:

```math
\boxed{
 n_e+n_h
 \ge
 n_{e,B}^{act}+n_{h,B}^{act}
 \ge
 \frac{2}{\pi e^2(v_B^{cap})^2}
 \int_B
 \frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}
 d\omega.
}
```

No density of states, parabolicity, recombination law, or one-to-one transition assumption enters the theorem. It is restricted to equilibrium independent-quasiparticle direct transitions crossing the chemical potential, and it requires a finite selected shell velocity capacity.

---

# V. Dispersive bands: where does the state-count bound lose tightness?

The shell formulation lets the abstract selectivity relation of Sec. II be inserted directly into the material theorem.

Index every selected endpoint shell by `a`. Let

```math
M_a
```

be its optical block and define

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

```math
\mathcal S_a^{act}=r_a/r_{st,a}.
```

Let `p_a` be the electron or hole occupation weight of that exact shell and

```math
c_a=\lambda_a/(v_B^{cap})^2
```

its utilization of the global capacity. Define thermal active-population weights

```math
w_a^{act}
=\frac{p_ar_a}{\sum_bp_br_b}.
```

The capacity-step tightness is exactly

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

Thus singular concentration, shell-capacity nonuniformity, and thermal occupation have separate roles.

Define also

```math
\eta_F
=\frac{\mathcal L_B}{\mathcal R_B}
\le1.
```

The full observable theorem tightness is

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

For one shell that itself defines the global capacity,

```math
c_1=1
```

and we recover the reciprocal relation

```math
\mathcal S_1^{act}\tau_{cap}^{act}=1.
```

The full optical theorem gives

```math
\mathcal S_1^{act}\tau_{obs}^{act}=\eta_F.
```

This identifies two independent reasons why a measured optical response may certify only part of the available thermal population: the response may be concentrated into bright singular directions, or different energy shells may use less than the worst-case global velocity capacity. The Fermi/Kubo step supplies a third, statistically distinct source of slack.

---

# VI. Eight-band HgCdTe validation

We evaluate the decomposition in the same bulk second-order eight-band Kane model used to test the optical population theorem for 10-um-class HgCdTe at 300 K. The chemical potential is fixed by charge neutrality. The velocity operator is obtained analytically from `partial H/partial k_x`, and the selected direct cross-`mu` blocks are grouped within exact model degeneracies before singular values are taken.

For the broad window

```text
E_g <= Delta E <= 0.5 eV,
```

the controlling Experiment-12 calculation gives approximately

```text
reference cross-mu thermal population  = 1.005 x 10^17 cm^-3,
production v_B^cap                     = 1.01764 x 10^6 m/s,
optically active population            ~= 6.72 x 10^16 cm^-3,
observable lower bound                 ~= 1.18 x 10^16 cm^-3.
```

Thus the lower bound is about `11.8%` of the reference cross-`mu` population and about `17.6%` of the optically active population.

The new shellwise audit resolves the latter ratio. At moderate refined quadrature,

```text
eta_F                                  ~= 0.308,
capacity-step active tightness          ~= 0.571
using the separately validated ordinary supremum,
```

so

```math
0.308\times0.571\approx0.176.
```

More unexpectedly, every thermally important selected **active** exact-shell block in this model has

```math
\boxed{\mathcal S_a^{act}=1}
```

to numerical precision. Equivalently, its nonzero singular values are equal within the selected active shell block. The active-population looseness is therefore not caused by local coherence concentration. Instead, the blocks use different fractions of the global capacity, and the Fermi/Kubo inequality is substantially nonsaturated.

This result is useful precisely because it does not force the realistic material into the coherence-selective limit of Sec. III. The same decomposition distinguishes two different regimes:

```text
ideal bright selector:
    strong spectral concentration and exact dark directions;

bulk HgCdTe validation:
    locally isotropic active shell coupling,
    but nonuniform shell capacity and thermal asymmetry.
```

The previously reported broad population bound remains unchanged; the new result explains its tightness.

---

# VII. From internal dynamics to terminal observability

The preceding sections concern optical/task coupling. A second loss of information occurs after excitation, when internal dynamics are mapped to electrical terminals.

## A. Complete Poisson lineages

Consider independent primary event classes `a`, each arriving as a Poisson process of rate `Lambda_a`. One primary event generates a complete random multichannel terminal waveform

```math
\mathbf h_a(t)
```

with Fourier transform

```math
\mathbf H_a(\omega).
```

Campbell's theorem for marked Poisson shot noise gives the matrix spectrum

```math
\boxed{
S_y(\omega)
=\sum_a\Lambda_a
E[\mathbf H_a(\omega)\mathbf H_a^\dagger(\omega)].
}
```

Hence

```math
\boxed{
S_{ij}(\omega)
=\sum_a\Lambda_a
E[H_{a,i}(\omega)H_{a,j}^*(\omega)].
}
```

The cross-spectrum is therefore an overlap of **complete lineage waveforms**. Internal coupling alone is insufficient. The same primary lineage must leave correlated waveform support in both measured channels.

If every complete lineage contributes to only one terminal, each outer product is diagonal and all interterminal cross-spectra vanish.

## B. Conservative two-pixel recycling

For two identical carrier reservoirs with local non-transfer relaxation `gamma` and conservative exchange rate `k`, internal occupancy fluctuations have drift matrix

```math
M_x=
\begin{pmatrix}
\gamma+k&-k\\
-k&\gamma+k
\end{pmatrix}.
```

Their internal cross-spectrum is

```math
\boxed{
S_{x,12}(\omega)
=m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right].
}
```

It is positive at low frequency, negative at high frequency, and crosses zero at

```math
\omega_x=\sqrt{\gamma(\gamma+2k)}.
```

Thus the internal populations are dynamically coupled even though their equal-time cross covariance vanishes.

Now idealize the terminal current as counting only the final extraction event of each independent carrier lineage. A generated excitation may hop or recycle internally many times, but it eventually terminates in exactly one sink. Independent Poisson marking, thinning, and random displacement imply that the final sink streams are independent Poisson processes. Consequently

```math
\boxed{S_{I,12}^{end}(\omega)=0}
```

for all frequencies in the ideal endpoint-counting model.

Mean optical crosstalk and terminal noise correlation are therefore different observables.

## C. Finite-transit Shockley–Ramo reopening

A real junction current can respond before final collection. Let `phi_k(r)` be the weighting potential of electrode `k`. For an electron-hole pair,

```math
\boxed{
 i_k(t)
 =e\frac{d}{dt}
 [\phi_k(\mathbf r_e(t))-\phi_k(\mathbf r_h(t))].
}
```

If the pair is created internally at one point and later recombines internally at a common point, its integrated induced charge on every electrode is exactly zero:

```math
\boxed{Q_k^{rec}=\int i_k(t)dt=0.}
```

However, its finite-frequency waveform is

```math
\boxed{
H_k^{rec}(\omega)
=i\omega e
\int
\Delta\phi_k(t)e^{-i\omega t}dt,
}
```

so

```math
H_k^{rec}(0)=0
```

while generically

```math
H_k^{rec}(\omega)\ne0
```

for finite `omega`.

Consider a conservative recycling lineage

```text
pair created in pixel A
-> carrier motion in A
-> radiative recombination in A
-> photon transfer and reabsorption in B
-> carrier motion and final collection in B.
```

With sufficiently localized weighting fields, its terminal waveform has the form

```math
\mathbf H_{A\to B}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}.
```

Its cross term is

```math
H_A^{rec}(\omega)
H_B^{col*}(\omega)e^{i\omega T_{AB}}.
```

At zero frequency the source-pixel term vanishes, but at finite frequency it is generally nonzero. Thus finite-transit Ramo motion can expose a conservative recycling lineage that a pure endpoint counter erases completely.

The result does not claim new Shockley–Ramo electrodynamics or new Poisson shot-noise theory. The detector-specific prediction is the readout boundary between internal photon-recycling dynamics and measured interpixel noise.

---

# VIII. Discussion

The results above organize several detector questions by the information retained or discarded by the relevant coupling map.

For a fixed positive operator `G`, the trace gives only the total quadratic strength. The full eigenvalue spectrum tells how that strength is distributed over tasks. The largest eigenvalue controls the strongest selected response and the per-state capacity entering an inverse bound. Stable rank quantifies how concentrated the response is. Rank deficiency identifies directions that are exactly invisible to that stage of the detector.

This gives a useful hierarchy:

```text
Tr G:
    total coupling/information budget;

lambda_max:
    strongest selected task and worst-case per-state capacity;

stable rank:
    coherent selectivity and inverse state-count tightness;

full spectrum:
    task anisotropy and ordering;

null space:
    exactly hidden directions;

energy-shell occupations:
    thermal realization of the microscopic coupling;

lineage waveform overlaps:
    survival of internal dynamics to measured terminals.
```

The framework also clarifies what the results do **not** say.

First, there is no proposal to replace `D*` by stable rank. Conventional detector figures remain useful within specified measurement conditions. The point is that no scalar is generally complete for arbitrary tasks unless the relevant normalized information operator is effectively isotropic on the task subspace.

Second, the optical population theorem is not a universal dark-current or detector-noise floor. It is an equilibrium one-body state-count bound for selected direct transitions. Recombination kinetics, excitons, phonon-assisted processes, many-body spectral functions, intentional doping, and unconstrained photonic path enhancement lie outside its present theorem class.

Third, coherence selectivity is not automatically available in a bulk semiconductor. The HgCdTe calculation in fact lies near the opposite local singular-spectrum limit on its active shells. Engineering a rank-one bright selector is an additional architectural resource.

Fourth, internal noise correlations are not directly observable quantities. Their visibility depends on the downstream readout map. This distinction is especially important when comparing photoconductive occupancy-sensitive readout, finite-transit photovoltaic current, and ideal endpoint counting.

The common spectral language is therefore most useful as an accounting framework: it identifies which resource or information loss is responsible for a particular detector limitation rather than attributing all limits to one universal figure of merit.

---

# IX. Conclusion

We have connected four photodetector problems through the spectral geometry of their physical coupling and readout maps.

At fixed total coupling strength, concentrating response into a bright direction produces an exact three-way relation:

```math
\boxed{
\text{maximum task advantage}
=
\text{coherent selectivity}
=
\frac{1}{\text{state-count capacity tightness}}.
}
```

The same selectivity forces a quantitative loss on at least one other task. In an equilibrium semiconductor, Fermi statistics and Kubo-Greenwood response convert the capacity geometry into a lower bound on the thermal population of the optically active states. For dispersive bands, the bound tightness separates into inverse selectivity, shell capacity utilization, and Fermi asymmetry. The eight-band HgCdTe calculation shows that its broad-window `~17.6%` active-population tightness is explained by the latter two factors rather than local coherence concentration.

Downstream, observability is controlled by a different map but the same geometric logic. Conservative photon recycling can remain entirely hidden from ideal endpoint-counting cross-noise even while producing internal correlations and mean crosstalk; finite-transit Shockley–Ramo motion can restore finite-frequency interpixel correlations without changing the recycling process itself.

The resulting picture is not that one scalar detector metric is wrong, nor that one new scalar should replace it. Rather, detector performance, microscopic resource inference, and internal-process visibility depend on different spectral features of the physical map connecting the quantity of interest to the measurement. Resolving that geometry reveals both what a detector can preferentially measure and what its measured response can certify about the underlying material.

---

# References — Rev0 working list

1. H. H. Barrett, J. L. Denny, R. F. Wagner, and K. J. Myers, objective assessment of image quality using Fisher information and task-based matrices, *J. Opt. Soc. Am. A* **12**, 834 (1995), DOI: 10.1364/JOSAA.12.000834.
2. E. Clarkson and F. Shen, Fisher-information kernels and task-based figures of merit, *J. Opt. Soc. Am. A* **27**, 2313 (2010), DOI: 10.1364/JOSAA.27.002313.
3. S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Phys. Rev. A* **98**, 063835 (2018), DOI: 10.1103/PhysRevA.98.063835.
4. H. Xu et al., “Experimental Quantification of Coherence of a Tunable Quantum Detector,” *Phys. Rev. Lett.* **125**, 060404 (2020), DOI: 10.1103/PhysRevLett.125.060404.
5. Y. Onishi and L. Fu, “Fundamental Bound on Topological Gap,” *Phys. Rev. X* **14**, 011052 (2024).
6. D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury, “Low-energy optical absorption in correlated insulators: Projected sum rules and the role of quantum geometry,” *Phys. Rev. B* **112**, 075116 (2025).
7. B. A. Bernevig, T. L. Hughes, and S.-C. Zhang / related Kane-model literature as appropriate for final HgCdTe reference chain. **[Rev0 placeholder: replace with exact Experiment-12 reference set.]**
8. E. G. Novik et al., eight-band `k.p` model used for HgTe/HgCdTe parameterization, *Phys. Rev. B* **72**, 035321 (2005).
9. A. Laurenti et al., empirical HgCdTe band-gap relation used in the numerical validation. **[Rev0 placeholder: insert exact bibliographic entry from Experiment 12.]**
10. W. van Roosbroeck and W. Shockley, “Photon-Radiative Recombination of Electrons and Holes in Germanium,” *Phys. Rev.* **94**, 1558 (1954).
11. W. Dąbrowski, transport equations and Ramo theorem applied to semiconductor detector impulse response and generation-recombination noise, *Prog. Quantum Electron.* **13**, 233 (1989), DOI: 10.1016/0079-6727(89)90004-9.
12. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe photodiodes, *Opt. Eng.* **50**, 061003 (2011).
13. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe heterostructure photodiodes, *J. Electron. Mater.* **41**, 2766 (2012), DOI: 10.1007/s11664-012-2093-7.
14. A. Jóźwikowska and K. Jóźwikowski, photon reabsorption and optical crosstalk in HgCdTe photodiode arrays, *Opt. Quantum Electron.* **51**, 85 (2019), DOI: 10.1007/s11082-019-1781-4.
15. A. Mirasol, Poisson output of the `M/G/infinity` queue, *Operations Research* **11**, 282 (1963), DOI: 10.1287/opre.11.2.282.
16. J. M. Harrison and A. J. Lemoine, open networks of infinite-server queues, *J. Appl. Prob.* **18** (1981), DOI: 10.2307/3213306.
17. X. Zhao, L.-M. Kuang, and J.-Q. Liao, “General dark-state theory for arbitrary multilevel quantum systems,” *Phys. Rev. A* **113**, 013723 (2026).

**Rev0 reference note:** this list is intentionally incomplete. Before any submission-oriented revision, import the verified reference networks from Experiments 01, 09, and 12, remove placeholders, and audit every DOI/title against primary sources.
