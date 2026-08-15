# Experiment 13 — flagship journal target strategy

**Date:** 2026-08-15  
**Controlling manuscript:** Rev. 4 claim/reference-clean scientific draft  
**Status:** **FIRST TARGET SELECTED / APS REGULAR-ARTICLE PRODUCTION AUTHORIZED**

## Recommendation

### First target: Physical Review Applied — Regular Article

This is the best first target for the unified flagship because the paper's center of gravity is an applied-physics detector/material theorem rather than abstract operator mathematics:

```text
selected optical conductivity -> minimum thermal endpoint population;
realistic eight-band HgCdTe validation;
quantitative diagnosis of theorem tightness;
coherence/task consequences of coupling concentration;
terminal-noise observability consequences of detector readout.
```

The manuscript bridges fundamental detector theory and practical semiconductor photodetector constraints, matching the intended basic/applied interface better than a narrowly quantum or condensed-matter journal.

Use an APS regular-article architecture. Do not force the work into a letter-length format.

### Second target: Physical Review Research

Natural fallback if PR Applied judges the manuscript too broad or insufficiently device-specific. The scientific structure can be reused with minimal formatting change because the APS manuscript architecture is compatible.

### Third target: Optica

Plausible high-selectivity optics/photonics target if the presentation is shifted more strongly toward optical-response bounds and detector-system implications. The present Rev. 4 is more naturally organized as an applied-physics theory paper than as a concise optics flagship article.

### High-risk stretch targets

PRX / Nature Communications should not be the default first submission at the present evidence level. The manuscript has broad conceptual reach, but the central reciprocity is elementary algebra and the realistic validation is one BIA-neglecting HgCdTe model. A desk rejection on perceived general significance would not provide useful scientific feedback.

---

# Editorial positioning for PR Applied

Lead with the material theorem, not the positive-operator identity.

Recommended one-sentence positioning:

> We derive a direct optical lower bound on the equilibrium population of the electronic states carrying selected interband response, resolve the bound's tightness into spectral and thermal factors in realistic HgCdTe, and show that the same coupling geometry controls coherent/task selectivity and downstream visibility of conservative internal recycling.

Do not position the paper as:

```text
"a unified theory of all photodetectors";
"a replacement for D*";
"a new mathematical theory of measurement operators."
```

---

# Main-text priority

For PR Applied, allocate main-text emphasis approximately as follows:

```text
Introduction / physical motivation                   10%
Optical thermal-population theorem                  25%
Admissible-domain selectivity/resource geometry     12%
Task + coherence specializations                    10%
Shell decomposition + production HgCdTe             25%
Terminal recycling / Ramo observability             13%
Discussion / conclusion                              5%
```

The Experiment-12 theorem and HgCdTe application together should remain the majority of the paper.

---

# What belongs in appendices / Supplemental Material

Move technical detail out of the main line when it is needed for rigor but not for the conceptual argument:

```text
A. Full proof of the Fermi endpoint inequality and equality condition.
B. Finite-volume exact-shell / thermodynamic-limit formalization.
C. Trace-rank and direct-sum proofs.
D. Stable-rank / task-penalty proof.
E. Full eight-band Kane Hamiltonian and parameters.
F. Chemical-potential / quadrature / ordinary-supremum convergence.
G. PT/quaternionic proof of shell singular-value isotropy in the BIA-neglecting model.
H. Poisson-lineage derivation and Shockley-Ramo Fourier-domain proof.
```

The main text should state enough to make every theorem understandable without requiring the supplement for definitions.

---

# Figure plan

Limit the first production pass to **five theorem-bearing figures**.

## Fig. 1 — staged detector map and spectral accounting

Show the detector chain

```text
task -> optical excitation -> internal dynamics -> terminal readout
```

with the physical map/positive effect used at each stage. This figure exists to prevent the false impression that one universal matrix is being reused physically.

## Fig. 2 — thermal optical population theorem

Compact flow from selected cross-mu conductivity through the Fermi/Kubo functional and exact-shell capacity to the active endpoint population lower bound.

## Fig. 3 — forward/inverse spectral geometry

Use representative fixed-domain spectra to show:

```text
ensemble-average response;
maximum allowed capacity;
forward selectivity;
inverse certified fraction;
stable-rank uniform limit;
rank-one N_eff endpoint.
```

No decorative eigenvalue art; every plotted quantity must correspond to an equation.

## Fig. 4 — production HgCdTe decomposition

Primary panel:

```text
0.5726 capacity factor x 0.3068 Fermi/Kubo factor = 0.1757.
```

Secondary panel: shell capacity utilization distribution, with `S_a^act=1` in the BIA-neglecting model made explicit.

## Fig. 5 — recycling observability boundary

Compare the same A-to-B conservative lineage under:

```text
final-sink counting -> source-channel null;
finite-transit Ramo -> zero DC source charge but finite-frequency source support allowed.
```

Tie the panels to `G_A(omega)` and the cross-channel overlap.

Experiment-01's specialized timing-search witness does not require its own flagship figure unless the paper is difficult to motivate without it. Prefer one concise textual/analytic witness or an inset in Fig. 3.

---

# Production format

Use REVTeX/APS-compatible LaTeX from the first typeset pass so that PR Applied and PR Research remain low-cost alternatives.

Production order:

```text
1. write lean REVTeX source from Rev. 4;
2. create theorem figures from deterministic code/vector output;
3. import verified bibliography;
4. compile;
5. check equation/reference numbering and page balance;
6. all-page visual QA;
7. hostile rendered-manuscript review;
8. only then write cover letter and submission metadata.
```

---

# Submission strategy

Keep the Experiment-01, -09, and -12 manuscript packages frozen as fallbacks.

Do not simultaneously submit materially overlapping standalone and unified papers.

If PR Applied rejects for breadth/significance rather than a scientific defect, use the decision to choose between:

```text
PR Research / Optica continuation of the flagship;
or
reversion to the mature standalone packages.
```

Do not dismantle the fallback packages merely because the flagship is now the primary route.
