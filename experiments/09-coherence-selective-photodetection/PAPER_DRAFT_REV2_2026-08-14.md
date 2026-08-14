# Rate-scaling phase diagram for internal dark counts in a coherence-selective photodetector

**Draft status:** Rev. 2 / rebuilt after second hostile referee review  
**Date:** 2026-08-14  
**Scope:** analytical/theoretical  
**Novelty status:** not established; no priority language authorized

## Abstract

We analyze a coherence-selective photodetector in which an absorbed photon prepares one collective bright excitation across `N` local states while independent internal dark-generation events populate those states incoherently. The static mode-selection geometry is established; our question is instead how the detector scales when useful bright extraction and local dephasing themselves vary with system size. We take

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
```

and choose the minimum gate required to reach a fixed conditional internal collection efficiency `eta`. With `N` independent local dark-generation sites of fixed per-site rate, the accepted internal-dark mean has three rate sectors. If `alpha>beta`, every fixed `eta<1` eventually uses the fast branch and both gate and dark burden scale as `N^{-alpha}`. If `alpha<beta`, every fixed positive `eta` requires slow recycling, giving `T_N~N^{1-alpha}` and `mu_N~N^{2-alpha}`. On the balanced line `alpha=beta=s`, a critical efficiency `eta_c=kappa_0/(kappa_0+gamma_0)` separates `N^{-s}` scaling from `N^{1-s}`/`N^{2-s}` scaling, with a logarithmic boundary. The fixed-rate result is the slice `alpha=beta=0`. The theory isolates a detector-operational scaling law without claiming novelty for coherent collective detector architectures or decoherence scaling in general.

---

# 1. Introduction

Quantum-coherent detector models have established that field-matter coherence and amplification backaction can control photodetector efficiency, dark counts, jitter, and optimal design [1]. Coherently interacting subwavelength detector elements have also been proposed explicitly as a route to simultaneous high efficiency, low dark counts, high count rate, and photon-number resolution [2]. Collective bright and dark states, dephasing-induced transfer between them, and dark-state protection are mature topics in quantum optics and photocell theory [3-5]. More recently, collective electronic polarization has been connected directly to an electronic extractor and photocurrent in a quantum infrared detector [6].

The present work therefore does **not** claim that coherent collective photodetection, bright/dark detector manifolds, or coherence-assisted low-dark operation are new concepts.

A second established neighboring literature concerns large-system collective scaling. In Dicke superradiance and superabsorption, competition between collective rates and local decoherence produces distinct large-`N` dynamical regimes and transient scaling boundaries [7,8]. The present work does not claim the broad discovery of a new decoherence-induced scaling transition.

We ask a narrower detector-operational question. Suppose a photon has prepared one coherent bright material excitation across `N` local states, whereas internally generated dark events arise independently and locally. Suppose further that the detector counts only through the bright sector. For a prescribed **conditional internal collection efficiency**, how long must the detector remain open, and how many internally generated local events are accepted during that gate?

That question becomes nontrivial because the detector size can change not only the number of dark-generation sites but also the useful extraction and dephasing rates. We therefore write

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
```

where `kappa_N` is the bright extraction rate and `gamma_N` the local pure-dephasing rate. The local dark-generation rate per microscopic site is held fixed at `d`, so the raw internal generation rate remains extensive, `Nd`.

