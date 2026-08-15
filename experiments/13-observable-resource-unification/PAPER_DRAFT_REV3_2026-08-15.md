# Spectral geometry of photodetection: selectivity, resource certification, and internal observability

**Unified manuscript — Rev. 3**  
**Date:** 2026-08-15  
**Status:** scientific draft after Rev. 2 hostile review; not yet journal formatted

---

## Abstract

Photodetector figures of merit compress specified experiments to a few scalars, while detector response itself is distributed over signal tasks, microscopic excitation channels, and terminal observables. We identify a common spectral structure behind several detector-specific limits. On a physically declared admissible domain `D`, let `G_D` be the positive coupling/effect operator of the detector stage being interrogated, let `lambda_D` be its largest eigenvalue, and let `X` be a positive activity or population operator supported in `D`. The response of the strongest admissible direction relative to the actual ensemble-average response is exactly the reciprocal of the fraction of total activity certified when `Tr(G_D X)` is inverted using the maximum per-direction capacity `lambda_D`. The maximally mixed case reduces to a stable-rank relation and, under fixed total coupling strength, imposes a quantitative task penalty for spectral concentration. A rank-one coherent photodetector recovers the full nonuniform coherence dimension `N_eff=1/sum_j w_j^2` as this selectivity factor. In an equilibrium semiconductor, an exact Fermi inequality and the selected direct cross-chemical-potential Kubo conductivity turn the same capacity structure into a lower bound on the thermal population of optically active one-body endpoint states. A production-resolution eight-band HgCdTe calculation gives a capacity factor `0.573`, a Fermi/Kubo factor `0.307`, and their product `0.1757`. The selected active shell blocks are singular-value isotropic in the BIA-neglecting Kane validation because its fixed-k antiunitary doublets make the velocity blocks quaternionic; this exact isotropy is a model symmetry, not a universal property of zincblende HgCdTe. Downstream, each terminal defines a positive observability effect on the internal innovation space. Conservative photon recycling can lie in the source-channel null of ideal final-sink counting, forcing zero cross-noise, while finite-transit Shockley–Ramo motion can lift that null at finite frequency even though an internally created and recombined pair carries zero integrated induced charge. These results connect task selectivity, microscopic resource inference, and internal-process observability without proposing a new universal scalar detector metric.

---

# I. Introduction

Specific detectivity, responsivity, quantum efficiency, noise-equivalent power, bandwidth, dark current, and timing jitter are useful because each summarizes a defined detector experiment. None is expected to preserve the complete geometry of every possible optical task, microscopic excitation, or electrical readout.

That broad observation is established. Task-based imaging and detection theory uses information matrices and kernels; quantum measurement theory uses positive effects; semiconductor detector theory distinguishes internal carrier fluctuations from induced terminal current; and general quantum-photodetector frameworks already separate absorption, internal dynamics, amplification, and measurement. The present objective is not another generic measurement formalism. We ask a narrower question:

> When several detector limits are written using the physical map appropriate to each stage, do their apparently different tradeoffs become quantitatively related?

A useful schematic is

```math
\mathcal H_{task}
\xrightarrow{M_{opt}}
\mathcal H_{exc}
\xrightarrow{M_{dyn}}
\mathcal H_{int}
\xrightarrow{M_{ro}(\omega)}
\mathcal H_{term}.
```

The operators in these spaces are physically different. A transient matched-filter information operator is not the same matrix as a Kane velocity block, and neither is the same matrix as a terminal transfer operator. At a specified stage, however, quadratic response is governed by a positive operator

```math
G=M^\dagger M
```

or by the positive effect of the measurement under consideration. Its spectrum controls directional response; its spectral edge controls a worst-case per-direction capacity; and its null space identifies activity hidden from that observable.

Four independently developed detector problems motivate the connection.

First, two detector channels can be normalized to have the same eventual matched-filter sensitivity for one selected transient while having different response times. With known arrival time, faster response accumulates evidence sooner. With uncertain arrival time, the same speed increase enlarges the normalized timing-search interval for a fixed physical uncertainty window. A continuous-time construction gives a fast-to-slow reversal of a conservative sufficient global-false-alarm guarantee. One scalar sensitivity therefore does not determine every finite-time task ordering.

