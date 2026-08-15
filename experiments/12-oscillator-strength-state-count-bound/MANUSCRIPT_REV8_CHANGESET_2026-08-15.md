# Experiment 12 — PRB Rev8 scientific changeset

**Date:** 2026-08-15  
**Base:** QA-passed local PRB Rev7  
**Target:** PRB Rev8  
**Scope:** targeted response to Rev7 external re-review; no change to central finite-volume theorem

## Controlling local artifacts

```text
experiment12_prb_rev8.tex
SHA-256 18424af7052262b2974a94a5ed6f85495951674fdcc0333624f3426f635df3a9

experiment12_prb_rev8.pdf
SHA-256 36e3fa7c01053bd5ec20f235cbb3f4f99c5297c3d44f11845440f77dff1da402

kane_8band_tightness_rev8.py
SHA-256 805a1f501c6c7ed60a5751064189f65085d0f7881d06f0d7601aec057827c8bf
```

The repository copy of the reproducibility script is

`numerics/kane_8band_tightness.py`.

## Scientific changes from Rev7

### 1. Low-energy double uniformity

Rev8 replaces the informal moving-window statement by the explicit sequence conditions

```math
E_m=\sup_{\omega\in B_m}\hbar\omega\to0,
```

```math
W_m=\int_{B_m}\sigma_1^{cross}(\omega)d\omega\to W_0>0,
```

and

```math
\boxed{
v_*=
\sup_m\left[\limsup_{V\to\infty}v_{B_m,V}^{cap}\right]<\infty.
}
```

The low-energy conclusion is now the rigorous liminf bound

```math
\boxed{
\liminf_{m\to\infty}
(n_{e,B_m}^{act}+n_{h,B_m}^{act})
\ge
\frac{4k_BT}{\pi e^2v_*^2}W_0>0.
}
```

### 2. First-order Kane resource wording

The `sqrt(3/2) v_K` result is now described only as a first-order global microscopic **upper bound**, not as the actual selected-window capacity.

### 3. Second-order k.p scope

The manuscript now states that higher-order k-dependent velocities remain finite only on a finite spectral window inside a **bounded momentum domain where the k.p expansion is being used**.

### 4. Full second-order HgCdTe-like tightness validation

New subsection:

`Second-order HgCdTe bound/exact test`.

The calculation uses the bulk constant-parameter second-order eight-band Hamiltonian of Novik et al. with a representative 300-K, 10-um HgCdTe-like parameter interpolation.

Headline result:

```math
(n_e+n_h)_{exact}=1.005\times10^{17}\ \mathrm{cm^{-3}},
```

and for `Eg <= E_cv <= 0.5 eV`,

```math
v_B^{cap}\simeq1.02\times10^6\ \mathrm{m/s},
```

```math
(n_e+n_h)_{bound}\simeq1.19\times10^{16}\ \mathrm{cm^{-3}},
```

```math
\boxed{(n_e+n_h)_{bound}/(n_e+n_h)_{exact}\simeq0.118.}
```

A four-row table records the tightening as the selected upper transition energy increases:

```text
Eg..1.5Eg : 0.0320
Eg..2Eg   : 0.0749
Eg..3Eg   : 0.1110
Eg..0.5eV : 0.1180
```

The broad `0.5 eV` interval is explicitly called a model-validation window, not a detector bandwidth.

### 5. Appendix-A edge specification

The illustrative internal-absorptance window is shifted from

```text
[omega_g, 1.10 omega_g]
```

to

```text
[1.02 omega_g, 1.10 omega_g].
```

All column bounds are recomputed. The first-order HgCdTe capacity upper bound gives a conservative illustrative lower column of

```text
4.19e11 cm^-2.
```

### 6. References

Added:

```text
E. G. Novik et al., Phys. Rev. B 72, 035321 (2005).
J. P. Laurenti et al., J. Appl. Phys. 67, 6454 (1990).
```

## Claims intentionally unchanged

Rev8 does not claim a universal lower bound on

```text
dark current;
thermal generation rate;
D*;
finite-bandwidth detector noise.
```

It does not extend the theorem to

```text
bound excitons;
phonon-assisted transitions;
interacting many-body spectral functions;
unconstrained photonic path enhancement.
```

No `first`, `novel`, or priority language is authorized.

## Disposition

```text
REV8 SCIENTIFIC CHANGES: COMPLETE
CENTRAL THEOREM: UNCHANGED
REALISTIC MULTIBAND SIGNIFICANCE TEST: ADDED
NOVELTY: NOT ESTABLISHED
NEXT: INDEPENDENT HOSTILE REVIEW OF REV8
```