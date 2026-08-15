# Experiment 12 — PRB Rev11 minor-revision typeset QA

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **MINOR REFEREE CLEANUP COMPLETE / TYPESET QA PASS / CENTRAL THEOREM UNCHANGED**

## Production basis

Rev11 is a surgical delta from the QA-passed Rev10 referee-repaired source. The controlling delta is

`typeset/rev10_to_rev11_minor_revision.patch`.

The exact reconstruction was verified byte-for-byte against the final local TeX.

## Scientific changes

1. Added direct-sum/block-diagonal justification linking the complete exact-energy-shell definition in Eq. (21) to the k-resolved ordinary supremum in Eq. (49).
2. Stated the Table-II numerical support-rank criterion `s > 1e-6 m/s` and documented threshold stability from `1e-9` to `1e4 m/s` on a reduced audit grid.
3. Added and distinguished Onishi–Fu, Phys. Rev. X 14, 011052 (2024).
4. Added a reduced-grid one-at-a-time `+/-5%` HgCdTe parameter-sensitivity diagnostic; broad ratio remains order `10^-1`.
5. Added one-line square proof of Appendix B Eq. (B1).

No equation from the central derivation was changed. Main equations remain (1)–(50); appendix equations remain (A1) and (B1).

## Exact hashes

```text
Rev11 TeX SHA-256  a75b75d6016d335746751b7c75a01d49deea7c4796c2eff30a7dd99c1f73cd68
Rev11 PDF SHA-256  ed5a558ac561cb67f0e918de96f4774c493cacd54fd6f3bea01e597890a7df5d
```

## Typesetting

```text
REVTeX 4-2
APS / PRB / reprint
US letter
standard two-column journal typography
13 pages
```

Rev11 remains 13 pages; the minor revisions did not increase page count.

## Compile QA

Three `pdflatex` passes completed successfully.

```text
critical LaTeX/package/class warnings: none
overfull boxes:                      none
undefined references/citations:      none
unresolved/stuck floats:             none
```

## Structural QA

```text
main numbered equations: (1) through (50)
appendix equations:       (A1), (B1)
tables:                   I, II, III
references:               19
sections:                 I-VIII + Appendices A/B
central Eq. (29):         unchanged
```

## Visual QA

All 13 pages were rendered at 160 dpi and inspected. Specific checks:

- page 9: revised Eq. (49) direct-sum explanation and support-rank paragraph — clean;
- page 10: full-width Table II, sensitivity paragraph, and Onishi–Fu positioning — clean;
- page 13: Appendix B square proof, Table III, and 19-reference bibliography — clean.

No clipping, overlap, broken glyphs, float collision, table collision, or bibliography collision was found.

## Final disposition

```text
CENTRAL THEOREM:                         PASS / UNCHANGED
DIRECT-SUM EQ. (49) JUSTIFICATION:       FIXED
SUPPORT-RANK REPRODUCIBILITY:            FIXED
ONISHI–FU LITERATURE POSITIONING:        FIXED
PARAMETER-SENSITIVITY REQUEST:           ADDRESSED
APPENDIX B1 DERIVATION:                  FIXED
PRB COMPILE QA:                          PASS
ALL-PAGE VISUAL QA:                      PASS
READY FOR FINAL ADVERSARIAL/SUBMISSION:  YES
```
