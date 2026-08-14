# Experiment 09 — General passive-extraction affinity bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT UNDER LOCAL-DETAILED-BALANCE ASSUMPTIONS / ONE-PORT ASSUMPTION REMOVED / NOVELTY NOT ESTABLISHED

## Question

The previous reduced model gave a conditional result

```math
\Delta F_{extra}=kT\ln N
```

when a collectively enhanced bright optical mode with linewidth `Gamma=N gamma_o` was critically coupled to one passive counted extractor.

The question here is whether this logarithmic free-energy cost is an artifact of the one-port critical-coupling model.

It is not.

The correct invariant is not emitter number `N` itself, but the enhancement of the useful forward counted-conversion rate.

---

# 1. Arbitrary parallel passive extraction channels

Let a bright excitation `B` be converted into counted lower states/reservoir outcomes through channels `a=1,...,m`.

Write the forward rate coefficient of channel `a` as

```math
\kappa_a>0.
```

Assume each channel is stationary and thermodynamically reversible in the local-detailed-balance sense, with free-energy drop `Delta F_a` in the counted forward direction:

```math
\frac{\bar\kappa_a}{\kappa_a}
=e^{-\beta\Delta F_a},
\qquad
\beta=(kT)^{-1}.
```

Here `bar kappa_a` is the reverse bright-injection rate coefficient associated with the same microscopic channel. `Delta F_a` may include energetic and chemical work terms appropriate to the reservoir model.

Define total forward and reverse coefficients

```math
K_\to=\sum_a\kappa_a,
```

```math
K_\leftarrow=\sum_a\bar\kappa_a
=\sum_a\kappa_a e^{-\beta\Delta F_a}.
```

Introduce the normalized forward weights

```math
p_a=\frac{\kappa_a}{K_\to},
\qquad
\sum_a p_a=1.
```

Then exactly

```math
\boxed{
\frac{K_\leftarrow}{K_\to}
=\sum_a p_a e^{-\beta\Delta F_a}.
}
```

Define an effective affinity/free-energy drop by

```math
\boxed{
\Delta F_{eff}
=-kT\ln\left(\frac{K_\leftarrow}{K_\to}\right).
}
```

Therefore

```math
\boxed{
\Delta F_{eff}
=-kT\ln\left(\sum_a p_a e^{-\beta\Delta F_a}\right).
}
```

This is a log-sum-exp free-energy average.

---

# 2. Exact bounds on architectural mixing

Because the exponential is monotone,

```math
\min_a\Delta F_a
\le
\Delta F_{eff}
\le
\max_a\Delta F_a.
```

Thus no passive mixture of channels can produce an effective suppression stronger than its strongest microscopic affinity.

Jensen's inequality gives the stronger mean-affinity statement

```math
\sum_a p_a e^{-\beta\Delta F_a}
\ge
\exp\left[-\beta\sum_a p_a\Delta F_a\right],
```

hence

```math
\boxed{
\Delta F_{eff}
\le
\sum_a p_a\Delta F_a.
}
```

Therefore affinity heterogeneity does not help. At fixed forward-rate-weighted mean free-energy drop, spreading the channels over unequal `Delta F_a` can only increase the reverse coefficient relative to the uniform-affinity case.

This removes a possible architectural escape based on combining many weakly reversible pathways.

---

# 3. Collective enhancement theorem

Consider a sequence of detector architectures indexed by a scale parameter `N` or any other collective resource.

Let the useful forward counted-extraction coefficient satisfy

```math
K_\to(N)=\mathcal C(N)K_\to(1),
```

where

```math
\mathcal C(N)>1
```

is the actual collective enhancement factor.

The reverse coefficient is

```math
K_\leftarrow(N)
=K_\to(N)e^{-\beta\Delta F_{eff}(N)}.
```

Suppose the design goal is to prevent the reverse bright-aligned dark floor from growing, e.g.

```math
K_\leftarrow(N)
\le
K_\leftarrow(1).
```

Then necessarily

```math
\mathcal C(N)
K_\to(1)e^{-\beta\Delta F_{eff}(N)}
\le
K_\to(1)e^{-\beta\Delta F_{eff}(1)}.
```

