# Coherence-selective suppression of internal dark counts in a gated photodetector

**Draft status:** Rev. 0 / theory manuscript opened for adversarial review  
**Date:** 2026-08-14  
**Scope:** analytical/theoretical  
**Novelty status:** not established; no priority language authorized

## Abstract

Internal dark generation in a photodetector normally grows with the number of available microscopic generation sites. We ask whether this scaling can change if photon absorption prepares a coherent material excitation while internal dark processes populate the same microscopic states incoherently. In an `N`-state model, a bright-selective counted channel accepts the photon-created state with unit ideal probability but only the bright component of local dark excitations. For independent Poisson dark generation at rate `d` per site, the accepted gated dark-count mean is exactly independent of `N` in the coherence-preserving limit, despite a raw generation rate `Nd`. Local dephasing restores extensive dark leakage at long times. If useful extraction is collectively enhanced by a factor `mathcal C` and obeys local detailed balance, holding its thermally reversed bright-injection dark floor fixed requires at least `kT ln mathcal C` additional effective free-energy bias. The result identifies a finite-time coherence-based route to nonextensive internal dark counts and the dynamical and thermodynamic resources required to maintain it.

---

# 1. Introduction

Dark current and dark counts are central limits in photodetection. Their microscopic origins vary across detector classes—thermal generation, generation-recombination centers, tunneling, impact ionization, metastable switching, and other processes—but a common geometric feature is that increasing the amount of electrically active material generally increases the number of places where an internal dark event can originate. Many successful detector architectures therefore suppress dark current by reducing the electrically active volume, increasing energetic barriers, cooling the detector, improving material quality, or separating optical collection area from electrical area.

This paper asks a different theoretical question. Suppose an absorber contains `N` microscopic excited states and both a photon-created event and an internally generated dark event contain exactly one excitation. Suppose further that the two events have the same energy and the same probability of occupying each microscopic state. Can they nevertheless be distinguished by an ideal counted channel?

They can if the photon and dark bath populate different **directions in excitation Hilbert space**. A coherent optical field can prepare one bright superposition of the microscopic states, whereas statistically independent local dark processes generate the corresponding incoherent mixture. Energy, carrier number, and all observables diagonal in the local-state basis are then deliberately made useless; coherence is the only remaining event label.

The generic quantum-information statement that a coherent state and its dephased mixture are distinguishable is established. Collective bright and dark states, dephasing-induced transfer between them, and local detailed balance are also established. The question here is narrower and detector-specific: **what do those structures imply for the scaling of actual gated dark counts when the absorber contains many independent internal dark-generation sites?**

We obtain three connected results. First, for a bright-selective extractor, independent local dark generation with total raw rate `Nd` produces an accepted gated dark-count mean that is exactly independent of `N` when coherence is preserved. Second, local dephasing makes the effect finite-time; every dark excitation is eventually transferred into the counted bright sector for any nonzero dephasing rate. Third, if useful counted extraction is itself collectively enhanced and thermally reversible, the reverse bright-injection dark channel inherits that rate enhancement unless additional thermodynamic affinity is supplied. For a collective forward-rate enhancement `mathcal C`, a bounded reverse floor requires at least

```math
\Delta F_{extra}\ge kT\ln\mathcal C.
```

The result is therefore not a proposal for free dark-current elimination. It is a controlled counterexample to the assumption that accepted internal dark counts must necessarily inherit the raw extensive scaling of the microscopic generation volume. The coherence advantage exists only over a finite decision window and remains subject to ordinary thermodynamic reversibility of the counted extraction process.

The model is intentionally minimal. It is not assigned to a particular semiconductor, exciton platform, or detector technology. This separation is useful because it lets us determine which parts of the scaling follow from state geometry alone and which require additional material physics.

---

# 2. Coherent signal and incoherent internal dark excitation

## 2.1. Excitation manifold

Let the single-excitation manifold contain orthonormal local states

```math
|j\rangle,
\qquad
j=1,\ldots,N.
```

An optical mode couples through amplitudes `g_j`. The normalized photon-created bright excitation is

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

