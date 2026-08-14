# Extreme hostile referee review — Experiment 09 Paper Rev. 2

**Date:** 2026-08-14  
**Manuscript:** `PAPER_DRAFT_REV2_2026-08-14.md`  
**Disposition:** **MAJOR REVISION BUT PAPER PATH SURVIVES / GENERAL RATE-SCALING CLASSIFICATION IS CORRECT WITHIN MODEL / CLAIM SHOULD BE COMPRESSED AROUND THE SCALABLE-EFFICIENCY CEILING AND THE PENALTY FOR DARK-TO-BRIGHT RECYCLING**

---

# 1. Overall assessment

Rev. 2 successfully repairs the most important defect of Rev. 1: it no longer presents the fixed-`kappa` `O(N^2)` result as a universal scalability law. Allowing

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta
```

produces a coherent asymptotic classification, and the fixed-rate result appears correctly as the slice `alpha=beta=0`.

The new supporting results also improve physical discipline:

- bounded per-site counted coupling gives `alpha<=1`;
- the efficiency-selected reverse-injection burden is branch dependent rather than universally proportional to the forward collective rate;
- the old blanket `kT ln mathcal C` interpretation has been corrected.

I find no fatal algebraic contradiction in the current phase-diagram formulas.

I would still request major revision before submission because the manuscript risks overselling a mathematically straightforward scaling classification as a new “phase diagram,” and because the strongest detector-facing result is simpler than the current presentation.

---

# 2. Closest prior art is now very clear

The most dangerous detector paper is Young, Sarovar, and Leonard, ACS Photonics 7, 821–830 (2020).

Their work already proposes detectors composed of subwavelength elements interacting collectively with the photon field and explicitly targets high efficiency, low dark counts, low jitter, and high count rate. More importantly, their ideal-efficiency conditions include the requirement that relaxation processes **not couple dark states back into the optically active manifold**.

This is extremely close to the physical mechanism studied here.

The present work must therefore be framed as:

> Given a collective coherent detector of the Young–Sarovar–Leonard type, what happens to accepted internally generated events when the dark-to-bright isolation condition is violated by local dephasing, the detector gate is fixed by a required collection efficiency, and the useful and decohering rates scale with system size?

That is a legitimate narrower problem.

The paper must not imply that it discovers the need to isolate dark states from the optically active manifold.

---

# 3. Bassler et al. owns the broad scaling language

The 2026 Dicke-superradiance scaling paper of Bassler, Lyne, and Cuerda explicitly develops scaling regimes from competition between collective dynamics and local decoherence and identifies transient boundaries.

Therefore the phrase

```text
new rate-scaling phase diagram
```

is vulnerable unless immediately qualified as a **detector-operational accepted-dark scaling classification**.

I recommend avoiding the word “phase” in the title. “Scaling laws” or “scalability boundary” is safer and more precise.

The distinction is not that Experiment 09 also has exponents. The distinction is that its gate is chosen by a detector efficiency target and the dependent observable is the total accepted internally generated event burden during that gate.

---

# 4. The five-row table is useful but not the cleanest headline

The complete classification

```math
\begin{array}{c|c|c|c}
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}
\end{array}
```

is mathematically useful.

But a detector reader can understand the scientific content more directly through the bounded-coupling corollary.

Under the physically motivated resource assumptions

```math
0\le\alpha\le1
```

and bounded per-site counted coupling, define the supremum fixed efficiency that can retain bounded accepted local-dark burden:

```math
\eta_{sc}
=\sup\{\eta:\mu_N(\eta)=O(1)\}.
```

Then

```math
\boxed{
\eta_{sc}
=
\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}}
```

This is the best detector-facing summary currently in the project.

The full table should then explain how the detector approaches or fails beyond that ceiling.

---

# 5. Bounded-per-site extraction is an important physical constraint

The extraction-rate bound is elementary but useful:

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|,
```

```math
K_{jj}\le\kappa_{loc}
```

implies

```math
\kappa_B\le\lambda_{max}(K)\le\operatorname{Tr}K\le N\kappa_{loc}.
```

Thus `alpha<=1` in the linear single-excitation resource class.

This eliminates the otherwise artificial mathematical escape in which the detector sits on a slow-recycling branch but makes `kappa_N` grow as `N^2` or faster to keep the integrated dark burden bounded.

The resulting no-go statement is strong and should be stated explicitly:

> **With bounded counted coupling per microscopic state, any fixed operating point that lies strictly on the slow-recycling side incurs at least an `O(N)` accepted local-dark burden.**

This is more physically meaningful than listing the formal `alpha>=2` escape.

---

# 6. The thermodynamic correction is scientifically important

The project correctly discovered that the earlier fixed-gate `kT ln mathcal C` interpretation was not the right operational detector statement.

For an efficiency-selected gate and a thermally reversible bright extractor,

```math
\bar\kappa_N=\kappa_Ne^{-\beta\Delta F_N},
```

