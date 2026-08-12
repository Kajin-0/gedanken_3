# Step 37 — High-Threshold Cluster Overshoot Hazard and the Uniform-Crossover Obstruction

**Date:** 2026-08-12 00:38 EDT  
**Status:** DERIVED / ASYMPTOTIC / REFINEMENT / CONDITIONAL CLUSTER EXTENSION / REJECTED SHORTCUT / OPEN. Step 36 replaced global Gaussian anti-concentration by the exact fixed-excursion cluster-maximum strip measure and found numerically that its local intensity near the decision threshold is on the rare-event scale, about `5 alpha` per unit threshold. This step asks whether that scale follows analytically from classical Gaussian extreme-value theory. For every fixed local covariance class, Pickands' high-threshold law implies an exponential overshoot on the `1/u` height scale and therefore a cluster hazard `h(u)~u N(u)`. The result is independent of whether the local process is smooth (`gamma=2`) or rough (`gamma=1`) at leading order. However, the fixed-`q` theorem is nonuniform as `q->0`: finite `q` is infinitesimally smooth while `q=0` is rough, and the Step-36 operating point `u~4.96` sits in the previously identified Brownian-parabola / finite-band crossover. The remaining theorem gap is therefore a matched, uniform overshoot bound in the two-parameter tangent variables, not the existence of the rare-event hazard scale itself. No novelty claim.

---

## 1. Pickands tail law at fixed local roughness class

Let `z(t)` be a centered unit-variance stationary Gaussian process on `[0,ell]` with

```math
R(t)=1-c|t|^\gamma+o(|t|^\gamma),
\qquad 0<\gamma\le2,
```

and `R(t)<1` away from zero, under the standard regularity assumptions of Pickands' theorem.

Then

```math
\boxed{
P\!\left(\sup_{0\le t\le\ell}z(t)>u\right)
\sim
\ell c^{1/\gamma}H_\gamma
u^{2/\gamma}\bar\Phi(u)
}
```

as `u->infinity`, where `H_gamma` is the Pickands constant.

For the present excursion-cluster language, let

```math
N_a(u)=E[C_a(u)]
```

for a lower excursion geometry chosen so that distinct successful high clusters remain asymptotically separated. If the probability of two or more successful clusters is lower order,

```math
E[C_a(u)(C_a(u)-1)]
=o(P(\sup z>u)),
```

then

```math
\boxed{
N_a(u)
\sim
P(\sup z>u)
}
```

because `C_a>=1` is exactly the exceedance event and the excess first moment is carried only by multiple successful clusters.

This is the only additional cluster assumption needed below. It is consistent with the classical high-cluster Poisson/separation theory and with the nearly Bernoulli cluster counts observed numerically in Steps 33–36, but a dedicated proof for the exact fixed-amplitude cluster definition remains outside this step.

---

## 2. Overshoot ratio without differentiating the asymptotic remainder

Do **not** differentiate the Pickands equivalence directly; an `o(1)` multiplicative remainder need not have a controlled derivative.

Instead take a fixed `s>=0` and shift the threshold by

```math
\delta_u=\frac{s}{u}.
```

From the Gaussian tail ratio,

```math
\frac{\bar\Phi(u+s/u)}{\bar\Phi(u)}
\longrightarrow e^{-s},
```

while

```math
\left(\frac{u+s/u}{u}\right)^{2/\gamma}
\longrightarrow1.
```

Therefore Pickands' law gives

```math
\boxed{
\frac{N_a(u+s/u)}{N_a(u)}
\longrightarrow e^{-s}
}
```

for every fixed covariance class satisfying the cluster extension above.

Equivalently,

```math
\boxed{
\frac{N_a(u)-N_a(u+s/u)}{N_a(u)}
\longrightarrow1-e^{-s}.
}
```

Thus the conditional overshoot above a high successful-cluster threshold is asymptotically exponential on the natural height scale `1/u`.

---

## 3. Rare-event hazard follows in an iterated limit

Taking `s->0` after `u->infinity`,

```math
1-e^{-s}\sim s.
```

Hence

```math
\boxed{
\lim_{s\downarrow0}\lim_{u\to\infty}
\frac{N_a(u)-N_a(u+s/u)}{sN_a(u)}
=1.
}
```

If the cluster-maximum measure has a density `h_a(u)` and the limits may be interchanged locally, this is the familiar hazard statement

```math
\boxed{
h_a(u)\sim uN_a(u).}
```

The ratio formulation above is stronger epistemically for this step because it does not assume differentiability of the Pickands remainder.

**FIRST CONSEQUENCE:** the `O(alpha delta)` scale observed in Step 36 is not accidental. At a threshold where `N_a(u)` is of order `alpha`, a narrow one-sided strip of width `delta<<1/u` naturally carries probability/count mass of order

```math
u\,delta\,alpha.
```

A symmetric strip has leading scale `2u delta alpha`.

---

## 4. Smooth and rough endpoints have the same leading hazard scale

The polynomial prefactor in Pickands' law changes with `gamma`, but it does not affect the leading overshoot scale.

### Smooth endpoint class: `gamma=2`

```math
N(u)\asymp K_2 u\bar\Phi(u)
\sim K_2\phi(u).
```

Thus the leading hazard is

```math
\boxed{h/N\sim u.}
```

### Rough Brownian class: `gamma=1`

```math
N(u)\asymp K_1u^2\bar\Phi(u).
```

If one differentiates this explicit leading model only, its finite-`u` hazard is

```math
\frac{h}{N}
\approx
\frac{\phi(u)}{\bar\Phi(u)}-\frac{2}{u}
=u-\frac1u+O(u^{-3}),
```

again tending to `u`.

