# Scalable internal-dark-count limits in a coherence-selective photodetector

**Target:** Physical Review A — Regular Article  
**Suggested section:** A-3E Quantum Technologies  
**Draft status:** Rev. 4 / journal-facing scientific architecture  
**Date:** 2026-08-14  
**Novelty status:** not established; no priority language authorized

## Abstract

Coherently interacting detector elements and bright/dark internal manifolds are established tools of quantum photodetection. We study a narrower scalability problem: how imperfect dark-to-bright isolation affects internally generated dark counts when the detector size grows. A photon prepares one collective bright excitation across `N` local states, while independent internal events are generated locally at a fixed rate per site. Bright extraction and local dephasing scale as `kappa_N=kappa_0 N^alpha` and `gamma_N=gamma_0 N^beta`. The measurement gate is chosen as the minimum time required to reach a prescribed conditional internal collection efficiency. We derive the accepted local-dark burden and, assuming bounded counted coupling per microscopic state, obtain the scalable-efficiency ceiling

```math
\eta_{sc}=
\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

Any operating point strictly requiring slow dark-manifold recycling then incurs at least an `O(N)` accepted local-dark burden. A thermally reversed counted transition adds a branch-dependent gated floor. The result quantifies one failure mode of dark-state isolation in an established coherence-selective detector architecture.

---

# I. Introduction

Quantum photodetection is not restricted to an irreversible sequence of photon absorption followed by classical amplification. Fully quantum detector models show that coherence, internal-state structure, and amplification backaction can determine efficiency, dark counts, timing jitter, and optimal detector design [1]. Building on this viewpoint, Young, Sarovar, and Leonard proposed photon-number-resolving detectors composed of nanoscale elements that interact collectively with the incident field [2]. Their design conditions for ideal efficiency include a particularly relevant requirement: relaxation must not return population from dark internal states to the optically active manifold.

The present work asks what happens when that condition fails.

We deliberately do not introduce a new collective detector architecture. Instead, we use a minimal Gedanken model to quantify the scaling penalty produced by local dark-to-bright recycling. One absorbed photon prepares a coherent bright excitation distributed over `N` local states. Internally generated dark events originate independently and locally. A counted channel extracts only the bright sector, while local dephasing transfers excitation between the bright state and a large dark manifold.

The individual ingredients are established. Collective bright and dark states and dephasing-induced transfer are standard in open quantum optics [3]. Dark-state protection and coherence-assisted extraction have been studied in photocell theory [4,5]. Collective electronic polarization has been coupled directly to electronic extraction in a quantum infrared detector [6]. Large-`N` scaling regimes controlled by collective dynamics and local decoherence are also an active subject, including recent analytical work on Dicke superradiance [7]. We therefore do not claim novelty for coherent collective photodetection, dark-state physics, or collective/decoherence scaling in general.

Our detector question is operationally different. For each `N`, we choose the **minimum gate duration that reaches a prescribed conditional internal collection efficiency** and then count the internal dark events accepted during that gate. The raw number of local dark-generation sites grows as `N`; the useful extraction and dephasing rates are allowed to scale with `N` as

```math
\kappa_N=\kappa_0 N^\alpha,
\qquad
\gamma_N=\gamma_0 N^\beta.
```

This produces a simple separation between branch selection and physical clock rate. The sign of `alpha-beta` determines whether the required efficiency is reached on the fast bright branch or only after slow dark-manifold recycling. The absolute extraction exponent `alpha` then determines how long the gate remains open and therefore how much extensive internal generation is admitted.

The full asymptotic classification is useful, but the most compact detector consequence appears after imposing a microscopic resource constraint. For a linear single-excitation extractor whose counted coupling per local state remains bounded, the collective extraction rate can scale at most linearly with `N`, so `alpha<=1`. If useful extraction also does not weaken with size, `0<=alpha<=1`, the supremum fixed efficiency compatible with a bounded accepted local-dark burden is

```math
\boxed{
\eta_{sc}=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

Any operating point that lies strictly on the slow-recycling side then incurs at least an `O(N)` accepted local-dark burden.

Figure 1 summarizes the two clocks underlying this result. The fast counted path competes with local dephasing, while population transferred to the dark manifold returns only through a slow mode whose rate is suppressed by `1/N`.

The theorem concerns internally generated local dark events. A background photon entering through the accepted optical mode prepares the same bright state as the signal and is not rejected. The model also separates internal collection from optical absorption: the efficiency below is conditional on the photon having already prepared the bright excitation.

---

# II. Coherence-selective detector model

## A. Bright signal and local internal event

Let

```math
|j\rangle,
\qquad j=1,\ldots,N,
```

be orthonormal local single-excitation states. We take the photon-created signal state to be the symmetric bright superposition

```math
\boxed{
|B\rangle=\frac{1}{\sqrt N}\sum_{j=1}^{N}|j\rangle.
}
```

An internally generated event is localized at one site. If all sites are equally likely, the one-event ensemble is

```math
\rho_D=\frac1N\sum_{j=1}^{N}|j\rangle\langle j|.
```

The ideal bright projector `|B><B|` accepts the photon-created state with probability one but a uniformly local event with probability `1/N`. We use this familiar coherent-mode selection only to define the selected detector direction; the static `1/N` projection is not the principal result.

More generally, if internal-generation channels define a positive covariance matrix `D` and the optical coupling vector is `g`, direct dark injection into the counted direction is

```math
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
```

Thus correlated internal processes aligned with the optical bright vector can eliminate the state-space rejection. The scaling theorem below treats independent local generation.

## B. Extraction and local dephasing

A counted sink extracts the bright state at rate `kappa_N`. Independent local pure dephasing acts at rate `gamma_N`. Within the surviving one-excitation manifold define

```math
P(t)=\operatorname{Tr}\rho(t),
```

and

```math
b(t)=\langle B|\rho(t)|B\rangle.
```

Permutation symmetry closes the dynamics exactly:

```math
\boxed{\dot P=-\kappa_N b,}
```

```math
\boxed{
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P.
}
```

Eliminating `b` gives

```math
\boxed{
\ddot P
+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
}
```

Let

```math
a_N=\kappa_N+\gamma_N,
```

```math
\Delta_N=\sqrt{a_N^2-4\kappa_N\gamma_N/N},
```

and

```math
r_{\pm,N}=\frac{a_N\pm\Delta_N}{2}.
```

For an initial excitation with bright population `b_0`, `P(0)=1` and `\dot P(0)=-\kappa_Nb_0`, so

```math
\boxed{
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa_Nb_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa_Nb_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
}
```

The cumulative collection probability is

```math
C_{b_0,N}(t)=1-P_{b_0,N}(t).
```

For the photon-created bright state, `b_0=1`; for a uniformly local event, `b_0=1/N`. We write these kernels as `C_{S,N}` and `C_{D,N}`.

For every nonzero dephasing rate,

```math
C_{S,N}(\infty)=C_{D,N}(\infty)=1.
```

Thus coherence selectivity is a finite-time resource in this model. The slow eigenvalue is

```math
\boxed{
r_{-,N}
=\frac1N
\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
}
```

The `1/N` factor is the origin of the slow dark-manifold recycling clock.

---

# III. Fixed-efficiency counting task

The one-excitation master equation defines the exact collection kernel for one generated excitation. It does not, by itself, define an arbitrary finite-density many-particle detector. We therefore state the counting model separately.

Each of the `N` microscopic sites generates distinguishable, noninteracting internal dark excitations as an independent Poisson process of fixed rate `d`. Each generated excitation follows an independent copy of the one-body kernel above. This is an extensive low-density kinetic limit: saturation, Pauli blocking, heating, particle-particle interactions, and shared reset dynamics are neglected.

The raw internal generation rate is

```math
\Gamma_{raw}=Nd.
```

For a gate `[0,T]`, independent Poisson marking gives the accepted local-dark mean

```math
\boxed{
\mu_{\mathrm{loc},N}(T)
=Nd\int_0^T C_{D,N}(u)\,du.
}
```

A photon that has already prepared `|B>` is collected with conditional internal efficiency

```math
\eta_{\mathrm{int},N}(T)=C_{S,N}(T).
```

We fix a target

```math
0<\eta<1
```

and choose the shortest gate that reaches it:

```math
\boxed{
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\}.
}
```

The corresponding local-dark burden is

```math
\boxed{
\mu_{\mathrm{loc},N}(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)\,du.
}
```

This definition couples detector dynamics to an explicit operating point. An arbitrary fixed gate can hide whether a detector is actually collecting the required fraction of the signal.

---

# IV. Size-dependent scaling laws

We allow

```math
\boxed{
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta.
}
```

The fast branching fraction is

```math
q_N=\frac{\kappa_N}{\kappa_N+\gamma_N}
=\frac{1}{1+(\gamma_0/\kappa_0)N^{\beta-\alpha}}.
```

Therefore

```math
q_N\to
\begin{cases}
1,&\alpha>\beta,\\
q_0=\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

The asymptotic gate and accepted local-dark mean are summarized in Table I:

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \mu_{\mathrm{loc},N}\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}.
\end{array}}
```

Appendix B gives the coefficients. Here we emphasize the physical content.

### Extraction-dominated sector: `alpha>beta`

The fast branching fraction approaches one, so every fixed `eta<1` is eventually reached before slow recycling is required. Writing

```math
x_\eta=-\ln(1-\eta),
```

we obtain

```math
T_N
\sim\frac{x_\eta}{\kappa_0}N^{-\alpha},
```

and

```math
\mu_{\mathrm{loc},N}
\sim\frac{d}{\kappa_0}(x_\eta-\eta)N^{-\alpha}.
```

Thus collective growth of the useful rate can offset both the increasing number of local sources and the fast-branch collection kernel.

### Dephasing-dominated sector: `alpha<beta`

Here `q_N->0`. Every fixed positive efficiency requires the slow recycling mode. The same `x_eta` gives

```math
T_N
\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha},
```

and

```math
\mu_{\mathrm{loc},N}
\sim\frac{d}{\kappa_0}(x_\eta-\eta)N^{2-\alpha}.
```

The additional factor of `N` in the gate combines with the extensive raw generation rate to generate the severe dark-count scaling.

### Balanced sector: `alpha=beta=s`

Now the fast branching fraction remains finite,

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0}.
```

For `eta<q_0`, the gate remains on the fast branch and both `T_N` and `mu_loc,N` scale as `N^{-s}`. For `eta>q_0`, the detector must wait for slow recycling, producing `T_N~N^{1-s}` and `mu_loc,N~N^{2-s}`. Exactly at `eta=q_0`, the two clocks balance and the leading scaling is

```math
T_N=\Theta(N^{-s}\ln N),
```

```math
\mu_{\mathrm{loc},N}
=\Theta[N^{-s}(\ln N)^2].
```

Figure 2 compares these asymptotic exponents with exact finite-`N` evaluation of the collection kernels. The numerical curves approach the predicted slopes without introducing an independent effective-trial or continuum approximation.

---

# V. Bounded microscopic coupling and scalable efficiency

The formal power-law model allows arbitrary positive `alpha`. A linear single-excitation extractor with a fixed microscopic coupling budget cannot realize arbitrary collective enhancement.

Let arbitrary counted sink channels define the positive extraction matrix

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|.
```

