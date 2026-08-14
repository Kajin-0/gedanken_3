# Extreme hostile referee review — Experiment 09 Paper Rev. 0

**Date:** 2026-08-14  
**Manuscript:** `PAPER_DRAFT_REV0_2026-08-14.md`  
**Review posture:** highly skeptical quantum-photodetector / open-quantum-systems referee  
**Disposition:** **MAJOR REVISION / REV. 0 CENTERPIECE IS TOO CLOSE TO STANDARD MODE PROJECTION / MANUSCRIPT REMAINS ALIVE ONLY BECAUSE THE FINITE-DEPHASING FIXED-EFFICIENCY SCALING TRANSITION IS SUBSTANTIALLY STRONGER**

---

# 1. Referee summary

The manuscript begins from a clear Gedanken construction: a photon prepares one coherent bright superposition across `N` local excited states, while internal local dark generation produces the same local populations incoherently. A bright-selective extractor therefore distinguishes the two event classes even though energy, excitation number, and all local-basis populations are identical.

The paper then claims that independent local dark generation with raw rate `Nd` can produce an accepted gated dark-count mean independent of `N`, that local dephasing makes the benefit finite-time, and that collectively enhanced thermally reversible extraction carries a logarithmic free-energy cost.

In its **Rev. 0 form**, I would not recommend publication. The mathematical centerpiece is not yet sufficiently distinct from standard coherent mode projection, and one part of the detector-count interpretation overstates exactness relative to the stated single-excitation dynamical model.

However, the hostile review generated a stronger result that materially changes the paper's prospects. At fixed required conditional internal collection efficiency `eta`, finite local dephasing produces an asymptotically sharp threshold

```math
\eta_c=\frac{\kappa}{\kappa+\gamma},
```

with three distinct large-`N` regimes:

```math
\boxed{
\begin{array}{c|c|c}
\eta<\eta_c & T_N=O(1) & \mu_N=O(1)\\
\eta=\eta_c & T_N=\Theta(\log N) & \mu_N=\Theta((\log N)^2)\\
\eta>\eta_c & T_N=O(N) & \mu_N=O(N^2).
\end{array}}
```

This is substantially more detector-specific and less reducible to the trivial `1/N` projection observation. I would permit a **major revision centered on this theorem**, followed by another novelty/significance review.

---

# 2. Major objection 1 — the Rev. 0 `N` cancellation is too close to ordinary coherent mode filtering

Rev. 0 emphasizes

```math
D=dI,
```

and a normalized bright vector `B`, giving

```math
\langle B|D|B\rangle=d
```

while

```math
\operatorname{Tr}D=Nd.
```

This is mathematically the same geometry that appears whenever a normalized coherent mode is selected out of `N` independent equal-noise degrees of freedom. A matched spatial mode, array beamformer, or normalized coherent sum accepts the phase-aligned signal while isotropic uncorrelated noise contributes only its variance along that normalized direction.

The manuscript's Hilbert-space language is legitimate, but language does not make the algebra new.

Likewise, in the no-dephasing limit,

```math
C_D(t)=\frac{1}{N}C_S(t)
```

and raw event rate `Nd` immediately give an `O(1)` accepted rate. This is a physically interesting detector interpretation of mode projection, but by itself it is not strong enough for a full theoretical research article.

### Required revision

The paper must demote the `gamma=0` cancellation from **principal theorem** to **limiting corollary / motivating case**.

The manuscript should explicitly acknowledge the coherent-mode-filtering equivalence rather than inviting a referee to discover it and accuse the authors of repackaging elementary projection geometry.

---

# 3. Major objection 2 — the Poisson-thinning result is not exact under the strict single-excitation model as written

Sections 2–3 define a one-excitation manifold. Section 4 then lets each of `N` sites generate a Poisson process at rate `d` and calls the resulting accepted count process exact.

At fixed `d` and increasing `N`, the raw event rate is `Nd`. Unless `dT` is taken to zero sufficiently rapidly with `N`, multiple dark excitations overlap in time. A strict single-excitation Hilbert space cannot represent those overlapping events.

Therefore the statement

> “Independent Poisson thinning therefore gives a Poisson-distributed number of accepted internal dark counts with exact mean ...”

is not exact **from the single-excitation Lindblad model alone**.

This is a real modeling defect, not a semantic complaint.

### Repair

There is a clean solution: state an explicit **independent-particle stochastic lift**.