Second, optical absorption can prepare a coherent bright superposition while internal generation prepares exactly the same microscopic basis populations incoherently. A bright-state projector distinguishes those states even when energy, carrier number, and populations are identical.

Third, direct optical response can be used inversely. For transitions crossing the chemical potential, a finite selected velocity capacity and exact Fermi statistics imply that a measured selected conductivity functional requires a minimum equilibrium population of the electronic endpoint states carrying that response.

Fourth, internal dynamics need not remain visible at the terminals. Conservative photon recycling can generate internal carrier correlations and mean optical crosstalk while ideal final-sink count streams remain independent. Finite-transit carrier motion changes the readout because Shockley–Ramo current is induced before final recombination or collection.

The central bridge developed below is mathematically simple but physically useful: **forward selectivity relative to the actual activity ensemble is reciprocal to inverse resource-certification tightness when both are evaluated with the same declared maximum capacity.** The later sections show that this relation recovers the nonuniform coherence dimension of the bright-state detector and the global thermal capacity tightness of the optical population theorem. A shell-resolved decomposition then explains the realistic HgCdTe result. Finally, channel-specific observability effects put the recycling problem into the same staged positive-operator language.

---

# II. Admissible-domain selectivity and resource certification

## A. The domain is part of the physical theorem

Let `D` be a **physically declared admissible input/activity domain** for one detector stage and let `P_D` be its projector. The domain must be specified by the physical problem before the capacity is evaluated. Examples include a declared task subspace, a selected microscopic excited-state manifold, a cross-chemical-potential optical window, or an internal lineage sector at a chosen terminal frequency.

Let the stage coupling/effect operator be `G>=0`. Define its restriction

```math
\boxed{
G_D=P_DGP_D\succeq0.
}
```

Let

```math
\boxed{
\lambda_D=\lambda_{max}(G_D)>0.
}
```

The maximum is taken only over admissible directions. Enlarging `D` after seeing the result would change the resource definition and is not allowed.

Let

```math
X\succeq0,
\qquad
TrX>0,
\qquad
supp(X)\subseteq D.
```

`X` can represent an internal population, stochastic activity covariance, or ensemble weight on the declared domain.

## B. Actual ensemble-average response

Normalize

```math
\boxed{
\rho_X=X/TrX.
}
```

The response to the activity is

```math
\boxed{
Q_X=Tr(G_DX),
}
```

and the actual ensemble-average response per unit activity is

```math
\boxed{
\bar q_X
=Tr(G_D\rho_X)
=\frac{Tr(G_DX)}{TrX}.
}
```

The capacity-maximizing direction need not carry substantial weight in `X`. It is the strongest **admissible** direction, not necessarily the most occupied one. This distinction is precisely what can make the inverse bound loose.

## C. Forward response selectivity

When `Q_X>0`, define

```math
\boxed{
\mathcal S_{X|D}
=\frac{\lambda_D}{\bar q_X}
=\frac{\lambda_DTrX}{Tr(G_DX)}.
}
```

This is the ratio of the strongest admissible pure-direction response to the average response of the actual ensemble.

For a generic map it is a response-selectivity quantity, not automatically an optimal classification advantage.

## D. Inverse resource certification

Positivity gives

```math
Tr(G_DX)\le\lambda_DTrX.
```

If only the measured response and the maximum admissible per-direction capacity are retained, the certified minimum activity is

```math
\boxed{
N_{cap}
=\frac{Tr(G_DX)}{\lambda_D}.
}
```

Relative to the true total activity

```math
N_X=TrX,
```

define the capacity tightness

```math
\boxed{
\tau_{X|D}
=\frac{N_{cap}}{N_X}
=\frac{Tr(G_DX)}{\lambda_DTrX}.
}
```

Therefore exactly

```math
\boxed{
\mathcal S_{X|D}\tau_{X|D}=1.
}
```

The equality is a normalized spectral-capacity identity and is not claimed as new matrix theory. Its detector interpretation is that the same physical map gives reciprocal answers to two different questions:

```text
forward:
    how strongly can the detector favor its best allowed direction
    over the actual activity ensemble?

inverse:
    what fraction of the ensemble's total activity is guaranteed by
    the observed response if only the maximum allowed coupling is known?
```

