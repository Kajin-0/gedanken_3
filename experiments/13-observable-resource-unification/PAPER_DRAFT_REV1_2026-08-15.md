# Spectral geometry of photodetection: task selectivity, thermal state-count bounds, and hidden internal dynamics

**Unified manuscript — Rev. 1**  
**Date:** 2026-08-15  
**Status:** scientific revision after hostile Rev. 0 review; not submission formatted

---

## Abstract

Scalar photodetector figures of merit summarize specified operating conditions but do not preserve how detector response is distributed over signal tasks, microscopic excitations, or terminal observables. We connect four detector-specific questions through the spectral geometry of the physical map relevant to each stage of detection. For a positive operator `G` on a `d`-dimensional subspace with fixed total strength `Tr G`, a uniform-shell comparison gives an exact relation between the maximum task advantage over an equal-trace isotropic comparator, the response of the brightest coherent direction relative to a uniform incoherent excitation, and the reciprocal tightness of a spectral-capacity state-count estimate. The same concentration forces a quantitative loss on at least one orthogonal task. We then derive a direct optical theorem in which the selected cross-chemical-potential contribution to the optical conductivity bounds from below the equilibrium population of the one-body states carrying that response, subject to a basis-invariant shell velocity capacity. In dispersive bands, the bound tightness separates into thermal Fermi asymmetry, shell-to-global capacity utilization, and inverse shell response selectivity. An eight-band 300-K HgCdTe audit reconstructs the broad-window active-population tightness as approximately `0.57 x 0.31 = 0.176`; the contributing active shell blocks are locally isotropic in this model, so singular-spectrum concentration does not cause the looseness. Finally, a complete-lineage shot-noise formulation shows that conservative photon recycling can be exactly invisible to ideal final-sink counting under independent Poisson-lineage assumptions, while finite-transit Shockley–Ramo motion permits the same lineage to acquire finite-frequency support in more than one terminal. These results identify which spectral information is lost by scalar detector summaries and which microscopic resources can still be certified from appropriately resolved response measurements.

---

# I. Introduction

Photodetector performance is commonly communicated through scalar quantities such as responsivity, quantum efficiency, noise-equivalent power, specific detectivity, bandwidth, dark current, and timing jitter. These quantities are indispensable when the measurement protocol and operating conditions are specified. None is expected to encode every possible optical task, microscopic transition channel, or readout observable.

That general statement is established. Task-based imaging and detection theory has long used matrices and information kernels rather than a single scalar. Quantum measurement theory represents detector outcomes by positive effects. Semiconductor detector theory distinguishes internal carrier fluctuations from the current induced at external electrodes, and general quantum-photodetector models already separate absorption, internal evolution, amplification, and measurement. We do not propose another generic formalism for measurement. Our narrower question is whether several photodetector limits derived independently become quantitatively linked when the correct physical map is retained instead of compressed to one number.

The detector chain contains several distinct maps. Schematically,

```math
\mathcal H_{task}
\xrightarrow{M_{opt}}
\mathcal H_{exc}
\xrightarrow{M_{dyn}}
\mathcal H_{int}
\xrightarrow{M_{ro}(\omega)}
\mathcal H_{term}.
```

The spaces and maps depend on the problem. A task-information map is not literally the same matrix as a microscopic velocity block, and neither is literally the same matrix as a terminal readout transfer matrix. At a specified stage, however, a quadratic response is governed by a positive Gram or effect operator

```math
G_j=M_j^\dagger M_j
```

or by the corresponding explicitly stated composite map. The unity developed below is spectral and structural, not an identification of physically different operators.

Four examples motivate the construction.

First, two photodetector channels may be normalized to have the same eventual matched-filter sensitivity for one selected transient while having different response times. When arrival time is known, the faster channel accumulates evidence sooner. When arrival time is uncertain, the faster channel also expands the normalized timing-search interval for a fixed physical uncertainty window. A validated continuous-time construction shows a fast-to-slow reversal of a conservative sufficient global-false-alarm guarantee. This physical example does not assume that the full task-information operators have equal trace; it establishes a more general point that one scalar normalization does not fix finite-time task ordering.

