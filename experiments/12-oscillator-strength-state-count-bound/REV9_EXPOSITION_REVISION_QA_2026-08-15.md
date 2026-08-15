# Experiment 12 — Rev9 exposition-revision scientific invariance QA

**Date:** 2026-08-15  
**Source:** exact QA-passed `experiment12_prb_rev9.pdf` recovered from the user Library  
**Revised manuscript:** `MANUSCRIPT_REV9_EXPOSITION_REVISED_2026-08-15.md`  
**Disposition:** **PASS — EXPOSITION CHANGED / SCIENTIFIC CONTENT RETAINED**

## 1. Structural invariants

Verified against the exact nine-page Rev9 PDF:

```text
main-text numbered equations retained: (1) through (50)
appendix equations retained:            (A1), (B1)
validation tables retained:             Tables I, II, III
references retained:                    18, same order and DOI metadata
main section sequence retained:          I through VIII + Appendices A/B
paper title retained:                    yes
```

The revision adds explanatory prose around the formal objects and derivations but does not delete any numbered equation from Rev9.

## 2. Central theorem and hypotheses

Retained exactly in mathematical content:

```math
n_e+n_h
\ge n_{e,B}^{act}+n_{h,B}^{act}
\ge
\frac{2}{\pi e^2(v_B^{cap})^2}
\int_B
\frac{\hbar\omega\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

Retained qualifications:

```text
finite-system inequalities are exact before the thermodynamic limit;
macroscopic density-floor language requires limsup_{V->infinity} v_B,V^cap < infinity;
the low-energy moving-window statement requires a second uniformity over the window sequence;
nonvanishing integrated cross-mu spectral weight is required;
peak conductivity alone is insufficient when useful bandwidth can vanish.
```

## 3. Rev9-specific corrections preserved

The exposition revision explicitly retains the two corrections that motivated Rev9:

### Intrinsic-gap corollary

`n_e=n_h=n_th` is used only for an intrinsic neutral semiconductor whose chemical potential lies in a gap so that the lower/upper-mu partition coincides with the valence/conduction manifolds.

The manuscript explicitly says Eq. (29), not Eq. (30), is the general theorem when `mu` lies inside a nominal band.

### Projected-block capacity

The second-order HgCdTe calculation retains the theorem capacity as the essential supremum of the largest singular values of the full projected shell blocks. It is explicitly distinguished from a pairwise `max |v_cv|`.

## 4. Pointwise and low-energy mathematics

Preserved:

```text
exact Fermi occupation definitions;
AM-GM derivation of Eq. (9);
mirror-symmetry equality condition Eq. (10);
Kubo-Greenwood cross-mu conductivity normalization;
thermal kernel K_T(E)=E/[exp(E/2kBT)-1];
trace <= operator-norm^2 x rank inequality;
active support-rank population definitions;
K_T(E)=2kBT-E/2+O(E^2/kBT);
E_m -> 0;
W_m -> W_0 > 0;
v_* finite uniformly over thermodynamic and moving-window limits;
positive liminf floor in Eq. (35).
```

No low-energy conclusion is stated from `E_g -> 0` alone.

## 5. Equality and model-validation invariants

### Parabolic family

Retained:

```text
equal-mass mirror-symmetric active-subspace saturation for every selected direct window;
total-population saturation only when the full relevant direct spectrum is selected;
explicit warning that the unbounded parabolic/constant-matrix-element construction is not claimed as a UV-complete semiconductor Hamiltonian;
unequal-mass nondegenerate ratio [4 m_e m_h/(m_e+m_h)^2]^(3/4);
finite-temperature ratios 0.9161, 0.6455, 0.4379 for mass ratios 2, 5, 10.
```

### Dirac family

Retained:

```text
2-D massless Dirac bound/exact = 0.5000;
3-D massless Dirac bound/exact = 0.6667;
3-D massive Dirac bound/exact = 0.794684 at 2 Delta/kBT = 4.7959;
Table-I values unchanged.
```

### First-order HgCdTe Kane capacity

Retained:

```text
||v_x||_op = sqrt(3/2) v_K;
v_B^cap <= sqrt(3/2) v_K;
v_B^cap <= P/hbar = sqrt(E_P/2m0);
measured v_K = (1.07 +/- 0.05)e6 m/s;
first-order central capacity upper-bound scale ~1.31e6 m/s;
E_P = 18.8 eV -> 1.286e6 m/s;
first-order coefficient not claimed for higher-order k.p velocity terms.
```

### Second-order HgCdTe test

Retained numerical/model qualifications:

```text
T = 300 K;
Eg = 0.123984 eV;
x = 0.17973;
Delta = 1.04945 eV;
F = -0.01618;
gamma1 = 3.6273;
gamma2 = 0.3598;
gamma3 = 1.0717;
EP = 18.8 eV;
carrier domain |k| <= 2.0 nm^-1;
charge-neutral mu ~11.5 meV above nominal Gamma6 edge;
cross-mu reference = 1.005e17 cm^-3;
conventional e+h = 1.010e17 cm^-3;
difference ~0.5%;
Gauss-Legendre k and cos(theta), uniform azimuth;
production degeneracy tolerance = 1e-7 eV.
```

Table II retained:

```text
Eg..1.5Eg : vcap 1.017e6 m/s, ratio 0.0320, ksel,max 0.149 nm^-1
Eg..2Eg   : vcap 1.017e6 m/s, ratio 0.0749, ksel,max 0.240 nm^-1
Eg..3Eg   : vcap 1.015e6 m/s, ratio 0.1110, ksel,max 0.415 nm^-1
Eg..0.5eV : vcap 1.016e6 m/s, ratio 0.1180, ksel,max 0.583 nm^-1
```

Retained diagnostics:

```text
broad-window projected-block singular value = 1.0156e6 m/s;
largest pairwise element = 0.8681e6 m/s;
pairwise substitution would overstate bound by ~37%;
degeneracy tolerance 1e-10..1e-5 eV leaves capacity unchanged to reported precision;
selected broad-window k <= 0.583 nm^-1;
Gamma8-derived -> Gamma6-derived selected transitions;
Gamma7-derived split-off pair excluded over sampled domain;
carrier cutoff 1.5 -> 2.0 nm^-1 changes reference by <1%;
quadrature/domain variations change broad ratio at few-1e-4 level;
0.5-eV interval remains explicitly a model-validation window, not detector bandwidth;
no arbitrary-k validity claim for the k.p continuum model.
```

## 6. Scope and nonclaims

All Rev9 escape routes remain present:

```text
neutral excitons / collective states;
phonon-assisted indirect transitions;
interaction-generated many-body spectral functions;
localization versus terminal current;
finite-bandwidth-noise kinetics;
photonic path enhancement;
measured total conductivity versus isolated sigma_1^cross;
rank discontinuity / non-robust participation-count interpretation;
vanishing useful bandwidth.
```

Explicit nonclaims retained or made more visible:

```text
no universal dark-current floor;
no universal D* limit;
no universal thermal-generation-rate limit;
no universal finite-bandwidth-noise floor;
no claim that small band gap alone forces large carrier density;
no claim that every optical absorber pays the free-quasiparticle population cost;
no claim that real HgCdTe exactly realizes Appendix A;
no novelty or priority claim.
```

## 7. Appendix invariants

Appendix A retains:

```text
weak-loss alpha ~ sigma_1^cross/(n_b epsilon_0 c);
300 K, 10 um, n_b=3.5;
internal A_int >= 0.90;
window [1.02 omega_g, 1.10 omega_g];
ideal AR/index-matched entrance assumption;
Fresnel entrance loss excluded;
intrinsic-gap use of Eq. (30);
Table-III columns unchanged;
first-order Kane illustrative lower column 4.19e11 cm^-2;
photonic path-enhancement caveat.
```

Appendix B retains Eq. (B1) and the explicit statement that the variance result is frequency integrated and does not imply a finite-bandwidth noise bound without kinetics.

## 8. Exposition changes intentionally introduced

Only scaffolding was added:

```text
plain-language physical gloss before new formal objects;
"why this step" transitions before derivation stages;
one-sentence physical restatements after major equations;
shorter sentences where Rev9 stacked several qualifiers;
equal-mass mirror-symmetric parabolic model introduced in the Introduction and threaded through Sections II-IV as an intuition anchor;
additional plain statements distinguishing what a theorem statement does and does not imply.
```

No additional mechanism, detector-performance theorem, or novelty claim was introduced.

## Final disposition

```text
SCIENTIFIC INVARIANCE: PASS
REV9-SPECIFIC CORRECTIONS: PASS
EQUATION/REFERENCE RETENTION: PASS
EXPOSITION REQUEST: IMPLEMENTED
NEXT: reader/referee-style clarity reread of the revised manuscript; no new science by default
```
