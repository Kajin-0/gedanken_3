# Paper architecture — Coherence-selective internal-dark scaling

**Date:** 2026-08-14  
**Status:** MANUSCRIPT PHASE OPEN / ARCHITECTURE ONLY / NOVELTY NOT CLAIMED

## Recommended working title

> **Coherence-selective suppression of internal dark counts in a gated photodetector**

Alternative, more theorem-forward:

> **Nonextensive internal dark counts from coherent photodetection**

Avoid `fundamental`, `novel`, `first`, and `quantum advantage` in the title until external-style review supports stronger language.

---

# Central paper claim

Do not center the manuscript on the generic fact that coherent and incoherent density matrices can be distinguished.

Center it on the detector-level theorem:

> In a gated detector whose photon creates one coherent bright excitation across `N` local states while independent internal dark events populate those same states incoherently, an ideal bright-selective extractor can make the accepted internal dark-count mean independent of `N` even though raw internal dark generation grows as `Nd`. Local dephasing makes this advantage finite-time, and collectively enhanced thermally reversible extraction requires an additional effective free-energy bias of at least `kT ln mathcal C` to keep its reverse bright-injection dark floor fixed.

The cleanest exact result is

```math
\boxed{
\mu_{local}(T)
=d\left[
T-\frac{1-e^{-\kappa T}}{\kappa}
\right]
\qquad(\gamma=0),
}
```

while

```math
\Gamma_{dark}^{raw}=Nd.
```

This exact cancellation of `N` is the conceptual center of the paper.

---

# Proposed article structure

## 1. Introduction

Four moves only.

### Move 1 — detector problem

Internal dark generation usually grows with the number/volume of available microscopic generation sites. Conventional strategies suppress it through energetic barriers, reduced electrical volume, cooling, material quality, etc.

### Move 2 — Gedanken question

Ask whether a photon-created excitation and an internally generated excitation can be physically distinguishable even when they contain the **same carrier number, energy, and microscopic populations**.

Force the only difference to be coherence.

### Move 3 — answer

Yes. A photon can prepare a coherent bright superposition while independent local dark processes create the corresponding incoherent mixture. A bright-selective counted channel distinguishes these states without sacrificing ideal signal-state acceptance.

### Move 4 — paper contribution and limits

State the gated scaling theorem, finite-dephasing leakage, and thermodynamic reverse-channel cost.

Immediately acknowledge that state discrimination, collective bright/dark physics, and local detailed balance are established; the paper studies their detector-specific composition and exact dark-count scaling.

Do not begin with a long general discussion of `D*`, quantum sensing, or detector figures of merit.

---

# 2. Minimal state-space detector

## 2.1 Excitation manifold

Use local states

```math
|j\rangle,
\qquad j=1,...,N.
```

Photon coupling vector

```math
g=(g_1,...,g_N)^T
```

prepares

```math
|B\rangle
=\frac{1}{\sqrt{g^\dagger g}}
\sum_jg_j|j\rangle.
```

For the symmetric theorem use

```math
|B\rangle=\frac1{\sqrt N}\sum_j|j\rangle.
```

## 2.2 Population-matched dark event

Construct the adversarial dark state to have the same diagonal populations:

```math
\rho_D
=\sum_jw_j|j\rangle\langle j|.
```

This makes energy, carrier number, and every diagonal observable exactly useless for provenance discrimination.

## 2.3 Unit-signal-efficiency optimum

For

```math
\Pi_B=|B\rangle\langle B|,
```

```math
\eta_S=1,
```

```math
\epsilon_D=\sum_jw_j^2=1/N_{eff}.
```

State and prove briefly that among POVM elements satisfying unit acceptance of `|B>`, `Pi_B` minimizes acceptance of `rho_D`.

Generalize internal dark generation with covariance/Kossakowski matrix `D`:

```math
\boxed{
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

For `D=dI`,

```math
\Gamma_D^B=d
```

while total raw dark generation is `Tr D=Nd`.

This Rayleigh-quotient versus trace distinction is the general state-space statement.

---

# 3. Finite-time counted extraction

## 3.1 Markov model

Bright extraction `kappa` plus local dephasing `gamma`:

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+(\gamma/N)P.
```

Obtain

```math
\ddot P+(\kappa+\gamma)\dot P+(\kappa\gamma/N)P=0.
```

Define `Delta`, `r_+`, `r_-` and give the exact solution for arbitrary initial bright population `b_0`.

## 3.2 Photon and local-dark collection kernels

Use

