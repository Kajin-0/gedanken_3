# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 22:54 EDT:** compact chronology preserving consequential results, corrections, invalidations, rejected shortcuts, numerical validations, asymptotic qualifications, and current stopping point. Full derivations remain in dedicated step files.

---

## Steps 01–04
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite windows can because magnitude-only `D*(f)` discards temporal phase/placement.

## Steps 05–12
Derived finite-record optimal SNR and task-level detection time. Faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

## Step 13
Finite hard-window ideal-white-noise scan is locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` invalid.

## Steps 14–19
A genuine finite timing bandwidth removes the hard-window cusp. Exact smooth Palm identity is available; Rice/EC is an upper bound and nonuniform as bandwidth grows. With common physical bandwidth, forcing accessible SNR equal gives no finite optimum. Holding physical signal/noise fixed produces a genuine finite large-`r` optimum; later Palm work confirms a shallow optimum broadly near `kappa~50–65`, about `0.3–0.4%` above infinity.

## Steps 20–23
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, Rice gave apparent switches `25.4898402` and `130.1945883`. Palm preserves only `kappa_cross~21.7 +/-0.3`; **INVALIDATED:** upper Rice switch. Palm boundary reaches about `Lambda~0.91` around `kappa_f~60–200`. Direct occupation sampling at `kappa=infinity` gives `Lambda_cross^infinity~0.905 +/-0.004`; `Lambda=0.895` remains fast-preferred.

## Steps 24–28
Finite bandwidth adds `zeta=kappa/(sqrt(2)u sqrt(b))`; generalized Pickands structure is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity but not physical-boundary monotonicity. Common-white-noise coupling gives the rough/smoothed path scale. **INVALIDATED INTERMEDIATE:** `0.8131`; correct pointwise RMS coefficient is `0.8906480701 sqrt(chi/zeta)`. Two-sided-BES(3) Brownian-extremum zoom-in identifies a positive `zeta^-1/2` Gaussian-mollifier correction under stable-convergence/localization/UI.

## Steps 29–30
Small `chi` introduces Brownian–parabola scales

```math
h_chi=sqrt(2)chi^(1/3),
m_chi=2chi^(2/3),
mu=sqrt(2)zeta chi^(1/3).
```

At the `r=2` endpoint, `mu_f~0.009776 kappa_f`, `mu_s~0.16139 kappa_f`. The small-`chi` fast crossover reduces to

```math
F(mu)=(2/sqrt(pi))E[M_inf-M_mu].
```

Representative continuum values: `F(0)~.892`, `F(.5,1,2,3,5,10,20)~.806,.729,.597,.512,.410,.297,.213`; `sqrt(mu)F(mu)->~0.98`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical curve; fast asymptotic `C_H` refines to about `0.0088`.

## Step 31
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor residual finite-threshold offset to Palm points plus the rough endpoint. Central bridge peaks near `kappa_f~94.9`, `Lambda~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** original `Lambda=0.895` task has no numerically supported bounded high-band re-entrant pocket. **CONDITIONAL:** the finite-`u` offset was empirical.

## Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan,

```math
X_u=1_{z(0)<=u}N_u^+,
P_FA=Q(u)+P(X_u>=1).
```

With `m1=E[X_u]`, `lambda=E[N_u^+]`, `lambda2=E[N_u^+(N_u^+-1)]`,

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `Lambda=0.895`, `X=7.04`:

```text
kappa_f   fast upper/alpha   slow lower/alpha
100           0.99737             1.04649
130           0.99861             1.02562
160           0.99961             1.00950
170           0.99990             1.00491
175           1.00004             1.00275
```

**PARTIAL CERTIFICATE:** fast preference directly enclosed through at least `kappa_f=170`. **NEGATIVE RESULT:** around `175–200`, raw crossing second moments lose sharpness because one physical excursion contains many micro-upcrossings.

Full derivation: `FINITE_U_RICE_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/finite_u_rice_moment_enclosure.py`.

## Step 33 — excursion-cluster moment renormalization
Choose finite amplitude gap `Delta>0`, set `a=u-Delta`, decompose `{t:z(t)>a}` into connected components, and count only components whose maximum exceeds `u`; call this `C_Delta`.

Pathwise,

```math
sup z>u iff C_Delta>=1.
```

For fixed `Delta`, the count remains finite on continuous compact paths even when raw level-`u` upcrossings proliferate.

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Under lower-level occupation-Palm measure `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`,

```math
E[C_Delta]=ell Q(a)E_a[S/L],
E[C_Delta^2]=ell Q(a)E_a[S C_Delta/L].
```

For the original task at `X=7.16`, `Delta=0.15`, cluster bounds separate fast/slow at `kappa_f=300`, `1000`, and the rough endpoint. Endpoint (`50000` paths, grid `~0.001`): fast `0.98940–0.98968 alpha`, slow `1.22367–1.22583 alpha`.

**NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE:** Step-32 divergence belongs to micro-upcrossing multiplicity, not the physical excursion event.