the local populations of the bright state are `w_j`.

Construct the adversarial internal dark event to have exactly those same populations but no phase coherence:

```math
\boxed{
\rho_D
=\sum_{j=1}^{N}w_j|j\rangle\langle j|.
}
```

Thus

```math
\langle j|\rho_D|j\rangle
=|\langle j|B\rangle|^2
=w_j.
```

Any observable diagonal in the local basis gives identical statistics for the photon and dark event.

## 2.2. Bright-selective counted channel

Consider an ideal counted measurement with acceptance operator

```math
\Pi_B=|B\rangle\langle B|.
```

The photon-created state is accepted with probability

```math
\boxed{\eta_S=1.}
```

The population-matched incoherent dark state is accepted with probability

```math
\boxed{
\epsilon_D
=\mathrm{Tr}(\Pi_B\rho_D)
=\sum_jw_j^2
=\frac{1}{N_{eff}},
}
```

where

```math
N_{eff}=\frac{1}{\sum_jw_j^2}.
```

For equal optical participation,

```math
w_j=1/N,
```

and therefore

```math
\boxed{\epsilon_D=1/N.}
```

Among positive measurement operators constrained to accept `|B>` with probability one, `Pi_B` is the minimum-support choice and minimizes acceptance of positive weight outside the bright direction. This is standard state-verification mathematics; its role here is to define the detector's counted sector.

## 2.3. General internal dark-generation covariance

Let independent or correlated microscopic dark-generation channels be represented by vectors `|l_alpha>` in the excitation manifold. Define

```math
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|.
```

The total raw internal dark-generation strength is proportional to

```math
\mathrm{Tr}D.
```

The rate injected directly into the counted bright direction is instead

```math
\boxed{
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

The raw dark process is therefore trace-like, while the accepted process is a Rayleigh quotient along the optical coupling vector.

For independent identical local dark channels,

```math
D=dI,
```

so

```math
\boxed{\mathrm{Tr}D=Nd,}
```

but

```math
\boxed{\Gamma_D^B=d.}
```

This static scaling difference motivates the gated detector calculation below.

---

# 3. Counted extraction in the presence of local dephasing

For the remainder of the main derivation we use the symmetric bright state

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle.
```

Let counted extraction act only on the bright state at rate `kappa`, and let independent local pure dephasing act at rate `gamma`.

Define the surviving excitation probability

```math
P(t)=\mathrm{Tr}\rho(t)
```

within the uncounted excitation manifold and the bright population

```math
b(t)=\langle B|\rho(t)|B\rangle.
```

The symmetric dynamics closes exactly:

```math
\boxed{\dot P=-\kappa b,}
```

```math
\boxed{
\dot b
=-(\kappa+\gamma)b
+\frac\gamma N P.
}
```

Eliminating `b` gives

```math
\boxed{
\ddot P
+(\kappa+\gamma)\dot P
+\frac{\kappa\gamma}{N}P=0.
}
```

Define

```math
\Delta
=\sqrt{(\kappa+\gamma)^2-rac{4\kappa\gamma}{N}},
```

and

```math
r_\pm
=\frac{\kappa+\gamma\pm\Delta}{2}.
```

For an initial state with bright population `b_0`, `P(0)=1` and `\dot P(0)=-\kappa b_0`, so

```math
\boxed{
P_{b_0}(t)
=
\frac{r_+-\kappa b_0}{\Delta}e^{-r_-t}
+
\frac{\kappa b_0-r_-}{\Delta}e^{-r_+t}.
}
```

The probability of a counted extraction by time `t` is

```math
C_{b_0}(t)=1-P_{b_0}(t).
```

For a photon-created bright excitation,

```math
b_{0,S}=1,
```

while a uniformly local internal dark event has

```math
b_{0,D}=1/N.
```

We write the corresponding collection kernels as `C_S(t)` and `C_D(t)`. Their exact difference is

```math
\boxed{
C_S(t)-C_D(t)
=
\frac{\kappa(1-1/N)}{\Delta}
\left(e^{-r_-t}-e^{-r_+t}\right).
}
```

