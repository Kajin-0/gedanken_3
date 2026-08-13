# Task-dependent photodetector ordering under unknown arrival time

**Target:** Applied Optics — Research Article  
**Status:** journal-facing Rev. 4 / referee comments triaged / robustness additions incorporated / not yet template-formatted  
**Date:** 2026-08-13

## Abstract

With eventual event-specific sensitivity held fixed, a shorter photodetector response time accelerates known-arrival transient measurements but enlarges the normalized timing search when arrival is uncertain. We analyze causal optical-to-electrical channels with equal eventual matched-filter SNR under a batch global-false-alarm scan. We prove a fast-to-slow crossover of the **sufficient post-window guarantee time**, not of the exact scan detection time. A continuous Rice/Slepian witness gives slow-only guarantee feasibility, complete-scan Monte Carlo points in the same direction, and a single-pole corollary shows that the crossover mechanism is not unique to the double-pole construction.

---

# 1. Introduction

Specific detectivity, `D*`, is a useful photodetector figure of merit when its operating and measurement conditions are stated. It is not, however, a complete descriptor of arbitrary transient measurements. Pulse and energy detection have long been treated using frequency-dependent detector sensitivity rather than a single scalar value [1], and detector characterization has long separated sensitivity from temporal bandwidth [2,3]. Modern characterization guidance likewise emphasizes the measurement conditions under which detector figures of merit are evaluated [4].

The present paper does not revisit those established points. Nor does it claim that a faster detector must be worse. Instead, it asks a narrower task-level question: **if two detector channels are normalized to have the same eventual matched-filter SNR for one specified optical event, does the faster channel necessarily require less measurement time when the event arrival time is uncertain?**

The answer depends on the acquisition protocol. In some known-signal settings, optimal processing can strongly reduce or even remove the effect of a detector time constant on overall efficiency [5]. Unknown arrival introduces a different constraint: a receiver must search a timing interval, and a fixed global false-alarm probability is then controlled by the maximum of a correlated random process rather than by the statistic at one known time [6–8]. Classical spread-spectrum acquisition, optical code acquisition, and direct-detection ranging already contain uncertainty-region, dwell-time, detection-probability, false-alarm, and search-strategy tradeoffs [9–14]. Those ingredients are established prior art.

The remaining question is what happens when the **detector time scale itself** simultaneously changes two things while eventual event-specific sensitivity is held fixed:

```text
shorter detector time scale
    -> faster accumulation of matched-filter evidence,

but also

shorter detector time scale
    -> shorter timing-scan correlation length
    -> larger normalized search over the same physical arrival-time interval.
```

The construction intentionally removes the ordinary sensitivity-speed/noise-bandwidth tradeoff by normalizing eventual matched-filter SNR while holding the output-noise convention fixed. The effect studied here is therefore **separate from** the conventional increase of detector noise with measurement bandwidth. The purpose is to isolate the timing-search mechanism after that familiar tradeoff has been removed as a confounding variable.

We first construct a causal time-scaled detector family for which this competition can be analyzed exactly. The receiver uses one global noise-only threshold and a conservative true-alignment condition that guarantees the complete scan has detection probability at least `beta`. The resulting quantity is therefore a **sufficient batch guarantee time**, not an intrinsic detector latency and not the exact first crossing time of the full signal-present scan.

The main scaling relation is

