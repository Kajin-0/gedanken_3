# Progress Log — Experiment 01

**Consolidation note — 2026-08-12 00:38 EDT:** compact chronology preserving consequential derivations, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and the current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–12
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude-only `D*(f)` discards temporal phase/placement. Derived finite-record optimal SNR and task-level detection time. Faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` invalid.

## Steps 14–19
A genuine finite timing bandwidth removes the hard-window cusp. Exact smooth Palm identity available; Rice/EC is an upper bound and nonuniform as bandwidth grows. With common physical bandwidth, forcing accessible SNR equal gives no finite optimum. Holding physical signal/noise fixed produces a genuine finite large-`r` optimum; later Palm work confirms a shallow optimum near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Steps 20–23
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only `kappa_cross~21.7 +/-0.3`; **INVALIDATED:** upper Rice switch. Palm boundary reaches about `Lambda~0.91` around `kappa_f~60–200`. Direct occupation sampling at `kappa=infinity` gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Steps 24–30
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Common-white-noise coupling and Bessel extremum zoom-in identify the rough/smoothed high-band correction. **INVALIDATED INTERMEDIATE:** `0.8131`; correct pointwise coupling coefficient is `0.8906480701 sqrt(chi/zeta)`. Small `chi` introduces Brownian–parabola scales and crossover `mu=sqrt(2)zeta chi^(1/3)`; the fast channel reduces to

```math
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

**INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were grid biased; continuum-extrapolated full-field values agree with the canonical curve. Fast asymptotic `C_H` refines to about `0.0088`.

## Step 31
Canonical crossover inserted into the finite-`r` boundary; Palm/occupation anchoring gave a one-hump central bridge peaking near `kappa_f~94.9`, `Lambda~0.91068`, then descending toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** no high-band re-entrant pocket supported for `Lambda=0.895`. **CONDITIONAL:** finite-`u` offset was empirical.

## Step 32
Finite-`u` first-/second-order Rice moment enclosure:

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `X=7.04`, fast is directly certified feasible and slow infeasible through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, raw crossing moments lose sharpness because one physical slow excursion contains many micro-upcrossings. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

Full derivation: `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/finite_u_rice_moment_enclosure.py`.

## Step 33
Finite-amplitude excursion-cluster count `C_Delta` satisfies

```math
sup z>u iff C_Delta>=1,
```

and

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Occupation-Palm identities for `E[C_Delta]` and `E[C_Delta^2]` use selected-component duration `L` and success indicator `S`, with no derivative/upcrossing count. Cluster bounds remain sharp at `kappa_f=300`, `1000`, and `infinity`; rough endpoint fast `0.98940–0.98968 alpha`, slow `1.22367–1.22583 alpha`. **NUMERICAL ENDPOINT CERTIFICATE.**

Full derivation: `EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/excursion_cluster_moment_enclosure.py`.

## Step 34
Use `q=kappa_f^-1/2` and common-random-number pairing to the rough endpoint. Dense paired scan plus measured grid/inter-node allowances gives fast envelope `U_f/alpha~<0.99955` and slow envelope `L_s/alpha~>1.10` across `170<=kappa_f<=infinity`. **PAIRED NUMERICAL INTERVAL CLOSURE:** original high-band conclusion no longer depends on Step-31 empirical `delta(kappa)`. **QUALIFICATION:** inter-node allowance is empirical, not theorem-level continuity.

Full derivation: `ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md`.  
Calculator: `numerics/adaptive_cluster_tail_closure.py`.

## Step 35
For normalized spectral amplitude

```math
A_q(w)=|H_x(w)|exp(-w^2q^4/2)/sqrt(I_x(q)),
```

exactly

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

The finite-window `1/w^2` spectral-mass tail makes the `q->0` derivative finite, so the common-noise field is `L2`-Lipschitz through the rough endpoint. Fast `x=7.16`, `Delta q=0.005` gives pointwise RMS process change `~<7.5e-5`; threshold motion `~<2.8e-5`.

Exact event sandwich under a sup-norm coupling:

```math
p_q(u_q+delta)-eta <= p(r) <= p_q(u_q-delta)+eta.
```

**REJECTED SHORTCUT:** cluster counts/moments are not pathwise Lipschitz. **NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is orders of magnitude too coarse at `alpha=1e-6`; the theorem gap is tail-sensitive rare-excursion continuity.

