# Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR

**Draft status:** Paper A major-revision manuscript / operational semantics repaired / novelty not established  
**Date:** 2026-08-12

## Abstract

Specific detectivity, `D*`, is useful for comparing photodetector sensitivity under stated measurement conditions, but it does not by itself define the outcome of an arbitrary time-dependent detection task. Here we study a narrower question. Two causal linear photodetector channels observe the same optical event and are deliberately normalized to have the same eventual matched-filter signal-to-noise ratio `rho_0`, while their response time scales differ. Event arrival is known only to lie in a fixed physical window of duration `L`. A batch receiver scans all candidate arrival times with a finite-duration matched filter and sets one threshold from the maximum of the correlated noise-only timing scan so that the global false-alarm probability is `alpha`.

To make the acquisition clock explicit, a candidate filter duration `t` requires a record of duration `L+t`: the arrival window closes after `L`, followed by `t` additional integration time so that every candidate arrival receives the same finite post-arrival record. We therefore define `T_G` as the minimum **post-window integration duration** for which the statistic at the true event alignment exceeds the global threshold with probability at least `beta`. Because true-alignment threshold crossing is a subset of threshold crossing by the complete signal-present scan, this criterion guarantees total scan-detection probability at least `beta`, but it is not the exact signal-present scan-power criterion.

For the controlled time-scaled family, the guarantee time has the exact dimensionless form

```math
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
```

while the batch wall-clock decision time measured from the opening of the arrival window is

```math
T_{\rm wall}=L+T_G.
```

At fixed `L`, `T_wall` and `T_G` induce the same detector ordering. Shortening `tau` accelerates evidence accumulation but also increases the normalized timing-search interval `L/tau`. For the family constructed here, these competing effects imply at least one finite fast-to-slow **guarantee-time** crossover and a slow-only guarantee-feasibility region. The result is task- and protocol-specific. It does not prove a reversal of the exact full signal-present scan detection times, does not establish a general preference for slower photodetectors, and does not introduce a universal replacement for `D*`.

---

# I. Introduction

Specific detectivity, `D*`, is one of the most widely used figures of merit for photodetector comparison. Its conventional normalization includes detector area and noise-equivalent measurement bandwidth; that bandwidth normalization should not be confused with the detector's temporal response bandwidth or `-3 dB` speed. `D*` remains useful when the operating condition to which it refers is specified, but it is not a complete descriptor of arbitrary time-dependent detection. That limitation is longstanding rather than new. Jones treated energy detection from radiation pulses using frequency-dependent detectivity in 1960 [1], detector characterization has long treated temporal bandwidth as a separate performance dimension [2,3], and modern guidance emphasizes application- and protocol-dependent characterization [4].

The relevant signal-detection quantity also depends on the task. For a known deterministic waveform observed for sufficiently long time in stationary Gaussian noise, maximum matched-filter SNR is set by the spectral overlap of signal and noise. Unknown arrival time changes the problem because event time becomes a nuisance parameter. A fixed global false-alarm probability must then be imposed over a correlated timing scan, and the threshold depends on the correlation structure of that scan rather than on raw digital sample count alone [5–7]. Similar acquisition-time / range-window questions have long appeared in radar, sonar, synchronization, and optical ranging [8].

The present question is therefore deliberately narrower than whether `D*` “contains bandwidth.” Suppose two detector channels are normalized so that neither has an eventual matched-filter SNR advantage for one specified optical event. One channel responds faster than the other. If event time were known, the faster channel would accumulate any fixed fraction of its available evidence sooner. If event time is uncertain over one fixed physical interval, however, temporal compression also shortens the physical correlation length of the matched-filter timing statistic. The faster channel therefore spans a larger normalized search domain.

The two effects oppose one another:

```text
shorter detector time scale
    -> faster accumulation of signal evidence,

but also

shorter detector time scale
    -> shorter timing-scan correlation length
    -> larger normalized unknown-arrival search.
```

The issue is whether this competition can prevent a detector-only ordering by response time even after eventual matched-filter SNR has been equalized.