```math
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

At known arrival the faster channel wins. At a finite timing uncertainty we give a continuous-time example in which the slower channel remains guarantee-feasible while the faster channel is already guarantee-infeasible. The general feasibility structure then implies at least one fast-to-slow **sufficient-guarantee-time** crossover under ordinary continuity regularity.

Two robustness checks are added. First, exact state-space Monte Carlo of the complete full-template signal-present scan shows the same slow/fast separation at the witness point. Second, a standard first-order single-pole detector family satisfies the same covariance-ordering and feasibility argument, so the crossover mechanism is not unique to the critically damped double-pole example used for the analytic continuum witness.

---

# 2. Model and decision protocol

## 2.1. Common optical event and causal detector family

All channels receive the same optical event

```math
p(t)=e^{-bt}u(t),
\qquad b>0,
```

with Laplace transform

```math
P(s)=\frac{1}{s+b}.
```

For detector time scale `tau>0`, define the causal, stable, proper transfer function

```math
\boxed{
G_\tau(s)=A_\tau\frac{s+b}{(s+1/\tau)^2}.
}
```

Here `G_tau` is interpreted as a linear small-signal optical-to-electrical channel for the selected event; its purpose is to isolate temporal response rather than a particular microscopic carrier-transport mechanism. Then

```math
G_\tau(s)P(s)=\frac{A_\tau}{(s+1/\tau)^2},
```

and the output signal is

```math
\boxed{
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
}
```

The pole-zero matching is a controlled **existence construction**; it is not proposed as a generic microscopic model of a specific photodetector material or architecture. Its impulse response is

```math
\boxed{
g_\tau(t)=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac{1}{\tau}\right)t\right]u(t).
}
```

For a finite fast/slow pair with `tau_f<tau_s`, choosing `b>=1/tau_f` makes both impulse responses nonnegative. After the pole-zero cancellation in the selected event response, all SNR, covariance, threshold, and guarantee-time equations used below are independent of `b`; `b` remains only in the physical realization constraint.

## 2.2. Equal eventual matched-filter SNR

Let the additive output noise be zero-mean white Gaussian noise with

```math
\boxed{E[n(t)n(t')]=N\delta(t-t').}
```

With this convention,

```math
\rho^2=\frac{1}{N}\int s^2(t)dt.
```

For the complete waveform,

```math
\rho_{\tau,\infty}^2
=\frac{A_\tau^2\tau^3}{4N}.
```

Choosing

```math
\boxed{
A_\tau=\frac{2\rho_0\sqrt N}{\tau^{3/2}}
}
```

gives

```math
\boxed{\rho_{\tau,\infty}=\rho_0}
```

for every channel. This normalization is **event-specific** and is distinct from equality of a scalar conventional `D*`. It is imposed only to remove eventual matched-filter sensitivity advantage for the selected optical event. It also deliberately suppresses the usual detector bandwidth/noise tradeoff; any ordering reversal obtained below is therefore not produced by assigning the faster detector a larger white-noise floor.

For a post-arrival integration duration `t`, let

```math
x=\frac{t}{\tau}.
```

The fraction of total squared matched-filter SNR accumulated by `x` is

```math
\boxed{
\eta(x)=1-e^{-2x}(1+2x+2x^2),
}
```

so

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
}
```

Because

```math
\eta'(x)=4x^2e^{-2x}>0,
```

shorter `tau` always accumulates a given fraction of the eventual evidence sooner in physical time.

**Figure 1** (`paper_a_fig1_evidence`) plots `rho_{tau,t}/rho_0` for `tau_s=6 tau_f`. It shows the unambiguous known-arrival advantage of the faster channel before any timing-search penalty is introduced.

## 2.3. Timing scan and batch acquisition clock

The normalized finite template is proportional to

```math
h_x(v)=v e^{-v}1_{[0,x]}(v).
```

Under noise alone, scanning it across candidate arrival times produces a unit-variance stationary Gaussian process. For dimensionless lag `0<=y<x`, its covariance is

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}dv
}{
\int_0^xv^2e^{-2v}dv},
}
```

with `R_x(y)=0` for `y>=x`.

In physical time,

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

Suppose the event arrival time is known only to lie in

```math
0\le\theta\le L.
```

In an optical measurement, `L` can represent an asynchronous transient window, trigger or synchronization uncertainty, a prior time-of-flight/range gate, or another finite timing interval established before the detector record is searched. The theorem requires only that the same physical `L` apply to the channels being compared.

A duration-`t` template must be evaluable even for the latest candidate `theta=L`, so the batch record must extend through `L+t`. The normalized search length is

```math
\boxed{\ell=L/\tau.}
```

Thus reducing `tau` accelerates evidence accumulation but increases the normalized timing-search interval over the same physical `L`.

As the integration duration becomes long compared with `tau`, the timing covariance becomes

```math
\boxed{
R_\infty(y)=(1+y)e^{-y},
\qquad y\ge0.
}
```

In physical lag units this is

```math
R_\tau(\Delta)
=\left(1+\frac{|\Delta|}{\tau}\right)
\exp\left(-\frac{|\Delta|}{\tau}\right).
```

**Figure 2** (`paper_a_fig2_covariance`) plots this covariance for the same `r=6` pair over one common physical uncertainty interval `L=9 tau_f`. The faster channel's timing statistic is nearly decorrelated across that interval, whereas the slower channel retains substantial correlation.

## 2.4. Global threshold and sufficient detection guarantee

Let `Z_x(q)` be the normalized noise-only timing scan. Define the global threshold

```math
\boxed{
\Gamma(x,\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>u\right]\le\alpha
\right\}.
}
```

No independent-trials approximation is introduced.

Let `q_0` denote the generative true alignment. The receiver is **not** given `q_0`; it still scans the full interval. At `q_0`, the signal-present statistic has unit variance and mean `rho_0 sqrt(eta(x))`, hence

```math
\boxed{
P_{D,true}(x)
=\Phi\left[
\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\right].
}
```

For the complete signal-present scan,

```math
P_D^{scan}(x)
=\Pr\left[\sup_qY_x(q)>\Gamma\right].
```

Since true-alignment crossing is a subset of complete-scan crossing,

```math
\boxed{P_D^{scan}(x)\ge P_{D,true}(x).}
```

Therefore `P_D,true>=beta` is a sufficient condition guaranteeing `P_D^scan>=beta`.

Define

```math
M_G(x;\ell)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
```

and

```math
\boxed{
X_G(\rho_0,\alpha,\beta,\ell)
=\inf\{x>0:M_G(x;\ell)\ge\Phi^{-1}(\beta)\}.
}
```

The required **post-window guarantee time** is

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
}
```