Therefore

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge
kT\ln\mathcal C(N).
}
```

This is the generalized affinity bound.

The earlier `kT ln N` law is the special case

```math
\mathcal C(N)=N.
```

More generally, if

```math
K_\to(N)\propto N^\alpha,
```

then

```math
\boxed{
\Delta F_{eff}(N)
\gtrsim
\alpha kT\ln N+const.
}
```

for a bounded reverse floor.

The theorem therefore depends on the actual collective rate enhancement, not on a particular Dicke model or on emitter count by itself.

---

# 4. Equivalent lower bound when microscopic affinities are bounded

If every available passive channel satisfies

```math
\Delta F_a\le\Delta F_{max},
```

then

```math
K_\leftarrow
=\sum_a\kappa_a e^{-\beta\Delta F_a}
\ge
e^{-\beta\Delta F_{max}}\sum_a\kappa_a.
```

Thus

```math
\boxed{
K_\leftarrow
\ge
K_\to e^{-\beta\Delta F_{max}}.
}
```

Consequently, if `K_to` grows by `mathcal C` while `Delta F_max` remains fixed, the reverse coefficient must grow by at least the same factor `mathcal C`.

This is a useful no-go form because it makes no assumption about the distribution of microscopic channels.

---

# 5. Hidden passive intermediate states do not supply equilibrium rectification

A second apparent escape is to insert an arbitrary network of passive intermediate states between the bright excitation and the counted sink.

For a finite continuous-time Markov network satisfying equilibrium detailed balance with stationary weights `pi_i`, the generator can be symmetrized by the Gibbs weights. In one common convention,

```math
\mathcal L
=-\Pi^{1/2}Q\Pi^{-1/2},
\qquad
\Pi=diag(\pi_i),
```

and detailed balance makes `mathcal L` symmetric.

Partition states into visible boundary states `O` and hidden internal states `H`:

```math
\mathcal L=
\begin{pmatrix}
L_{OO} & L_{OH}\\
L_{HO} & L_{HH}
\end{pmatrix}.
```

Eliminating the hidden states in the quasistatic / Dirichlet-to-Neumann sense gives the Schur complement

```math
\boxed{
L_{eff}
=L_{OO}-L_{OH}L_{HH}^{-1}L_{HO}.
}
```

Because a Schur complement of a symmetric matrix is symmetric,

```math
L_{eff}=L_{eff}^{T}.
```

Transforming back to the boundary generator therefore preserves detailed balance:

```math
\boxed{
\pi_i K_{i\to j}^{eff}
=\pi_j K_{j\to i}^{eff}.
}
```

Hence arbitrary passive equilibrium intermediate-state complexity cannot create an effective one-way counted transition between the boundary states.

It can alter the absolute kinetics, introduce bottlenecks, and generate memory outside the Markov reduction, but it cannot produce equilibrium forward/reverse asymmetry beyond the free-energy ratio of the boundary problem.

This is a structural closure of the simplest hidden-network escape.

---

# 6. Relation to the coherence-selective Gedanken detector

The optical bright state is

```math
|B\rangle
=\frac{1}{\sqrt{g^\dagger g}}
\sum_j g_j|j\rangle.
```

For dark-generation covariance `D`, the instantaneous bright-aligned internal dark-generation rate is

```math
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
```

For independent identical local dark channels,

```math
D=dI,
```

so

```math
\boxed{\Gamma_D^B=d}
```

independent of the number of participating sites, even though the total raw local dark-generation rate grows as `Nd`.

This is the coherence-selection resource.

Now suppose the useful counted extraction of the same bright mode is collectively enhanced by

```math
\mathcal C.
```

If that counted extractor is stationary and locally detailed-balanced, the generalized result above says that keeping its reverse bright-injection floor fixed requires

```math
\boxed{
\Delta F_{extra}\ge kT\ln\mathcal C.
}
```

Therefore the scalable detector problem contains two distinct sectors:

```text
local incoherent internal dark generation:
    coherence projection can prevent the accepted rate from scaling with system size;

thermally reversed counted extraction:
    any collectively enhanced locally-detailed-balanced forward rate carries the same enhancement into its reverse coefficient unless additional free-energy bias is supplied.