For `N>1`, the signal collection probability is strictly larger at every finite `t>0`. For any `gamma>0`, however,

```math
\boxed{
C_S(\infty)=C_D(\infty)=1.
}
```

Thus local dephasing converts the static state-space discrimination into a finite-time resource.

For large `N`,

```math
r_-
\simeq
\frac{\kappa\gamma}{N(\kappa+\gamma)},
```

which gives the slow leakage time

```math
\boxed{
\tau_{leak}
\simeq
N\left(\frac1\kappa+\frac1\gamma\right).
}
```

High signal collection before dephasing destroys the bright state requires `kappa>>gamma`.

---

# 4. Exact gated internal-dark-count scaling

We now turn the conditional single-excitation result into a photodetection task.

Assume each of the `N` local sites generates internal dark excitations as an independent Poisson process with rate `d`. The total raw internal dark-generation rate is

```math
\Gamma_{raw}=Nd.
```

Open a detection gate of duration `T` with the excitation manifold initially empty. A dark excitation created at time `s` has age `u=T-s` at gate closure and is counted with probability `C_D(u)`. Independent Poisson thinning therefore gives a Poisson-distributed number of accepted internal dark counts with exact mean

```math
\boxed{
\mu_{local}(T)
=Nd\int_0^T C_D(u)\,du.
}
```

The corresponding false-count probability is

```math
\boxed{
P_{FA,local}(T)
=1-e^{-\mu_{local}(T)}.
}
```

A photon arriving at the gate opening is detected with probability

```math
\boxed{
\eta_S(T)=C_S(T).
}
```

These two quantities define an explicit reduced-model detection operating curve as `T` is varied.

## 4.1. Coherence-preserving theorem

When `gamma=0`, the photon and dark collection kernels reduce to

```math
C_S(t)=1-e^{-\kappa t},
```

and

```math
\boxed{
C_D(t)=\frac1N(1-e^{-\kappa t}).
}
```

Substitution into the gated Poisson mean gives

```math
\mu_{local}(T)
=Nd\int_0^T\frac1N(1-e^{-\kappa u})du,
```

hence

```math
\boxed{
\mu_{local}(T)
=d\left[
T-\frac{1-e^{-\kappa T}}{\kappa}
\right].
}
```

The factor `N` cancels exactly.

The raw internal generation process is extensive,

```math
\Gamma_{raw}\propto N,
```

while the accepted gated count mean is nonextensive,

```math
\boxed{\mu_{local}(T)=O(1).}
```

At the same time, for `\kappa T>>1`,

```math
\eta_S(T)\to1.
```

Thus in the ideal coherence-preserving model, increasing the number of independent dark-generating microscopic sites does not increase the accepted internal false-count mean of the bright-selective detector.

This result does not arise from reducing the number of dark-generating sites. All `N` sites remain present and the raw dark-generation rate remains `Nd`; the cancellation occurs because independent local dark events occupy only `1/N` of the counted coherent direction on average.

## 4.2. Finite dephasing

For `gamma>0`, `C_D(t)` eventually approaches unity, so sufficiently long gates recover extensive counting:

```math
\mu_{local}(T)\sim NdT
```

at long times.

The useful coherence-selective regime requires

```math
1/r_+\ll T\ll1/r_-.
```

For `kappa>>gamma` and large `N`, this becomes approximately

```math
\boxed{
1/\kappa\ll T\ll N/\gamma.
}
```

Within this finite gate, signal collection can be close to unity while the accepted internal dark process remains approximately nonextensive. Dephasing therefore sets the lifetime of the scaling advantage.

---

# 5. Thermally reversible extraction and the return of a dark floor

The previous result concerns internal local dark generation. The counted extraction channel itself can generate a second dark mechanism through thermally reversed injection into the bright state.

Let counted extraction occur through arbitrary stationary channels `a` with forward coefficients `\kappa_a`. Assume each channel obeys local detailed balance,

```math
\frac{\bar\kappa_a}{\kappa_a}
=e^{-\beta\Delta F_a},
\qquad
\beta=(kT)^{-1}.
```