The batch wall-clock time measured from the opening of the arrival window is

```math
T_{wall}=L+T_G.
```

At fixed `L`, the two clocks give identical detector ordering.

### Notation summary

| Symbol | Meaning |
|---|---|
| `tau` | detector response-time scale |
| `tau_f`, `tau_s` | fast and slow channel time scales |
| `r=tau_s/tau_f` | speed ratio |
| `L` | physical arrival-time uncertainty interval |
| `ell=L/tau` | dimensionless search length |
| `rho_0` | common eventual matched-filter SNR for the selected event |
| `alpha` | allowed global false-alarm probability |
| `beta` | requested detection guarantee |
| `Gamma` | finite-template global noise-only scan threshold |
| `Gamma_infinity` | full-template global threshold |
| `X_G` | dimensionless first time satisfying the sufficient guarantee |
| `T_G=tau X_G` | physical post-window sufficient guarantee time |

---

# 3. Results

## 3.1. Response time enters the task twice

For fixed lag `y`, the covariance `R_x(y)` can be written as a positive-weight average of a nondecreasing function of the integration limit. Consequently,

```math
x_2>x_1
\quad\Longrightarrow\quad
R_{x_2}(y)\ge R_{x_1}(y).
```

Slepian comparison [15] then gives

```math
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
```

The signal term `rho_0 sqrt(eta(x))` increases strictly while the threshold does not increase, so the guarantee margin is strictly increasing in `x`. The cross-channel reversal below therefore does not arise from assigning either channel a self-suboptimal integration duration.

The central scaling relation

```math
T_G
=\tau X_G\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right)
```

shows the two roles of detector time scale directly. `tau` multiplies the physical evidence clock, but the same `tau` divides the physical uncertainty interval inside the task function.

