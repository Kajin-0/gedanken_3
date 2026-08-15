# Progress Log — Experiment 12: Oscillator-Strength / Thermal-State-Count Bound

## 2026-08-14 — branch opened provisionally

Branch:

```text
experiment-12-oscillator-strength-state-count-bound
```

Opened only after the premise survived a focused search better than the preceding rejected candidates.

Question: can fixed interband optical spectral weight coexist with arbitrarily small intrinsic thermal carrier population when the physical velocity operator has a finite norm?

---

## 2026-08-14 — exact two-manifold theorem

For flat conduction/valence manifolds separated by `E_gamma`, intrinsic neutrality and exact Fermi occupations were combined with the singular-value bound

```math
\|P_c\hat v_iP_v\|_F^2
\le
v_{max}^2\min(N_c,N_v).
```

Including Pauli blocking gives the tight result

```math
\boxed{
N_{th}
\ge
\frac{S_{abs}}{v_{max}^2}
\frac{1}{e^{E_\gamma/(2k_BT)}-1}.
}
```

The Bose-like thermal factor is an optimized ratio of fermionic thermal occupation to Pauli-unblocked oscillator strength, not a bosonic assumption.

Using Kubo-Greenwood,

```math
\boxed{
n_{th}
\ge
\frac{E_\gamma}{\pi e^2v_{max}^2}
\frac{W_\sigma}{e^{E_\gamma/(2k_BT)}-1},
}
```

where

```math
W_\sigma=\int\sigma_1(\omega)d\omega.
```

Sheet form follows by multiplying by absorber thickness.

Low-energy limit:

```math
\boxed{
n_{th,min}
\to
\frac{2k_BT}{\pi e^2v_{max}^2}W_\sigma
}
```

at fixed integrated optical spectral weight as `E_gamma -> 0`.

A single-pass narrowband optical-depth corollary was also derived.

Disposition:

```text
FIRST EXACT RESULT SURVIVES.
NOVELTY NOT ESTABLISHED.
```

---

## Active frontier

Generalize to dispersive bands and multiple transition energies.

Primary danger:

```text
one conduction or valence state may participate in optical transitions at more than one energy;
frequency-bin state counts may therefore not be additive.
```

Need either:

```text
a valid global weighted-rank inequality,
```

or

```text
a counterexample proving the flat-manifold theorem cannot be generalized without an additional resource.
```

Do not jump to D* or candidate materials before this is resolved.
