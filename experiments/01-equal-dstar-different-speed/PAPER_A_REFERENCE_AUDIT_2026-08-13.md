# Paper A — Final Reference Audit

**Date:** 2026-08-13  
**Target:** Applied Optics rendered manuscript  
**Status:** PRIMARY/TRACEABLE RECORD CHECK COMPLETE ENOUGH FOR RENDER FREEZE; TWO MATERIAL CITATION-METADATA ERRORS CORRECTED

## Purpose

This audit checks the 16-reference journal-facing bibliography after the theorem and submission architecture were already frozen. It is a production/citation audit, not a new prior-art search and not a reopening of the theory.

## Material corrections found

### Ref. 8 — Croce et al. 2004

The earlier journal-facing Markdown listed the authors in the wrong order after the first two names.

Correct APS record:

```text
R. P. Croce
Th. Demma
M. Longo
S. Marano
V. Matta
V. Pierro
I. M. Pinto
```

Correct title:

> Correlator bank detection of gravitational wave chirps—False-alarm probability, template density, and thresholds: Behind and beyond the minimal-match issue

Correct record:

```text
Phys. Rev. D 70, 122001 (2004)
DOI: 10.1103/PhysRevD.70.122001
```

The rendered LaTeX/PDF now uses this order and title.

### Ref. 11 — Milstein et al. 2008

The earlier journal-facing Markdown contained an incorrect author list (`S. M. Oh`, `D. A. Kashdan`, etc.).

The official Applied Optics record gives:

```text
Adam B. Milstein
Leaf A. Jiang
Jane X. Luu
Eric L. Hines
Kenneth I. Schultz
```

Correct record:

> Acquisition algorithm for direct-detection ladars with Geiger-mode avalanche photodiodes

```text
Applied Optics 47, 296–311 (2008)
DOI: 10.1364/AO.47.000296
```

The rendered LaTeX/PDF now uses this corrected author list.

## Remaining references checked

The following metadata were checked against publisher records, official archives, or the original official preprint record as appropriate:

1. R. C. Jones, JOSA 50, 883–886 (1960), DOI `10.1364/JOSA.50.000883`.
2. J. P. Garcia and E. L. Dereniak, Applied Optics 29, 559–569 (1990), DOI `10.1364/AO.29.000559`.
3. Y. Yang et al., Nature Communications 17, article 6077 (2026), DOI `10.1038/s41467-026-72259-1`.
4. V. Pecunia et al., Nature Photonics 19, 1178–1188 (2025), DOI `10.1038/s41566-025-01759-1`.
5. C. R. Doering and P. M. Harvey, Applied Optics 26, 633–642 (1987), DOI `10.1364/AO.26.000633`.
6. R. Vio and P. Andreani, arXiv:1602.02392 (2016).
7. G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, and E. Ruiz Morales, Physical Review D 107, 023027 (2023), DOI `10.1103/PhysRevD.107.023027`.
9. A. Polydoros and C. L. Weber, IEEE Transactions on Communications 32(5), 550–560 (1984), DOI `10.1109/TCOM.1984.1096113`.
10. Y.-T. Su, IEEE Transactions on Communications 36(6), 724–733 (1988), DOI `10.1109/26.2793`.
12. M. M. Mustapha and R. F. Ormondroyd, Journal of Lightwave Technology 18(12), 1742–1748 (2000), DOI `10.1109/50.908711`.
13. A. Keshavarzian and J. A. Salehi, IEEE Transactions on Communications 50(3), 473–483 (2002), DOI `10.1109/26.990909`.
14. A. T. Pham and H. Yashima, IEICE Transactions on Communications E88-B(12), 4570–4577 (2005), DOI `10.1093/ietcom/e88-b.12.4570`.
15. D. Slepian, Bell System Technical Journal 41, 463–501 (1962), DOI `10.1002/j.1538-7305.1962.tb02419.x`.
16. S. O. Rice, Bell System Technical Journal 23(3), 282–332 (1944), DOI `10.1002/j.1538-7305.1944.tb00874.x`.

For IEEE records whose full Xplore metadata page was not consistently retrievable in the audit environment, title/order/pages/DOI were cross-checked against official or authoritative archival metadata rather than inferred from memory.

## Rendered-source status

The local rendered LaTeX source and PDF contain the corrected Ref. 8 and Ref. 11 metadata.

The older Markdown Rev. 3 bibliography should therefore be treated as superseded for final citation metadata by the rendered source and this audit record.

No scientific theorem or prior-art disposition changed as a result of the citation corrections.
