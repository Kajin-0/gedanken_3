# Experiment 12 — Progress-log addendum: Rev8

**Date:** 2026-08-15

## Rev7 extreme re-review

A second independent hostile review again found the central theorem mathematically sound and moved its disposition to moderate revision / close to submission quality.

The remaining formal issue was a hidden second quantifier in the low-energy moving-window limit. The main significance request was a full bound/exact comparison in the same realistic multiband HgCdTe model.

## Double-uniformity correction

For low-energy windows `B_m`, Rev8 now requires

```math
\sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty,
```

in addition to shrinking transition energies and nonzero limiting integrated spectral weight.

This yields a rigorous positive liminf population floor. The finite-volume theorem itself is unchanged.

## Second-order eight-band calculation

The first-order Kane model is insufficient for a finite-temperature bulk carrier-density test because of its ideal flat heavy-hole branch.

A full population/optical calculation was therefore implemented using the bulk constant-parameter second-order eight-band Hamiltonian of Novik et al. on a bounded momentum domain.

Representative target:

```text
T=300 K
Eg=0.123984198 eV
x=0.179727548
```

Charge-neutral state:

```text
mu-Ec = +11.477 meV
cross-mu exact population = 1.005141e17 cm^-3
```

Broad low-energy validation window:

```text
Eg <= Ecv <= 0.5 eV
v_B^cap ~= 1.016e6 m/s
n_bound ~= 1.186e16 cm^-3
bound/exact ~= 0.1180
```

The bound is substantially looser than the ideal symmetric/Dirac checks but remains order `10^-1`.

Reproducibility:

`numerics/kane_8band_tightness.py`

Controlling note:

`HGCDTE_SECOND_ORDER_8BAND_TIGHTNESS_2026-08-15.md`

## Rev8 manuscript

Rev8 adds the full second-order validation, corrects first-order upper-bound wording, restricts higher-order k.p claims to bounded momentum domains, and shifts the Appendix-A internal-absorptance window above the exact edge.

Production state:

```text
8 pages
warning-free REVTeX compile
US-letter PDF
PDF preflight pass
all pages visually inspected
```

Hashes:

```text
Rev8 TeX: 18424af7052262b2974a94a5ed6f85495951674fdcc0333624f3426f635df3a9
Rev8 PDF: 36e3fa7c01053bd5ec20f235cbb3f4f99c5297c3d44f11845440f77dff1da402
```

## Current disposition

```text
CENTRAL THEOREM: SURVIVES
REALISTIC MULTIBAND FULL TEST: COMPLETE
REV8 RENDER QA: PASS
NOVELTY: NOT ESTABLISHED
NEXT: EXTREME ADVERSARIAL REVIEW OF REV8
```