# Current State — Experiment 01: Equal D*, Different Speed

**Date:** 2026-08-11 22:54 EDT  
**Status:** thirty-five logical steps completed. Step 35 derives an analytic common-white-noise continuity law in the high-band coordinate `q=kappa_f^(-1/2)`. The normalized Gaussian timing field is `L2`-Lipschitz in `q` all the way to the nondifferentiable rough endpoint. For the Step-34 fast channel, the pointwise RMS process change across `Delta q=0.005` is bounded at about `7.5e-5`, and the decision threshold moves by only about `2.8e-5`. However, the excursion-cluster functional is not pathwise Lipschitz, and generic Gaussian-supremum anti-concentration is many orders of magnitude too coarse at `alpha=1e-6`. The remaining theorem gap is therefore a tail-sensitive successful-excursion continuity bound, not continuity of the Gaussian field itself. No universal scalar replacement metric and no novelty claim.

---

## 1. Original question

Two hypothetical photodetectors satisfy

```math
D_A^*=D_B^*
```

but have radically different temporal responses. Does equal conventional specific detectivity imply equal ability to detect arbitrary optical signals?

---

## 2. Surviving logical chain

### Steps 01–04 — scalar and magnitude-only `D*`
Equal scalar reference `D*` does **not** determine arbitrary temporal-signal SNR; an explicit 1 Hz construction gave `SNR_A/SNR_B~6.36`. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation stationary-Gaussian maximum-SNR problem. **NEGATIVE RESULT:** unknown timing alone does not break that ideal equivalence. Finite observation can because magnitude-only `D*(f)` discards temporal phase/placement.

### Steps 05–12 — finite records and timing-search task
Derived finite-record optimal SNR and task-level detection time. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by unknown-time search burden. **REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. **NEGATIVE RESULT:** no finite interior integration-duration optimum in the original scaled family.

### Step 13 — rough hard-window obstruction
Finite hard-window ideal-white-noise scans have

```math
R_x(y)=1-a_x|y|+O(y^2)
```

and are locally Brownian-like. **FAILED NUMERICAL ESTIMATE:** rough-grid crossover near `ell~49` moved under refinement and is invalid.

### Steps 14–19 — genuine timing bandwidth and fixed physical signal/noise
A genuine finite timing-information bandwidth removes the cusp. Exact smooth Palm rare-event identity is available; Rice/EC is an upper bound and nonuniform as bandwidth grows. With common physical bandwidth `kappa_i=Omega_B tau_i`, forcing accessible eventual SNR equal gives no finite optimum. Holding the physical signal/noise fixed restores bandwidth-dependent accessible SNR and yields a finite large-`r` optimum; later Palm work confirms a shallow optimum broadly near `kappa~50–65`, only `~0.3–0.4%` above infinity.

### Steps 20–23 — finite-`r` Rice reversal corrected, Palm map, rough endpoint
For

```text
r=2, rho_full=6.2407571, alpha=1e-6, beta=0.90, Lambda=0.895
```

converged Rice produced apparent switches at `25.4898402` and `130.1945883`. Continuous Palm preserves only

```math
kappa_cross^Palm ~ 21.7 +/- 0.3
```

and **INVALIDATES** the upper Rice switch. Palm maps the high-band finite-`r` boundary near `Lambda~0.91` around `kappa_f~60–200`; high-band slow-preferred tasks still exist above that boundary. Exact occupation-time importance sampling at `kappa=infinity` gives

```math
Lambda_cross^infinity ~ 0.905 +/- 0.004,
X ~ 7.75.
```

Thus `Lambda=0.895` remains fast-preferred at the rough endpoint.

### Steps 24–28 — two-parameter tangent, generalized Pickands, Bessel correction
Finite bandwidth adds

```math
zeta=kappa/(sqrt(2)u sqrt(b)).
```

**REJECTED SHORTCUT:** `H_mix(chi)` alone is only the infinite-band endpoint. Generalized Pickands/Dieker–Yakir structure is two-parameter. Brown–Resnick Slepian comparison proves local monotonicity but not physical-boundary monotonicity. Common-white-noise coupling gives the rough/smoothed path scale. **INVALIDATED INTERMEDIATE:** `0.8131` was the wrong RMS coefficient; correct pointwise value is `0.8906480701 sqrt(chi/zeta)`. Two-sided-BES(3) Brownian-extremum zoom-in identifies a positive `zeta^-1/2` Gaussian-mollifier correction under stable-convergence/localization/UI.

