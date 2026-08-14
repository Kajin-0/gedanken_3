# Experiment 09 — Gated reverse-injection thermodynamic phase law

**Date:** 2026-08-14  
**Status:** CORRECTS EARLIER FIXED-RATE AFFINITY INTERPRETATION / DETECTOR-TASK-SPECIFIC THERMODYNAMIC RESULT / NOVELTY NOT ESTABLISHED

## Why this correction is necessary

Earlier Experiment-09 work used local detailed balance

```math
\bar\kappa_N
=\kappa_Ne^{-\beta\Delta F_N}
```

to argue that if the useful forward extraction coefficient `kappa_N` is collectively enhanced, keeping the **reverse coefficient** fixed requires an additional affinity `kT ln(mathcal C)`.

That rate-coefficient statement is correct.

It is **not**, however, the correct statement for the detector's accepted reverse dark counts when the gate duration itself is chosen by a required collection efficiency. If a larger `kappa_N` shortens the minimum gate, the increased reverse injection rate can be canceled by the reduced exposure time.

The correct object is

```math
\boxed{
\mu_{rev,N}(\eta)
=\bar\kappa_N
\int_0^{T_N(\eta)}C_{S,N}(u)du,
}
```

where `T_N(eta)` is the minimum gate reaching the prescribed conditional internal signal efficiency.

This note derives the asymptotic scaling of that gated reverse contribution across the rate-scaling phase diagram.

---

# 1. Reverse channel model

Assume the counted extraction transition is thermally reversible and obeys an effective local-detailed-balance relation

```math
\boxed{
\frac{\bar\kappa_N}{\kappa_N}
=e^{-\beta\Delta F_N}.
}
```

A reverse event injects a bright excitation. Under the same independent-event lift used for local dark generation, each injected bright excitation subsequently produces a counted forward event with probability `C_{S,N}(u)` after age `u`.

Thus

```math
\boxed{
\mu_{rev,N}(\eta)
=\kappa_N e^{-\beta\Delta F_N}
I_{S,N}(\eta),
}
```

with

```math
I_{S,N}(\eta)
=\int_0^{T_N(\eta)}C_{S,N}(u)du.
```

The question is how the product `kappa_N I_S` scales.

---

# 2. Extraction-dominated sector: alpha > beta

Here `q_N->1` and every fixed `eta<1` is on the fast branch.

Define

```math
x_\eta=-\ln(1-\eta).
```

On the fast variable `v=kappa_N t`,

```math
C_{S,N}\to1-e^{-v}.
```

The gate is

```math
T_N\sim x_\eta/\kappa_N.
```

Therefore

```math
I_{S,N}
\sim
\frac1{\kappa_N}
\int_0^{x_\eta}(1-e^{-v})dv
=
\frac{x_\eta-\eta}{\kappa_N}.
```

Hence

```math
\boxed{
\mu_{rev,N}(\eta)
\sim
e^{-\beta\Delta F_N}
[x_\eta-\eta].
}
```

For fixed affinity, the gated reverse burden is **O(1)** even if `kappa_N` grows collectively.

Thus no `kT ln(kappa_N)` affinity increase is required merely to keep the efficiency-selected gated reverse burden bounded on this fast branch.

---

# 3. Balanced sector: alpha = beta = s

