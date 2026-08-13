# Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity

**Draft status:** Paper A complete detector-facing manuscript / consistency-compressed / novelty not established  
**Date:** 2026-08-12

## Abstract

Specific detectivity is a useful measure of detector sensitivity under stated operating conditions, but pulse detection and sensitivity–bandwidth tradeoffs are already known to require temporal or spectral information beyond a single scalar figure of merit. Here we ask a different question: if two detector channels are deliberately normalized to have the same eventual matched-filter signal-to-noise ratio, does the faster detector necessarily reach a prescribed detection decision first when event arrival time is unknown? For a controlled time-scaled Gaussian detector family under a specified global-false-alarm matched-filter scan, the detection time takes the exact dimensionless form

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
```

where `tau` is the detector time scale, `L` is the physical arrival-time uncertainty interval, `alpha` is the allowed global false-alarm probability, `beta` is the required true-alignment detection probability, and `rho_0` is the common eventual matched-filter SNR. Shortening `tau` accelerates evidence accumulation but also increases the normalized search interval `L/tau` and shortens the correlation length of the timing scan. Under stated continuity and large-search assumptions, these competing effects imply at least one finite fast-to-slow detection-time crossover in the constructed equal-eventual-SNR family, together with a slow-only feasibility region near the faster detector's search-limited boundary. The result is task- and protocol-specific: it neither establishes a general preference for slower photodetectors nor introduces a universal replacement for `D*`.

---

# I. Introduction

Specific detectivity, `D*`, is one of the most widely used figures of merit for comparing photodetectors. It combines responsivity, noise, active area, and measurement bandwidth into a normalized sensitivity measure and is useful when the operating condition to which it refers is specified. It is not, however, a complete descriptor of arbitrary time-dependent detection. That limitation is longstanding rather than new. Jones treated the energy detectable from radiation pulses using frequency-dependent detectivity in 1960 [1], detector characterization has long treated temporal bandwidth as a separate performance dimension [2,3], and modern guidance emphasizes that detector figures of merit are meaningful only together with their measurement conditions [4].

The appropriate signal-detection quantity also depends on the task. For a known deterministic waveform observed for sufficiently long time in stationary Gaussian noise, the maximum matched-filter SNR is determined by the spectral overlap of the signal with the detector and noise response. In that restricted problem, a complete frequency-dependent sensitivity description can be sufficient. Unknown arrival time changes the problem. The receiver must search over a nuisance parameter—the event time—and a fixed global false-alarm probability must be imposed over the resulting correlated timing scan. This search penalty is established in matched-filter detection theory: false-alarm behavior depends on the correlation structure of the filtered process and cannot generally be identified with the raw digital sample count [5–7].

These observations motivate a narrower question than whether `D*` “contains bandwidth.” Suppose two detector channels are deliberately normalized so that neither has an eventual matched-filter sensitivity advantage. They produce the same eventual matched-filter SNR for the event of interest, but one responds on a shorter time scale than the other. If the event time were known, the faster detector would accumulate any fixed fraction of its available evidence sooner. If the event time is unknown, however, temporal compression also shortens the physical correlation length of the matched-filter output. Over one fixed physical arrival-time interval, the faster detector therefore presents a larger normalized timing-search domain.

The two effects oppose one another:

```text
shorter detector time scale
    -> faster accumulation of signal evidence,

but also

shorter detector time scale
    -> shorter timing-scan correlation length
    -> larger normalized unknown-arrival search.
```

The question studied here is whether that competition can prevent a detector-only ordering by response time even after eventual matched-filter SNR has been equalized.

We answer the question in a deliberately controlled family rather than attempt to model every physical detector mechanism. The family is time-scaled, linear, and observed in additive white Gaussian output noise. Its members are normalized to the same eventual matched-filter SNR `rho_0`. Event arrival is unknown over a physical interval `L`; one threshold is chosen to satisfy a global false-alarm probability `alpha`; and detection time is defined by reaching a specified true-alignment detection probability `beta`. The decision rule is explicit, but it is not asserted to be Bayes-optimal, minimax-optimal, or sequentially optimal for the general unknown-arrival problem.

Within this construction, detector time scale enters the decision problem twice: it sets the physical rate of evidence accumulation and rescales the nuisance-parameter domain through `L/tau`. The resulting detection time therefore takes the task-dependent form

```math
T_D
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

