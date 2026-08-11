# AGENTS.md — Research Recovery and Scientific Integrity Protocol

**Repository:** `Kajin-0/gedanken_3`  
**Active experiment:** `experiments/01-equal-dstar-different-speed/`  
**Current mode:** first-principles photodetector thought experiment. Twenty-one logical steps completed. Step 21 applies the exact continuous Palm rare-event structure to the finite-r fixed-physics bandwidth sweep. The lower slow-to-fast bandwidth reversal survives at `kappa_f ~21.7 +/-0.3`; the reported Step-20 upper Rice switch near `130.19` is invalidated. No universal replacement metric and no novelty claim.

Read this file first, then:

1. `experiments/01-equal-dstar-different-speed/CURRENT_STATE.md`
2. `experiments/01-equal-dstar-different-speed/PROGRESS_LOG.md`
3. dedicated step files in chronological order
4. latest: `experiments/01-equal-dstar-different-speed/PALM_CORRECTED_FINITE_R_BANDWIDTH_STEP.md`
5. latest numerical helper: `experiments/01-equal-dstar-different-speed/numerics/finite_r_palm_validation.py`

The repository follows the physics rather than a predetermined criticism of `D*`. Preserve assumptions, cancellations, counterexamples, negative results, rejected shortcuts, failed numerical estimates, numerical validations, invalidations, asymptotic limits, refinements, and unresolved branches.

---

## 1. Mandatory repository protocol

Before every material write:

1. fetch live `main` / current target;
2. inspect intervening changes when needed;
3. fetch the exact current blob SHA before replacing an existing file;
4. never overwrite stale state;
5. preserve failed/corrected branches and explain why they changed;
6. make narrow edits or explicit compact consolidations;
7. update `CURRENT_STATE.md` whenever the scientific frontier changes;
8. append or explicitly consolidate `PROGRESS_LOG.md` for consequential work.

**Live `main` overrides chat summaries, memory, and stale recovery notes.**

---

## 2. Epistemic labels

Use explicitly where useful:

- **DEFINED** — convention/model definition.
- **ASSUMED** — idealization introduced for the thought experiment.
- **DERIVED** — follows mathematically from stated assumptions.
- **COUNTEREXAMPLE** — construction sufficient to disprove an implication.
- **CONDITIONAL** — true only under listed assumptions.
- **REFINEMENT** — sharpens a prior statement without erasing it.
- **NEGATIVE RESULT** — candidate effect tested and absent under stated model.
- **REJECTED SHORTCUT** — tempting inference shown not to answer the actual question.
- **FAILED NUMERICAL ESTIMATE** — failed convergence/validation; never reuse as a result.
- **NUMERICAL VALIDATION** — survived stated numerical cross-checks within scope.
- **NUMERICAL COUNTEREXAMPLE** — converged construction disproves a broader implication within stated approximation/model.
- **INVALIDATED** — previously reported result shown not to survive the stronger calculation.
- **ASYMPTOTIC** — derived only in a controlled limiting regime.
- **OPEN** — not established.
- **NON-CLAIM** — deliberately not asserted.

Do not use `novel`, `universal`, `fundamental`, `first`, etc. without a separate prior-art audit.

---

## 3. Original question

Two detectors satisfy

```math
D_A^*=D_B^*
```

but initially have

```math
\tau_A=1\ \mathrm{ns},
\qquad
\tau_B=1\ \mathrm{s}.
```

Does equal conventional specific detectivity imply equal ability to detect an arbitrary optical signal?

---

## 4. Compact surviving chain

### Steps 01–04
Equal scalar reference `D*` does not determine arbitrary temporal-signal SNR. Complete magnitude `D*(f)` is sufficient only for the restricted known-waveform/full-observation maximum-linear-SNR problem. Unknown timing alone does not break that ideal stationary-Gaussian equivalence, but finite windows can because magnitude `D*(f)` discards phase/temporal placement.

### Steps 05–08

```math
\rho_t^2=\langle s_t,C_t^{-1}s_t\rangle,
```

and known-time Gaussian detection obeys

```math
P_D(t;\alpha)=\Phi[\rho_t-\Phi^{-1}(1-\alpha)].
```

Unknown timing raises a global threshold governed by timing-scan covariance, not digital sample count.

### Step 09
**REJECTED SHORTCUT:** finite-window SNR accumulation cannot be mixed directly with full-template timing bandwidth. For the controlled time-scaled family, faster SNR acquisition can be outweighed by unknown-time search burden.

### Steps 10–12
Task-level detection time:

```math
\mathcal T_D(\alpha,\beta,L)
=\inf\{t:\rho_t-\gamma_t(L,\alpha)\ge\Phi^{-1}(\beta)\}.
```

The scaled family has a fast/slow task boundary. **NEGATIVE RESULT:** no finite interior integration-duration optimum exists in that original family.

