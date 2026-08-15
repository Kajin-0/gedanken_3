# Spectral geometry of photodetection: selectivity, resource certification, and hidden internal dynamics

**Unified manuscript — Rev. 2**  
**Date:** 2026-08-15  
**Status:** central-theorem revision after Rev. 1 hostile review; scientific draft, not submission formatted

---

## Abstract

Photodetector figures of merit compress a specified experiment to a small number of scalars, while detector response itself is distributed over signal tasks, microscopic excitation channels, and terminal observables. We show that several detector-specific limits derived independently are linked by the spectral geometry of the physical map relevant to each stage of detection. For any positive coupling operator `G` and positive internal activity or population operator `X`, the response of the brightest available direction relative to the actual ensemble-average response is exactly the reciprocal of the fraction of total activity certified when the measured response `Tr(GX)` is inverted using only the maximum per-direction capacity `lambda_max(G)`. The maximally mixed case reduces to a stable-rank relation and, at fixed total coupling strength, yields a quantitative task penalty for spectral concentration. A rank-one coherent photodetector recovers the full nonuniform coherence dimension `N_eff=1/sum_j w_j^2` as this selectivity factor. In an equilibrium semiconductor, an exact Fermi inequality and the selected direct cross-chemical-potential Kubo conductivity turn the same capacity structure into a lower bound on the population of optically active one-body states. For dispersive bands, the bound tightness decomposes into Fermi asymmetry, shell-to-global capacity utilization, and inverse shell selectivity. A production-resolution eight-band HgCdTe calculation gives a capacity factor `0.573`, a Fermi/Kubo factor `0.307`, and their product `0.1757`, while every contributing active shell is locally singular-value isotropic. Finally, a complete-lineage shot-noise theorem shows that conservative photon recycling can be exactly invisible to ideal final-sink counting under independent Poisson-lineage assumptions, whereas an internally created and recombined Shockley–Ramo segment has zero DC charge but can carry finite-frequency terminal waveform support. The results separate task preference, microscopic resource inference, and internal-process observability without proposing a new universal scalar detector metric.

---

# I. Introduction

Specific detectivity, responsivity, quantum efficiency, bandwidth, noise-equivalent power, dark current, and timing jitter are useful because they compress a detector experiment into quantities that can be compared. Their validity does not imply that any one scalar should rank every optical task or reveal every internal process. Task-based detection theory, quantum measurement theory, and semiconductor readout theory have long made this distinction in their respective domains.

The question here is narrower: **can detector-specific results that appear unrelated become quantitatively connected once the full coupling map is retained?**

Four independently developed problems motivate the question.

First, a detector normalized to have the same eventual matched-filter sensitivity as another detector can still have different finite-time performance. In a transient experiment with uncertain arrival time, shortening the detector time scale accelerates evidence accumulation but increases the normalized timing-search interval for the same physical uncertainty window. A continuous-time construction gives a fast-to-slow reversal of a conservative sufficient global-false-alarm guarantee. The theorem is not that faster detectors are worse; it is that one scalar event-specific sensitivity does not determine the ordering of all finite-time tasks.

Second, optical absorption may prepare a coherent bright superposition while internal dark generation prepares exactly the same microscopic populations incoherently. A suitable coherent readout can distinguish these states even when energy, charge, and basis populations match.

Third, optical response itself can be used inversely. For direct transitions crossing the chemical potential, finite selected optical spectral weight requires a minimum equilibrium population of the electronic endpoint states when the optical velocity block has finite capacity.

Fourth, internal dynamics need not be visible at the terminals. Conservative photon recycling can alter mean crosstalk and internal population fluctuations while ideal final-sink count streams remain independent. A finite-transit junction can respond differently because carrier motion induces current before recombination or collection.

We do not identify the physical operators in these problems with one another. The detector chain is staged,

```math
\mathcal H_{task}
\xrightarrow{M_{opt}}
\mathcal H_{exc}
\xrightarrow{M_{dyn}}
\mathcal H_{int}
\xrightarrow{M_{ro}(\omega)}
\mathcal H_{term},
```

and the relevant map depends on the question. At a specified stage, however, quadratic response is governed by a positive operator

```math
G=M^\dagger M
```

or by the positive effect appropriate to that measurement. The common structure is that the spectrum and null geometry of the relevant map determine what is preferentially measured, what total activity can be inferred from the response, and what can remain hidden.

