# Efficiency-controlled dark-count scaling transition in a coherence-selective photodetector

**Draft status:** Rev. 1 / rebuilt after hostile referee review  
**Date:** 2026-08-14  
**Scope:** analytical/theoretical  
**Novelty status:** not established; no priority language authorized

## Abstract

A photon can prepare a coherent material excitation that occupies the same local populations as an incoherently generated internal dark event. We study whether this state-space distinction can change detector scaling when the absorber contains `N` independent dark-generation sites. A bright-selective extractor with rate `kappa` competes with local dephasing at rate `gamma`. For a fixed required conditional internal collection efficiency `eta`, we derive a sharp large-`N` boundary at

```math
\eta_c=\frac{\kappa}{\kappa+\gamma}.
```

Below this boundary, the minimum detection gate and accepted local-dark mean remain `O(1)` even though raw dark generation is `O(N)`. At the boundary they scale as `Theta(log N)` and `Theta((log N)^2)`, respectively. Above it, the gate grows as `O(N)` and the accepted dark mean as `O(N^2)`. The no-dephasing `N` cancellation appears as a limiting corollary. The result identifies an efficiency-dependent scalability condition for coherence-selective photodetection and separates it from ordinary physical-volume dark-current suppression.

---

# 1. Introduction

Photodetector dark events can originate from thermal generation, generation-recombination centers, tunneling, switching, multiplication fluctuations, and other internal processes. A common device-level concern is extensivity: increasing the amount of electrically active material generally increases the number of microscopic locations from which an internal event can originate. Established detector strategies therefore suppress dark current or dark counts through material quality, energetic barriers, cooling, reduced electrical volume, field engineering, or architectures that separate optical collection area from electrically active area.

This paper asks a different, deliberately idealized question. Suppose one absorbed photon and one internally generated dark event produce exactly the same excitation energy, exactly one excitation, and exactly the same local-state populations. Can the detector nevertheless respond differently to them?

The answer can be yes if the two events occupy different **directions in excitation Hilbert space**. An optical mode can prepare one coherent bright superposition of `N` local excited states, while independent local dark processes prepare the corresponding incoherent local mixture. Energy, excitation number, and all observables diagonal in the local basis are then intentionally useless for provenance discrimination. Only coherence distinguishes the event classes.

The static geometry of this construction is not new. Quantum-state discrimination and detector-POVM theory already establish that a pure coherent state can be distinguished from its dephased mixture. Likewise, selecting one normalized coherent mode from isotropic independent noise is standard mode-filtering geometry. Collective bright and dark states, dephasing-induced scattering between them, coherence-sensitive photocurrent, and quantum-coherent photodetector models are all established [1-6]. The purpose here is therefore not to relabel the `1/N` bright-state overlap as a new principle.

Instead, we ask a detector-operational scaling question that appears only after finite dephasing and a required collection efficiency are specified:

> **At fixed internal signal-collection efficiency, how do the minimum gate duration and the accepted internal dark-count burden scale with the number of coherently participating dark-generating sites?**

For the symmetric Markov model studied below, the answer has a sharp boundary. Let `kappa` be the bright extraction rate and `gamma` the local pure-dephasing rate. Define

```math
\boxed{
\eta_c=\frac{\kappa}{\kappa+\gamma}.
}
```

For a fixed required conditional internal collection efficiency `eta`, the large-`N` detector has three asymptotic regimes:

```math
\boxed{
\begin{array}{c|c|c}
\text{required efficiency} & \text{minimum gate} & \text{accepted local-dark mean}\\
\hline
0<\eta<\eta_c & O(1) & O(1)\\
\eta=\eta_c & \Theta(\ln N) & \Theta((\ln N)^2)\\
\eta_c<\eta<1 & O(N) & O(N^2).
\end{array}}
```

The transition has a simple physical origin. Only fraction `eta_c` of an initially bright excitation can be collected on the fast timescale before local dephasing transfers amplitude into the large dark manifold. If the required efficiency is smaller than that fraction, the detector can close its gate before slow recycling matters. If the requested efficiency is larger, it must wait for dephased signal population to return to the bright sector on an `O(N)` timescale. During that long gate, an `O(N)` raw local dark-generation rate accumulates for `O(N)` time, producing an `O(N^2)` accepted dark burden in the independent-particle model.

