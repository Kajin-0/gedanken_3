# Paper A major revision — operational guarantee-time repair

**Date:** 2026-08-12  
**Status:** BLOCKING SEMANTIC ISSUES REPAIRED / THEOREM STRENGTHENED / QUANTITATIVE EXAMPLE STILL OPEN / NOVELTY NOT ESTABLISHED

This note records the first major-revision pass after `PAPER_A_ADVERSARIAL_REVIEW_AUDIT.md`. It is intentionally separate from the manuscript so the correction history remains explicit.

---

## 1. What was changed

### 1.1 Detection-time language replaced by an operational guarantee time

The old manuscript used

```math
T_D=\tau X_D(\rho_0,\alpha,\beta,L/\tau)
```

while scanning a duration-`t` template over every candidate arrival in `[0,L]`. That construction implicitly requires data through `L+t`, so `T_D=t` was not an ordinary online latency.

The revised manuscript defines

```math
\boxed{
T_G=\tau X_G(\rho_0,\alpha,\beta,L/\tau)
}
```

as the minimum **post-window integration duration**. The receiver acquires a batch record of length

```math
\boxed{
T_{\rm wall}=L+T_G.
}
```

At fixed `L`, the detector ordering is unchanged because the common `L` cancels from pairwise differences.

### 1.2 The true-alignment criterion is now explicitly a sufficient guarantee

The old quantity

```math
P_{D,\mathrm{true}}
=\Phi[\rho_0\sqrt{\eta(x)}-\Gamma]
```

is retained, but its logical role is now explicit. If `Y_x(q)` is the complete signal-present scan and `q_0` is the true alignment,

```math
\{Y_x(q_0)>\Gamma\}
\subseteq
\{\sup_qY_x(q)>\Gamma\},
```

so

```math
\boxed{
P_D^{\rm scan}\ge P_{D,\mathrm{true}}.
}
```

Therefore `P_D,true>=beta` is a conservative sufficient condition that guarantees complete-scan detection probability at least `beta`.

The revised theorem orders the time required to satisfy this guarantee. It does **not** claim that the exact solutions of `P_D^scan=beta` reverse ordering.

### 1.3 The photodetector realization was restored

The same optical event

```math
p(t)=e^{-bt}u(t)
```

is passed through the causal, proper, stable detector family

```math
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2},
```

which gives

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
```

This prevents the construction from reading as a set of unrelated hand-chosen output templates.

Equal eventual matched-filter SNR is now explicitly described as **event-specific** and stronger/more task-specific than equality of one scalar reference `D*`.

### 1.4 Noise normalization was made explicit

The manuscript now fixes

```math
E[n(t)n(t')]=N\delta(t-t')
```

and therefore

```math
\rho^2=\frac1N\int s^2(t)dt.
```

The existing normalization

```math
A_\tau=2\rho_0\sqrt N/\tau^{3/2}
```

then follows without a factor-of-two ambiguity.

### 1.5 `D*` bandwidth wording was corrected

The revised Introduction distinguishes conventional noise-equivalent measurement-bandwidth normalization in `D*` from detector temporal / `-3 dB` bandwidth.

---

## 2. Proposition 1 was strengthened rather than merely relabeled

The previous proposition carried four assumptions:

1. known-time feasibility;
2. continuity of `X_D`;
3. `Gamma_infty(ell,alpha)->infinity`;
4. divergence of `X_D` at `ell_crit`.

The revision removes assumptions 3 and 4 as independent hypotheses.

### 2.1 Large-search threshold divergence is proved from `R_infty`

The full-template covariance is

```math
R_\infty(y)=(1+y)e^{-y}\to0.
```

For any `epsilon in (0,1)`, sample sufficiently widely separated points so every off-diagonal covariance is at most `epsilon`. Compare those samples by Slepian to the equicorrelated vector

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i.
```

The equicorrelated maximum diverges in probability because `max_i E_i->infinity`. Since the actual process is less correlated, its sampled maximum is stochastically at least as large. Therefore

```math
\boxed{
\Gamma_\infty(\ell,\alpha)\to\infty.
}
```

A finite guarantee-feasibility boundary follows whenever the known-time criterion is feasible.

### 2.2 Boundary divergence is derived

For finite `x`,

```math
\eta(x)<1.
```

The previously proved covariance ordering gives

```math
R_x(y)\le R_\infty(y)
```

and hence by Slepian

```math
\Gamma(x,\ell,\alpha)
\ge\Gamma_\infty(\ell,\alpha).
```

At a continuous critical boundary satisfying

```math
\Gamma_\infty(\ell_{crit},\alpha)
=\rho_0-z_\beta,
```

every finite `x` obeys

```math
M_G(x;\ell_{crit})<z_\beta.
```

A bounded sequence of first-crossing times approaching `ell_crit` would therefore contradict continuity. Thus

```math
\boxed{
X_G(\ell)\to\infty
\quad\text{as}\quad
\ell\uparrow\ell_{crit}.
}
```

The revised proposition now requires only known-time guarantee feasibility plus ordinary threshold/first-crossing continuity in the interior and at the critical boundary.

---

## 3. What was deliberately NOT done

The revision preserves the Step-49 hard stop.

It does not:

- reopen the exact signal-present Gaussian-extremes problem;
- create a Step 50;
- revive the invalid Step-13 `ell~49` rough-grid crossover;
- revive the invalid Step-20 upper Rice reversal;
- treat Step-44 as a continuum certificate;
- treat Steps 47–49 spectral-intensity transfer as an exact finite-`u` false-alarm theorem;
- claim crossover uniqueness;
- claim an online or sequential detection latency theorem;
- claim novelty.

---

## 4. Quantitative example status

The adversarial review correctly requested one robust, non-knife-edge numerical example for the exact Paper A model.

That requirement is **not yet closed**.

The history provides two tempting but unacceptable shortcuts:

1. Step 13's hard-window grid crossover is invalid because the finite hard-window timing process is locally rough and grid maxima converge slowly.
2. Step 44's high-band rough-endpoint witness has a genuine finite-grid statistical certificate but insufficient margin after continuum grid correction.

The smooth finite-information model from Steps 14–16 is numerically well behaved and demonstrates that the mechanism survives regularization, but it is a different model and is not silently substituted for the exact hard-window Paper A theorem.

The next numerical task should therefore be a **new continuum-controlled example chosen for margin first**, not another attempt to rescue the old knife-edge calibration.

---

## 5. Current disposition after this revision

```text
BLOCKING ACQUISITION-CLOCK ISSUE: RESOLVED
BLOCKING TRUE-ALIGNMENT CLAIM-SCOPE ISSUE: RESOLVED BY REFRAMING
COMMON OPTICAL INPUT / DETECTOR REALIZATION: RESTORED
WHITE-NOISE NORMALIZATION: RESOLVED
PROPOSITION ASSUMPTIONS: REDUCED
ROBUST EXACT-MODEL QUANTITATIVE EXAMPLE: OPEN
DEEP NOVELTY / CLOSEST-PRIOR-ART AUDIT: STILL OPEN
```

The manuscript is materially stronger and its main theorem is now aligned with what is actually proved, but it is still **not submission-ready** until the robust exact-model example and final novelty/citation audit are completed.