If

```math
Tr(G_DX)=0,
```

then the activity sector is null to the observable. The certified fraction is zero.

---

# III. Uniform task ensembles and stable-rank concentration

Let `D` be a `d`-dimensional task subspace and take the uniform ensemble

```math
X=I_D.
```

Then

```math
TrX=d,
```

and define

```math
T=TrG_D.
```

The stable rank is

```math
\boxed{
r_{st}=T/\lambda_D.
}
```

The general theorem reduces to

```math
\boxed{
\mathcal S_{mix}=d/r_{st},
\qquad
\tau_{mix}=r_{st}/d.
}
```

The equal-total-strength isotropic comparator is

```math
G_{iso}=(T/d)I_D.
```

For a normalized task `|s>`,

```math
q(s)=\langle s|G_D|s\rangle.
```

The maximum task advantage over the isotropic comparator is

```math
\boxed{
\mathcal A_{max}
=\frac{\lambda_D}{T/d}
=d/r_{st}
=\mathcal S_{mix}.
}
```

Concentrating a fixed trace into a preferred direction necessarily weakens another direction. At least one orthogonal task obeys

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{mix}}{d-1},
}
```

or equivalently

```math
\boxed{
\mathcal L_{task}
\ge
\frac{\mathcal S_{mix}-1}{d-1}.
}
```

This bound is tight when the remaining `d-1` eigenvalues are equal.

If two positive task operators have the same trace but are unequal, their difference is nonzero Hermitian trace-zero and therefore indefinite. Opposite task orderings must exist somewhere in `D`.

This exact equal-trace statement is a spectral comparison principle. The separate unknown-arrival transient construction that motivated this branch uses a different physical normalization—equal eventual event-specific matched-filter SNR for one waveform—and an explicit correlated timing search. It remains a concrete demonstration of scalar incompleteness rather than a direct consequence of equal trace.

---

# IV. Coherent bright-state rejection: exact nonuniform specialization

Consider a microscopic excited-state manifold `D` with orthonormal states `|j>`. One accepted optical mode prepares

```math
|B\rangle
=\sum_{j=1}^N\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

where

```math
w_j\ge0,
\qquad
\sum_jw_j=1.
```

The photon-created state is

```math
\rho_\gamma=|B\rangle\langle B|.
```

Construct the population-matched incoherent internal state

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Use the bright-state effect

```math
\boxed{
G_D=\Pi_B=|B\rangle\langle B|.
}
```

Its maximum eigenvalue is one. The photon state is accepted with unit probability,

```math
Tr(\Pi_B\rho_\gamma)=1,
```

while

```math
Tr(\Pi_B\rho_D)=\sum_jw_j^2.
```

Choosing

```math
X=\rho_D
```

in the activity-weighted theorem gives

```math
\boxed{
\mathcal S_{\rho_D|D}
=\frac1{\sum_jw_j^2}
\equiv N_{eff},
}
```

and

```math
\boxed{
\tau_{\rho_D|D}
=\sum_jw_j^2
=1/N_{eff}.
}
```

For this particular rank-one effect, the response selectivity has an independently proved discrimination meaning. Any yes/no POVM element with unit acceptance of `|B>` must contain `|B>` as a unit-eigenvalue eigenvector, so its accepted dark probability cannot be lower than the bright projector's value. Thus `N_eff` is the optimal conditional rejection factor at unit signal acceptance for this matched-population construction.

The uniform case `w_j=1/N` gives

```math
N_{eff}=N.
```

The relation does not claim that coherence alone solves detector dark count. Dephasing, extraction, detailed balance, and finite-density kinetics remain separate constraints.

---

# V. Optical response as inverse thermal endpoint certification

We next apply the inverse side of the theorem to a direct semiconductor optical response.

The observable entering the theorem is the selected **direct cross-chemical-potential contribution** to the conductivity. A raw total measured spectrum can contain other processes and must be decomposed or measured in a regime where the selected contribution is isolated.

## A. Fermi endpoint inequality

For exact one-particle states with

```math
E_v<\mu<E_c,
```

let

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