A critical distinction is made at the outset. The paper does **not** solve a sequential online stopping problem, and it does **not** derive the exact signal-present scan detection probability. Instead, it defines a batch acquisition protocol and a conservative sufficient criterion: the matched-filter statistic at the true arrival alignment must exceed a threshold calibrated against the maximum of the complete noise-only scan. Meeting that true-alignment criterion with probability `beta` guarantees that the complete signal-present scan declares a detection with probability at least `beta`.

Within this explicit protocol, detector time scale enters the guarantee problem twice. It sets the physical rate of evidence accumulation and rescales the nuisance-parameter domain through `L/tau`. The resulting post-window guarantee time is

```math
T_G
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
```

and the batch wall-clock time is `L+T_G`. At known arrival time the faster member reaches the guarantee criterion first. As timing uncertainty grows, the faster member reaches its search-limited guarantee-feasibility boundary at a smaller physical `L`. Under the finite-dimensional continuity condition stated below, these facts force at least one fast-to-slow guarantee-time crossover.

Section II defines a common optical event, a realizable time-scaled detector family, and its finite-time matched-filter statistics. Section III defines the batch acquisition protocol, global scan threshold, and guarantee-time surface. Section IV proves the feasibility partition and crossover. Section V states the physical interpretation and, equally importantly, the limits of what the theorem establishes.

---

# II. Controlled equal-eventual-SNR photodetector family

## A. Common optical event and causal detector realization

To keep the construction detector-facing, all channels receive the same incident optical event

```math
p(t)=e^{-bt}u(t),
\qquad b>0,
```

with Laplace transform

```math
P(s)=\frac{1}{s+b}.
```

For each detector time scale `tau>0`, define the causal stable proper transfer function

```math
\boxed{
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}.
}
```

The output signal is then

```math
G_\tau(s)P(s)
=\frac{A_\tau}{(s+1/\tau)^2},
```

so

```math
\boxed{
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
}
```

Thus the compared waveforms are not independently chosen templates: they arise from one fixed optical event passed through a realizable family of causal detector channels. The construction is intentionally idealized and is not asserted to represent a unique microscopic photodetector mechanism.

## B. Noise convention and equal eventual matched-filter SNR

Let the additive output noise be zero-mean white Gaussian noise with

```math
\boxed{
E[n(t)n(t')]=N\,\delta(t-t').
}
```

Under this convention, the matched-filter squared SNR for a deterministic signal segment is

```math
\rho^2=\frac{1}{N}\int s^2(t)\,dt.
```

For the full output waveform,

```math
\rho_{\tau,\infty}^2
=\frac{A_\tau^2}{N}
\int_0^\infty t^2e^{-2t/\tau}dt
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
\boxed{
\rho_{\tau,\infty}=\rho_0
}
```

for every `tau`.

This equality is **event-specific**: all channels have the same eventual matched-filter SNR for the specified optical input `p(t)`. It is deliberately stronger and more task-specific than equality of one scalar reference `D*`; it should not be read as equality of detector sensitivity for every possible waveform or wavelength.

Let

```math
x=\frac{t}{\tau}
```

be the available post-arrival signal duration in detector-time units. The accumulated fraction of total squared matched-filter SNR is

```math
\eta(x)
=\frac{\int_0^x v^2e^{-2v}\,dv}
{\int_0^\infty v^2e^{-2v}\,dv}
=1-e^{-2x}(1+2x+2x^2),
```

so

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
}
```

Since

```math
\eta'(x)=4x^2e^{-2x}>0
```

for `x>0`, every channel monotonically accumulates evidence, and at any fixed physical `t` the smaller-`tau` channel reaches a larger fraction of its eventual SNR.

## C. Finite-template timing covariance

At finite integration duration `t`, the normalized template in detector-time units is proportional to

```math
h_x(v)=v e^{-v}1_{[0,x]}(v).
```

Under noise alone, scanning this template across candidate arrival times produces a zero-mean unit-variance stationary Gaussian process. Its covariance depends only on dimensionless lag

```math
y=\frac{|\Delta|}{\tau}.
```

For `0\le y<x`,

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}\,dv
}{
\int_0^x v^2e^{-2v}\,dv},
}
```

