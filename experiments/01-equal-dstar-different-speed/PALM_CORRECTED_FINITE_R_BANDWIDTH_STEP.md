# Step 21 — Palm Correction of the Finite-r Bandwidth Reversals

**Date:** 2026-08-11 16:37 EDT  
**Status:** NUMERICAL VALIDATION / REFINEMENT / INVALIDATION / OPEN. The exact continuous upcrossing-Palm identity from Step 16 is applied to the finite-r fixed-physics bandwidth sweep from Step 20. The lower Rice reversal survives but shifts substantially downward in bandwidth. The reported upper Rice reversal near `kappa_f ~= 130.19` does not survive the Palm correction: at that bandwidth, and at wider tested bandwidths through `kappa_f=300`, the fast detector meets the global false-alarm requirement at physical times for which the slow detector does not. The specific Step-20 upper switch is therefore invalidated. A different unobserved high-band Palm reversal is not rigorously excluded; the tested finite-band points and the rough-limit high-threshold asymptote give no evidence for one. No novelty claim.

---

## 1. Question

Step 20 found, at the finite-duration Rice/Euler-characteristic level,

```math
\text{slow}\to\text{fast}\to\text{slow}
```

as one common physical readout bandwidth was increased for

```text
r        = 2
rho_full = 6.2407571
alpha    = 1e-6
beta     = 0.90
Lambda   = L/tau_f = 0.895.
```

The two Rice switch points were

```text
kappa_cross_1^Rice ~= 25.4898402
kappa_cross_2^Rice ~=130.1945883.
```

Step 17 already warned that Rice accuracy is nonuniform at large finite-window `kappa`. The present step asks whether the two reversals survive the exact continuous Palm correction.

---

## 2. Exact decision criterion used for the Palm solve

For a candidate dimensionless integration duration `x`, the target detection probability `beta` fixes the largest admissible global threshold directly:

```math
\boxed{
u_{avail}(x)=\rho(x)-\Phi^{-1}(\beta).}
```

Therefore there is no need to invert a noisy estimated threshold inside the outer detection-time solve.

The exact smooth-process decision condition is simply

```math
\boxed{
P_{FA}^{Palm}\!\left(u_{avail}(x)\right)\le\alpha.
}
```

Using Step 16,

```math
P_{FA}^{Palm}(u)
=Q(u)
+\ell\frac{\sigma(x,\kappa)}{2\pi}
 e^{-u^2/2}
 C_\uparrow(x,\ell,\kappa,u),
```

where

```math
\boxed{
C_\uparrow
=E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
\le1.
}
```

The selected upcrossing is imposed continuously by Gaussian conditioning on

```math
z(T)=u,
\qquad
z'(T)>0,
```

with the Palm slope distribution

```math
z'(T)\sim\mathrm{Rayleigh}(\sigma).
```

Only the rare secondary-upcrossing and endpoint-overlap corrections are counted on a fine timing grid.

For a common physical decision time `X=T/tau_f`,

```math
x_f=X,
\qquad
x_s=X/r,
```

and

```math
\ell_f=\Lambda,
\qquad
\ell_s=\Lambda/r,
```

with

```math
\kappa_s=r\kappa_f.
```

A true preference switch requires both Palm false-alarm equations to equal `alpha` at the same physical `X`.

---

## 3. Lower switch — survives but moves downward

The lower Rice switch was

```text
kappa_cross_1^Rice ~= 25.4898402.
```

At a Palm-corrected candidate near

```text
kappa_f ~=21.47
X        ~=7.505,
```

a refined rare-event calculation gave approximately

```text
fast:
    C_up ~=0.99424 +/-0.00045
    x_f  ~=7.505

slow:
    C_up ~=0.95297 +/-0.00164
    x_s  ~=3.7525
```

with `20000` fast Palm paths and `12000` slow Palm paths.

Solving the two Palm-balance equations while holding those locally measured correction factors fixed gives