- The one-body Lindblad equation defines the collection kernel of one generated excitation.
- Dark-generation times are a classical Poisson immigration process.
- Each generated excitation is distinguishable, noninteracting, and carries an independent copy of the one-body dynamics.
- Counted outcomes are independent marks of those events.

Under that lifted model, Poisson thinning is exact by construction.

Alternatively, if no such lift is intended, the paper must restrict the result to the dilute first-order mean-count regime and stop claiming an exact finite-rate Poisson ROC.

The first repair is preferable because it preserves a precise detector task while making the extra assumption explicit.

---

# 4. Major objection 3 — `eta_S` is not end-to-end photon detection efficiency

Rev. 0 writes

```math
\eta_S(T)=C_S(T)
```

and repeatedly calls this photon detection efficiency.

But the model begins **after** a photon has already created the bright material excitation. It does not derive the probability of coupling the incident photon into that excitation, nor reflection, transmission, radiative escape, parasitic absorption, or competing optical modes.

Therefore `C_S(T)` is conditional **internal collection efficiency after bright-state preparation**, not total photon quantum efficiency.

### Required revision

Rename it throughout:

```text
conditional internal collection efficiency
```

or

```math
\eta_{int}(T)=C_S(T).
```

If an absorption/preparation probability `eta_abs` is introduced, the simplest factorized end-to-end model would give

```math
\eta_{det}=\eta_{abs}\eta_{int},
```

but the paper does not need to solve the optical-coupling problem.

This correction materially improves scientific precision.

---

# 5. Major objection 4 — the statement “dephasing restores extensive dark leakage” is incomplete and hides the strongest result

Rev. 0 treats finite dephasing primarily as a failure mechanism:

```text
short gate: useful coherence discrimination;
long gate: all dark excitations eventually leak into the counted sector.
```

That is true but shallow.

The exact solution contains a stronger asymptotic structure. Define

```math
q=\frac{\kappa}{\kappa+\gamma}.
```

At fixed physical time and large `N`, the signal collection saturates at

```math
C_S(t)\to q(1-e^{-(\kappa+\gamma)t}),
```

so `q` is the maximum signal fraction available on the fast timescale.

This creates a task-level threshold when the gate is chosen to achieve a fixed internal efficiency `eta`.

### New main theorem

For the minimal gate `T_N(eta)` satisfying

```math
C_{S,N}(T_N)=\eta,
```

and the accepted local-dark mean at that gate, the large-`N` behavior is:

```math
\boxed{
\eta<q:
\quad
T_N=O(1),
\quad
\mu_N=O(1),
}
```

```math
\boxed{
\eta=q:
\quad
T_N=\Theta(\log N),
\quad
\mu_N=\Theta((\log N)^2),
}
```

```math
\boxed{
\eta>q:
\quad
T_N=O(N),
\quad
\mu_N=O(N^2).
}
```

The explicit coefficients are derived in `EFFICIENCY_SCALABILITY_TRANSITION_2026-08-14.md`.

This is the result that should replace the no-dephasing cancellation as the manuscript's center.

---

# 6. Why the new theorem is scientifically stronger

The static projection result can be summarized as

```text
N incoherent equal-strength noise channels
projected onto one normalized coherent mode
-> O(1) accepted noise.
```

That is familiar geometry.

The fixed-efficiency theorem instead combines

```text
coherent optical state preparation
+ local dephasing into a growing dark manifold
+ bright-only irreversible extraction
+ an operational signal-efficiency target
+ extensive continuous internal dark generation
```

and produces a **change of asymptotic scaling class** at one sharply defined efficiency.

The physical threshold

```math
\boxed{
\eta_c=\frac{\kappa}{\kappa+\gamma}
}
```

has a transparent interpretation: it is the fraction of the initial bright excitation that can be extracted on the fast branch before local dephasing sends amplitude into the dark manifold.

Below that target, the detector can close the gate before slow recycling matters. Above it, the detector must wait `O(N)` for dark-manifold leakage, and the accepted local-dark burden becomes `O(N^2)`.

At the boundary, fast-tail decay and incipient slow recycling balance, yielding the Lambert-W / logarithmic crossover scale.

This is a real dynamical detector theorem rather than a static mode-selection identity.

---

# 7. Major objection 5 — the thermodynamic `kT ln C` result is too generic to be coequal novelty

For locally detailed-balanced channels,