The central theorem below is deliberately simple mathematically. Its significance lies in the fact that its two sides correspond to independent detector questions: a **forward selectivity problem** and an **inverse resource-certification problem**. The later sections show that the same relation recovers the nonuniform coherence dimension of a bright-state detector and the global thermal capacity tightness of an optical population bound, while a shell-resolved decomposition explains the realistic HgCdTe result. A separate downstream theorem then addresses stochastic observability of photon recycling.

---

# II. Activity-weighted selectivity and inverse resource certification

## A. Positive activity pairing

Let

```math
G\succeq0,
\qquad
G\ne0
```

be the positive coupling/effect operator relevant to one specified detector stage. Let

```math
\lambda_+
=\lambda_{max}(G)>0.
```

Let

```math
X\succeq0,
\qquad
N_X=TrX>0
```

represent the internal activity, population, covariance, or ensemble weight whose coupling to the detector is being interrogated.

Normalize it as

```math
\boxed{
\rho_X=X/TrX.
}
```

The measured quadratic response is

```math
\boxed{
Q_X=Tr(GX),
}
```

and the average response per unit activity is

```math
\boxed{
\bar q_X
=Tr(G\rho_X)
=\frac{Tr(GX)}{TrX}.
}
```

The largest response available to any normalized pure direction is `lambda_+`.

## B. Forward selectivity

Define the activity-weighted response selectivity

```math
\boxed{
\mathcal S_X
=\frac{\lambda_+}{Tr(G\rho_X)}
=\frac{\lambda_+TrX}{Tr(GX)}
}
```

when `Tr(GX)>0`.

`S_X` asks how much more strongly the detector stage can respond to its brightest direction than it responds, on average, to the **actual ensemble `rho_X`**.

This is a generic response ratio. A quantum-optimal discrimination interpretation requires additional structure and is invoked only where separately proved.

## C. Inverse capacity estimate

Positivity gives the spectral-capacity inequality

```math
Tr(GX)
\le
\lambda_+TrX.
```

If one knows the observed response but retains only the maximum per-direction capacity `lambda_+`, the corresponding lower estimate of total activity is

```math
\boxed{
N_{cap}
=\frac{Tr(GX)}{\lambda_+}.
}
```

Define the fraction of true activity certified by this inversion:

```math
\boxed{
\tau_X
=\frac{N_{cap}}{N_X}
=\frac{Tr(GX)}{\lambda_+TrX}.
}
```

Therefore

```math
\boxed{
\mathcal S_X\tau_X=1.
}
```

This is the central reciprocity.

The algebra is a normalized form of the upper spectral bound and is not proposed as new matrix theory. The detector statement is that the same physical coupling map gives reciprocal answers to two independently meaningful questions:

```text
forward:
    how selective can the detector be relative to the actual internal ensemble?

inverse:
    how much of that ensemble's total activity can its observed response certify
    when only the maximum allowed coupling per direction is used?
```

Strong concentration improves the first quantity and weakens the second by exactly the reciprocal factor.

If

```math
Tr(GX)=0,
```

then positive activity lies entirely in the null space of the map on its support. The certified fraction is zero and the activity is completely hidden from that observable.

---

# III. Stable rank and task ordering as the uniform-ensemble limit

## A. Stable rank

Let `G` act on a `d`-dimensional comparison subspace and choose the maximally mixed activity

```math
X=I_d.
```

Then

```math
TrX=d
```

and

```math
Tr(G\rho_X)=TrG/d.
```

Define

```math
T=TrG,
```

and stable rank

```math
\boxed{
r_{st}=T/\lambda_+.
}
```

The activity-weighted theorem becomes

```math
\boxed{
\mathcal S_{mix}
=\frac{d}{r_{st}},
\qquad
\tau_{mix}
=\frac{r_{st}}{d}.
}
```

Thus stable rank is the uniform-ensemble specialization, not the fundamental object for arbitrary activity distributions.

## B. Equal-trace task comparator

The equal-total-strength isotropic comparator is

```math
\boxed{
G_{iso}=\frac{T}{d}I_d.
}
```

For a normalized task `|s>`, the quadratic task response is

```math
q_G(s)=\langle s|G|s\rangle.
```

The maximum task advantage over `G_iso` is

```math
\boxed{
\mathcal A_{max}
=\frac{\lambda_+}{T/d}
=\frac{d}{r_{st}}
=\mathcal S_{mix}.
}
```