Second, a photon can prepare a coherent superposition of microscopic excited states while internal generation prepares the same basis-state populations incoherently. In the ideal uniform `N`-state construction, projection onto the optical bright state accepts the photon state with unit probability while accepting the population-matched incoherent state with probability `1/N`. This is an actual quantum state-discrimination result for that rank-one projector.

Third, direct interband optical response can certify a minimum equilibrium quasiparticle population. For transitions crossing the chemical potential, Fermi statistics and a finite microscopic velocity-block capacity prevent finite selected optical spectral weight from being supported by arbitrarily few thermally occupied endpoint states. The resulting theorem does not require a density of states, parabolic dispersion, a recombination law, or one-to-one transitions.

Fourth, internal dynamics need not survive to the measured terminals. Conservative photon recycling can produce internal population correlations and deterministic optical crosstalk while ideal final-extraction streams remain independent Poisson processes. A finite-transit photovoltaic readout differs because carrier motion induces Shockley–Ramo current before the lineage reaches its final sink.

The paper develops one quantitative spine through these problems. We first derive a **uniform-shell spectral-concentration identity** under a fixed-trace comparison. The same stable-rank factor controls maximum task response, coherent-versus-uniform-incoherent response selectivity, and the reciprocal tightness of a state-count capacity estimate. A separate inequality quantifies the task penalty forced by that concentration. We then insert the same singular-spectrum structure into the direct optical thermal-population theorem, generalize it shell by shell to dispersive bands, and test the resulting decomposition in an eight-band HgCdTe model. Finally, we move downstream to terminal readout and derive the complete-lineage observability boundary for photon recycling.

---

# II. Uniform-shell spectral concentration

## A. Positive response pairing

Consider one detector stage with linear map

```math
y=Mx.
```

Its quadratic response to a pure input is

```math
\|y\|^2
=\langle x|M^\dagger M|x\rangle.
```

Define

```math
\boxed{G=M^\dagger M\succeq0.}
```

For a positive input state or covariance `X`,

```math
\boxed{Q_G[X]=Tr(GX).}
```

Let `G` act on a `d`-dimensional comparison subspace with eigenvalues

```math
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_d\ge0.
```

Define

```math
T=TrG,
```

and, for `T>0`, the stable rank

```math
\boxed{r_{st}=T/\lambda_1.}
```

The equal-total-strength isotropic comparator is

```math
\boxed{G_{iso}=\frac{T}{d}I_d.}
```

This is a mathematical comparator, not a claim that every device class admits an isotropic physical realization with the same trace.

## B. Maximum task response at fixed total strength

For a normalized task `|s>`,

```math
q_G(s)=\langle s|G|s\rangle.
```

The maximum is `lambda_1`, whereas the isotropic comparator gives `T/d`. Therefore

```math
\boxed{
\mathcal A_{max}
=\frac{\lambda_1}{T/d}
=\frac{d}{r_{st}}.
}
```

Spectral concentration redistributes a fixed quadratic-strength budget into preferred directions.

## C. Coherent response selectivity

Now compare the brightest coherent input

```math
\rho_B=|1\rangle\langle1|
```

with the **uniform incoherent state on the same parent subspace**,

```math
\rho_{mix}=I_d/d.
```

Then

```math
Q_G[\rho_B]=\lambda_1,
```

```math
Q_G[\rho_{mix}]=T/d.
```

Define the response-selectivity factor

```math
\boxed{
\mathcal S_{resp}
=\frac{Q_G[\rho_B]}{Q_G[\rho_{mix}]}
=\frac{d}{r_{st}}
=\mathcal A_{max}.
}
```

For a generic coupling map, `S_resp` is only a response ratio. It is not automatically a Helstrom-optimal discrimination factor or a minimum false-positive probability. The stronger quantum-discrimination interpretation used later applies to the specific rank-one Experiment-09 projector.

## D. Reciprocal state-count capacity under common shell occupation

Suppose the same `d` microscopic states form one exact shell or manifold with a common incoherent occupation weight `p`. Their total coupling-weighted response is

```math
R=pTrG=pT.
```

