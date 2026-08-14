# Theoretical Isotope-Control Sum Rule for Sequential SRH Cycles

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** EXACT CONTROL IDENTITY / GENERIC PRIOR ART EXISTS / USE AS TOOL, NOT NOVELTY CLAIM

## 1. Sequential cycle

Consider a unidirectional defect cycle with sequential elementary steps `i=1...N`, each with rate `r_i(M)` and mean waiting time

```math
\tau_i=1/r_i.
```

For one completed recombination event per cycle, the mean cycle rate is

```math
R_{cyc}=\frac{1}{\sum_i \tau_i}.
```

Define logarithmic isotope sensitivity

```math
S_X \equiv \frac{d\ln X}{d\ln M}.
```

Then

```math
\boxed{
S_{R_{cyc}}
=\sum_i \frac{\tau_i}{\sum_j\tau_j} S_{r_i}.
}
```

Proof:

```math
\ln R_{cyc}=-\ln\left(\sum_i \tau_i\right),
\qquad
S_{\tau_i}=-S_{r_i}.
```

Differentiation gives the result directly.

The weights

```math
w_i=\frac{\tau_i}{\sum_j\tau_j}
```

are nonnegative and sum to one. Therefore

```math
\boxed{
\min_i S_{r_i}\le S_{R_{cyc}}\le\max_i S_{r_i}.
}
```

The slowest step automatically receives the largest control weight. A fast elementary step can have an enormous microscopic isotope sensitivity while contributing negligibly to the complete recombination cycle.

For the ordinary two-step capture cycle,

```math
R=\frac{r_n r_p}{r_n+r_p},
```

and

```math
\boxed{
S_R
=\frac{r_p}{r_n+r_p}S_{r_n}
+\frac{r_n}{r_n+r_p}S_{r_p}.
}
```

If electron capture is much slower (`r_n << r_p`), then `S_R -> S_{r_n}`.

## 2. Parallel microscopic channels inside each step

Let elementary step `i` contain parallel channels

```math
r_i=\sum_a r_{ia}.
```

Then

```math
S_{r_i}
=\sum_a \frac{r_{ia}}{r_i}S_{r_{ia}}.
```

Combining serial and parallel weighting,

```math
\boxed{
S_{R_{cyc}}
=\sum_{i,a} W_{ia}S_{r_{ia}},
\qquad
W_{ia}=\frac{\tau_i}{\sum_j\tau_j}\frac{r_{ia}}{r_i}.
}
```

Because

```math
W_{ia}\ge0,
\qquad
\sum_{i,a}W_{ia}=1,
```

the complete cycle sensitivity is inside the convex hull of all microscopic channel sensitivities.

Consequences:

1. an isotope-insensitive bypass channel (`S=0`) can only dilute the total isotope response;
2. strong isotope sensitivity of a non-bottleneck step cannot dominate the detector-level SRH rate;
3. strong isotope sensitivity of a tiny parallel channel does not matter unless that channel carries a non-negligible fraction of the relevant step rate;
4. the strongest detector-level isotope response requires the isotope-sensitive channel to be both kinetically important within its step and located in a cycle-controlling step.

## 3. Exact standard-SRH capture-only sensitivity

For ordinary SRH recombination

```math
U
=N_t\frac{C_n C_p (np-n_i^2)}
{C_n(n+n_1)+C_p(p+p_1)}.
```

Hold `N_t`, `n`, `p`, `n_i`, `n_1`, and `p_1` fixed so that isotope mass perturbs only the capture coefficients. Define

```math
A=C_n(n+n_1),
\qquad
B=C_p(p+p_1).
```

Then

```math
\boxed{
S_U^{(capture)}
=\frac{B}{A+B}S_{C_n}
+\frac{A}{A+B}S_{C_p}.
}
```

Again the weights are nonnegative and sum to one.

This is the standard-SRH analogue of the sequential waiting-time theorem.

## 4. Full isotope response decomposes into three sectors

If isotope substitution is allowed to change electronic energies and defect thermodynamics as well, then

```math
S_U
=S_{N_t}+S_{np-n_i^2}
+\frac{B}{A+B}S_{C_n}
+\frac{A}{A+B}S_{C_p}
-\frac{A}{A+B}S_{n+n_1}
-\frac{B}{A+B}S_{p+p_1}.
```

Thus the total isotope response contains three conceptually distinct sectors:

