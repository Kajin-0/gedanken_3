# Experiment 09 — Efficiency-controlled dark-count scalability transition

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** MAIN MANUSCRIPT-LEVEL THEOREM / EXACT ONE-BODY DYNAMICS + EXACT INDEPENDENT-PARTICLE STOCHASTIC LIFT / NOVELTY NOT ESTABLISHED

## Why this note exists

The first gated formulation emphasized the exact `gamma=0` cancellation

```math
\mu_D(T)=O(1)
```

while raw local dark generation is `O(N)`. A hostile review exposed two issues:

1. the static/no-dephasing cancellation is mathematically close to ordinary coherent-mode projection and is probably too weak to carry the manuscript by itself;
2. a strict single-excitation Lindblad model cannot, by itself, justify an exact finite-rate Poisson count process when many generated excitations may overlap.

This note repairs both issues and derives a stronger result.

The one-excitation master equation is used only to calculate the exact **one-event collection kernels**. A separate, explicitly stated independent-particle stochastic lift then supplies the continuous stream of dark-generation events. Within that lift, Poisson thinning is exact because the events are noninteracting and each event carries its own independent copy of the one-body quantum dynamics.

The resulting detector has a sharp large-`N` scalability boundary controlled by the required internal collection efficiency.

---

# 1. One-body detector dynamics

Use the symmetric bright state

```math
|B\rangle=\frac{1}{\sqrt N}\sum_{j=1}^{N}|j\rangle.
```

A counted sink extracts only the bright state at rate `kappa`. Independent local pure dephasing acts at rate `gamma`.

Within the surviving one-excitation manifold define

```math
P(t)=\operatorname{Tr}\rho(t),
```

and

```math
b(t)=\langle B|\rho(t)|B\rangle.
```

