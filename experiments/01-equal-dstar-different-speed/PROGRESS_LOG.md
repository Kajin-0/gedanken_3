# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 23:04 EDT:** compact chronology preserving consequential derivations, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and the current stopping point. Full derivations remain in dedicated step files.

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

## Step 36 — 23:04 EDT — fixed-cluster maximum strip bound
Freeze a lower level `a` and let `M_j` be maxima of the connected components of `{z>a}`. Define

```math
C_a(y)=sum_j1_{M_j>y},
```

and for `a<y1<y2`,

```math
D_a(y1,y2)=C_a(y1)-C_a(y2)
=sum_j1_{y1<M_j<=y2}.
```

Then pathwise

```math
{y1<sup z<=y2} subset {D_a>=1},
```

so

```math
\boxed{
P(y1<sup z<=y2)<=E[D_a(y1,y2)].
}
```

Under the Step-33 lower-level occupation-Palm law,

```math
\boxed{
E[D_a(y1,y2)]
=ell Q(a)E_a[1_{y1<M_I<=y2}/L].
}
```

Define the cluster-maximum intensity measure

```math
nu_a(B)=ell Q(a)E_a[1_{M_I in B}/L].
```

Then

```math
P(y1<sup z<=y2)<=nu_a((y1,y2]).
```

This is exact, finite-threshold, derivative-free, and valid at the rough endpoint.

For the original fast high-band trajectory (`x=7.16`, `ell=0.895`, `Delta=0.15`, `u~4.959`), `12000`-path diagnostics at half-widths `w=.005,.01,.02` give

```text
kappa_f   nu((u-w,u+w])/(2w alpha)
170                ~4.95–5.16
300                ~5.03–5.17
1000               ~5.17–5.54
infinity           ~5.19–5.53
```

An independent `20000`-path rough-endpoint check gives the same `~5.1–5.5` scale.

**NUMERICAL VALIDATION:** local cluster-max strip intensity is about

```math
h_a(u)~5 alpha
```

per unit threshold. Thus numerically

```math
nu_a((u-delta,u+delta])~10 delta alpha.
```

A linear extrapolation to `delta=1e-4` gives order `1e-9` absolute probability, versus the useless `O(1e-4)` global anti-concentration scale from Step 35.

**QUALIFICATION:** exact strip inequality/occupation identity are analytic; the local density value and `delta=1e-4` extrapolation are numerical. No uniform density/hazard theorem yet.

Full derivation: `TAIL_SENSITIVE_CLUSTER_STRIP_CONTINUITY_STEP.md`.  
Calculator: `numerics/cluster_maximum_strip.py`.

---

## Current stopping point

The threshold-buffer part of Step 35 has been converted into a rare physical-excursion cluster-maximum measure with the correct observed `O(alpha delta)` scale. The remaining mathematical gap is an analytic uniform bound on the local cluster-max intensity.

### Single natural next question

> Can the local cluster-maximum intensity `h_{a,q}(u)` be bounded analytically and uniformly over the high-band `q` interval—ideally by a rare-event hazard form such as `h_{a,q}(u) <= C u E[C_a(u)]`—so that the buffered-threshold term becomes theorem-level rather than numerically extrapolated?
