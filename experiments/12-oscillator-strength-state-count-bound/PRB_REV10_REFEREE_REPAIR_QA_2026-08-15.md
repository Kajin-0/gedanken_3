# Experiment 12 — PRB Rev10 referee-repair QA

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **FORMAL SUPREMUM REPAIR COMPLETE / CENTRAL THEOREM UNCHANGED / TYPESET QA PASS**

## Trigger

An extreme Rev9 adversarial rereview correctly identified that the finite-system theorem uses an ordinary supremum in Eqs. (21)–(22), whereas the HgCdTe bulk specialization had been written with an essential supremum in Eq. (49). The same rereview proposed an isolated-Gamma capacity correction that would lower the broad HgCdTe ratio from 0.118 to about 0.110.

The formal notation objection is valid. The proposed Gamma correction is not applicable to the actual cross-chemical-potential numerical state because the charge-neutral chemical potential lies 11.477 meV above the nominal Gamma6 edge. At k=0 the Gamma6 pair and Gamma8 manifold are all below mu, so there is no selected Gamma8-to-Gamma6 cross-mu block at Gamma.

Detailed resolution: `REV9_SUPREMUM_REREVIEW_RESOLUTION_2026-08-15.md`.

Reproducible audit code: `numerics/supremum_active_support_audit.py`.

## Rev10 scientific changes

The central analytical chain and Eq. (29) are unchanged.

Surgical repairs:

1. Eq. (49) now uses the **ordinary supremum** over the stated bounded momentum domain, matching Eqs. (21)–(22).
2. The HgCdTe text explicitly records why Gamma is not a selected cross-mu shell in the numerical state.
3. A continuous-parameter projected-block search gives `v_B^cap ~= 1.01764e6 m/s` for all four Table-II windows at the reported resolution.
4. The more precise broad-window ratio becomes `0.1175`; the manuscript-level headline remains `0.118` / `11.8%` after rounding.
5. The broad population lower bound becomes approximately `1.18e16 cm^-3`.
6. Eq. (48) now defines the energy-domain image `E_B={hbar omega: omega in B}` and applies the indicator to transition energy, removing the frequency/energy notation mismatch.
7. Production quadrature orders are stated explicitly: `160 x 10 x 16`; a `200 x 12 x 20` grid is reported as an additional support-population check.
8. Table II now decomposes tightness into `n_B^act/n_ref` and `n_bound/n_B^act`.
9. Broad-window decomposition: selected-support fraction `~0.669`; Fermi/capacity tightness within that support `~0.176`.
10. Continuous pairwise diagnostic is `~0.87165e6 m/s`; pairwise substitution would overstate the population bound by about `36.3%`.

## Exact source provenance

The full Rev9 exposition production source remains archived as

`typeset/experiment12_prb_rev9_exposition_revised.tex.gz.b64`.

The exact Rev10 source is reconstructed by applying

`typeset/rev9_exposition_to_rev10_referee_repaired.patch`

to that source. The resulting Rev10 TeX hash is:

```text
SHA-256 454a2ff8aba637d2e4c66ef5747899e85894996a020c633296cf950044c79b3d
```

Final PDF hash:

```text
SHA-256 31ec4dd408552318f21de3e6bc7366e1b87badd7721a21575250c73adbb59a54
```

## Typesetting

```text
REVTeX 4-2
APS / PRB / reprint
US letter
standard two-column journal typography
13 pages
```

The page count increases from 12 to 13 because the referee repair adds the explicit supremum explanation and the expanded Table II. Font size, equation sizing, margins, and column geometry were not compressed.

## Compile QA

Three `pdflatex` passes completed successfully.

```text
critical LaTeX/package/class warnings: none
overfull boxes:                      none
undefined references/citations:      none
unresolved/stuck floats:             none
```

## Structural QA

Verified in the final PDF:

```text
main numbered equations: (1) through (50)
appendix equations:       (A1), (B1)
tables:                   I, II, III
references:               18
sections:                 I-VIII + Appendices A/B
central Eq. (29):         unchanged
```

## Visual QA

All 13 pages were rendered at high resolution and inspected. In particular:

- page containing Eq. (48): clean;
- page containing revised Eq. (49) and Gamma discussion: clean;
- expanded full-width Table II: readable, no clipping or collision;
- Table III / bibliography transition: clean;
- final reference page: clean.

No broken glyphs, text/equation overlap, clipped equations, float collisions, or bibliography collisions were found.

## Final disposition

```text
CENTRAL THEOREM:                    PASS / UNCHANGED
SUP vs ESS SUP FORMAL ISSUE:       FIXED
PROPOSED GAMMA 11.0% CORRECTION:   NOT APPLICABLE
HGCDTE BROAD PRECISE RATIO:        ~0.1175
HEADLINE ROUNDED RATIO:             11.8%
EQ. (48) UNIT NOTATION:            FIXED
QUADRATURE REPRODUCIBILITY:        FIXED
TIGHTNESS DIAGNOSTIC:              ADDED
PRB COMPILE / VISUAL QA:           PASS
READY FOR NEXT ADVERSARIAL REVIEW: YES
```