and

```math
R_x(y)=0,\qquad y\ge x.
```

In physical time,

```math
\boxed{
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
}
```

For one fixed physical arrival-time uncertainty interval `L`, the normalized search length is therefore

```math
\boxed{
\ell=\frac{L}{\tau}.
}
```

Reducing `tau` simultaneously accelerates signal accumulation and enlarges this normalized timing-search interval.

---

# III. Batch acquisition and the guarantee-time surface

## A. Operational acquisition clock

Let the event arrival time `theta` be known a priori to lie in

```math
0\le\theta\le L.
```

For a candidate post-arrival integration duration `t`, every candidate arrival must be evaluated with the same finite template support `[0,t]`. The latest candidate arrival, `theta=L`, therefore requires data through physical time `L+t`. The protocol is consequently:

```text
1. open the allowed event-arrival window at time 0;
2. close the arrival window at time L;
3. acquire t additional seconds of data;
4. scan all candidate arrivals in [0,L] with the same duration-t matched filter;
5. compare the scan maximum with one global threshold.
```

The quantity optimized below is the required **post-window integration duration**. If that duration is `T_G`, then the wall-clock batch decision time measured from the opening of the arrival window is

```math
\boxed{
T_{\rm wall}=L+T_G.
}
```

This is a batch protocol, not a sequential stopping rule. Because `L` is common to both detectors in a comparison,

```math
T_{{\rm wall},f}-T_{{\rm wall},s}
=T_{G,f}-T_{G,s},
```

so detector ordering is identical whether it is expressed in `T_G` or `T_wall`.

## B. Global false-alarm threshold

Let `Z_x(q)` denote the normalized noise-only matched-filter scan at dimensionless candidate arrival time `q`. For `x=t/tau`,

```math
\operatorname{Cov}[Z_x(q),Z_x(q')]
=R_x(|q-q'|).
```

For fixed `(x,ell,alpha)`, define the generalized global threshold `Gamma(x,ell,alpha)` by

```math
\boxed{
\Pr\!\left[
\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)
\right]\le\alpha,
}
```

with `Gamma` taken as the smallest threshold satisfying this inequality. This retains the correlated timing scan and makes no independent-trials approximation.

## C. True-alignment guarantee criterion

Let `q_0` denote the true dimensionless event alignment under the signal-present hypothesis. **The receiver is not given `q_0`; it still scans the entire interval.** The symbol `q_0` is used only to evaluate performance at the generative true alignment.

Under signal plus noise, the normalized matched-filter statistic at `q_0` has unit variance and mean

```math
\rho_0\sqrt{\eta(x)}.
```

Let `Y_x(q)` denote the complete normalized signal-present timing scan. Define

```math
P_{D,\mathrm{true}}(x)
=\Pr\left[Y_x(q_0)>\Gamma(x,\ell,\alpha)\right].
```

Then

```math
\boxed{
P_{D,\mathrm{true}}(x)
=\Phi\!\left[
\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\right],
}
```

where `Phi` is the standard-normal cumulative distribution function.

The complete scan detection probability is

```math
P_D^{\mathrm{scan}}(x)
=\Pr\left[
\sup_{0\le q\le\ell}Y_x(q)>\Gamma(x,\ell,\alpha)
\right].
```

Pathwise,

```math
\{Y_x(q_0)>\Gamma\}
\subseteq
\{\sup_qY_x(q)>\Gamma\},
```

therefore

```math
\boxed{
P_D^{\mathrm{scan}}(x)
\ge P_{D,\mathrm{true}}(x).
}
```

Accordingly, the condition

```math
P_{D,\mathrm{true}}(x)\ge\beta
```

is a conservative sufficient condition guaranteeing

```math
P_D^{\mathrm{scan}}(x)\ge\beta.
```

This one-sided implication is central to the scope of the paper. The theorem below orders the time required to satisfy this **guarantee criterion**. It does not order the exact first integration durations obtained by solving `P_D^{scan}=beta` directly.