### Step 13
The ideal-white-noise finite hard window is locally Brownian-like:

```math
R_x(y)=1-a_x|y|+O(y^2).
```

**FAILED NUMERICAL ESTIMATE:** the rough-grid `ell~49` crossover is invalid.

### Steps 14–15
A genuine finite timing-information bandwidth removes the cusp. The smooth surrogate

```math
J_{x,\kappa}(\nu)=|H_x(\nu)|^2e^{-(\nu/\kappa)^2}
```

has controlled correlated-scan numerics.

### Step 16
Exact smooth one-dimensional Palm identity:

```math
\boxed{
P_{FA}(u)
=Q(u)+\lambda_u
E_\uparrow\!\left[
\frac{1_{\{z(0)\le u\}}}{N_u^+}
\right]
}
```

Rice/EC is an upper bound; its error is multiple excursions plus endpoint overlap.

### Step 17
A compact high-threshold crossover law follows in the isolated-excursion limit. Rice accuracy is **not uniform** as finite-window bandwidth tends to infinity:

```math
\sigma_\kappa^2(x)\sim a_x\kappa/\sqrt\pi.
```

### Step 18
With one shared physical bandwidth and accessible SNR artificially forced equal, the large-r crossover transitions from electronics-limited `~1/Omega_B` to detector-limited `~tau_f`. **NEGATIVE RESULT:** no finite bandwidth optimum under that artificial normalization.

### Step 19
Hold physical signal/noise fixed while bandwidth varies. SNR loss near wide band is `O(1/kappa^2)` while timing-search simplification is `O(1/kappa)`. **DERIVED / CONDITIONAL:** a finite large-r Rice bandwidth optimum exists; Palm spot checks preserve finite-vs-infinite ordering.

### Step 20
At finite `r=2`, common physical bandwidth without SNR renormalization gives the slower detector a narrow-band SNR advantage with

```math
\rho_{\infty,s}/\rho_{\infty,f}\to\sqrt r.
```

Finite-duration Rice produced two apparent bandwidth switches:

```text
25.4898402
130.1945883
```

and apparent topology `slow -> fast -> slow`. Spectral quadrature was converged, but exact Palm validation was explicitly open.

### Step 21 — current frontier
For candidate duration `x`, use

```math
u_{avail}=\rho(x)-\Phi^{-1}(\beta)
```

and test directly

```math
P_{FA}^{Palm}(u_{avail})\le\alpha.
```

#### Lower switch survives
Palm balance plus local-grid refinement gives

```math
\boxed{\kappa_{\times,1}^{Palm}\approx21.7\pm0.3.}
```

About `15%` below Rice `25.49`.

#### Upper Rice switch fails
At `kappa_f=130`:

```text
X=7.0: fast P_FA/alpha~0.9918, slow~1.2668
X=7.5: fast~0.9897, slow~1.0444
```

Fast meets the task while slow does not. The same ordering is seen at Palm-checked `kappa_f=160` and `300`.

**INVALIDATED:** `kappa_cross_2^Rice ~=130.1945883` as a continuous Palm switch.

Cause: nonuniform Rice micro-upcrossing overcount, especially severe for the shorter slow-detector finite window.

Directly validated topology through `kappa_f<=300`:

```math
\boxed{\text{slow}\to\text{fast}.}
```

**OPEN:** a different high-band Palm reversal is not rigorously excluded.

---

## 5. Current frontier

Map the Palm-corrected boundary in

```text
(Lambda, kappa_f)
```

well enough to determine:

1. whether the high-band slow-preferred region disappears entirely;
2. whether the Step-19 finite-bandwidth optimum survives as a true maximum of the Palm-corrected boundary.

---

## 6. Scope boundary

Do not claim:

- faster detectors are universally better or worse;
- a universal speed-detectivity tradeoff or scalar replacement for `D*`;
- the Step-13 `ell~49` result is valid;
- arbitrary low-pass filtering is a true information-band limitation;
- the Gaussian information weighting is a literal circuit transfer function;
- Rice is uniformly accurate at high finite-window bandwidth;
- Step-20's double reversal is an exact physical result;
- no high-band Palm reversal can exist anywhere without a full boundary proof;
- Step-19's exact Palm optimum has been solved;
- any GHz translation is a hardware recommendation;
- novelty.

Unknown amplitudes/phases, signal-dependent noise, sequential stopping, nonlinear response, saturation, dead time, nonstationarity, and globally optimal non-Gaussian decisions remain untouched.

---

## 7. Single next question — DO NOT ANSWER UNTIL PROMPTED

> Can the full Palm-corrected preference boundary in `(Lambda,kappa_f)` be mapped well enough to determine whether the high-band slow-preferred region disappears entirely, and whether the finite bandwidth optimum from Step 19 survives as a true Palm boundary maximum?
