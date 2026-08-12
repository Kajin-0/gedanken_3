# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 00:38 EDT  
**Status:** thirty-seven logical steps completed. Step 37 explains analytically why the Step-36 cluster-maximum strip has the rare-event scale `O(u delta alpha)`: for every fixed Gaussian local roughness class, Pickands' high-threshold tail law implies an exponential overshoot on the `1/u` height scale, hence cluster hazard `h(u)~u N(u)` under asymptotic single-cluster separation. The leading hazard scale is the same for smooth (`gamma=2`) and rough (`gamma=1`) classes. However, this fixed-class result is nonuniform as `q=kappa_f^-1/2 -> 0`; finite `q` is infinitesimally smooth while `q=0` is rough, and the physical threshold `u~4.96` lies in the previously identified finite-band/Brownian-parabola crossover. The remaining theorem gap is an explicit uniform finite-crossover hazard multiplier, naturally encoded by logarithmic derivatives of the two-parameter generalized Pickands constant `H(chi,zeta)`. No universal scalar replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical photodetectors satisfy

```math
D_A^*=D_B^*
```

but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

---

## 2. Surviving logical chain

### Steps 01–12 — scalar `D*`, full observation, finite records
- Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that ideal full-observation equivalence.
- Finite observation can because magnitude-only `D*(f)` discards temporal phase/placement.
- Derived exact finite-record optimal SNR and task-level detection time.
- Faster SNR accumulation can be offset by unknown-time search burden.
- **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth.
- **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13 — hard-window roughness
Finite hard-window ideal-white-noise scans are locally Brownian-like,

```math
R_x(y)=1-a_x|y|+O(y^2).
```

**FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` moved under refinement and is invalid.

### Steps 14–19 — genuine timing bandwidth and physical signal/noise
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity is available; Rice/EC is an upper bound and becomes nonuniform as bandwidth grows. With common physical bandwidth `kappa_i=Omega_B tau_i`, artificially forcing accessible eventual SNR equal gives no finite bandwidth optimum. Holding physical signal/noise fixed restores bandwidth-dependent SNR and produces a finite large-`r` optimum; later Palm work confirms a shallow optimum broadly near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Steps 20–23 — finite-`r` reversal corrected; rough endpoint
For

```text
r=2, rho_full=6.2407571, alpha=1e-6, beta=0.90, Lambda=0.895
```

converged Rice produced apparent switches at `25.4898402` and `130.1945883`. Continuous Palm preserves only

```math
kappa_cross^Palm ~ 21.7 +/- 0.3
```

and **INVALIDATES** the upper Rice switch. Palm maps the high-band boundary near `Lambda~0.91`. Exact occupation-time importance sampling at `kappa=infinity` gives

```math
Lambda_cross^infinity ~0.905 +/-0.004,
X~7.75,
```

so `Lambda=0.895` remains fast-preferred at the rough endpoint.

### Steps 24–30 — finite-band tangent, Pickands, Bessel, Brownian-parabola crossover
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; the generalized Pickands problem is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity but not physical-boundary monotonicity. Common-white-noise coupling gives the rough/smoothed path scale.

**INVALIDATED INTERMEDIATE:** `0.8131` was the wrong coupling RMS coefficient; correct pointwise coefficient is

```math
0.8906480701 sqrt(chi/zeta).
```

A two-sided-BES(3) extremum zoom-in identifies a positive Gaussian-mollifier `zeta^-1/2` correction under stable-convergence/localization/UI assumptions.

Small `chi` introduces

```math
h_chi=sqrt(2)chi^(1/3),
m_chi=2chi^(2/3),
mu=sqrt(2)zeta chi^(1/3).
```

The difficult fast channel reduces to the canonical Brownian-minus-parabola function

```math
F(mu)=(2/sqrt(pi))E[M_infinity-M_mu].
```

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were grid biased; continuum-extrapolated full-field values agree with the canonical function. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31 — empirical Palm-anchored bridge
Canonical crossover inserted into the finite-`r` boundary gave a one-hump central bridge peaking near

```math
kappa_f~94.9,
Lambda~0.91068,
```

then descending toward `Lambda_infinity~0.90513`.

**NUMERICAL CLOSURE:** no high-band re-entrant pocket supported for `Lambda=0.895`.

**CONDITIONAL:** residual finite-`u` correction was empirical; later steps remove this fit from the original high-band conclusion.

### Step 32 — direct finite-`u` Rice moment enclosure
For smooth finite bandwidth,

```math
P_FA=Q(u)+P(X_u>=1),
X_u=1_{z(0)<=u}N_u^+.
```

First-/second-order Rice moments give

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `X=7.04`, fast is directly certified feasible and slow infeasible through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, the bound loses sharpness because one physical slow excursion contains many micro-upcrossings. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

### Step 33 — excursion-cluster moment renormalization
Choose `Delta>0`, set `a=u-Delta`, and count connected components of `{z>a}` whose maximum exceeds `u`; call this `C_Delta`. Pathwise,

```math
sup z>u iff C_Delta>=1.
```

Then

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Under lower-level occupation-Palm `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`,

```math
E[C_Delta]=ell Q(a)E_a[S/L],
E[C_Delta^2]=ell Q(a)E_a[S C_Delta/L].
```

No derivative/upcrossing count appears. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`. Rough endpoint (`50000` paths, grid `~0.001`): fast `0.98940–0.98968 alpha`, slow `1.22367–1.22583 alpha`. **NUMERICAL ENDPOINT CERTIFICATE.**