If the only microscopic capacity information retained is the largest per-direction response `lambda_1`, the capacity estimate of the populated state count is

```math
N_{cap}=R/\lambda_1=pr_{st}.
```

The true parent-shell population is

```math
N=pd.
```

Hence

```math
\boxed{
\tau_{count}
=\frac{N_{cap}}{N}
=\frac{r_{st}}{d}.
}
```

For this **uniform-shell/common-occupation comparison**,

```math
\boxed{
\mathcal A_{max}
=\mathcal S_{resp}
=\frac1{\tau_{count}}
=\frac{d}{r_{st}}.
}
```

The equality is algebraically simple. Its detector significance is that the three factors arise from different questions posed of the same coupling block: which task is favored, how strongly the brightest coherent direction is favored over a uniform incoherent ensemble, and how completely the total shell population can be inferred from response when only the worst-case single-direction capacity is known.

The common-occupation hypothesis is natural inside an exact equilibrium energy shell. It is not valid across arbitrary dispersive energies. Section V gives the energy-resolved generalization.

## E. Selectivity forces a quantitative task penalty

Because the trace is fixed,

```math
\sum_{j=2}^d\lambda_j
=T-\lambda_1.
```

At least one orthogonal eigen-direction therefore satisfies

```math
\lambda_d
\le
\frac{T-\lambda_1}{d-1}.
```

Using

```math
\mathcal S_{resp}=d\lambda_1/T,
```

we obtain

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{resp}}{d-1}.
}
```

Thus the guaranteed fractional degradation on at least one task is

```math
\boxed{
\mathcal L_{task}
\ge
\frac{\mathcal S_{resp}-1}{d-1}.
}
```

The inequality is tight when the remaining `d-1` eigenvalues are equal.

A related exact statement follows for two operators. If

```math
TrG_A=TrG_B
```

and

```math
G_A\ne G_B,
```

then `G_A-G_B` is a nonzero Hermitian trace-zero operator and therefore indefinite. There exist normalized tasks with opposite orderings under `G_A` and `G_B`.

This fixed-trace result is distinct from the detailed unknown-arrival detector construction used as motivation in Sec. I. The latter equalizes one event-specific eventual matched-filter SNR and introduces a timing-search process; it is not asserted to be obtained by imposing equal traces on the full task operators.

---

# III. Coherence-selective photodetection: the rank-one endpoint

Consider `N` degenerate excited states `|j>` and one accepted optical mode that prepares

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

Conditioned on absorption,

```math
\rho_\gamma=|B\rangle\langle B|.
```

Construct a population-matched incoherent internal event

```math
\rho_D
=\sum_jw_j|j\rangle\langle j|.
```

Every observable diagonal in this basis gives the same expectation value for `rho_gamma` and `rho_D`. The bright-state projector

```math
\Pi_B=|B\rangle\langle B|
```

gives instead

```math
Tr(\Pi_B\rho_\gamma)=1,
```

```math
Tr(\Pi_B\rho_D)=\sum_jw_j^2.
```

Define

```math
\boxed{
N_{eff}=\frac1{\sum_jw_j^2}.
}
```

The accepted-dark fraction under the bright projector is exactly `1/N_eff`. Moreover, among yes/no POVM elements with unit acceptance of `|B>`, the bright projector minimizes the accepted probability of `rho_D` in this construction.

For uniform weights,

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

This uniform case is exactly the rank-one endpoint of Sec. II:

```math
G_{opt}=\Pi_B,
\qquad
T=1,
\qquad
r_{st}=1,
\qquad
d=N.
```

Therefore the generic response selectivity and the actual bright-projector rejection factor coincide:

```math
\boxed{
\mathcal S_{resp}=N,
\qquad
\tau_{count}=1/N.
}
```

The `N-1` orthogonal combinations are exactly dark to the selector. The detector has concentrated all accepted response into one coherent direction.

For nonuniform `w_j`, the exact quantum result remains the `N_eff` expression above. It should not be replaced by the simple `d/r_st` formula unless the comparison state is uniform on the same parent subspace.

This section concerns conditional state discrimination. It does not by itself establish a scalable low-dark-count detector. Dephasing, extraction kinetics, detailed balance, and finite-density generation remain separate resources.

---

# IV. Selected direct optical response forces a minimum thermal population

We now consider an equilibrium independent-quasiparticle semiconductor and ask an inverse question: how much equilibrium endpoint population is required to support a selected direct optical response?

The theorem applies to the **cross-chemical-potential contribution** to the conductivity. A raw measured total conductivity can contain additional channels and cannot in general be inserted without isolating or modeling the selected contribution.

## A. Pointwise Fermi bound

Let `|v>` and `|c>` be exact one-particle eigenstates with

```math
E_v<\mu<E_c,
```

and transition energy

```math
E_{cv}=E_c-E_v>0.
```

Define

```math
p_c=f(E_c),
\qquad
h_v=1-f(E_v),
```

and

```math
D_{cv}=f(E_v)-f(E_c).
```

The exact Fermi occupations satisfy

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le
p_c+h_v.
}
```