For normalized excitation `|\psi\rangle`, the instantaneous counted extraction rate is

```math
\kappa(\psi)=\langle\psi|K|\psi\rangle.
```

Assume each local state has an `N`-independent total counted-coupling budget,

```math
K_{jj}\le\kappa_{\mathrm{loc}}.
```

Then

```math
\boxed{
\kappa(\psi)
\le\lambda_{\max}(K)
\le\operatorname{Tr}K
\le N\kappa_{\mathrm{loc}}.
}
```

Thus

```math
\boxed{\alpha\le1.}
```

within this resource class. Linear collective enhancement is attainable when local extraction amplitudes add coherently into one sink, so the bound does not exclude ordinary collective rate enhancement.

Assume also that useful extraction does not weaken with size,

```math
0\le\alpha\le1.
```

Define the **scalable internal-efficiency ceiling**

```math
\eta_{\mathrm{sc}}
=\sup\{\eta\in(0,1):
\mu_{\mathrm{loc},N}(\eta)=O(1)\}.
```

The scaling laws immediately give the main theorem:

```math
\boxed{
\eta_{\mathrm{sc}}
=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

If extraction scales faster than dephasing, every fixed efficiency below unity eventually remains on the fast branch and has bounded local-dark burden. If the two rates scale together, the ceiling is the finite fast branching fraction. If dephasing scales faster, no fixed positive efficiency has bounded accepted local-dark burden.

A useful no-go form follows immediately:

```math
\boxed{
\text{strict slow-recycling operation}
\quad\Longrightarrow\quad
\mu_{\mathrm{loc},N}=\Omega(N)
}
```

under bounded per-site counted coupling. The formal possibility of compensating the slow branch with `\kappa_N\sim N^2` or faster is unavailable unless the microscopic coupling budget itself grows with `N` or the model leaves the linear single-excitation class.

Figure 3 shows the ceiling as a function of the rate-scaling imbalance `alpha-beta`.

---

# VI. Reversible extraction as a gated dark-count floor

The local-generation theorem does not imply a free asymptotic detector. The counted transition itself may be thermally reversible.

Assume an effective local-detailed-balance relation

```math
\bar\kappa_N
=\kappa_N e^{-\Delta F_N/(kT)},
```

where `\bar\kappa_N` is the reverse bright-injection rate. A reverse injection creates a bright excitation; under the same independent-event approximation its accepted contribution during the efficiency-selected gate is

```math
\boxed{
\mu_{\mathrm{rev},N}
=\bar\kappa_N
\int_0^{T_N(\eta)}C_{S,N}(u)\,du.
}
```

At fixed effective affinity, the gate dependence produces

```math
\boxed{
\mu_{\mathrm{rev},N}
\sim
\begin{cases}
O(1),&\text{fast branch},\\
O(\ln N),&\text{balanced boundary},\\
O(N),&\text{strict slow branch}.
\end{cases}}
```

This corrects a tempting but incomplete rate-only argument: a collectively enhanced forward rate does not by itself imply a proportionally enhanced **gated** reverse count burden, because the same enhancement shortens the measurement gate. On a fast branch these two effects cancel at leading order.

Keeping the gated reverse contribution bounded therefore requires only an `O(1)` affinity on a fast branch, an additional `kT\ln\ln N` at the balanced boundary, and `kT\ln N` on a strict slow branch, up to additive constants.

For the favorable limiting case

```math
\kappa_N\propto N,
\qquad
\gamma_N=O(1),
```

we obtain

```math
\mu_{\mathrm{loc},N}\sim N^{-1},
```

while

```math
\mu_{\mathrm{rev},N}=O(1)
```

at fixed affinity. The reversible counted transition then sets an asymptotic floor even though its gated contribution does not diverge.

The thermodynamic relation is used here only as a supporting detector constraint. General quantum-detector thermodynamic tradeoffs are already an established subject [8].

---

# VII. Discussion

## A. Relation to established coherent detector designs

The closest detector precedent is Ref. [2]. Young, Sarovar, and Leonard already formulate coherent collective detector elements and show that returning population from dark states to the optically active manifold conflicts with their ideal-efficiency conditions. The present paper should therefore be read as a quantitative failure/scalability theory for that isolation condition, not as an independent architecture proposal.

Our additional ingredients are an extensive internal local-generation process and an efficiency-selected measurement gate. Together they turn dark-to-bright recycling into an accepted-count scaling problem. The main theorem states how much conditional internal signal efficiency can remain compatible with bounded local-dark burden as the number of microscopic generation sites grows.

## B. Relation to collective/decoherence scaling theory

The sign of `alpha-beta` resembles the collective-versus-local competition that appears throughout Dicke and superradiance theory. Recent work explicitly derives large-system scaling regimes and transient boundaries under local decoherence [7]. We do not claim that structure as new.

The detector-specific observable is the time-integrated accepted internal generation accumulated while waiting for a required signal collection. This is why the same dynamical rate sector translates into a detector efficiency ceiling and a minimum `O(N)` penalty on strict slow-recycling operation under bounded microscopic coupling.

## C. What the model does not suppress

Same-mode background photons are not rejected. A background photon in the accepted optical mode prepares the same bright state as the signal. Likewise, a correlated internal bath whose generation covariance is aligned with the bright vector can directly populate the counted sector.

The theorem therefore concerns independent or sufficiently misaligned **internal local generation**, not arbitrary detector noise.

## D. Independent-particle limit

The Poisson lift is an explicit model assumption. It should be interpreted as an extensive low-density kinetic limit in which generated excitations do not interact or saturate the extractor. A true many-excitation collective detector can introduce Pauli blocking, heating, collective saturation, or reset correlations that alter the count statistics and possibly the `N` scaling.

## E. Realization versus theorem

No material system is assigned to `|j\rangle`, `\kappa_N`, or `\gamma_N`. The exponent pair `(alpha,beta)` must ultimately be derived from a microscopic detector architecture. The present result says what follows once those rate scalings and the bounded local-coupling resource are specified.

This abstraction limits direct engineering claims but is useful for separating general detector logic from platform-specific details.

---

# VIII. Conclusion

We considered a coherence-selective photodetector in which a photon creates one collective bright excitation while internally generated dark events originate locally across `N` microscopic sites. Local dephasing violates perfect dark-to-bright isolation, and the measurement gate is chosen as the minimum time needed to collect a prescribed fraction of the signal excitation.

Allowing the useful extraction and dephasing rates to scale as `N^alpha` and `N^beta` yields a compact detector classification. Under bounded counted coupling per microscopic state, the collective extraction exponent satisfies `alpha<=1`. If extraction scaling outruns dephasing, any fixed internal efficiency below unity can retain bounded accepted local-dark burden. If the rates scale together, the scalable efficiency is limited by the fast branching fraction `kappa_0/(kappa_0+gamma_0)`. If dephasing scaling outruns extraction, no fixed positive efficiency remains scalable. Any strict slow-recycling operating point incurs at least an `O(N)` local-dark burden. A thermally reversed counted transition adds a branch-dependent floor rather than a universal penalty proportional to the collective forward rate.

The result quantifies one detector-level consequence of imperfect dark-state isolation within an established coherent collective architecture. Its applicability to a specific device requires a microscopic realization of the assumed coherent manifold, rate scalings, and low-density counting limit.

---

# Figure captions

**FIG. 1.** Minimal coherence-selective detector and its two dynamical clocks. A photon prepares the collective bright state, while internal events are generated locally. Bright extraction at rate `kappa_N` feeds the counted sink. Local dephasing at rate `gamma_N` transfers excitation into the dark manifold; recovery occurs through the slow mode `r_- ~ [kappa_N gamma_N/(kappa_N+gamma_N)]/N`. The gate closes at the minimum time `T_N` satisfying `C_{S,N}(T_N)=eta`.

**FIG. 2.** Exact finite-`N` accepted local-dark mean versus `N` for representative rate sectors, evaluated from the exact one-event kernels and the independent-particle count lift. Dashed guides show the asymptotic slopes predicted by Table I. Illustrated parameter values are dimensionless and chosen only to expose the scaling classes.

**FIG. 3.** Scalable internal-efficiency ceiling under bounded counted coupling per microscopic state. If extraction scales faster than dephasing (`alpha>beta`), every fixed `eta<1` can remain locally scalable. If the rates scale together, the ceiling is `q_0=kappa_0/(kappa_0+gamma_0)`. If dephasing scales faster, no nonzero fixed efficiency has bounded accepted local-dark burden.

---

# Appendix A: Exact finite-N solution

For completeness, define

```math
a_N=\kappa_N+\gamma_N,
```

```math
\Delta_N=\sqrt{a_N^2-4\kappa_N\gamma_N/N},
```

```math
r_{\pm,N}=(a_N\pm\Delta_N)/2.
```

For initial bright population `b_0`,

```math
P_{b_0,N}(t)
=A_{b_0,N}e^{-r_{-,N}t}
+B_{b_0,N}e^{-r_{+,N}t},
```

where

```math
A_{b_0,N}=\frac{r_{+,N}-\kappa_Nb_0}{\Delta_N},
```

```math
B_{b_0,N}=\frac{\kappa_Nb_0-r_{-,N}}{\Delta_N}.
```

The cumulative collection probability is `C=1-P`. The photon and uniformly local kernels use `b_0=1` and `b_0=1/N`, respectively.

The exact signal-local separation is

```math
C_{S,N}(t)-C_{D,N}(t)
=
\frac{\kappa_N(1-1/N)}{\Delta_N}
\left(e^{-r_{-,N}t}-e^{-r_{+,N}t}\right),
```

which is positive for every finite `t>0` and `N>1` but vanishes as `t->infinity` when `gamma_N>0`.

---

# Appendix B: Asymptotic coefficients

## 1. Extraction-dominated sector

For `alpha>beta`, let

```math
x_\eta=-\ln(1-\eta).
```

Then

```math
T_N
\sim\frac{x_\eta}{\kappa_0}N^{-\alpha},
```

```math
\mu_{\mathrm{loc},N}
\sim
\frac{d}{\kappa_0}(x_\eta-\eta)N^{-\alpha}.
```

## 2. Dephasing-dominated sector

For `alpha<beta`,

```math
T_N
\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha},
```

```math
\mu_{\mathrm{loc},N}
\sim
\frac{d}{\kappa_0}(x_\eta-\eta)N^{2-\alpha}.
```

## 3. Balanced sector

Let

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0},
```