At known arrival time the faster member reaches the required decision first. As timing uncertainty grows, however, the faster detector searches the larger dimensionless interval and reaches its search-limited feasibility boundary at a smaller physical `L`. Under the assumptions stated below, these facts guarantee at least one finite fast-to-slow detection-time crossover. The result is a counterexample, within the constructed family, to a detector-only monotonic ordering by response time. It is not a claim that slower detectors are generally better.

Section II defines the equal-eventual-SNR family and derives its finite-time SNR and timing-scan covariance. Section III introduces the dimensionless detection-time surface. Section IV derives the fast/slow task boundary and feasibility partition. Section V discusses interpretation, limitations, and implications for detector specification and experiment design.

---

# II. Controlled equal-eventual-SNR detector family

## A. Time-scaled matched-filter template

We choose a family whose output signal for the event of interest is

```math
s_\tau(t)=A_\tau t e^{-t/\tau}u(t),
```

where `u(t)` is the unit step and `tau` sets the detector time scale. The waveform can be generated by a stable causal linear response, but here it is used primarily because temporal scaling is explicit and all members can be normalized to identical eventual matched-filter SNR.

Assume additive white Gaussian output noise with two-sided spectral density `N` under a consistent normalization. Choosing

```math
A_\tau=\frac{2\rho_0\sqrt{N}}{\tau^{3/2}}
```

gives

```math
\boxed{\rho_{\tau,\infty}=\rho_0}
```

for every `tau`. The comparison therefore removes eventual matched-filter sensitivity as an explanatory variable: any difference in finite-task performance must arise from temporal scaling and its interaction with the decision protocol.

Let

```math
x=\frac{t}{\tau}
```

be observation duration in detector-time units. The fraction of total squared matched-filter SNR accumulated by time `t` is

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

Because

```math
\eta'(x)=4x^2e^{-2x}>0
```

for `x>0`, each detector monotonically accumulates available evidence. At fixed physical time, the smaller-`tau` member has the larger `x` and therefore reaches any fixed fraction of its eventual SNR earlier.

## B. Unknown arrival time converts the same temporal scale into a search scale

Let the event arrival time be unknown within a physical interval of length `L`. At observation duration `t`, the normalized finite-record matched-filter template is proportional to

```math
h_x(v)=v e^{-v}\,1_{[0,x]}(v)
```

in detector-time units. Under noise alone, scanning this template across candidate arrival times produces a stationary Gaussian process whose normalized covariance depends only on the dimensionless lag

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

with

```math
R_x(y)=0,\qquad y\ge x.
```

Thus, in physical time,

```math
\boxed{
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).}
```

Reducing `tau` therefore does two things simultaneously: it accelerates signal accumulation and compresses the timing-scan covariance in physical lag. For one fixed physical uncertainty interval `L`, the faster detector searches the larger dimensionless interval

```math
\boxed{\ell=\frac{L}{\tau}.}
```

This is the competition formalized below.

---

# III. Detection time as a dimensionless task surface

## A. Global threshold for the correlated timing scan

Let `Z_x(q)` denote the normalized noise-only matched-filter scan at dimensionless trial arrival time `q`. For `x=t/tau`, `Z_x` is a zero-mean, unit-variance stationary Gaussian process with covariance

```math
\operatorname{Cov}[Z_x(q),Z_x(q')]
=R_x(|q-q'|).
```

For fixed `(x,ell,alpha)`, define the global threshold `Gamma(x,ell,alpha)` by

```math
\boxed{
\Pr\!\left[
\sup_{0\le q\le\ell}Z_x(q)>\Gamma(x,\ell,\alpha)
\right]=\alpha,
}
```

with the usual generalized-quantile interpretation when necessary. This definition retains the correlated timing search rather than replacing it by an independent-trials approximation. In physical units,

```math
\gamma_{\tau,t}(L,\alpha)
=\Gamma\!\left(\frac{t}{\tau},\frac{L}{\tau},\alpha\right).
```

At the true event alignment, the normalized matched-filter output under signal plus noise has unit variance and mean `rho_0 sqrt(eta(x))`. Under the true-alignment criterion used here,

```math
\boxed{
P_{D,\mathrm{true}}(x)
=\Phi\!\left[
\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\right].
}
```

Define the dimensionless decision margin

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

This criterion is narrower than the total probability that the maximum of the entire signal-present scan crosses threshold. It asks when the matched filter at the true alignment reaches the specified operating point while the threshold is set by the global noise-only search.

## B. Monotone first-crossing time