## 3.2. Continuous-time feasibility witness

Choose

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=\frac{\tau_s}{\tau_f}=6.
```

These values are chosen to give an analytically transparent finite-scale witness in which the continuous-time upper and lower bounds separate cleanly. They are **not** proposed as a recommended false-alarm specification or as a representative fast/slow detector pair.

At known arrival, the scalar guarantee equation gives

```math
\boxed{x_0=1.80519795247,}
```

so

```math
T_{G,f}(0)=\tau_fx_0
<\tau_sx_0=T_{G,s}(0).
```

The faster channel is therefore exactly preferred when there is no timing uncertainty.

Now take one common physical uncertainty

```math
\boxed{L=9\tau_f=1.5\tau_s.}
```

For a dimensional illustration only, if `tau_f=10 microseconds`, then `tau_s=60 microseconds` and this same point corresponds to `L=90 microseconds`. The result itself is scale-free and does not assume a particular detector material.

The normalized search lengths are

```math
\ell_f=9,
\qquad
\ell_s=1.5,
```

and the full-template feasibility threshold budget is

```math
c=\rho_0-\Phi^{-1}(\beta)
=2.21844843445540.
```

Define `Q(c)=1-\Phi(c)`.

For the slow channel, `R_infinity''(0)=-1`, so Rice's exact mean upcrossing formula [16] gives

```math
\nu_c^+=\frac{1}{2\pi}e^{-c^2/2}.
```

A continuous path exceeding `c` must either start above `c` or contain at least one upcrossing. Therefore

```math
\boxed{
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841<0.05.
}
```

Thus the slow channel is guarantee-feasible.

For the fast channel, take seven points in `[0,9]` separated by `1.5`. Every distinct-pair covariance is at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Compare the sampled process with the equicorrelated Gaussian vector

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i,
\qquad i=1,\ldots,7,
```

where `V,E_1,...,E_7` are independent standard normals. Slepian comparison gives

```math
\Pr[\max_iZ_i>c]
\ge\Pr[\max_iY_i>c].
```

The latter probability is the one-dimensional integral

```math
1-\int_{-\infty}^{\infty}
\phi(v)
\Phi\left(
\frac{c-\sqrt\epsilon v}{\sqrt{1-\epsilon}}
\right)^7dv,
```

which evaluates to

```math
\boxed{
\Pr[\max_iY_i>c]
=0.0624701020698>0.05.
}
```

Since the continuous supremum contains this seven-point maximum, the fast channel is guarantee-infeasible. Hence

```math
\boxed{
P_{FA,s}\le0.0336428
<0.05
<0.0624701\le P_{FA,f}.
}
```

**Figure 3** (`paper_a_fig3_feasibility`) presents these explicitly as a slow-channel upper bound and a fast-channel lower bound. Neither bound is plotted as an exact false-alarm probability. The witness is continuous-time and does not use a timing-grid extrapolation or a numerical estimate of the crossover location.

## 3.3. Feasibility partition and crossover theorem

Define the full-template threshold

```math
\Gamma_\infty(\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_\infty(q)>u\right]\le\alpha
\right\}.
```

Enlarging the search interval enlarges the supremum domain pathwise, so `Gamma_infinity(ell,alpha)` is nondecreasing in `ell`.

Normalized-template `L2` convergence gives

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0,
```

and the corresponding threshold limit is used under ordinary compact-interval Gaussian-supremum/quantile continuity regularity.

Finite guarantee time is possible when

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
<\rho_0-\Phi^{-1}(\beta).
}
```