Define the guarantee margin

```math
\boxed{
M_G(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
}
```

Let

```math
z_\beta=\Phi^{-1}(\beta).
```

The guarantee criterion is

```math
M_G(x;\ell,\rho_0,\alpha)\ge z_\beta.
```

## D. Monotonicity with integration duration

For fixed dimensionless lag `y`, write

```math
R_x(y)
=\frac{\int_0^x w(v)H_y(v)\,dv}
{\int_0^x w(v)\,dv},
\qquad
w(v)=v^2e^{-2v}>0,
```

where

```math
H_y(v)=
\begin{cases}
0, & 0\le v<y,\\
e^y\!\left(1-\dfrac{y}{v}\right), & v\ge y.
\end{cases}
```

Because `H_y(v)` is nondecreasing in `v`,

```math
x_2>x_1
\quad\Longrightarrow\quad
R_{x_2}(y)\ge R_{x_1}(y)
\quad\text{for all }y.
```

Slepian's Gaussian comparison inequality [9] then gives

```math
\boxed{
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
}
```

The signal term increases strictly while the threshold does not increase, so `M_G` is strictly increasing in `x`. Every channel benefits from additional integration time; the cross-channel reversal is not produced by assigning one channel a self-suboptimal duration.

Define the dimensionless guarantee time

```math
\boxed{
X_G(\rho_0,\alpha,\beta,\ell)
=\inf\left\{
x>0:
M_G(x;\ell,\rho_0,\alpha)\ge z_\beta
\right\}.
}
```

Whenever the guarantee criterion is feasible,

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

This is the central scaling relation of the paper.

## E. Full-template limit and guarantee feasibility

As `x\to\infty`,

```math
\eta(x)\to1,
\qquad
R_x(y)\to R_\infty(y)=(1+y)e^{-y}.
```

Let `Z_\infty(q)` denote the stationary unit-variance Gaussian timing process with covariance

```math
\operatorname{Cov}[Z_\infty(q),Z_\infty(q')]
=R_\infty(|q-q'|).
```

Define its global threshold directly by

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
=\inf\left\{u:
\Pr\!\left[
\sup_{0\le q\le\ell}Z_\infty(q)>u
\right]\le\alpha
\right\}.
}
```

This full-template threshold is also the limit of the finite-template thresholds under the same ordinary supremum-quantile continuity regularity used below. To see the process convergence, normalize

```math
\hat h_x(v)
=\frac{v e^{-v}1_{[0,x]}(v)}
{\|v e^{-v}1_{[0,x]}\|_2},
\qquad
\hat h_\infty(v)
=\frac{v e^{-v}1_{[0,\infty)}(v)}
{\|v e^{-v}1_{[0,\infty)}\|_2}.
```

Then

```math
\|\hat h_x-\hat h_\infty\|_2\to0,
```

and the autocorrelation identity plus Cauchy-Schwarz gives the uniform covariance bound

```math
\boxed{
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
}
```

Thus the finite-template Gaussian scans converge to the full-template scan on every fixed compact search interval at the covariance level, and `Gamma(x,ell,alpha)->Gamma_infty(ell,alpha)` under the stated threshold-continuity regularity.

Define

```math
\boxed{
M_{G,\infty}(\ell)
=\rho_0-\Gamma_\infty(\ell,\alpha).
}
```

Finite guarantee time exists when

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
<\rho_0-z_\beta.
}
```

If the reverse strict inequality holds, the limiting full-template margin itself is below the requested guarantee level, so no finite post-window integration duration can satisfy the true-alignment guarantee criterion. Equality is the asymptotic boundary treated below.

The threshold is nondecreasing in `ell` because increasing the search interval enlarges the supremum domain. In addition, for the present full-template covariance the threshold is unbounded as `ell\to\infty`. A short proof avoids placing this fact among the theorem assumptions.

Choose any `0<epsilon<1`. Since

```math
R_\infty(y)=(1+y)e^{-y}\to0,
```

there exists a spacing `d_epsilon` such that

```math
R_\infty(d_\epsilon)\le\epsilon.
```

