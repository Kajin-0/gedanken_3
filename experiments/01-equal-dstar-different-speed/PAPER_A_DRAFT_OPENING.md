# Task-Dependent Ordering of Photodetectors with Equal Asymptotic Sensitivity

**Draft status:** Paper A opening draft / detector-facing main narrative / novelty not established  
**Date:** 2026-08-12

## Abstract

Specific detectivity is a useful measure of detector sensitivity under a stated operating condition, but pulse detection and sensitivity–bandwidth tradeoffs are already known to require temporal or spectral information beyond a single scalar figure of merit. Here we ask a different question: if two detector channels are deliberately normalized to have the same eventual matched-filter signal-to-noise ratio, does the faster detector necessarily reach a prescribed detection decision first when the event arrival time is unknown? For a controlled time-scaled Gaussian detector family under a specified global-false-alarm matched-filter scanning protocol, the detection time takes the dimensionless form

```math
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,X_D\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
```

where `tau` is the detector time scale, `L` is the physical arrival-time uncertainty interval, `alpha` is the allowed global false-alarm probability, `beta` is the required true-alignment detection probability, and `rho_0` is the common eventual matched-filter SNR. Shortening `tau` accelerates finite-time evidence accumulation but simultaneously increases the normalized search interval `L/tau` and shortens the correlation length of the timing scan. Under stated continuity and large-search assumptions, these competing effects imply at least one finite fast-to-slow detection-time crossover in the constructed equal-eventual-SNR family, together with a slow-only feasibility regime near the faster detector's search-limited boundary. The result is task- and protocol-specific: it does not imply that slower photodetectors are generally superior, does not assert universal optimality of the chosen search rule, and does not introduce a universal replacement for `D*`.

---

## Central proposition — equal-eventual-SNR task reversal

**Proposition 1 (task-dependent fast/slow ordering).** Consider a time-scaled family of linear detector channels whose matched-filter output templates have characteristic time scale `tau` and are normalized so that every member has the same eventual matched-filter SNR `rho_0`. Let an event arrive at an unknown time within a physical interval of length `L`. For each candidate arrival time, use the corresponding finite-record matched filter and impose a threshold chosen to give global false-alarm probability `alpha` over the entire timing scan. Define the detection time as the earliest observation duration for which the true-alignment detection probability reaches `beta`.

For the family defined below, the detection time has the exact scaling form

```math
\boxed{
T_D(\alpha,\beta,L;\tau,\rho_0)
=\tau\,
X_D\!\left(
\rho_0,\alpha,\beta,\frac{L}{\tau}
\right).
}
```

Now compare two members with

```math
\tau_f<\tau_s,
\qquad
r=\frac{\tau_s}{\tau_f}>1,
```

and define

```math
\ell=\frac{L}{\tau_s}.
```

Then

```math
T_{D,f}
=\tau_f X_D(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{D,s}
=r\tau_f X_D(\rho_0,\alpha,\beta,\ell),
```

so their task boundary is the zero set

```math
\boxed{
B_r(\ell;\rho_0,\alpha,\beta)
=X_D(\rho_0,\alpha,\beta,r\ell)
-rX_D(\rho_0,\alpha,\beta,\ell)=0.
}
```

Assume that (i) the required operating point is feasible when arrival time is known; (ii) the Gaussian-scan threshold and resulting detection-time surface vary continuously with timing-search length away from feasibility singularities; (iii) the full-template global threshold increases without bound as the normalized search interval tends to infinity; and (iv) the detection time diverges as a detector approaches its asymptotic feasibility boundary from below. Then:

1. at `L=0`, the faster member reaches the required decision first;
2. the maximum feasible physical arrival-time uncertainty satisfies

```math
\boxed{L_{crit}(\tau)=\tau\,\ell_{crit},}
```

so the faster member reaches its feasibility boundary first;
3. as `L` approaches that fast-detector boundary, the fast detection time diverges while the slow detector remains feasible;
4. therefore at least one finite `L_x` exists for which

```math
\boxed{T_{D,f}(L_x)=T_{D,s}(L_x).}
```

Within this equal-eventual-SNR scaled family, a slow-only feasibility region is possible whereas a fast-only feasibility region is excluded. The proposition does **not** establish uniqueness of the crossover and does not assert the same ordering for other detector families or other unknown-arrival decision rules.

