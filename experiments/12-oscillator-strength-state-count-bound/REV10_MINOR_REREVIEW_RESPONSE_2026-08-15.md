# Experiment 12 — Rev10 minor rereview response

**Date:** 2026-08-15  
**Branch:** `experiment-12-oscillator-strength-state-count-bound`  
**Disposition:** **MINOR REREVIEW ADDRESSED / CENTRAL EQ. (29) UNCHANGED / REV11 READY FOR TYPESET QA**

## Trigger

A focused adversarial rereview of `experiment12_prb_rev10_referee_repaired` concluded that the Rev9 `sup`/`ess sup` objection is correctly repaired and no longer identified a major technical defect. The remaining requests were:

1. explicitly connect the bulk k-resolved Eq. (49) to the complete exact-energy-shell definition in Eq. (21);
2. state the numerical singular-value criterion used for the active-support rank and test its stability;
3. cite and distinguish Onishi and Fu, Phys. Rev. X 14, 011052 (2024);
4. preferably add a lightweight HgCdTe parameter-sensitivity check;
5. optionally show the one-line proof of Appendix B1 and avoid unnecessary further defensive expansion.

## 1. Eq. (49) direct-sum clarification — accepted

The manuscript now states explicitly that in a finite periodic normalization volume the homogeneous velocity operator preserves crystal momentum. Therefore a complete exact-energy shell decomposes as

```math
P_\epsilon v_xQ_{\epsilon,B}
=\bigoplus_{\mathbf k}
P_{\epsilon,\mathbf k}v_x(\mathbf k)Q_{\epsilon,\mathbf k,B}.
```

The operator norm of the complete shell is the maximum of the finite-k block norms, becoming the ordinary supremum in the bulk limit. This directly justifies Eq. (49) as the translationally invariant specialization of Eq. (21).

No theorem change is required.

## 2. Support-rank numerical criterion — accepted and stability-tested

The exact theorem uses mathematical rank. The Rev10 numerical audit already implemented the floating-point diagnostic with

```text
rank threshold = 1e-6 m/s
```

but the manuscript did not report it.

Rev11 states this threshold explicitly and emphasizes that it affects only the Table-II active-support decomposition, not the central population lower bound.

A reduced-grid stability audit gives

```text
40 x 6 x 8 broad-window audit grid

rank threshold (m/s)     n_B^act / n_ref
1e-9                     0.660512373
1e-6                     0.660512373
1e-3                     0.660512373
1                        0.660512373
1e2                      0.660512373
1e4                      0.660512373
```

Thus the diagnostic support fraction is unchanged across 13 orders of magnitude in the threshold on that audit grid. The production-grid Table-II value remains `~0.669`.

## 3. Onishi–Fu literature positioning — accepted

Primary source checked:

```text
Y. Onishi and L. Fu,
"Fundamental Bound on Topological Gap,"
Phys. Rev. X 14, 011052 (2024),
DOI 10.1103/PhysRevX.14.011052.
```

The paper connects generalized optical weight to topology, quantum geometry, and an upper bound on the topological gap, with applications including infrared absorption near topological band inversion.

Rev11 cites it in the optical-sum-rule discussion and states the distinction explicitly:

```text
Onishi–Fu: generalized optical weight / topology / quantum geometry / gap bound.
Experiment 12: finite-temperature cross-mu thermal population bound with
              E/[exp(E/2kBT)-1] kernel and per-shell velocity capacity.
```

This is neighboring literature, not an identified collision with Eq. (29).

## 4. Lightweight HgCdTe parameter sensitivity — added

A one-at-a-time sensitivity diagnostic perturbs

```text
EP, Delta, F, gamma1, gamma2, gamma3
```

by `+/-5%`, re-solving charge neutrality and the broad-window optical problem for every case. The diagnostic uses a common reduced `24 x 4 x 6` quadrature and a continuous projected-block capacity search.

Results:

```text
reduced-grid baseline ratio = 0.1226
perturbed ratio range       = 0.1098 ... 0.1293
relative range              = approximately -10.5% ... +5.5%
```

This is deliberately **not** presented as experimental parameter uncertainty or as a replacement for the production `0.1175` result. It establishes only that the order-`10^-1` conclusion survives modest independent perturbations of the representative remote-band parameters.

Reproducibility script:

`numerics/parameter_sensitivity_audit.py`

## 5. Appendix B1 proof — added

Using the `a,b` variables already defined in Eq. (7), Eq. (B1) reduces after multiplication by its positive denominator to

```math
[\sqrt a(1+b)-\sqrt b(1+a)]^2\ge0.
```

This is now stated directly in Appendix B.

## Presentation decision

No broad 10–15% compression pass was performed in this revision. The explanatory scaffolding was deliberately added at the user's request, and the rereview found the remaining presentation issue to be editorial rather than technical. Rev11 makes only the surgical additions above and remains 13 pages in standard PRB/REVTeX formatting.

## Scientific disposition

```text
CENTRAL EQ. (29):                 UNCHANGED / PASS
ORDINARY SUPREMUM REPAIR:        RETAINED
GAMMA CROSS-MU ANALYSIS:         RETAINED
K-RESOLVED / FULL-SHELL LINK:    CLARIFIED
SUPPORT-RANK NUMERICS:           DEFINED + STABILITY TESTED
ONISHI–FU POSITIONING:           ADDED
HGCDTE PARAMETER ROBUSTNESS:     DIAGNOSTIC ADDED
APPENDIX B1:                     ONE-LINE PROOF ADDED
NEW PRIORITY CLAIM:              NONE
```
