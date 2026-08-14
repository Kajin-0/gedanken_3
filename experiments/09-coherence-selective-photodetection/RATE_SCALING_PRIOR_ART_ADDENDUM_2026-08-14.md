# Experiment 09 — Rate-scaling prior-art addendum

**Date:** 2026-08-14  
**Status:** BROAD COLLECTIVE-DETECTOR AND DECOHERENCE-SCALING CLAIMS NARROWED / NO DIRECT MATCH TO CURRENT DETECTOR TASK FOUND / NOVELTY NOT ESTABLISHED

## Current theorem under audit

The active result is no longer a fixed-`kappa` law. Let

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
```

At fixed required conditional internal collection efficiency `eta`, the detector's minimum gate `T_N` and accepted internally generated local-event burden `mu_N` have the phase diagram recorded in `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`.

The specific candidate contribution is therefore:

```text
collective coherent detector kernel
+ extensive independent internal local-event generation
+ minimum gate chosen by required internal collection efficiency
+ size-dependent extraction/dephasing rates
-> explicit accepted-event burden phase diagram.
```

No broad claim that collective/decoherence scaling itself is new is authorized.

---

# 1. Closest coherent detector architecture — Young, Sarovar, Leonard 2020

Steve M. Young, Mohan Sarovar, and Francois Leonard,

> “Design of High-Performance Photon-Number-Resolving Photodetectors Based on Coherently Interacting Nanoscale Elements,” ACS Photonics 7, 821–830 (2020), DOI `10.1021/acsphotonics.9b01754`.

This is a substantially closer precedent than generic quantum-state discrimination.

The paper explicitly proposes subwavelength detector elements that interact **collectively with the photon field** and seeks a detector with simultaneous photon-number resolution, high efficiency, low jitter, low dark counts, and high count rate. It is part of the same Young–Sarovar–Leonard quantum-photodetector program that treats field, absorption, and amplification as one quantum system.

Therefore Experiment 09 must not claim novelty for:

```text
coherently interacting detector elements;
collective optical coupling;
bright/dark internal detector manifolds;
coherence-sensitive detector optimization;
high-efficiency / low-dark-count quantum detector design.
```

The current theorem remains narrower. The screened source does not state the present task

```text
N independent internal local-generation sites
+ gate chosen by prescribed conditional internal efficiency
+ kappa_N~N^alpha and gamma_N~N^beta
-> accepted internal-event phase diagram.
```

**Disposition:** mandatory central prior art; no direct theorem match identified.

---

# 2. Young, Sarovar, Leonard 2018 and general quantum photodetector theory

The earlier Phys. Rev. A 97, 033836 (2018) work establishes that quantum coherence and amplification backaction control detector efficiency, dark counts, jitter, and optimal design.

This eliminates any claim that Experiment 09 newly identifies coherence as a detector resource or a tradeoff between coherent dynamics and detector performance.

The current paper must present its contribution as an **asymptotic scaling theorem for one specified detector task**, not a new general theory of quantum photodetection.

---

# 3. Dicke/superradiance decoherence scaling — Bassler, Lyne, Cuerda 2026

The July 2026 preprint

> N. S. Bassler, J. Lyne, and J. Cuerda, “Scaling theory of decoherence in Dicke superradiance,” arXiv:`2607.28034`

develops a large-`N` analytical scaling theory including local dephasing and spontaneous emission. It obtains fully collective, partially collective, and independent-emitter regimes and identifies a transient phase boundary.

This is direct prior art for the methodology

```text
collective rate scaling versus local decoherence scaling
-> distinct large-N dynamical regimes.
```

Therefore the `alpha-beta` rate-sector structure in Experiment 09 cannot be sold as a new generic phase-diagram concept.

The remaining distinction is the measured/optimized object. Bassler et al. study superradiant emission observables and their collective scaling. Experiment 09 chooses a gate by a **detector efficiency requirement** and then evaluates the total accepted burden from an explicitly extensive internal local-generation process.

No direct statement of this minimum-gate accepted-event phase diagram was identified in the screened source.

**Disposition:** closest scaling-theory neighbor; broad scaling novelty rejected; detector task still distinct in focused audit.

---

# 4. Quantum-detector thermodynamics — Schwarzhans et al. 2026

E. Schwarzhans et al.,

> “Quantum Detectors as Autonomous Machines: Assessing the Nonequilibrium Thermodynamics of Information Acquisition,” PRX Quantum 7, 033001 (2026), DOI `10.1103/wm5p-tjtg`

models a quantum particle detector as an autonomous nonequilibrium thermal machine and explicitly connects entropy production to detection efficiency, gain, jitter, dead time, and dark counts.

This is strong detector-level prior art for thermodynamic performance tradeoffs. It further supports the current decision to keep the Experiment-09 `kT ln(mathcal C)` local-detailed-balance relation as a secondary resource caveat rather than a principal novelty claim.

---

# 5. Other close collective/dark-state physics

Established neighboring physics also includes:

```text
bright/dark quasiparticle scattering under local dephasing;
dark-state and coherence-assisted photocells;
collective electronic polarization feeding extractor current in quantum infrared detectors;
many-body dark-state transport and storage;
collective-state protection from dephasing.
```

These literatures make the ingredients individually non-novel.

---

# 6. Focused search result for the complete detector task

Primary-source searches were targeted at combinations of

```text
collective coherent photodetector + dark count scaling;
bright/dark detector + dephasing + efficiency;
collective detector elements + size-dependent extraction;
Dicke scaling + detector efficiency + dark counts;
minimum detection gate + internal dark generation;
kappa/(kappa+gamma) + detector efficiency;
collective rate exponent + accepted dark counts.
```

No direct primary source was identified in this focused pass that contains all of:

```text
1. N coherently participating detector states;
2. independent internal local-generation rate proportional to N;
3. a gate selected by fixed conditional internal signal collection eta;
4. explicit kappa_N~N^alpha and gamma_N~N^beta scaling;
5. analytical scaling of the accepted internally generated event burden.
```

This is not proof of novelty and is not an exhaustive patent/citation-network search.

---

# 7. Current novelty matrix

```text
coherent collective photodetector elements:
    ESTABLISHED

coherence/backaction detector tradeoffs:
    ESTABLISHED

bright/dark detector manifolds:
    ESTABLISHED

local-dephasing bright/dark transfer:
    ESTABLISHED

collective-vs-decoherence large-N scaling sectors:
    ESTABLISHED ACTIVE FIELD

quantum-detector thermodynamic performance tradeoffs:
    ESTABLISHED

Experiment-09 minimum-gate accepted-internal-event phase diagram:
    NO DIRECT MATCH FOUND IN FOCUSED AUDIT

novelty:
    NOT ESTABLISHED
```

---

# 8. Manuscript consequence

Any Rev. 2 paper must put Young et al. 2020 and Bassler et al. 2026 near the center of the Introduction/Discussion.

The defensible possible contribution is narrow:

> Given a coherence-selective detector kernel, extensive independent internal local generation, a prescribed conditional internal collection efficiency, and specified scaling of useful extraction and local dephasing with detector size, derive the asymptotic gate and accepted-internal-event burden.

The manuscript should state that the broader collective detector architecture and broader decoherence scaling framework are established.

**Decision:** continue to Rev. 2, but with conservative novelty language and the general rate-scaling theorem as the central result.
