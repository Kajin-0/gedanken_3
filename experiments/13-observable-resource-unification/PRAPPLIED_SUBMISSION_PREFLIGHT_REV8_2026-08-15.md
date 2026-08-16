# Physical Review Applied submission preflight — Experiment 13 Rev. 8

**Date:** 2026-08-15  
**Target:** Physical Review Applied — Regular Article  
**Status:** **SCIENTIFIC/PRODUCTION PREFLIGHT COMPLETE / HUMAN METADATA + DATA-ARCHIVE DECISION REQUIRED**

This file supersedes the Rev. 7 preflight for manuscript-specific production identity, source-package instructions, and cover-letter wording.

## 1. Controlling manuscript

Title:

> **Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability**

Controlling identity:

```text
GitHub Actions run:   31916728949
source commit:        813fd8a2fc3011ef6e3ba63a0567cb3eee30297b
artifact ID:          9255118533
artifact digest:      a5d7aac0a5f3a68783a3510c9c2e8632af3e5b4e34f326e3012dd1aa6316bfcd
PDF SHA-256:          309655aec80a7778428beedad4c95b53b27b8ebae24143310b1f4fdc1c6faf87
TeX SHA-256:          08efd63da8e5558a07bbc5a4bc9be8667811bf2314705c69f257e30b9b565973
pages:                8
undefined refs/cites: none
overfull/underfull:   none
all-page visual QA:   PASS
hostile review:       PASS
```

## 2. Claim hierarchy for submission

Foreground in this order:

```text
1. finite-temperature optical population lower bound;
2. full support/Fermi/capacity/selectivity tightness hierarchy;
3. numerically converged HgCdTe production closure;
4. homogeneous full-BIA robustness of the exact-shell hierarchy;
5. stage-specific non-transferability framework;
6. terminal photon-recycling/readout observability boundary.
```

Do not headline the definitional `S tau = 1` identity.

The BIA result is a **homogeneous effective eight-band stress test**, not an atomistic/interface prediction.

## 3. Suitability statement

Use a concise statement along these lines:

> This manuscript derives an equilibrium lower bound linking selected direct optical conductivity to the minimum thermal population of the one-body states carrying that response under a finite exact-shell coupling capacity. It resolves the bound’s tightness into support coverage, Fermi-statistical slack, shell-to-global capacity utilization, and within-shell selectivity, and validates the decomposition in a numerically converged HgCdTe model. A symmetry-checked homogeneous inversion-asymmetry stress test shows that realistic fixed-k splitting leaves the sampled within-shell factor at unity and changes the full bound/reference ratio by less than one percent. The broader framework connects material inference to stage-specific detector observability.

Do not add unsupported priority language.

## 4. Cover-letter draft

```text
Dear Editors of Physical Review Applied,

Please consider our manuscript, “Stage-specific spectral geometry of photodetection: state-count bounds, selectivity, and observability,” for publication as a Regular Article in Physical Review Applied.

The manuscript derives an equilibrium lower bound on the thermal one-body endpoint population required to support selected direct optical conductivity when the exact-shell optical-velocity coupling has finite capacity. It then resolves the bound’s tightness into selected-support coverage, Fermi statistics, shell-to-global capacity mismatch, and within-shell singular-value concentration.

A numerically converged second-order eight-band HgCdTe calculation provides an end-to-end material test. In the broad validation window, the selected active-support fraction is 0.66897, the Fermi-statistical factor is 0.30684, and the spectral-capacity tightness is 0.57262, giving an active-population bound tightness of 0.17570 and a full bound/reference ratio of approximately 0.1175.

We additionally test the principal material-model caveat by adding symmetry-checked homogeneous B8v+, B8v-, and C_k bulk-inversion-asymmetry couplings. The inversion breaking changes the sampled active exact shells from two-dimensional PT doublets to one-dimensional shells, but every active block remains at unit within-shell selectivity. The independently optimized capacity changes by about 0.43% and the full bound/reference ratio by about -0.82%. The manuscript explicitly limits this result to the homogeneous effective eight-band model and does not claim atomistic or interface-BIA completeness.

The broader detector framework is stage-specific: optical capacity, task/coherence selectivity, internal correlation, and terminal observability belong to different physical maps. A conservative photon-recycling example shows how ideal final-sink counting can erase interterminal cross-noise while finite-transit Shockley-Ramo motion can restore finite-frequency source-channel support.

The manuscript treats positive-operator methods, stable-rank concepts, bright/dark-state physics, Shockley-Ramo theory, Poisson splitting, photon recycling, and optical sum rules as established ingredients rather than priority claims.

[SUBMISSION-HISTORY / RELATED-MANUSCRIPT STATEMENT — HUMAN CONFIRMATION REQUIRED]

[OPTIONAL RECOMMENDED OR EXCLUDED REFEREES]

Thank you for considering the manuscript.

Sincerely,
[AUTHOR NAME]
[AFFILIATION]
[EMAIL]
```

## 5. Experiment-12 relationship

Project policy remains:

```text
Experiment 13 Rev. 8: sole primary active submission manuscript;
Experiment 12 manuscript: frozen fallback/development provenance;
concurrent or later substantially overlapping submission without a new overlap audit: prohibited.
```

The human author must still supply the truthful journal submission-history declaration.

## 6. Data Availability / software archive

Preferred route before publication:

```text
archive the controlling Rev. 8 source and reproduction scripts in a persistent repository;
obtain a DOI or other permanent identifier;
add the archive as a formal data/software reference;
use a concise Data Availability Statement pointing to it.
```

Do not invent a DOI. If no persistent archive exists at submission, use a truthful public-repository/commit statement consistent with journal requirements and update later if appropriate.

The reproduction archive should include the mature BIA scripts and QA, not just the manuscript source.

## 7. Source package for APS

Repository reconstruction:

```text
build_rev4.py
-> Rev4-to-Rev5 patches
-> build_rev6.py
-> build_rev7.py
-> build_rev8.py
-> finalize_rev8.py
```

For journal upload prefer the generated self-contained inputs:

```text
rev8_prapplied.tex
rev8_figures.tex
rev4_unified.bib
rev8_extra.bib
```

The submitted PDF must match the final metadata-complete source compilation.

## 8. Science closed by default

Do not reopen absent a concrete defect:

```text
central cross-mu population theorem;
thermodynamic uniform-capacity / liminf formalism;
full tightness factorization;
production HgCdTe baseline;
rank and carrier-cutoff convergence audits;
homogeneous full-BIA implementation and exact-shell result;
BIA continuous-capacity multi-seed/grid/cluster robustness;
coherent N_eff specialization;
immigration-death-exchange spectrum;
Poisson final-sink cancellation;
Shockley-Ramo zero-DC / finite-frequency-support result.
```

No Rev. 9 is authorized by default.

## 9. Human completion checklist

```text
[ ] author name(s)
[ ] affiliation(s)
[ ] corresponding-author email
[ ] ORCID if desired/required
[ ] acknowledgments/funding statement
[ ] conflicts/disclosures as applicable
[ ] truthful submission-history / related-manuscript declaration
[ ] final Data Availability / persistent archive decision
[ ] optional recommended/excluded referees
[ ] replace manuscript metadata placeholders
[ ] rebuild metadata-complete Rev. 8 through CI
[ ] record final PDF/source hashes
[ ] visually inspect every final page
[ ] verify submitted source compiles to submitted PDF
```