Sample the process at `n` points separated by `d_epsilon`. Their off-diagonal covariances satisfy

```math
R_\infty(kd_\epsilon)\le\epsilon,
\qquad k\ge1.
```

Compare this vector with an equicorrelated Gaussian vector

```math
Y_i=\sqrt\epsilon\,V
+\sqrt{1-\epsilon}\,E_i,
```

where `V,E_1,...,E_n` are independent standard normals. The comparison vector has larger off-diagonal covariance, so Slepian gives

```math
\Pr\left[\max_i Z_i\le u\right]
\le
\Pr\left[\max_iY_i\le u\right].
```

But

```math
\max_iY_i
=\sqrt\epsilon\,V
+\sqrt{1-\epsilon}\max_iE_i
\to\infty
```

in probability as `n\to\infty`. Hence the sampled maximum, and therefore the continuous supremum, exceeds every fixed level with probability tending to one over sufficiently long intervals. Thus

```math
\boxed{
\Gamma_\infty(\ell,\alpha)\to\infty
\qquad(\ell\to\infty).
}
```

The guarantee-feasibility boundary is therefore finite whenever known-time operation is feasible.

---

# IV. Task-dependent fast/slow guarantee ordering

## A. Exact guarantee-time boundary

Consider two channels with

```math
\tau_f<\tau_s,
\qquad
r=\frac{\tau_s}{\tau_f}>1,
```

and define timing uncertainty in slow-channel units,

```math
\ell=\frac{L}{\tau_s}.
```

The fast channel searches `r ell`, while the slow channel searches `ell`. Therefore

```math
\boxed{
T_{G,f}
=\tau_fX_G(\rho_0,\alpha,\beta,r\ell),
}
```

and

```math
\boxed{
T_{G,s}
=r\tau_fX_G(\rho_0,\alpha,\beta,\ell).
}
```