```text
kappa_cross_1 ~=21.80
X_cross       ~=7.5023.
```

A separate local-grid refinement from Palm correction spacing

```text
0.0025 -> 0.00125
```

at the displaced switch gave

```text
C_fast ~=0.9940
C_slow ~=0.95189
```

and inferred

```text
kappa_cross_1 ~=21.68.
```

The difference is smaller than the rare-event sampling sensitivity of the switch.

A conservative numerical summary is therefore

```math
\boxed{
\kappa_{\times,1}^{Palm}
\approx21.7\pm0.3.
}
```

Relative to Rice,

```text
shift ~= -15%.
```

**NUMERICAL VALIDATION / CONDITIONAL:** the first slow-to-fast reversal survives the continuous Palm correction, but Rice placed it substantially too high in bandwidth.

The large switch sensitivity comes mainly from the fast channel: its Palm factor is very close to one, but it lies near a feasibility edge, so a correction of only a few parts in `10^-3` can move the required bandwidth appreciably.

---

## 4. Upper Rice switch — direct Palm test invalidates it

The Step-20 upper Rice switch was

```text
kappa_cross_2^Rice ~=130.1945883.
```

At the Rice equality point the first Palm calculation already showed strongly unequal correction factors:

```text
fast C_up  ~0.985
slow C_up  ~0.76
```

because the slow finite window at

```text
kappa_s ~=260
```

contains many more high-level micro-upcrossings than Rice's first-moment count treats as independent excursions.

A cleaner test is to evaluate both detectors at the **same physical decision time** and ask directly whether each satisfies

```math
P_{FA}^{Palm}(u_{avail})\le10^{-6}.
```

At

```text
kappa_f = 130
X       = 7.0
```

the Palm estimates were

```text
fast: P_FA/alpha ~=0.9918 +/-0.0014
slow: P_FA/alpha ~=1.2668 +/-0.0079.
```

Thus the fast detector already satisfies the target while the slow detector does not.

At the later common time

```text
X = 7.5
```

the result remains

```text
fast: P_FA/alpha ~=0.9897 +/-0.0014
slow: P_FA/alpha ~=1.0444 +/-0.0060.
```

Therefore

```math
\boxed{
T_f<T_s
\quad\text{at }\kappa_f\approx130.
}
```

The Rice equality at `130.19` is not a Palm-corrected switch.

**INVALIDATED:** `kappa_cross_2^Rice ~=130.1945883` is not a valid continuous Palm switch value.

---

## 5. Wider-band stress checks

The same preference ordering persists at wider tested bandwidths.

### `kappa_f = 160`, common physical time `X=7.0`

```text
fast: P_FA/alpha ~=0.9903 +/-0.0017
slow: P_FA/alpha ~=1.2565 +/-0.0098.
```

Fast satisfies the task; slow does not.

### `kappa_f = 300`, common physical time `X=6.5`

```text
fast: P_FA/alpha ~=0.9950 +/-0.0029
slow: P_FA/alpha ~=1.7006 +/-0.0248.
```

Again fast satisfies the task while slow does not.

At `kappa_f=300`, the slow Palm ensemble has a very large multiple-upcrossing fraction, demonstrating directly why the finite-window Rice count is a poor approximation in this regime.

---

## 6. Why the high-band Rice reversal disappears

At finite hard-window duration, Step 17 showed

```math
\sigma_\kappa^2(x)
\sim
\frac{a_x}{\sqrt\pi}\kappa,
```

so Rice's expected number of smooth upcrossings diverges as `sqrt(kappa)` even though the probability of a distinct high excursion remains bounded.

The Palm factor must compensate:

```math
C_\uparrow\to0
```

along the rough-limit sequence.

The crucial finite-r detail is that, near the Step-20 upper switch, the **slow detector is using a much shorter dimensionless integration window** than the fast detector. Its hard-window endpoint is therefore much larger, giving it a substantially larger roughness coefficient `a_x` and a much stronger micro-upcrossing overcount.