```math
A=\kappa_0+\gamma_0,
```

```math
\lambda_0=\frac{\kappa_0\gamma_0}{A}.
```

For `eta<q_0`, set

```math
x_\eta=-\ln(1-\eta/q_0).
```

Then

```math
T_N\sim\frac{x_\eta}{A}N^{-s},
```

```math
\mu_{\mathrm{loc},N}
\sim\frac{d}{A}
\left[
\frac{q_0(1-q_0)}2x_\eta^2
+q_0^2x_\eta-q_0\eta
\right]N^{-s}.
```

For `eta>q_0`, define

```math
L_\eta=\ln\frac{1-q_0}{1-\eta},
```

```math
H_\eta=L_\eta-\frac{\eta-q_0}{1-q_0}.
```

Then

```math
T_N\sim\frac{L_\eta}{\lambda_0}N^{1-s},
```

```math
\mu_{\mathrm{loc},N}
\sim\frac{dH_\eta}{\lambda_0}N^{2-s}.
```

At `eta=q_0`, the robust boundary statements are

```math
T_N=\Theta(N^{-s}\ln N),
```

```math
\mu_{\mathrm{loc},N}
=\Theta[N^{-s}(\ln N)^2].
```

A leading boundary-layer estimate is

```math
A N^sT_N
\sim W\left(\frac{N}{(1-q_0)^2}\right),
```