The exact guarantee-time preference boundary is

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
}
```

Because `T_wall=L+T_G`, this is also the batch wall-clock ordering boundary at fixed `L`.

## B. Guarantee-feasibility partition

Let

```math
\boxed{
c=\rho_0-z_\beta.
}
```

The slow channel has finite guarantee time when

```math
\Gamma_\infty(\ell,\alpha)<c,
```

whereas the fast channel requires

```math
\Gamma_\infty(r\ell,\alpha)<c.
```

Since `Gamma_infty` is nondecreasing,

```math
\Gamma_\infty(r\ell,\alpha)
\ge\Gamma_\infty(\ell,\alpha).
```

Thus only three guarantee-feasibility regimes are possible:

```math
\boxed{
\begin{array}{ll}
\text{both guarantee-feasible:}
& c>\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{slow guarantee-feasible only:}
& \Gamma_\infty(\ell,\alpha)<c
\le\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{neither guarantee-feasible:}
& c\le\Gamma_\infty(\ell,\alpha).
\end{array}
}
```

A fast-only guarantee-feasibility region is impossible in this equal-eventual-SNR scaled family.

Define

```math
\boxed{
\ell_{\rm crit}
=\sup\left\{\ell\ge0:
\Gamma_\infty(\ell,\alpha)<\rho_0-z_\beta
\right\}.
}
```

Then

```math
\boxed{
L_{\rm crit}(\tau)=\tau\ell_{\rm crit},
}
```

so

```math
\boxed{
\frac{L_{{\rm crit},s}}{L_{{\rm crit},f}}
=\frac{\tau_s}{\tau_f}=r.
}
```

## C. Boundary divergence is a consequence, not an assumption

Assume the ordinary finite-dimensional regularity needed for the threshold to vary continuously with `(x,ell)` and for `Gamma_infty(ell,alpha)` to be continuous at `ell_crit`. Then

```math
\Gamma_\infty(\ell_{\rm crit},\alpha)=c.
```

For every finite `x`,

```math
\eta(x)<1.
```

Also, since `R_x(y)\le R_\infty(y)` pointwise, Slepian gives

```math
\Gamma(x,\ell,\alpha)
\ge\Gamma_\infty(\ell,\alpha).
```

Therefore at `ell=ell_crit`, for every finite `x`,

```math
\begin{aligned}
M_G(x;\ell_{\rm crit})
&=\rho_0\sqrt{\eta(x)}
-\Gamma(x,\ell_{\rm crit},\alpha)\\
&<\rho_0-\Gamma_\infty(\ell_{\rm crit},\alpha)\\
&=z_\beta.
\end{aligned}
```

No finite `x` reaches the guarantee boundary itself. If `X_G(ell)` remained bounded along a sequence `ell\uparrow ell_crit`, continuity would produce a finite limiting `x` satisfying the criterion at `ell_crit`, contradicting the strict inequality above. Hence

```math
\boxed{
X_G(\ell)\to\infty
\qquad
(\ell\uparrow\ell_{\rm crit}).
}
```

The divergence previously carried as a separate assumption is therefore a consequence of the specific family plus the stated continuity regularity.

## D. Proposition 1: existence of a fast-to-slow guarantee-time crossover

**Proposition 1 (task-dependent guarantee-time ordering).** Consider the equal-eventual-SNR family above with `tau_f<tau_s`. Suppose:

1. the requested `(alpha,beta)` criterion is guarantee-feasible for known arrival time;
2. the finite-dimensional threshold / first-crossing surface is continuous in the interior of its guarantee-feasible domain, and `Gamma_infty(ell,alpha)` is continuous at the critical boundary.

Then at least one finite physical arrival-time uncertainty

```math
L_\times\in(0,L_{{\rm crit},f})
```

exists at which the two channels have equal guarantee time. The fast channel has smaller guarantee time for sufficiently small `L`; the slow channel has smaller guarantee time sufficiently near the fast channel's guarantee-feasibility boundary.

**Proof.** At `L=0`, both channels solve the same dimensionless known-time problem. Let

```math
x_0=X_G(\rho_0,\alpha,\beta,0).
```

Known-time guarantee feasibility gives finite `x_0`, so

```math
T_{G,f}(0)=\tau_fx_0,
\qquad
T_{G,s}(0)=\tau_sx_0,
```

and therefore

```math
\boxed{
T_{G,f}(0)<T_{G,s}(0).
}
```

By continuity, fast preference persists over a nonzero neighborhood of `L=0`.

The critical physical uncertainties are

```math
L_{{\rm crit},f}=\tau_f\ell_{\rm crit},
\qquad
L_{{\rm crit},s}=\tau_s\ell_{\rm crit}
=rL_{{\rm crit},f}.
```

Thus the fast channel reaches its guarantee-feasibility boundary first. As

```math
L\uparrow L_{{\rm crit},f},
```

its normalized search length approaches `ell_crit`, and Section IV.C gives

```math
T_{G,f}(L)\to\infty.
```

At the same physical `L`, the slow channel's normalized search length approaches

```math
\frac{L_{{\rm crit},f}}{\tau_s}
=\frac{\ell_{\rm crit}}{r}
<\ell_{\rm crit},
```

so the slow channel remains strictly inside its guarantee-feasible domain and has finite `T_G`. Therefore

```math
D_G(L)=T_{G,f}(L)-T_{G,s}(L)
```

is negative at `L=0` and positive sufficiently near `L_{{\rm crit},f}`. Continuity implies at least one

```math
\boxed{
L_\times\in(0,L_{{\rm crit},f})
}
```

for which

```math
\boxed{
T_{G,f}(L_\times)=T_{G,s}(L_\times).
}
```

Because adding the common `L` leaves differences unchanged,

```math
T_{{\rm wall},f}(L_\times)
=T_{{\rm wall},s}(L_\times)
```

at the same crossover. `\square`

The proposition establishes existence, not uniqueness. More importantly, it establishes a crossover in the **sufficient guarantee times**. It does not imply that the exact solutions of

```math
P_D^{\rm scan}(t)=\beta
```

must cross at the same `L`, or cross at all.

---

# V. Interpretation, limitations, and implications

## A. What is ordered

The ordered object is not an intrinsic detector latency. It is the post-window integration duration required by one explicit batch protocol to guarantee a global-scan detection probability through a true-alignment sufficient condition:

```math
\boxed{
T_G
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
}
```

The corresponding wall-clock batch time is `L+T_G`. At fixed `L`, these two clocks induce identical channel rankings.

This distinction matters because an online receiver can use partial information before the arrival window closes, and a full signal-present scan can cross threshold because of off-alignment signal contributions even when the true-alignment statistic has not yet crossed. Neither effect is modeled as an exact stopping-time theorem here.

## B. Detector characterization versus task qualification

A detector specification such as `D*`, responsivity, noise, response time, or bandwidth describes a device under stated measurement conditions. `T_G` belongs to a detector **and** a task. The same pair of detector channels can therefore occupy different preference regimes as `L`, `alpha`, or `beta` changes.

The result does not make conventional detector figures of merit incorrect. It identifies a level at which detector-only scalars no longer determine ordering. Device characterization reports physical response and noise properties; task qualification asks what those properties imply under a specified acquisition and decision protocol.

## C. Why the conclusion is not another sensitivity-speed product

Sensitivity-speed products are already established in detector literature [2,3], and the present result does not propose a new universal scalar. The relevant search variable is

```math
\frac{L}{\tau},
```

while the guarantee surface also depends on

```math
\rho_0,\qquad\alpha,\qquad\beta,
```

and on the decision rule. A scalar formed only from detector properties would remove precisely the task dependence that produces the crossover.

## D. Physical origin of the guarantee-time reversal

Every member is normalized to the same eventual matched-filter SNR for the specified event, and every member benefits monotonically from longer integration. The reversal is therefore not created by assigning the slower channel more eventual signal evidence or by stopping the faster channel prematurely.

It arises from the geometry of the unknown-arrival search. Compressing the detector response in physical time compresses the timing-scan correlation length. For fixed physical `L`, the faster channel spans a larger normalized search domain and consequently pays a larger global false-alarm threshold. At small `L`, the physical time-scale advantage dominates. Near the fast channel's guarantee-feasibility boundary, the search penalty dominates strongly enough that the slow channel still satisfies the guarantee while the fast channel does not.

## E. Scope limitations

The construction is intentionally narrow.

First, the channels are linear and time-scaled, and the output noise is additive, stationary, white, and Gaussian. Real detectors may exhibit colored or signal-dependent noise, nonlinear response, saturation, drift, dead time, temperature dependence, and other effects.

Second, equal eventual matched-filter SNR is event-specific. Unequal eventual sensitivity would introduce another task axis and could reinforce or oppose the search effect.

Third, arrival time is the only nuisance parameter. Unknown amplitude, phase, spectrum, background, or multiple events enlarge the composite-hypothesis space.

Fourth, the global threshold is calibrated from the noise-only scan, but power is guaranteed using the true-alignment statistic. The exact signal-present scan probability satisfies

```math
P_D^{\rm scan}\ge P_{D,\mathrm{true}},
```

so the criterion is conservative. The theorem does **not** prove ordering of exact scan-power times.

Fifth, the protocol is batch. It does not claim optimal online latency, Bayesian optimality, minimax optimality, localization accuracy, or sequential optimality.

Finally, Proposition 1 proves at least one crossover but not uniqueness. The purpose is to construct a clean failure of detector-only guarantee-time ordering, not a complete theory of transient photodetection.

## F. Numerical status

The analytical existence result does not by itself establish that a crossover occurs far from the fast guarantee-feasibility singularity for a practically representative parameter set. The repository's later numerical stress-test branch deliberately explored this issue and also documented several invalidated shortcuts. In particular, the original hard-window Step-13 grid crossover was rejected because the finite template produces a locally rough timing process, and the later Step-44 result was certified only on a finite grid and was too close to the continuum discretization correction to use as a publication-grade example.

A smooth finite-information surrogate was independently validated against correlated-process Monte Carlo and continuous Rice theory, showing that the search mechanism survives regularization, but that surrogate is not substituted here for the exact hard-window theorem. A robust continuum-validated quantitative example for the exact Paper A model therefore remains a **separate open presentation task**, not something inferred from the invalidated or knife-edge calculations.

## G. Implications for detector specification and experiment design

A task-oriented comparison should report enough information to reconstruct the decision problem rather than only a detector scalar. In the present setting, the essential quantities are the event-specific eventual matched-filter SNR or its ingredients, the detector temporal response, the physical arrival-time uncertainty interval, and the global false-alarm / guaranteed-detection criteria.

This is especially relevant when detectors with substantially different response times are compared for transient measurements. A response-time advantage does not automatically imply a shorter guarantee time once the detector is embedded in an unknown-arrival global-threshold search. Conversely, the theorem does not license choosing a slower detector merely to reduce search complexity. The operating task determines the ordering.

The central practical statement is therefore:

> **For an unknown-arrival batch detection task, detector response time affects both evidence accumulation and the statistical size of the timing search. Equal eventual matched-filter SNR therefore need not imply a detector-only ordering of the integration time required to guarantee a specified global-scan operating point.**

## H. Conclusion

We considered causal time-scaled photodetector channels driven by the same optical event and normalized to equal eventual matched-filter SNR. Event arrival is unknown over a fixed window `L`, and a batch global-threshold matched-filter scan is performed after acquiring `t` additional seconds beyond the end of that window.

The minimum post-window integration duration that guarantees the requested scan-detection probability through the true-alignment sufficient condition is

```math
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