Hence, for a uniform task ensemble, best-task advantage, mixed-ensemble response selectivity, and reciprocal capacity tightness coincide.

## C. No-free-selectivity task penalty

A fixed trace prevents concentration from improving every direction. Since

```math
\sum_{j=2}^d\lambda_j=T-\lambda_+,
```

at least one orthogonal eigen-direction satisfies

```math
\boxed{
\frac{q_{worst}}{q_{iso}}
\le
\frac{d-\mathcal S_{mix}}{d-1}.
}
```

The guaranteed fractional loss on at least one task is

```math
\boxed{
\mathcal L_{task}
\ge
\frac{\mathcal S_{mix}-1}{d-1}.
}
```

The result is tight when the remaining `d-1` eigenvalues are equal.

If two positive task-information operators have equal trace but are unequal, their difference is nonzero Hermitian trace-zero and is therefore indefinite. There exist tasks with opposite detector orderings.

This supplies an exact geometric ordering result. It should not be confused with the separate unknown-arrival transient theorem that motivated the present program. That physical construction equalizes eventual event-specific matched-filter SNR for one waveform and includes a correlated timing search; it does not require equal traces of the full information operators.

---

# IV. Coherence-selective photodetection: exact recovery of `N_eff`

Consider `N` degenerate microscopic excited states `|j>` and an accepted optical mode that prepares

```math
|B\rangle
=\sum_{j=1}^{N}
\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

with

```math
w_j\ge0,
\qquad
\sum_jw_j=1.
```

The photon-created state is

```math
\rho_\gamma=|B\rangle\langle B|.
```

Construct an incoherent internal event with exactly the same populations,

```math
\rho_D
=\sum_jw_j|j\rangle\langle j|.
```

Any observable diagonal in the microscopic basis is blind to the difference.

Use the bright projector

```math
\boxed{
G_{B}=\Pi_B=|B\rangle\langle B|.
}
```

Its largest eigenvalue is one. The photon state is accepted with probability

```math
Tr(\Pi_B\rho_\gamma)=1,
```

whereas the incoherent state is accepted with probability

```math
Tr(\Pi_B\rho_D)
=\sum_jw_j^2.
```

Therefore the Experiment-II activity-weighted selectivity for

```math
X=\rho_D
```

is

```math
\boxed{
\mathcal S_{\rho_D}
=\frac1{\sum_jw_j^2}
\equiv N_{eff}.
}
```

This recovers the full nonuniform coherence dimension exactly, not merely the uniform case.

Here the generic response ratio has an additional operational meaning. For any yes/no POVM element `E` with unit acceptance of `|B>`, `|B>` must be a unit-eigenvalue eigenvector, so

```math
Tr(E\rho_D)
\ge
Tr(\Pi_B\rho_D).
```

Thus the bright projector is the minimum-dark-acceptance measurement subject to unit signal acceptance, and the conditional rejection factor is exactly `N_eff`.

The reciprocal inverse-certification statement is

```math
\boxed{
\tau_{\rho_D}
=\sum_jw_j^2
=1/N_{eff}.
}
```

The most coherence-selective ensemble is correspondingly the least completely identifiable from the selected response when only its unit per-direction capacity is retained.

For `w_j=1/N`,

```math
N_{eff}=N.
```

This is the rank-one/stable-rank endpoint, but the activity-weighted theorem shows that uniformity is not required.

Coherence discrimination is not by itself a complete detector architecture. Dephasing, extraction kinetics, detailed balance, and finite-density dark generation remain independent constraints.

---

# V. Direct optical response and thermal population

We now apply the inverse side of the reciprocity to a physical semiconductor response.

The theorem concerns the selected **direct cross-chemical-potential contribution** to the optical conductivity. A raw total measured conductivity may contain additional channels and cannot in general be inserted without decomposition or a regime in which the selected contribution is isolated.

## A. Fermi endpoint inequality

Let `|v>` and `|c>` be exact one-particle eigenstates with

```math
E_v<\mu<E_c,
```

and

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

The exact Fermi occupations obey

```math
\boxed{
\frac{2D_{cv}}
{e^{E_{cv}/(2k_BT)}-1}
\le
p_c+h_v.
}
```

Equality occurs only for mirror-symmetric excitation energies about `mu`:

```math
E_c-\mu=\mu-E_v=E_{cv}/2.
```

## B. Selected Kubo conductivity

For physical velocity polarization `i`, let

```math
v_{cv}=\langle c|\hat v_i|v\rangle.
```

The selected positive-frequency cross-`mu` conductivity is

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

Define the exact thermal kernel

```math
\boxed{
K_T(E)
=\frac{E}{e^{E/(2k_BT)}-1}.
}
```

For any selected positive-frequency window `B`, the pointwise Fermi inequality gives

```math
\boxed{
\mathcal R_B
\ge
\mathcal L_B
\equiv
\frac{2}{\pi e^2}
\int_B
K_T(\hbar\omega)
\sigma_1^{cross}(\omega)d\omega,
}
```

where `R_B` is the exact thermally weighted selected squared-velocity strength.

## C. Direct-sum endpoint operator

Let `P_epsilon` project onto the complete exact one-particle eigenspace at energy `epsilon`.

For every selected upper shell define

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,B},
```