Then

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le
p_c+h_v.
}
```

Equality holds exactly for mirror-symmetric endpoint excitation energies about `mu`.

## B. Selected Kubo conductivity

For physical velocity polarization `i`,

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

The selected positive-frequency conductivity is

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

Define

```math
\boxed{
K_T(E)
=\frac{E}{e^{E/(2k_BT)}-1}.
}
```

For any selected positive-frequency window `B`,

```math
\boxed{
\mathcal R_B
\ge
\mathcal L_B
\equiv
\frac{2}{\pi e^2}
\int_BK_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega.
}
```

`R_B` is the exact thermally weighted selected velocity strength.

## C. Physically declared optical capacity domain

The admissible domain is now fixed by the detector problem:

```text
endpoints straddle mu;
transition frequency lies in B;
physical velocity polarization i is specified;
only exact-energy-shell basis rotations are allowed.
```

Let `P_epsilon` project onto a complete exact one-particle eigenspace. For an upper endpoint shell define

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,B},
```

and for a lower endpoint shell define

```math
B_{\epsilon_v,B}
=Q^+_{\epsilon_v,B}\hat v_iP_{\epsilon_v}.
```

The basis-invariant selected velocity capacity is

```math
\boxed{
(v_B^{cap})^2
=\max\left[
\sup_{\epsilon_c>\mu}\|A_{\epsilon_c,B}\|_{op}^2,
\sup_{\epsilon_v<\mu}\|B_{\epsilon_v,B}\|_{op}^2
\right].
}
```

This is precisely `lambda_D` for the declared optical endpoint domain. It cannot be enlarged by adding unrelated states without changing the physical theorem.

## D. Endpoint-lifted activity space

Construct the positive endpoint operator

```math
\boxed{
G_B
=\bigoplus_{\epsilon_c>\mu}
A_{\epsilon_c,B}A_{\epsilon_c,B}^\dagger
\oplus
\bigoplus_{\epsilon_v<\mu}
B_{\epsilon_v,B}^\dagger B_{\epsilon_v,B}.
}
```

The upper and lower sectors are deliberately both retained because the resource being bounded is electron-plus-hole endpoint population. Each optical transition contributes through its electron endpoint and through its hole endpoint, matching the two terms in the exact thermal velocity strength.

For the active theorem let `P_a^{act}` project onto the support of each corresponding Gram block and define

```math
\boxed{
X_B^{act}
=\bigoplus_{\epsilon_c>\mu}
f(\epsilon_c)P_{\epsilon_c}^{act}
\oplus
\bigoplus_{\epsilon_v<\mu}
[1-f(\epsilon_v)]P_{\epsilon_v}^{act}.
}
```

Then

```math
\boxed{
TrX_B^{act}/V
=n_{e,B}^{act}+n_{h,B}^{act}
\equiv n_B^{act},
}
```

```math
\boxed{
Tr(G_BX_B^{act})/V=\mathcal R_B,
}
```

and

```math
\boxed{
\lambda_{max}(G_B)=(v_B^{cap})^2.
}
```

The global activity-weighted reciprocity is therefore

```math
\boxed{
\mathcal S_{th,B}^{act}
=\frac{(v_B^{cap})^2n_B^{act}}{\mathcal R_B},
}
```

```math
\boxed{
\tau_{cap}^{act}
=\frac{\mathcal R_B}{(v_B^{cap})^2n_B^{act}},
}
```

and

```math
\boxed{
\mathcal S_{th,B}^{act}\tau_{cap}^{act}=1.
}
```

The capacity-maximizing shell can be only weakly thermally populated. That is allowed: the theorem uses the strongest admissible per-state response, whereas `X_B^{act}` contains the actual thermal occupations.

The experimentally connected lower functional introduces

```math
\eta_F=\mathcal L_B/\mathcal R_B\le1,
```

so

```math
\boxed{
\tau_{obs}^{act}
=\eta_F\tau_{cap}^{act},
}
```

and

```math
\boxed{
\mathcal S_{th,B}^{act}\tau_{obs}^{act}
=\eta_F.
}
```

Finally,

```math
\boxed{
 n_e+n_h
 \ge n_B^{act}
 \ge
 \frac{2}{\pi e^2(v_B^{cap})^2}
 \int_B
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}d\omega.
}
```

