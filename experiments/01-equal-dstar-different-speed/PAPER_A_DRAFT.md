# Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity

**Draft status:** Paper A through Section IV / detector-facing main narrative / novelty not established  
**Date:** 2026-08-12

## Abstract

Specific detectivity is a useful measure of detector sensitivity under a stated operating condition, but pulse detection and sensitivity–bandwidth tradeoffs are already known to require temporal or spectral information beyond a single scalar figure of merit. Here we ask a different question: if two detector channels are deliberately normalized to have the same eventual matched-filter signal-to-noise ratio, does the faster detector necessarily reach a prescribed detection decision first when the event arrival time is unknown? For a controlled time-scaled Gaussian detector family under a specified global-false-alarm matched-filter scanning protocol, the detection time takes the dimensionless form

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
```

where `tau` is the detector time scale, `L` is the physical arrival-time uncertainty interval, `alpha` is the allowed global false-alarm probability, `beta` is the required true-alignment detection probability, and `rho_0` is the common eventual matched-filter SNR. Shortening `tau` accelerates finite-time evidence accumulation but simultaneously increases the normalized search interval `L/tau` and shortens the correlation length of the timing scan. Under stated continuity and large-search assumptions, these competing effects imply at least one finite fast-to-slow detection-time crossover in the constructed equal-eventual-SNR family, together with a slow-only feasibility regime near the faster detector's search-limited boundary. The result is task- and protocol-specific: it does not imply that slower photodetectors are generally superior, does not assert universal optimality of the chosen search rule, and does not introduce a universal replacement for `D*`.

---

# I. Introduction

Specific detectivity, `D*`, is one of the most widely used figures of merit for comparing photodetectors. It combines responsivity, noise, active area, and measurement bandwidth into a normalized sensitivity measure and is useful when the operating condition to which it refers is specified. It is not, however, a complete descriptor of arbitrary time-dependent detection. That limitation is longstanding rather than new. Jones treated the energy detectable from radiation pulses using frequency-dependent detectivity in 1960 [1], and detector characterization has long treated temporal bandwidth as a separate performance dimension [2,3]. Modern guidance likewise emphasizes that detector figures of merit are meaningful only together with their measurement conditions [4].

The appropriate signal-detection quantity also depends on the task. For a known deterministic waveform observed for sufficiently long time in stationary Gaussian noise, the maximum matched-filter SNR is determined by the spectral overlap of the signal with the detector/noise transfer function. In that restricted problem, a complete frequency-dependent sensitivity description can be sufficient. Unknown arrival time changes the problem. The receiver must then search over a nuisance parameter—the event time—and a fixed global false-alarm probability must be distributed over the resulting correlated timing scan. This search penalty is established in matched-filter detection theory: false-alarm behavior depends on the correlation structure of the filtered process and cannot generally be identified with the raw digital sample count [5–7].

These observations motivate a narrower question than whether `D*` “contains bandwidth.” Suppose two detector channels are deliberately normalized so that neither has an eventual matched-filter sensitivity advantage. They produce the same asymptotic matched-filter SNR for the event of interest, but one responds on a shorter time scale than the other. If the event time were known, the faster detector would naturally accumulate a given fraction of its available evidence sooner. If event time is unknown, however, temporal compression also makes the matched-filter output decorrelate over a shorter physical lag. Over one fixed physical arrival-time interval, the faster detector therefore presents a larger normalized timing-search domain.

The two effects act in opposite directions:

```text
shorter detector time scale
    -> faster accumulation of signal evidence,

but also

shorter detector time scale
    -> shorter timing-scan correlation length
    -> larger normalized unknown-arrival search.
```

The central issue of this paper is whether that competition can destroy any detector-only ordering by response time, even after eventual matched-filter sensitivity has been equalized.

We study this question in a deliberately controlled family rather than attempt to model every physical detector mechanism. The family is time-scaled, linear, and observed in additive white Gaussian output noise. Its members are normalized to the same eventual matched-filter SNR `rho_0`. The unknown event arrival is searched over a physical interval `L`; a single threshold is chosen to satisfy a global false-alarm probability `alpha`; and detection time is defined by reaching a specified true-alignment detection probability `beta`. The decision rule is therefore explicit. It is not asserted to be Bayes-optimal, minimax-optimal, or sequentially optimal for the general unknown-arrival problem.

Within this construction, the detector time scale enters the decision problem in two distinct ways. First, it scales the physical rate of evidence accumulation. Second, it rescales the nuisance-parameter domain through `L/tau`. The resulting detection time is not a function of detector properties alone but a task surface,

```math
T_D
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