The exactly coherence-preserving result—raw local dark generation proportional to `N` but accepted gated dark counts independent of `N`—is recovered as the special case `gamma=0`. It is useful as a limiting check, but it is not the central contribution of this manuscript.

The theory is intentionally restricted. The quantum dynamics derived below is a one-excitation kernel. Continuous dark generation is then introduced through an explicit **independent-particle stochastic lift**: generated excitations are distinguishable, noninteracting, and each follows an independent copy of the one-body dynamics. This makes the Poisson counting result exact within the lifted model without pretending that a strict one-excitation Hilbert space contains multiple simultaneous excitations. The signal efficiency used here is also conditional internal collection after a photon has already prepared the bright excitation; it is not total optical quantum efficiency.

---

# 2. Minimal coherence-selective detector model

## 2.1. Bright optical excitation and population-matched dark excitation

Let the local single-excitation basis be

```math
|j\rangle,
\qquad j=1,\ldots,N.
```

An optical mode couples with amplitudes `g_j` and prepares the normalized bright state

```math
\boxed{
|B\rangle
=\frac{1}{\sqrt{g^\dagger g}}
\sum_{j=1}^{N}g_j|j\rangle.
}
```

Writing

```math
w_j=\frac{|g_j|^2}{g^\dagger g},
```

the bright state has local populations `w_j`.

Construct an adversarial internal dark event with exactly the same local populations but no phase coherence:

```math
\boxed{
\rho_D=\sum_{j=1}^{N}w_j|j\rangle\langle j|.
}
```

Hence

```math
\langle j|\rho_D|j\rangle
=|\langle j|B\rangle|^2.
```

Every local-basis diagonal observable therefore gives identical single-event statistics for signal and dark excitation.

An ideal bright-selective counted operator

```math
\Pi_B=|B\rangle\langle B|
```

accepts the bright state with probability one but the incoherent population-matched state with probability

```math
\epsilon_D
=\operatorname{Tr}(\Pi_B\rho_D)
=\sum_jw_j^2
=\frac{1}{N_{eff}}.
```

For uniform participation, `w_j=1/N` and `epsilon_D=1/N`.

This is standard coherent-mode/state-verification geometry and will be used only as the starting point for the dynamical detector calculation.

## 2.2. General internal-dark covariance

If microscopic dark-generation channels inject excitation vectors `|l_alpha>`, define the positive matrix

```math
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|.
```

The total raw dark-generation strength is trace-like,

```math
\Gamma_{raw}\propto\operatorname{Tr}D,
```

whereas direct injection into the counted optical direction is the Rayleigh quotient