The theorem is an equilibrium one-body endpoint-population bound, not a universal dark-current or total-conductivity bound.

---

# VI. Shell-resolved origin of global thermal selectivity

The global reciprocity gives the average capacity slack but not its origin.

For each selected endpoint shell `a`, define

```math
\lambda_a=\|M_a\|_{op}^2,
```

```math
r_a=rank(M_a),
```

```math
r_{st,a}
=Tr(M_aM_a^\dagger)/\lambda_a,
```

and

```math
\boxed{
\mathcal S_a^{act}=r_a/r_{st,a}.
}
```

Define shell utilization of the global capacity

```math
\boxed{
c_a=\lambda_a/(v_B^{cap})^2}
```

and thermal active-population weights

```math
\boxed{
w_a^{act}=p_ar_a/\sum_bp_br_b.
}
```

Then

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}},
}
```

and therefore

```math
\boxed{
\mathcal S_{th,B}^{act}
=
\left[
\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}
\right]^{-1}.
}
```

The observable tightness is

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_aw_a^{act}\frac{c_a}{\mathcal S_a^{act}}.
}
```

Hence global selectivity can arise from two spectrally different sources:

```text
within-shell anisotropy: S_a^act>1;
between-shell capacity variation: c_a<1.
```

The thermal Fermi/Kubo factor is separate from both.

---

# VII. Production eight-band HgCdTe and the origin of shell isotropy

We evaluate the decomposition in the same second-order bulk eight-band Kane validation used for the 300-K, 10-um-class HgCdTe population theorem.

For the broad window

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
v_B^cap                       = 1.01764e6 m/s
eta_F                         = 0.30684
tau_cap^act                   = 0.57262
tau_obs^act                   = 0.17570
S_th,B^act                    = 1.746.
```

Thus

```math
0.30684\times0.57262=0.17570.
```

The lower bound remains approximately `11.8%` of the reference cross-`mu` thermal population and `17.6%` of the selected active population.

## A. Machine-precision shell result

Every thermally important selected active endpoint block satisfies

```math
\boxed{\mathcal S_a^{act}=1}
```

to numerical precision; the maximum observed departure from unity is approximately `4e-14`.

This equality is not a numerical accident.

## B. Symmetry explanation inside the validation model

The second-order Kane Hamiltonian used here omits explicit bulk-inversion-asymmetry/Dresselhaus terms. Within this model there is an inversion operation `P` and spinful time reversal `T`, so the antiunitary combination

```math
\Theta=PT
```

leaves each bulk `k` fixed and satisfies

```math
\Theta^2=-1.
```

Generic endpoint shells therefore form twofold `Theta` doublets.

Velocity is odd under `P` and odd under `T`, hence even under `PT`:

```math
\Theta\hat v_i\Theta^{-1}=\hat v_i.
```

In `Theta`-adapted bases, the velocity matrix between two doublets has quaternionic form

```math
\boxed{
M=\begin{pmatrix}
a&b\\-b^*&a^*\end{pmatrix},
}
```

so

```math
MM^\dagger=(|a|^2+|b|^2)I_2.
```

The two singular values are equal. Concatenating several partner doublets preserves `MM^dagger proportional I_2`, so every nonzero selected active endpoint block has stable rank equal to rank and therefore `S_a^act=1`.

## C. Physical caveat

Real HgCdTe has the zincblende crystal structure and therefore true bulk inversion asymmetry. More complete BIA-inclusive multiband models can lift the fixed-k doublet/quaternionic structure and permit `S_a^act` to depart from one.

Accordingly, the production result should be read as

```text
within-shell anisotropy:
    symmetry-forbidden in the BIA-neglecting validation model;

between-shell capacity variation:
    thermal weighted factor 0.57262;

Fermi/Kubo asymmetry:
    factor 0.30684;

final active bound tightness:
    0.17570.
