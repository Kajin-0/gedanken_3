# Experiment 07 — Theoretical isotope-sensitivity bounds for sequential SRH

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only

## 1. Two-step SRH elasticity

For sequential electron and hole capture rates `r_n` and `r_p`,

```math
g=\frac{r_n r_p}{r_n+r_p}.
```

For isotope parameter `M`, define

```math
\alpha_n=\frac{\partial\ln r_n}{\partial\ln M},
\qquad
\alpha_p=\frac{\partial\ln r_p}{\partial\ln M}.
```

Then

```math
\boxed{
\frac{\partial\ln g}{\partial\ln M}
=\frac{r_p}{r_n+r_p}\alpha_n
+\frac{r_n}{r_n+r_p}\alpha_p.
}
```

Equivalently, with waiting times `tau_i=1/r_i`,

```math
\boxed{
\alpha_g
=\frac{\tau_n}{\tau_n+\tau_p}\alpha_n
+\frac{\tau_p}{\tau_n+\tau_p}\alpha_p.
}
```

The weights are positive and sum to one. Hence the cycle elasticity lies between the two step elasticities.

## 2. General serial-parallel convexity theorem

For an N-step sequential cycle,

```math
g=\left(\sum_i r_i^{-1}\right)^{-1}.
```

Then

```math
\boxed{
\frac{\partial\ln g}{\partial\ln M}
=\sum_i W_i\alpha_i,
\qquad
W_i=\frac{r_i^{-1}}{\sum_j r_j^{-1}}.
}
```

If step `i` contains parallel microscopic channels

```math
r_i=\sum_k r_{ik},
```

then

```math
\alpha_i=\sum_k f_{ik}\beta_{ik},
\qquad
f_{ik}=\frac{r_{ik}}{r_i},
```

where `beta_ik=d ln r_ik/d ln M`.

Therefore

```math
\boxed{
\alpha_g=\sum_{i,k}W_{ik}\beta_{ik},
\qquad
W_{ik}=W_i f_{ik}\ge0,
\qquad
\sum_{i,k}W_{ik}=1.
}
```

Thus positive serial waiting times and positive parallel capture pathways cannot amplify isotope elasticity beyond the microscopic channel extrema.

This mathematical structure is an instance of established flux-control / multistep kinetic-isotope theory and is not claimed as novel.

## 3. Finite isotope-change bound

Let every microscopic channel change from isotope state A to B by factor

```math
K_{ik}=r_{ik}^{(B)}/r_{ik}^{(A)}.
```

If

```math
K_min <= K_ik <= K_max
```

for all microscopic channels, monotonicity and degree-one homogeneity give

```math
\boxed{
K_{min}\le\frac{g_B}{g_A}\le K_{max}.
}
```

Hence a full sequential SRH cycle cannot produce a finite isotope ratio larger than the largest microscopic channel ratio.

## 4. One isotope-sensitive step

If only electron capture changes, with

```math
K_n=r_{n,B}/r_{n,A},
\qquad
b=r_{n,A}/r_{p,A},
```

then exactly

```math
\boxed{
\frac{g_B}{g_A}
=K_n\frac{1+b}{1+K_n b}.
}
```

Therefore

```text
K_n < 1  =>  K_n <= g_B/g_A <= 1
K_n > 1  =>  1 <= g_B/g_A <= K_n
```

The serial cycle masks the intrinsic electron-capture isotope effect but cannot reverse its sign when the hole step is isotope-insensitive.

## 5. Whole-cycle sign reversal is not unique evidence for a threshold

If electron and hole elasticities have opposite signs,

```math
\alpha_g
=\frac{\tau_n}{\tau_n+\tau_p}\alpha_n
+\frac{\tau_p}{\tau_n+\tau_p}\alpha_p.
```

The total isotope effect crosses zero when

```math
\boxed{
\frac{\tau_n}{\tau_p}=-\frac{\alpha_p}{\alpha_n}.
}
```

Thus a system-level sign reversal can arise solely from temperature-dependent redistribution of the kinetic bottleneck between two oppositely isotope-sensitive steps. It is not by itself a unique signature of a one-phonon threshold.

## 6. Exact finite-isotope relation for one one-phonon channel

Use the reduced model

```math
r(M,T)=A(M)\Delta(M)^\nu
\exp[-\Delta(M)/(kT)],
```

where for the simple 3-D optical-phonon phase-space model `nu=1/2` and

```math
\Delta=\hbar\omega-\varepsilon.
```

For isotope states A and B,

```math
\boxed{
\ln\frac{r_B}{r_A}
=\ln\frac{A_B}{A_A}
+\nu\ln\frac{\Delta_B}{\Delta_A}
-\frac{\Delta_B-\Delta_A}{kT}.
}
```

Therefore, with `x=1/(kT)`,

```math
\boxed{
\frac{d}{dx}\ln\frac{r_B}{r_A}
=-(\Delta_B-\Delta_A).
}
```

Within this model the isotope-ratio slope is independent of the unknown prefactor ratio and of the threshold power `nu`; both enter only the intercept.

This is the cleanest surviving one-channel analytical closure.

## 7. Full sequential Arrhenius structure

Let isotope state `s` have serial rates

```math
r_i^{(s)}=a_i^{(s)}\exp[-\Delta_i^{(s)}x],
\qquad x=1/(kT).
```

Then

```math
g_s=\left[\sum_i a_i^{(s)-1}\exp(\Delta_i^{(s)}x)\right]^{-1}.
```

Define

```math
L(x)=\ln[g_B/g_A].
```

Exactly,

```math
\boxed{
L'(x)=\langle\Delta\rangle_A-\langle\Delta\rangle_B,
}
```

where each average is weighted by the corresponding fraction of total mean waiting time.

Also

```math
\boxed{
L''(x)=\operatorname{Var}_A(\Delta)-\operatorname{Var}_B(\Delta).
}
```

Thus:

- one effective channel gives exact linearity of `ln(g_B/g_A)` versus `1/(kT)`;
- multiple serial barriers generically introduce curvature because the bottleneck weights change with temperature;
- curvature quantifies redistribution of waiting-time control, but zero curvature is not unique proof of a single channel because multiple contributions can cancel.

## 8. Prior-art boundary

The convex weighting / masking structure is closely related to established metabolic-control summation theorems and to apparent kinetic isotope effects in multistep steady-state reactions. Do not claim this generic mathematics as new.

The remaining HgCdTe-specific theoretical question is narrower:

> Given realistic isotope dependence of the HgTe-like phonon frequency and of the mercury-vacancy electronic separation, what range of microscopic one-phonon isotope ratios is mathematically allowed, and how much of that range can survive the negative-U SRH cycle after arbitrary positive bypass pathways are admitted?

## 9. Next theoretical step

Derive a bound for

```math
\beta=\frac{\partial\ln r}{\partial\ln M}
```

for the one-optical-phonon channel when

```math
\Delta=\hbar\omega-\varepsilon,
```

including both

```math
\partial\omega/\partial M
```

and

```math
\partial\varepsilon/\partial M.
```

Then determine whether any large isotope effect can be guaranteed from mass scaling alone, or whether an unknown electronic isotope shift can always cancel the phonon contribution. That is the next analytical no-go question.