where `Q^-` contains all lower-shell partners in the optical window. For every lower shell define

```math
B_{\epsilon_v,B}
=Q^+_{\epsilon_v,B}\hat v_iP_{\epsilon_v}.
```

Construct the positive endpoint Gram operator

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

Its spectral edge is exactly the basis-invariant optical-velocity capacity:

```math
\boxed{
\lambda_{max}(G_B)
=(v_B^{cap})^2.
}
```

For the active theorem, let `P_a^{act}` project onto the support of each endpoint Gram block and define the thermal activity operator

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
\frac1VTrX_B^{act}
=n_{e,B}^{act}+n_{h,B}^{act}
\equiv n_B^{act},
}
```

and

```math
\boxed{
\frac1VTr(G_BX_B^{act})
=\mathcal R_B.
}
```

The activity-weighted theorem therefore gives the **global thermal capacity reciprocity**

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

and exactly

```math
\boxed{
\mathcal S_{th,B}^{act}\tau_{cap}^{act}=1.
}
```

The actual optical observable contains the additional Fermi/Kubo step,

```math
\eta_F=\mathcal L_B/\mathcal R_B\le1.
```

Hence

```math
\boxed{
\tau_{obs}^{act}
=\frac{\mathcal L_B}{(v_B^{cap})^2n_B^{act}}
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

Finally, because the active population is no larger than the total electron-plus-hole population,

```math
\boxed{
 n_e+n_h
 \ge
 n_B^{act}
 \ge
 \frac{2}{\pi e^2(v_B^{cap})^2}
 \int_B
 \frac{\hbar\omega\sigma_1^{cross}(\omega)}
 {e^{\hbar\omega/(2k_BT)}-1}
 d\omega.
}
```

The physical theorem is thus a direct realization of inverse resource certification, with a separate exact statistical conversion from the selected conductivity to the internal velocity-strength response.

---

# VI. Why is the thermal bound loose? Shell-resolved decomposition

The global reciprocity gives

```math
\mathcal S_{th,B}^{act}=1/\tau_{cap}^{act}
```

but does not identify the microscopic origin of the global selectivity.

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

and the local active response selectivity

```math
\boxed{
\mathcal S_a^{act}
=\frac{r_a}{r_{st,a}}.
}
```

Define shell utilization of the global capacity

```math
\boxed{
c_a=\frac{\lambda_a}{(v_B^{cap})^2}}
```

and normalized thermal active-population weights

```math
\boxed{
w_a^{act}
=\frac{p_ar_a}{\sum_bp_br_b}.
}
```

Then

```math
\boxed{
\tau_{cap}^{act}
=\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

Equivalently,

```math
\boxed{
\mathcal S_{th,B}^{act}
=
\left[
\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}
\right]^{-1}.
}
```

The full observable tightness is

```math
\boxed{
\tau_{obs}^{act}
=\eta_F
\sum_aw_a^{act}
\frac{c_a}{\mathcal S_a^{act}}.
}
```

Thus a global thermal ensemble can lie far below the maximum capacity for two distinct spectral reasons:

```text
within-shell concentration:
    S_a^act > 1;

between-shell capacity variation:
    c_a < 1.
```

The Fermi/Kubo factor `eta_F` is independent of both.

---

# VII. Production eight-band HgCdTe validation

We evaluate the preceding identities in the same bulk second-order eight-band Kane model used for the 300-K, 10-um-class HgCdTe validation of the thermal-population theorem.

For the broad selected transition-energy window

```text
E_g <= Delta E <= 0.5 eV,
```

the production quadrature gives

```text
charge-neutral chemical potential
    mu = 0.1354615 eV,

