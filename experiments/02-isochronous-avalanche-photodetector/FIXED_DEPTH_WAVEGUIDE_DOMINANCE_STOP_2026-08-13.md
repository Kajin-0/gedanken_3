# Fixed-depth waveguide dominance stop

**Date:** 2026-08-13  
**Status:** NEGATIVE RESULT / CURRENT ISOCHRONOUS DEPTH-MAP DEVICE PATH CLOSED AS A PUBLICATION PATH / EXACT COMPENSATION IDENTITY RETAINED / NOVELTY NOT ESTABLISHED

## 1. Why this stop was necessary

Experiment 02 progressively moved from a direct-illumination APD thought experiment to a waveguide/common-output implementation. Once a waveguide and distributed electrical readout are allowed, a stronger comparator becomes mandatory:

> Why correlate longitudinal optical delay with transverse absorption depth at all, instead of localizing absorption at one shallow timing depth and handling longitudinal propagation independently?

That comparator dominates the present timing objective under the same reduced-order assumptions.

## 2. Separable comparator

Let a short-pulse detector timestamp be

```math
T=t_o(X)+t_e(X)+t_c(Z)+\epsilon.
```

The proposed transverse-depth map correlates `X` and `Z` so that the first three mean-delay terms cancel.

A separable waveguide detector can instead do two independent things:

1. confine absorption to a fixed narrow depth distribution near the multiplication region, so `t_c(Z)` has small mean and variance;
2. make the longitudinal optical length short enough that `t_o(X)` is negligible, or use established traveling-wave electrical velocity matching so `t_o(X)+t_e(X)` is approximately constant.

No transverse depth migration is then required.

This is not a new theorem or metric. It is the correct strong engineering control once waveguide geometry is admitted.

## 3. Quantitative dominance on the existing benchmark

Keep the Experiment-02 scale

```text
d=2 um
v_c=5e4 m/s
v_g=7.5e7 m/s
Pe=100
avalanche RMS=5 ps
electronics RMS=2 ps
optical RMS=1 ps
```

and the historical direct-control RMS

```text
12.6454 ps.
```

The historical 30% gate is therefore

```text
8.8518 ps RMS.
```

Consider one fixed `200 nm` absorbing sheet adjacent to the multiplication side. For uniform generation across the sheet,

```math
\sigma_z=t_s/\sqrt{12}=57.7\ \mathrm{nm},
```

and the mean carrier path is approximately `100 nm` in the first constant-drift surrogate.

With **no electrical velocity matching at all**, a 40-um longitudinal absorption length gives

```text
fixed-depth waveguide RMS ~5.740 ps
improvement vs historical direct control ~54.6%.
```

The longitudinal optical-delay contribution is only about `0.136 ps RMS` at this length.

Under the same model the fixed 200-nm sheet continues to clear the 30% gate until the absorption length reaches approximately

```text
L ~1.98 mm
```

before any traveling-wave electrical cancellation is invoked.

At `L=40 um`, an additional independent stochastic interface/readout term of about

```text
6.74 ps RMS
```

could be added before the historical 30% gate is lost.

This margin is far larger than the approximately few-picosecond aggregate interface budgets found for the multi-sheet mapped architecture.

Companion calculation: `numerics/fixed_depth_waveguide_dominance.py`.

## 4. Even the broad dielectric-mode comparator wins

The first symmetric-slab optical surrogate for an ordinary III-V dielectric guide used roughly

```text
n_core ~3.47
n_InP ~3.17
lambda=1.55 um.
```

Its best fundamental-mode intensity RMS was about

```text
sigma_z ~0.198 um.
```

That width was nearly fatal to the **three-state migrating** implementation: with the previous 2-ps readout floor, N=3 falls below the 30% target and N~5-6 plus approximately 98% state-transfer fidelity is needed to recover it.

But if the same approximately 0.198-um localization is simply held at one depth near the multiplication region, a conservative `0.2 um` mean carrier path and `40 um` optical length give about

```text
7.0 ps RMS
```

under the same reduced-order stochastic assumptions, still comfortably beyond the 30% gate.

Thus increasing the number of migrating optical states is the wrong rescue path for the current timing objective.

## 5. Why this is established engineering territory

The relevant ingredients are not speculative:

- Shishikura et al., *Integrated Photonics Research* (1995), DOI `10.1364/IPR.1995.IThA2`, explicitly state that in a waveguide APD the quantum-efficiency/bandwidth tradeoff is relaxed because incident light and photogenerated carriers travel in different directions.
- Shiba et al., *J. Lightwave Technol.* 29, 153-161 (2011), demonstrated InP/InGaAs waveguide APDs designed for simultaneous high speed and high responsivity, with >20-GHz bandwidth up to gain 7 and 0.75 A/W responsivity at 1.55 um.
- Shi, Liu & Liu, *J. Lightwave Technol.* 22, 1583-1590 (2004), DOI `10.1109/JLT.2004.829230`, modeled traveling-wave APDs including distributed optical generation, carrier transport/multiplication, microwave loss, reflection, and optical/electrical velocity mismatch.
- US5270532A (1993) already discloses a traveling-wave photodetector using a very thin InGaAs absorbing layer, distributed absorption, and RF/optical velocity synchronism. It is not an APD timing paper, but it makes the thin-absorber + distributed-absorption + velocity-match combination especially important prior art.
- Hole trapping at InGaAs/InP heterointerfaces and its mitigation with graded/quaternary transition layers are established APD transport physics; see Tsuchiya, Ogawa & Miyoshi, *Integrated Photonics Research* (1991).

These references do **not** prove that the exact transverse-depth compensation map was previously published. They do show that the simpler engineering route needed to defeat the present motivation is established.

## 6. Scientific disposition

The exact conditional-mean identity remains correct:

```math
m(X)=constant
```

removes the position-dependent mean term, and a transverse depth map can mathematically realize that condition.

However, for the APD/SPAD timing problem as currently posed, the implementation is dominated by a simpler separable architecture:

```text
fixed shallow absorption depth
+
waveguide absorption length
+
(optional) ordinary traveling-wave velocity matching.
```

The correlated depth map adds state-transfer accuracy, multiple depth states, or multiple heterointerfaces without establishing a timing advantage over that strong comparator.

Therefore:

```text
Experiment-02 exact timing identity: RETAIN
transverse-depth map as pedagogical/device possibility: RETAIN
current APD/SPAD device path as publication claim: CLOSE
full Maxwell/TCAD optimization of the migrating map: DO NOT PURSUE BY DEFAULT
novelty/priority claim: NOT AUTHORIZED
```

## 7. Reopen conditions

Only reopen this path if a new physical constraint is introduced that defeats the separable comparator, for example:

1. a thick absorption volume is itself mandatory for a resource other than quantum efficiency (e.g. saturation/power/energy handling), so a thin fixed-depth absorber is not allowed;
2. longitudinal absorption must remain multi-millimeter and electrical velocity matching is unavailable by construction;
3. the detector must provide one passive position-blind timestamp with no distributed electrical compensation, and that restriction is physically motivated rather than imposed to protect the hypothesis;
4. a material system is found where fixed-depth waveguide localization is intrinsically impossible but controlled depth migration is practical.

Without such a constraint, further optimization would be engineering a more complicated solution to a problem already removed by waveguide geometry.