For this family, increasing observation duration improves the decision margin. The signal term increases strictly because `eta'(x)>0`. The global threshold does not increase.

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

Standard Gaussian comparison then gives

```math
\boxed{
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
}
```

Therefore `M(x;ell,rho_0,alpha)` is strictly increasing with `x`. Each detector individually benefits from additional observation time; the cross-detector reversal derived in Section IV is not produced by assigning one detector a self-suboptimal integration duration.

Define

```math
\boxed{
X_D(\rho_0,\alpha,\beta,\ell)
=\inf\left\{
x>0:
M(x;\ell,\rho_0,\alpha)\ge z_\beta
\right\}.
}
```

Whenever the requested operating point is feasible, this first crossing is unambiguous. Returning to physical time gives the central scaling relation

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

The scaling exposes the two opposing roles of `tau`: a smaller value shortens the physical time unit but evaluates the same dimensionless task surface at a larger search length `L/tau`.

## C. Full-template limit and task feasibility

As `x\to\infty`,

```math
\eta(x)\to1,
\qquad
R_x(y)\to R_\infty(y)=(1+y)e^{-y}.
```

Define

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
=\lim_{x\to\infty}\Gamma(x,\ell,\alpha)
}
```

and

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

If the reverse strict inequality holds, the requested operating point cannot be reached at any observation duration under the stated criterion. Equality defines the asymptotic feasibility boundary; under the strict-convergence assumption used below, it is approached only as `T_D\to\infty`.

The function `Gamma_infty(ell,alpha)` is nondecreasing in `ell` because enlarging the search interval enlarges the supremum domain. This monotonicity determines the feasibility structure without requiring a closed form for the correlated-scan quantile.

---

# IV. Task-dependent fast/slow ordering

## A. Exact task boundary

Consider two members of the family with equal eventual matched-filter SNR `rho_0` and

```math
\tau_f<\tau_s.
```

Define

```math
\boxed{r=\frac{\tau_s}{\tau_f}>1}
```

and measure timing uncertainty in units of the slower detector,

```math
\boxed{\ell=\frac{L}{\tau_s}.}
```

The faster detector then searches the normalized interval `r ell`, while the slower detector searches `ell`. Section III gives

```math
\boxed{
T_{D,f}=\tau_fX_D(\rho_0,\alpha,\beta,r\ell),
}
```

and

```math
\boxed{
T_{D,s}=r\tau_fX_D(\rho_0,\alpha,\beta,\ell).
}
```

The exact preference boundary is the zero set

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

This boundary must compare the full finite-time task surfaces. Comparing only eventual margins is insufficient: for every `L>0` the slower member has the smaller normalized search burden, yet at known arrival time the faster member reaches the same dimensionless decision point in less physical time.

## B. Feasibility partition

Let

```math
\boxed{c=\rho_0-z_\beta.}
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

The task therefore has three feasibility regimes:

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

A fast-only feasibility region is excluded within this deliberately equal-eventual-SNR scaled family.

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

The corresponding physical boundary is

```math
\boxed{
L_{\mathrm{crit}}(\tau)=\tau\ell_{\mathrm{crit}},
}
```

so

```math
\boxed{
\frac{L_{\mathrm{crit},s}}
{L_{\mathrm{crit},f}}
=\frac{\tau_s}{\tau_f}=r.
}
```

The slower member therefore remains feasible over a proportionally larger physical arrival-time interval in this normalized family.

## C. Proposition 1: existence of a fast-to-slow crossover

**Proposition 1 (task-dependent fast/slow ordering).** Consider the equal-eventual-SNR family above with `tau_f<tau_s`. Assume:

1. the requested `(alpha,beta)` operating point is feasible when event arrival time is known;
2. `X_D(rho_0,alpha,beta,ell)` varies continuously with `ell` away from feasibility singularities;
3. `Gamma_infty(ell,alpha)` grows without bound as `ell\to\infty`, so a finite critical search length exists for the chosen operating point;
4. as `ell\uparrow ell_crit`, the required dimensionless detection time diverges.

Then at least one finite physical arrival-time uncertainty `L_x` exists at which the two detectors have equal detection time. The faster detector is preferred for sufficiently small `L`, whereas the slower detector is preferred near the faster detector's feasibility boundary.

**Proof.** At `L=0`, both detectors solve the same dimensionless decision problem. Let

```math
x_0=X_D(\rho_0,\alpha,\beta,0).
```

Known-time feasibility makes `x_0` finite, so