Full derivation: `EXCURSION_CLUSTER_MOMENT_ENCLOSURE_STEP.md`.  
Calculator: `numerics/excursion_cluster_moment_enclosure.py`.

## Step 34 — adaptive paired cluster tail closure
Use

```math
q=kappa_f^(-1/2)
```

so the unresolved tail becomes finite: `0<=q<=0.0767 <-> infinity>=kappa_f>=~170`.

For fast `U_f(q)=E[C_Delta(q)]`, generate finite-`q` and endpoint fields from the same white noise, truncated-normal uniform, and selected occupation time. Dense `3000`-path paired scan plus refined midpoints gives

```text
max sampled positive correction/alpha ~= +1.9e-8
min correction/alpha                  ~= -0.00188
max paired SE/alpha                   ~= 0.00106
max adjacent 0.005-node change/alpha  ~= 0.000548.
```

Paired nested-grid rough-endpoint check gives shifts of only about `-0.00093 alpha` at `~0.00150` grid and `-0.00134 alpha` at `~0.00300` relative to a fine `~0.000751` grid.

Using endpoint anchor `0.98968 +/-0.00429`, one-sided Gaussian factor `1.645`, grid allowance `0.002`, and inter-node allowance `0.0006` gives

```math
U_f/alpha ~<0.99955<1.
```

Slow absolute scan remains well above threshold; deliberately conservative deductions leave

```math
L_s/alpha ~>1.10>1.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** original `Lambda=0.895` task is numerically separated over `170<=kappa_f<=infinity` without the Step-31 empirical `delta(kappa)` fit. **QUALIFICATION:** inter-node allowance is empirical, not theorem-level continuity.

Full derivation: `ADAPTIVE_CLUSTER_TAIL_CLOSURE_STEP.md`.  
Calculator: `numerics/adaptive_cluster_tail_closure.py`.

## Step 35 — 22:54 EDT — analytic `q` coupling and rare-event obstruction
Define normalized spectral amplitude

```math
A_q(w)=|H_x(w)|exp(-w^2q^4/2)/sqrt(I_x(q)),
I_x(q)=int |H_x(w)|^2 exp(-w^2q^4)dw.
```

With normalized spectral moments `M_2n(q)`, exact differentiation gives

```math
\boxed{
dA_q/dq=-2q^3(w^2-M2(q))A_q,
}
```

```math
\boxed{
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
}
```

For the hard finite-window spectral tail `|H_x(w)|^2~c_x^2/w^2`, `c_x=xe^-x`, the rough-endpoint limit is finite:

```math
\boxed{
lim_{q->0}||dA_q/dq||_2^2
=2sqrt(pi)c_x^2/I_x(0).
}
```

Thus the common-noise Gaussian field is genuinely regular in `q`, including `q=0`.

For fast `x=7.16`, deterministic spectral quadrature gives

```text
q        ||dA/dq||_2
0        0.00836
0.020    0.00840
0.040    0.00898
0.060    0.01130
0.0767   0.01493
```

so across `Delta q=0.005`,

```math
SD[z_q(t)-z_{q+Delta q}(t)] ~<7.5e-5.
```

The available threshold obeys

```math
u'(q)=-2q^3M2(q)rho(q),
```

with max fast `|u'|~5.6e-3`, so threshold motion over the same cell is `~<2.8e-5`.

Exact pathwise event sandwich: if `||z_q-z_r||_inf<=epsilon`, `delta=epsilon+|u_q-u_r|`, and `eta=P(||z_q-z_r||_inf>epsilon)`, then

```math
p_q(u_q+delta)-eta <= p(r) <= p_q(u_q-delta)+eta.
```

**REJECTED SHORTCUT:** `C_Delta` and the Palm weights are not pathwise Lipschitz because small perturbations can merge/split lower components, flip a component maximum across `u`, or amplify `1/L` for a short component.

**NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is unusably coarse at the required rare-event scale. The standard bound

```math
P(|sup X-y|<=epsilon) <= 4epsilon(E sup X+1)
```

already gives at least `4e-4=400 alpha` for `epsilon=1e-4`, while Step 34's empirical inter-node allowance was only `0.0006 alpha = 6e-10` absolute.

The remaining theorem gap is therefore a **tail-sensitive successful-excursion continuity law**, not Gaussian-field continuity in `q`.

Full derivation: `Q_COUPLING_CONTINUITY_OBSTRUCTION_STEP.md`.  
Calculator: `numerics/q_coupling_continuity.py`.

---

## Current stopping point

The Step-34 coordinate `q=kappa_f^-1/2` is now analytically justified: the normalized common-noise field is `L2`-Lipschitz through the rough endpoint. Generic anti-concentration cannot exploit the `alpha=1e-6` high-threshold scale.

### Single natural next question

> Can the successful-excursion cluster representation yield a tail-sensitive buffered-threshold continuity bound near `u~5`, so that the probability of a cluster whose maximum lies in `[u-delta,u+delta]` scales like the rare-event intensity times `delta` rather than the global `O(delta)` Gaussian anti-concentration bound?