```

The general population theorem itself does not rely on inversion symmetry and would remain valid after recomputing the capacity and ranks in a BIA-inclusive model.

---

# VIII. Channel-specific observability of conservative photon recycling

We now move downstream from microscopic optical coupling to terminal readout.

At a fixed frequency let the internal innovation vector have positive spectral covariance

```math
\Sigma(\omega)\succeq0
```

and let

```math
\mathbf y=M(\omega)\boldsymbol\xi.
```

Then

```math
\boxed{
S_y=M\Sigma M^\dagger.
}
```

## A. Positive observability effect of one terminal

For terminal `i`, define

```math
M_i=\langle i|M
```

and

```math
\boxed{
G_i(\omega)
=M_i^\dagger M_i
=M^\dagger|i><i|M
\succeq0.
}
```

Its auto-spectrum is a positive activity pairing:

```math
\boxed{
S_{ii}=Tr[G_i(\omega)\Sigma].
}
```

Thus each terminal has its own frequency-dependent admissible-domain observability operator and its own selectivity/certification relation when a positive internal sector is specified.

## B. Cross-channel overlap

For channels `i` and `j`, define

```math
\boxed{
C_{ij}(\omega)
=M_j^\dagger M_i
=M^\dagger|j><i|M.
}
```

Then

```math
\boxed{
S_{ij}=Tr(C_{ij}\Sigma).
}
```

`C_ij` is not generally positive. Whitening `Sigma` turns the terminal rows into vectors `w_i`, giving

```math
S_{ij}=<w_j,w_i>
```

and therefore

```math
\boxed{
|S_{ij}|^2\le S_{ii}S_{jj}.
}
```

If an internal sector `X>=0` is null to channel `i`,

```math
Tr(G_iX)=0,
```

then its auto-response in that channel is zero and its cross contribution with every other channel is forced to zero.

Cross-noise therefore requires **joint terminal visibility** of the same internal sector.

## C. Internal conservative exchange

For two identical carrier reservoirs with local non-transfer relaxation `gamma`, conservative exchange rate `k`, and stationary mean `m`, the internal occupancy cross-spectrum is

```math
\boxed{
S_{x,12}(\omega)
=m\left[
\frac{\gamma}{\gamma^2+\omega^2}
-
\frac{\gamma+2k}{(\gamma+2k)^2+\omega^2}
\right],
}
```

with zero crossing

```math
\boxed{
\omega_x=\sqrt{\gamma(\gamma+2k)}.
}
```

Thus conservative routing is visible to an occupancy-sensitive internal observable.

## D. Endpoint-counting channel null

Assume:

```text
Poisson primary generation;
independent noninteracting complete lineages;
one final sink per primary lineage;
final-sink-only measurement;
no branching/gain producing multiple recorded descendants;
no common electronic coupling between output channels.
```

A complete conservative lineage that begins in A and ultimately exits through B has endpoint waveform

```math
\mathbf H_{A\to B}^{end}(\omega)
=g_B(\omega)\mathbf e_B.
```

For that lineage sector,

```math
Tr(G_A^{end}X_{A\to B})=0.
```

The source terminal is a channel null, so

```math
\boxed{
S_{AB}^{A\to B,end}=0.
}
```

When every conservative lineage has support in exactly one final terminal, every per-lineage outer product is diagonal. Independent Poisson final-sink streams therefore have zero interterminal cross-spectrum at all frequencies.

## E. Finite-transit Shockley–Ramo lifting of the null

Let `phi_i(r)` be the weighting potential of terminal `i`. An electron-hole pair induces

```math
\boxed{
 i_i(t)
 =e\frac{d}{dt}
 [\phi_i(\mathbf r_e(t))-\phi_i(\mathbf r_h(t))].
}
```

If the pair is created internally at one point and later recombines internally at a common point,

```math
\boxed{
Q_i^{rec}=\int i_i(t)dt=0.
}
```

But

```math
\boxed{
H_i^{rec}(\omega)
=i\omega e
\int\Delta\phi_i(t)e^{-i\omega t}dt,
}
```

so

```math
H_i^{rec}(0)=0
```

while an individual trajectory can have finite-frequency support.

For the same A-to-B recycling lineage, finite-transit readout can produce

```math
\mathbf H_{A\to B}^{Ramo}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}.
```

The A-channel effect is no longer necessarily null for `omega!=0`:

```math
Tr[G_A^{Ramo}(\omega)X_{A\to B}]>0
```

is permitted.

Once the lineage is visible to both channels, a nonzero cross contribution becomes allowed. It is not guaranteed: trajectory symmetry, opposing lineage classes, weighting-field structure, and electronics can still make the overlap vanish.

The readout transition is therefore a change in the frequency-dependent channel-specific positive operator:

```text
endpoint map:
    A-to-B lineage lies in null(G_A);
    A-B cross contribution forced to zero;