Equality holds if and only if

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
```

The Bose-like denominator is not an assumed bosonic occupation; it results from optimizing the two fermionic endpoint occupations at fixed transition energy.

## B. Authoritative Kubo–Greenwood convention

For one physical velocity polarization `i`, define

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

The positive-frequency conductivity contributed only by selected direct transitions whose endpoints straddle `mu` is written

```math
\boxed{
\sigma_1^{cross}(\omega)
=
\frac{\pi e^2}{V}
\sum_{cv}^{cross}
\frac{D_{cv}|v_{cv}|^2}{E_{cv}}
\delta\!\left(\omega-\frac{E_{cv}}{\hbar}\right).
}
```

Let `B` be any measurable set of positive angular frequencies. Define the exact thermal kernel

```math
\boxed{
K_T(E)
=\frac{E}{e^{E/(2k_BT)}-1}.
}
```

Multiplying the pointwise Fermi bound by `|v_cv|^2`, summing over selected transitions, and using the conductivity representation yields

```math
\boxed{
\mathcal R_B(T)
\ge
\frac{2}{\pi e^2}
\int_B
K_T(\hbar\omega)
\sigma_1^{cross}(\omega)
\,d\omega,
}
```

where

```math
\mathcal R_B(T)
=\frac1V
\left[
\sum_cp_cR_c(B)
+
\sum_vh_vC_v(B)
\right]
```

is the exact thermally weighted selected squared-velocity strength. Here `R_c` and `C_v` are the selected row and column strengths of the velocity matrix.

No velocity ceiling, density-of-states approximation, or one-to-one pairing has entered yet.

## C. Basis-invariant shell capacity

A transition-by-transition maximum is insufficient in an exactly degenerate multiband shell because coherent combinations within the shell can redistribute individual matrix elements. Work in finite volume and let `P_epsilon` project onto the complete exact eigenspace at energy `epsilon`.

For an upper shell `epsilon_c>mu`, define

```math
Q^-_{\epsilon_c,B}
=\sum_{\substack{\epsilon_v<\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in B}}
P_{\epsilon_v}
```

and

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,B}.
```

For a lower shell `epsilon_v<mu`, define

```math
Q^+_{\epsilon_v,B}
=\sum_{\substack{\epsilon_c>\mu\\
(\epsilon_c-\epsilon_v)/\hbar\in B}}
P_{\epsilon_c}
```

and

```math
B_{\epsilon_v,B}
=Q^+_{\epsilon_v,B}\hat v_iP_{\epsilon_v}.
```

The selected basis-invariant optical-velocity capacity is

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}
\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}
\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

The maximization permits arbitrary basis choice only inside an exact energy eigenspace; it does not coherently mix states of different equilibrium energies.

For any selected finite-rank shell block `M`,

```math
Tr(MM^\dagger)
\le
\|M\|_{op}^2rank(M).
```

Define the optically active equilibrium populations

```math
\boxed{
n_{e,B}^{act}
=\frac1V
\sum_{\epsilon_c>\mu}
f(\epsilon_c)
rank(A_{\epsilon_c,B}),
}
```

