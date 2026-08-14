# Extreme hostile referee review — Experiment 09 Paper Rev. 1

**Date:** 2026-08-14  
**Manuscript:** `PAPER_DRAFT_REV1_2026-08-14.md`  
**Disposition:** **MAJOR REVISION / CENTRAL THREE-REGIME THEOREM IS MATHEMATICALLY COHERENT, BUT FIXED-RATE SCALING CLASS IS TOO SPECIAL TO PRESENT AS THE COMPLETE SCALABILITY STORY / CLOSEST COHERENT-DETECTOR PRIOR ART MUST BE DEEPENED**

---

# 1. Executive assessment

Rev. 1 is a major scientific improvement over Rev. 0.

The paper now correctly:

- admits that static `1/N` bright projection is standard coherent-mode/state-verification geometry;
- repairs the finite-rate count process with an explicit independent-particle stochastic lift;
- calls `C_S` conditional internal collection rather than end-to-end photon efficiency;
- demotes the `kT ln mathcal C` local-detailed-balance relation;
- centers the paper on a fixed-efficiency large-`N` detector theorem.

The central theorem

```math
\eta_c=\frac{\kappa}{\kappa+\gamma}
```

with

```math
\eta<\eta_c:
\quad T_N=O(1),\quad\mu_N=O(1),
```

```math
\eta=\eta_c:
\quad T_N=\Theta(\ln N),\quad\mu_N=\Theta((\ln N)^2),
```

```math
\eta>\eta_c:
\quad T_N=O(N),\quad\mu_N=O(N^2)
```

survives my current algebraic check for fixed positive `kappa`, `gamma`, and per-site dark rate `d`.

I do not find a fatal mathematical contradiction in this theorem.

I still would not recommend submission yet. Two problems now dominate:

1. the nearest coherent-detector prior art is closer than the manuscript currently presents;
2. the scaling result fixes `kappa` and `gamma` while changing `N`, even though collective detector architectures can themselves have `N`-dependent useful rates.

The second issue is especially important because it may change the apparent `O(N^2)` catastrophe into an entirely different scaling class.

---

# 2. Strongest prior-art threat — Young, Sarovar, Léonard 2020

The manuscript cites Young et al. 2018, but the more dangerous comparator is:

> S. M. Young, M. Sarovar, and F. Léonard, “Design of High-Performance Photon-Number-Resolving Photodetectors Based on Coherently Interacting Nanoscale Elements,” ACS Photonics 7, 821–830 (2020), DOI `10.1021/acsphotonics.9b01754`.

This paper explicitly proposes detector elements within a wavelength that interact **collectively and coherently** with the photon field and seeks simultaneous high efficiency, low jitter, low dark counts, high count rate, and photon-number resolution.

Its theory includes:

```text
coherently interacting detector elements;
optically active and dark internal states;
incoherent relaxation/transduction;
conditions under which relaxation does or does not feed optically active manifolds;
detector efficiency and intrinsic dark-count metrics;
collective-coupling scaling with number of elements.
```

One particularly relevant statement is that unit efficiency in their broadened detector model requires, among other things, that relaxation processes do not couple dark states back into the optically active manifold. This is conceptually adjacent to the present paper's central concern: what happens when local dephasing *does* couple population between bright and dark sectors.

Therefore the current manuscript must not imply that

```text
coherently interacting nanoscale detector elements
+ dark internal states
+ collective optical coupling
+ high efficiency / low dark counts
```

is a new detector concept.

### What remains distinct

The screened Young et al. paper does not appear to derive the current fixed-efficiency asymptotic theorem for continuous local internal dark generation:

```text
eta_c=kappa/(kappa+gamma)
-> O(1), logarithmic, O(N^2) accepted-dark regimes.
```

But this distinction must be stated explicitly in the Introduction and closest-prior-art discussion.

---

# 3. Major scaling objection — why is kappa fixed as N grows?

Rev. 1 varies `N` at fixed

