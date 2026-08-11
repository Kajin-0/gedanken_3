# Step 22 — Palm-Corrected Bandwidth Boundary Map and Survival of the Finite Optimum

**Date:** 2026-08-11 18:42 EDT  
**Status:** NUMERICAL VALIDATION / REFINEMENT / CONDITIONAL / OPEN. The Step-21 continuous upcrossing-Palm machinery is used to map representative points of the finite-`r` preference boundary in `(Lambda,kappa_f)` and to perform a higher-statistics Palm scan of the large-`r` full-template bandwidth objective from Step 19. Two conclusions survive: (1) the high-band slow-preferred region does **not** disappear entirely; Palm correction lifts the finite-`r` boundary above the old `Lambda=0.895` slice, so the second reversal on that slice disappears while slow-preferred tasks remain at larger timing uncertainty; (2) the Step-19 finite-bandwidth optimum survives the Palm correction as a shallow but statistically resolved finite maximum. The exact finite-`r` `kappa_f -> infinity` boundary remains open because finite-hard-window roughness and full-template convergence do not commute. No uniqueness or novelty claim.

---

## 1. Question

Step 21 invalidated the Step-20 high-band Rice switch at

```text
kappa_f ~=130.19
```

for the fixed slice

```text
Lambda=L/tau_f=0.895.
```

That did **not** answer two broader questions:

1. did Palm correction eliminate the high-band slow-preferred region itself, or merely move its boundary to larger `Lambda`?;
2. does the finite bandwidth optimum found in Step 19 remain after the exact continuous rare-event correction is used more systematically?

This step maps enough of the Palm boundary to distinguish those possibilities.

---

## 2. Boundary formulation

Retain the Step-20 fixed-physics finite-speed-ratio model

```math
r=\frac{\tau_s}{\tau_f},
\qquad
\kappa_s=r\kappa_f,
```

with fixed full-band eventual SNR `rho_full` and common physical readout bandwidth.

For a common physical decision time

```math
X=T/\tau_f,
```

the two dimensionless integration times are

```math
x_f=X,
\qquad
x_s=X/r.
```

For physical arrival uncertainty

```math
\Lambda=L/\tau_f,
```

the normalized search lengths are

```math
\ell_f=\Lambda,
\qquad
\ell_s=\Lambda/r.
```

For either detector define the available decision threshold

```math
\boxed{
u_{avail}(x,\kappa)
=\rho(x,\kappa)-\Phi^{-1}(\beta).}
```

The exact smooth-process false-alarm relation is

```math
P_{FA}
=Q(u)
+\ell\frac{\sigma(x,\kappa)}{2\pi}
 e^{-u^2/2}C_\uparrow,
```

where

```math
C_\uparrow
=E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right].
```

At a fast/slow preference boundary both detectors meet the same `(alpha,beta)` requirement at the same physical `X`.

If the locally measured Palm factors are held fixed during one deterministic update, the maximum admissible normalized search lengths are

```math
\ell_{Palm}
=
\frac{
2\pi[\alpha-Q(u)]e^{u^2/2}
}{\sigma C_\uparrow}.
```

The boundary update therefore solves

```math
\boxed{
\frac{\ell_{Rice,f}(X,\kappa_f)}{C_f}
=
r\frac{\ell_{Rice,s}(X/r,r\kappa_f)}{C_s}.
}
```

The resulting `Lambda` is

```math
\boxed{
\Lambda_\times
=\frac{\ell_{Rice,f}}{C_f}.
}
```

The Palm factors are then resampled at the displaced boundary and the process is iterated locally. This is the boundary-map analogue of the Step-21 local Palm switch correction.

---

## 3. Finite-r map used here

Use the same task as Steps 20–21:

```text
r        = 2
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90.
```

The previously validated horizontal-slice crossing remains

```math
\boxed{
\Lambda=0.895
\quad\Rightarrow\quad
\kappa_{\times}^{Palm}\approx21.7\pm0.3.
}
```

Representative Palm-corrected boundary points from local iterative solves are:

```text
kappa_f     Lambda_cross^Palm      numerical status
----------------------------------------------------
~10         ~0.794                 exploratory Palm map
~20         ~0.891                 exploratory Palm map
21.7        0.895                  Step-21 validated crossing
30          ~0.9052                8000-path local map
60          ~0.9098                8000-path local map
100         ~0.9103                8000-path local map
200         ~0.9099                10000-path local map
```

The pointwise Palm-factor uncertainties and the local fixed-factor iteration make the last digits less meaningful than the overall shape. The accepted structure is:

```text
low bandwidth:
    boundary rises rapidly as fast-channel accessible SNR is recovered

moderate bandwidth:
    boundary reaches approximately 0.91

high tested bandwidth:
    boundary remains near 0.91 instead of dropping below 0.895
```

---

## 4. High-band slow-preferred region survives

Step 21 showed that, at `Lambda=0.895`, the fast detector remains preferred at Palm-checked `kappa_f=130`, `160`, and `300`.

The boundary map now explains why.

At approximately

```text
kappa_f=200
```

the Palm boundary is

```math
\boxed{
\Lambda_\times^{Palm}\approx0.910.
}
```

Thus the old horizontal slice

```text
Lambda=0.895
```

lies **below** the corrected boundary and stays fast-preferred.

But tasks with slightly larger unknown-arrival interval, on the opposite side of the tracked boundary, remain slow-preferred.

Therefore:

```math
\boxed{
\text{Palm correction removes the Step-20 second crossing at }
\Lambda=0.895,
\text{ but it does not eliminate the high-band slow-preferred region.}
}
```

**REFINEMENT:** Step 21 changed the location and topology of one horizontal task slice; it did not destroy the slow-preferred side of the two-dimensional task boundary.

---

## 5. Why the corrected high-band boundary is lifted

At large finite `kappa`, finite hard-window Rice theory increasingly counts micro-upcrossings inside the same rough excursion.

The slow detector near the old high-band Rice crossing uses the shorter dimensionless window and consequently has the larger hard-window endpoint/roughness coefficient. Its Rice overcount is therefore stronger:

```text
C_s << C_f
```

at high bandwidth.

Since the exact admissible search length contains

```math
\ell_{Palm}=\ell_{Rice}/C_\uparrow,
```

the much smaller slow-channel Palm factor lifts the physical fast/slow boundary to larger `Lambda`.

That is why the Step-20 Rice boundary fell through `Lambda=0.895` while the Palm boundary remains above it.

---

## 6. Large-r full-template Palm boundary

The Step-19 bandwidth optimum is cleanest in the large-speed-ratio limit, where the fast detector is using its full accessible template.

For the full template

```math
H_\infty(\nu)=\frac1{(1+i\nu)^2},
```

the fixed-physics accessible SNR is

```math
\rho_\infty(\kappa)
=\rho_{full}\sqrt{F(\kappa)},
```

and the Rice feasibility length is

```math
\ell_{crit}^{Rice}(\kappa)
=
\frac{
2\pi[\alpha-Q(u(\kappa))]e^{u(\kappa)^2/2}
}{\sigma_\infty(\kappa)}.
```

The continuous Palm correction gives

```math
\boxed{
\ell_{crit}^{Palm}(\kappa)
=\frac{\ell_{crit}^{Rice}(\kappa)}{C_\uparrow(\kappa)}
}
```

with the Palm factor evaluated self-consistently at the corresponding search length.

Because the full template is smooth even when the Gaussian bandwidth penalty is removed, this large-`r` scan does not inherit the finite-hard-window singularity.

---

## 7. Higher-statistics Palm scan of the Step-19 optimum

For the Step-19 calibration

```text
rho_full ~=6.2407571
alpha    =1e-6
beta     =0.90
```

higher-statistics full-template Palm calculations give representative values

