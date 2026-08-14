# Scalable internal-dark-count limits in a coherence-selective photodetector

**Draft status:** Rev. 3 / concise theory-paper architecture after three hostile review rounds  
**Date:** 2026-08-14  
**Novelty status:** not established; no priority language authorized

## Abstract

Coherently interacting detector elements and bright/dark internal manifolds are established routes to high-performance quantum photodetection. We ask a narrower question: when local processes couple an internal dark manifold back to the counted bright sector, what fixed signal-collection efficiency can remain scalable as the number of dark-generating microscopic sites increases? A photon is assumed to prepare one collective bright excitation across `N` local states, while independent internal dark events are generated locally at fixed rate per site. Bright extraction and local dephasing scale as `kappa_N=kappa_0N^alpha` and `gamma_N=gamma_0N^beta`. For a gate chosen to reach a prescribed conditional internal collection efficiency, we derive the accepted local-dark burden. With bounded counted coupling per microscopic state, so that `alpha<=1`, the supremum fixed efficiency compatible with bounded accepted local-dark counts is

```math
\eta_{sc}=
\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

Any strict slow-recycling operating point incurs at least an `O(N)` local-dark burden. The full asymptotic laws show how gate duration and accepted dark counts approach this ceiling, while a thermally reversed extractor supplies an `O(1)`, `O(ln N)`, or `O(N)` gated floor on the fast, boundary, and slow branches. The result quantifies the detector penalty for violating dark-to-bright isolation in a coherence-selective architecture; it does not claim novelty for collective photodetection or decoherence scaling in general.

---

# 1. Introduction

Fully quantum photodetector models have established that coherence and amplification backaction can determine efficiency, dark counts, jitter, and optimal detector design [1]. Young, Sarovar, and Leonard subsequently proposed photon-number-resolving detectors made from subwavelength elements interacting collectively with the photon field, targeting simultaneous high efficiency, low dark counts, low jitter, and high count rate [2]. Their ideal-efficiency conditions explicitly require relaxation not to couple dark states back into the optically active manifold.

That condition motivates the present Gedanken experiment. Rather than proposing a new collective detector architecture, we ask what happens when the dark-to-bright isolation condition is deliberately violated by local dephasing while the number of internally dark-generating microscopic sites is increased.

The neighboring physics is mature. Collective bright/dark states and local-dephasing transfer are established [3]; dark-state and coherence-assisted photocells are established [4,5]; collective electronic polarization has been connected to extractor current in a quantum infrared detector [6]. Large-`N` scaling regimes controlled by collective dynamics and local decoherence are also an active subject, including a recent analytical scaling theory of Dicke superradiance [7]. We therefore do not claim novelty for coherent collective detectors, dark-state physics, or collective/decoherence scaling as broad concepts.

Our narrower observable is detector operational. For each system size `N`, we choose the **minimum gate needed to reach a prescribed conditional internal signal-collection efficiency** and calculate the accepted burden from an extensive set of independent internal local dark-generation processes. This converts bright/dark dynamics into a detector scalability question.

Let the useful bright extraction and local dephasing rates scale as

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
```

The accepted local-dark burden has distinct fast and slow-recycling branches. Under a bounded microscopic counted-coupling resource, the largest possible collective extraction-rate exponent is `alpha=1`. This removes the formal superlinear-rate escape and gives a compact detector limit:

```math
\boxed{
\eta_{sc}
=
\begin{cases}
1,&\alpha>\beta,\\[3pt]
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\[8pt]
0,&\alpha<\beta.
\end{cases}}
```

Here `eta_sc` is the supremum fixed conditional internal collection efficiency for which accepted **local internal** dark counts remain bounded as `N` grows.

The result concerns internal generation, not same-mode optical background. A background photon entering the accepted optical mode prepares the same bright state as the signal and is not rejected by this mechanism.

---

# 2. Minimal coherence-selective detector

## 2.1. Signal and local dark excitation

Let

```math
|j\rangle,
\qquad j=1,\ldots,N
```

be orthonormal local single-excitation states. For the symmetric model the photon-created state is

```math
\boxed{
|B\rangle=\frac1{\sqrt N}\sum_{j=1}^{N}|j\rangle.
}
```

An internally generated event is local, `|j><j|`, with sites equally likely. Its ensemble state is

```math
\rho_D=\frac1N\sum_j|j\rangle\langle j|.
```

The bright projector accepts the photon state with probability one and the uniformly local dark event with probability `1/N`.

This static `1/N` result is standard coherent-mode/state-verification geometry and is not our principal claim.

For general internal-generation covariance `D` and optical coupling vector `g`, direct injection into the counted bright direction is