This structure is sufficient to obtain a qualitative fast/slow regime theorem. When `L=0`, the two members face the same dimensionless decision problem, so the faster member reaches the required decision first. As `L` grows, the faster member searches the larger dimensionless interval. For the equal-eventual-SNR scaled family considered here, its asymptotic feasibility boundary is therefore reached at a proportionally smaller physical `L`. Under standard continuity and large-search conditions, the fast detection time must cross the slow detection time at least once before that boundary. Beyond it, a region can exist in which the slow detector remains feasible while the fast detector cannot satisfy the requested global-false-alarm/detection operating point at any integration duration.

The conclusion is intentionally limited. We do not claim that slower detectors are generally better, that speed intrinsically carries a sensitivity penalty, or that the present scanning protocol is the unique way to handle unknown arrival time. The result is instead a counterexample to a detector-only ordering: even with equal eventual matched-filter sensitivity, finite-time ranking can depend on the arrival-time uncertainty and global decision criterion. The relevant comparison is therefore between detector–task pairs, not detector time constants in isolation.

The remainder of the paper is organized as follows. Section II defines the equal-eventual-SNR family and derives the finite-time SNR and timing-scan covariance. Section III introduces the dimensionless detection-time surface. Section IV derives the fast/slow task boundary and feasibility partition. Section V will discuss the interpretation, limitations, and implications for detector specification and comparison.

---

# II. Controlled equal-eventual-SNR detector family

## A. Time-scaled matched-filter template

We choose a family whose output signal for the event of interest can be written

```math
s_\tau(t)=A_\tau\,t e^{-t/\tau}u(t),
```

where `u(t)` is the unit step and `tau` sets the detector time scale. This waveform can be generated by a stable causal linear response, but here it is used primarily because temporal scaling is explicit and all members can be normalized to identical eventual matched-filter SNR.

Assume additive white Gaussian output noise with two-sided spectral density `N` under a consistent normalization. Choosing

```math
A_\tau=\frac{2\rho_0\sqrt{N}}{\tau^{3/2}}
```

gives

```math
\boxed{\rho_{\tau,\infty}=\rho_0}
```

for every `tau`. The comparison therefore removes asymptotic matched-filter sensitivity as an explanatory variable: any difference in finite-task performance comes from temporal scaling and the way that scaling interacts with the decision protocol.

Let

```math
x=\frac{t}{\tau}
```

be the observation duration in detector-time units. The fraction of the total squared matched-filter SNR accumulated by time `t` is

```math
\eta(x)
=\frac{\int_0^x v^2 e^{-2v}\,dv}
{\int_0^\infty v^2 e^{-2v}\,dv}
=1-e^{-2x}(1+2x+2x^2),
```

so

```math
\boxed{
\rho_{\tau,t}=\rho_0\sqrt{\eta(x)}.
}
```

Because

```math
\eta'(x)=4x^2e^{-2x}>0
```

for `x>0`, each detector monotonically accumulates available evidence as observation time increases. At fixed physical time, the smaller-`tau` member has the larger `x` and therefore reaches any fixed fraction of its eventual SNR earlier. This is the familiar advantage of a faster response.

## B. Unknown arrival time changes the same temporal scaling into a search scale

Now let the event arrival time be unknown within a physical interval of length `L`. At observation duration `t`, the normalized finite-record matched-filter template is proportional to

```math
h_x(v)=v e^{-v}\,1_{[0,x]}(v)
```

in detector-time units. Under noise alone, scanning this template across candidate arrival times produces a stationary Gaussian process whose normalized covariance depends only on the dimensionless lag

```math
y=\frac{|\Delta|}{\tau}.
```