Define

```math
K_\to=\sum_a\kappa_a,
```

```math
K_\leftarrow=\sum_a\bar\kappa_a,
```

and forward weights

```math
p_a=\frac{\kappa_a}{K_\to}.
```

Then

```math
\boxed{
\frac{K_\leftarrow}{K_\to}
=\sum_ap_ae^{-\beta\Delta F_a}
=e^{-\beta\Delta F_{eff}},
}
```

where

```math
\boxed{
\Delta F_{eff}
=-kT\ln\left(\sum_ap_ae^{-\beta\Delta F_a}\right).
}
```

The effective affinity satisfies

```math
\min_a\Delta F_a
\le\Delta F_{eff}
\le\sum_ap_a\Delta F_a
\le\max_a\Delta F_a.
```

Thus adding heterogeneous passive pathways cannot create reverse suppression stronger than the available microscopic affinities.

Suppose useful counted extraction is enhanced collectively by

```math
K_\to(N)
=\mathcal C(N)K_\to(1).
```

The reverse coefficient is

```math
K_\leftarrow(N)
=K_\to(N)e^{-\beta\Delta F_{eff}(N)}.
```

Requiring

```math
K_\leftarrow(N)
\le K_\leftarrow(1)
```

therefore gives

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge kT\ln\mathcal C(N).
}
```

For equal collectively coupled constituents with `\mathcal C=N`, this becomes

```math
\Delta F_{extra}\ge kT\ln N.
```

A reverse injection creates a bright excitation and can later produce a counted forward event. In the dilute Poisson limit its gated contribution is

```math
\boxed{
\mu_{rev}(T)
=K_\leftarrow\int_0^T C_S(u)du.
}
```

The total reduced-model dark-count mean is therefore

```math
\boxed{
\mu_{dark}(T)
=\mu_{local}(T)+\mu_{rev}(T).
}
```

In the high-efficiency finite gate,

```math
\int_0^T C_S(u)du\simeq T,
```

so

```math
\mu_{rev}(T)
\simeq
K_\to e^{-\beta\Delta F_{eff}}T.
```

The thermodynamic affinity bound is therefore directly a false-count scaling law.

---

# 6. Discussion

## 6.1. What is being suppressed?

The mechanism applies to **internally generated incoherent excitations** whose state-space covariance is not aligned with the optically prepared bright vector. It does not reject a thermal or background photon entering through the same optical mode as the signal, because such a photon prepares the same bright excitation.

This distinction is important for infrared detection, where background photon flux and internal generation-recombination noise can be separate limitations.

## 6.2. Difference from optical/electrical area decoupling

Resonant infrared detectors and antenna-coupled photodetectors can achieve a photonic collection area larger than the electrically active semiconductor area. This is a powerful established route to suppress dark current while preserving optical coupling.

The present construction is different. The theorem retains all `N` microscopic dark-generating sites and therefore retains the raw generation rate `Nd`. It reduces only the fraction of those internally generated excitations that occupy the counted Hilbert-space direction. The distinction is therefore

```text
physical-space suppression
versus
state-space suppression.
```

Whether a real device can exploit the latter strongly enough to outperform ordinary geometric strategies is a separate materials problem and is not claimed here.

## 6.3. Dephasing as a finite-window constraint

The coherence-selected dark advantage cannot survive indefinitely. Local dephasing continuously transfers population between bright and dark sectors. The slow eigenvalue

```math
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)}
```

sets the leakage of initially rejected excitations into the counted channel. Consequently, the useful resource is not coherence in the abstract but a separation of timescales:

```math
1/\kappa
\ll T
\ll1/r_-.
```

This makes the prediction operationally falsifiable within any microscopic realization of the model.

## 6.4. Thermodynamic cost of collective extraction

The local-dark cancellation can create the appearance that increasing the number of coherently participating sites gives signal scaling without a corresponding dark penalty. Local detailed balance shows why that conclusion is incomplete. If the useful counted extraction rate itself is enhanced, its reverse thermal coefficient carries the same enhancement unless the effective free-energy drop increases.

For a collective rate enhancement `mathcal C`, the required compensation is logarithmic:

```math
\Delta F_{extra}\ge kT\ln\mathcal C.
```

At `77 K`, the equal-emitter special case gives approximately

```text
N=10:    15.28 meV
N=100:   30.56 meV
N=1000:  45.84 meV.
```

These values are scale illustrations, not material-design recommendations.

## 6.5. Scope and possible escape routes

The theory assumes a single-excitation manifold, dilute independent Poisson dark generation, Markovian local dephasing, a bright-selective counted channel, and local detailed balance for the thermally reversible extraction channels.

Several physically meaningful directions lie outside that theorem class:

- correlated dark baths whose covariance is itself aligned with the optical bright vector;
- strongly non-Markovian transient dynamics;
- static nonreciprocal systems in which pairwise local detailed balance is not represented by one scalar forward/reverse ratio;
- actively driven or time-modulated extraction;
- maintained nonequilibrium reservoirs or chemical biases;
- saturation and many-excitation effects;
- real material constraints on creating and preserving the required coherent excitation.

These are not assumed impossible. They specify where additional resources enter.

---

# 7. Conclusion

A simple photodetector Gedanken experiment reveals a distinction between the number of microscopic dark-generation sites and the number of dark events accepted by a coherent counted channel. When a photon prepares one bright superposition across `N` local excited states while independent internal dark processes populate those states incoherently, the raw dark-generation rate grows as `Nd` but the accepted gated dark-count mean is exactly independent of `N` in the coherence-preserving limit. Local dephasing makes this nonextensive scaling finite-time, with a slow leakage time that grows approximately as `N(1/kappa+1/gamma)`. If useful counted extraction is collectively enhanced and thermally reversible, maintaining a fixed reverse bright-injection dark floor requires at least `kT ln mathcal C` additional effective free-energy bias for a forward-rate enhancement `mathcal C`. The resulting detector theory separates three resources that are usually conflated: microscopic dark-generation volume, excitation-state coherence, and thermodynamic extraction asymmetry.

---

# Reference placeholders for Rev. 0

The next draft must replace these category placeholders with verified full citations from the primary-source audit.

1. Quantum state discrimination / state verification.
2. Quantum detector tomography with coherence-sensitive POVMs.
3. Collective bright/dark-state and superradiance theory.
4. Dephasing-induced bright/dark transfer.
5. Collective electronic transport in a quantum infrared detector: Nature Communications 14, 3914 (2023), DOI `10.1038/s41467-023-39594-z`.
6. Resonant infrared detector optical-area/electrical-area decoupling: Nature Communications (2020), `s41467-020-14426-6`.
7. Quantum jump photodetector: Phys. Rev. Research 6, 033338 (2024), DOI `10.1103/PhysRevResearch.6.033338`.
8. Local detailed balance across scales: Phys. Rev. E 103, 042114 (2021), DOI `10.1103/PhysRevE.103.042114`.
9. Quantum detailed balance/KMS thermalization.
10. Superradiant many-qubit absorption refrigerator: Phys. Rev. Applied 16, 044061 (2021), DOI `10.1103/PhysRevApplied.16.044061`.
11. Nonreciprocal many-body radiative heat transfer: Phys. Rev. B 97, 094302 (2018), DOI `10.1103/PhysRevB.97.094302`.
12. Thermodynamic constraints on reciprocal/nonreciprocal radiative heat transfer: Phys. Rev. B 102, 085401 (2020), DOI `10.1103/PhysRevB.102.085401`.

---

# Rev. 0 review gate

Before expanding this manuscript:

1. perform a hostile referee-style review focused on whether the central gated `N` cancellation is scientifically distinct enough from ordinary state discrimination and optical/electrical area decoupling;
2. independently re-derive the Poisson-thinning and finite-dephasing equations from the Lindblad model;
3. generate only figures that expose the exact scaling claims;
4. do not add material-specific device speculation merely to make the paper look more practical;
5. if the hostile reviewer finds a direct stronger theorem or a fatal physical equivalence to established detector architecture, close the manuscript honestly.
