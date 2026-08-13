# Task-Dependent Guarantee-Time Ordering of Photodetector Channels with Equal Eventual Matched-Filter SNR

**Draft status:** TECHNICAL CORE PASSES INTERNAL ADVERSARIAL QA / continuum witness / novelty not established  
**Date:** 2026-08-12

## Abstract

Specific detectivity, `D*`, is useful for comparing photodetector sensitivity under stated measurement conditions, but it does not by itself define the outcome of an arbitrary time-dependent detection task. Here we study a narrower question. Two causal linear photodetector channels observe the same optical event and are deliberately normalized to have the same eventual matched-filter signal-to-noise ratio `rho_0`, while their response time scales differ. Event arrival is known only to lie in a fixed physical window of duration `L`. A batch receiver scans all candidate arrival times with a finite-duration matched filter and sets one threshold from the maximum of the correlated noise-only timing scan so that the global false-alarm probability is `alpha`.

A candidate filter duration `t` requires a record through `L+t`. We define `T_G` as the minimum **post-window integration duration** for which the statistic at the true event alignment exceeds the global threshold with probability at least `beta`. Because true-alignment threshold crossing is a subset of threshold crossing by the complete signal-present scan, this criterion guarantees total scan-detection probability at least `beta`, but it is not the exact signal-present scan-power criterion.

For the controlled time-scaled family,

```math
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right),
```

and the batch wall-clock time is

```math
T_{\rm wall}=L+T_G.
```

At fixed `L`, both clocks induce the same channel ordering. Shortening `tau` accelerates evidence accumulation but also increases the normalized timing-search interval `L/tau`. For the constructed family, these competing effects imply at least one finite fast-to-slow **guarantee-time** crossover and a slow-only guarantee-feasibility region. A continuous-process witness at `rho_0=3.5`, `alpha=0.05`, `beta=0.90`, and `tau_s/tau_f=6` provides a concrete scale: fast is preferred at known arrival, whereas at `L=9 tau_f=1.5 tau_s`,

```math
P_{FA,s}\le0.0336428<0.05<0.0624701\le P_{FA,f},
```

so slow is guarantee-feasible and fast guarantee-infeasible. The result is task- and protocol-specific. It does not prove a reversal of exact full signal-present scan detection times, does not establish a general preference for slower photodetectors, and does not introduce a universal replacement for `D*`.

---

# I. Introduction

Specific detectivity, `D*`, is one of the most widely used figures of merit for photodetector comparison. Its conventional normalization includes detector area and noise-equivalent measurement bandwidth; that bandwidth normalization should not be confused with the detector's temporal response bandwidth or `-3 dB` speed. `D*` remains useful when the operating condition to which it refers is specified, but it is not a complete descriptor of arbitrary time-dependent detection. That limitation is longstanding rather than new. Jones treated energy detection from radiation pulses using frequency-dependent detectivity in 1960 [1], detector characterization has long treated temporal bandwidth as a separate performance dimension [2,3], and modern guidance emphasizes application- and protocol-dependent characterization [4].

The relevant signal-detection quantity also depends on the task. For a known deterministic waveform observed for sufficiently long time in stationary Gaussian noise, maximum matched-filter SNR is set by the spectral overlap of signal and noise. Unknown arrival time changes the problem because event time becomes a nuisance parameter. A fixed global false-alarm probability must then be imposed over a correlated timing scan, and the threshold depends on the correlation structure of that scan rather than on raw digital sample count alone [5–7].

Unknown-delay acquisition itself is mature. Classical spread-spectrum work derives acquisition-time statistics from search-region size, dwell strategy, predetection SNR, detection probability, false alarms, and a priori epoch information [10,11]. Related acquisition problems occur in optical CDMA [12–14] and direct-detection ladar [8]. The present construction does **not** claim these ingredients as new.

The question here is narrower: what happens when the **detector response time itself** rescales both finite-time evidence accumulation and the normalized unknown-arrival search while eventual matched-filter SNR for one specified optical event is deliberately held fixed?