The central result is a phase diagram for the minimum gate `T_N(eta)` and accepted local-dark mean `mu_N(eta)` at fixed required internal collection efficiency `eta`:

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \mu_N\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<\eta_c & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=\eta_c & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>\eta_c & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha},
\end{array}}
```

where

```math
\boxed{
\eta_c=\frac{\kappa_0}{\kappa_0+\gamma_0}
}
```

on the balanced line.

This result separates two questions that are easy to conflate. The sign of `alpha-beta` determines which dynamical branch is required to reach a fixed efficiency; the absolute extraction exponent `alpha` determines whether the resulting gate and accepted dark burden increase or decrease with detector size.

The calculation uses an exact one-excitation open-system kernel and an explicit independent-particle stochastic lift for continuous local dark generation. It does not model end-to-end photon absorption, same-mode optical background, saturation, many-body interactions, or a material-specific realization.

---

# 2. Coherent signal state and local internal dark events

## 2.1. Bright state

Let the local single-excitation basis be

```math
|j\rangle,
\qquad j=1,\ldots,N.
```

An optical mode with coupling amplitudes `g_j` prepares

```math
|B\rangle
=\frac{1}{\sqrt{g^\dagger g}}
\sum_jg_j|j\rangle.
```

For the symmetric theorem,

```math
\boxed{
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle.
}
```

A local dark event is created at one site with no phase relation to events at other sites. Averaged over uniformly likely sites its density operator is

```math
\rho_D=\frac1N\sum_j|j\rangle\langle j|.
```

The bright projector accepts the signal state with probability one and the uniformly local dark event with probability `1/N`.

This static result is standard normalized coherent-mode filtering/state-verification geometry. It is included only to define the detector's selected state-space direction.

## 2.2. General dark-generation orientation

For microscopic dark-generation vectors `|l_a>`, define

```math
D=\sum_a|l_a\rangle\langle l_a|.
```

The raw generation strength is trace-like, while direct injection into the counted bright direction is

```math
\boxed{
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

Correlated dark processes aligned with `g` can therefore remove the state-space advantage entirely. The scaling theorem below deliberately treats independent equal local generation.

---

# 3. Exact one-body extraction/dephasing dynamics

The counted sink acts on the bright state at rate `kappa_N`. Independent local pure dephasing acts at rate `gamma_N`.

Within the surviving single-excitation manifold define

```math
P(t)=\operatorname{Tr}\rho(t),
```

and

```math
b(t)=\langle B|\rho(t)|B\rangle.
```

Permutation symmetry gives exactly

```math
\boxed{\dot P=-\kappa_N b,}
```

```math
\boxed{
\dot b
=-(\kappa_N+\gamma_N)b
+\frac{\gamma_N}{N}P.
}
```

Hence

```math
\boxed{
\ddot P
+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
}
```

Define

```math
a_N=\kappa_N+\gamma_N,
```

```math
\Delta_N
=\sqrt{a_N^2-\frac{4\kappa_N\gamma_N}{N}},
```

```math
r_{\pm,N}=\frac{a_N\pm\Delta_N}{2}.
```

For initial bright population `b_0`,

```math
\boxed{
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa_Nb_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa_Nb_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
}
```

The collection probability is

```math
C_{b_0,N}(t)=1-P_{b_0,N}(t).
```

For the photon-created bright excitation use `b_0=1`; for a uniformly local dark event use `b_0=1/N`:

```math
C_{S,N}=C_{1,N},
\qquad
C_{D,N}=C_{1/N,N}.
```

For every nonzero dephasing rate, both eventually reach the counted sink:

```math
C_{S,N}(\infty)=C_{D,N}(\infty)=1.
```

Thus state-space rejection is finite-time, not permanent.

The slow rate is

```math
\boxed{
r_{-,N}
=\frac{\lambda_N}{N}[1+O(N^{-1})],
}
```

where

```math
\lambda_N
=\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}.
```

---

# 4. Counting model and detector task

## 4.1. Independent-particle stochastic lift

The one-body master equation supplies a collection kernel for one generated excitation. Continuous local dark generation is introduced separately.

Each of the `N` sites generates distinguishable, noninteracting dark excitations as an independent Poisson process of rate `d`. Each generated excitation follows an independent copy of the one-body dynamics. This is an extensive low-density reference model: it neglects saturation, Pauli blocking, heating, particle-particle interactions, and shared reset dynamics.

The aggregate raw local generation rate is

```math
\Gamma_{raw}=Nd.
```

For a gate `[0,T]`, Poisson marking gives an accepted local-dark count mean

```math
\boxed{
\mu_N(T)
=Nd\int_0^T C_{D,N}(u)du.
}
```

## 4.2. Conditional internal collection efficiency

A photon that has already prepared the material bright state at gate opening is collected with

```math
\eta_{int,N}(T)=C_{S,N}(T).
```

This is not end-to-end photon quantum efficiency. Optical coupling and absorption occur upstream of the present reduced model.

Fix a required internal collection target

```math
0<\eta<1.
```

Define the minimum gate

```math
\boxed{
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\},
}
```

and the associated accepted local-dark burden

```math
\boxed{
\mu_N(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
}
```

These two quantities are the observables whose asymptotic scaling we classify.

---

# 5. Size-dependent extraction and dephasing

Let

```math
\boxed{
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
}
```

Define the fast extraction branching fraction

```math
q_N
=\frac{\kappa_N}{\kappa_N+\gamma_N}.
```

Then

```math
\boxed{
q_N\to
\begin{cases}
1, & \alpha>\beta,\\
q_0=\kappa_0/(\kappa_0+\gamma_0), & \alpha=\beta,\\
0, & \alpha<\beta.
\end{cases}}
```

The phase diagram follows from these three limits.

---

# 6. Extraction-dominated sector: alpha > beta

Here `q_N->1`. Every fixed target `eta<1` is eventually attainable on the fast branch before dark-manifold recycling is required.

Let

```math
x_\eta=-\ln(1-\eta).
```

Since `a_N~kappa_0N^alpha`,

```math
\boxed{
T_N(\eta)
\sim
\frac{x_\eta}{\kappa_0}N^{-\alpha}.
}
```

The local-dark burden is

```math
\boxed{
\mu_N(\eta)
\sim
\frac{d}{\kappa_0}
[x_\eta-\eta]
N^{-\alpha}.
}
```

Thus

```math
\boxed{
\alpha>\beta:
\quad
T_N\asymp N^{-\alpha},
\quad
\mu_N\asymp N^{-\alpha}.
}
```

The sign of `alpha` remains important. If `alpha>0`, both quantities decrease with size; if `alpha=0`, they remain finite; if `alpha<0`, they increase despite extraction still dominating dephasing in relative terms.

---

# 7. Dephasing-dominated sector: alpha < beta

Now `q_N->0`. Every fixed positive target eventually exceeds the fast-branch ceiling, so the detector must wait for slow recycling.

Again let

```math
x_\eta=-\ln(1-\eta).
```

Because

```math
\lambda_N\sim\kappa_0N^\alpha,
```

the relevant slow variable is `z=lambda_N t/N`. The asymptotic signal and local-dark kernels both become `1-e^{-z}` on that timescale. Therefore

```math
\boxed{
T_N(\eta)
\sim
\frac{x_\eta}{\kappa_0}N^{1-\alpha},
}
```

and

```math
\boxed{
\mu_N(\eta)
\sim
\frac{d}{\kappa_0}
[x_\eta-\eta]
N^{2-\alpha}.
}
```

Hence

```math
\boxed{
\alpha<\beta:
\quad
T_N\asymp N^{1-\alpha},
\quad
\mu_N\asymp N^{2-\alpha}.
}
```

The accepted local-dark burden is bounded only if the absolute extraction exponent reaches `alpha>=2`, even though dephasing remains parametrically faster.

---

# 8. Balanced sector: alpha = beta = s

If extraction and dephasing scale with the same power, their ratio remains finite. Define

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0},
```

```math
A=\kappa_0+\gamma_0,
```

```math
\lambda_0=\frac{\kappa_0\gamma_0}{A}.
```

This line retains an efficiency-controlled transition.

## 8.1. eta < q0

Let

```math
x_\eta=-\ln(1-\eta/q_0).
```

Then

```math
\boxed{
T_N\sim\frac{x_\eta}{A}N^{-s},
}
```

and

```math
\boxed{
\mu_N
\sim
\frac{d}{A}
\left[
\frac{q_0(1-q_0)}2x_\eta^2
+q_0^2x_\eta-q_0\eta
\right]N^{-s}.
}
```

## 8.2. eta = q0

At the boundary, the vanishing fast exponential and incipient slow recycling balance. At leading logarithmic order,

```math
A N^s T_N(q_0)
\sim
W\left(\frac{N}{(1-q_0)^2}\right).
```

The robust scaling statements are

```math
\boxed{
T_N(q_0)=\Theta(N^{-s}\ln N),
}
```

```math
\boxed{
\mu_N(q_0)=\Theta[N^{-s}(\ln N)^2].
}
```

Because finite-`N` convergence of the Lambert-W prefactor is slow, we use only the scaling-level claim in the main theorem.

## 8.3. eta > q0

Define

```math
L_\eta=\ln\frac{1-q_0}{1-\eta},
```

```math
H_\eta
=L_\eta-\frac{\eta-q_0}{1-q_0}.
```

Then

```math
\boxed{
T_N
\sim
\frac{L_\eta}{\lambda_0}N^{1-s},
}
```

and

```math
\boxed{
\mu_N
\sim
\frac{dH_\eta}{\lambda_0}N^{2-s}.
}
```

The Rev. 1 fixed-rate theorem is the special case `s=0`.

---

# 9. Phase diagram and bounded-dark boundaries

Collecting the results,

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \mu_N\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}.
\end{array}}
```