Let

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0},
```

```math
A=\kappa_0+\gamma_0,
```

and `kappa_N=q_0 A N^s`.

## 3.1 Subcritical efficiency eta < q0

Use

```math
x_\eta=-\ln(1-\eta/q_0).
```

On the fast variable `v=A N^s t`,

```math
C_{S,N}\to q_0(1-e^{-v}).
```

Thus

```math
I_{S,N}
\sim
\frac1{A N^s}
[q_0x_\eta-\eta].
```

Multiplying by `kappa_N=q_0 A N^s` gives

```math
\boxed{
\mu_{rev,N}
\sim
e^{-\beta\Delta F_N}
q_0[q_0x_\eta-\eta].
}
```

Again the gated reverse burden is `O(1)` at fixed affinity.

## 3.2 Critical efficiency eta = q0

At the boundary,

```math
A N^s T_N
\sim x_N,
\qquad
x_N\sim W\left(\frac{N}{(1-q_0)^2}\right)
\sim\ln N.
```

Over most of this logarithmically extended fast-time window,

```math
C_{S,N}\simeq q_0.
```

Therefore

```math
I_{S,N}
\sim
\frac{q_0}{A N^s}x_N
```

at leading logarithmic order, and

```math
\boxed{
\mu_{rev,N}
\sim
e^{-\beta\Delta F_N}q_0^2x_N
=\Theta(e^{-\beta\Delta F_N}\ln N).
}
```

At fixed affinity the reverse burden grows only logarithmically.

Keeping it bounded requires only

```math
\boxed{
\Delta F_N
\gtrsim
kT\ln\ln N
}
```

up to an `O(kT)` additive constant.

## 3.3 Supercritical efficiency eta > q0

Define

```math
L_\eta=\ln\frac{1-q_0}{1-\eta}.
```

On the slow variable

```math
y=\frac{\lambda_0N^s t}{N},
```

```math
C_{S,N}\to1-(1-q_0)e^{-y}.
```

The gate ends at `y=L_eta`. Hence

```math
I_{S,N}
\sim
\frac{N^{1-s}}{\lambda_0}
\left[L_\eta-(\eta-q_0)\right].
```

Using

```math
\frac{\kappa_0}{\lambda_0}
=\frac1{1-q_0},
```

gives

```math
\boxed{
\mu_{rev,N}
\sim
e^{-\beta\Delta F_N}
\frac{N}{1-q_0}
\left[L_\eta-(\eta-q_0)\right].
}
```

Thus the gated reverse burden is `O(N)` at fixed affinity, independent of the common rate exponent `s`.

Keeping it bounded requires

```math
\boxed{
\Delta F_N
\gtrsim kT\ln N
}
```

up to an additive constant.

---

# 4. Dephasing-dominated sector: alpha < beta

Here every fixed positive efficiency is on the slow-recycling branch.

Let

```math
x_\eta=-\ln(1-\eta).
```

Since `lambda_N~kappa_N`, the slow variable is

```math
z=\frac{\kappa_Nt}{N}.
```

Then

```math
C_{S,N}\to1-e^{-z},
```

and the minimum gate ends at `z=x_eta`.

Therefore

```math
I_{S,N}
\sim
\frac{N}{\kappa_N}[x_\eta-\eta].
```

Multiplying by `bar kappa_N=kappa_N exp(-beta DeltaF_N)` yields

```math
\boxed{
\mu_{rev,N}
\sim
e^{-\beta\Delta F_N}
N[x_\eta-\eta].
}
```

At fixed affinity the gated reverse burden is `O(N)`, again independent of `alpha` and `beta` once this slow branch is selected.

Keeping it bounded requires

```math
\boxed{
\Delta F_N\gtrsim kT\ln N.
}
```

---

# 5. Gated thermodynamic phase law

At fixed effective affinity,

```math
\boxed{
\begin{array}{c|c|c}
\text{rate/efficiency sector} & \mu_{rev,N} & \text{extra affinity for bounded }\mu_{rev}\\
\hline
\alpha>\beta & O(1) & O(kT)\\
\alpha=\beta,\ \eta<q_0 & O(1) & O(kT)\\
\alpha=\beta,\ \eta=q_0 & O(\ln N) & kT\ln\ln N\\
\alpha=\beta,\ \eta>q_0 & O(N) & kT\ln N\\
\alpha<\beta & O(N) & kT\ln N
\end{array}}
```

This replaces the earlier blanket interpretation that collective forward-rate enhancement always forces an extra `kT ln(mathcal C)` affinity in the **gated detector burden**.

The rate-coefficient statement remains true:

```math
\bar\kappa_N/\kappa_N=e^{-\beta\Delta F_N}.
```

But the operational detector cost depends on how long the detector must remain exposed to the reverse process.

---

# 6. Combined local-dark and reverse-dark scaling

The local internally generated burden from `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md` is

```text
fast extraction-dominated:
    mu_local ~ N^{-alpha};

balanced subcritical:
    mu_local ~ N^{-s};

balanced critical:
    mu_local ~ N^{-s}(ln N)^2;

balanced supercritical:
    mu_local ~ N^{2-s};

dephasing dominated:
    mu_local ~ N^{2-alpha}.
```

The thermally reversed extractor at fixed affinity contributes

```text
fast branches:
    mu_rev ~ O(1);

critical balanced branch:
    mu_rev ~ O(ln N);

slow branches:
    mu_rev ~ O(N).
```

Thus collective extraction can suppress the local-generation contribution faster than it suppresses the thermodynamic reverse floor. For example, with

```math
\kappa_N\propto N,
\qquad
\gamma_N=O(1),
```

one finds

```math
\mu_{local}\sim N^{-1},
```

but

```math
\mu_{rev}\sim O(1)
```

at fixed affinity.

The reverse channel therefore becomes the asymptotic floor even though it does **not** diverge with `N` in the efficiency-selected fast gate.

This is a more accurate detector-level interpretation than the previous fixed-gate `kT ln N` argument.

---

# 7. Prior-art and claim boundary

Local detailed balance and thermodynamic detector-performance tradeoffs are established. In particular, current autonomous quantum-detector theory explicitly relates thermodynamic dissipation to efficiency, dark counts, jitter, and dead time.

The present result should therefore be positioned narrowly as the consequence of applying a reversible bright extractor to the **same efficiency-selected gate** used in the coherence/dephasing phase diagram.

No generic thermodynamic novelty is claimed.

---

# 8. Manuscript consequence

Rev. 2 should not retain the old statement

```text
collective rate enhancement C
-> extra affinity kT ln C required for bounded gated reverse dark counts
```

without qualification.

The correct detector statement is branch dependent:

```text
fast gate:
    rate enhancement and gate shortening cancel -> O(1) reverse burden;

critical balanced gate:
    O(log N) reverse burden;

slow-recycling gate:
    O(N) reverse burden.
```

This gated thermodynamic phase law is a secondary result supporting the main internal-dark phase diagram.
