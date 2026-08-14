# Experiment 09 — Robustness of the scalable-efficiency ceiling to one-shot site saturation

**Date:** 2026-08-14  
**Status:** STRENGTHENS HEADLINE THEOREM / EXACT POWER-LAW TABLE REMAINS MODEL-SPECIFIC / NOVELTY NOT ESTABLISHED

## Why this check is necessary

The Rev. 4 counting model uses an independent-particle Poisson lift: every local site generates dark excitations at rate `d`, generated excitations do not interact, and multiple events from one site are allowed during one gate.

That lift is mathematically clean, but on a strict slow-recycling branch the efficiency-selected gate can grow with `N`. At fixed `d`, many events per site can then occur, so describing the lift as universally “low density” is too strong.

A hostile detector referee could therefore ask whether the headline scalable-efficiency ceiling is merely an artifact of allowing unlimited noninteracting events per microscopic site.

This note tests the opposite extreme: **maximal one-shot saturation**, in which each microscopic site can generate at most one dark excitation during the entire gate.

The headline ceiling survives.

---

# 1. One-shot saturated-site model

Each of the `N` local sites begins available. Its first internal dark event occurs after an independent exponential waiting time with rate `d`. After that first event, the site produces no additional dark events during the gate.

The generated excitation follows the same one-body collection kernel `C_{D,N}(t)` as in the main model.

For a gate of duration `T`, the expected number of accepted dark events is

```math
\boxed{
\mu_{\mathrm{sat},N}(T)
=N\int_0^T d e^{-ds}
C_{D,N}(T-s)\,ds.
}
```

This is the most aggressive simple saturation model: there can be at most `N` accepted local events in a gate.

It is therefore strictly no larger than the unlimited Poisson-lift mean,

```math
\boxed{
\mu_{\mathrm{sat},N}(T)
\le
\mu_{\mathrm{Pois},N}(T)
=Nd\int_0^T C_{D,N}(u)\,du.
}
```

The exact superlinear slow-branch powers of the Poisson lift are consequently not universal once site capacity is imposed.

---

# 2. Fast branches remain bounded

On every fast branch identified in the main scaling theorem,

```math
\mu_{\mathrm{Pois},N}[T_N(\eta)]=O(1)
```

under the bounded-resource assumptions used to define the scalable efficiency ceiling.

Since one-shot saturation can only reduce the accepted event count,

```math
\boxed{
\mu_{\mathrm{sat},N}[T_N(\eta)]
\le O(1).
}
```

Thus every efficiency target classified as scalable by the Poisson reference model remains scalable under maximal one-shot saturation.

---

# 3. Strict slow branches still incur Omega(N) accepted events

Let `T_N=T_N(eta)` be an operating point that lies strictly on a slow-recycling branch.

Restrict attention to sites whose first dark event occurs during the first half of the gate. Every such excitation has age at least `T_N/2` at gate closure. Because `C_{D,N}(t)` is nondecreasing,

```math
\mu_{\mathrm{sat},N}(T_N)
\ge
N
\left(1-e^{-dT_N/2}\right)
C_{D,N}(T_N/2).
```

This lower bound is enough.

## A. Dephasing-dominated sector, alpha < beta

For every fixed `eta>0`,

```math
T_N
\sim
\frac{x_\eta}{\kappa_0}N^{1-\alpha},
\qquad
x_\eta=-\ln(1-\eta).
```

On the slow variable `z=lambda_N t/N`, the local-event kernel tends to

```math
C_{D,N}\to1-e^{-z}.
```

At half the minimum gate,

```math
\boxed{
C_{D,N}(T_N/2)
\longrightarrow
1-e^{-x_\eta/2}>0.
}
```

Under the bounded local-extraction resource, `alpha<=1`.

- If `alpha<1`, then `T_N->infinity`, so `1-e^{-dT_N/2}->1`.
- If `alpha=1`, then `T_N` approaches a positive constant, so `1-e^{-dT_N/2}` approaches a positive constant.

Therefore

```math
\boxed{
\mu_{\mathrm{sat},N}[T_N(\eta)]
=\Omega(N)
\qquad(\alpha<\beta).
}
```

Because the one-shot model also enforces `mu_sat,N<=N`, the strict slow branch is in fact `Theta(N)` in this maximally saturating reference model.

## B. Balanced supercritical sector, alpha = beta = s and eta > q0

Here

```math
T_N
\sim
\frac{L_\eta}{\lambda_0}N^{1-s},
```

with

```math
L_\eta=\ln\frac{1-q_0}{1-\eta}>0.
```

On the slow variable the local-event kernel tends to

```math
C_{D,N}\to1-e^{-y}.
```

Hence

```math
\boxed{
C_{D,N}(T_N/2)
\longrightarrow
1-e^{-L_\eta/2}>0.
}
```

The bounded local-extraction theorem gives `s<=1`.

Again, either `T_N->infinity` (`s<1`) or `T_N` approaches a positive constant (`s=1`), so the probability of at least one first-half generation event per site stays bounded away from zero.

Thus

```math
\boxed{
\mu_{\mathrm{sat},N}[T_N(\eta)]
=\Omega(N)
\qquad(\alpha=\beta=s,\ eta>q_0).
}
```

And, because at most one event is allowed per site,

```math
\mu_{\mathrm{sat},N}=\Theta(N)
```

on the strict slow branch.

---

# 4. Robust scalable-efficiency ceiling

The Poisson lift supplies the exact detailed power-law table used in the main manuscript.

The one-shot saturated model changes the **magnitude and exponent** of the divergent slow-branch burden, but not the bounded/unbounded classification that defines the headline ceiling.

Under

```math
0\le\alpha\le1
```

and bounded counted coupling per microscopic state,

```math
\boxed{
\eta_{\mathrm{sc}}
=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta
\end{cases}}
```

holds for both:

```text
unlimited independent-particle Poisson generation;
and
maximally suppressive one-shot generation per microscopic site.
```

The exact slow-branch count law differs:

```text
Poisson independent-particle reference:
    mu_local ~ N^{2-alpha} (or N^{2-s});

one-shot saturated reference:
    mu_local ~ Theta(N) on every strict slow branch.
```

But **strict slow recycling remains incompatible with bounded accepted local-dark burden.**

---

# 5. Manuscript consequence

The Rev. 4 manuscript should no longer describe the independent-particle lift simply as a “low-density” model without qualification.

A more accurate statement is:

> The Poisson lift is a linear independent-particle reference model that gives exact count coefficients and powers when multiple noninteracting events per site are allowed. Its strict slow-branch exponents are not universal under saturation. However, the headline scalable-efficiency ceiling and the `Omega(N)` no-go for strict slow recycling survive even in the opposite one-shot-per-site limit.

This is a stronger and more physically defensible claim boundary.

No new experiment branch is justified by this correction.