The theorem does not assume that the channels have equal conventional `D*`. The equal-`rho_0` normalization is a distinct, event-specific choice made to remove eventual matched-filter sensitivity as a confounding variable. It should not be identified with equality of a scalar reference `D*`.

The two effects of shorter `tau` oppose one another:

```text
shorter detector time scale
    -> faster accumulation of signal evidence,

but also

shorter detector time scale
    -> shorter timing-scan correlation length
    -> larger normalized unknown-arrival search.
```

The issue is whether this coupling can prevent a detector-only ordering by response time after eventual matched-filter SNR has been equalized.

The paper does **not** solve a sequential online stopping problem, and it does **not** derive the exact signal-present scan detection probability. It defines a batch acquisition protocol and a conservative sufficient criterion: the matched-filter statistic at the true arrival alignment must exceed a threshold calibrated against the maximum of the complete noise-only scan. Meeting that criterion with probability `beta` guarantees that the complete signal-present scan detects with probability at least `beta`.

---

# II. Controlled equal-eventual-SNR photodetector family

## A. Common optical event and causal detector realization

All channels receive

```math
p(t)=e^{-bt}u(t),
\qquad b>0,
```

with

```math
P(s)=\frac1{s+b}.
```

For each detector time scale `tau>0`, define

```math
\boxed{
G_\tau(s)
=A_\tau\frac{s+b}{(s+1/\tau)^2}.
}
```

Then

```math
G_\tau(s)P(s)=\frac{A_\tau}{(s+1/\tau)^2},
```

so

```math
\boxed{
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
}
```

The exact pole-zero matching is part of this controlled **existence construction**, not a claim of generic detector microphysics.

The channel impulse response is

```math
\boxed{
g_\tau(t)
=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac1\tau\right)t\right]u(t).
}
```

For a finite pair with `tau_f<tau_s`, choosing

```math
b\ge\frac1{\tau_f}
```

makes both impulse responses nonnegative for all `t>=0`.

## B. Noise convention and equal eventual matched-filter SNR

Let

```math
\boxed{
E[n(t)n(t')]=N\delta(t-t').
}
```

Then

```math
\rho^2=\frac1N\int s^2(t)dt.
```

For the full output waveform,

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

for every channel.

This equality is event-specific and is distinct from equality of scalar `D*`.

Let

```math
x=t/\tau.
```

The accumulated fraction of total squared matched-filter SNR is

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

Since

```math
\eta'(x)=4x^2e^{-2x}>0,
```

each channel monotonically accumulates evidence.

## C. Finite-template timing covariance

The normalized finite template is proportional to

```math
h_x(v)=v e^{-v}1_{[0,x]}(v).
```

For `0<=y<x`, the normalized noise-only timing covariance is

```math
\boxed{
R_x(y)
=\frac{
\int_0^{x-y}v(v+y)e^{-2v-y}dv
}{
\int_0^xv^2e^{-2v}dv},
}
```

and `R_x(y)=0` for `y>=x`.

In physical units,

```math
r_{\tau,t}(\Delta)=R_{t/\tau}(|\Delta|/\tau).
```

Thus the normalized search length over one fixed physical uncertainty interval is

```math
\boxed{\ell=L/\tau.}
```

---

# III. Batch acquisition and guarantee-time surface

## A. Acquisition clock

The event arrival `theta` is known only to satisfy

```math
0\le\theta\le L.
```

A duration-`t` template applied at every candidate arrival requires data through `L+t`.

Define the post-window guarantee time `T_G`; the corresponding batch wall time is

```math
\boxed{T_{wall}=L+T_G.}
```

At fixed `L`, adding the common term does not alter channel ordering.

## B. Global false-alarm threshold

Let `Z_x(q)` be the normalized noise-only timing scan with covariance `R_x` and normalized search length `ell`. Define