### Steps 29–30 — Brownian–parabola crossover and canonical function
Small `chi` introduces

```math
h_chi=sqrt(2)chi^(1/3),
m_chi=2chi^(2/3),
mu=sqrt(2)zeta chi^(1/3).
```

At the `r=2` endpoint,

```math
mu_f~0.009776 kappa_f,
mu_s~0.16139 kappa_f.
```

The difficult small-`chi` fast crossover reduces to the canonical Brownian-minus-parabola function

```math
F(mu)=(2/sqrt(pi)) E[M_infinity-M_mu].
```

Representative continuum values are `F(0)~.892`, `F(.5,1,2,3,5,10,20)~.806,.729,.597,.512,.410,.297,.213`, with `sqrt(mu)F(mu)->~0.98`. **INVALIDATED NUMERICAL INTERPRETATION:** raw Step-27 tiny-`chi` fast values were biased low by rough-maximum grid under-resolution. Refined full-field values agree with the canonical function at percent level. Fast asymptotic `C_H` refines to about `0.0088`.

### Step 31 — Palm-anchored universal high-band bridge
Insert `F(mu)` into the finite-`u` coupled tangent boundary and anchor only the residual finite-threshold offset to Palm points plus the occupation endpoint. The central bridge has one shallow maximum near `kappa_f~94.9`, `Lambda_max~0.91068`, then decreases toward `Lambda_infinity~0.90513`. **NUMERICAL CLOSURE:** for the original `Lambda=0.895` task, no bounded high-band re-entrant pocket is numerically supported. **CONDITIONAL:** the Step-31 finite-`u` discrepancy law was empirical.

### Step 32 — direct finite-`u` Rice moment enclosure
For a smooth finite-band scan define

```math
X_u=1_{z(0)<=u} N_u^+,
```

so exactly

```math
P_FA=Q(u)+P(X_u>=1).
```

First-/second-order Rice moments give

```math
Q(u)+m1^2/(lambda+lambda2) <= P_FA <= Q(u)+m1.
```

At `Lambda=0.895`, `X=7.04`, fast upper is below `alpha` and slow lower above `alpha` through at least `kappa_f=170`. **PARTIAL CERTIFICATE.** Around `175–200`, the bound loses sharpness because one physical slow-channel excursion contains many micro-upcrossings. **NEGATIVE RESULT:** raw crossing multiplicity is the wrong rough-tail variable.

### Step 33 — excursion-cluster moment renormalization
Choose `Delta>0`, set `a=u-Delta`, and decompose `{t:z(t)>a}` into connected components. Count only components whose maximum exceeds `u`; call this `C_Delta`. Pathwise,

```math
sup z>u iff C_Delta>=1.
```

For fixed amplitude gap, `C_Delta` remains finite on continuous compact paths even as raw level-`u` crossings proliferate. The exact moment enclosure is

```math
E[C_Delta]^2/E[C_Delta^2] <= P_FA <= E[C_Delta].
```

Under lower-level occupation-Palm `Q_a`, with selected-component duration `L`, success indicator `S`, and total successful count `C_Delta`,

```math
E[C_Delta]=ell Q(a)E_a[S/L],
E[C_Delta^2]=ell Q(a)E_a[S C_Delta/L].
```

At `X=7.16`, `Delta=0.15`, cluster bounds separate fast/slow at `kappa_f=300`, `1000`, and directly at `infinity`. Rough endpoint (`50000` paths, grid `~0.001`): fast lower-upper `0.98940–0.98968 alpha`, slow `1.22367–1.22583 alpha`. **NUMERICAL ENDPOINT CERTIFICATE / CLUSTER-RENORMALIZED ENCLOSURE.**

### Step 34 — adaptive paired cluster tail closure
Use

```math
q=kappa_f^(-1/2)
```

so the unresolved tail is finite: `0<=q<=0.0767` corresponds to `infinity>=kappa_f>=~170`. Common-random-number pairing of the fast first cluster moment to the rough endpoint reduces variance dramatically. Dense paired `q` scan plus nested-grid checks gives a conservative numerical fast envelope

```math
U_f/alpha ~<0.99955<1,
```

