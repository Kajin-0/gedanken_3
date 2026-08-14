# Experiment 09 — Rev. 1 targeted scaling prior-art audit

**Date:** 2026-08-14  
**Target claim:** fixed-efficiency coherence/dephasing dark-count scalability transition  
**Status:** NO DIRECT MATCH FOUND IN FOCUSED PRIMARY-SOURCE SEARCH / BROAD SCALING AND THERMODYNAMIC CLAIMS NARROWED / NOVELTY NOT ESTABLISHED

---

# 1. Claim under audit

The audit target is no longer the static `1/N` bright projection or the `gamma=0` `N` cancellation. Those are too close to standard normalized coherent-mode selection to carry a broad novelty claim.

The current manuscript-level claim is:

For a symmetric `N`-state bright excitation with bright extraction rate `kappa`, independent local pure dephasing rate `gamma`, `N` independent local dark-generation sites of per-site rate `d`, and a fixed required **conditional internal collection efficiency** `eta`, define

```math
\eta_c=\frac{\kappa}{\kappa+\gamma}.
```

Within the one-body Lindblad kernel plus explicit independent-particle Poisson lift,

```math
\boxed{
\begin{array}{c|c|c}
\eta<\eta_c & T_N=O(1) & \mu_N=O(1)\\
\eta=\eta_c & T_N=\Theta(\ln N) & \mu_N=\Theta((\ln N)^2)\\
\eta>\eta_c & T_N=O(N) & \mu_N=O(N^2).
\end{array}}
```

The novelty question is whether this detector-operational efficiency threshold and its accepted internal-dark scaling law are already explicit in stronger prior theory.

---

# 2. Young–Sarovar–Léonard quantum photodetector theory

S. M. Young, M. Sarovar, and F. Léonard, *Fundamental limits to single-photon detection determined by quantum coherence and backaction*, Phys. Rev. A 97, 033836 (2018), develops a fully quantum photodetector model and shows that coherence and amplification backaction control efficiency, dark counts, and jitter.

This is direct prior art for:

```text
coherence as a detector resource;
quantum-to-classical transfer dynamics;
efficiency/dark-count/jitter tradeoffs;
coherent internal-state design.
```

It is not a direct match to the present local-dark provenance model. The screened source does not state an efficiency boundary equivalent to

```math
\eta_c=\kappa/(\kappa+\gamma)
```

for an `N`-site bright/dark manifold or derive the associated `O(N^2)` accepted local-dark burden above that boundary.

**Disposition:** foundational detector prior art; no direct match to current theorem.

---

# 3. Shammah et al. and bright/dark dephasing

N. Shammah, N. Lambert, F. Nori, and S. De Liberato, *Superradiance with local phase-breaking effects*, Phys. Rev. A 96, 023863 (2017), explicitly treats local dephasing and nonradiative losses in collective emission. In the dilute-excitation regime it describes bright and dark bosonic quasiparticles and maps local dephasing into intermode scattering and lifetimes.

Therefore the manuscript must not claim novelty for:

```text
local dephasing moves excitation between bright and dark sectors;
collective-state lifetimes depend on local phase breaking;
large dark manifolds create slow collective dynamics.
```

The current candidate contribution is the detector task imposed on that dynamics: choose the *minimal gate at fixed internal collection efficiency* and determine the scaling of accepted continuous local dark generation.

**Disposition:** very close dynamical machinery; no direct detector-efficiency scaling match found.

---

# 4. Dark-state and coherence-assisted photocells

Coherence/dark-state control of absorption, radiative loss, and extraction is established in quantum photocell and light-harvesting theory, including:

- C. Creatore et al., Phys. Rev. Lett. 111, 253601 (2013);
- A. Fruchtman et al., Phys. Rev. Lett. 117, 203603 (2016).

These works make broad claims such as “quantum coherence or dark-state protection can improve photoconversion” unavailable to the present manuscript.

Their task is different: useful excitation is often parked in or transferred through dark states to suppress radiative loss and improve power/extraction. Experiment 09 instead treats independent internal dark *generation events* as the unwanted population and asks how many are accepted at a prescribed detection efficiency.