A bounded accepted local-dark burden requires

```text
alpha>beta:                   alpha >= 0
alpha=beta=s and eta<q0:      s >= 0
alpha=beta=s and eta=q0:      s > 0
alpha=beta=s and eta>q0:      s >= 2
alpha<beta:                   alpha >= 2
```

The same relative branch can therefore contain improving, constant, or worsening detector performance depending on the absolute useful-rate exponent.

---

# 10. Relation to established collective detector and scaling theory

Young, Sarovar, and Leonard have already proposed detectors made from subwavelength elements interacting collectively with the photon field, explicitly targeting high efficiency, low dark counts, low jitter, and high count rate [2]. Their broader quantum-photodetector framework also treats absorption and transduction coherently [1]. The present paper therefore does not claim coherent collective detector architecture as new.

Likewise, Bassler, Lyne, and Cuerda develop a large-`N` scaling theory of Dicke superradiance with local dephasing and obtain distinct collective/decoherence regimes [7]. This makes a broad claim of a new collective/decoherence phase diagram inappropriate here.

The narrower detector result is the mapping from those dynamical rate sectors to a **minimum gate selected by a prescribed collection efficiency** and then to the accepted burden from a physically extensive internal local-generation process.

The distinction is operational rather than terminological: the observable is not peak collective emission or a coherence order parameter but the number of internally generated events accepted while waiting long enough to collect a specified fraction of a signal excitation.