while a conservative slow envelope remains

```math
L_s/alpha ~>1.10>1.
```

**PAIRED NUMERICAL INTERVAL CLOSURE:** at common witness time `X=7.16`, the original `Lambda=0.895` task is numerically separated over `170<=kappa_f<=infinity` without the Step-31 empirical `delta(kappa)` fit. **QUALIFICATION:** the Monte Carlo/grid/inter-node allowances are measured numerical scales, not theorem-level continuity bounds.

### Step 35 — analytic `q`-coupling continuity and obstruction
Define

```math
I_x(q)=int |H_x(w)|^2 exp(-w^2 q^4) dw,
A_q(w)=|H_x(w)| exp(-w^2 q^4/2)/sqrt(I_x(q)).
```

Then exactly

```math
dA_q/dq=-2q^3(w^2-M2(q))A_q,
```

and

```math
||dA_q/dq||_2^2=4q^6 Var_q(w^2).
```

For the finite-window tail `|H_x(w)|^2~(x e^-x)^2/w^2`,

```math
lim_{q->0} ||dA_q/dq||_2^2
=2 sqrt(pi) (x e^-x)^2/I_x(0),
```

so the normalized Gaussian field is regular in `q` even at the rough endpoint.

Common-white-noise coupling therefore gives

```math
SD[z_q(t)-z_r(t)] <= L_x^* |q-r|.
```

For the fast Step-34 channel (`x=7.16`), deterministic spectral quadrature gives `||dA/dq||~0.00836` at `q=0`, rising to about `0.01493` at `q=0.0767`. Thus for `Delta q=0.005`, pointwise RMS change is bounded at about `7.5e-5`. The available threshold satisfies

```math
u'(q)=-2q^3 M2(q)rho(q),
```

with max fast `|u'|~5.6e-3`, so threshold motion across the same cell is only about `2.8e-5`.

Exact event sandwich: if `||z_q-z_r||_inf<=epsilon`, with `delta=epsilon+|u_q-u_r|`, then

```math
p_q(u_q+delta)-eta <= p(r) <= p_q(u_q-delta)+eta,
eta=P(||z_q-z_r||_inf>epsilon).
```

**REJECTED SHORTCUT:** the excursion-cluster count/moment is not pathwise Lipschitz because arbitrarily small perturbations can merge/split lower components, flip a component maximum across `u`, or amplify the Palm weight `1/L` for a short component.

**NEGATIVE RESULT:** generic Gaussian-supremum anti-concentration is far too coarse at `alpha=1e-6`. The standard bound `P(|sup X-y|<=epsilon)<=4 epsilon(E sup X+1)` already gives at least `4e-4=400 alpha` for `epsilon=1e-4`, while Step 34's empirical inter-node budget was `6e-10` absolute. The remaining theorem gap is therefore a **tail-sensitive rare-successful-cluster continuity law**, not process continuity in `q`.

See `Q_COUPLING_CONTINUITY_OBSTRUCTION_STEP.md` and `numerics/q_coupling_continuity.py`.

---

## 3. Current frontier

The high-band Gaussian field itself is analytically regular in `q=kappa_f^-1/2`. What is missing is a high-threshold continuity estimate whose probability scale follows the rare successful-excursion intensity near `u~5`, rather than an order-one global Gaussian supremum density.

### Single next question — DO NOT ANSWER YET

> Can the successful-excursion cluster representation yield a tail-sensitive buffered-threshold continuity bound near `u~5`, so that the probability of a cluster whose maximum lies in `[u-delta,u+delta]` scales like the rare-event intensity times `delta` rather than the global `O(delta)` Gaussian anti-concentration bound?

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
- Step-31 empirical `delta(kappa)` is exact or still necessary for the original high-band conclusion;
- Step-32 raw crossing moments stay sharp in the rough limit;
- Step-33/34 Monte Carlo estimates are formal interval arithmetic;
- Step-34 is theorem-level continuous-parameter closure;
- Step-35 process Lipschitz continuity implies cluster-moment Lipschitz continuity;
- generic Gaussian anti-concentration is sharp enough for this rare-event scale;
- no re-entrant pocket can occur for other task parameters;
- Palm bandwidth optimum is unique or exactly located;
- any GHz translation is a hardware recommendation;
- novelty.
