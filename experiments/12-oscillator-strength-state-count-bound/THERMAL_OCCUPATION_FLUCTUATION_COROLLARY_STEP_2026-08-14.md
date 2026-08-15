# Experiment 12 — Thermal Occupation-Fluctuation Corollary

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **EXACT SINGLE-PARTICLE OCCUPATION-VARIANCE INEQUALITY DERIVED / NOT A FINITE-BANDWIDTH DETECTOR-NOISE THEOREM / SECONDARY COROLLARY ONLY**

## 1. Motivation

The controlling Experiment-12 theorem bounds equilibrium thermally excited quasiparticle population by a thermally weighted direct-interband optical spectral weight.

A natural detector question is whether the same optical requirement also forces equilibrium carrier-number fluctuations even when the relevant states are localized and contribute weakly to dc current.

The answer is partially yes at the level of independent Fermi occupations, but this does **not** by itself create a universal finite-bandwidth dark-noise floor.

---

## 2. Pointwise occupation-variance inequality

For one direct interband transition

```math
E_v<\mu<E_c,
\qquad
E=E_c-E_v>0,
```

define

```math
p=f(E_c),
\qquad
h=1-f(E_v),
\qquad
D=f(E_v)-f(E_c).
```

Let

```math
a=e^{-\beta(E_c-\mu)},
\qquad
b=e^{-\beta(\mu-E_v)},
\qquad
ab=e^{-\beta E}\equiv z.
```

Then

```math
D=\frac{1-z}{(1+a)(1+b)},
```

while the sum of Bernoulli occupation variances is

```math
p(1-p)+h(1-h)
=
\frac{a}{(1+a)^2}
+
\frac{b}{(1+b)^2}.
```

Use

```math
\sinh(\beta E/2)
=\frac{1-z}{2\sqrt z}.
```

After cancelling the common factor `1-z`, the desired inequality is equivalent to

```math
2\sqrt{ab}
\le
\frac{a(1+b)}{1+a}
+
\frac{b(1+a)}{1+b}.
```

The two terms on the right have product exactly

```math
ab.
```

Therefore AM-GM proves

```math
\boxed{
D
\le
\sinh\!\left(\frac{E}{2k_BT}\right)
\left[p(1-p)+h(1-h)\right].
}
```

Equality holds when

```math
a=b,
```

i.e. when the two states are symmetric about the chemical potential.

---

## 3. Sum over arbitrary independent-particle states

For direct interband velocity matrix elements `v_cv`, multiply the pointwise result by `|v_cv|^2` and sum over all transitions crossing `mu`.

Assume the same Experiment-12 row/column velocity-strength resource

```math
\sum_v|v_{cv}|^2\le v_*^2
\quad\forall c,
```

```math
\sum_c|v_{cv}|^2\le v_*^2
\quad\forall v.
```

Define the independent-fermion one-body occupation-variance density

```math
\mathcal V_{1b}
=\frac1V
\left[
\sum_c p_c(1-p_c)
+
\sum_v h_v(1-h_v)
\right].
```

Then

```math
\boxed{
\frac1V
\sum_{cv}
\frac{D_{cv}|v_{cv}|^2}
{\sinh[E_{cv}/(2k_BT)]}
\le
v_*^2\mathcal V_{1b}.
}
```

Using Kubo-Greenwood gives

```math
\boxed{
\mathcal V_{1b}
\ge
\frac{1}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{\sinh[\hbar\omega/(2k_BT)]}
d\omega.
}
```

This is the exact independent-particle occupation-variance corollary.

---

## 4. Low-energy behavior

For `E << kBT`,

```math
\frac{E}{\sinh(E/2k_BT)}
\to2k_BT.
```

Therefore low-energy optical spectral weight also forces a finite lower bound on the sum of one-body thermal occupation variances when `v_*` is finite.

At high energy,

```math
\frac{E}{\sinh(E/2k_BT)}
\sim2E e^{-E/(2k_BT)}.
```

The variance and population kernels therefore have the same leading Boltzmann activation but differ away from the nondegenerate limit.

---

## 5. Dirac checks

For neutral 2-D massless Dirac quasiparticles / graphene, the exact total electron-plus-hole one-body occupation variance is

```math
\mathcal V_{1b}^{exact}
=\frac{4\ln2}{\pi}
\left(\frac{k_BT}{\hbar v_F}\right)^2.
```

The corollary gives

```math
\mathcal V_{1b}^{bound}
=\frac{2\ln2}{\pi}
\left(\frac{k_BT}{\hbar v_F}\right)^2,
```

so

```math
\boxed{\mathcal V_{1b}^{bound}/\mathcal V_{1b}^{exact}=1/2.}
```

For 3-D massless Dirac quasiparticles the analogous ratio is `2/3`.

For the finite-gap 3-D massive-Dirac Experiment-10 point

```text
Delta/kBT = 2.39796146,
```

numerical evaluation gives approximately

```math
\boxed{\mathcal V_{1b}^{bound}/\mathcal V_{1b}^{exact}\simeq0.793.}
```

Thus the fluctuation corollary has essentially the same tightness pattern as the population theorem in the Dirac validation family.

---

## 6. Why this is NOT yet a detector-noise theorem

Several distinctions are mandatory.

### 6.1 Ensemble dependence

The expression

```math
\sum_j f_j(1-f_j)
```

is the sum of independent grand-canonical Fermi occupation variances.

For a strictly isolated canonical system, fixed total particle number introduces occupation covariances. The measured variance of a chosen carrier-number observable must then be derived in the correct ensemble rather than identified automatically with `mathcal V_1b`.

### 6.2 Integrated variance is not finite-bandwidth noise

Even when `mathcal V_1b` equals the equilibrium variance of the electrically relevant carrier-number observable, Wiener-Khinchin only fixes the **frequency-integrated** fluctuation spectral weight.

The distribution of that noise over frequency depends on kinetics:

```text
recombination/generation lifetime;
escape/collection time;
trapping and detrapping;
contact exchange;
correlations between states.
```

Therefore no lower bound on a particular readout band follows without a dynamical resource or timescale condition.

### 6.3 Electrical transduction is separate

Localized optically active states can have occupation fluctuations yet couple weakly to terminal current. A current-noise theorem would require a separate lower bound on electrical activity / collection coupling.

---

## 7. Scientific role in Experiment 12

Retain this result as a supporting corollary:

```math
\boxed{
\mathcal V_{1b}
\ge
\frac{1}{\pi e^2v_*^2}
\int_0^\infty
\frac{\hbar\omega\,\sigma_1^{inter}(\omega)}
{\sinh[\hbar\omega/(2k_BT)]}
d\omega.
}
```

Do **not** make it the headline claim and do not call it a universal dark-noise floor.

The headline remains the thermal-population versus direct-interband optical spectral-weight inequality, which has fewer ensemble/dynamical assumptions.

## Novelty status

The exact `sinh`-weighted corollary was not located in the focused search performed during this step, but it is mathematically adjacent to standard Fermi occupation fluctuations, fluctuation-dissipation relations, and finite-temperature response inequalities.

```text
NOVELTY NOT ESTABLISHED.
SECONDARY RESULT ONLY.
```