Exactly,

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+\frac{\gamma}{N}P.
```

Thus

```math
\ddot P+(\kappa+\gamma)\dot P+\frac{\kappa\gamma}{N}P=0.
```

Write

```math
a=\kappa+\gamma,
```

```math
\Delta_N=\sqrt{a^2-\frac{4\kappa\gamma}{N}},
```

and

```math
r_{\pm,N}=\frac{a\pm\Delta_N}{2}.
```

For an initial excitation with bright population `b_0`,

```math
P_{b_0,N}(t)
=
\frac{r_{+,N}-\kappa b_0}{\Delta_N}e^{-r_{-,N}t}
+
\frac{\kappa b_0-r_{-,N}}{\Delta_N}e^{-r_{+,N}t}.
```

The cumulative collection probability is

```math
C_{b_0,N}(t)=1-P_{b_0,N}(t).
```

For a photon-created bright excitation,

```math
C_{S,N}(t)=C_{1,N}(t).
```

For a uniformly local dark event,

```math
C_{D,N}(t)=C_{1/N,N}(t).
```

Both functions are nondecreasing because the counted sink is absorbing.

---

# 2. Independent-particle stochastic lift

The following is an additional model assumption and must be stated explicitly in any manuscript.

Each internally generated dark event is treated as a distinguishable, noninteracting excitation carrying an independent copy of the one-body dynamics above. The creation times at each of the `N` local sites form independent Poisson processes of rate `d` per site.

Therefore the aggregate raw dark-generation process is Poisson with rate

```math
\Gamma_{raw}=Nd.
```

Conditional on age `u`, each created excitation produces a counted event before gate closure with probability `C_{D,N}(u)`. Independent marking/thinning of the Poisson process is then exact within this lifted model.

For a gate `[0,T]`, the accepted local dark counts are Poisson with mean

```math
\boxed{
\mu_N(T)
=Nd\int_0^T C_{D,N}(u)\,du.
}
```

The corresponding false-count probability is

```math
P_{FA,N}(T)=1-e^{-\mu_N(T)}.
```

A photon that has already created the material bright excitation at gate opening has **conditional internal collection efficiency**

```math
\boxed{
\eta_{int,N}(T)=C_{S,N}(T).
}
```

This is not end-to-end photon quantum efficiency. If optical absorption/preparation succeeds with probability `eta_abs`, then the end-to-end signal efficiency is `eta_abs C_{S,N}(T)` in this reduced factorized description.

---

# 3. Define the fixed-efficiency detector task

Fix a requested conditional internal collection efficiency

```math
0<\eta<1.
```

Define the minimal gate needed to reach that operating point:

```math
\boxed{
T_N(\eta)
=\inf\{t\ge0:C_{S,N}(t)\ge\eta\}.
}
```

Because `C_{S,N}` is monotone, this is the physically minimal gate for the specified internal efficiency.

Define the corresponding accepted local-dark mean

```math
\boxed{
\mu_N(\eta)
=Nd\int_0^{T_N(\eta)}C_{D,N}(u)\,du.
}
```

The question is now sharp:

> At fixed required internal signal efficiency, how does the minimum gate and its accepted local-dark burden scale with `N`?

---

# 4. The fast branching fraction

Define

```math
\boxed{
q=\frac{\kappa}{\kappa+\gamma}=\frac{\kappa}{a}.
}
```

For `gamma>0`, `0<q<1`.

Also define the slow large-`N` rate scale

```math
\boxed{
\lambda=\frac{\kappa\gamma}{\kappa+\gamma}
=q(1-q)a.
}
```

The physical interpretation of `q` is crucial. In the large-`N` limit, the initial bright excitation has a fast component of weight `q` that can be extracted before local dephasing transfers amplitude into the enormous dark manifold. The remaining fraction `1-q` resides in the slow sector and can only be recovered through `O(N)` leakage back toward the bright state.

This creates an efficiency threshold at

```math
\boxed{\eta_c=q.}
```

---

# 5. Large-N fixed-time limits

The exact rates obey

```math
r_{-,N}=\frac{\lambda}{N}+O(N^{-2}),
```

```math
r_{+,N}=a-\frac{\lambda}{N}+O(N^{-2}).
```

For every fixed physical time `t`, the signal kernel tends to

```math
\boxed{
C_{S,N}(t)
\longrightarrow
q\left(1-e^{-at}\right).
}
```

Thus no fixed gate can asymptotically collect more than fraction `q` of the initial bright excitation.

For a local dark excitation, the `1/N` initial bright overlap and dephasing-induced leakage are both retained at leading order by multiplying the collection probability by `N`:

```math
\boxed{
N C_{D,N}(t)
\longrightarrow
f_D(t),
}
```

where

```math
\boxed{
f_D(t)
=q(1-q)at+q^2\left(1-e^{-at}\right).
}
```

Equivalently,

```math
f_D(t)
=\frac{\kappa\gamma}{a}t
+\frac{\kappa^2}{a^2}\left(1-e^{-at}\right).
```

The first term is dephasing-enabled leakage into the counted direction; the second is the direct `1/N` bright overlap of the locally created excitation.

---

# 6. Regime I — subcritical efficiency, 0 < eta < q

For

```math
0<\eta<q,
```

the requested signal efficiency lies below the fast-branch ceiling. Therefore the minimal gate remains on the `O(1)` fast timescale.

Define

```math
\boxed{
x_\eta=-\ln\left(1-\frac{\eta}{q}\right).}
```

Then

```math
\boxed{
aT_N(\eta)\longrightarrow x_\eta,}
```

so

```math
T_N(\eta)=O(1).
```

Using the fixed-time dark-kernel limit,

```math
\mu_N(\eta)
=Nd\int_0^{T_N}C_{D,N}(u)du
\longrightarrow
d\int_0^{x_\eta/a}f_D(u)du.
```

The integral is

```math
\boxed{
\mu_{<}(\eta)
=\frac{d}{a}
\left[
\frac{q(1-q)}{2}x_\eta^2
+q^2x_\eta
-q\eta
\right].
}
```

Therefore

```math
\boxed{
0<\eta<q:
\qquad
T_N=O(1),
\qquad
\mu_N=O(1).
}
```

The raw internal dark-generation rate still grows as `Nd`; only the accepted count burden at the fixed-efficiency operating point is nonextensive.

### No-dephasing corollary

When `gamma=0`,

```math
q=1,
\qquad a=\kappa.
```

Every fixed target `0<eta<1` is subcritical, and

```math
x_\eta=-\ln(1-\eta).
```

The limiting dark burden becomes

```math
\boxed{
\mu_N(\eta)
=\frac{d}{\kappa}
\left[-\ln(1-\eta)-\eta\right],
\qquad\gamma=0,
}
```

which is exactly the earlier `N`-cancellation result expressed at fixed signal efficiency rather than fixed gate duration.

Thus the old theorem is now a corollary of the subcritical branch, not the main paper result.

---

# 7. Regime II — supercritical efficiency, q < eta < 1

For

```math
q<\eta<1,
```

the fast branch cannot meet the requested efficiency. The detector must wait for population that dephased into the dark manifold to leak back into the counted bright direction.

Use the slow timescale

```math
t=Ny.
```

For fixed `y>0`, the exact kernels have limits

```math
\boxed{
C_{S,N}(Ny)
\longrightarrow
1-(1-q)e^{-\lambda y},
}
```

and

```math
\boxed{
C_{D,N}(Ny)
\longrightarrow
1-e^{-\lambda y}.
}
```

The efficiency equation gives

```math
1-(1-q)e^{-\lambda y_\eta}=\eta,
```

hence

```math
\boxed{
y_\eta
=\frac{1}{\lambda}
\ln\left(\frac{1-q}{1-\eta}\right).}
```

Therefore

```math
\boxed{
\frac{T_N(\eta)}{N}
\longrightarrow y_\eta,}
```

so

```math
T_N(\eta)=O(N).
```

The dark count mean now accumulates over an `O(N)` gate while the raw dark-generation rate is itself `O(N)`. Consequently it becomes quadratic.

Indeed,

```math
\frac{\mu_N(\eta)}{N^2}
\longrightarrow
d\int_0^{y_\eta}\left(1-e^{-\lambda y}\right)dy,
```

which gives

```math
\boxed{
\frac{\mu_N(\eta)}{N^2}
\longrightarrow
\frac{d}{\lambda}
\left[
\ln\left(\frac{1-q}{1-\eta}\right)
-
\frac{\eta-q}{1-q}
\right].
}
```

Therefore

```math
\boxed{
q<\eta<1:
\qquad
T_N=O(N),
\qquad
\mu_N=O(N^2).
}
```

This is not merely a gradual loss of the `1/N` projection advantage. The efficiency requirement changes the asymptotic class of the detector task.

---

# 8. Regime III — critical efficiency, eta = q

At exactly

```math
\eta=q,
```

the fast component approaches the target only asymptotically, while waiting all the way onto the `O(N)` slow timescale is unnecessary. The gate lives in a boundary layer between the two scales.

Using the leading composite form

```math
P_{S,N}(t)
\simeq
(1-q)e^{-\lambda t/N}+qe^{-at},
```

and setting `C_S=q`, equivalently `P_S=1-q`, gives for `t=o(N)`

```math
qe^{-at}
\simeq
(1-q)\frac{\lambda t}{N}.
```

Since

```math
\lambda=q(1-q)a,
```

this reduces to

```math
e^{-at}
\simeq
\frac{(1-q)^2at}{N}.
```

Let `x=at`. Then

```math
xe^x
\simeq
\frac{N}{(1-q)^2},
```

so

```math
\boxed{
aT_N(q)
\sim
W\left(\frac{N}{(1-q)^2}\right),}
```

where `W` is the Lambert-W function.

Hence

```math
\boxed{
T_N(q)=\Theta(\ln N).}
```

On this logarithmic gate scale, the fixed-time expression for `N C_D` remains asymptotically valid at leading order. Integrating it gives

```math
\mu_N(q)
\sim
\frac{d}{a}
\left[
\frac{q(1-q)}{2}x_N^2
+q^2x_N
-q^2
\right],
```

with

```math
x_N=W\left(\frac{N}{(1-q)^2}\right),
```

up to lower-order corrections.

Therefore the robust scaling statement is

```math
\boxed{
\eta=q:
\qquad
T_N=\Theta(\ln N),
\qquad
\mu_N=\Theta((\ln N)^2).
}
```

The critical law is parametrically distinct from both neighboring phases.

---

# 9. Main scalability theorem

For fixed `kappa>0`, `gamma>0`, per-site dark-generation rate `d>0`, and fixed required conditional internal signal efficiency `0<eta<1`, define

```math
q=\frac{\kappa}{\kappa+\gamma}.
```

Within the symmetric one-body Lindblad model plus the explicit independent-particle Poisson lift, the minimal gate and accepted local-dark mean satisfy the large-`N` partition

```math
\boxed{
\begin{array}{c|c|c}
\text{efficiency regime} & T_N(\eta) & \mu_N(\eta)\\
\hline
0<\eta<q & O(1) & O(1)\\
\eta=q & \Theta(\ln N) & \Theta((\ln N)^2)\\
q<\eta<1 & O(N) & O(N^2)
\end{array}
}
```

with explicit coefficients given in Sections 6–8.

This is the strongest current detector-level result of Experiment 09.

---

# 10. Physical interpretation

The transition follows from two separate clocks.

### Fast clock

The bright excitation is acted on simultaneously by extraction and local dephasing. The fraction that can be collected before dephasing transfers it into the large dark manifold is

```math
q=\frac{\kappa}{\kappa+\gamma}.
```

If the requested conditional efficiency is below `q`, the detector can close its gate while the event still lives almost entirely on the fast bright clock. The gate does not grow with system size, and the accepted internal dark burden stays `O(1)`.

### Slow clock

If the requested efficiency exceeds `q`, the detector must recover some of the signal population that entered the dark manifold. The return rate is

```math
r_-\sim\frac{\lambda}{N},
```

so the required gate grows as `N`. During that gate, there are `O(N)` local dark-generation events per unit time for `O(N)` time, giving `O(N^2)` accepted dark burden after the slow channel becomes active.

At the exact boundary, the vanishing fast tail balances the incipient slow leakage and produces the logarithmic Lambert-W scaling.

The scalability condition is therefore not merely `kappa >> gamma`. It is task dependent:

```math
\boxed{
\eta<\frac{\kappa}{\kappa+\gamma}
}
```

is the asymptotic condition for bounded gate time and bounded accepted local-dark burden at fixed `kappa`, `gamma`, and `d`.

Equivalently, to sustain a specified internal efficiency `eta` in the scalable branch,

```math
\boxed{
\frac{\kappa}{\gamma}
>
\frac{\eta}{1-\eta}.
}
```

For example, an internal collection target `eta=0.99` requires `kappa/gamma>99` to remain strictly subcritical in the large-`N` limit.

---

# 11. What is genuinely stronger than the Rev. 0 centerpiece

The `gamma=0` statement

```text
raw dark generation O(N)
+ normalized bright projection 1/N
-> accepted dark O(1)
```

is mathematically close to standard coherent mode filtering of independent noise.

The finite-dephasing theorem adds a nontrivial detector task constraint:

```text
state-space filtering
+ open-system leakage
+ fixed required collection efficiency
-> three distinct N-scaling regimes.
```

The strongest candidate contribution is therefore the **efficiency-controlled scaling transition**, not the static projection identity.

---

# 12. Prior-art boundary after focused audit

The following neighboring physics is established and must not be claimed as new:

- quantum coherence/backaction as a photodetector design resource (Young, Sarovar, Léonard, Phys. Rev. A 97, 033836 (2018));
- bright/dark bosonic modes and dephasing-induced intermode scattering (Shammah et al., Phys. Rev. A 96, 023863 (2017));
- dark-state protection and coherence-assisted photocells (e.g. Fruchtman et al., Phys. Rev. Lett. 117, 203603 (2016));
- collective electronic polarization coupled to extractor transport in a quantum infrared detector (Pisani et al., Nature Communications 14, 3914 (2023));
- broad finite-size/decoherence scaling transitions in Dicke/superabsorption systems, including recent 2026 work.

A focused primary-source search did not locate the specific detector theorem

```text
fixed required internal collection efficiency eta
+ bright extraction kappa
+ local dephasing gamma
+ N independent internal dark-generation sites