Consequently Rice penalized the slow detector's high-band timing scan in a way that does not translate into distinct false-alarm excursions. Palm correction removes much of that artificial penalty.

This changes the Step-20 high-band competition qualitatively.

---

## 7. Rough-band high-threshold asymptote

For the ideal hard-window rough limit,

```math
R_x(y)=1-a_x|y|+o(|y|).
```

The standard high-threshold Pickands form for the local `alpha=1` Gaussian class gives the leading excursion contribution

```math
P_{FA}(u)
\approx
Q(u)
+\ell a_x u^2 Q(u).
```

Using this as a **high-threshold rough-limit asymptotic check**, the present task gives approximate detection times

```text
fast: T_f/tau_f ~3.37
slow: T_s/tau_f ~6.43.
```

Thus the wide-band asymptotic ordering is also fast-preferred by a large margin.

**ASYMPTOTIC / NOT AN EXACT finite-alpha result:** this supports the finite-k Palm trend but is not used as an exact proof for `alpha=1e-6`.

---

## 8. Corrected interpretation of Step 20

Step 20 correctly demonstrated that the **Rice approximation itself** can generate two bandwidth crossings, and the spectral quadrature of that Rice calculation was converged.

Step 21 shows that this was not enough to establish two physical continuous-Gaussian-process reversals.

The corrected status is:

```text
narrow band:
    slow preferred / slow feasible first

first Palm switch:
    kappa_f ~21.7 +/-0.3

intermediate through tested high band:
    fast preferred

reported Rice upper switch at 130.19:
    invalidated by Palm correction
```

Therefore the Step-20 statement

```math
\text{slow}\to\text{fast}\to\text{slow}
```

must **not** be carried forward as an exact continuous-process result.

The surviving directly validated topology is

```math
\boxed{
\text{slow}\to\text{fast}
}
```

through the tested Palm range `kappa_f <=300`.

---

## 9. What is and is not established

### ESTABLISHED / NUMERICALLY VALIDATED WITHIN THE SMOOTH PALM MODEL

- The lower Step-20 reversal survives.
- Its switch moves from Rice `~25.49` to Palm `~21.7 +/-0.3`.
- The specific Rice upper switch near `130.19` does not survive.
- Fast is preferred at Palm-checked points `kappa_f=130`, `160`, and `300`.
- The high-band Rice error is driven by clustered micro-upcrossings, especially in the shorter slow-detector finite window.

### INVALIDATED

- The Step-20 value `kappa_cross_2^Rice ~=130.1945883` as a physical continuous-Palm switch.
- Any statement that Step 20 already established two exact continuous-process reversals.

### OPEN

- A rigorous proof that **no other** high-band Palm reversal exists at any finite `kappa_f`.
- A complete Palm-corrected `(Lambda,kappa_f)` phase boundary.
- Exact continuum control of the `kappa -> infinity` rough limit at fixed finite `alpha`.
- Exact Palm optimization of the Step-19 finite bandwidth optimum.
- Any hardware interpretation of the Gaussian information-band parameter.
- Novelty.

---

## 10. First nontrivial consequence

**REFINEMENT / INVALIDATION:** a numerically converged approximation can possess the wrong task topology when its asymptotic assumptions fail nonuniformly.

Here, the Step-20 Rice calculation had fully converged spectral quadrature and still produced a spurious second detector-preference reversal because the approximation counted an increasing number of high-band micro-upcrossings that belong to the same underlying rough excursion.

The Palm correction does more than shift a threshold; it changes the inferred phase topology.

---

## 11. Stopping point

The lower reversal is Palm-validated and the reported upper Rice reversal is invalidated.

### Single natural next question

> Can the full Palm-corrected preference boundary in `(Lambda,kappa_f)` be mapped well enough to determine whether the high-band slow-preferred region disappears entirely, and whether the finite bandwidth optimum from Step 19 survives as a true Palm boundary maximum?