```text
kappa       ell_crit^Palm
-------------------------
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

At `kappa=60`, independent `20000`-path runs gave approximately

```text
0.91198 +/-0.00062
0.91202 +/-0.00062
```

and a separate `30000`-path run gave approximately

```text
0.91234 +/-0.00052.
```

At infinite information bandwidth, a `30000`-path run gave approximately

```text
0.90897 +/-0.00063.
```

The finite-minus-infinite difference is therefore roughly

```math
\boxed{
\Delta\ell_{crit}^{Palm}
\sim3\times10^{-3},
}
```

or about

```text
0.3–0.4%
```

of the infinite-band boundary, resolved at several combined standard errors in the repeated runs.

The Palm-corrected maximum is shallow; the exact maximizer cannot be distinguished more finely than roughly

```math
\boxed{
\kappa_{opt}^{Palm}\sim50\text{–}65
}
```

with the present Monte Carlo precision.

---

## 8. Step-19 optimum survives, but is smaller and broader

Step 19's Rice result was

```text
kappa_opt^Rice ~=42.23
relative gain over infinity ~=1.32%.
```

The higher-statistics Palm scan changes the quantitative conclusion:

```text
Palm optimum region: roughly kappa ~50–65
Palm gain over infinity: roughly 0.3–0.4%
```

but preserves the qualitative one:

```math
\boxed{
\max_{0<\kappa<\infty}
\ell_{crit}^{Palm}(\kappa)
>
\ell_{crit}^{Palm}(\infty).
}
```

**NUMERICAL VALIDATION / CONDITIONAL:** the finite readout-bandwidth optimum is not a Rice artifact. Palm correction makes the optimum shallower and shifts/broadens its location, but a finite band remains better than the infinite-band endpoint for this large-`r` unknown-time objective.

No uniqueness claim is made.

---

## 9. Corrected two-dimensional picture

For the `r=2` fixed-physics example, the current Palm-supported picture is:

```text
small kappa_f:
    slow detector feasible/preferred first

lower boundary crossing:
    Lambda=0.895 crosses near kappa_f ~21.7

moderate/high tested kappa_f:
    fast-preferred region extends up to Lambda ~0.91

above that boundary:
    slow-preferred tasks still exist
```

Thus the two-dimensional boundary is nontrivial even though the particular Step-20 horizontal slice has only one validated crossing.

The Step-20 `slow -> fast -> slow` sequence was a false one-dimensional topology generated by Rice overcount. The surviving Palm geometry is instead a boundary that is lifted and flattened at high bandwidth.

---

## 10. What remains open

The present map is sufficient to answer the two Step-21 questions, but it is not a global finite-`r` theorem.

### ESTABLISHED / NUMERICALLY SUPPORTED

- The high-band slow-preferred region does **not** disappear entirely after Palm correction.
- The old `Lambda=0.895` second crossing disappears because the Palm boundary is lifted to about `Lambda~0.91` in the tested high-band range.
- The large-`r` Step-19 finite bandwidth optimum survives continuous Palm correction.
- The Palm optimum is shallower than Rice suggested and lies broadly near `kappa~50–65` for the calibration used here.

### OPEN

- The exact finite-`r` limit of `Lambda_cross(kappa_f)` as `kappa_f -> infinity`.
- A proof of whether the finite-`r` Palm boundary has one maximum, several extrema, or a plateau.
- A proof excluding additional horizontal-slice reversals at other `Lambda` values.
- Exact finite-alpha control of the noncommuting finite-window rough and full-template limits.
- Hardware interpretation of the Gaussian information-band parameter.
- Novelty.

---

## 11. First nontrivial consequence

**REFINEMENT:** Palm correction does not simply erase the high-band timing-search tradeoff. It changes the geometry.

For the finite-`r` example, it removes a spurious second crossing of one horizontal task slice by lifting the high-band boundary. At the same time, a genuine finite-band optimum remains in the large-`r` full-template boundary.

So the surviving statement is not

```text
more bandwidth eventually makes the slow detector win at Lambda=0.895,
```

but rather

```text
bandwidth reshapes the task boundary, and there remains a finite bandwidth at which the tolerable unknown-arrival interval is maximized.
```

---

## 12. Stopping point

The finite-r Palm boundary has been mapped well enough to distinguish a shifted high-band slow region from its disappearance, and the large-r finite-bandwidth optimum has been validated beyond Rice.

### Single natural next question

> Can the high-band finite-r Palm boundary be derived asymptotically by matching the finite-hard-window rough excursion law to the smooth full-template limit, so that the `kappa_f -> infinity` boundary and the possibility of any additional reversals can be settled analytically rather than by Monte Carlo mapping?