### Step 34 — adaptive paired cluster tail closure
Use

```math
q=kappa_f^(-1/2)
```

so `170<=kappa_f<=infinity` becomes `0<=q<=0.0767`. Common-random-number pairing of the fast cluster upper moment to the rough endpoint plus dense `q` sampling gives a conservative numerical envelope

```math
U_f/alpha ~<0.99955<1,
```

while the slow lower envelope remains

```math
L_s/alpha ~>1.10>1.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** original high-band conclusion no longer depends on the Step-31 empirical fit. **QUALIFICATION:** inter-node allowance remains empirical rather than theorem-level.

### Step 35 — analytic `q` process continuity; global anti-concentration fails
For normalized spectral amplitude

```math
A_q(w)=|H_x(w)|exp(-w^2q^4/2)/sqrt(I_x(q)),
```

exactly

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

The hard-window `1/w^2` spectral-mass tail makes the `q->0` derivative finite, so the common-noise field is `L2`-Lipschitz through the rough endpoint. For fast `x=7.16`, `Delta q=0.005` gives pointwise RMS process change `~<7.5e-5`; threshold motion is only `~<2.8e-5`.

Exact event sandwich under a sup-norm coupling:

```math
p_q(u_q+delta)-eta <= p(r) <= p_q(u_q-delta)+eta.
```

**REJECTED SHORTCUT:** excursion-cluster counts/moments are not pathwise Lipschitz.

**NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is many orders too coarse at `alpha=1e-6`; the missing theorem must be tail-sensitive to rare successful excursions.

### Step 36 — fixed-cluster maximum strip measure
Freeze one lower declustering level `a` and let `M_j` be the maxima of the connected components of `{z>a}`. Define

```math
C_a(y)=sum_j 1_{M_j>y}
```

and for `a<y1<y2`,

```math
D_a(y1,y2)=C_a(y1)-C_a(y2)
=sum_j1_{y1<M_j<=y2}.
```

Pathwise,

```math
{y1<sup z<=y2} subset {D_a>=1},
```

hence the exact tail-sensitive strip bound

```math
P(y1<sup z<=y2)<=E[D_a(y1,y2)].
```

Under lower-level occupation-Palm,

```math
E[D_a(y1,y2)]
=ell Q(a) E_a[1_{y1<M_I<=y2}/L].
```

Define the cluster-maximum intensity measure

```math
nu_a(B)=ell Q(a)E_a[1_{M_I in B}/L].
```

Then

```math
P(y1<sup z<=y2)<=nu_a((y1,y2]).
```

For the original fast high-band trajectory (`x=7.16`, `ell=0.895`, `Delta=0.15`, `u~4.959`), numerical diagnostics give local strip intensity about `5 alpha` per unit threshold over `kappa_f=170,300,1000,infinity`, hence the observed buffered probability scales as `~10 delta alpha`. **QUALIFICATION:** the exact strip inequality/occupation identity are analytic; the local density value is numerical.

### Step 37 — high-threshold cluster overshoot hazard
For a fixed local covariance class

```math
R(t)=1-c|t|^gamma+o(|t|^gamma),
0<gamma<=2,
```

Pickands' theorem gives

```math
P(sup z>u)
~ ell c^(1/gamma) H_gamma u^(2/gamma) Q(u).
```

If multiple successful finite-amplitude clusters are asymptotically lower order, then `N_a(u)=E[C_a(u)]` has the same leading tail. For fixed `s>=0`, the threshold shift `delta=s/u` yields

```math
\boxed{
N_a(u+s/u)/N_a(u) -> exp(-s).
}
```

Hence

```math
\boxed{
[N_a(u)-N_a(u+s/u)]/N_a(u) -> 1-exp(-s),
}
```

and, taking `s->0` after `u->infinity`, the cluster hazard obeys

```math
h_a(u)~u N_a(u)
```

when a local density exists. This explains analytically why the Step-36 strip mass is `O(u delta alpha)` rather than global `O(delta)`.

The leading scale is the same for smooth `gamma=2` and rough `gamma=1` classes. At the physical `u~4.959`, however, the pure smooth and pure rough leading models give hazard coefficients around `4.96` and `4.74`, while Step-36 numerics give `~5.0–5.5`. **REFINEMENT / REJECTED SHORTCUT:** this finite discrepancy reflects the already identified Brownian-parabola / finite-band crossover; substituting the pure rough fixed-class Pickands asymptotic at `u~5` is not a quantitative certificate.

The matched tangent intensity has

```math
N_tan(u;q)
=ell [u sqrt(b)/sqrt(2)] H(chi,zeta) Q(u),
```

with

```math
chi=a_xu/sqrt(b),
zeta=kappa/[sqrt(2)u sqrt(b)].
```

Its formal logarithmic hazard is

```math
h_tan/N_tan
=phi(u)/Q(u)-1/u
 -(chi/u) d_chi log H
 +(zeta/u) d_zeta log H.