Because `R_infinity(y)->0`, a Slepian comparison of widely separated samples with an equicorrelated Gaussian vector gives

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\qquad(\ell\to\infty).
```

Thus a finite search-feasibility boundary exists whenever the requested known-time operating point is feasible.

For two channels let

```math
\tau_f<\tau_s,
\qquad
r=\frac{\tau_s}{\tau_f}>1,
\qquad
\ell=\frac{L}{\tau_s}.
```

Then

```math
T_{G,f}=\tau_fX_G(\rho_0,\alpha,\beta,r\ell)
```

and

```math
T_{G,s}=r\tau_fX_G(\rho_0,\alpha,\beta,\ell).
```

The exact sufficient-guarantee-time preference boundary is

```math
\boxed{
B_r(\ell)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
}
```

Let

```math
c=\rho_0-\Phi^{-1}(\beta).
```

Since `Gamma_infinity` is nondecreasing with search length, only three feasibility regimes exist:

```math
\boxed{
\begin{array}{ll}
\text{both feasible:} & c>\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{slow only:} & \Gamma_\infty(\ell,\alpha)<c\le\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{neither:} & c\le\Gamma_\infty(\ell,\alpha).
\end{array}}
```

A fast-only feasibility regime is impossible in this equal-eventual-SNR scaled family.

Define

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<c\}.
```

The physical boundary scales as

```math
L_{crit}(\tau)=\tau\ell_{crit}.
```

For every finite `x`, `eta(x)<1` and `Gamma(x,ell)>=Gamma_infinity(ell)`. At the continuous critical boundary no finite `x` reaches the requested guarantee, so

```math
X_G(\ell)\to\infty
\qquad(\ell\uparrow\ell_{crit}).
```

At `L=0`, fast is preferred as shown above. The fast physical feasibility boundary occurs first,

```math
L_{crit,f}=\tau_f\ell_{crit}
<L_{crit,s}=\tau_s\ell_{crit}.
```

As `L` approaches `L_crit,f` from below, `T_G,f` diverges while the slow channel remains strictly feasible. Continuity therefore implies at least one

```math
\boxed{L_\times\in(0,L_{crit,f})}
```

for which

```math
\boxed{T_{G,f}(L_\times)=T_{G,s}(L_\times).}
```

This proves crossover existence, not uniqueness. It also concerns the **sufficient guarantee time** `T_G`; it does not establish the ordering of the exact first integration times solving `P_D^scan=beta`.

## 3.4. Complete full-template scan validation

The preceding theorem uses the true-alignment event only as a sufficient certificate. To test whether the complete signal-present scan points in the same direction, we numerically evaluate the **full-template** scan at the same witness.

The full-template noise covariance

```math
R_\infty(y)=(1+|y|)e^{-|y|}
```

is Matérn-3/2 and admits the exact stationary state-space realization

```math
\frac{d}{dq}
\begin{bmatrix}Z\\V\end{bmatrix}
=
\begin{bmatrix}0&1\\-1&-2\end{bmatrix}
\begin{bmatrix}Z\\V\end{bmatrix}
+
\begin{bmatrix}0\\2\end{bmatrix}\xi(q).
```

For a full matched signal at true alignment `q_0`, the deterministic scan mean is

```math
m(q)=\rho_0R_\infty(|q-q_0|).
```

We generated `100000` stationary Gaussian paths using the exact matrix-exponential state transition and evaluated nested timing grids `Delta=0.020,0.010,0.005`. The numerical noise-only 95th-percentile threshold sets `alpha=.05`; then the complete scan power is estimated from the maximum of `Z(q)+m(q)`.

At the finest grid, the results are:

| channel | `ell` | tested `q_0/L` | `P_D^{scan,infinity}` |
|---|---:|---|---|
| slow | 1.5 | 0, .25, .50, .75, 1 | 0.9455 to 0.9547 |
| fast | 9 | 0, .25, .50, .75, 1 | 0.8566 to 0.8847 |

The nested-grid values are essentially unchanged across the three spacings. Thus every tested slow-channel arrival placement lies comfortably above `beta=.90`, while every tested fast-channel placement remains below it.