---

# 11. Physical interpretation

The phase diagram contains two levels of competition.

First, `alpha-beta` determines the fate of the fast branching fraction:

```text
extraction outruns dephasing -> q_N -> 1;
balanced scaling          -> q_N -> q0;
dephasing outruns extraction -> q_N -> 0.
```

Second, the absolute rate scale determines the clock. Even a detector on the fast branch can perform worse with size if `kappa_N` itself decreases. Conversely, even a slow-recycling branch can have bounded dark burden in the mathematical model if `kappa_N` grows as `N^2` or faster.

Three illustrative cases are useful:

```text
kappa_N ~ N, gamma_N ~ 1:
    T_N ~ N^-1, mu_N ~ N^-1;

kappa_N ~ N, gamma_N ~ N:
    below q0: mu_N ~ N^-1;
    at q0:    mu_N ~ (ln N)^2/N;
    above q0: mu_N ~ N;

kappa_N ~ 1, gamma_N increasing:
    T_N ~ N, mu_N ~ N^2.
```

The fixed-rate Rev. 1 quadratic law is therefore one slice, not a universal prediction.

---

# 12. Limitations

The theorem assumes:

- an exactly symmetric bright manifold;
- Markovian local pure dephasing;
- one bright-selective counted sink;
- polynomial size dependence of extraction and dephasing;
- fixed per-site local dark-generation rate;
- an independent-particle Poisson lift with no saturation or interactions;
- a fixed efficiency target independent of `N`.