```math
b_{0,S}=1,
\qquad
b_{0,D}=1/N.
```

Define

```math
C_S(t),
\qquad
C_D(t).
```

Main exact finite-time separation:

```math
\boxed{
C_S(t)-C_D(t)
=\frac{\kappa(1-1/N)}{\Delta}
\left(e^{-r_-t}-e^{-r_+t}\right).
}
```

Show:

```text
positive for every finite t>0;
zero at t=0;
returns to zero as t->infinity for gamma>0.
```

Give

```math
t_*=\ln(r_+/r_-)/\Delta
```

if useful, probably in an appendix unless it materially helps a figure.

## 3.3 Finite-dephasing no-go

For every `gamma>0`,

```math
C_S(\infty)=C_D(\infty)=1.
```

Thus coherence selection is not a permanent dark-current eliminator.

Large-`N` slow leakage:

```math
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)},
```

```math
\tau_{leak}\simeq N(1/\kappa+1/\gamma).
```

---

# 4. Exact gated dark-count theorem

This should be the strongest Results subsection and probably the abstract's mathematical centerpiece.

## 4.1 Continuous local dark generation

Each local site generates dark excitations as an independent Poisson process with rate `d`.

Raw generation:

```math
\Gamma_{raw}=Nd.
```

A dark event created at time `s` inside a gate `[0,T]` is counted with probability `C_D(T-s)`.

Poisson thinning gives

```math
\boxed{
\mu_{local}(T)
=Nd\int_0^T C_D(u)du.
}
```

and

```math
P_{FA,local}(T)=1-e^{-\mu_{local}(T)}.
```

A photon arriving at the gate opening is detected with

```math
\eta_S(T)=C_S(T).
```

This is the paper's explicit reduced-model ROC.

## 4.2 Exact coherence-preserving cancellation

For `gamma=0`,

```math
C_D(t)=\frac1N(1-e^{-\kappa t}).
```

Therefore

```math
\boxed{
\mu_{local}(T)
=d\left[
T-\frac{1-e^{-\kappa T}}{\kappa}
\right].
}
```

`N` cancels exactly.

State explicitly:

```text
raw internal dark-generation rate: O(N)
accepted gated dark-count mean: O(1)
ideal photon acceptance after the fast extraction time: O(1)
```

This is the paper's principal theorem/counterexample.

## 4.3 Finite-coherence window

For `gamma>0`, long gates recover

```math
\mu_{local}(T)\sim NdT.
```

The useful regime is

```math
1/r_+\ll T\ll1/r_-.
```

For `kappa>>gamma`, large `N`:

```math
1/\kappa\ll T\ll N/\gamma.
```

Within this window:

```text
signal collection near unity;
local accepted dark counts remain approximately nonextensive.
```

---

# 5. Thermodynamic cost of scalable counted extraction

## 5.1 Parallel locally detailed-balanced channels

For channels `a`,

```math
\bar\kappa_a/\kappa_a=e^{-\beta\Delta F_a}.
```

Define

```math
K_\to=\sum_a\kappa_a,
```

```math
K_\leftarrow=\sum_a\bar\kappa_a.
```

Then

```math
\boxed{
\frac{K_\leftarrow}{K_\to}
=\sum_a p_a e^{-\beta\Delta F_a}
=e^{-\beta\Delta F_{eff}}.
}
```

Give

```math
\Delta F_{eff}
=-kT\ln\sum_ap_ae^{-\beta\Delta F_a}.
```

and bounds

```math
\min\Delta F_a
\le\Delta F_{eff}
\le\sum_ap_a\Delta F_a
\le\max\Delta F_a.
```

This kills the many-passive-channel escape.

## 5.2 Collective extraction scaling

If

```math
K_\to(N)=\mathcal C(N)K_\to(1),
```