**Disposition:** close conceptual lineage; no direct `eta_c` dark-count scaling law found.

---

# 5. Collective quantum infrared detector transport

F. Pisani et al., *Electronic transport driven by collective light-matter coupled states in a quantum device*, Nature Communications 14, 3914 (2023), is the strongest current device-physics neighbor.

The work explicitly connects collective electronic polarization/coherence in a semiconductor infrared detector to a single-particle extractor and photocurrent. It also discusses prospects for low intrinsic dark current through extractor placement.

Accordingly, the present paper must not present

```text
collective optical excitation + electronic extractor + photocurrent
```

as a new architecture.

The focused comparison did not find the current provenance construction or the fixed-efficiency `N`-scaling transition in that paper.

**Disposition:** mandatory central comparator; not a direct theorem match.

---

# 6. 2026 Dicke/superabsorption scaling literature

This is the most serious threat to broad scaling language.

## Bassler, Lyne, Cuerda — Scaling theory of decoherence in Dicke superradiance

The July 2026 preprint `arXiv:2607.28034` develops an analytical large-`N` scaling theory for Dicke superradiance with local dephasing and spontaneous emission. It obtains fully collective, partially collective, and independent-emitter scaling regimes and identifies transient nonanalytic boundaries. For local dephasing, the relevant scaling variable compares the dephasing rate to the `N`-enhanced collective rate.

This directly establishes that:

```text
competition between collective dynamics and local decoherence can define distinct large-N scaling regimes;
transient observables can exhibit critical scaling boundaries;
logarithmic timing factors occur naturally in Dicke collective dynamics.
```

Therefore Experiment 09 must not claim the broad discovery of a “decoherence-induced scaling transition.”

The physical observable and control parameter are different. Bassler et al. study superradiant peak intensity and its scaling as decoherence is scaled relative to collective emission. Rev. 1 fixes `kappa` and `gamma`, varies detector size `N`, imposes a fixed **required collection efficiency `eta`**, and derives the minimum gate plus accepted local-dark burden from continuous internal dark generation.

No expression equivalent to

```math
\eta_c=\frac{\kappa}{\kappa+\gamma}
```

as a detector-efficiency scalability boundary, or the corresponding

```text
O(1) -> O((ln N)^2) -> O(N^2)
```

accepted dark-count partition, was identified in the screened source.

## Álvarez-Cuartas and Reina — quantum superabsorption

*Entanglement and dynamical scaling laws in quantum superabsorption*, Phys. Rev. Research 8, 033035 (2026), studies finite-size scaling of energy, charging time, power, and entanglement in open Dicke/Tavis-Cummings quantum batteries under relaxation and dephasing.

This further establishes collective/dephasing scaling as a mature active field. It does not directly formulate the present photodetector dark-count task.

**Disposition:** broad scaling novelty strongly narrowed; specific detector task still survives focused audit.

---

# 7. 2026 autonomous quantum-detector thermodynamics

E. Schwarzhans, T. J. G. Apollaro, I. Khomchenko, M. P. E. Lock, M. T. Mitchison, and M. Huber, *Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition*, PRX Quantum 7, 033001 (2026), DOI `10.1103/wm5p-tjtg`, develops a minimal autonomous quantum particle detector and explicitly analyzes detection efficiency, gain, jitter, dead time, and dark counts as functions of nonequilibrium thermodynamic resources.

This source makes a broad detector-level statement that better performance generally requires more dissipation and that temporal-performance improvements can increase dark counts.

It materially weakens any attempt to make Experiment 09's `kT ln mathcal C` local-detailed-balance algebra a principal novelty claim.

The Rev. 1 decision is therefore correct:

```text
thermodynamic affinity result: supporting constraint / corollary;
not coequal manuscript novelty.
```

The current fixed-efficiency bright/dark-manifold scaling theorem is structurally different from the autonomous-machine model, and no direct match was identified in the screened article.