For `0\le y<x`, the covariance is

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}\,dv
}{
\int_0^x v^2e^{-2v}\,dv},
}
```

with

```math
R_x(y)=0,\qquad y\ge x.
```

Thus, in physical time,

```math
\boxed{
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).}
```

The same reduction in `tau` that accelerates signal accumulation therefore compresses the timing-scan covariance in physical lag. For one fixed physical uncertainty interval `L`, the faster detector searches a dimensionless interval

```math
\ell=\frac{L}{\tau}
```

that is larger in inverse proportion to its response time.

This is the central competition. Detector speed does not merely change when signal evidence becomes available; under an unknown-arrival global-false-alarm task it also changes the statistical size of the timing search.

---

# III. Detection time as a dimensionless task surface

## A. Global threshold for the correlated timing scan

Let `Z_x(q)` denote the normalized noise-only matched-filter scan at dimensionless trial arrival time `q`. For an observation duration `x=t/tau`, `Z_x` is a zero-mean, unit-variance stationary Gaussian process with covariance

```math
\operatorname{Cov}[Z_x(q),Z_x(q')]
=R_x(|q-q'|).
```

The physical arrival-time interval `L` becomes the dimensionless search interval

```math
\boxed{\ell=\frac{L}{\tau}.}
```

For fixed `(x,ell,alpha)`, define the global threshold `Gamma(x,ell,alpha)` by

```math
\boxed{
\Pr\!\left[
\sup_{0\le q\le\ell} Z_x(q)>\Gamma(x,\ell,\alpha)
\right]=\alpha,
}
```

with the usual generalized-quantile interpretation if the equality is not attained exactly. This definition contains the timing-search penalty without replacing the correlated scan by an independent-trials approximation. In physical units the threshold therefore satisfies

```math
\gamma_{\tau,t}(L,\alpha)
=\Gamma\!\left(\frac{t}{\tau},\frac{L}{\tau},\alpha\right).
```

At the true event alignment, the normalized matched-filter output under signal plus noise is Gaussian with unit variance and mean `rho_0 sqrt(eta(x))`. Under the true-alignment criterion used throughout this paper, the probability that the true-alignment output exceeds the global threshold is therefore

```math
\boxed{
P_{D,\mathrm{true}}(x)
=\Phi\!\left[
\rho_0\sqrt{\eta(x)}
-\Gamma(x,\ell,\alpha)
\right].
}
```

It is useful to define the dimensionless decision margin

```math
\boxed{
M(x;\ell,\rho_0,\alpha)
=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha).
}
```

The required detection probability `beta` is reached when

```math
M(x;\ell,\rho_0,\alpha)
\ge z_\beta,
\qquad
z_\beta\equiv\Phi^{-1}(\beta).
```

The criterion is deliberately narrower than the total probability that the maximum of the entire signal-present scan crosses threshold; it asks when the matched filter at the true alignment reaches the specified operating point while the threshold is still set by the global noise-only search.

## B. The first-crossing time is well defined for this family

For the controlled family, increasing the observation duration improves both terms that enter the decision margin. The signal term increases strictly because `eta'(x)>0`. The threshold term does not increase.

To see the latter, for fixed dimensionless lag `y` the covariance can be written as a positive-weight average

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

For fixed `y`, `H_y(v)` is nondecreasing in `v`. Consequently,

```math
x_2>x_1
\quad\Longrightarrow\quad
R_{x_2}(y)\ge R_{x_1}(y)
\quad\text{for all }y.
```

Standard Gaussian comparison then orders the corresponding suprema on the same interval `[0,ell]`:

```math
\boxed{
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
}
```

Thus `M(x;ell,rho_0,alpha)` is strictly increasing with `x`. Each detector therefore benefits monotonically from additional observation time; the cross-detector reversal derived below is not produced by assigning one detector a self-suboptimal integration duration.

Define the dimensionless detection time

```math
\boxed{
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\left\{
x>0:
M(x;\ell,\rho_0,\alpha)\ge z_\beta
\right\}.
}
```

Whenever the requested operating point is feasible, the monotonicity above makes this first crossing unambiguous.

Returning to physical time with `t=tau x` gives the central scaling relation

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

This collapse is exact for the controlled family. It makes clear why response time alone cannot order the task. A smaller `tau` multiplies the dimensionless detection time by a smaller physical time unit, but it simultaneously evaluates the same task surface at the larger normalized search length `L/tau`.

## C. Full-template limit and task feasibility

As `x` tends to infinity,

```math
\eta(x)\to1,
\qquad
R_x(y)\to R_\infty(y)=(1+y)e^{-y}.
```

Let

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
=\lim_{x\to\infty}\Gamma(x,\ell,\alpha)
}
```

and define the limiting margin

```math
\boxed{
M_\infty(\ell;\rho_0,\alpha)
=\rho_0-\Gamma_\infty(\ell,\alpha).
}
```

Because the finite-time margin increases toward this limit, a finite detection time exists when

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
<\rho_0-z_\beta.
}
```

If the reverse strict inequality holds, the requested operating point cannot be reached at any observation duration under the stated criterion. Equality defines the asymptotic feasibility boundary; under the ordinary strict-convergence assumption used below, it is approached only as `T_D` tends to infinity.

The quantity `Gamma_infty` is nondecreasing in `ell` simply because enlarging the search interval enlarges the set over which the supremum is taken. This monotonicity will determine the fast/slow feasibility structure independently of any closed-form expression for the correlated-scan quantile.

---

# IV. Task-dependent fast/slow ordering

## A. Exact task boundary

Consider two members of the family with equal eventual matched-filter SNR `rho_0` and time constants

```math
\tau_f<\tau_s.
```

Define

```math
\boxed{
r=\frac{\tau_s}{\tau_f}>1}
```

and measure the physical arrival-time uncertainty in units of the slower detector,

```math
\boxed{
\ell=\frac{L}{\tau_s}.
}
```

The faster detector then searches the normalized interval `r ell`, while the slower detector searches `ell`. Section III gives

```math
\boxed{
T_{D,f}
=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
}
```

and

```math
\boxed{
T_{D,s}
=r\tau_f X_D(\rho_0,\alpha,\beta,\ell).
}
```

The exact preference boundary is therefore implicit in the zero set

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
\equiv
X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)
=0.
}
```

This boundary compares the complete finite-time task surfaces. Comparing only the asymptotic margins would be insufficient: the slower member has the smaller normalized search burden for every `L>0`, yet at known arrival time the faster member reaches the same dimensionless decision point in a shorter physical time.

## B. Feasibility partition

Let

```math
\boxed{
c=\rho_0-z_\beta.}
```

For the slower detector, finite detection time requires

```math
\Gamma_\infty(\ell,\alpha)<c,
```

whereas the faster detector requires

```math
\Gamma_\infty(r\ell,\alpha)<c.
```

Since `Gamma_infty` is nondecreasing in search length,

```math
\Gamma_\infty(r\ell,\alpha)
\ge\Gamma_\infty(\ell,\alpha).
```

The task therefore has only three feasibility regimes:

```math
\boxed{
\begin{array}{ll}
\text{both feasible:}
& c>\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{slow only:}
& \Gamma_\infty(\ell,\alpha)<c
\le\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{neither feasible:}
& c\le\Gamma_\infty(\ell,\alpha).
\end{array}
}
```

A fast-only feasibility region is impossible within this equal-eventual-SNR scaled family. This statement is not a general preference for slow detectors; it follows from the deliberately equalized eventual SNR together with the fact that the faster member must search the larger dimensionless interval.

Define the critical normalized uncertainty

```math
\boxed{
\ell_{\mathrm{crit}}
=\sup\left\{\ell\ge0:
\Gamma_\infty(\ell,\alpha)
<\rho_0-z_\beta
\right\}.
}
```

The corresponding physical boundary for a detector with time scale `tau` is

```math
\boxed{
L_{\mathrm{crit}}(\tau)
=\tau\,\ell_{\mathrm{crit}}.
}
```

Hence

```math
\boxed{
\frac{L_{\mathrm{crit},s}}
{L_{\mathrm{crit},f}}
=\frac{\tau_s}{\tau_f}=r.
}
```

The slower member therefore remains feasible over a proportionally larger physical arrival-time interval in this particular normalized family.

## C. Proposition 1: existence of a fast-to-slow crossover

**Proposition 1 (task-dependent fast/slow ordering).** Consider the equal-eventual-SNR family above with `tau_f<tau_s`. Assume:

1. the requested `(alpha,beta)` operating point is feasible when the event arrival time is known;
2. `X_D(rho_0,alpha,beta,ell)` varies continuously with `ell` away from feasibility singularities;
3. the full-template global threshold `Gamma_infty(ell,alpha)` grows without bound as `ell` tends to infinity, so a finite critical search length exists for the chosen operating point;
4. as `ell` approaches `ell_crit` from below, the required dimensionless detection time diverges.

Then at least one finite physical arrival-time uncertainty `L_x` exists at which the two detectors have equal detection time, with the fast detector preferred at sufficiently small `L` and the slow detector preferred near the fast detector's feasibility boundary.

**Proof.** When `L=0`, both detectors have zero normalized timing uncertainty and therefore solve the same dimensionless decision problem. Let

```math
x_0=X_D(\rho_0,\alpha,\beta,0).
```

Known-time feasibility makes `x_0` finite. Hence

```math
T_{D,f}(0)=\tau_f x_0,
\qquad
T_{D,s}(0)=\tau_s x_0,
```

and therefore

```math
\boxed{T_{D,f}(0)<T_{D,s}(0).}
```

By continuity, the faster detector remains preferred for a nonzero neighborhood of `L=0`.

The critical physical search lengths are

```math
L_{\mathrm{crit},f}=\tau_f\ell_{\mathrm{crit}},
\qquad
L_{\mathrm{crit},s}=\tau_s\ell_{\mathrm{crit}}
=rL_{\mathrm{crit},f}.
```

Thus the faster detector reaches its feasibility boundary first. As

```math
L\uparrow L_{\mathrm{crit},f},
```

its normalized search length approaches `ell_crit`, so assumption 4 gives

```math
T_{D,f}(L)\to\infty.
```

At the same physical `L`, the slower detector's normalized search length approaches

```math
\frac{L_{\mathrm{crit},f}}{\tau_s}
=\frac{\ell_{\mathrm{crit}}}{r}
<\ell_{\mathrm{crit}},
```

so it remains strictly inside its feasible region and has finite detection time. The difference

```math
D(L)=T_{D,f}(L)-T_{D,s}(L)
```

is therefore negative at `L=0` and positive for `L` sufficiently close to `L_crit,f`. Continuity implies that at least one

```math
\boxed{
L_\times\in(0,L_{\mathrm{crit},f})
}
```

satisfies

```math
\boxed{
T_{D,f}(L_\times)=T_{D,s}(L_\times).
}
```

This proves the existence of a finite fast-to-slow crossover. `\square`

The proposition establishes existence, not uniqueness. The function `B_r(ell)` may in principle have more than one zero. Nor does the argument extend automatically to detector families that are not related by the present temporal scaling, to unequal eventual SNR, or to other composite-hypothesis decision rules.

## D. Physical content of the theorem

The crossover is not generated by an intrinsic speed–sensitivity tradeoff: eventual matched-filter SNR was explicitly held fixed. It is also not generated by a poor choice of integration time: Section III showed that each member individually benefits from additional observation time. The reversal arises because changing `tau` rescales two parts of one task in opposite directions:

```text
smaller tau
    -> smaller physical time per unit x
    -> earlier accumulation of the available evidence,