```

Thus the remaining uniform hazard theorem is equivalent to controlling the logarithmic elasticities of the two-parameter generalized Pickands constant along the detector-relevant trajectory. Step 25 supplies monotonicity signs, but not a sufficiently strong upper bound on the positive `zeta` elasticity.

See `CLUSTER_HAZARD_OVERSHOOT_STEP.md` and `numerics/cluster_hazard_overshoot.py`.

---

## 3. Current frontier

The rare-event hazard scale itself is now analytically explained. The remaining mathematical task is to bound the finite-crossover multiplier uniformly over the detector-relevant `(chi,zeta)` trajectory, especially the positive `zeta d_zeta log H` contribution.

### Single next question — DO NOT ANSWER YET

> Can the variogram ordering and Dieker–Yakir representation bound the logarithmic elasticities `chi d_chi log H` and `zeta d_zeta log H`—especially the positive `zeta` term—strongly enough to give an explicit uniform hazard multiplier along the high-band detector trajectory?

---

## 4. Scope boundary

Do not claim:
- faster detectors are universally better or worse;
- a universal scalar replacement for `D*`;
- Step-13 `ell~49` is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20 double reversal is exact;
- raw Step-27 fast values are continuum crossover data;
- Step-31 empirical `delta(kappa)` is exact or still required for the original high-band conclusion;
- Step-32 raw crossing moments stay sharp in the rough limit;
- Step-33/34 Monte Carlo estimates are formal interval arithmetic;
- Step-34 is theorem-level continuous-parameter closure;
- Step-35 process Lipschitz continuity implies cluster-moment Lipschitz continuity;
- generic Gaussian anti-concentration is sharp enough at the rare-event scale;
- Step-36 proves a uniform cluster-max density/hazard bound;
- Step-37 fixed-class Pickands asymptotics are quantitatively uniform through `q->0` at `u~5`;
- the pure rough `gamma=1` hazard formula is a finite-u certificate for the fast endpoint;
- no re-entrant pocket can occur for other task parameters;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
