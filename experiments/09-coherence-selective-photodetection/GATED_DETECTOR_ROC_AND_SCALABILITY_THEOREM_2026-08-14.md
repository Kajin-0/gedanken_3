# Experiment 09 — Exact gated detector ROC and scalability theorem

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT IN THE REDUCED MARKOV MODEL / CONNECTS STATE DISCRIMINATION TO A DETECTOR OPERATING POINT / NOVELTY NOT ESTABLISHED

## Purpose

The previous files establish:

1. a photon-created coherent bright state can be distinguished from an incoherent internal dark excitation with identical populations;
2. local dephasing makes this discrimination finite-time rather than permanent;
3. collectively enhanced thermally reversible extraction carries a reverse-channel free-energy cost.

This note puts those results into one explicit gated photodetection task.

The result is an exact detection-efficiency / false-count model for the reduced theory.

---

# 1. Reduced dynamics

Use the uniform bright state

```math
|B\rangle=\frac1{\sqrt N}\sum_{j=1}^N|j\rangle.
```

Bright extraction occurs at rate `kappa`; independent local pure dephasing occurs at rate `gamma`.

Let

```math
P(t)=\text{surviving excitation probability},
```

```math
b(t)=\langle B|\rho(t)|B\rangle.
```

Exactly,

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+\frac\gamma N P.
```

Therefore

```math
\ddot P+(\kappa+\gamma)\dot P+\frac{\kappa\gamma}{N}P=0.
```

Define

```math
\Delta
=\sqrt{(\kappa+\gamma)^2-\frac{4\kappa\gamma}{N}},
```

```math
r_\pm=\frac{\kappa+\gamma\pm\Delta}{2}.
```

For an initial excitation with bright population `b_0`,

```math
P(0)=1,
\qquad
\dot P(0)=-\kappa b_0.
```

The exact solution is

```math
\boxed{
P_{b_0}(t)
=
\frac{r_+-\kappa b_0}{\Delta}e^{-r_-t}
+
\frac{\kappa b_0-r_-}{\Delta}e^{-r_+t}.
}
```

The probability that the excitation has produced a counted extraction by time `t` is

```math
\boxed{
C_{b_0}(t)=1-P_{b_0}(t).
}
```

---

# 2. Photon event versus internal dark event

A photon creates the bright state, so

```math
b_{0,S}=1.
```

An internal local dark event is uniformly distributed over the `N` local states, hence

```math
b_{0,D}=1/N.
```

Define

```math
C_S(t)=C_{1}(t),
```

```math
C_D(t)=C_{1/N}(t).
```

Then the exact collection-probability separation is

```math
\boxed{
C_S(t)-C_D(t)
=
\frac{\kappa(1-1/N)}{\Delta}
\left(e^{-r_-t}-e^{-r_+t}\right).
}
```

This difference is positive for every finite `t>0` when `N>1`, and tends to zero as `t->infinity` for every `gamma>0`.

Thus:

```text
finite-time discrimination: YES
permanent discrimination under any nonzero local dephasing: NO
```

The contrast has one maximum at

```math
\boxed{
t_*
=\frac{\ln(r_+/r_-)}{r_+-r_-}
=\frac{\ln(r_+/r_-)}{\Delta}.
}
```

The corresponding maximum collection-probability gap is

```math
\boxed{
\Delta C_{max}
=
\frac{\kappa(1-1/N)}{r_+}
\left(\frac{r_-}{r_+}\right)^{r_-/\Delta}.
}
```

For `kappa >> gamma` and large `N`, the useful finite-time contrast approaches unity while the slow leakage time grows approximately as

```math
\tau_{leak}\simeq N/\gamma.
```

more precisely

```math
\tau_{leak}\simeq N(1/\kappa+1/\gamma).
```

---

# 3. Exact no-dephasing limit

For `gamma=0`,

```math
C_S(t)=1-e^{-\kappa t},
```

while

```math
\boxed{
C_D(t)=\frac1N\left(1-e^{-\kappa t}\right).
}
```

Therefore the conditional dark acceptance is exactly `1/N` of the photon acceptance at every time:

```math
\boxed{
\frac{C_D(t)}{C_S(t)}=\frac1N
\qquad(\gamma=0).
}
```

This is the dynamic form of the static bright-projector theorem.

---

# 4. Continuous internal dark generation in a finite gate

Now turn the state-discrimination problem into a detector task.

Assume independent local internal dark-generation events at each site form Poisson processes of rate `d` per site.

The total raw internal dark-generation rate is therefore

```math
Nd.
```

Open a detection gate at `t=0` with the detector initially empty. A local dark event created at time `s` has age

```math
u=T-s
```

at gate closure `T`, and is counted with probability `C_D(nu)`.

Poisson thinning gives an exact Poisson count process with mean

```math
\boxed{
\mu_{local}(T)
=Nd\int_0^T C_D(u)\,du.
}
```

Since

```math
C_D(u)=1-A_D e^{-r_-u}-B_D e^{-r_+u},
```

with

```math
A_D=\frac{r_+-\kappa/N}{\Delta},
```

```math
B_D=\frac{\kappa/N-r_-}{\Delta},
```

the integral is exact:

```math
\boxed{
\mu_{local}(T)
=Nd\left[
T
-\frac{A_D}{r_-}(1-e^{-r_-T})
-\frac{B_D}{r_+}(1-e^{-r_+T})
\right].
}
```

This expression is interpreted by continuity in the `gamma->0` limit.

The probability of at least one internally generated false count is

```math
\boxed{
P_{FA,local}(T)=1-e^{-\mu_{local}(T)}.
}
```

A photon arriving at the gate opening is detected with probability

```math
\boxed{
\eta_\gamma(T)=C_S(T).
}
```

Thus `T` parametrizes an exact reduced-model ROC curve:

```text
signal efficiency = C_S(T)
false-count probability = 1-exp[-mu_local(T)].
```

---

# 5. Exact cancellation of extensive local dark generation when gamma=0

Using

```math
C_D(u)=\frac1N(1-e^{-\kappa u}),
```

we obtain

```math
\mu_{local}(T)
=Nd\int_0^T\frac1N(1-e^{-\kappa u})du.
```

Hence

```math
\boxed{
\mu_{local}(T)
=d\left[
T-\frac{1-e^{-\kappa T}}{\kappa}
\right],
\qquad
\gamma=0.
}
```

The site number `N` cancels **exactly**.

Therefore an absorber containing `N` independent local dark-generation sources can have raw dark generation proportional to `N`, while its coherence-selective accepted dark-count mean remains independent of `N` in the ideal coherence-preserving model.

This is stronger and more detector-specific than the per-event `1/N` statement.

It is the cleanest expression of the coherence-selection resource found so far.

---

# 6. Finite-dephasing useful-window scaling

For nonzero `gamma`, long-time suppression cannot survive because

```math
C_D(t)->1.
```

Hence at sufficiently long gates

```math
\mu_{local}(T)\sim NdT.
```

The useful detector regime instead requires

```math
1/r_+\ll T\ll1/r_-.
```

For large `N`,

```math
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)}.
```

Thus the upper edge of the coherence-selective gate scales as

```math
\boxed{
T\ll
N\left(\frac1\kappa+\frac1\gamma\right).
}
```

High signal efficiency within that interval additionally requires

```math
\kappa\gg\gamma.
```

In the combined asymptotic regime

```text
kappa >> gamma,
1/kappa << T << N/gamma,
```

one has approximately

```math
C_S(T)\simeq1,
```

while accepted local-dark counts remain of order

```math
\mu_{local}(T)\sim dT
```

rather than `NdT`, until slow dephasing leakage becomes appreciable.

The coherence advantage is therefore a **finite-gate scaling regime**.

---

# 7. Add the thermally reversed counted extractor

Let the useful bright extraction consist of arbitrary locally detailed-balanced channels with total coefficients

```math
K_\to,
\qquad
K_\leftarrow
=K_\to e^{-\beta\Delta F_{eff}}.
```

A reverse event injects a bright excitation. If such injections are dilute and Poissonian, their subsequent counted forward events form another thinned Poisson contribution with exact mean

```math
\boxed{
\mu_{rev}(T)
=K_\leftarrow\int_0^T C_S(u)du.
}
```

Writing

```math
C_S(u)=1-A_S e^{-r_-u}-B_S e^{-r_+u},
```

with

```math
A_S=\frac{r_+-\kappa}{\Delta},
```

```math
B_S=\frac{\kappa-r_-}{\Delta},
```

gives

```math
\boxed{
\mu_{rev}(T)
=K_\leftarrow\left[
T
-\frac{A_S}{r_-}(1-e^{-r_-T})
-\frac{B_S}{r_+}(1-e^{-r_+T})
\right].
}
```

The total reduced-model dark-count mean is

```math
\boxed{
\mu_{dark}(T)
=\mu_{local}(T)+\mu_{rev}(T).
}
```

and therefore

```math
\boxed{
P_{FA}(T)
=1-e^{-\mu_{dark}(T)}.
}
```

The photon detection efficiency remains

```math
\eta_\gamma(T)=C_S(T).
```

This produces a complete gated detector operating curve within the model.

---

# 8. Gated scalability theorem

In the useful high-efficiency finite-window regime

```text
kappa >> gamma,
1/kappa << T << tau_leak,
```

we have

```math
\int_0^T C_S(u)du\simeq T-O(1/\kappa),
```

and the local-dark term remains nonextensive to leading order:

```math
\mu_{local}(T)=O(dT)
```

rather than `O(NdT)`.

But the reverse extractor contributes

```math
\mu_{rev}(T)
\simeq
K_\to e^{-\beta\Delta F_{eff}}T.
```

If useful counted extraction is enhanced by

```math
K_\to(N)=\mathcal C(N)K_\to(1),
```

then holding the reverse contribution to the gated false-count mean fixed requires

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge kT\ln\mathcal C(N).
}
```