**Disposition:** important new 2026 detector-thermodynamics prior art; thermodynamic claims demoted.

---

# 8. Quantum-jump and other low-dark quantum detectors

Quantum-state architectures already achieve or target low dark-count operation. For example, the single-atom quantum-jump photodetector (Phys. Rev. Research 6, 033338 (2024)) reports state-selective photon-triggered jumps with low signal-unprovoked dark-jump rates.

This means the paper cannot suggest that quantum-state engineering for low dark counts is itself new.

The distinction remains that the present theorem deliberately keeps an extensive set of internal dark-generation sites and studies the asymptotic acceptance of those events under a coherent collective filter and local dephasing.

**Disposition:** relevant device context; not a direct scaling match.

---

# 9. Direct searches for the threshold form

Focused primary-source searches included combinations of:

```text
photodetector + bright state + dephasing + dark counts;
coherence + detector efficiency + dark count scaling;
collective bright/dark + fixed efficiency;
kappa/(kappa+gamma) + dephasing + bright state;
Dicke scaling + detector efficiency;
local dephasing + dark-count N scaling.
```

No primary source found in this focused pass stated an equivalent theorem with all of the following:

```text
fixed kappa and gamma;
N coherently participating local states;
independent local internal dark-generation rate proportional to N;
minimal gate selected by a fixed conditional internal signal efficiency eta;
critical eta_c=kappa/(kappa+gamma);
O(1), logarithmic, and O(N)/O(N^2) gate/dark-count regimes.
```

This is not proof of novelty and is not an exhaustive citation-network or patent search.

---

# 10. Revised novelty matrix

```text
coherent state vs incoherent mixture discrimination:
    ESTABLISHED

normalized bright-mode rejection of isotropic independent noise:
    STANDARD / NOT A NOVELTY CLAIM

bright/dark-state physics:
    ESTABLISHED

local-dephasing bright/dark scattering:
    ESTABLISHED

coherence-assisted photocurrent / photocells:
    ESTABLISHED

collective quantum infrared detector extraction:
    ESTABLISHED

collective/decoherence scaling regimes:
    ESTABLISHED ACTIVE FIELD

quantum detector efficiency/dark-count thermodynamic tradeoffs:
    ESTABLISHED, INCLUDING 2026 PRX QUANTUM WORK

Rev. 1 fixed-efficiency internal-dark scalability theorem:
    NO DIRECT MATCH FOUND IN FOCUSED PRIMARY-SOURCE AUDIT

novelty:
    NOT ESTABLISHED
```

---

# 11. Current publication-risk assessment

The paper is now stronger than Rev. 0 because its center is not the elementary `1/N` projection cancellation.

A skeptical referee can still argue that the theorem is a straightforward consequence of a two-timescale linear system once the detector task is chosen. The response must be the exact detector-level content, not stronger rhetoric:

- the operating-point variable `eta` creates a sharp asymptotic boundary;
- the lower branch keeps an `O(N)` raw dark-generation system at `O(1)` accepted dark burden;
- crossing the boundary forces use of the slow dark-manifold recycling mode and changes the accepted burden to `O(N^2)`;
- the critical boundary has an intermediate Lambert-W/logarithmic scaling.

That combination is sufficiently nontrivial to justify continued manuscript development, but not yet enough to authorize priority language.

---

# 12. Decision

```text
REV. 1 THEOREM: SURVIVES FOCUSED PRIOR-ART CHECK
BROAD COHERENCE NOVELTY: REJECTED
BROAD DECOHERENCE-SCALING NOVELTY: REJECTED
THERMODYNAMIC kT ln C AS PRINCIPAL NOVELTY: REJECTED
SPECIFIC FIXED-EFFICIENCY DARK-COUNT SCALING CONTRIBUTION: STILL PLAUSIBLE
PAPER PATH: CONTINUE
NOVELTY: NOT ESTABLISHED
```

Next scientific gate should be an adversarial review of Rev. 1 itself, followed—if it survives—by theory figures and a more complete citation-production audit.
