# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-12 01:11 EDT  
**Status:** thirty-eight logical steps completed. Step 38 proves an exact cross-elasticity ordering for the two-parameter generalized Pickands constant. The finite-band smoothing function obeys `0 <= zeta d_zeta F_zeta <= F_zeta`, implying by Brown–Resnick Slepian comparison that `H(chi,lambda zeta) <= H(lambda chi,zeta)` for every `lambda>=1`. Hence, wherever derivatives exist, `0 <= zeta d_zeta log H <= chi d_chi log H`. Along the fixed-`kappa` physical threshold trajectory (`chi proportional u`, `zeta proportional 1/u`) `H` is nondecreasing in `u`, and the matched tangent hazard is uniformly bounded by `phi(u)/Q(u)-1/u`. At the operating `u~4.959` this is `~4.9452`, with an exact symmetric tangent-strip factor `~9.89e-4` for `delta=1e-4`, i.e. `~9.9e-10` when the cluster intensity is `~alpha=1e-6`. However, Step-36 exact finite-threshold cluster-strip numerics remain somewhat larger (`~5.0–5.5 alpha` per threshold unit), so the remaining gap is now explicitly the finite-`u` correction between the exact cluster measure and the tangent/Pickands leading model—not the `zeta` elasticity. No universal scalar replacement metric and no novelty claim.

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
- Equal scalar reference `D*` does **not** determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem.
- **NEGATIVE RESULT:** unknown timing alone does not break that ideal full-observation equivalence.
- Finite observation can because magnitude-only `D*(f)` discards temporal phase/placement.
- Exact finite-record optimal SNR and task-level detection time were derived.
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
kappa_cross^Palm ~21.7 +/-0.3
```

and **INVALIDATES** the upper Rice switch. Palm maps the high-band boundary near `Lambda~0.91`. Exact occupation-time importance sampling at `kappa=infinity` gives

```math
Lambda_cross^infinity ~0.905 +/-0.004,
X~7.75,
```

so `Lambda=0.895` remains fast-preferred at the rough endpoint.

### Steps 24–30 — tangent field, generalized Pickands, Bessel and Brownian-parabola crossover
Finite bandwidth adds

```math
zeta=kappa/(sqrt(2)u sqrt(b)),
```

and the generalized Pickands problem is two-parameter. Brown–Resnick Slepian comparison proves coordinatewise monotonicity but not physical-boundary monotonicity. Common-white-noise coupling gives the rough/smoothed path scale.

**INVALIDATED INTERMEDIATE:** `0.8131` was the wrong coupling RMS coefficient; correct pointwise value is

```math
0.8906480701 sqrt(chi/zeta).
```

A two-sided-BES(3) extremum zoom-in identifies a positive Gaussian-mollifier `zeta^-1/2` correction under stable-convergence/localization/UI assumptions.

Small `chi` introduces

```math
h_chi=sqrt(2)chi^(1/3),
m_chi=2chi^(2/3),
mu=sqrt(2)zeta chi^(1/3),
```

and the difficult fast channel reduces to the canonical Brownian-minus-parabola function

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

**CONDITIONAL:** residual finite-`u` correction was empirical; later direct finite-`u` steps remove dependence on this fit for the original high-band conclusion.

### Step 32 — direct finite-`u` Rice moment enclosure
For smooth finite bandwidth,

```math
P_FA=Q(u)+P(X_u>=1),
X_u=1_{z(0)<=u}N_u^+,
```

and first-/second-order Rice moments give

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `X=7.04`, fast is directly certified feasible and slow infeasible through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, the bound loses sharpness because one physical slow excursion contains many micro-upcrossings. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

### Step 33 — finite-amplitude excursion clusters
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

### Step 34 — paired numerical tail closure
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

**PAIRED NUMERICAL INTERVAL CLOSURE:** the original high-band conclusion no longer depends on the Step-31 empirical fit. **QUALIFICATION:** inter-node allowance remains empirical rather than theorem-level.

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
Freeze one lower declustering level `a`; let `M_j` be maxima of connected components of `{z>a}`. Define

```math
C_a(y)=sum_j1_{M_j>y}
```

and

```math
D_a(y1,y2)=sum_j1_{y1<M_j<=y2}.
```

Then

```math
P(y1<sup z<=y2)<=E[D_a(y1,y2)],
```

with exact lower-level occupation-Palm identity

```math
E[D_a(y1,y2)]
=ell Q(a)E_a[1_{y1<M_I<=y2}/L].
```

The cluster-maximum measure

```math
nu_a(B)=ell Q(a)E_a[1_{M_I in B}/L]
```

therefore provides a derivative-free, rough-endpoint-valid strip envelope. For the original fast high-band trajectory (`u~4.959`), numerical diagnostics give local strip intensity about `5 alpha` per threshold unit over `kappa_f=170,300,1000,infinity`, hence observed symmetric-buffer scaling `~10 delta alpha`. **TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION.**

### Step 37 — high-threshold cluster overshoot hazard
For fixed local covariance class

```math
R(t)=1-c|t|^gamma+o(|t|^gamma),
0<gamma<=2,
```

Pickands gives `P(sup z>u)~K u^(2/gamma)Q(u)`. Under asymptotically negligible multiple successful finite-amplitude clusters, `N_a(u)=E[C_a(u)]` has the same leading tail. For fixed `s>=0`,

```math
N_a(u+s/u)/N_a(u)->exp(-s),
```

so successful-cluster overshoot is asymptotically exponential on the `1/u` height scale and `h_a(u)~uN_a(u)` in the iterated local limit. This analytically explains the Step-36 `O(u delta alpha)` rare-event strip scale.

**REFINEMENT / REJECTED SHORTCUT:** fixed-class asymptotics are nonuniform through `q->0` at physical `u~4.96`. The matched tangent intensity

```math
N_tan=ell[u sqrt(b)/sqrt(2)]H(chi,zeta)Q(u)
```

has formal hazard

```math
h_tan/N_tan
=phi/Q-1/u
 -(chi/u)d_chi log H
 +(zeta/u)d_zeta log H.