Therefore the thermodynamic affinity theorem survives translation into an explicit false-count probability, not merely a rate-coefficient statement.

---

# 9. Coherence-selective detector trilemma

Within the reduced model, scalable operation confronts three independent requirements:

```text
1. preserve coherence long enough that local internal dark generation remains nonextensive in the decision gate;
2. extract the photon-created bright state rapidly enough for high detection efficiency;
3. suppress thermally reversed bright injection from the counted extractor.
```

The corresponding resources are

```text
coherence time / dephasing rate gamma,
forward extraction rate kappa,
effective free-energy affinity Delta F_eff.
```

The main asymptotic conditions are

```math
\boxed{
\kappa\gg\gamma,
}
```

```math
\boxed{
1/\kappa\ll T\ll N(1/\kappa+1/\gamma),
}
```

and, under collective forward enhancement `mathcal C`,

```math
\boxed{
\Delta F_{extra}\ge kT\ln\mathcal C
}
```

for a bounded reverse dark floor.

This is currently the strongest integrated statement of Experiment 09.

---

# 10. What is established and what is not

Established exactly within the reduced model:

```text
- signal and dark collection kernels C_S(t), C_D(t);
- exact finite-time contrast;
- exact gated local-dark Poisson mean;
- exact N cancellation for local dark counts when gamma=0;
- eventual loss of coherence discrimination for every gamma>0;
- exact reverse-injection gated contribution;
- kT ln(mathcal C) affinity requirement for bounded reverse false counts under local detailed balance.
```

Not established:

```text
- universality beyond the specified Markov/coherence model;
- that a real semiconductor supplies the required coherent material manifold;
- that static nonreciprocity cannot evade the pairwise LDB theorem;
- novelty of the combined detector result;
- practical superiority to every conventional area-decoupled detector architecture.
```

---

# 11. Manuscript relevance

This result materially changes the status of Experiment 09.

The Gedanken experiment now maps onto a concrete detection protocol with an exact efficiency/false-count relation. The central candidate contribution is no longer merely

```text
coherent state vs incoherent mixture.
```

It is

> a gated photodetection theory in which coherent optical preparation converts extensive independent internal dark generation into a nonextensive accepted count process over a finite coherence window, together with exact dephasing leakage and a logarithmic thermodynamic-affinity cost for collectively enhanced reversible extraction.

The next gate is closest-prior-art/significance review of this complete statement. If that survives, manuscript drafting is justified.