```math
T_{D,f}(0)=\tau_fx_0,
\qquad
T_{D,s}(0)=\tau_sx_0,
```

and therefore

```math
\boxed{T_{D,f}(0)<T_{D,s}(0).}
```

By continuity, the faster detector remains preferred for a nonzero neighborhood of `L=0`.

The critical physical search lengths satisfy

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

so the slower detector remains strictly feasible and has finite detection time. Hence

```math
D(L)=T_{D,f}(L)-T_{D,s}(L)
```

is negative at `L=0` and positive for `L` sufficiently close to `L_crit,f`. Continuity implies that at least one

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

This proves existence of a finite fast-to-slow crossover. `\square`

The proposition establishes existence, not uniqueness. `B_r(ell)` may in principle have more than one zero. The argument also does not extend automatically to detector families unrelated by the present temporal scaling, unequal eventual SNR, or different composite-hypothesis decision rules.

---

# V. Interpretation, limitations, and implications for detector comparison

## A. Detector characterization versus task qualification

The result is easiest to misread if detector speed is treated only as a device-side bandwidth parameter. In the present task, changing `tau` changes both the physical rate at which signal evidence becomes available and the normalized nuisance-parameter search `L/tau`. The first effect favors the faster detector; the second can favor the slower detector because the slower response produces a more strongly correlated timing scan over the same physical arrival-time interval.

A detector specification such as `D*`, response time, or bandwidth describes a device under stated measurement conditions. A decision time such as `T_D`, by contrast, belongs to a detector together with a task. Here,

```math
\boxed{
T_D
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
}
```

so the ordering cannot be reduced to `tau` alone even after eventual matched-filter SNR has been fixed. The same two detector channels can occupy different preference regimes as arrival-time uncertainty or the decision criterion changes.

This does not make conventional figures of merit incorrect. It identifies the level at which they cease to define an ordering. For a finite-time decision with unknown event time, a statement that one detector is “better” than another is incomplete unless the task specifies the relevant waveform and noise model, arrival-time uncertainty, and false-alarm/detection criterion.

The result therefore separates **device characterization** from **task qualification**. Device characterization can report responsivity, noise, detectivity, bandwidth, and temporal response. Task qualification asks what those properties imply under a specified measurement protocol. Proposition 1 concerns the second problem.

## B. Why the conclusion is not another scalar sensitivity–speed metric

Sensitivity–speed combinations are already established in detector literature, and the present result does not motivate a new universal product. The relevant variable is not merely `tau` or bandwidth but

```math
\frac{L}{\tau},
```

while the decision surface also depends on

```math
\rho_0,\qquad \alpha,\qquad \beta,
```

and on the chosen search rule. Two tasks performed with the same detector can therefore correspond to different normalized search geometries. A scalar formed only from detector properties would erase the task dependence that produces the crossover.

The practical lesson is consequently not to replace `D*` with another detector-only number. It is to attach detector comparisons to the measurement problem for which the comparison is intended. For the present model, the compact object is the task surface

```math
X_D(\rho_0,\alpha,\beta,L/\tau),
```

not a universal scalar ranking.

## C. Physical meaning and scope of the crossover

The fast-to-slow crossover is not an intrinsic penalty for fast response. Every member is normalized to the same eventual matched-filter SNR,

```math
\rho_{\tau,\infty}=\rho_0,
```

and Section III showed that every member benefits monotonically from additional observation time. The reversal is therefore neither a conventional sensitivity–speed tradeoff nor an artifact of choosing a poor integration duration.

Instead, it arises from the statistical geometry of the unknown-arrival search. Compressing the response in physical time compresses the matched-filter correlation length. For fixed physical uncertainty `L`, the faster channel then spans a larger normalized timing domain. Maintaining the same global false-alarm probability requires a correspondingly more stringent threshold. At small `L`, the physical time-scale advantage dominates. Near the faster detector's feasibility boundary, the search burden is large enough that the slower detector remains feasible while the faster detector does not.

This interpretation is protocol specific. A Bayesian rule with an explicit arrival-time prior, a minimax test, a sequential procedure, or a joint detection/localization objective can produce a different task surface. Proposition 1 states what follows for the global-threshold matched-filter scan defined here; it is not a theorem about every statistically admissible receiver.