```math
\frac{k_\leftarrow}{k_\to}=e^{-\beta\Delta F},
```

so compensating a forward-rate enhancement `mathcal C` with an extra affinity

```math
kT\ln\mathcal C
```

is algebraically immediate.

The parallel-channel log-sum-exp form is useful and correct under its assumptions, and the hidden-state detailed-balance preservation result is a useful no-go statement for equilibrium Markov reductions. But a knowledgeable thermodynamics referee will not regard the logarithm itself as a major new theorem.

### Required revision

Demote this section to a **secondary scalability constraint / thermodynamic corollary**.

Its purpose is to prevent the paper from falsely implying that coherence gives a free scaling advantage once the counted extractor itself is made collective.

It should not share equal billing in the title or abstract unless a stronger detector-specific thermodynamic result emerges.

Also, the reverse-injection-to-false-count mapping must explicitly state the same independent-event assumptions as the local-dark Poisson lift.

---

# 8. Major objection 6 — closest prior art must be discussed more aggressively

Several primary-source lineages are directly relevant.

### Young, Sarovar, Léonard — quantum photodetector coherence/backaction

*Fundamental Limits to Single-Photon Detection Determined by Quantum Coherence and Backaction*, Phys. Rev. A 97, 033836 (2018), establishes that quantum coherence and amplification backaction determine detector efficiency, dark counts, jitter, and optimal detector design.

The current paper cannot claim that using coherence as a photodetector resource is new.

### Shammah et al. — bright/dark transfer under local dephasing

*Superradiance with local phase-breaking effects*, Phys. Rev. A 96, 023863 (2017), explicitly treats dilute-excitation bright/dark quasiparticles and dephasing-induced intermode scattering.

The current paper cannot claim bright/dark leakage under dephasing as a new open-system mechanism.

### Collective quantum infrared detector

Pisani et al., *Electronic transport driven by collective light-matter coupled states in a quantum device*, Nature Communications 14, 3914 (2023), explicitly connects collective electronic polarization/coherence to an extractor and photocurrent in an infrared detector.

This is the strongest device-physics neighbor and must be treated centrally, not buried as background.

### Dark-state/coherence-enhanced photocells

Fruchtman et al., Phys. Rev. Lett. 117, 203603 (2016), and related coherence-assisted photocell work already use quantum interference and dark states to alter absorption/emission/extraction tradeoffs.

### Current collective scaling literature

Recent 2026 work derives nontrivial finite-size and dephasing scaling regimes in superabsorption / Dicke dynamics, including *Entanglement and dynamical scaling laws in quantum superabsorption* (Phys. Rev. Research 8, 033035 (2026)) and the July 2026 preprint *Scaling theory of decoherence in Dicke superradiance*.

Therefore the paper must not claim that “dephasing causes a collective scaling transition” in broad terms.

### Surviving narrow novelty question

The focused audit has not located the specific photodetector result

```text
fixed required internal collection efficiency eta
+ bright extraction kappa
+ local pure dephasing gamma
+ N independent internal dark-generation sites

-> eta_c=kappa/(kappa+gamma)
-> O(1), logarithmic, and O(N)/O(N^2) gate/dark-count regimes.
```

That is now the correct novelty burden.

---

# 9. Major objection 7 — practical comparator remains ordinary physical-space filtering

Resonant and antenna-coupled infrared detectors can keep a large optical collection area while minimizing electrically active semiconductor area. That established architecture already attacks the same engineering problem: obtain strong optical coupling without paying dark current proportional to optical footprint.

The manuscript's distinction is real but must remain precise:

```text
physical-space filtering:
    reduce or isolate the dark-generating electrical volume;

state-space filtering here:
    retain all N dark-generating sites and raw local generation,
    but accept only one coherent collective direction.
```

This distinction establishes that the models are not mathematically identical. It does **not** establish that the state-space strategy will outperform the geometric one in a real device.

Do not imply practical superiority without a microscopic realization.

---

# 10. Minor but important technical corrections