This numerical result is deliberately narrower than a theorem: it does **not** prove that finite-time `P_D^scan(x)` is monotone, nor that the first finite solutions of `P_D^scan(x)=beta` reverse ordering. It does show that, at the controlling finite physical uncertainty, the **complete** full-template scan agrees with the direction of the conservative guarantee witness rather than contradicting it. The calculation is reproduced by `numerics/paper_a_full_scan_validation.py`.

## 3.5. Robustness to a standard first-order detector response

The analytic witness above uses a double-pole family because its smooth full-template covariance permits the simple Rice bound. The crossover mechanism itself does not depend on that choice.

Consider an ideal impulsive optical event and the standard causal first-order channel

```math
G_\tau(s)=\frac{A_\tau}{s+1/\tau},
```

so

```math
s_\tau(t)=A_\tau e^{-t/\tau}u(t).
```

Choosing

```math
\boxed{
A_\tau=\rho_0\sqrt{\frac{2N}{\tau}}
}
```

again gives equal eventual matched-filter SNR `rho_0`. The finite squared-SNR fraction is

```math
\eta_1(x)=1-e^{-2x}.
```

For `0<=y<x`, the finite-template timing covariance is

```math
\boxed{
R_{1,x}(y)
=\frac{e^{-y}-e^{-2x+y}}{1-e^{-2x}},
}
```

with `R_{1,x}(y)=0` for `y>=x`, and

```math
\boxed{R_{1,\infty}(y)=e^{-y}.}
```

For fixed `y>0`, set `a=e^{-2x}`. Then

```math
\frac{\partial R_{1,x}}{\partial a}
=\frac{e^{-y}-e^y}{(1-a)^2}<0,
\qquad
\frac{da}{dx}<0,
```

so

```math
\frac{\partial R_{1,x}(y)}{\partial x}>0.
```

Also `R_{1,x}(y)<R_{1,infinity}(y)` for finite `x`, and `R_{1,infinity}(y)->0` as `y->infinity`. Consequently the same Slepian threshold ordering, finite feasibility boundary, boundary divergence, and intermediate-value argument apply. Under the same continuity regularity, the first-order family therefore also has at least one finite fast-to-slow **sufficient-guarantee-time crossover**.

This corollary is important for interpretation: the ordering reversal is not unique to the critically damped Gamma(2)-shaped output used for the main continuum witness. The double-pole family is retained because its differentiable full-template process makes the finite-scale Rice/Slepian bracket unusually transparent.

---

# 4. Discussion

The result is a failure of **detector-only ordering**, not a failure of detector characterization. A conventional detector specification describes a device under stated conditions. The quantity `T_G` belongs jointly to a detector and a task because the decision threshold depends on the physical arrival-time uncertainty interval, the global false-alarm requirement, and the requested detection guarantee.

The mechanism also differs from a generic sensitivity-bandwidth product. Sensitivity-speed combinations are established detector metrics [2,3]. Here the ordinary sensitivity-speed/noise-bandwidth tradeoff is intentionally removed by the controlled normalization; the remaining decision surface contains the external task variable `L/tau` together with `rho_0`, `alpha`, and `beta`. Compressing these into one detector-only scalar would erase the nuisance-domain dependence responsible for the crossover.

The result should also be read against classical acquisition theory rather than in competition with it. Unknown-delay search penalties, matched-filter acquisition, false alarms, dwell time, and uncertainty-region size are established [6–14]. The specific construction here couples that established acquisition geometry to a detector response scale while holding eventual event-specific matched-filter SNR equal. The contribution is therefore the detector-facing synthesis and explicit ordering result, not the individual ingredients.

In practical optical measurements, the relevant `L/tau` can arise from trigger jitter, asynchronous transient timing, a time-of-flight gate, or another externally supplied arrival-time window. The result therefore does not say that a slower detector is intrinsically preferable. It says that translating detector response time into a task-level operating time requires the timing uncertainty and the global decision rule as well.