cross-mu reference electron+hole population
    n_ref = 1.0051405e17 cm^-3,

exact selected thermal velocity strength
    R_B = 3.9874202e28 cm^-3 (m/s)^2,

selected observable Fermi/Kubo functional
    L_B = 1.2234865e28 cm^-3 (m/s)^2,

active thermal population
    n_B^act = 6.7241114e16 cm^-3.
```

The separately validated continuous ordinary-supremum capacity is

```text
v_B^cap = 1.01764e6 m/s.
```

Therefore

```math
\boxed{
\eta_F
=\mathcal L_B/\mathcal R_B
=0.30684,
}
```

```math
\boxed{
\tau_{cap}^{act}
=0.57262,
}
```

and

```math
\boxed{
\tau_{obs}^{act}
=0.17570.
}
```

The decomposition closes:

```math
0.30684\times0.57262=0.17570.
```

The corresponding global thermal activity-weighted selectivity is

```math
\boxed{
\mathcal S_{th,B}^{act}
=1/0.57262
\approx1.746.
}
```

The shell audit reveals where this factor comes from. For every thermally important selected **active** exact-shell block,

```math
\boxed{
\mathcal S_a^{act}=1
}
```

to numerical precision; the maximum observed departure from unity is approximately `4e-14`.

Thus the realistic HgCdTe result is not loose because oscillator strength is concentrated into one coherent singular direction within each active shell. Instead,

```text
within-shell selectivity factor:       1;
thermal weighted global capacity use: ~0.573;
Fermi/Kubo conversion:                 ~0.307;
final active tightness:                ~0.1757.
```

This distinction is important. The coherent bright-state detector of Sec. IV and the realistic HgCdTe absorber occupy different regimes of the same spectral accounting. The framework identifies that difference rather than forcing both systems into one mechanism.

The lower bound remains approximately `11.8%` of the full cross-`mu` reference thermal population and approximately `17.6%` of the selected optically active population.

---

# VIII. Downstream observability: conservative photon recycling

The preceding sections concern task and microscopic optical coupling. A second loss of information occurs when internal stochastic dynamics are mapped to terminal currents.

## A. Complete-lineage spectrum

Let independent primary event classes `a` arrive as Poisson processes of rates `Lambda_a`. One primary event produces a complete random multichannel terminal waveform

```math
\mathbf h_a(t)
```

with Fourier transform

```math
\mathbf H_a(\omega).
```

The marked-Poisson shot-noise spectrum is

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

Interterminal cross-noise is complete-lineage waveform overlap. Internal routing by itself does not guarantee terminal correlation.

## B. Internal exchange can be strongly correlated

For a symmetric two-pixel carrier-occupancy model with local non-transfer relaxation `gamma`, conservative exchange rate `k`, and stationary mean `m`, the internal population cross-spectrum is

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

It changes sign at

```math
\boxed{
\omega_x=\sqrt{\gamma(\gamma+2k)}.
}
```

Thus internal conservative exchange is dynamically visible in an occupancy-sensitive observable.

## C. Ideal final-sink counting can erase it exactly

Now impose the endpoint-counting assumptions:

```text
Poisson primary generation;
independent noninteracting complete lineages;
one final sink per primary lineage;
measurement records only the final sink event;
no branching/gain producing multiple recorded descendants;
no common electronic coupling between output channels.
```

A lineage may undergo arbitrarily many independent recycling/routing steps before its final sink. Marking each primary event by its final sink and final delay produces independent Poisson output streams for distinct sink classes.

Hence

```math
\boxed{
S_{I,12}^{end}(\omega)=0
}
```

for all frequencies in the ideal endpoint-counting model, even when internal occupancy correlations and deterministic mean crosstalk are nonzero.

## D. Finite-transit Shockley–Ramo motion changes the map

Let `phi_k(r)` be the weighting potential for electrode `k`. An electron-hole pair produces induced current

```math
\boxed{
 i_k(t)
 =e\frac{d}{dt}
 [\phi_k(\mathbf r_e(t))-\phi_k(\mathbf r_h(t))].
}
```

If the pair is created internally at one point and later recombines internally at a common point,

```math
\boxed{
Q_k^{rec}=\int i_k(t)dt=0
}
```

for every electrode.

Its finite-frequency waveform is

```math
\boxed{
H_k^{rec}(\omega)
=i\omega e
\int\Delta\phi_k(t)e^{-i\omega t}dt,
}
```

so

```math
H_k^{rec}(0)=0
```

while an individual trajectory can carry finite-frequency support.

For a conservative A-to-B recycling lineage,

```text
pair created in A
-> carrier motion in A
-> internal radiative recombination in A
-> photon reabsorption in B
-> carrier motion and final collection in B,
```

a localized-weighting-field representation has

```math
\mathbf H_{A\to B}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}.
```

The source component is rigorously zero at DC but can be nonzero at finite frequency. Therefore finite-transit Ramo readout can lift the endpoint-counting null and permit conservative recycling to contribute to interterminal AC correlations.

This does not guarantee a measurable ensemble cross-spectrum in every geometry. Symmetry, opposing lineage classes, weighting-field cancellation, and electronics can still suppress the ensemble overlap.

The scientific boundary is therefore:

```text
same conservative internal recycling process
+
final-sink-only map
    -> exact one-terminal lineage support and zero endpoint cross-noise;