Therefore the leading high-threshold hazard coefficient is insensitive to whether the limiting local process is smooth or rough.

---

## 5. The Step-36 operating point is not yet in the ultimate rough asymptotic

For the fast Step-36 trajectory,

```text
u ~= 4.959.
```

Two classical endpoint leading models give:

```text
model                                local hazard coefficient
----------------------------------------------------------------
smooth Gaussian peak                 ~4.959
rough Pickands u^2 Q(u)              ~4.744
```

whereas the Step-36 cluster-strip diagnostic gave roughly

```text
~5.0 to 5.5
```

across `kappa_f=170,300,1000,infinity`.

This does **not** invalidate the asymptotic law. The fast hard-window cusp coefficient is extremely small at this decision time, and Steps 29–30 already showed that the physical endpoint at moderate threshold is controlled by the Brownian-parabola crossover rather than by the ultimate pure-Brownian high-threshold limit.

**REJECTED SHORTCUT:** substituting `gamma=1` into the fixed-class Pickands formula at `u~5` is not a quantitative endpoint certificate for this detector problem.

---

## 6. Noncommuting limits explain the uniformity problem

For every fixed finite bandwidth `q>0`, the Gaussian-smoothed process is differentiable at infinitesimal time scales, so its fixed-`q`, `u->infinity` local class is `gamma=2`.

At exactly

```math
q=0
```

the hard-window process has the cusp

```math
R(t)=1-a_x|t|-\frac{b_x}{2}t^2+\cdots
```

and its ultimate fixed-endpoint high-threshold class is `gamma=1`.

Therefore

```math
\lim_{q\to0}\lim_{u\to\infty}
```

and

```math
\lim_{u\to\infty}\lim_{q\to0}
```

probe different local asymptotic descriptions.

This is the same noncommutativity that produced the two-parameter tangent field in Steps 24–30.

---

## 7. Matched tangent hazard formula

The Step-24/25 matched high-threshold excursion intensity has the schematic form

```math
\boxed{
N_{tan}(u;q)
=\ell\,\frac{u\sqrt b}{\sqrt2}
\mathcal H(\chi,\zeta)\bar\Phi(u),
}
```

with

```math
\chi=\frac{a_xu}{\sqrt b},
\qquad
\zeta=\frac{\kappa}{\sqrt2u\sqrt b}.
```

At fixed physical bandwidth `kappa`,

```math
u\frac{d\chi}{du}=\chi,
\qquad
u\frac{d\zeta}{du}=-\zeta.
```

Formally differentiating the matched leading model gives the crossover hazard

```math
\boxed{
\frac{h_{tan}}{N_{tan}}
=
\frac{\phi(u)}{\bar\Phi(u)}
-\frac1u
-\frac{\chi}{u}\,\partial_\chi\log\mathcal H
+\frac{\zeta}{u}\,\partial_\zeta\log\mathcal H.
}
```

This formula identifies exactly what a **uniform** hazard theorem must control: the logarithmic elasticities of the two-parameter generalized Pickands constant along the physical threshold trajectory.

Step 25 proved only the signs

```math
\partial_\chi\mathcal H\ge0,
\qquad
\partial_\zeta\mathcal H\ge0.
```

Those signs alone do not upper-bound the positive `zeta` elasticity term.

---

## 8. What classical theory does and does not solve

Classical Pickands theory rigorously supplies the fixed-class tail law and therefore the `1/u` overshoot scale. High-cluster theory likewise supports asymptotic separation/Poissonization of sufficiently high excursions under standard dependence conditions.

Recent Gaussian-extreme work also derives exponential-type overshoot behavior for high local maxima in smooth fields and broad high-level path functionals, reinforcing the same scaling picture.

But none of these fixed-class statements, by themselves, supplies the required **uniform finite-`u` bound across the singular `q->0` smooth-to-rough crossover** of this model.

Accordingly, this step does not promote the Step-36 numerical coefficient to a theorem-level constant.

---

## 9. First nontrivial consequence

The desired hazard form

```math
h_{a,q}(u)\lesssim C u N_{a,q}(u)
```

has now been justified at the level of **pointwise high-threshold asymptotics** for both endpoint regularity classes, and the exponential overshoot ratio shows why the rare-event strip mass scales as `u delta alpha` rather than `delta`.

The unresolved issue is narrower:

```text
not: why should the hazard be rare-event scaled?

but: can the O(1) hazard multiplier be bounded uniformly
     through the finite-u two-parameter smooth/rough crossover?
```

That multiplier is encoded by the threshold derivative of `H(chi,zeta)`.

---

## 10. What remains open

- prove a uniform bound on the logarithmic elasticities of `H(chi,zeta)` over the detector-relevant `(chi,zeta)` trajectory;
- or derive a direct finite-threshold cluster-maximum hazard inequality bypassing tangent asymptotics;
- control the asymptotic remainder uniformly enough at `u~5` to turn the hazard scale into a numerical theorem constant;
- combine such a bound with the Step-35 sup-norm coupling tail;
- formal interval/concentration treatment of all remaining numerical constants;
- extension to other task parameters and detector models;
- hardware interpretation;
- novelty.

---

## 11. Stopping point

Classical Gaussian extreme-value theory explains analytically why the Step-36 cluster strip has the correct rare-event scale. The only missing part of the threshold-buffer theorem is now a **uniform finite-crossover multiplier**, naturally expressible through the two-parameter generalized Pickands constant.

### Single natural next question

> Can the variogram ordering and Dieker–Yakir representation be used to bound the logarithmic elasticities `chi d_chi log H` and `zeta d_zeta log H`—especially the positive `zeta` term—strongly enough to obtain an explicit uniform hazard multiplier `C` along the detector-relevant high-band trajectory?