```math
\boxed{
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

Thus correlated dark generation aligned with `g` can eliminate the state-space rejection entirely. The symmetric scaling theorem below deliberately uses the opposite limit of independent equal local dark sources.

## 2.3. Symmetric one-body dynamics

For the main theorem use

```math
|B\rangle=\frac{1}{\sqrt N}\sum_j|j\rangle.
```

A counted sink extracts only the bright state at rate `kappa`. Independent local pure dephasing acts at rate `gamma`.

Within the surviving one-excitation manifold define

```math
P(t)=\operatorname{Tr}\rho(t),
```

and

```math
b(t)=\langle B|\rho(t)|B\rangle.
```

The permutation-symmetric dynamics closes exactly:

```math
\boxed{\dot P=-\kappa b,}
```

```math
\boxed{
\dot b=-(\kappa+\gamma)b+\frac{\gamma}{N}P.
}
```

Eliminating `b`,

```math
\boxed{
\ddot P+(\kappa+\gamma)\dot P+\frac{\kappa\gamma}{N}P=0.
}
```

Let

```math
a=\kappa+\gamma,
```

```math
\Delta_N=\sqrt{a^2-\frac{4\kappa\gamma}{N}},
```

and

```math
r_{\pm,N}=\frac{a\pm\Delta_N}{2}.
```

For an initial excitation with bright population `b_0`, `P(0)=1` and `\dot P(0)=-\kappa b_0`, giving

```math
\boxed{
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa b_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa b_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
}
```

The cumulative probability that this excitation has reached the counted sink by time `t` is

```math
\boxed{
C_{b_0,N}(t)=1-P_{b_0,N}(t).
}
```

A photon-created bright excitation has

```math
b_{0,S}=1,
```

while a uniformly local internal dark excitation has

```math
b_{0,D}=1/N.
```

Define

```math
C_{S,N}(t)=C_{1,N}(t),
```

```math
C_{D,N}(t)=C_{1/N,N}(t).
```

Their exact finite-time separation is

```math
\boxed{
C_{S,N}(t)-C_{D,N}(t)
=
\frac{\kappa(1-1/N)}{\Delta_N}
\left(e^{-r_{-,N}t}-e^{-r_{+,N}t}\right).
}
```

For `N>1` this is positive for every finite `t>0`. For every `gamma>0`, however,

```math
C_{S,N}(\infty)=C_{D,N}(\infty)=1.
```

Therefore the state-space discrimination is necessarily finite-time in this dephasing model.

---

# 3. From one-body dynamics to a counting detector

## 3.1. Independent-particle stochastic lift

The one-body Lindblad dynamics above does not itself describe arbitrary simultaneous multi-excitation occupancy. To define a continuous dark-count process without inconsistency, we introduce the following explicit lift.

Each local site generates distinguishable dark excitations according to an independent Poisson process of rate `d`. Generated excitations do not interact, saturate, or block one another. Each carries an independent copy of the one-body collection kernel `C_{D,N}`. The counted sink records each successful extraction independently.

The aggregate raw generation process is therefore Poisson with rate

```math
\boxed{\Gamma_{raw}=Nd.}
```

For a gate `[0,T]`, an excitation born at time `s` has age `T-s` at closure and is counted with probability `C_{D,N}(T-s)`. Independent Poisson marking then gives an exact Poisson accepted-count distribution within this lifted model with mean

```math
\boxed{
\mu_N(T)
=Nd\int_0^T C_{D,N}(u)\,du.
}
```

Hence

```math
P_{FA,N}(T)=1-e^{-\mu_N(T)}.
```

This lift should be viewed as the noninteracting/dilute reference model for the scaling theorem. Saturation, exclusion, many-body interactions, and detector reset are separate physical effects outside the present analysis.

## 3.2. Conditional internal signal collection

A photon that has already prepared the bright material excitation at gate opening is collected with conditional internal efficiency

```math
\boxed{
\eta_{int,N}(T)=C_{S,N}(T).
}
```

This quantity is not the probability that an incident photon is absorbed. If a separate optical preparation probability `eta_abs` factorizes from the internal dynamics, then an end-to-end efficiency would be `eta_abs eta_int,N`. We do not model that optical-coupling stage here.

## 3.3. Fixed-efficiency task

Fix

```math
0<\eta<1.
```

Define the minimal gate achieving the requested conditional internal collection:

```math
\boxed{
T_N(\eta)
=\inf\{t\ge0:C_{S,N}(t)\ge\eta\}.
}
```

The associated local-dark burden is

```math
\boxed{
\mu_N(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
}
```

The remainder of the paper studies the large-`N` scaling of this operating point at fixed `kappa`, `gamma`, `d`, and `eta`.

---

# 4. Efficiency-controlled scalability theorem

## 4.1. Fast and slow rate scales

Define

```math
\boxed{
q=\frac{\kappa}{\kappa+\gamma}=\frac{\kappa}{a},
}
```

and

```math
\boxed{
\lambda=\frac{\kappa\gamma}{\kappa+\gamma}=q(1-q)a.
}
```

For large `N`,

```math
r_{-,N}=\frac{\lambda}{N}+O(N^{-2}),
```

```math
r_{+,N}=a-\frac{\lambda}{N}+O(N^{-2}).
```

At fixed physical time,

```math
\boxed{
C_{S,N}(t)
\longrightarrow
q(1-e^{-at}).
}
```

Thus the fast branch can asymptotically collect at most fraction `q` of the initial bright excitation.

For one local dark event,

```math
\boxed{
NC_{D,N}(t)
\longrightarrow
q(1-q)at+q^2(1-e^{-at}).
}
```

The first term is dephasing-enabled return toward the counted sector; the second is the direct initial `1/N` bright overlap.

The threshold efficiency is therefore

```math
\boxed{
\eta_c=q=\frac{\kappa}{\kappa+\gamma}.
}
```

## 4.2. Subcritical target: 0 < eta < eta_c

For `eta<q`, the target lies below the fast-branch ceiling. Define

```math
\boxed{
x_\eta=-\ln\left(1-\frac{\eta}{q}\right).}
```

Then

```math
\boxed{
aT_N(\eta)\longrightarrow x_\eta,}
```

so the minimum gate stays finite as `N` grows.

The accepted local-dark mean converges to

```math
\boxed{
\mu_N(\eta)
\longrightarrow
\mu_{<}(\eta)
=\frac{d}{a}
\left[
\frac{q(1-q)}{2}x_\eta^2
+q^2x_\eta
-q\eta
\right].
}
```

Therefore

```math
\boxed{
0<\eta<\eta_c:
\qquad
T_N=O(1),
\qquad
\mu_N=O(1).
}
```

This is the scalable coherence-selective branch: the physical number of local dark sources grows, the raw generation rate is `Nd`, yet the accepted local-dark burden at the fixed-efficiency operating point remains bounded.

## 4.3. Supercritical target: eta_c < eta < 1

For `eta>q`, the fast branch cannot reach the requested collection efficiency. The detector must wait for population transferred into the dark manifold to leak back toward the bright sink.

Use the slow time

```math
t=Ny.
```

Then

```math
\boxed{
C_{S,N}(Ny)
\longrightarrow
1-(1-q)e^{-\lambda y},
}
```

and

```math
\boxed{
C_{D,N}(Ny)
\longrightarrow
1-e^{-\lambda y}.
}
```

The required gate satisfies

```math
\boxed{
\frac{T_N(\eta)}{N}
\longrightarrow
\frac1\lambda
\ln\left(\frac{1-q}{1-\eta}\right).
}
```

Thus `T_N=O(N)`.

The accepted local-dark burden obeys

```math
\boxed{
\frac{\mu_N(\eta)}{N^2}
\longrightarrow
\frac{d}{\lambda}
\left[
\ln\left(\frac{1-q}{1-\eta}\right)
-
\frac{\eta-q}{1-q}
\right].
}
```

Therefore

```math
\boxed{
\eta_c<\eta<1:
\qquad
T_N=O(N),
\qquad
\mu_N=O(N^2).
}
```

The quadratic dark burden is a compound consequence of an extensive raw generation rate operating for an extensive gate after slow manifold recycling becomes necessary.

## 4.4. Critical target: eta = eta_c

At `eta=q`, the detector lies in the boundary layer between the fast and slow clocks. The leading signal survival probability can be written

```math
P_{S,N}(t)
\simeq
(1-q)e^{-\lambda t/N}+qe^{-at}.
```

The condition `C_S=q`, or `P_S=1-q`, gives for `t=o(N)`

```math
e^{-at}
\simeq
\frac{(1-q)^2at}{N}.
```

With `x=at`,

```math
xe^x\simeq\frac{N}{(1-q)^2},
```

so

```math
\boxed{
aT_N(q)
\sim
W\left(\frac{N}{(1-q)^2}\right),}
```

where `W` is the Lambert-W function.

Consequently,

```math
\boxed{T_N(q)=\Theta(\ln N).}
```

Using the corresponding intermediate-scale dark kernel gives

```math
\boxed{\mu_N(q)=\Theta((\ln N)^2).}
```

More explicitly, with

```math
x_N=W\left(\frac{N}{(1-q)^2}\right),
```

the leading integrated dark burden is

```math
\mu_N(q)
\sim
\frac{d}{a}
\left[
\frac{q(1-q)}{2}x_N^2
+q^2x_N
-q^2
\right]
```

up to lower-order corrections.

## 4.5. Theorem statement

For fixed positive `kappa`, `gamma`, and `d`, with the independent-particle stochastic lift above and a fixed required conditional internal efficiency `0<eta<1`, let

```math
\eta_c=\frac{\kappa}{\kappa+\gamma}.
```

Then the minimum-gate detector task has the large-`N` partition

```math
\boxed{
\begin{array}{c|c|c}
\text{efficiency regime} & T_N(\eta) & \mu_N(\eta)\\
\hline
0<\eta<\eta_c & O(1) & O(1)\\
\eta=\eta_c & \Theta(\ln N) & \Theta((\ln N)^2)\\
\eta_c<\eta<1 & O(N) & O(N^2).
\end{array}}
```

The scalability condition can equivalently be written

```math
\boxed{
\eta<\frac{\kappa}{\kappa+\gamma}
}
```

or, for `gamma>0`,

```math
\boxed{
\frac{\kappa}{\gamma}>
\frac{\eta}{1-\eta}.
}
```

Thus a 99% conditional internal collection target requires `kappa/gamma>99` to lie strictly on the bounded large-`N` branch.

---

# 5. Coherence-preserving limit as a corollary

For `gamma=0`,

```math
\eta_c=1.
```

Every fixed target `0<eta<1` is therefore subcritical.

The exact kernels reduce to

```math
C_{S,N}(t)=1-e^{-\kappa t},
```

```math
C_{D,N}(t)=\frac1N(1-e^{-\kappa t}).
```

The minimal gate is

```math
T_N(\eta)
=\frac{-\ln(1-\eta)}{\kappa},
```

and the accepted local-dark mean is exactly

```math
\boxed{
\mu_N(\eta)
=\frac{d}{\kappa}
\left[-\ln(1-\eta)-\eta\right],
\qquad\gamma=0,
}
```

independent of `N`.

Equivalently, at fixed gate `T`,

```math
\mu_N(T)
=d\left[T-\frac{1-e^{-\kappa T}}{\kappa}\right].
```

This exact cancellation is a useful consistency check and an intuitive entry point, but the finite-dephasing scaling boundary is the principal result.

---

# 6. Secondary thermodynamic constraint on the counted extractor

The local-dark theorem concerns internally generated incoherent excitations. The counted extraction mechanism can itself produce dark events if its microscopic transition is thermally reversible.

For stationary extraction channels `a` obeying local detailed balance,

```math
\frac{\bar\kappa_a}{\kappa_a}
=e^{-\beta\Delta F_a},
\qquad
\beta=(kT)^{-1},
```

define

```math
K_\to=\sum_a\kappa_a,
```

```math
K_\leftarrow=\sum_a\bar\kappa_a,
```

and `p_a=\kappa_a/K_\to`. Then

```math
\boxed{
\frac{K_\leftarrow}{K_\to}
=\sum_ap_ae^{-\beta\Delta F_a}
=e^{-\beta\Delta F_{eff}},
}
```

with

```math
\boxed{
\Delta F_{eff}
=-kT\ln\left(\sum_ap_ae^{-\beta\Delta F_a}\right).
}
```

If useful forward extraction is collectively enhanced by a factor `mathcal C(N)`,

```math
K_\to(N)=\mathcal C(N)K_\to(1),
```

then holding the reverse coefficient fixed requires

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge kT\ln\mathcal C(N).
}
```

This logarithmic relation is a direct consequence of local detailed balance and is not claimed as a new thermodynamic law. Its role here is narrower: it prevents the coherence-selected local-dark result from being misread as a free collective scaling advantage when the counted conversion channel itself is thermally reversible.

Mapping reverse injections onto counts requires an independent-event model analogous to the local-dark stochastic lift. We therefore treat this result as a secondary resource constraint rather than part of the principal efficiency-transition theorem.

---

# 7. Discussion

## 7.1. Why the main result is not the static `1/N` projection

For independent equal local dark sources, projecting onto one normalized coherent mode gives an accepted direct dark strength independent of `N`. That is standard mode-filtering geometry.

The new detector result is the response of that geometry to a finite coherence lifetime **at fixed requested signal collection**. Dephasing does not merely weaken the rejection continuously. It creates two dynamical clocks whose relative use is selected by the operating point. The gate and dark burden therefore change asymptotic scaling class when `eta` crosses `eta_c`.

This is why the meaningful dimensionless detector criterion is not simply `kappa/gamma >> 1`. It is

```math
\eta<\frac{\kappa}{\kappa+\gamma}.
```

The same physical detector may be scalable at one required efficiency and catastrophically non-scalable at a slightly higher one.

## 7.2. Relation to established quantum-coherent detector theory

Fully quantum photodetector models already show that coherence and amplification backaction can control efficiency, dark counts, and jitter [1]. Collective bright/dark-state physics and dephasing-driven intermode transfer are established in superradiance and cavity-QED models [2,3]. Coherence and dark states have also been used to improve photocell extraction or suppress unwanted radiative pathways [4,5].

A particularly close device precedent is the collective quantum infrared detector of Pisani et al. [6], where collective electronic polarization and light-matter-coupled states feed a single-particle electronic extractor and photocurrent. The present model does not claim collective coherence-dependent extraction as a new device concept.

The narrower object studied here is the scaling of **internally generated local dark events** at a fixed required conditional collection efficiency, including the boundary between a bounded fast-gate branch and a slow-recycling branch with quadratic accepted dark burden.

Recent 2026 work also develops nontrivial finite-size and decoherence scaling regimes in Dicke superradiance and superabsorption [7,8]. Those results make broad claims of a new “decoherence scaling transition” inappropriate here. The current candidate contribution is specifically the detector-efficiency boundary and its dark-count scaling laws.

## 7.3. Physical-space versus state-space suppression

Resonant and antenna-coupled infrared detectors can maintain a large optical collection cross section while reducing electrically active semiconductor area, thereby suppressing dark current [9]. That is an established and powerful physical-space strategy.

The present Gedanken model deliberately retains all `N` local dark-generation sites. Its raw generation rate remains `Nd`; the filtering occurs because local events populate the wrong collective state-space direction.

Thus the mechanisms are distinct:

```text
physical-space strategy:
    remove or electrically isolate dark-generating volume;

state-space strategy:
    retain the dark-generating volume,
    but select one coherent excitation direction.
```

This distinction does not establish practical superiority of the state-space strategy. A microscopic realization would need to show that the required coherent manifold and selective extraction can be implemented without introducing larger competing noise channels.

## 7.4. Dark events this mechanism cannot reject

A thermal or background photon entering through the same accepted optical mode prepares the same bright excitation as the signal photon. The present state-space discriminator therefore cannot reject same-mode photon background.

Likewise, correlated internal dark processes with covariance concentrated along `g` can inject directly into the bright state and remove the `1/N` local-dark advantage.

The theorem concerns independent or sufficiently misaligned **internal** dark-generation processes, not all detector noise.

## 7.5. Scope of the stochastic lift

The independent-particle lift is mathematically useful because it converts an exact one-event quantum kernel into an exact count process without conflating one-excitation dynamics with many simultaneous excitations. It is nevertheless a model assumption.

Real detectors may have:

- Pauli blocking or saturation;
- exciton-exciton or carrier-carrier interactions;
- shared traps or correlated generation;
- state-dependent reset and dead time;
- nonlinear extraction;
- heating and signal-dependent dephasing.

Such effects can change the `N` scaling. The current theorem supplies a controlled noninteracting reference problem rather than a universal many-body detector law.

## 7.6. Energetic disorder and nonuniform couplings

The exact efficiency-transition theorem uses an exactly degenerate, uniformly coupled manifold. The general covariance expression

```math
\Gamma_D^B=\frac{g^\dagger Dg}{g^\dagger g}
```

shows how nonuniform optical participation and correlated dark generation modify the static selection. Energetic disorder additionally causes coherent phase evolution that can act like dephasing relative to the selected bright vector.

A full disorder theory is outside Rev. 1. It is a natural robustness question only if the symmetric theorem survives external novelty review.

---

# 8. Conclusion

A coherence-selective photodetector can have qualitatively different dark-count scalability depending on the required internal signal collection efficiency. In a symmetric `N`-state model, bright extraction at rate `kappa` competes with local dephasing at rate `gamma`, producing the critical efficiency

```math
\eta_c=\frac{\kappa}{\kappa+\gamma}.
```

With `N` independent local dark-generation sites and an explicit independent-particle count model, a target below `eta_c` is reached in an `O(1)` gate with `O(1)` accepted local-dark mean despite `O(N)` raw generation. At `eta_c`, the gate and dark burden grow logarithmically and quadratically-logarithmically, respectively. Above `eta_c`, recovering dephased signal population requires an `O(N)` gate and produces an `O(N^2)` accepted local-dark burden. The exact no-dephasing cancellation is the limiting case `eta_c=1`. The result shows that the scalability of state-space dark rejection is controlled not only by coherence lifetime or extraction rate separately, but by the requested detector operating point relative to their branching ratio.

---

# References — Rev. 1 working set

[1] S. M. Young, M. Sarovar, and F. Léonard, “Fundamental limits to single-photon detection determined by quantum coherence and backaction,” *Phys. Rev. A* **97**, 033836 (2018). DOI: `10.1103/PhysRevA.97.033836`.

[2] N. Shammah, N. Lambert, F. Nori, and S. De Liberato, “Superradiance with local phase-breaking effects,” *Phys. Rev. A* **96**, 023863 (2017). DOI: `10.1103/PhysRevA.96.023863`.

[3] E. Davidsson and M. Kowalewski, “The role of dephasing for dark state coupling in a molecular Tavis-Cummings model,” arXiv:`2304.09583` (2023).

[4] C. Creatore, M. A. Parker, S. Emmott, and A. W. Chin, “Efficient biologically inspired photocell enhanced by delocalized quantum states,” *Phys. Rev. Lett.* **111**, 253601 (2013). DOI: `10.1103/PhysRevLett.111.253601`.

[5] A. Fruchtman, R. Gómez-Bombarelli, B. W. Lovett, and E. M. Gauger, “Photocell optimization using dark state protection,” *Phys. Rev. Lett.* **117**, 203603 (2016). DOI: `10.1103/PhysRevLett.117.203603`.

[6] F. Pisani et al., “Electronic transport driven by collective light-matter coupled states in a quantum device,” *Nature Communications* **14**, 3914 (2023). DOI: `10.1038/s41467-023-39594-z`.

[7] J. D. Álvarez-Cuartas and J. H. Reina, “Entanglement and dynamical scaling laws in quantum superabsorption,” *Phys. Rev. Research* **8**, 033035 (2026). DOI: `10.1103/jtgg-tbnw`.

[8] N. S. Bassler, J. Lyne, and J. Cuerda, “Scaling theory of decoherence in Dicke superradiance,” arXiv:`2607.28034` (2026).

[9] “Synchronously wired infrared antennas for resonant single-quantum-well photodetection up to room temperature,” *Nature Communications* (2020), article `s41467-020-14426-6`. Final author/volume/page metadata to be verified in the citation-production pass.

---

# Rev. 1 review gate

Before journal formatting or figure polishing:

1. independently recheck the three asymptotic regimes from the exact finite-`N` kernels;
2. run a focused current-literature audit specifically for an existing fixed-efficiency threshold equivalent to `eta_c=kappa/(kappa+gamma)` and the associated `O(N^2)` dark-count law;
3. test robustness to modest nonuniformity only if it changes the novelty/significance judgment;
4. keep the thermodynamic affinity result secondary unless a stronger detector-specific consequence emerges;
5. if a direct stronger prior theorem is found, close or narrow the paper rather than changing vocabulary.