The equal-`rho_0` condition is deliberately event-specific. It is not equivalent to equal conventional `D*`, and the theorem does not require the channels to have equal `D*`. The normalization simply removes eventual matched-filter sensitivity advantage for the selected optical event so that the temporal search mechanism can be isolated.

Several limitations are explicit. The channels are linear and time-scaled; output noise is additive, stationary, white, and Gaussian; arrival time is the only nuisance parameter; the main double-pole transfer family is an existence construction; and the receiver is batch. Real detectors may couple response bandwidth, responsivity, and noise through additional device physics that are deliberately absent from this controlled comparison. The first-order corollary shows that the crossover proof is not unique to the double-pole response, but it retains the same equal-eventual-SNR thought-experiment normalization.

Most importantly, the theorem uses

```math
P_D^{scan}\ge P_{D,true}
```

to define a sufficient guarantee. It does **not** prove that the exact finite-time full signal-present scan detection times reverse ordering. The full-template Monte Carlo check makes the conservative-certificate interpretation less concerning at the witness point, but it remains numerical evidence rather than a replacement theorem. Crossover uniqueness is also not established.

These limitations suggest direct extensions. Colored detector noise can be included through whitening and a modified timing covariance; unequal eventual sensitivity introduces an additional task axis; and exact finite-time signal-present scan power would replace the sufficient true-alignment condition with the full composite-alternative probability. Those questions are outside the present result.

For transient detector qualification, the practical implication is modest but important: **response time should be interpreted together with the timing uncertainty and decision protocol, not only as a detector-isolated speed number.** A faster channel can accumulate evidence sooner yet pay a larger global-search penalty because it resolves more timing structure over the same physical uncertainty interval.

---

# 5. Conclusion

A controlled causal photodetector-channel family with equal event-specific eventual matched-filter SNR shows that detector response time can enter an unknown-arrival measurement in two opposing ways. Shorter `tau` accelerates evidence accumulation but increases the normalized search interval `L/tau`. A continuous-time Rice/Slepian witness gives a finite regime where the slow channel remains guarantee-feasible while the fast channel is not. More generally, the **sufficient guarantee time** `T_G=tau X_G(rho_0,alpha,beta,L/tau)` has at least one finite fast-to-slow ordering crossover under the stated continuity regularity.

Two independent robustness checks strengthen the interpretation. Complete full-template scan Monte Carlo at the witness gives `P_D^scan>0.94` for the slow channel and `<0.89` for the fast channel across the tested true-arrival positions, so the exact scan points in the same direction as the conservative certificate. Separately, the same crossover theorem holds for a standard first-order exponential detector response. Neither result proves a finite-time exact-scan crossover, which remains open.

---

## Figure captions

**Fig. 1.** Fraction of eventual matched-filter SNR accumulated versus physical integration time for the fast channel `tau=tau_f` and slow channel `tau=6 tau_f`. Both channels have equal eventual SNR `rho_0`; the faster channel reaches any fixed fraction sooner when arrival time is known.

**Fig. 2.** Full-template timing covariance in physical lag for the fast and slow channels. The same physical arrival-time uncertainty `L=9 tau_f=1.5 tau_s` spans a much larger number of fast-channel correlation lengths, producing the larger normalized search `ell_f=9` compared with `ell_s=1.5`.

**Fig. 3.** One-sided continuum false-alarm bounds at `rho_0=3.5`, `alpha=0.05`, `beta=0.90`, `tau_s/tau_f=6`, and `L=9 tau_f`. The slow-channel value is an **upper bound**, `P_FA,s<=0.0336428`; the fast-channel value is a **lower bound**, `P_FA,f>=0.0624701`. The required global PFA `alpha=0.05` lies strictly between the bounds, proving slow-only guarantee feasibility at this physical uncertainty.

---

## Funding

[Funding statement to be confirmed before submission.]

## Disclosures

[Author disclosure statement to be confirmed before submission.]

## Data availability

