# Task-dependent photodetector ordering under unknown arrival time

**Target:** Applied Optics — Research Article  
**Status:** journal-facing draft derived from the audited Paper A theorem; not yet submission-formatted  
**Date:** 2026-08-13

## Abstract

Photodetector response time is usually treated as an intrinsic speed advantage, but transient detection with unknown arrival time couples response time to the size of the timing search. We construct causal detector channels with equal event-specific eventual matched-filter SNR and analyze a batch matched-filter receiver with fixed global false-alarm probability. The required post-window guarantee time scales as `tau X_G(rho_0,alpha,beta,L/tau)`. Faster response accumulates evidence sooner but enlarges the normalized search interval. We prove at least one fast-to-slow ordering crossover and give a continuous-time feasibility witness in which the slow channel remains feasible while the fast channel does not.

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

We construct a causal time-scaled detector family for which this competition can be analyzed exactly. The receiver uses one global noise-only threshold and a conservative true-alignment condition that guarantees the complete scan has detection probability at least `beta`. The resulting quantity is therefore a **sufficient batch guarantee time**, not an intrinsic detector latency and not the exact first crossing time of the full signal-present scan.

The main result is

```math
T_G(\alpha,\beta,L;\tau,\rho_0)
=\tau X_G\!\left(\rho_0,\alpha,\beta,\frac{L}{\tau}\right).
```

At known arrival the faster channel wins. At sufficiently large timing uncertainty the faster channel reaches its guarantee-feasibility boundary first, while the slower channel remains feasible. Under ordinary continuity regularity this forces at least one finite fast-to-slow guarantee-time crossover. A continuous-time Rice/Slepian bracket provides a finite-scale example without numerical localization of the crossover.

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

Then

```math
G_\tau(s)P(s)=\frac{A_\tau}{(s+1/\tau)^2},
```

and the detector output for the selected event is

```math
\boxed{
s_\tau(t)=A_\tau t e^{-t/\tau}u(t).
}
```

The pole-zero matching is a controlled existence construction used to isolate temporal scaling; it is not proposed as a generic microscopic detector model. Its impulse response is

```math
\boxed{
g_\tau(t)=A_\tau e^{-t/\tau}
\left[1+\left(b-\frac{1}{\tau}\right)t\right]u(t).
}
```

For a finite fast/slow pair with `tau_f<tau_s`, choosing `b>=1/tau_f` makes both impulse responses nonnegative.

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

for every channel. This normalization is **event-specific** and is distinct from equality of a scalar conventional `D*`.

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

shorter `tau` always accumulates a given fraction of the eventual evidence sooner in physical time. Figure 1 will show this known-arrival advantage directly.

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

A duration-`t` template must be evaluable even for the latest candidate `theta=L`, so the batch record must extend through `L+t`. The normalized search length is

```math
\boxed{\ell=L/\tau.}
```

Thus reducing `tau` accelerates evidence accumulation but increases the normalized timing-search interval over the same physical `L`. Figure 2 will illustrate both covariance scales over the same physical uncertainty interval.

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

---

# 3. Results

## 3.1. Longer integration improves the guarantee margin

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

The signal term `rho_0 sqrt(eta(x))` increases strictly while the threshold does not increase, so `M_G` is strictly increasing in `x`. The fast/slow reversal below therefore does not arise from assigning either channel a self-suboptimal integration duration.

As `x->infinity`, the timing covariance becomes

```math
\boxed{
R_\infty(y)=(1+y)e^{-y},
\qquad y\ge0.
}
```

Define the corresponding full-template threshold

```math
\Gamma_\infty(\ell,\alpha)
=\inf\left\{u:
\Pr\left[\sup_{0\le q\le\ell}Z_\infty(q)>u\right]\le\alpha
\right\}.
```

Normalized-template `L2` convergence gives uniform covariance convergence on the full lag domain,

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

Because `R_infty(y)->0`, a Slepian comparison of widely separated samples with an equicorrelated Gaussian vector shows

```math
\Gamma_\infty(\ell,\alpha)\to\infty
\qquad(\ell\to\infty).
```

Thus a finite search-feasibility boundary exists whenever the requested known-time operating point is feasible.

## 3.2. Feasibility partition and crossover theorem

Let

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

The exact sufficient-guarantee-time preference boundary is therefore

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