same internal process
+
finite-transit Ramo map
    -> zero source-pixel DC charge for an internally recombined stage,
       but finite-frequency multichannel lineage support becomes allowed.
```

---

# IX. Discussion

The results separate three detector questions that are often mixed together.

## A. Forward selectivity

Given a physical map, which input or internal direction is favored relative to the activity ensemble that is actually present?

This is controlled by

```math
\mathcal S_X
=\lambda_{max}(G)/Tr(G\rho_X).
```

## B. Inverse certification

Given the measured response, how much total activity is forced if one knows only the largest possible response per direction?

This is controlled by

```math
\tau_X
=Tr(GX)/[\lambda_{max}(G)TrX],
```

with

```math
S_X tau_X=1.
```

## C. Observability after internal evolution

Does an internal process contribute to more than one terminal waveform after all routing, recombination, and readout dynamics are included?

This is controlled by complete-lineage terminal waveform overlap, not merely by the existence of internal coupling.

These quantities are related spectrally but are not operationally interchangeable. The bright-state `N_eff` result is a quantum discrimination theorem. The thermal HgCdTe result is an inverse equilibrium one-body theorem. The recycling result is a stochastic readout theorem.

The unification is useful because it exposes where information is lost.

For the optical population theorem, the measured-to-resource chain contains two separate reductions:

```text
cross-mu conductivity functional
    -- Fermi inequality -->
exact thermal velocity strength
    -- spectral capacity -->
