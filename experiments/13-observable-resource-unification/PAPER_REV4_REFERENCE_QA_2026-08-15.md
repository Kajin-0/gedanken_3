# Experiment 13 — Rev. 4 reference QA and controlling bibliography corrections

**Date:** 2026-08-15  
**Applies to:** `PAPER_DRAFT_REV4_CLAIM_REFERENCE_CLEAN_2026-08-15.md`  
**Status:** **REFERENCE QA PASS WITH ONE CONTROLLING INLINE CORRECTION / NO UNRESOLVED SCIENTIFIC PLACEHOLDER**

## 1. Purpose

Rev. 4 was deliberately written as a claim/reference-clean scientific draft. Its only explicit unresolved bibliography placeholder was Ref. 33, the bulk-inversion-asymmetry reference used to delimit the symmetry scope of the BIA-neglecting eight-band Kane validation.

This note records the verified correction and the final claim/reference disposition. Until a typeset source is generated, this note supersedes the placeholder wording in Rev. 4.

---

# 2. Ref. 33 — exact published BIA citation

Replace Rev. 4 Ref. 33 with:

```text
[33] X. Cartoixà, D. Z.-Y. Ting, and T. C. McGill,
“Description of bulk inversion asymmetry in the effective-bond-orbital model,”
Phys. Rev. B 68, 235319 (2003),
doi:10.1103/PhysRevB.68.235319.
```

The associated eight-band effective-mass preprint is `cond-mat/0212394`, but the published PRB citation above is the appropriate journal reference.

This supports the manuscript's narrow statement that more complete zincblende multiband descriptions can include bulk-inversion-asymmetry terms and that the exact fixed-k `PT` doublet argument of the present BIA-neglecting validation should not be generalized to full zincblende HgCdTe.

---

# 3. Ref. 18 — title normalization

Rev. 4 gives the 2012 HgCdTe recycling paper descriptively. The verified title is:

```text
K. Jóźwikowski, M. Kopytko, and A. Rogalski,
“Photon Recycling Effect in Double-Layer Heterojunction HgCdTe Photodiodes,”
J. Electron. Mater. 41, 2766–2774 (2012),
doi:10.1007/s11664-012-2093-7.
```

Use this exact title in the typeset bibliography.

---

# 4. Ref. 16 — Mao et al. 2025 neighboring optical-sum-rule paper

Verified publication metadata:

```text
D. Mao, J. F. Mendez-Valderrama, and D. Chowdhury,
“Low-energy optical absorption in correlated insulators:
Projected sum rules and the role of quantum geometry,”
Phys. Rev. B 112, 075116 (2025),
published 8 August 2025.
```

This reference is mandatory because it is close enough in optical-response/sum-rule space that omission would create an avoidable literature-completeness vulnerability.

The manuscript already distinguishes it correctly from the present theorem:

```text
Mao et al.:
    projected low-energy inverse-frequency-weighted optical sum rule,
    correlated projected Hilbert spaces,
    quantum geometry / QFI interpretation;

present work:
    direct cross-mu one-body transitions,
    thermal Fermi endpoint kernel,
    exact-energy shell velocity capacity,
    inverse lower bound on equilibrium endpoint population.
```

No direct collision is identified.

---

# 5. Claim/reference alignment audit

## Task/selectivity context

Rev. 4 correctly treats task-based information matrices as established and cites Barrett et al. and Clarkson/Shen. No priority claim is made for task dependence or operator-valued detector metrics.

**PASS.**

## General quantum photodetector / coherence context

Young–Sarovar–Léonard and Xu et al. delimit the general photodetector-framework and detector-coherence neighborhoods. Helstrom/Glauber/Dicke/Scully delimit generic state-discrimination/coherence/collective-bright-state ingredients.

Rev. 4 claims only the detector-specific cross-identification of `N_eff` with the same forward/inverse capacity ratio used in the thermal theorem.

**PASS.**

## Optical population theorem

Rev. 4 preserves the authoritative Experiment-12 Kubo convention, Fermi kernel, selected cross-mu scope, basis-invariant exact-shell capacity, active endpoint ranks, and the distinction from recombination/dark-current quantities.

The modern neighboring optical-response literature Onishi–Fu and Mao–Mendez-Valderrama–Chowdhury is present.

**PASS.**

## HgCdTe model/reference chain

Novik et al., Laurenti et al., Teppe et al., Man/Pan, and the now-resolved Cartoixà–Ting–McGill BIA reference support the stated model and symmetry boundary.

The manuscript does not claim that real zincblende HgCdTe has exact active-shell singular-value isotropy.

**PASS.**

## Ramo / GR-noise context

Dąbrowski 1987/1989 is explicitly cited. Rev. 4 does not claim first use of Shockley–Ramo theory or first recognition that internal carrier fluctuations and terminal current differ.

**PASS.**

## Photon recycling / crosstalk context

Direct HgCdTe recycling/reabsorption/crosstalk papers from 2011, 2012, and 2019 are cited. Rev. 4 claims only the conditional conservative-lineage final-sink null and its finite-transit Ramo lifting.

**PASS.**

## Poisson-output context

Classical M/G/infinity and infinite-server network results are cited to delimit the stochastic ingredient. No queueing-theory novelty is claimed.

**PASS.**

---

# 6. Remaining bibliography production work

There is no unresolved **scientific** reference placeholder after applying the Ref. 33 correction above.

Normal publication production still requires:

```text
- import the final journal/BibTeX formatting style;
- normalize capitalization, initials, page ranges, and article titles;
- verify DOI formatting mechanically in the final bibliography;
- decide whether every background textbook citation is necessary in main text;
- preserve the primary-source references carrying the actual novelty boundaries.
```

These are formatting/completeness tasks, not theory blockers.

---

# 7. Final reference-QA disposition

```text
UNRESOLVED SCIENTIFIC PLACEHOLDER:       NONE after Ref. 33 correction
BIA MODEL-SCOPE SUPPORT:                 PASS
MAO 2025 LITERATURE COMPLETENESS:        PASS
TASK/QUANTUM PRIOR-ART BOUNDARY:         PASS
RAMO/GR-NOISE PRIOR-ART BOUNDARY:        PASS
HgCdTe RECYCLING PRIOR-ART BOUNDARY:     PASS
POISSON-OUTPUT PRIOR-ART BOUNDARY:       PASS
REV4 REFERENCE NETWORK:                  SCIENTIFICALLY ADEQUATE FOR HOSTILE REVIEW
```

## Next action

Perform the final Rev. 4 hostile claim/reference review. If it finds no central defect or material overclaim, freeze the scientific content and promote Experiment 13 to the repository-wide active flagship frontier before beginning typesetting/figure production.