```math
\boxed{
n_{h,B}^{act}
=\frac1V
\sum_{\epsilon_v<\mu}
[1-f(\epsilon_v)]
rank(B_{\epsilon_v,B}).
}
```

Then

```math
\mathcal R_B(T)
\le
(v_B^{cap})^2
(n_{e,B}^{act}+n_{h,B}^{act}).
```

Combining the statistical, optical-response, and capacity steps gives

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

This is an equilibrium one-body theorem for selected direct cross-`mu` transitions. It is not a universal dark-current, generation-rate, detector-noise, or total-conductivity bound.

---

# V. Dispersive bands: decomposition of state-count tightness

The exact energy-shell formulation allows the singular-spectrum structure of Sec. II to enter without imposing an artificial flat manifold.

Index every selected electron or hole endpoint shell by `a`. Let its selected block be `M_a`, and define

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

and the active-support response selectivity

```math
\boxed{
\mathcal S_a^{act}
=\frac{r_a}{r_{st,a}}.
}
```

The global capacity satisfies

```math
(v_B^{cap})^2=\sup_a\lambda_a.
```

Define each shell's capacity utilization

```math
\boxed{
c_a=\frac{\lambda_a}{(v_B^{cap})^2},
\qquad0\le c_a\le1.
}
```

Let `p_a` be the equilibrium electron or hole occupation of the exact shell. The active thermal population is proportional to

```math
N_{act}=\sum_ap_ar_a.
```

Define normalized active-population weights

```math
\boxed{
w_a^{act}
=\frac{p_ar_a}{\sum_bp_br_b}.
}
```

The capacity-only estimate is

```math
N_{cap}
=\frac{\sum_ap_aTr(M_aM_a^\dagger)}{(v_B^{cap})^2}.
```

Since

```math
Tr(M_aM_a^\dagger)
=\lambda_ar_{st,a},
```

we obtain the exact dispersive identity

```math
\boxed{
\tau_{cap}^{act}
\equiv\frac{N_{cap}}{N_{act}}
=\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

For one isolated shell that itself sets the global capacity, `c_1=1`, so the uniform-shell reciprocal relation is recovered:

```math
\mathcal S_1^{act}\tau_{cap}^{act}=1.
```

Now define the global statistical/optical-response efficiency

```math
\boxed{
\eta_F
=\frac{\mathcal L_B}{\mathcal R_B},
\qquad0\le\eta_F\le1,
}
```

with `L_B` the Kubo thermal functional above. The full observable lower-bound tightness becomes

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

The theorem therefore separates three physically different sources of slack:

```text
1. thermal/Fermi asymmetry:                 eta_F;
2. shell-to-global capacity mismatch:       c_a;
3. singular-spectrum response concentration: 1/S_a^act.
```

The decomposition is exact at the shell level. It does not require assigning one common occupation weight across different energies.

A total-parent-space version follows by replacing the active ranks with the full selected parent-shell dimensions. Exact kernel states then appear explicitly as an additional source of total-population slack.

---

# VI. Eight-band HgCdTe: realistic decomposition

We evaluate the preceding decomposition in the same bulk second-order eight-band Kane model used for the 300-K, 10-um-class HgCdTe validation of the thermal-population theorem. Charge neutrality determines the chemical potential. The velocity operator is calculated analytically from `partial H/partial k_x`, and exact model degeneracies are grouped before singular values are evaluated.

For the broad selected transition-energy window

```text
E_g <= Delta E <= 0.5 eV,
```

the controlling Experiment-12 calculation gives approximately

```text
cross-mu reference thermal population    = 1.005 x 10^17 cm^-3,
production v_B^cap                       = 1.018 x 10^6 m/s,
optically active population              = 6.7 x 10^16 cm^-3,
observable lower bound                   = 1.18 x 10^16 cm^-3.
```

The lower bound is therefore about `11.8%` of the reference cross-`mu` population and about `17.6%` of the optically active population.

A separate stable-rank audit, using moderate refined quadrature and the independently validated production capacity, decomposes the active-population ratio as approximately

```text
capacity-step factor                    ~= 0.57,
Fermi/Kubo factor eta_F                 ~= 0.31,
product                                 ~= 0.176.
```

These decomposition numbers are **audit-level**, not yet frozen production values. A production stable-rank rerun using the full convergence protocol is required before journal-facing significant figures are fixed.

The qualitative result is robust in the present audit: every thermally important selected **active** exact-shell block satisfies

```math
\boxed{
\mathcal S_a^{act}=1
}
```

to numerical precision. Equivalently, its nonzero singular values are equal within the selected active shell block.

Thus local coherence concentration does not explain the broad-window active-bound looseness in this model. The dominant losses are instead shell-to-global capacity mismatch and nonsaturation of the Fermi/Kubo step:

```math
0.57\times0.31\approx0.176.
```

This is a useful counterpoint to Sec. III. The ideal bright selector occupies a maximally concentrated rank-one regime; the realistic HgCdTe active shell blocks occupy a locally isotropic regime. The same decomposition distinguishes the two rather than forcing them into one physical mechanism.

---

# VII. Internal photon recycling and terminal observability

The preceding sections concern task and optical coupling. A second information loss can occur downstream when internal stochastic dynamics are mapped to electrical terminals.

## A. Complete-lineage spectral matrix

Let independent primary event classes `a` arrive as Poisson processes with rates `Lambda_a`. One primary event generates a complete random multichannel terminal waveform

```math
\mathbf h_a(t)
```

with Fourier transform

```math
\mathbf H_a(\omega).
```

Under the marked-Poisson shot-noise assumptions,

```math
\boxed{
S_y(\omega)
=\sum_a\Lambda_a
E[\mathbf H_a(\omega)\mathbf H_a^\dagger(\omega)].
}
```

Therefore

```math
\boxed{
S_{ij}(\omega)
=\sum_a\Lambda_a
E[H_{a,i}(\omega)H_{a,j}^*(\omega)].
}
```

The terminal cross-spectrum is an overlap of complete event-lineage waveforms. Internal coupling alone does not guarantee a measured cross-spectrum.

## B. Internal conservative exchange

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
```

