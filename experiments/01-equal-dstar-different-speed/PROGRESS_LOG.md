# Progress Log — Experiment 01

**Consolidation note — 2026-08-11 18:42 EDT:** compact chronology preserving every consequential scientific result, correction, failed shortcut, invalidated numerical estimate, numerical validation, asymptotic qualification, and current stopping point. Full derivations live in dedicated step files.

---

## Steps 01–04 — scalar `D*`, full-observation equivalence, finite-window phase
- Equal scalar reference `D*` does not guarantee equal arbitrary temporal-signal SNR; explicit 1 Hz counterexample gave `SNR_A/SNR_B~6.36`.
- For known waveform/full observation, `rho_inf^2 = integral |P|^2 |G|^2/S_n df = A^-1 integral |P|^2 D*^2 df`.
- **NEGATIVE RESULT:** unknown timing alone does not break complete-magnitude `D*(f)` equivalence under stationary Gaussian full observation.
- Finite windows can break equivalence; causal all-pass construction removes pure-delay loophole.

## Steps 05–08 — finite-record SNR and timing search
Derived `rho_t^2=<s_t,C_t^-1 s_t>` and Gaussian deadline detection. Unknown timing raises a global threshold governed by timing-scan covariance, not digital sample count.

## Step 09 — finite-deadline ranking reversal
**REJECTED SHORTCUT:** finite-window SNR cannot be mixed directly with full-template timing bandwidth. In the controlled `t exp(-t/tau)` family, faster SNR accumulation can be offset by larger unknown-time search burden.

## Steps 10–12 — task surface and fast/slow boundary
Defined `T_D(alpha,beta,L)` and scaled boundary `X_D(r ell)-r X_D(ell)=0`.

**NEGATIVE RESULT:** no finite interior integration-duration optimum exists in the original scaled family.

## Step 13 — rough finite-window obstruction
`R_x(y)=1-a_x|y|+...`; finite hard-window ideal-white-noise scan is locally Brownian-like.

**FAILED NUMERICAL ESTIMATE:** Step-13 `ell~49` crossover is invalid.

## Steps 14–15 — genuine finite timing-information bandwidth
**REJECTED SHORTCUT:** invertible common low-pass is not necessarily a true information limit. Smooth Gaussian information weighting removes the cusp and gives controlled correlated-scan numerics.

## Step 16 — exact Palm rare-event identity

```math
P_{FA}=Q(u)+\lambda_u E_\uparrow[1_{z(0)\le u}/N_u^+].
```

Rice/EC is an upper bound; Palm importance sampling makes `alpha=1e-6` practical.

## Step 17 — nonuniform Rice limit and extreme speed ratio
For finite hard windows `sigma_kappa^2 ~ a_x kappa/sqrt(pi)`, so Rice accuracy is nonuniform as bandwidth grows. Co-scaled large-r crossover tends to fast full-template feasibility edge.

## Step 18 — common physical bandwidth, accessible SNR forced equal
With `kappa_i=Omega_B tau_i`, crossover moves from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`.

**NEGATIVE RESULT:** no finite bandwidth optimum under artificial equal-accessible-SNR normalization.

## Step 19 — fixed physical signal/noise; finite bandwidth optimum
Restoring bandwidth-dependent accessible SNR gives wide-band SNR loss `O(1/kappa^2)` but timing-search simplification `O(1/kappa)`.

**DERIVED / CONDITIONAL:** large-r Rice unknown-time objective has a finite bandwidth optimum. Initial Palm spot check preserved finite-vs-infinite ordering.

## Step 20 — finite-r Rice double reversal
For `r=2`, `rho_full=6.2407571`, `alpha=1e-6`, `beta=0.90`, `Lambda=0.895`, converged finite-duration Rice gave apparent switches at `25.4898402` and `130.1945883`, i.e. apparent `slow -> fast -> slow`.

## Step 21 — Palm correction changes topology
Use `u_avail=rho(x)-Phi^-1(beta)` and test `P_FA^Palm(u_avail)<=alpha` directly.

- Lower switch survives at `kappa_f~21.7 +/-0.3`.
- **INVALIDATED:** upper Rice switch `130.1945883` is not a Palm switch.
- Palm checks at `kappa_f=130,160,300` keep fast preferred for `Lambda=0.895`.
- Cause: nonuniform Rice micro-upcrossing overcount, especially severe for shorter slow-detector finite window.

## Step 22 — 18:42 EDT — Palm boundary map and survival of finite optimum
Mapped representative finite-r Palm boundary points by locally iterating the exact Palm correction factors:

```text
kappa_f     Lambda_cross^Palm
~10         ~0.794
~20         ~0.891
21.7         0.895
30          ~0.9052
60          ~0.9098
100         ~0.9103
200         ~0.9099
```

**REFINEMENT:** the high-band slow-preferred region does **not** disappear. Palm correction lifts the boundary above `Lambda=0.895`; the Step-20 second crossing disappears for that slice while larger-`Lambda` tasks remain slow-preferred.

Performed higher-statistics large-r full-template Palm scan:

```text
kappa       ell_crit^Palm
50          ~0.91162
55          ~0.91185
60          ~0.9120
65          ~0.91136
infinity    ~0.90897
```

Independent `kappa=60` runs and a `30000`-path infinite-band run resolve a finite-band advantage of roughly `0.3–0.4%` at several combined standard errors.

**NUMERICAL VALIDATION / CONDITIONAL:** Step-19 finite bandwidth optimum survives exact rare-event correction. Palm makes it shallower and broadens/shifts its location to approximately `kappa~50–65`. No uniqueness claim.

Full derivation: `PALM_BOUNDARY_MAP_STEP.md`.  
Code: `numerics/palm_boundary_map.py`.

---

## Current stopping point

Palm mapping now distinguishes two facts that Step 21 alone could not:

1. the high-band slow-preferred side of the finite-r task boundary survives, but the boundary is lifted to about `Lambda~0.91` in the tested range;
2. the large-r finite bandwidth optimum survives Palm correction, with only a shallow `~0.3–0.4%` gain over infinite bandwidth for the calibration used.

### Single natural next question

> Can the high-band finite-r Palm boundary be derived asymptotically by matching the finite-hard-window rough excursion law to the smooth full-template limit, so that the `kappa_f -> infinity` boundary and the possibility of any additional reversals can be settled analytically rather than by Monte Carlo mapping?