```

Step 37 therefore left the finite-crossover multiplier as a Pickands-elasticity problem.

### Step 38 — exact cross-elasticity ordering
The tangent smoothing function satisfies

```math
0 <= zeta d_zeta F_zeta(t) <= F_zeta(t)
```

for every `t,zeta>0`. Consequently, for every `lambda>=1`,

```math
F_{lambda zeta}(t) <= lambda F_zeta(t),
```

so

```math
g_{chi,lambda zeta}(t) <= g_{lambda chi,zeta}(t).
```

Brown–Resnick Slepian comparison therefore gives the exact finite-difference cross-ordering

```math
\boxed{
H(chi,lambda zeta) <= H(lambda chi,zeta).
}
```

Where logarithmic derivatives exist,

```math
\boxed{
0 <= zeta d_zeta log H <= chi d_chi log H.
}
```

Along a fixed-`kappa` threshold trajectory (`chi~u`, `zeta~1/u`), `H` is thus nondecreasing in `u` exactly. Hence the matched tangent hazard obeys

```math
\boxed{
h_tan/N_tan <= phi(u)/Q(u)-1/u.
}
```

At `u~4.959`, the right side is `~4.9452`. More strongly, finite-difference monotonicity gives the explicit symmetric tangent-strip factor

```math
\boxed{
B(u,delta)
=((u-delta)/u)Q(u-delta)/Q(u)
-((u+delta)/u)Q(u+delta)/Q(u).
}
```

For `delta=1e-4`,

```math
B~9.89e-4,
```

so when `N_tan~alpha=1e-6`, the predicted symmetric strip is at most `~9.9e-10` in absolute scale.

**NEGATIVE RESULT / REFINEMENT:** Step-36 exact finite-`u` cluster-strip numerics (`~5.0–5.5 alpha` per threshold unit) can exceed the tangent coefficient `~4.9452`. Therefore the positive `zeta` elasticity is **not** the source of the finite-crossover excess. The remaining discrepancy is the finite-threshold correction from the tangent/Pickands approximation to the exact cluster-maximum measure.

See `PICKANDS_ELASTICITY_ORDERING_STEP.md` and `numerics/pickands_elasticity_ordering.py`.

---

## 3. Current frontier

The generalized Pickands elasticity is no longer the unresolved part of the hazard problem. The remaining mathematical task is to control the finite-`u` remainder between the exact cluster first moment and the matched tangent intensity, especially its threshold variation near `u~5`.

### Single next question — DO NOT ANSWER YET

> Can the exact cluster first moment be factorized as `N_a(u,q)=N_tan(u,q) R(u,q)` with a controlled finite-threshold remainder, and can the threshold variation of `R` be bounded tightly enough at `u~5` to account for the observed `~5–10%` excess in the Step-36 strip intensity?

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
- Step-35 field Lipschitz continuity implies cluster-moment Lipschitz continuity;
- generic Gaussian anti-concentration is sharp enough at the rare-event scale;
- Step-36 proves a uniform cluster-max density/hazard bound;
- Step-37 fixed-class Pickands asymptotics are quantitatively uniform through `q->0` at `u~5`;
- Step-38 tangent hazard bound is already an exact finite-`u` bound for the physical cluster measure;
- the Step-36 `5.0–5.5` coefficient is caused by positive `zeta` elasticity;
- no re-entrant pocket can occur for other task parameters;
- the Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