The analytical derivations and reproduction scripts supporting the reported continuum feasibility witness, full-template scan validation, and manuscript figures are available in the public research repository `https://github.com/Kajin-0/gedanken_3`, under `experiments/01-equal-dstar-different-speed/`. A versioned archival snapshot should be attached to the final submission package.

---

## References

[1] R. C. Jones, "Energy detectable by radiation detectors," J. Opt. Soc. Am. **50**, 883–886 (1960). DOI: 10.1364/JOSA.50.000883.

[2] J. P. Garcia and E. L. Dereniak, "Extrinsic silicon photodetector characterization," Appl. Opt. **29**, 559–569 (1990). DOI: 10.1364/AO.29.000559.

[3] Y. Yang, et al., "Overcoming the sensitivity–speed trade-off in two-dimensional photodetectors via a functional oxide interlayer," Nat. Commun. **17**, 6077 (2026). DOI: 10.1038/s41467-026-72259-1.

[4] V. Pecunia, et al., "Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies," Nat. Photonics **19**, 1178–1188 (2025). DOI: 10.1038/s41566-025-01759-1.

[5] C. R. Doering and P. M. Harvey, "Optimal signal-to-noise in digital phase lock amplifiers," Appl. Opt. **26**, 633–642 (1987). DOI: 10.1364/AO.26.000633.

[6] R. Vio and P. Andreani, "On the correct estimate of the probability of false detection of the matched filter in weak-signal detection problems," arXiv:1602.02392 (2016).

[7] G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, et al., "The false alarms induced by Gaussian noise in gravitational wave detectors," Phys. Rev. D **107**, 023027 (2023). DOI: 10.1103/PhysRevD.107.023027.

[8] R. P. Croce, Th. Demma, V. Pierro, et al., "Correlator bank detection of GW chirps. False-alarm probability, template density and thresholds: behind and beyond the minimal-match issue," Phys. Rev. D **70**, 122001 (2004). DOI: 10.1103/PhysRevD.70.122001.

[9] A. Polydoros and C. L. Weber, "A unified approach to serial search spread-spectrum code acquisition—Part II: a matched-filter receiver," IEEE Trans. Commun. **32**(5), 550–560 (1984). DOI: 10.1109/TCOM.1984.1096113.

[10] Y.-T. Su, "Rapid code acquisition algorithms employing PN matched filters," IEEE Trans. Commun. **36**(6), 724–733 (1988). DOI: 10.1109/26.2793.

[11] A. B. Milstein, S. M. Oh, D. A. Kashdan, et al., "Acquisition algorithm for direct-detection ladars with Geiger-mode avalanche photodiodes," Appl. Opt. **47**, 296–311 (2008). DOI: 10.1364/AO.47.000296.

[12] M. M. Mustapha and R. F. Ormondroyd, "Dual-threshold sequential detection code synchronization for an optical CDMA network in the presence of multi-user interference," J. Lightwave Technol. **18**(12), 1742–1748 (2000). DOI: 10.1109/50.908711.

[13] A. Keshavarzian and J. A. Salehi, "Optical orthogonal code acquisition in fiber-optic CDMA systems via the simple serial-search method," IEEE Trans. Commun. **50**(3), 473–483 (2002). DOI: 10.1109/26.990909.

[14] A. T. Pham and H. Yashima, "Performance analysis of MDSS code acquisition using SLS for optical CDMA systems," IEICE Trans. Commun. **E88-B**(12), 4570–4577 (2005). DOI: 10.1093/ietcom/e88-b.12.4570.

[15] D. Slepian, "The one-sided barrier problem for Gaussian noise," Bell Syst. Tech. J. **41**, 463–501 (1962). DOI: 10.1002/j.1538-7305.1962.tb02419.x.

[16] S. O. Rice, "Mathematical analysis of random noise," Bell Syst. Tech. J. **23**(3), 282–332 (1944). DOI: 10.1002/j.1538-7305.1944.tb00874.x.