```math
\Gamma_D^B=\frac{g^\dagger Dg}{g^\dagger g}.
```

Hence a correlated internal bath aligned with `g` can remove the rejection entirely. We restrict the scaling theorem to independent local generation.

## 2.2. Bright extraction and local dephasing

A counted sink extracts the bright state at rate `kappa_N`. Independent local pure dephasing acts at rate `gamma_N`.

Within the surviving one-excitation manifold define

```math
P(t)=\operatorname{Tr}\rho(t),
\qquad
b(t)=\langle B|\rho(t)|B\rangle.
```

Permutation symmetry gives

```math
\boxed{\dot P=-\kappa_Nb,}
```

```math
\boxed{
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P.
}
```

Therefore

```math
\boxed{
\ddot P
+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
}
```

Let

```math
a_N=\kappa_N+\gamma_N,
```

```math
\Delta_N=\sqrt{a_N^2-4\kappa_N\gamma_N/N},
```

```math
r_{\pm,N}=(a_N\pm\Delta_N)/2.
```

For initial bright population `b_0`,

```math
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa_Nb_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa_Nb_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
```

Collection is `C=1-P`. The photon-created bright event uses `b_0=1`; one uniformly local dark event uses `b_0=1/N`.

For every nonzero dephasing rate both are eventually collected. State-space rejection is therefore finite-time.

The slow recycling rate is

```math
\boxed{
r_{-,N}
=\frac{1}{N}
\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
}
```

---

# 3. Counting model and fixed-efficiency task

The one-excitation master equation supplies the exact collection kernel for one generated excitation. Continuous local generation is represented by an explicit extensive low-density lift: each of the `N` microscopic sites generates distinguishable, noninteracting dark excitations as an independent Poisson process of fixed rate `d`, and each excitation follows an independent copy of the one-body kernel.

Thus the raw local generation rate is `Nd`, and the accepted local-dark mean in a gate `[0,T]` is

```math
\boxed{
\mu_{loc,N}(T)
=Nd\int_0^T C_{D,N}(u)du.
}
```

A photon that has already prepared `|B>` is collected with **conditional internal** efficiency

```math
\eta_{int,N}(T)=C_{S,N}(T).
```

We do not model the preceding optical absorption probability.

For a fixed target `0<eta<1`, define

```math
\boxed{
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\},
}
```

and

```math
\boxed{
\mu_{loc,N}(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
}
```

The detector question is whether `mu_loc,N(eta)` remains bounded as the number of local dark-generation sites grows.

---

# 4. Rate-scaling classification

Take

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
```

Define

```math
q_N
=\frac{\kappa_N}{\kappa_N+\gamma_N}.
```

Then

```math
q_N\to
\begin{cases}
1,&\alpha>\beta,\\
q_0=\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

The sign of `alpha-beta` therefore decides whether a fixed efficiency target lies on the fast branch, on an efficiency-dependent balanced branch, or on the slow-recycling branch.

## 4.1. Extraction outruns dephasing: alpha > beta

Every fixed `eta<1` eventually lies on the fast branch. With

```math
x_\eta=-\ln(1-\eta),
```

```math
\boxed{
T_N
\sim\frac{x_\eta}{\kappa_0}N^{-\alpha},
}
```

and

```math
\boxed{
\mu_{loc,N}
\sim\frac{d}{\kappa_0}
[x_\eta-\eta]N^{-\alpha}.
}
```

## 4.2. Dephasing outruns extraction: alpha < beta

Every fixed positive `eta` eventually requires slow recycling. Again using `x_eta=-ln(1-eta)`,

```math
\boxed{
T_N
\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha},
}
```

```math
\boxed{
\mu_{loc,N}
\sim\frac{d}{\kappa_0}
[x_\eta-\eta]N^{2-\alpha}.
}
```

## 4.3. Balanced scaling: alpha = beta = s

Set

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0},
```

```math
A=\kappa_0+\gamma_0,
\qquad
\lambda_0=\frac{\kappa_0\gamma_0}{A}.
```

For `eta<q_0`, let `x_eta=-ln(1-eta/q_0)`. Then

```math
T_N\sim(x_\eta/A)N^{-s}
```

and

```math
\mu_{loc,N}
\sim\frac{d}{A}
\left[
\frac{q_0(1-q_0)}2x_\eta^2
+q_0^2x_\eta-q_0\eta
\right]N^{-s}.
```

At `eta=q_0`,

```math
T_N=\Theta(N^{-s}\ln N),
```

```math
\mu_{loc,N}=\Theta[N^{-s}(\ln N)^2].
```

For `eta>q_0`, define

```math
L_\eta=\ln\frac{1-q_0}{1-\eta},
```

```math
H_\eta=L_\eta-\frac{\eta-q_0}{1-q_0}.
```

Then

```math
\boxed{
T_N\sim\frac{L_\eta}{\lambda_0}N^{1-s},
}
```

```math
\boxed{
\mu_{loc,N}\sim\frac{dH_\eta}{\lambda_0}N^{2-s}.
}
```

The fixed-rate theorem is the special case `s=0`.

---

# 5. Bounded microscopic extraction resource

The formal scaling classification allows arbitrarily large positive `alpha`. A linear single-excitation extractor with a fixed microscopic coupling budget does not.

Allow arbitrary counted sink channels `a` and write

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0.
```

