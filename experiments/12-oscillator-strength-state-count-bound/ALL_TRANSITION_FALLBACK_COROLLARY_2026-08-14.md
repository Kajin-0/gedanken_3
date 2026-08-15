# Experiment 12 — All-Transition Thermal-Excitation Fallback Corollary

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Role:** robustness corollary when `cross-mu` optical weight cannot be separated experimentally  
**Disposition:** **EXACT BUT WEAKER / LIKELY CLOSE TO DETAILED-BALANCE RESPONSE THEORY / NOT A NOVELTY CLAIM**

## 1. Motivation

The strong Experiment-12 population theorem uses the conductivity from transitions that cross the chemical potential. The half-transition thermal scale

```math
e^{E/(2k_BT)}
```

comes from the fact that a cross-`mu` transition has one thermally costly state on each side of `mu`.

An experimental optical spectrum may also contain transitions whose two one-particle states both lie below `mu` or both lie above it.

There is a weaker theorem that includes **all** one-body transitions and does not require classifying them by which side of `mu` they occupy.

---

## 2. Exact detailed-balance identity for any one-body transition

Take any two exact one-particle states

```math
E_a<E_b,
\qquad
E=E_b-E_a>0.
```

Let

```math
f_a=f(E_a),
\qquad
f_b=f(E_b).
```

Fermi algebra gives exactly

```math
\boxed{
\frac{f_a-f_b}{e^{E/(k_BT)}-1}
=f_b(1-f_a).
}
```

Define the thermal deviation of each state from the zero-temperature Fermi sea,

```math
q_j
=\left|f(E_j)-\Theta(\mu-E_j)\right|.
```

Thus

```text
E_j > mu: q_j = f_j;
E_j < mu: q_j = 1-f_j.
```

For every ordered transition,

```math
\boxed{
2f_b(1-f_a)
\le q_a+q_b.
}
```

This follows directly in the three cases:

```text
both above mu;
both below mu;
one on each side.
```

Therefore

```math
\boxed{
\frac{2(f_a-f_b)}{e^{E/(k_BT)}-1}
\le q_a+q_b.
}
```

The full-energy Bose denominator is weaker than the half-energy denominator available for cross-`mu` transitions.

---

## 3. Windowed all-transition theorem

For any positive-frequency window `B`, let `T_B^all` contain **all** allowed one-body optical transitions in that window.

Define selected row/column velocity strengths exactly as in the main theorem and let

```math
v_{*,B}^{all\,2}
```

be the maximum selected weighted degree of that full transition graph.

Define total thermal excitation density relative to the zero-temperature Fermi sea,

```math
\boxed{
n_{exc}
=\frac1V\sum_jq_j.
}
```

Then

```math
\boxed{
n_{exc}
\ge
\frac{2}{\pi e^2v_{*,B}^{all\,2}}
\int_B
\frac{\hbar\omega\,\sigma_1^{all}(\omega)}
{e^{\hbar\omega/(k_BT)}-1}
d\omega.
}
```

Here `sigma_1^all` is the complete independent-particle positive-frequency optical conductivity within the chosen one-body model and polarization.

---

## 4. Comparison with the strong cross-`mu` theorem

For the same transition energy `E`,

```math
\frac{E}{e^{E/(2k_BT)}-1}
\gg
\frac{E}{e^{E/(k_BT)}-1}
```

when `E >> kBT`.

Thus the cross-`mu` theorem contains the important intrinsic-semiconductor half-gap activation and is exponentially stronger in the detector regime.

The all-transition version is primarily a robustness statement:

```text
failure to spectroscopically decompose the optical response does not destroy every thermal-excitation constraint;
it only loses the stronger cross-mu information.
```

---

## 5. Novelty disposition

The exact identity

```math
(f_a-f_b)/(e^{\beta E}-1)=f_b(1-f_a)
```

is ordinary finite-temperature detailed balance / Fermi statistics. This all-transition corollary is therefore likely much closer to standard fluctuation-response theory than the cross-`mu` half-gap theorem.

```text
DO NOT USE AS A NOVELTY CLAIM.
```

Its role is to clarify scope and experimental fallback only.