```math
\boxed{
\Gamma(x,\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_x(q)>u\right]\le\alpha
\right\}.
}
```

No independent-trials approximation is used.

## C. True-alignment guarantee

Let `q_0` be the generative true alignment. **The receiver is not given `q_0`; it scans the full interval.**

At `q_0`, the signal-present statistic has unit variance and mean `rho_0 sqrt(eta(x))`. Hence

```math
\boxed{
P_{D,true}(x)
=\Phi\left[
\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha)
\right].
}
```

The complete signal-present scan has

```math
P_D^{scan}(x)
=\Pr\left[\sup_qY_x(q)>\Gamma\right].
```

Pathwise,

```math
\boxed{P_D^{scan}(x)\ge P_{D,true}(x).}
```

Thus `P_D,true>=beta` is a sufficient guarantee that `P_D^scan>=beta`.

Define

```math
M_G(x;\ell)=\rho_0\sqrt{\eta(x)}-\Gamma(x,\ell,\alpha),
```

and

```math
\boxed{
X_G(\rho_0,\alpha,\beta,\ell)
=\inf\{x>0:M_G(x;\ell)\ge\Phi^{-1}(\beta)\}.
}
```

Then

```math
\boxed{
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\left(\rho_0,\alpha,\beta,\frac L\tau\right).
}
```

## D. Monotonicity in integration duration

For fixed lag `y`, `R_x(y)` can be written as a positive-weight average of a nondecreasing function of the integration limit. Therefore

```math
x_2>x_1\Longrightarrow R_{x_2}(y)\ge R_{x_1}(y).
```

Slepian comparison [9] gives

```math
\Gamma(x_2,\ell,\alpha)
\le\Gamma(x_1,\ell,\alpha).
```

Since the SNR term also increases strictly, the guarantee margin is strictly increasing with `x`.

## E. Full-template limit and feasibility

As `x->infinity`,

```math
\boxed{
R_\infty(y)=(1+y)e^{-y},
\qquad y\ge0.
}
```