minimum active population.
```

The production HgCdTe decomposition quantifies those reductions and shows that local singular anisotropy is not responsible for the realistic slack.

For photon recycling, the loss occurs downstream: a final-sink-only readout discards all pre-terminal history of a conservative lineage. A Ramo-sensitive finite-transit readout retains part of that history.

No new universal scalar metric follows from these observations. Conventional detector metrics remain appropriate within their intended experiments. The claim is instead that a scalar compression can be understood by asking which spectral or lineage information has been retained and which has been discarded.

Several boundaries remain important.

The optical population theorem requires an isolated or modeled direct cross-`mu` conductivity contribution and a finite selected velocity capacity. It does not cover arbitrary many-body optical states, excitons, phonon-assisted absorption, intentional nonequilibrium carrier populations, or unconstrained photonic path enhancement.

The coherent bright-state result requires preservation and extraction of the relevant coherence; its conditional rejection factor is not by itself a complete dark-count prediction.

The Poisson endpoint theorem fails for branching gain, correlated generation, interacting lineages, shared electronics, or any measurement that records pre-final-sink motion.

---

# X. Conclusion

A detector response map contains both a preferred-direction problem and an inverse-resource problem.

For any positive internal activity `X` coupled through a positive operator `G`,

```math
\boxed{
\underbrace{\frac{\lambda_{max}(G)}{Tr(GX)/TrX}}
_{\text{brightest-direction response relative to actual ensemble}}
\times
\underbrace{\frac{Tr(GX)}{\lambda_{max}(G)TrX}}
_{\text{fraction of total activity certified by max-capacity inversion}}
=1.
}
```

This general reciprocity contains the stable-rank task-selectivity relation as the maximally mixed special case. In a rank-one coherence-selective detector it reproduces the full nonuniform `N_eff` rejection factor. In the direct-sum thermal endpoint space of an equilibrium semiconductor it gives the exact reciprocal of the optical velocity-capacity tightness, while a separate Fermi/Kubo factor connects that internal response to the selected cross-chemical-potential conductivity.

The production eight-band HgCdTe example then resolves the physical source of its finite bound tightness: the active exact-shell blocks themselves are singular-value isotropic, while shell-to-global capacity variation contributes a factor `0.573` and Fermi asymmetry contributes `0.307`, yielding the observed active-population tightness `0.1757`.

Downstream, a different map determines whether internal dynamics reach the terminals. Conservative photon recycling can be completely erased by ideal final-sink counting even when internal populations are correlated, whereas finite-transit Shockley–Ramo motion can give an internally recombined stage finite-frequency terminal support despite its rigorously zero integrated charge.

The resulting framework does not replace `D*`, responsivity, or any other detector figure with a new scalar. It identifies the spectral and dynamical information that those scalars omit, and it shows how that omitted structure controls task ordering, microscopic resource certification, and terminal observability.

---

# References — Rev. 2 working set

1. H. H. Barrett, J. L. Denny, R. F. Wagner, and K. J. Myers, task-based image-quality assessment using Fisher-information and crosstalk matrices, *J. Opt. Soc. Am. A* **12**, 834–852 (1995), DOI: 10.1364/JOSAA.12.000834.
2. E. Clarkson and F. Shen, Fisher-information kernels as task-based figures of merit, *J. Opt. Soc. Am. A* **27**, 2313–2326 (2010), DOI: 10.1364/JOSAA.27.002313.
3. S. M. Young, M. Sarovar, and F. Léonard, “General modeling framework for quantum photodetectors,” *Phys. Rev. A* **98**, 063835 (2018), DOI: 10.1103/PhysRevA.98.063835.
4. H. Xu et al., “Experimental Quantification of Coherence of a Tunable Quantum Detector,” *Phys. Rev. Lett.* **125**, 060404 (2020), DOI: 10.1103/PhysRevLett.125.060404.
5. Y. Onishi and L. Fu, “Fundamental Bound on Topological Gap,” *Phys. Rev. X* **14**, 011052 (2024).
6. D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury, “Low-energy optical absorption in correlated insulators: Projected sum rules and the role of quantum geometry,” *Phys. Rev. B* **112**, 075116 (2025).
7. E. G. Novik et al., eight-band `k.p` model used for HgTe/HgCdTe parameterization, *Phys. Rev. B* **72**, 035321 (2005).
8. W. van Roosbroeck and W. Shockley, “Photon-Radiative Recombination of Electrons and Holes in Germanium,” *Phys. Rev.* **94**, 1558–1560 (1954).
9. W. Dąbrowski, semiconductor-detector impulse response and generation–recombination noise with transport/Ramo coupling, *Prog. Quantum Electron.* **13**, 233–266 (1989), DOI: 10.1016/0079-6727(89)90004-9.
10. W. Dąbrowski, comments on collective and corpuscular generation–recombination noise in a p-n junction, *Solid-State Electron.* **30**, 205–208 (1987), DOI: 10.1016/0038-1101(87)90150-X.
11. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe photodiodes, *Opt. Eng.* **50**, 061003 (2011).
12. K. Jóźwikowski, M. Kopytko, and A. Rogalski, photon recycling in HgCdTe heterostructure photodiodes, *J. Electron. Mater.* **41**, 2766–2774 (2012), DOI: 10.1007/s11664-012-2093-7.
13. A. Jóźwikowska and K. Jóźwikowski, photon reabsorption and optical crosstalk in HgCdTe photodiode arrays, *Opt. Quantum Electron.* **51**, 85 (2019), DOI: 10.1007/s11082-019-1781-4.
14. M. Kopytko et al., “Photon recycling effect in small pixel p-i-n HgCdTe long wavelength infrared photodiodes,” *Infrared Phys. Technol.* **97**, 38–42 (2019), DOI: 10.1016/j.infrared.2018.12.015.
15. A. Mirasol, Poisson output of the `M/G/infinity` queue, *Operations Research* **11**, 282 (1963), DOI: 10.1287/opre.11.2.282.
16. J. M. Harrison and A. J. Lemoine, open networks of infinite-server queues, *J. Appl. Prob.* **18** (1981), DOI: 10.2307/3213306.

**Reference-production note:** import and independently verify the full Experiment-01, Experiment-09, and Experiment-12 primary-source networks before any journal-facing typeset revision. The exact HgCdTe empirical band-gap reference also remains to be imported from the controlling Experiment-12 bibliography.