```

The second sector is not removed by using more passive extraction pathways or passive hidden-state networks.

---

# 7. Scalability trilemma

Under the stated assumptions, the following three design requirements cannot all remain `N`-independent:

```text
A. collectively increasing useful counted extraction K_to;
B. bounded effective thermodynamic affinity Delta F_eff;
C. bounded thermally reversed bright-aligned dark coefficient K_leftarrow.
```

At least one must give.

Quantitatively,

```math
\boxed{
K_\leftarrow
=K_\to e^{-\beta\Delta F_{eff}}.
}
```

Thus a factor `mathcal C` increase in `K_to` demands either:

```text
reverse dark coefficient increases by mathcal C,
```

or

```text
effective affinity increases by at least kT ln(mathcal C),
```

or the architecture leaves the local-detailed-balance/passive-stationary class.

This is the sharper replacement for the earlier one-port critical-coupling statement.

---

# 8. Numerical scale only

At `T=77 K`, the extra affinity corresponding to `mathcal C=N` is approximately

```text
N=10:    15.28 meV
N=100:   30.56 meV
N=1000:  45.84 meV
```

At `300 K`, `N=1000` gives about `178.6 meV`.

These are thermodynamic scale illustrations only, not proposed device specifications.

---

# 9. Adversarial escape audit

## Escape A — many parallel passive pathways

**Fails.** They collapse to `Delta F_eff` through the log-sum-exp identity.

## Escape B — heterogeneous affinities

**Fails as an advantage.** At fixed forward-weighted mean affinity, Jensen's inequality shows heterogeneity worsens reverse suppression.

## Escape C — arbitrary passive equilibrium intermediate states

**Fails in the reversible Markov reduction.** Schur-complement elimination preserves detailed balance.

## Escape D — static nonreciprocity / broken microscopic time reversal

**Not covered by the pairwise local-detailed-balance proof.** Nonreciprocal many-body thermal systems can support persistent equilibrium currents and directional emissivity/absorptivity differences. However, global equilibrium remains constrained by fluctuation-dissipation / second-law conservation, so directional suppression need not imply elimination of the total thermal return channel. This must be treated as a separate escape class rather than silently declared impossible.

## Escape E — time modulation, active gain, maintained chemical bias, driven reservoirs

**Outside the theorem by construction.** These supply nonequilibrium work/free energy and are precisely the resources that can break the stationary passive rate relation.

## Escape F — non-Markovian transient storage

**Not ruled out by the effective-rate theorem.** It may delay reverse injection rather than reduce the long-time thermodynamic return. This is analogous to the already-derived finite-window dephasing resource and requires a separate time-domain bound.

---

# 10. Prior-art position

The ingredients are individually established:

- local detailed balance / KMS thermalization;
- reversible Markov networks and coarse graining;
- collective superradiant/subradiant light-matter coupling;
- collective electronic transport in quantum infrared detectors;
- nonreciprocal thermal radiation and persistent equilibrium heat currents.

Relevant primary sources screened in this step include:

1. Falasco and Esposito, *Phys. Rev. E* **103**, 042114 (2021), local detailed balance across scales, DOI `10.1103/PhysRevE.103.042114`.
2. Ramezani et al., *Phys. Rev. E* **98**, 052104 (2018), quantum detailed balance and thermalizing dynamics, DOI `10.1103/PhysRevE.98.052104`.
3. Ding and Xing, *Phys. Rev. Research* **5**, 013193 (2023), coarse graining with preservation of detailed balance, DOI `10.1103/PhysRevResearch.5.013193`.
4. Kloc et al., *Phys. Rev. Applied* **16**, 044061 (2021), collectively enhanced reservoir-coupled transport with current/noise/entropy-production scaling, DOI `10.1103/PhysRevApplied.16.044061`.
5. Zhu, Guo, and Fan, *Phys. Rev. B* **97**, 094302 (2018), nonreciprocal many-body radiative heat transfer and persistent equilibrium currents, DOI `10.1103/PhysRevB.97.094302`.
6. Guo and Fan, *Phys. Rev. B* **102**, 085401 (2020), second-law constraints on reciprocal and nonreciprocal many-body radiative heat transfer, DOI `10.1103/PhysRevB.102.085401`.
7. the 2023 collective quantum-infrared-detector transport work, *Nature Communications* **14**, 3914, DOI `10.1038/s41467-023-39594-z`.

No source in this focused audit was found to state the complete detector-specific chain

```text
coherent bright-state selection suppresses independent internal dark scaling
+
collective counted extraction enhancement mathcal C
+
local detailed balance

-> required additional affinity >= kT ln mathcal C for a bounded reverse bright dark floor.
```

That absence is not proof of novelty.

---

# 11. Current interpretation

The useful paper-level candidate is becoming narrower and stronger:

> Coherence can make photon-created and internally generated excitations distinguishable even when all microscopic populations are identical. For local incoherent dark generation, bright projection prevents accepted dark generation from scaling with the number of participating sites. But a collectively enhanced stationary counted extractor cannot preserve that scaling advantage for free: under local detailed balance, a collective forward-rate enhancement `mathcal C` requires at least `kT ln mathcal C` additional effective free-energy bias to hold the thermally reversed bright-injection floor fixed.

This combines a quantum-state geometry result, a finite-time decoherence result, and a thermodynamic scalability bound.

It is not yet authorized as a novelty claim.

---

# 12. Next question

The passive-equilibrium / local-detailed-balance escape is now substantially closed.

The next high-value task is **not** another device embellishment. It is to determine whether the combined Experiment-09 result is already coherent enough for a paper-level contribution after the closest literature is attacked specifically on this combined claim.

The immediate next work should therefore be:

1. targeted primary-literature search for detector proposals/theorems using coherent bright-state projection specifically to reject incoherent internal dark generation;
2. search for an existing collective-rate versus reverse-noise/free-energy scaling theorem that already implies the complete `kT ln mathcal C` detector statement;
3. if no direct stronger result is found, construct a manuscript architecture and use a hostile referee pass to determine whether the synthesis is significant enough to publish.