1. Rev. 0 contains a TeX typo in the definition of `Delta`: `\nrac` must be `\frac`.
2. Distinguish raw generation rate, accepted count mean, and stationary dark current; they are not interchangeable quantities.
3. Same-mode thermal/background photons are not rejected. This limitation belongs in the Abstract or early Discussion, not only deep in the paper.
4. Correlated dark baths can have `D` aligned with the bright vector and eliminate the projection advantage.
5. `N` is an effective number of coherently participating microscopic states, not automatically physical absorber volume. Any later material interpretation must state what controls `N`.
6. The symmetric exactly degenerate manifold is an existence model. Energetic disorder and inhomogeneous coupling are obvious later robustness tests, but they are not required before the revised central theorem is properly framed.
7. Reset/dead-time semantics are absent. That is acceptable for a gated independent-particle model if explicitly stated; do not pretend the paper has solved detector recovery dynamics.

---

# 11. Referee assessment of the new theorem

I independently checked the asymptotic logic behind the three-regime result.

Let

```math
a=\kappa+\gamma,
```

```math
q=\kappa/a,
```

```math
\lambda=\kappa\gamma/a.
```

For fixed `t`,

```math
C_{S,N}(t)\to q(1-e^{-at}),
```

while

```math
N C_{D,N}(t)
\to
q(1-q)at+q^2(1-e^{-at}).
```

For `eta<q`, the gate converges to

```math
T_N\to\frac{-\ln(1-\eta/q)}{a},
```

and the integrated dark burden converges to a finite constant.

For `eta>q`, on `t=Ny`,

```math
C_{S,N}(Ny)\to1-(1-q)e^{-\lambda y},
```

so

```math
\frac{T_N}{N}
\to
\frac1\lambda\ln\frac{1-q}{1-\eta}.
```

The dark kernel tends to `1-e^{-lambda y}`, yielding an `N^2` integrated burden.

At `eta=q`, balancing the fast exponential tail with the `t/N` slow leakage yields

```math
aT_N
\sim
W\left(\frac{N}{(1-q)^2}\right),
```

and therefore `T_N=Theta(log N)` and `mu_N=Theta((log N)^2)`.

I find no algebraic contradiction in this asymptotic partition.

---

# 12. Recommended Rev. 1 scientific architecture

The paper should be rewritten, not merely patched.

### Results hierarchy

1. **Minimal coherent/incoherent event construction** — one page, explicitly old state-discrimination geometry.
2. **Exact one-body extraction/dephasing dynamics** — define the detector kernel.
3. **Independent-particle stochastic lift** — make the counting model mathematically honest.
4. **Fixed-efficiency scalability theorem** — main result and main figure.
5. **No-dephasing exact `N` cancellation** — corollary.
6. **General covariance / correlated-dark limitation** — short generalization.
7. **Thermodynamic reverse-extraction constraint** — secondary discussion/corollary.

### Recommended title

> **Efficiency-controlled dark-count scaling transition in a coherence-selective photodetector**

A slightly less aggressive alternative:

> **Coherence-selective photodetection across an efficiency-driven dark-count scaling boundary**

Do not put “quantum advantage,” “fundamental,” or “novel” in the title.

---

# 13. Publication-level significance judgment

### Rev. 0 as written

```text
REJECT / TOO CLOSE TO STANDARD MODE PROJECTION + MODEL-EXACTNESS DEFECT.
```

### After re-centering on the new theorem

```text
MAJOR REVISION WORTH REVIEWING.
```

The new result is compact, exact/asymptotic within a clearly stated model, detector-operational, and produces a surprising scaling reversal:

```text
slightly below eta_c -> bounded dark burden;
slightly above eta_c -> quadratic dark burden.
```

That qualitative jump is stronger than a pedagogical synthesis.

The remaining publication risk is **novelty/significance**, not an identified fatal mathematical contradiction.

A full article may still be ambitious because the device realization is abstract. A concise theoretical photodetection / quantum-device paper is currently more defensible than a broad general photodetector manifesto.

---

# 14. Required next action

**Revise the actual manuscript to Rev. 1 around `EFFICIENCY_SCALABILITY_TRANSITION_2026-08-14.md`.**

Do not open a new experiment.

After Rev. 1:

1. run another hostile review focused only on the new fixed-efficiency theorem and its nearest scaling literature;
2. perform a targeted citation audit of current 2025–2026 Dicke/dephasing scaling work;
3. only then decide whether figures and journal-format preparation are justified.

Current overall disposition:

```text
REV. 0: FAILS AS WRITTEN
EXPERIMENT 09 PAPER PATH: REMAINS ACTIVE
NEW CENTRAL THEOREM: SURVIVES CURRENT HOSTILE CHECK
NOVELTY: NOT ESTABLISHED
NEXT: REV. 1, NOT EXPERIMENT 10
```