```math
\kappa,\quad\gamma,\quad d.
```

This is a legitimate asymptotic class, but the manuscript currently lets it read like *the* scalability result for a coherence-selective detector.

That is too broad.

In collective light-matter systems, useful bright-state rates often depend strongly on the number of participating elements. Indeed, the closest detector and superradiance literature explicitly contains collective rate enhancement.

If

```math
\kappa=\kappa_N
```

increases with `N`, then

```math
q_N=\frac{\kappa_N}{\kappa_N+\gamma}
```

can approach unity. For every fixed target `eta<1`, the detector may then eventually become subcritical, eliminating the fixed-`kappa` supercritical branch.

Thus the dramatic

```math
\mu_N=O(N^2)
```

law is not universal. It belongs to one scaling class.

This is not a fatal flaw—the paper can become stronger by treating the rate scaling explicitly.

### Required next analysis

At minimum, analyze

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta
```

or the simpler `gamma=constant` version.

The fixed-rate theorem is then the line `alpha=beta=0` in a larger scaling phase diagram.

---

# 4. Preliminary general-rate consequence

The fixed-rate equations already suggest the following rate-scaling structure.

Assume first

```math
\gamma_N=\gamma_0>0,
```

and

```math
\kappa_N=\kappa_0N^\alpha.
```

## alpha > 0

Then

```math
q_N\to1.
```

Every fixed target `eta<1` eventually lies below the fast-branch ceiling. The minimum gate scales as

```math
T_N\sim\frac{-\ln(1-\eta)}{\kappa_0N^\alpha},
```

while direct local-dark acceptance gives

```math
\mu_N\sim
\frac{d}{\kappa_0N^\alpha}
[-\ln(1-\eta)-\eta].
```

Thus collectively enhanced extraction can make the accepted local-dark burden **decrease** with size in the ideal noninteracting model.

## alpha = 0

This is exactly Rev. 1's three-regime theorem.

## alpha < 0

Then `q_N->0`, so every fixed target `eta>0` is eventually supercritical. The slow return scale is set by `kappa_N/N`, giving

```math
T_N=O(N^{1-\alpha}),
```

and

```math
\mu_N=O(N^{2-\alpha}).
```

This preliminary extension already shows that the system-size scaling of the useful extraction rate is an essential axis of the detector theorem.

A complete derivation should replace this referee sketch before Rev. 2.

---

# 5. Independent-particle lift — acceptable as a theorem class, but physical scope must remain narrow

Rev. 1 repairs the logical inconsistency in Rev. 0 by declaring a Poisson immigration model of distinguishable, noninteracting excitations, each carrying an independent one-body quantum kernel.

Mathematically this is sufficient.

Physically, a referee will still ask what kind of material excitation satisfies this lift as `N->infinity` at fixed per-site generation rate.

The defensible interpretation is an extensive low-density kinetic limit:

```text
number of sites grows;
mean excitation density per site remains small;
interactions, Pauli blocking, heating, and extractor saturation are neglected;
multiple particles can coexist but do not modify each other's one-body dynamics.
```

The manuscript should state this interpretation directly.

If the intended microscopic states are strict two-level sites with collective many-excitation dynamics, then the independent-copy lift is no longer exact and a separate many-body model would be needed.

Do not blur these two physical realizations.

---

# 6. Critical Lambert-W branch — mathematically plausible, but the coefficient needs a proper asymptotic statement

The claimed leading balance

```math
aT_N(q)
\sim W\left(\frac{N}{(1-q)^2}\right)
```

is consistent with the large-`N` expansion.

However finite-`N` convergence is slow because the next correction to the slow-mode amplitude contributes at the same level as an `O(1)` shift inside the logarithm.

For manuscript purposes, the robust theorem is

```math
T_N(q)=\Theta(\ln N),
```

```math
\mu_N(q)=\Theta((\ln N)^2).
```

The Lambert-W form may remain as a leading asymptotic provided the paper says clearly that it controls the leading logarithmic scale, not a precision finite-`N` approximation.

If the paper wants to display the coefficient as a theorem, derive the next amplitude term and provide a controlled remainder.

---

# 7. Detector significance — fixed-efficiency formulation is the right operational variable

One of Rev. 1's strongest conceptual choices is to select the gate by required internal collection efficiency rather than by arbitrary time.

This makes the scaling result genuinely detector-operational:

```text
How long must I wait to collect the specified fraction of a photon-created excitation,
and what internal-dark burden do I incur by waiting that long?
```

This is more compelling than simply plotting bright/dark populations versus time.

A useful corollary would invert the result:

> At fixed accepted-dark budget, what is the asymptotic maximum internal collection efficiency?

For the fixed-rate class and any finite `O(1)` dark budget, the asymptotically scalable operating point must remain below `q`. Such a statement could strengthen the practical detector interpretation without adding new physics.

This is optional, not a submission blocker.

---

# 8. Same-mode photon background remains an unavoidable limitation

The paper correctly states that same-mode thermal/background photons prepare the same bright state and cannot be rejected.

This should be made impossible to miss because otherwise “dark-count suppression” can be misread as general background-noise suppression.

The title says **dark-count**, not background rejection, which is appropriate.

The Abstract should ideally say “internally generated local dark events” rather than simply “dark counts” in its strongest sentence.

---

# 9. Thermodynamic section — keep it secondary

The recent paper

> E. Schwarzhans et al., “Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition,” PRX Quantum 7, 033001 (2026)

already gives a broad detector-level framework relating thermodynamic resources to detection efficiency, dark counts, jitter, and dead time.

This makes any attempt to elevate the `kT ln mathcal C` relation especially vulnerable.

Rev. 1's current placement is appropriate: a secondary caveat saying that collective useful-rate enhancement cannot be presumed thermodynamically free.

Do not expand this section unless it produces a result specifically tied to the new rate-scaling phase diagram.

---

# 10. Current novelty assessment

I see no direct primary-source statement of the exact Rev. 1 fixed-rate detector theorem.

But the novelty neighborhood is crowded:

```text
coherent quantum photodetector design: Young et al. 2018, 2020;
collective bright/dark dephasing: Shammah et al. 2017 and successors;
coherence/dark-state photocells: established;
collective quantum IR extractor transport: Pisani et al. 2023;
large-N decoherence scaling transitions: active 2026 Dicke literature;
quantum-detector efficiency/dark-count thermodynamics: Schwarzhans et al. 2026.
```

Therefore the paper's defensible possible contribution is narrow:

> a fixed-efficiency internal-dark-count scalability theorem for a bright-selective detector with local dephasing and extensive local dark generation, together with its extension across system-size-dependent useful extraction rates.

That is enough to justify continuation, not priority language.

---

# 11. Referee disposition

```text
REV. 1 MATHEMATICAL CORE: PASS IN FIXED-RATE CLASS
REV. 1 CLAIM SCOPE: MUCH IMPROVED
POISSON MODEL CONSISTENCY: PASS AFTER EXPLICIT LIFT
CLOSEST PRIOR ART: NEEDS YOUNG 2020 ADDED PROMINENTLY
FIXED-kappa UNIVERSALITY: FAIL / MUST BE NARROWED OR GENERALIZED
CRITICAL LAMBERT-W PRECISION: NEEDS CAUTIOUS WORDING OR TIGHTER PROOF
THERMODYNAMIC SECTION: SUPPORTING ONLY
NOVELTY: NOT ESTABLISHED
PAPER PATH: CONTINUE
```

## Required next action

Do not open Experiment 10.

Derive the **system-size-dependent extraction/dephasing scaling extension**. If it yields a clean phase diagram, rebuild Rev. 1 into Rev. 2 around the broader theorem. If the extension makes the fixed-efficiency transition trivial or directly coincident with known Dicke scaling theory, narrow/close honestly.