```text
1. defect-population response     S_Nt
2. electronic/thermodynamic response through ni, n1, p1, Eg, Et, masses
3. capture-kinetic response       convex combination of S_Cn and S_Cp
```

A total dark-current isotope effect is therefore not, by itself, evidence for an isotope-sensitive capture coefficient.

For reverse-generation conditions where `|np| << n_i^2`, the numerator contains approximately

```math
n_i^2=N_cN_v\exp[-E_g/(kT)],
```

so even a small isotope-induced band-gap shift contributes

```math
\delta\ln n_i^2
\simeq
\delta\ln(N_cN_v)-\frac{\delta E_g}{kT}.
```

This can be comparable to or larger than a few-percent kinetic isotope effect in a narrow-gap material.

## 5. Generic one-phonon threshold with finite broadening

A sharp three-dimensional one-phonon onset has reduced phase-space form

```math
F_0(\Delta)\propto \Delta^{1/2}\Theta(\Delta).
```

Convolve the onset with a Gaussian energy distribution of standard deviation `sigma`:

```math
F_\sigma(\Delta)
=\int_0^\infty x^{1/2}
\frac{\exp[-(x-\Delta)^2/(2\sigma^2)]}
{\sqrt{2\pi}\sigma}\,dx.
```

At exact threshold `Delta=0`,

```math
\boxed{
\frac{1}{F_\sigma}
\frac{\partial F_\sigma}{\partial\Delta}
=\frac{\sqrt2\,\Gamma(5/4)}{\Gamma(3/4)}\frac1\sigma
\approx\frac{1.04605}{\sigma}.
}
```

Therefore a small isotope-induced detuning shift gives

```math
\boxed{
\delta\ln F_\sigma
\approx1.04605\frac{\delta\Delta}{\sigma}
}
```

at threshold, before thermal and matrix-element corrections.

More generally, for an onset `F_0 ~ Delta^beta Theta(Delta)`,

```math
\boxed{
\left.\frac{\partial\ln F_\sigma}{\partial\Delta}\right|_{0}
=\frac{\sqrt2\,\Gamma[(\beta+2)/2]}
{\Gamma[(\beta+1)/2]}\frac1\sigma.
}
```

Finite broadening therefore converts the formal sharp-threshold divergence into the dimensionless control parameter

```math
\delta\Delta/\sigma.
```

## 6. No universal isotope-amplification bound without regularity assumptions

The convexity theorem bounds the complete cycle response by the microscopic channel sensitivities, but it does not by itself bound those microscopic sensitivities.

For an exactly sharp threshold, a channel can have divergent relative sensitivity as its rate approaches zero. Therefore no universal finite bound of the form

```math
|S_R| < constant
```

can follow from isotope mass scaling alone.

A finite bound requires additional physical regularity such as:

- finite phonon linewidth;
- finite defect-energy distribution;
- finite lifetime broadening;
- a nonzero parallel bypass;
- or a specified microscopic capture spectral function.

This is an important no-go: isotope mass alone does not determine a maximum possible relative SRH response.

## 7. Prior-art boundary

Do not claim the generic control/summation structure as new. Flux-control summation theorems and cycle-control coefficients are established in reaction-network theory, including catalytic/enzyme cycles. A 2026 Phys. Rev. Applied paper also develops rate analysis for generalized defect-assisted recombination cycles including nonstandard channels.

The present value is as a compact analytical tool for Experiment 07, not as a novelty claim.

Relevant sources:

- Tak et al., Phys. Rev. Applied 25, 054061 (2026), rate analysis of defect-assisted recombination cycles.
- established flux-control/cycle-summation theory in reaction networks.
- Kozlov et al., JETP 165, 840-847 (2024), single-optical-phonon electron/hole capture on mercury vacancies in ~40-meV HgCdTe.
- Kozlov et al., JETP 170, 131-138 (2026), narrow-gap HgCdTe QW carrier capture; electron capture slower than hole capture and controls SRH.

## 8. Next theoretical question

The exact remaining HgCdTe-specific problem is no longer whether a large microscopic isotope response can exist. It can near a narrow phonon threshold.

The harder theoretical question is:

> after including the isotope dependence of the quantized electron-phonon matrix element, Bose occupation, detuning, electronic-level renormalization, and finite broadening, what is the full sign and magnitude of `S_Cn` for the mercury-vacancy electron-capture channel?

Derive that next. Do not return to experimental design.