Define the full-template threshold

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_\infty(q)>u\right]\le\alpha
\right\}.
}
```

Normalized-template `L2` convergence gives the uniform covariance bound

```math
\sup_y|R_x(y)-R_\infty(y)|
\le2\|\hat h_x-\hat h_\infty\|_2
\to0.
```

Threshold convergence is used under ordinary compact-interval Gaussian-supremum/quantile continuity regularity.

Finite guarantee time exists when

```math
\boxed{
\Gamma_\infty(\ell,\alpha)
<\rho_0-\Phi^{-1}(\beta).
}
```

Because `R_infty(y)->0`, widely separated samples plus Slepian comparison imply

```math
\boxed{
\Gamma_\infty(\ell,\alpha)\to\infty
\qquad(\ell\to\infty).
}
```

---

# IV. Task-dependent fast/slow guarantee ordering

## A. Exact task boundary

Let

```math
\tau_f<\tau_s,
\qquad
r=\tau_s/\tau_f>1,
\qquad
\ell=L/\tau_s.
```

Then

```math
T_{G,f}=\tau_fX_G(\rho_0,\alpha,\beta,r\ell),
```

```math
T_{G,s}=r\tau_fX_G(\rho_0,\alpha,\beta,\ell),
```

so the exact preference boundary is

```math
\boxed{
B_r(\ell)
=X_G(\rho_0,\alpha,\beta,r\ell)
-rX_G(\rho_0,\alpha,\beta,\ell)=0.
}
```

## B. Feasibility partition

Let

```math
c=\rho_0-\Phi^{-1}(\beta).
```

Since `Gamma_infty` is nondecreasing in search length, the only regimes are

```math
\boxed{
\begin{array}{ll}
\text{both feasible:} & c>\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{slow only:} & \Gamma_\infty(\ell,\alpha)<c\le\Gamma_\infty(r\ell,\alpha),\\[4pt]
\text{neither:} & c\le\Gamma_\infty(\ell,\alpha).
\end{array}}
```

Fast-only feasibility is impossible in this scaled equal-eventual-SNR family.

Define

```math
\ell_{crit}
=\sup\{\ell:\Gamma_\infty(\ell,\alpha)<c\}.
```

Then

```math
L_{crit}(\tau)=\tau\ell_{crit}.
```

For every finite `x`, `eta(x)<1` and `Gamma(x,ell)>=Gamma_infinity(ell)`. At the continuous critical boundary, no finite `x` reaches the target. Therefore

```math
\boxed{
X_G(\ell)\to\infty
\qquad(\ell\uparrow\ell_{crit}).
}
```

## C. Proposition 1: crossover existence

Assume known-time guarantee feasibility and ordinary continuity of the threshold/first-crossing surface in the feasible interior and at the full-template boundary.

At `L=0`, both channels have the same dimensionless first crossing `x_0`, so

```math
T_{G,f}(0)=\tau_fx_0<\tau_sx_0=T_{G,s}(0).
```

The fast physical feasibility boundary is

```math
L_{crit,f}=\tau_f\ell_{crit},
```

while

```math
L_{crit,s}=\tau_s\ell_{crit}>L_{crit,f}.
```

As `L` approaches `L_crit,f` from below, `T_G,f` diverges while the slow channel remains strictly feasible. Continuity therefore implies at least one

```math
\boxed{L_\times\in(0,L_{crit,f})}
```

such that

```math
\boxed{T_{G,f}(L_\times)=T_{G,s}(L_\times).}
```

The theorem proves existence, not uniqueness, and concerns sufficient guarantee times rather than exact full-scan detection times.

## D. Continuum quantitative regime witness

Choose

```math
\rho_0=3.5,
\qquad
\alpha=0.05,
\qquad
\beta=0.90,
\qquad
r=6.
```

At known arrival,

```math
\boxed{x_0=1.80519795247,}
```

so fast is exactly preferred.

Now take

```math
\boxed{L=9\tau_f=1.5\tau_s.}
```

Then

```math
\ell_f=9,
\qquad
\ell_s=1.5,
```

and

```math
c=\rho_0-\Phi^{-1}(\beta)
=2.21844843445540.
```

### Slow side

For the full-template process,

```math
R_\infty''(0)=-1.
```

Rice's exact mean upcrossing formula [15] gives

```math
\nu_c^+=\frac1{2\pi}e^{-c^2/2}.
```

A path exceeding `c` must start above `c` or contain at least one upcrossing. Hence

```math
\boxed{
P_{FA,s}
\le Q(c)+\frac{1.5}{2\pi}e^{-c^2/2}
=0.0336427995841<0.05.
}
```

Thus

```math
\Gamma_\infty(1.5,0.05)<c,
```

and the slow channel is guarantee-feasible.

### Fast side

Take seven points over `[0,9]` at spacing `1.5`. Their distinct-pair covariances are at most

```math
\epsilon=R_\infty(1.5)=0.557825400371075.
```

Compare with

```math
Y_i=\sqrt\epsilon V+\sqrt{1-\epsilon}E_i,
\qquad i=1,\ldots,7,
```

where all variables on the right are independent except for the common component `V`. Slepian gives

```math
\Pr[\max_iZ_i>c]\ge\Pr[\max_iY_i>c].
```

The one-dimensional Gaussian integral for the comparison vector gives

```math
\boxed{
\Pr[\max_iY_i>c]=0.0624701020698>0.05.
}
```

Therefore

```math
\Gamma_\infty(9,0.05)>c,
```

and the fast channel is guarantee-infeasible.

Thus

```math
\boxed{
P_{FA,s}\le0.0336428<0.05<0.0624701\le P_{FA,f}.
}
```

This is a continuous-process regime bracket, not a numerical localization of `L_x`. The calculation is reproduced by `numerics/paper_a_analytic_feasibility_bracket.py`.

---

# V. Interpretation and limitations

The ordered object is a **task-level sufficient guarantee time**, not an intrinsic detector latency.

The result does not make conventional detector figures of merit incorrect. It shows that, for the constructed unknown-arrival batch task, detector response time enters both evidence accumulation and the statistical size of the timing search.

Classical acquisition theory already contains uncertainty-region, SNR, false-alarm, detection-probability, dwell, matched-filter, and search-strategy tradeoffs [8,10–14]. Paper A does not claim those ingredients as new.

Its narrower construction is that changing detector time scale changes both the evidence clock and normalized timing-search geometry while the eventual matched-filter SNR for the specified optical event is held equal.

Sensitivity-speed products are also established [2,3]. No universal replacement scalar is proposed.

The model remains idealized:

- linear time-scaled channels;
- additive stationary white Gaussian output noise;
- event-specific equal eventual SNR;
- only arrival time is unknown;
- the transfer family is an existence construction;
- the receiver is batch;
- the guarantee is conservative;
- crossover uniqueness is not established;
- exact signal-present scan-time reversal is not established.

The central practical statement is:

> **For an unknown-arrival batch detection task, detector response time affects both evidence accumulation and the statistical size of the timing search. Equal eventual matched-filter SNR therefore need not imply a detector-only ordering of the integration time required to guarantee a specified global-scan operating point.**

---

# VI. Conclusion

For the constructed causal detector family driven by one common optical event and normalized to equal event-specific eventual matched-filter SNR,

```math
T_G
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac L\tau\right).
```

A shorter detector time scale accelerates evidence accumulation but enlarges the normalized unknown-arrival search. Under the stated continuity regularity, at least one fast-to-slow guarantee-time crossover follows.

The continuum witness gives a finite-scale example: fast is preferred at known arrival, whereas for `rho0=3.5`, `alpha=.05`, `beta=.90`, `tau_s/tau_f=6`, and `L=9 tau_f=1.5 tau_s`,

```math
P_{FA,s}\le.0336428<.05<.0624701\le P_{FA,f},
```

so slow is guarantee-feasible and fast guarantee-infeasible.

The result is narrower than an exact unknown-arrival scan-power theorem and narrower than classical acquisition theory as a whole. Novelty of the detector-scaling synthesis remains unestablished.

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

[10] A. Polydoros and C. L. Weber, “A Unified Approach to Serial Search Spread-Spectrum Code Acquisition—Part II: A Matched-Filter Receiver,” *IEEE Transactions on Communications* **32**(5), 550–560 (1984). DOI: 10.1109/TCOM.1984.1096113.

[11] Y.-T. Su, “Rapid Code Acquisition Algorithms Employing PN Matched Filters,” *IEEE Transactions on Communications* **36**(6), 724–733 (1988). DOI: 10.1109/26.2793.

[12] M. M. Mustapha and R. F. Ormondroyd, “Dual-Threshold Sequential Detection Code Synchronization for an Optical CDMA Network in the Presence of Multi-User Interference,” *Journal of Lightwave Technology* **18**(12), 1742–1748 (2000). DOI: 10.1109/50.908711.

[13] A. Keshavarzian and J. A. Salehi, “Optical Orthogonal Code Acquisition in Fiber-Optic CDMA Systems via the Simple Serial-Search Method,” *IEEE Transactions on Communications* **50**(3), 473–483 (2002). DOI: 10.1109/26.990909.

[14] A. T. Pham and H. Yashima, “Performance Analysis of MDSS Code Acquisition Using SLS for Optical CDMA Systems,” *IEICE Transactions on Communications* **E88-B**(12), 4570–4577 (2005). DOI: 10.1093/ietcom/e88-b.12.4570.

[15] S. O. Rice, “Mathematical Analysis of Random Noise,” *Bell System Technical Journal* **23**(3), 282–332 (1944). DOI: 10.1002/j.1538-7305.1944.tb00874.x.