but

```math
\mu_{rev,N}
=\bar\kappa_N\int_0^{T_N}C_{S,N}(u)du.
```

On a fast branch the increased reverse rate is canceled by the shortened gate, leaving `O(1)` reverse burden at fixed affinity. The balanced boundary gives `O(ln N)`, and a strict slow branch gives `O(N)`.

This is a substantially better detector statement than the earlier rate-only argument.

I recommend including only this corrected gated result in the manuscript. Move the old `kT ln mathcal C` coefficient theorem to derivation history or an appendix.

---

# 7. Is the mathematics too obvious for publication?

This is now the central editorial question.

Once the exact two-rate one-body kernel is written down, much of the asymptotic phase table follows by comparing

```math
q_N=\frac{\kappa_N}{\kappa_N+\gamma_N}
```

and

```math
r_-\sim\frac{\lambda_N}{N}.
```

A skeptical mathematical physicist may call the exponents straightforward asymptotic bookkeeping.

The paper therefore cannot rely on mathematical difficulty for significance.

Its value must come from the detector formulation:

1. signal and local dark events have identical populations and differ only by coherence;
2. the gate is selected by a specified detector efficiency rather than chosen arbitrarily;
3. raw internal event generation remains extensive;
4. the accepted dark burden has a sharp scalable-efficiency ceiling under a bounded microscopic coupling resource;
5. violating the dark-to-bright isolation condition identified in existing coherent-detector theory produces a quantified system-size penalty.

That synthesis is potentially publishable as a concise theoretical detector paper even if none of the algebra individually is deep.

---

# 8. The independent-particle lift remains the largest physical abstraction

The asymptotic burden assumes `N` local Poisson sources whose generated excitations are noninteracting distinguishable copies of the one-body kernel.

This is mathematically clear, but the paper should not casually identify `N` with an arbitrary number of two-level emitters at finite excitation density. In a true many-excitation collective system, saturation and collective extraction can change the count process.

The clean interpretation is:

> an extensive low-density kinetic limit in which the number of available microscopic generation sites grows while occupation probability per site remains small and generated excitations propagate independently.

State this in the main Model section, not only in Limitations.

---

# 9. Same-mode optical background must remain outside the claim

The mechanism does not reject background photons entering the accepted optical mode. Those photons prepare the same bright excitation as the signal.

This is not a minor caveat. It means the paper is about **internally generated local dark events**, not general background-limited photodetection.

The title and abstract should use “internal dark events/counts” consistently.

---

# 10. Recommended Rev. 3 structure

I recommend one more scientific rewrite before figures.

### Proposed title

> **Scalable internal-dark-count limits in a coherence-selective photodetector**

or

> **Efficiency limits for scalable dark-count suppression in a coherence-selective photodetector**

### Results order

1. closest established coherent-detector architecture and the dark-to-bright isolation condition;
2. minimal bright/local-dark Gedanken construction;
3. exact extraction/dephasing kernel;
4. independent-particle local-generation lift;
5. scalable-efficiency ceiling under bounded local coupling — headline theorem;
6. full `alpha,beta,eta` asymptotic table — supporting theorem;
7. gated reverse-injection floor — supporting thermodynamic result;
8. fixed-rate and no-dephasing limits as corollaries.

This is shorter and more defensible than presenting a generic phase-diagram paper.

---

# 11. Publication format

At the current level I would favor a **concise theoretical research article / letter-length paper** rather than a broad full-length manifesto about photodetector limits.

The core is now coherent enough for a paper:

```text
established coherent detector architecture
+ quantified violation of its dark-state isolation condition
+ efficiency-selected measurement protocol
+ extensive internal local-event source
+ scaling/no-go theorem under bounded microscopic coupling.
```

The main remaining risk is novelty/significance relative to the Young detector program and current collective-decoherence scaling literature, not an identified internal inconsistency.

---

# 12. Referee disposition

```text
REV. 2 ALGEBRA: PASS AT CURRENT CHECK LEVEL
GENERAL RATE-SCALING CLASSIFICATION: PASS WITHIN MODEL
BOUNDED-LOCAL-COUPLING COROLLARY: STRONG / SHOULD BE PROMOTED
GATED REVERSE-INJECTION CORRECTION: PASS / REPLACES OLD INTERPRETATION
YOUNG 2020 PRIOR ART: MUST BE CENTRAL
BASSLER 2026 SCALING PRIOR ART: MUST BE CENTRAL
INDEPENDENT-PARTICLE LIFT: ACCEPTABLE BUT ABSTRACT
NOVELTY: NOT ESTABLISHED
PAPER PATH: CONTINUE
RECOMMENDED FORMAT: CONCISE THEORY PAPER
```

## Next action

Build Rev. 3 around the scalable-efficiency ceiling and bounded-coupling no-go, then generate figures only if that compressed manuscript still reads as a distinct research result.