It crosses zero at

```math
\boxed{
\omega_x=\sqrt{\gamma(\gamma+2k)}.
}
```

Thus the internal populations can be dynamically cross-correlated even though equal-time cross covariance vanishes.

## C. Exact endpoint-counting cancellation

Now impose the stronger idealized readout assumptions:

```text
1. primary generation is Poisson;
2. complete carrier/photon lineages evolve independently;
3. one primary lineage ultimately terminates in exactly one final sink;
4. the terminal observable records only that final sink event;
5. there is no branching/gain that creates multiple recorded descendants;
6. there is no common electronic coupling between output channels.
```

A lineage may undergo arbitrarily many independent conservative routing or recycling steps before termination. Each primary event can nevertheless be marked by one final sink and one random final delay. Poisson marking, thinning, displacement, and superposition preserve independent Poisson output streams for distinct final-sink classes.

Therefore an ideal final-extraction readout obeys

```math
\boxed{
S_{I,12}^{end}(\omega)=0
}
```

for every frequency, even when internal occupancy correlations and mean crosstalk are nonzero.

The result is not expected to survive branching SPAD/e-APD gain, nonlinear carrier interactions, correlated primary generation, common electronics, or any readout that responds before the final sink.

## D. Finite-transit Shockley–Ramo motion

A real photovoltaic current can respond to carrier motion before collection. For electrode `k`, let `phi_k(r)` be its weighting potential. An electron-hole pair gives induced current

```math
\boxed{
 i_k(t)
 =e\frac{d}{dt}
 [\phi_k(\mathbf r_e(t))-\phi_k(\mathbf r_h(t))].
}
```

If the pair is created internally at one point and later recombines internally at a common point, both endpoint weighting-potential separations vanish. Hence

```math
\boxed{
Q_k^{rec}=\int i_k(t)dt=0
}
```

for every electrode.

For the Fourier transform convention

```math
H_k(\omega)=\int i_k(t)e^{-i\omega t}dt,
```

integration by parts gives

```math
\boxed{
H_k^{rec}(\omega)
=i\omega e
\int
\Delta\phi_k(t)e^{-i\omega t}dt.
}
```