finite-transit Ramo map:
    source-channel null can be lifted at finite frequency;
    joint A/B visibility and cross-noise become possible.
```

This places the recycling problem inside the same staged observability geometry without treating the off-diagonal cross-spectrum itself as a positive operator.

---

# IX. Discussion

The results separate three questions.

## A. Which directions are favored?

For a declared physical domain `D`,

```math
\mathcal S_{X|D}
=\lambda_D/[Tr(G_DX)/TrX]
```

measures the strongest admissible response relative to the actual ensemble average.

## B. What total activity is certified by the response?

The maximum-capacity inversion gives

```math
\tau_{X|D}
=Tr(G_DX)/(\lambda_DTrX),
```

with

```math
S_{X|D}tau_{X|D}=1.
```

The domain declaration is essential. A capacity maximum over irrelevant or inaccessible directions would have no physical meaning.

## C. Does internal activity survive to a terminal?

Each terminal has a positive observability effect `G_i(omega)`. A null to one channel forces the corresponding cross contribution to vanish. Changing the readout physics changes the observability operator and can lift or create such nulls.

These are spectrally related questions, not identical experiments.

The bright-state `N_eff` result is a quantum state-discrimination theorem. The HgCdTe result is an equilibrium one-body resource bound. The recycling result is a stochastic readout theorem. Their independent physical derivations are what make the common geometry informative rather than merely notational.

The production HgCdTe calculation gives a useful example of why the decomposition matters. Its global thermal selectivity `~1.746` does not arise from within-shell bright-state concentration; that mechanism is symmetry forbidden in the current BIA-neglecting model. It arises from a globally defined capacity that exceeds the thermally weighted average shell capacity. The observable bound is then reduced further by the Fermi/Kubo factor.

The framework does not imply that conventional detector figures are defective or obsolete. A scalar metric is appropriate for the experiment it defines. The point is that once the task, microscopic resource, or readout observable changes, the omitted spectral geometry can become decisive.

Important boundaries remain:

```text
- the optical population theorem requires a selected direct cross-mu conductivity contribution;
- it does not cover arbitrary many-body, excitonic, or phonon-assisted response;
- coherence selectivity requires preserved/extractable coherence;
- the BIA-neglecting Kane validation is a model, not the full zincblende band structure;
- endpoint Poisson cancellation fails for branching, interacting lineages, correlated generation, or shared electronics;
- finite-frequency Ramo support does not guarantee a measurable ensemble cross-spectrum.
```

---

# X. Conclusion

A physically declared detector domain has both a strongest allowed response and an ensemble-average response. Their ratio is the forward selectivity of that stage. The same ratio is exactly the reciprocal of how tightly a maximum-capacity inversion can certify the total activity that produced the response:

```math
\boxed{
\frac{\lambda_D}{Tr(G_DX)/TrX}
\times
\frac{Tr(G_DX)}{\lambda_DTrX}
=1.
}
```

This simple reciprocity becomes physically nontrivial through its detector specializations.

For a uniform task ensemble it reduces to a stable-rank concentration factor and forces a quantitative loss on another task at fixed total response strength. For a rank-one coherent detector it recovers the full nonuniform `N_eff` rejection factor against a population-matched incoherent state. For the endpoint-lifted thermal space of a semiconductor it becomes the reciprocal capacity tightness of an optical state-count theorem, while an exact Fermi/Kubo factor connects that internal response to the selected cross-chemical-potential conductivity.

In the production second-order eight-band HgCdTe validation, the active-population bound tightness `0.1757` factors into `0.5726` from shell-to-global capacity variation and `0.3068` from Fermi/Kubo asymmetry. The absence of an additional within-shell selectivity penalty is enforced by the `PT` symmetry of the BIA-neglecting validation model and should not be generalized to full zincblende HgCdTe.

Downstream, terminal-specific observability effects determine whether internal activity reaches the readout. Conservative photon recycling can be exactly null to a source terminal under ideal final-sink counting, whereas finite-transit Shockley–Ramo motion can lift that channel null at finite frequency despite zero integrated charge for an internally created and recombined pair segment.

The common result is therefore not a replacement scalar for `D*`, responsivity, or noise. It is a spectral accounting principle: the same detector can be selective, resource-informative, or blind depending on which physical map and admissible domain connect the quantity of interest to the measurement.

---

# References — Rev. 3 working set

1. H. H. Barrett, J. L. Denny, R. F. Wagner, and K. J. Myers, task-based image-quality assessment using Fisher-information and crosstalk matrices, *J. Opt. Soc. Am. A* **12**, 834–852 (1995), DOI: 10.1364/JOSAA.12.000834.
2. E. Clarkson and F. Shen, Fisher-information kernels as task-based figures of merit, *J. Opt. Soc. Am. A* **27**, 2313–2326 (2010), DOI: 10.1364/JOSAA.27.002313.
3. S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Phys. Rev. A* **98**, 063835 (2018), DOI: 10.1103/PhysRevA.98.063835.
4. H. Xu et al., “Experimental Quantification of Coherence of a Tunable Quantum Detector,” *Phys. Rev. Lett.* **125**, 060404 (2020), DOI: 10.1103/PhysRevLett.125.060404.
5. Y. Onishi and L. Fu, “Fundamental Bound on Topological Gap,” *Phys. Rev. X* **14**, 011052 (2024).
6. D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury, “Low-energy optical absorption in correlated insulators: Projected sum rules and the role of quantum geometry,” *Phys. Rev. B* **112**, 075116 (2025).
7. E. G. Novik et al., “Band structure of semimagnetic Hg1-yMnyTe quantum wells,” *Phys. Rev. B* **72**, 035321 (2005), DOI: 10.1103/PhysRevB.72.035321.
8. X. Cartoixa, D. Z.-Y. Ting, and T. C. McGill, eight-band zincblende modeling including bulk inversion asymmetry, arXiv:cond-mat/0212394 and associated publication.
9. W. van Roosbroeck and W. Shockley, “Photon-Radiative Recombination of Electrons and Holes in Germanium,” *Phys. Rev.* **94**, 1558–1560 (1954).
10. W. Dąbrowski, semiconductor-detector impulse response and generation–recombination noise with transport/Ramo coupling, *Prog. Quantum Electron.* **13**, 233–266 (1989), DOI: 10.1016/0079-6727(89)90004-9.
11. W. Dąbrowski, comments on collective and corpuscular generation–recombination noise in a p-n junction, *Solid-State Electron.* **30**, 205–208 (1987), DOI: 10.1016/0038-1101(87)90150-X.
12. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe photodiodes, *Opt. Eng.* **50**, 061003 (2011).
13. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe heterostructure photodiodes, *J. Electron. Mater.* **41**, 2766–2774 (2012), DOI: 10.1007/s11664-012-2093-7.
14. A. Jóźwikowska and K. Jóźwikowski, photon reabsorption and optical crosstalk in HgCdTe photodiode arrays, *Opt. Quantum Electron.* **51**, 85 (2019), DOI: 10.1007/s11082-019-1781-4.
15. M. Kopytko et al., “Photon recycling effect in small pixel p-i-n HgCdTe long wavelength infrared photodiodes,” *Infrared Phys. Technol.* **97**, 38–42 (2019), DOI: 10.1016/j.infrared.2018.12.015.
16. A. Mirasol, Poisson output of the `M/G/infinity` queue, *Operations Research* **11**, 282 (1963), DOI: 10.1287/opre.11.2.282.
17. J. M. Harrison and A. J. Lemoine, open networks of infinite-server queues, *J. Appl. Prob.* **18** (1981), DOI: 10.2307/3213306.

**Reference-production note:** the final reference set must still import and independently verify the complete primary-source networks from Experiments 01, 09, and 12, including the exact empirical HgCdTe gap/parameter citations. The present list is a scientific working set, not final journal formatting.