---

# I. Introduction

Specific detectivity, `D*`, is one of the most widely used figures of merit for comparing photodetectors. It combines responsivity, noise, active area, and measurement bandwidth into a normalized sensitivity measure and is useful when the operating condition to which it refers is specified. It is not, however, a complete descriptor of arbitrary time-dependent detection. That limitation is longstanding rather than new. Jones treated the energy detectable from radiation pulses using frequency-dependent detectivity in 1960 [1], and detector characterization has long treated temporal bandwidth as a separate performance dimension [2,3]. Modern guidance likewise emphasizes that detector figures of merit are meaningful only together with their measurement conditions [4].

The appropriate signal-detection quantity also depends on the task. For a known deterministic waveform observed for sufficiently long time in stationary Gaussian noise, the maximum matched-filter SNR is determined by the spectral overlap of the signal with the detector/noise transfer function. In that restricted problem, a complete frequency-dependent sensitivity description can be sufficient. Unknown arrival time changes the problem. The receiver must then search over a nuisance parameter—the event time—and a fixed global false-alarm probability must be distributed over the resulting correlated timing scan. This search penalty is established in matched-filter detection theory: false-alarm behavior depends on the correlation structure of the filtered process and cannot generally be identified with the raw digital sample count [5–7].

These observations motivate a narrower question than whether `D*` "contains bandwidth." Suppose two detector channels are deliberately normalized so that neither has an eventual matched-filter sensitivity advantage. They produce the same asymptotic matched-filter SNR for the event of interest, but one responds on a shorter time scale than the other. If the event time were known, the faster detector would naturally accumulate a given fraction of its available evidence sooner. If event time is unknown, however, temporal compression also makes the matched-filter output decorrelate over a shorter physical lag. Over one fixed physical arrival-time interval, the faster detector therefore presents a larger normalized timing-search domain.

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

The remainder of the paper is organized as follows. Section II defines the equal-eventual-SNR family and derives the finite-time SNR and timing-scan covariance. Section III introduces the dimensionless detection-time surface. Section IV derives the fast/slow task boundary and feasibility partition. Section V discusses the interpretation, limitations, and implications for detector specification and comparison.

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

This is the central competition. Detector speed does not merely change when signal evidence becomes available; under an unknown-arrival global-false-alarm task it also changes the statistical size of the timing search. The next section converts these two scalings into a single dimensionless detection-time surface.

---

## References cited in this opening draft

[1] R. Clark Jones, "Energy Detectable by Radiation Detectors," *Journal of the Optical Society of America* **50**, 883–886 (1960). DOI: 10.1364/JOSA.50.000883.

[2] J. P. Garcia and E. L. Dereniak, "Extrinsic silicon photodetector characterization," *Applied Optics* **29**, 559–569 (1990). DOI: 10.1364/AO.29.000559.

[3] Y. Yang *et al.*, "Overcoming the sensitivity–speed trade-off in two-dimensional photodetectors via a functional oxide interlayer," *Nature Communications* **17**, 6077 (2026).

[4] V. Pecunia *et al.*, "Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies," *Nature Photonics* **19**, 1178–1188 (2025). DOI: 10.1038/s41566-025-01759-1.

[5] R. Vio and P. Andreani, "On the Correct Estimate of the Probability of False Detection of the Matched Filter in Weak-Signal Detection Problems," arXiv:1602.02392 (2016).

[6] G. Morras, J. F. Nuño Siles, J. Garcia-Bellido, and E. Ruiz Morales, "The False Alarms induced by Gaussian Noise in Gravitational Wave Detectors," *Physical Review D* **107**, 023027 (2023). DOI: 10.1103/PhysRevD.107.023027.

[7] R. P. Croce *et al.*, "Correlator Bank Detection of GW chirps. False-Alarm Probability, Template Density and Thresholds: Behind and Beyond the Minimal-Match Issue," *Physical Review D* **70**, 122001 (2004). DOI: 10.1103/PhysRevD.70.122001.

---

## Draft boundary

This file intentionally stops after the opening controlled-family setup. It does not import the Steps 13–49 Gaussian-extremes closure machinery into Paper A. The next drafting step should write Section III (`T_D=\tau X_D(...)`) and Section IV (task-boundary proposition/proof) in manuscript form, while keeping the stated scope and novelty restrictions intact.