but we do not use this as a precision finite-`N` formula.

---

# Appendix C: Bounded-local-coupling proof

Let the counted extraction channels be represented by excitation-space vectors `|\ell_a\rangle`, so

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0.
```

For any normalized excitation `|\psi\rangle`,

```math
\kappa(\psi)=\langle\psi|K|\psi\rangle
\le\lambda_{\max}(K).
```

For a positive semidefinite matrix,

```math
\lambda_{\max}(K)\le\operatorname{Tr}K.
```

If

```math
K_{jj}\le\kappa_{\mathrm{loc}}
```

for each local state, then

```math
\operatorname{Tr}K
=\sum_jK_{jj}
\le N\kappa_{\mathrm{loc}}.
```

Therefore

```math
\kappa(\psi)\le N\kappa_{\mathrm{loc}},
```

which implies `alpha<=1` for any power-law collective extraction rate within this resource class.

---

# Appendix D: Gated reverse-injection scaling

Assume

```math
\bar\kappa_N
=\kappa_Ne^{-\Delta F_N/(kT)}.
```

The accepted reverse contribution is

```math
\mu_{\mathrm{rev},N}
=\bar\kappa_N
\int_0^{T_N(\eta)}C_{S,N}(u)du.
```

On an extraction-dominated fast branch, with `x_eta=-ln(1-eta)`,

```math
\int_0^{T_N}C_{S,N}(u)du
\sim\frac{x_\eta-\eta}{\kappa_N},
```

so

```math
\mu_{\mathrm{rev},N}
\sim e^{-\Delta F_N/(kT)}(x_\eta-\eta).
```

On the balanced fast branch the corresponding expression is also `O(1)` at fixed affinity. At the balanced boundary the integral yields an additional logarithmic factor, while on a strict slow branch it scales as `N/\kappa_N`, giving an `O(N)` reverse burden at fixed affinity.

---

# Working references

[1] S. M. Young, M. Sarovar, and F. Leonard, “Fundamental limits to single-photon detection determined by quantum coherence and backaction,” *Phys. Rev. A* **97**, 033836 (2018), DOI `10.1103/PhysRevA.97.033836`.

[2] S. M. Young, M. Sarovar, and F. Leonard, “Design of high-performance photon-number-resolving photodetectors based on coherently interacting nanoscale elements,” *ACS Photonics* **7**, 821–830 (2020), DOI `10.1021/acsphotonics.9b01754`.

[3] N. Shammah, N. Lambert, F. Nori, and S. De Liberato, “Superradiance with local phase-breaking effects,” *Phys. Rev. A* **96**, 023863 (2017), DOI `10.1103/PhysRevA.96.023863`.

[4] C. Creatore, M. A. Parker, S. Emmott, and A. W. Chin, “Efficient biologically inspired photocell enhanced by delocalized quantum states,” *Phys. Rev. Lett.* **111**, 253601 (2013), DOI `10.1103/PhysRevLett.111.253601`.

[5] A. Fruchtman, R. Gomez-Bombarelli, B. W. Lovett, and E. M. Gauger, “Photocell optimization using dark state protection,” *Phys. Rev. Lett.* **117**, 203603 (2016), DOI `10.1103/PhysRevLett.117.203603`.

[6] F. Pisani et al., “Electronic transport driven by collective light-matter coupled states in a quantum device,” *Nat. Commun.* **14**, 3914 (2023), DOI `10.1038/s41467-023-39594-z`.

[7] N. S. Bassler, J. Lyne, and J. Cuerda, “Scaling theory of decoherence in Dicke superradiance,” arXiv:`2607.28034` (2026).

[8] E. Schwarzhans, T. J. G. Apollaro, I. Khomchenko, M. P. E. Lock, M. T. Mitchison, and M. Huber, “Quantum detectors as autonomous machines: Assessing the nonequilibrium thermodynamics of information acquisition,” *PRX Quantum* **7**, 033001 (2026), DOI `10.1103/wm5p-tjtg`.

---

# Rev. 4 production gate

Before rendering:

1. verify every reference against a primary publisher/preprint record;
2. generate the three figures from `numerics/paper_rev3_figures.py` and inspect them;
3. run a final regression search for obsolete Rev. 0/Rev. 1 claims (`photon detection efficiency`, universal `kT ln C`, novelty language, static `1/N` centerpiece);
4. then prepare PRA-style LaTeX and PDF for one final rendered-manuscript adversarial review.