-> critical eta_c=kappa/(kappa+gamma)
-> O(1), logarithmic, and O(N)/O(N^2) gate/dark-count regimes.
```

This absence is not proof of novelty. The recent literature on decoherence-induced collective scaling makes broad priority claims especially inappropriate.

---

# 13. Claim boundaries

This theorem does not establish:

- end-to-end photon absorption efficiency; `eta` is conditional internal collection after bright-state preparation;
- interacting/many-excitation exactness; the Poisson stream is an explicit independent-particle lift;
- protection from same-mode background photons;
- robustness to correlated dark baths aligned with the bright state;
- universality beyond the symmetric Markovian pure-dephasing model;
- that a real semiconductor can realize the required coherent manifold and bright-selective extraction;
- novelty or practical superiority to conventional photodetector architectures.

Those limitations must remain visible in any manuscript.

---

# 14. Manuscript consequence

Rev. 1 should be rebuilt around this theorem.

Recommended hierarchy:

1. static bright projection as setup, not novelty centerpiece;
2. exact one-body extraction/dephasing kernel;
3. explicit independent-particle stochastic lift;
4. fixed-efficiency scaling theorem as the main result;
5. `gamma=0` `N` cancellation as a corollary;
6. thermodynamic local-detailed-balance affinity result as a secondary scalability constraint rather than a coequal novelty claim.

Do not open Experiment 10 while this manuscript line remains alive.