Since `Gamma_infty` is nondecreasing with search length, only three feasibility regimes exist:

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

At known arrival (`L=0`) the channels share the same dimensionless first crossing `x_0`, hence

```math
T_{G,f}(0)=\tau_fx_0<\tau_sx_0=T_{G,s}(0).
```

The fast physical feasibility boundary occurs first,

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

This proves crossover existence, not uniqueness. It also concerns the sufficient guarantee time `T_G`; it does not establish the ordering of the exact first integration times solving `P_D^scan=beta`.

## 3.3. Continuous-time quantitative feasibility witness

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

At known arrival, the scalar guarantee equation gives

```math
\boxed{x_0=1.80519795247,}
```

so the fast channel is exactly preferred.

Now take one common physical uncertainty

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

For the slow channel, `R_infty''(0)=-1`, so Rice's exact mean upcrossing formula [16] gives

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

Figure 3 will present these as one-sided bounds, not as exact false-alarm probabilities. This witness is continuous-time and does not use a timing-grid extrapolation or a numerical estimate of `L_x`.

---

# 4. Discussion

The result is a failure of **detector-only ordering**, not a failure of detector characterization. A conventional detector specification describes a device under stated conditions. The quantity `T_G` belongs jointly to a detector and a task because the decision threshold depends on the physical arrival-time uncertainty interval, the global false-alarm requirement, and the requested detection guarantee.

The mechanism also differs from a generic sensitivity-bandwidth product. Sensitivity-speed combinations are established detector metrics [2,3], but the present decision surface contains the external task variable `L/tau` together with `rho_0`, `alpha`, and `beta`. Compressing these into one detector-only scalar would erase the nuisance-domain dependence responsible for the crossover.

The result should also be read against classical acquisition theory rather than in competition with it. Unknown-delay search penalties, matched-filter acquisition, false alarms, dwell time, and uncertainty-region size are established [6–14]. The specific construction here couples that established acquisition geometry to a detector parameter while holding eventual event-specific matched-filter SNR equal. The contribution is therefore the detector-facing synthesis and explicit ordering theorem, not the individual ingredients.

The equal-`rho_0` condition is deliberately event-specific. It is not equivalent to equal conventional `D*`, and the theorem does not require the channels to have equal `D*`. The normalization simply removes eventual matched-filter sensitivity advantage for the selected optical event so that the temporal mechanism can be isolated.

Several limitations are explicit. The channels are linear and time-scaled; output noise is additive, stationary, white, and Gaussian; arrival time is the only nuisance parameter; the transfer family is an existence construction; and the receiver is batch. Most importantly, the theorem uses

```math
P_D^{scan}\ge P_{D,true}
```

to define a sufficient guarantee. It does **not** prove that the exact full signal-present scan detection times reverse ordering. It also does not prove crossover uniqueness.

These limitations suggest direct extensions rather than weaknesses to hide. Colored detector noise can be included through whitening and a modified timing covariance; unequal eventual sensitivity introduces an additional task axis; and exact signal-present scan power would replace the sufficient true-alignment condition with the full composite-alternative probability. Those questions are outside the present result.

For transient detector qualification, the practical implication is modest but important: **response time should be interpreted together with the timing uncertainty and decision protocol, not only as a detector-isolated speed number.** A faster channel can accumulate evidence sooner yet still require a less favorable global threshold because it resolves more timing structure over the same physical uncertainty interval.

---

# 5. Conclusion

A controlled causal photodetector family with equal event-specific eventual matched-filter SNR shows that detector response time can enter an unknown-arrival measurement in two opposing ways. Shorter `tau` accelerates evidence accumulation but increases the normalized search interval `L/tau`. Under a global-false-alarm batch protocol, the sufficient guarantee time is `T_G=tau X_G(rho_0,alpha,beta,L/tau)`, producing at least one finite fast-to-slow ordering crossover. A continuous-time Rice/Slepian witness places the slow and fast channels on opposite sides of the same finite-`L` feasibility boundary. Exact full-scan detection-time ordering remains an open problem.

---

## Funding

[Funding statement to be confirmed before submission.]

## Disclosures

[Author disclosure statement to be confirmed before submission.]

## Data availability

The analytical derivations and reproduction scripts supporting the reported continuum feasibility witness are available in the public research repository `https://github.com/Kajin-0/gedanken_3`, under `experiments/01-equal-dstar-different-speed/`.

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