Thus

```math
\boxed{H_k^{rec}(0)=0,}
```

while an individual finite-transit trajectory can have nonzero finite-frequency support.

Consider a conservative recycling lineage

```text
pair created in pixel A
-> carrier motion in A
-> internal radiative recombination in A
-> photon transfer and reabsorption in B
-> carrier motion and final collection in B.
```

When the relevant weighting fields are sufficiently localized, a representative complete lineage has

```math
\mathbf H_{A\to B}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}.
```

The individual-lineage off-diagonal term is

```math
H_A^{rec}(\omega)H_B^{col*}(\omega)e^{i\omega T_{AB}}.
```

The source-pixel term is exactly zero at `omega=0` but can be nonzero at finite frequency. Therefore finite-transit Shockley–Ramo readout **permits** conservative recycling to become visible in interterminal AC correlations even when ideal endpoint counting erases it.

This is not a guarantee that every real photodiode exhibits a measurable recycling cross-spectrum. Ensemble symmetry, opposing lineage classes, weighting-field geometry, electronic transfer functions, or insufficient waveform overlap can still cancel or suppress the terminal cross-spectrum. The exact result is the DC null of an internally created/recombined Ramo segment and the opening of finite-frequency multichannel support at the lineage level.

---

# VIII. Discussion

The staged-map view clarifies what information is retained at different points in a detector.

For a fixed positive operator on a specified subspace,

```text
Tr G
    gives total quadratic strength;

lambda_max
    gives the strongest selected response and the worst-case per-direction capacity;

stable rank
    quantifies response concentration and, under uniform-shell comparison, reciprocal state-count tightness;

the full spectrum
    determines task anisotropy and ordering;

the null space
    identifies directions exactly invisible to that stage.
```

In the equilibrium optical theorem, additional physical structure enters:

```text
exact energy-shell occupations
    prevent arbitrary mixing across dispersive energies;

shell capacity utilization
    measures how closely each shell approaches the global selected velocity capacity;

eta_F
    measures the independent statistical slack between the exact thermally weighted velocity strength and the observable cross-mu conductivity functional.
```

Downstream, the corresponding object is the complete-lineage terminal waveform rather than the microscopic velocity block. Cross-noise depends on waveform overlap in terminal space, not on the existence of internal routing by itself.

Several limitations are essential.

First, no claim is made that stable rank should replace conventional `D*` or any other detector metric. A scalar can be complete only for the restricted family of tasks it was designed to summarize or, in the special quadratic setting above, on a subspace where the normalized relevant operator is effectively isotropic.

Second, the Experiment-12 theorem requires the selected direct cross-`mu` conductivity contribution. A total measured spectrum may require decomposition before the theorem can be applied. Same-side-of-`mu` transitions, free-carrier response, phonon-assisted processes, excitons, and other channels are outside the stated conductivity term.

Third, the thermal-population theorem is not a dark-current theorem. Recombination kinetics, intentional doping, many-body spectral functions, and unconstrained photonic path enhancement can introduce additional independent resources.

Fourth, the ideal coherence-selective construction is not generic to bulk HgCdTe. The present eight-band audit finds locally isotropic active shell singular spectra. Engineering a highly concentrated bright-state selector is an additional architectural resource.

Fifth, internal stochastic correlations are not terminal observables until a readout map is specified. This is why occupancy-sensitive photoconductive readout, finite-transit Shockley–Ramo current, and ideal final-sink counting can report different noise structure for the same internal recycling process.

The common spectral language is therefore an accounting framework rather than a universal new detector metric. Its value is that it identifies which physical resource or information bottleneck is responsible for a measured limitation.

---

# IX. Conclusion

Several apparently separate photodetector limits can be organized by the spectral geometry of the physical map relevant to the question being asked.

For one uniformly occupied shell or comparison subspace at fixed total quadratic strength,

```math
\boxed{
\text{maximum task response advantage}
=
\text{bright-versus-uniform-incoherent response selectivity}
=
\frac{1}{\text{state-count capacity tightness}}.
}
```