Several additional assumptions delimit the result. The detector family is linear and time-scaled, and the output noise is additive, stationary, Gaussian, and white under the chosen normalization. Real photodetectors can exhibit colored or signal-dependent noise, nonlinear response, saturation, dead time, drift, temperature dependence, and other effects. The channels are deliberately normalized to equal eventual matched-filter SNR; unequal eventual sensitivity adds another axis to the comparison. Arrival time is the only nuisance parameter; unknown amplitude, phase, spectral shape, background, or multiple nuisance parameters would enlarge the search space. Finally, detection probability is evaluated at the true alignment while the threshold is set by the global noise-only scan; this is narrower than a full signal-present maximum test and does not impose localization accuracy.

Proposition 1 proves existence of at least one crossover under the stated continuity and large-search assumptions. It does not establish uniqueness and does not imply that every practical parameter set contains a broad slow-preferred region. These restrictions are features of the construction: the aim is to exhibit a clean failure of detector-only ordering, not to claim a complete theory of transient photodetection.

## D. Implications for detector specification and experiment design

Reference-condition sensitivity remains useful for establishing the available signal-to-noise budget, and temporal response determines how quickly that budget can be accumulated. When event timing is uncertain and a global false-alarm requirement is imposed, however, the correlation structure of the timing statistic also becomes part of the measurement problem.

A task-oriented detector comparison should therefore report enough information to reconstruct the decision problem rather than only a device scalar. In the present setting the essential quantities are the eventual matched-filter SNR or the ingredients needed to calculate it, the temporal response or matched-filter template, the physical arrival-time uncertainty interval, and the required global false-alarm and detection probabilities. More general noise models or decision rules require the corresponding noise spectrum and protocol definition as well.

This is especially relevant when detectors with substantially different temporal responses are compared for transient measurements. A bandwidth or rise-time advantage does not automatically translate into a lower decision time once the detector is embedded in an unknown-arrival search. Conversely, the theorem does not license choosing a slower detector merely to reduce the search burden; at low timing uncertainty the faster detector remains preferred in the constructed family. The comparison must be made at the operating point of interest.

The central practical statement is therefore:

> **Detector specifications rank devices only relative to the task for which the ranking is being made. When arrival time is uncertain, response time affects both signal accumulation and the statistical size of the timing search.**

Within the controlled family studied here, that coupling is sufficient to reverse the fast/slow detection-time ordering even though eventual matched-filter sensitivity is identical.

## E. Conclusion

We considered two time-scaled photodetector channels normalized to equal eventual matched-filter SNR and asked whether the faster channel must reach a fixed detection operating point first when event arrival time is unknown. For the specified global-false-alarm matched-filter scan, the problem collapses to

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

The faster channel benefits from a smaller physical time scale but pays a larger normalized timing-search burden. Under the assumptions of Proposition 1, these effects imply at least one finite fast-to-slow crossover and a slow-only feasibility region before the slower detector reaches its own search-limited boundary.

The result is not a preference for slow detectors and does not replace established detector figures of merit. Its narrower implication is that equal eventual matched-filter sensitivity does not define a detector-only ordering for this finite-time, unknown-arrival task. The ordering belongs to the detector together with the measurement protocol.

---

## References

[1] R. Clark Jones, “Energy Detectable by Radiation Detectors,” *Journal of the Optical Society of America* **50**, 883–886 (1960). DOI: 10.1364/JOSA.50.000883.

[2] J. P. Garcia and E. L. Dereniak, “Extrinsic silicon photodetector characterization,” *Applied Optics* **29**, 559–569 (1990). DOI: 10.1364/AO.29.000559.

[3] Y. Yang *et al.*, “Overcoming the sensitivity–speed trade-off in two-dimensional photodetectors via a functional oxide interlayer,” *Nature Communications* **17**, 6077 (2026).

[4] V. Pecunia *et al.*, “Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies,” *Nature Photonics* **19**, 1178–1188 (2025). DOI: 10.1038/s41566-025-01759-1.

[5] R. Vio and P. Andreani, “On the Correct Estimate of the Probability of False Detection of the Matched Filter in Weak-Signal Detection Problems,” arXiv:1602.02392 (2016).

[6] G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, and E. Ruiz Morales, “The False Alarms induced by Gaussian Noise in Gravitational Wave Detectors,” *Physical Review D* **107**, 023027 (2023). DOI: 10.1103/PhysRevD.107.023027.

[7] R. P. Croce *et al.*, “Correlator Bank Detection of GW chirps. False-Alarm Probability, Template Density and Thresholds: Behind and Beyond the Minimal-Match Issue,” *Physical Review D* **70**, 122001 (2004). DOI: 10.1103/PhysRevD.70.122001.