The faster channel benefits from a smaller physical time scale but pays a larger normalized timing-search burden. For the constructed equal-eventual-SNR family, the full-template threshold grows without bound with search length, the guarantee time diverges at a finite search-feasibility boundary, and at least one fast-to-slow guarantee-time crossover follows under ordinary threshold-continuity regularity.

The result is intentionally narrower than an exact unknown-arrival scan-power theorem. It establishes task-dependent ordering of a conservative, operationally defined guarantee time. Whether the exact signal-present scan detection times exhibit the same reversal is a distinct problem and is not claimed here.

---

## References

[1] R. Clark Jones, “Energy Detectable by Radiation Detectors,” *Journal of the Optical Society of America* **50**, 883–886 (1960). DOI: 10.1364/JOSA.50.000883.

[2] J. P. Garcia and E. L. Dereniak, “Extrinsic silicon photodetector characterization,” *Applied Optics* **29**, 559–569 (1990). DOI: 10.1364/AO.29.000559.

[3] Y. Yang *et al.*, “Overcoming the sensitivity–speed trade-off in two-dimensional photodetectors via a functional oxide interlayer,” *Nature Communications* **17**, 6077 (2026). DOI: 10.1038/s41467-026-72259-1.

[4] V. Pecunia *et al.*, “Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies,” *Nature Photonics* **19**, 1178–1188 (2025). DOI: 10.1038/s41566-025-01759-1.

[5] R. Vio and P. Andreani, “On the Correct Estimate of the Probability of False Detection of the Matched Filter in Weak-Signal Detection Problems,” arXiv:1602.02392 (2016).

[6] G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, and E. Ruiz Morales, “The False Alarms induced by Gaussian Noise in Gravitational Wave Detectors,” *Physical Review D* **107**, 023027 (2023). DOI: 10.1103/PhysRevD.107.023027.

[7] R. P. Croce *et al.*, “Correlator Bank Detection of GW chirps. False-Alarm Probability, Template Density and Thresholds: Behind and Beyond the Minimal-Match Issue,” *Physical Review D* **70**, 122001 (2004). DOI: 10.1103/PhysRevD.70.122001.

[8] A. B. Milstein *et al.*, “Acquisition algorithm for direct-detection ladars with Geiger-mode avalanche photodiodes,” *Applied Optics* **47**, 296–311 (2008). DOI: 10.1364/AO.47.000296.

[9] D. Slepian, “The One-Sided Barrier Problem for Gaussian Noise,” *Bell System Technical Journal* **41**, 463–501 (1962). DOI: 10.1002/j.1538-7305.1962.tb02419.x.