smaller tau
    -> larger L/tau
    -> larger normalized timing-search domain
    -> more stringent global search threshold.
```

Consequently, the detector ordering is not a function of `tau` alone. It is a property of the detector together with the arrival-time uncertainty, false-alarm requirement, detection-probability requirement, and decision rule.

For sufficiently small timing uncertainty, the physical time-scale advantage dominates and the fast detector reaches the decision first. At larger uncertainty, the global search burden can reverse that ordering while both detectors remain feasible. Beyond the faster detector's critical search length, the present family enters a slow-only feasibility regime before the slower detector eventually reaches its own boundary.

This task structure is the principal detector-facing result of the paper. It should not be read as a claim that slower detectors are generally superior. Rather, it gives an explicit family in which equal asymptotic sensitivity is insufficient to define a detector-only ordering for a finite-time, unknown-arrival decision task.

---

## References

[1] R. Clark Jones, “Energy Detectable by Radiation Detectors,” *Journal of the Optical Society of America* **50**, 883–886 (1960). DOI: 10.1364/JOSA.50.000883.

[2] J. P. Garcia and E. L. Dereniak, “Extrinsic silicon photodetector characterization,” *Applied Optics* **29**, 559–569 (1990). DOI: 10.1364/AO.29.000559.

[3] Y. Yang *et al.*, “Overcoming the sensitivity–speed trade-off in two-dimensional photodetectors via a functional oxide interlayer,” *Nature Communications* **17**, 6077 (2026).

[4] V. Pecunia *et al.*, “Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies,” *Nature Photonics* **19**, 1178–1188 (2025). DOI: 10.1038/s41566-025-01759-1.

[5] R. Vio and P. Andreani, “On the Correct Estimate of the Probability of False Detection of the Matched Filter in Weak-Signal Detection Problems,” arXiv:1602.02392 (2016).

[6] G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, and E. Ruiz Morales, “The False Alarms induced by Gaussian Noise in Gravitational Wave Detectors,” *Physical Review D* **107**, 023027 (2023). DOI: 10.1103/PhysRevD.107.023027.

[7] R. P. Croce *et al.*, “Correlator Bank Detection of GW chirps. False-Alarm Probability, Template Density and Thresholds: Behind and Beyond the Minimal-Match Issue,” *Physical Review D* **70**, 122001 (2004). DOI: 10.1103/PhysRevD.70.122001.

---

## Draft boundary

Paper A is now drafted through the mathematical core in Section IV. The specialized Steps 13–49 Gaussian-extremes closure machinery remains outside the main narrative. The next drafting step should write Section V (interpretation, limitations, detector-specification implications) and then perform a manuscript-level consistency pass; it should not reopen the stopped closure chain.