For normalized excitation `|psi>`, the counted extraction rate is

```math
\kappa(\psi)=\langle\psi|K|\psi\rangle.
```

Assume each local state has an `N`-independent total counted-coupling budget

```math
K_{jj}\le\kappa_{loc}.
```

Then

```math
\boxed{
\kappa(\psi)
\le\lambda_{max}(K)
\le\operatorname{Tr}K
\le N\kappa_{loc}.
}
```

Therefore

```math
\boxed{\alpha\le1.}
```

Linear collective enhancement can saturate this bound when all local extraction amplitudes add coherently into one counted sink.

This removes the mathematical `alpha>=2` escape that would otherwise keep a slow-recycling dark burden bounded.

---

# 6. Main detector theorem — scalable efficiency ceiling

Assume additionally that useful extraction does not weaken with system size,

```math
0\le\alpha\le1.
```

Define

```math
\eta_{sc}
=\sup\{\eta\in(0,1):\mu_{loc,N}(\eta)=O(1)\}.
```

Then

```math
\boxed{
\eta_{sc}
=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

### Proof from the scaling laws

If `alpha>beta`, every fixed `eta<1` is fast branch and

```math
\mu_{loc,N}\asymp N^{-\alpha}=O(1).
```

Hence the supremum is one.

If `alpha=beta=s`, every `eta<q_0` has

```math
\mu_{loc,N}\asymp N^{-s}=O(1),
```

whereas every strict `eta>q_0` has

```math
\mu_{loc,N}\asymp N^{2-s}.
```

Because `s<=1`, every strict supercritical target diverges at least linearly. Thus the supremum is `q_0`.

If `alpha<beta`, every fixed positive target has

```math
\mu_{loc,N}\asymp N^{2-\alpha}.
```

With `alpha<=1`, this is at least linear, so no nonzero fixed efficiency is scalable and the supremum is zero.

Therefore any operating point that lies **strictly on the slow-recycling side** incurs

```math
\boxed{
\mu_{loc,N}=\Omega(N)
}
```

under bounded local counted coupling.

### Balanced-boundary detail

At `alpha=beta=s` and `eta=q_0`, local-dark burden scales as

```math
N^{-s}(\ln N)^2.
```

For `s=0`, `q_0` is a supremum but not itself a bounded operating point. For any `s>0`, the local-dark contribution at the boundary tends to zero. The distinction matters once thermally reversed extraction is included below.

---

# 7. Thermally reversed counted extraction

Suppose the counted transition itself has a reverse process obeying effective local detailed balance,

```math
\bar\kappa_N
=\kappa_Ne^{-\Delta F_N/(kT)}.
```

A reverse injection creates a bright excitation. Under the same independent-event approximation its accepted reverse contribution is

```math
\mu_{rev,N}
=\bar\kappa_N
\int_0^{T_N(\eta)}C_{S,N}(u)du.
```

For fixed thermodynamic affinity, the gate scaling gives

```math
\boxed{
\mu_{rev,N}\sim
\begin{cases}
O(1), & \alpha>\beta,\\
O(1), & \alpha=\beta,\ \eta<q_0,\\
O(\ln N), & \alpha=\beta,\ \eta=q_0,\\
O(N), & \alpha=\beta,\ \eta>q_0,\\
O(N), & \alpha<\beta.
\end{cases}}
```

Thus the earlier rate-only statement “collective enhancement requires `kT ln N` extra affinity” is not the correct gated detector law. On a fast branch the increased reverse rate is canceled by the shorter efficiency-selected gate.

Keeping the gated reverse burden bounded requires only constant affinity on a fast branch, an additional `kT ln ln N` at the balanced boundary, and `kT ln N` on a strict slow branch.

For the favorable maximally collective example

```math
\kappa_N\propto N,
\qquad
\gamma_N=O(1),
```

one obtains

```math
\mu_{loc,N}\sim N^{-1},
```

while at fixed affinity

```math
\mu_{rev,N}=O(1).
```

The reversible extractor therefore becomes the asymptotic floor even though it does not diverge with detector size.

---

# 8. Relation to prior work

The closest coherent detector precedent is Young, Sarovar, and Leonard [2]. Their design already uses coherently interacting nanoscale elements and identifies dark-to-optically-active relaxation as incompatible with their ideal-efficiency conditions. The present work should be read as quantifying the scalability penalty when this isolation condition fails while an extensive internal local-generation process is present.

The closest scaling precedent is the 2026 Dicke-superradiance theory of Bassler, Lyne, and Cuerda [7], which establishes collective/decoherence large-`N` scaling regimes. Our result does not compete with that general scaling framework. The detector-specific step is to choose the measurement gate through a required collection efficiency and propagate the resulting time scale into the total number of internally generated events accepted during measurement.

Current autonomous quantum-detector thermodynamics also establishes broad tradeoffs among thermodynamic resources, efficiency, dark counts, jitter, and dead time [8]. We therefore use the reverse-injection result only as a detector-task corollary rather than as a new thermodynamic law.

---

# 9. Scope and limitations

The theorem is a controlled analytical model, not a material proposal. It assumes:

- a symmetric coherent bright excitation;
- Markovian local pure dephasing;
- a linear bright-selective counted extractor;
- bounded per-site counted coupling for the main ceiling theorem;
- fixed per-site local dark-generation rate;
- a low-density independent-particle Poisson lift;
- fixed efficiency targets independent of `N`.

It excludes:

- same-mode photon background;
- correlated dark baths aligned with the bright state;
- energetic disorder and inhomogeneous phase evolution;
- saturation and many-excitation collective effects;
- detector reset/dead time;
- active or time-dependent extraction;
- a microscopic derivation of the achievable exponents `alpha` and `beta` in a specific material.

These restrictions are essential to the claim boundary.

---

# 10. Conclusion

Existing coherent-detector theory already identifies dark-to-bright isolation as a condition for high-performance collective photodetection. The present Gedanken model quantifies how violating that isolation affects scalability when internal local dark-generation sites grow with detector size. The accepted dark burden depends jointly on the required internal collection efficiency and on the relative system-size scaling of useful extraction and local dephasing. With bounded counted coupling per microscopic state, the resulting scalable-efficiency ceiling is one if extraction outruns dephasing, the finite fast-branch fraction `kappa_0/(kappa_0+gamma_0)` if the two rates scale together, and zero if dephasing outruns extraction. Any strict slow-recycling operating point then incurs at least a linear accepted local-dark burden. A thermally reversed extractor adds a branch-dependent gated floor rather than a universal penalty proportional to its collective forward rate. These results define a narrow detector scalability theorem within an established coherent collective architecture.

---

# Working references

[1] S. M. Young, M. Sarovar, and F. Leonard, “Fundamental limits to single-photon detection determined by quantum coherence and backaction,” *Phys. Rev. A* **97**, 033836 (2018). DOI `10.1103/PhysRevA.97.033836`.

[2] S. M. Young, M. Sarovar, and F. Leonard, “Design of High-Performance Photon-Number-Resolving Photodetectors Based on Coherently Interacting Nanoscale Elements,” *ACS Photonics* **7**, 821–830 (2020). DOI `10.1021/acsphotonics.9b01754`.

[3] N. Shammah, N. Lambert, F. Nori, and S. De Liberato, “Superradiance with local phase-breaking effects,” *Phys. Rev. A* **96**, 023863 (2017). DOI `10.1103/PhysRevA.96.023863`.

[4] C. Creatore, M. A. Parker, S. Emmott, and A. W. Chin, “Efficient biologically inspired photocell enhanced by delocalized quantum states,” *Phys. Rev. Lett.* **111**, 253601 (2013). DOI `10.1103/PhysRevLett.111.253601`.

[5] A. Fruchtman, R. Gomez-Bombarelli, B. W. Lovett, and E. M. Gauger, “Photocell optimization using dark state protection,” *Phys. Rev. Lett.* **117**, 203603 (2016). DOI `10.1103/PhysRevLett.117.203603`.

[6] F. Pisani et al., “Electronic transport driven by collective light-matter coupled states in a quantum device,” *Nature Communications* **14**, 3914 (2023). DOI `10.1038/s41467-023-39594-z`.

[7] N. S. Bassler, J. Lyne, and J. Cuerda, “Scaling theory of decoherence in Dicke superradiance,” arXiv:`2607.28034` (2026).

[8] E. Schwarzhans et al., “Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition,” *PRX Quantum* **7**, 033001 (2026). DOI `10.1103/wm5p-tjtg`.

---

# Rev. 3 gate

If this compressed manuscript survives one more significance/novelty review, the next useful work is figures and journal-facing preparation rather than additional arbitrary theory branches.