It does not determine which exponents are physically realizable in a semiconductor or quantum detector. It also does not account for energetic disorder, correlated dark baths, same-mode background photons, many-excitation collective effects, detector reset, heating, or the thermodynamic work needed to realize a strongly increasing extraction rate.

Same-mode background photons are a particularly important boundary: they prepare the same bright state as the signal and are not rejected by this mechanism.

A separate local-detailed-balance calculation shows that increasing a thermally reversible extraction rate generally increases its reverse coefficient unless additional free-energy bias is supplied. Because quantum-detector thermodynamic tradeoffs are already an active established subject [9], we treat this only as a secondary resource caveat rather than a principal result.

---

# 13. Conclusion

A coherence-selective photodetector with extensive internal local generation does not have one universal large-size dark-count law. The scaling is jointly controlled by the required internal collection efficiency and by how useful extraction and local dephasing scale with the number of coherently participating states. When extraction outruns dephasing, every fixed efficiency below unity eventually lies on a fast branch and the accepted local-dark burden scales with the inverse useful-rate scale. When dephasing outruns extraction, every fixed positive efficiency requires slow dark-manifold recycling and the burden acquires an additional factor `N^2` relative to the useful-rate scale. When the two rates scale together, a finite critical efficiency separates the branches and produces a logarithmic boundary. The fixed-rate efficiency transition is the `alpha=beta=0` slice of this broader classification. The result is a detector-operational phase diagram for internally generated events, not a claim of a new general theory of coherent collective dynamics.

---

# Working references for Rev. 2

[1] S. M. Young, M. Sarovar, and F. Leonard, “Fundamental limits to single-photon detection determined by quantum coherence and backaction,” *Phys. Rev. A* **97**, 033836 (2018). DOI `10.1103/PhysRevA.97.033836`.

[2] S. M. Young, M. Sarovar, and F. Leonard, “Design of High-Performance Photon-Number-Resolving Photodetectors Based on Coherently Interacting Nanoscale Elements,” *ACS Photonics* **7**, 821–830 (2020). DOI `10.1021/acsphotonics.9b01754`.

[3] N. Shammah, N. Lambert, F. Nori, and S. De Liberato, “Superradiance with local phase-breaking effects,” *Phys. Rev. A* **96**, 023863 (2017). DOI `10.1103/PhysRevA.96.023863`.

[4] C. Creatore, M. A. Parker, S. Emmott, and A. W. Chin, “Efficient biologically inspired photocell enhanced by delocalized quantum states,” *Phys. Rev. Lett.* **111**, 253601 (2013). DOI `10.1103/PhysRevLett.111.253601`.

[5] A. Fruchtman, R. Gomez-Bombarelli, B. W. Lovett, and E. M. Gauger, “Photocell optimization using dark state protection,” *Phys. Rev. Lett.* **117**, 203603 (2016). DOI `10.1103/PhysRevLett.117.203603`.

[6] F. Pisani et al., “Electronic transport driven by collective light-matter coupled states in a quantum device,” *Nature Communications* **14**, 3914 (2023). DOI `10.1038/s41467-023-39594-z`.

[7] N. S. Bassler, J. Lyne, and J. Cuerda, “Scaling theory of decoherence in Dicke superradiance,” arXiv:`2607.28034` (2026).

[8] J. D. Alvarez-Cuartas and J. H. Reina, “Entanglement and dynamical scaling laws in quantum superabsorption,” *Phys. Rev. Research* **8**, 033035 (2026). DOI `10.1103/jtgg-tbnw`.

[9] E. Schwarzhans et al., “Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition,” *PRX Quantum* **7**, 033001 (2026). DOI `10.1103/wm5p-tjtg`.

---

# Rev. 2 review gate

Before journal formatting:

1. run an extreme hostile review focused on whether the new phase diagram is more than a change of observables applied to known Dicke scaling;
2. verify the asymptotic coefficients numerically in all three rate sectors;
3. determine whether a concise fixed-dark-budget corollary adds genuine detector interpretation;
4. decide whether a full article or shorter theoretical note is the more defensible format;
5. do not use novelty or priority language unless a deeper citation-network audit materially strengthens the evidence.