then holding reverse bright injection fixed requires

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge kT\ln\mathcal C(N).
}
```

For `mathcal C=N`, recover `kT ln N`.

At 77 K:

```text
N=10:    15.28 meV
N=100:   30.56 meV
N=1000:  45.84 meV
```

Treat these only as scale illustrations.

## 5.3 Gated reverse dark counts

Reverse bright injection contributes

```math
\mu_{rev}(T)
=K_\leftarrow\int_0^T C_S(u)du.
```

Total dark mean

```math
\boxed{
\mu_{dark}(T)
=\mu_{local}(T)+\mu_{rev}(T).
}
```

In the high-efficiency finite gate,

```math
\mu_{rev}\simeq
K_\to e^{-\beta\Delta F_{eff}}T.
```

Thus the affinity theorem is directly a false-count theorem.

---

# 6. Discussion

Organize around four questions.

## 6.1 What resource is being used?

Not extra signal energy and not extra carrier number.

The resource is **state-space direction**: optical excitation populates a coherent direction that independent local dark baths do not.

## 6.2 Why is this not ordinary optical/electrical area decoupling?

Conventional resonant detectors can maximize optical collection area while minimizing electrically active dark-current area.

Here the theorem retains all `N` dark-generating sites and raw dark generation `Nd`; it rejects their events in Hilbert space rather than eliminating their physical volume.

This comparison must be explicit and fair.

## 6.3 What dark counts cannot be rejected?

Thermal/background photons in the same optical mode create the same bright state and are indistinguishable from signal photons by this mechanism.

This theorem concerns **internally generated incoherent dark excitations**, not blackbody photon background in the accepted optical mode.

## 6.4 What breaks the theorem?

List explicitly:

```text
rapid dephasing;
collective/correlated internal dark baths aligned with g;
non-Markovian dynamics outside the reduction;
static nonreciprocity beyond pairwise LDB;
active/time-modulated extraction;
maintained nonequilibrium reservoirs;
real material constraints preventing preparation/readout of B.
```

Do not call these flaws; they define the theorem's physical boundary.

---

# 7. Conclusion

One paragraph.

Desired final logic:

```text
coherent optical preparation can make accepted internal dark counts nonextensive even when raw microscopic dark generation is extensive;
this suppression is finite-time under dephasing;
collectively enhanced reversible extraction reintroduces a logarithmic thermodynamic resource requirement;
therefore dark-current scaling depends not only on how many microscopic generation sites exist, but also on which directions of excitation Hilbert space the optical and dark processes populate.
```

---

# Proposed figures

## Figure 1 — Gedanken detector state geometry

Show `N` local states, one coherent optical bright vector, incoherent local dark injection, and bright-selective extractor.

Purpose: make the mechanism understandable without equations.

## Figure 2 — exact signal/dark collection dynamics

Plot `C_S(t)` and `C_D(t)` for one illustrative `N` and `kappa/gamma`, plus the finite contrast window.

Recommended dimensionless example for theory visualization only:

```text
N=100
kappa/gamma=100
```

Do not claim representative material values.

## Figure 3 — gated internal-dark scaling

Plot `mu_local(T)` versus `N` at fixed gate for:

```text
gamma=0;
small finite gamma;
long-gate asymptote.
```

Show the exact `gamma=0` horizontal `O(1)` behavior against raw `NdT` growth.

This is likely the strongest figure.

## Figure 4 — thermodynamic scalability

Plot required extra `Delta F/(kT)=ln mathcal C` versus collective extraction enhancement `mathcal C` on a log x-axis.

Optionally annotate `N=10,100,1000` for the equal-emitter special case.

---

# Appendices

### Appendix A — unit-signal-efficiency POVM optimum

Short proof.

### Appendix B — exact two-rate solution and finite-time contrast maximum

Include arbitrary `b_0`, `t_*`, and limiting cases.

### Appendix C — Poisson thinning derivation

Formal derivation of `mu_local` and `mu_rev`.

### Appendix D — hidden-state detailed-balance preservation

Gibbs symmetrization + Schur complement.

### Appendix E — prior-art comparison table

Only if useful; do not turn paper into a review.

---

# Closest references that must appear

At minimum, manuscript context should include primary work from these categories:

```text
quantum state discrimination / detector POVM coherence;
collective bright/dark and dephasing physics;
collective electronic transport in a quantum infrared detector (Nature Communications 2023);
resonant IR detector optical-area/electrical-area decoupling (Nature Communications 2020);
quantum-jump photodetector with low dark counts (PRR 2024);
local detailed balance / coarse graining (PRE 2021);
collective thermodynamic current/noise scaling (PR Applied 2021);
nonreciprocal thermal transport constraints (PRB 2018/2020).
```

Do not cite adjacent work merely to inflate the bibliography.

---

# Manuscript gate

The architecture is now justified.

Next action:

1. draft abstract + Introduction + theorem statement in journal-facing prose;
2. generate the exact theory figures from the closed equations;
3. perform a hostile referee review focused on **significance and novelty**, not algebra already audited;
4. if the referee can reduce the central gated `N` cancellation to a known stronger detector theorem, stop;
5. otherwise continue to a complete paper.

Do not open Experiment 10 while this manuscript candidate remains alive.