Full derivation: `Q_COUPLING_CONTINUITY_OBSTRUCTION_STEP.md`.  
Calculator: `numerics/q_coupling_continuity.py`.

## Step 36
Freeze a lower level `a`; let `M_j` be maxima of the connected components of `{z>a}` and define

```math
C_a(y)=sum_j1_{M_j>y}.
```

For `a<y1<y2`,

```math
D_a(y1,y2)=C_a(y1)-C_a(y2)
=sum_j1_{y1<M_j<=y2}.
```

Then

```math
P(y1<sup z<=y2)<=E[D_a(y1,y2)].
```

Under lower-level occupation-Palm,

```math
E[D_a(y1,y2)]
=ell Q(a)E_a[1_{y1<M_I<=y2}/L].
```

Thus the cluster-maximum measure `nu_a` gives an exact finite-threshold strip envelope that survives the rough endpoint. For the fast high-band trajectory near `u~4.959`, numerical strip intensity is `~5 alpha` per unit threshold across `kappa_f=170,300,1000,infinity`, giving observed `~10 delta alpha` symmetric-buffer scaling. **TAIL-SENSITIVE ENVELOPE / NUMERICAL VALIDATION.**

Full derivation: `TAIL_SENSITIVE_CLUSTER_STRIP_CONTINUITY_STEP.md`.  
Calculator: `numerics/cluster_maximum_strip.py`.

## Step 37 — 00:38 EDT — high-threshold cluster overshoot hazard
For fixed Gaussian local covariance class

```math
R(t)=1-c|t|^gamma+o(|t|^gamma),
0<gamma<=2,
```

Pickands' tail law is

```math
P(sup z>u)
~ell c^(1/gamma)H_gamma u^(2/gamma)Q(u).
```

Assuming asymptotically negligible multiple successful finite-amplitude clusters, `N_a(u)=E[C_a(u)]` has the same leading tail. Rather than differentiating an uncontrolled `o(1)` remainder, shift the threshold by `s/u`. Gaussian tail ratios then give the rigorous fixed-class overshoot relation

```math
\boxed{
N_a(u+s/u)/N_a(u)->exp(-s)
}
```

for fixed `s>=0`, hence

```math
\boxed{
[N_a(u)-N_a(u+s/u)]/N_a(u)->1-exp(-s).
}
```

Taking `s->0` after `u->infinity` yields the rare-event hazard scale

```math
h_a(u)~uN_a(u)
```

when a local density exists. The leading scale is the same for smooth `gamma=2` and rough `gamma=1` classes; this analytically explains the Step-36 `O(u delta alpha)` strip scale.

At the physical `u~4.959`, pure endpoint leading models give finite hazard coefficients around `4.96` (smooth) and `4.74` (rough), while Step-36 diagnostics are `~5.0–5.5`. **REFINEMENT / REJECTED SHORTCUT:** the discrepancy is consistent with the previously established finite-band/Brownian-parabola crossover; fixed-class `gamma=1` asymptotics are not quantitatively uniform through `q->0` at this threshold.

The matched tangent intensity

```math
N_tan=ell[u sqrt(b)/sqrt(2)]H(chi,zeta)Q(u)
```

implies the formal crossover hazard

```math
h_tan/N_tan
=phi/Q-1/u
 -(chi/u)d_chi log H
 +(zeta/u)d_zeta log H.
```

Thus the remaining uniform hazard theorem reduces to controlling the logarithmic elasticities of the two-parameter generalized Pickands constant along the detector trajectory. Step 25 gives monotonicity signs but not a strong enough upper bound on the positive `zeta` term.

Full derivation: `CLUSTER_HAZARD_OVERSHOOT_STEP.md`.  
Calculator: `numerics/cluster_hazard_overshoot.py`.

---

## Current stopping point

The `h~uN` rare-event scale is analytically explained for fixed Gaussian local classes. The remaining gap is a uniform finite-crossover multiplier through the singular smooth/rough transition, naturally encoded by `H(chi,zeta)`.

### Single natural next question

> Can variogram ordering and the Dieker–Yakir representation bound `chi d_chi log H` and `zeta d_zeta log H`, especially the positive `zeta` elasticity, strongly enough to produce an explicit uniform hazard multiplier along the detector-relevant high-band trajectory?