The same concentration forces a calculable loss on at least one orthogonal task. In the rank-one bright-state detector, the generic response selectivity becomes the actual `N`-fold conditional rejection factor against a uniform population-matched incoherent state.

For an equilibrium semiconductor, Fermi statistics and Kubo–Greenwood response turn the same capacity structure into a lower bound on the population of the one-body states carrying a selected direct cross-chemical-potential optical response. In dispersive bands, the bound tightness is a thermal weighted sum of shell capacity utilization divided by shell response selectivity, multiplied by an independent Fermi/Kubo factor. The current eight-band HgCdTe audit places the realistic broad-window example in a locally isotropic active-shell regime and attributes its approximately `17.6%` active-population tightness primarily to shell-capacity variation and Fermi asymmetry.

A separate information loss occurs downstream. Under independent conservative Poisson lineages, ideal final-sink counting can erase all interpixel cross-noise even when internal recycling and mean crosstalk are present. Internally created and recombined carrier segments carry zero net Shockley–Ramo charge but can have finite-frequency waveform support, so finite-transit readout can reopen interterminal sensitivity to the same recycling lineage without changing the internal recycling mechanism.

The resulting picture does not replace one scalar detector metric with another. It separates task preference, microscopic resource inference, and terminal observability into the spectral features of the physical maps that connect each quantity of interest to the measurement.

---

# References — Rev. 1 working list

1. H. H. Barrett, J. L. Denny, R. F. Wagner, and K. J. Myers, task-based image-quality assessment using Fisher-information and crosstalk matrices, *J. Opt. Soc. Am. A* **12**, 834–852 (1995), DOI: 10.1364/JOSAA.12.000834.
2. E. Clarkson and F. Shen, Fisher-information kernels as task-based figures of merit, *J. Opt. Soc. Am. A* **27**, 2313–2326 (2010), DOI: 10.1364/JOSAA.27.002313.
3. S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Phys. Rev. A* **98**, 063835 (2018), DOI: 10.1103/PhysRevA.98.063835.
4. H. Xu et al., “Experimental Quantification of Coherence of a Tunable Quantum Detector,” *Phys. Rev. Lett.* **125**, 060404 (2020), DOI: 10.1103/PhysRevLett.125.060404.
5. Y. Onishi and L. Fu, “Fundamental Bound on Topological Gap,” *Phys. Rev. X* **14**, 011052 (2024).
6. D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury, “Low-energy optical absorption in correlated insulators: Projected sum rules and the role of quantum geometry,” *Phys. Rev. B* **112**, 075116 (2025).
7. E. G. Novik et al., eight-band `k.p` model used for HgTe/HgCdTe parameterization, *Phys. Rev. B* **72**, 035321 (2005).
8. W. van Roosbroeck and W. Shockley, “Photon-Radiative Recombination of Electrons and Holes in Germanium,” *Phys. Rev.* **94**, 1558–1560 (1954).
9. W. Dąbrowski, semiconductor-detector impulse response and generation–recombination noise with transport/Ramo coupling, *Prog. Quantum Electron.* **13**, 233–266 (1989), DOI: 10.1016/0079-6727(89)90004-9.
10. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe photodiodes, *Opt. Eng.* **50**, 061003 (2011).
11. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe heterostructure photodiodes, *J. Electron. Mater.* **41**, 2766 (2012), DOI: 10.1007/s11664-012-2093-7.
12. A. Jóźwikowska and K. Jóźwikowski, photon reabsorption and optical crosstalk in HgCdTe photodiode arrays, *Opt. Quantum Electron.* **51**, 85 (2019), DOI: 10.1007/s11082-019-1781-4.
13. A. Mirasol, Poisson output of the `M/G/infinity` queue, *Operations Research* **11**, 282 (1963), DOI: 10.1287/opre.11.2.282.
14. J. M. Harrison and A. J. Lemoine, open networks of infinite-server queues, *J. Appl. Prob.* **18** (1981), DOI: 10.2307/3213306.

**Reference-production note:** the final submission-oriented revision must import and verify the complete primary-source reference networks from Experiments 01, 09, and 12, including the exact HgCdTe band-gap parameterization citation. This working list is not yet a journal-ready bibliography.
