# Experiment 09 — Rate-scaling phase diagram

**Date:** 2026-08-14  
**Status:** GENERALIZES REV. 1 FIXED-RATE THEOREM / NOVELTY NOT ESTABLISHED

## Setup

Let the useful bright extraction and local dephasing rates scale with the number of coherently participating states as

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
```

with fixed positive `kappa_0`, `gamma_0`, per-site local event rate `d`, and fixed required conditional internal collection efficiency `0<eta<1`.

The exact one-body dynamics remains

```math
\ddot P+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
```

Define

```math
a_N=\kappa_N+\gamma_N,
\qquad
q_N=\frac{\kappa_N}{a_N},
\qquad
\lambda_N=\frac{\kappa_N\gamma_N}{a_N}.
```

The slow rate satisfies

```math
r_{-,N}=\frac{\lambda_N}{N}[1+O(N^{-1})].
```

Continuous local event generation uses the explicit independent-particle Poisson lift from Rev. 1:

```math
\mu_N(T)=Nd\int_0^T C_{D,N}(u)du.
```

For fixed `eta`, define the minimum gate

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\}
```

and the accepted local-event burden

```math
\mu_N(\eta)=Nd\int_0^{T_N(\eta)}C_{D,N}(u)du.
```

## Branch selection

Exactly,

```math
q_N=\frac{1}{1+(\gamma_0/\kappa_0)N^{\beta-\alpha}},
```

so

```math
q_N\to
\begin{cases}
1,&\alpha>\beta,\\
q_0=\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

Thus `alpha-beta` decides which dynamical branch a fixed efficiency target uses. The absolute value of `alpha` determines the physical gate and local-event scaling.

---

# 1. Extraction-dominated sector: alpha > beta

Every fixed `eta<1` is eventually on the fast branch. Define

```math
x_\eta=-\ln(1-\eta).
```

Since `a_N~kappa_0 N^alpha`,

```math
\boxed{
T_N(\eta)
\sim\frac{x_\eta}{\kappa_0}N^{-\alpha}.
}
```

The fast-time local-event kernel gives

```math
\boxed{
\mu_N(\eta)
\sim\frac{d}{\kappa_0}[x_\eta-\eta]N^{-\alpha}.
}
```

Therefore

```math
\boxed{
\alpha>\beta:
\quad T_N\asymp N^{-\alpha},
\quad \mu_N\asymp N^{-\alpha}.
}
```

Extraction dominance alone does not imply bounded performance: `alpha>0` improves with size, `alpha=0` is constant, and `alpha<0` grows even though extraction still dominates dephasing.

---

# 2. Dephasing-dominated sector: alpha < beta

Now `q_N->0`, so every fixed positive `eta` requires slow recycling. Again let

```math
x_\eta=-\ln(1-\eta).
```

Because

```math
\lambda_N\sim\kappa_0N^\alpha,
```

the slow variable is `z=lambda_N t/N`. Hence

```math
\boxed{
T_N(\eta)
\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha}.
}
```

and

```math
\boxed{
\mu_N(\eta)
\sim\frac{d}{\kappa_0}[x_\eta-\eta]N^{2-\alpha}.
}
```

Therefore

```math
\boxed{
\alpha<\beta:
\quad T_N\asymp N^{1-\alpha},
\quad \mu_N\asymp N^{2-\alpha}.
}
```

The minimum gate is bounded only for `alpha>=1`; the accepted local-event burden is bounded only for `alpha>=2`.

---

# 3. Balanced sector: alpha = beta = s

Define

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0},
\quad
A=\kappa_0+\gamma_0,
\quad
\lambda_0=\frac{\kappa_0\gamma_0}{A}.
```

This line retains the Rev. 1 efficiency boundary.

## eta < q0

With

```math
x_\eta=-\ln(1-\eta/q_0),
```

```math
\boxed{T_N\sim(x_\eta/A)N^{-s}.}
```

Also

```math
\boxed{
\mu_N\sim\frac{d}{A}
\left[
\frac{q_0(1-q_0)}2x_\eta^2
+q_0^2x_\eta-q_0\eta
\right]N^{-s}.
}
```

## eta = q0

At the boundary,

```math
A N^s T_N
\sim
W\left(\frac{N}{(1-q_0)^2}\right)
```

at leading logarithmic scale. Robustly,

```math
\boxed{
T_N=\Theta(N^{-s}\ln N),
\qquad
\mu_N=\Theta[N^{-s}(\ln N)^2].
}
```

## eta > q0

Define

```math
L_\eta=\ln\frac{1-q_0}{1-\eta},
\qquad
H_\eta=L_\eta-\frac{\eta-q_0}{1-q_0}.
```

Then

```math
\boxed{
T_N\sim\frac{L_\eta}{\lambda_0}N^{1-s},
}
```

```math
\boxed{
\mu_N\sim\frac{dH_\eta}{\lambda_0}N^{2-s}.
}
```

The fixed-rate Rev. 1 theorem is exactly the slice `s=0`.

---

# 4. Complete phase diagram

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \mu_N\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}
\end{array}}
```

This separates branch selection from absolute scalability.

A bounded accepted local-event burden requires:

```text
alpha>beta:                  alpha >= 0
alpha=beta=s, eta<q0:        s >= 0
alpha=beta=s, eta=q0:        s > 0
alpha=beta=s, eta>q0:        s >= 2
alpha<beta:                  alpha >= 2
```

---

# 5. Illustrative consequences

### Collective extraction outruns fixed dephasing

For `alpha=1`, `beta=0`, every fixed `eta<1` eventually lies on the fast branch:

```math
T_N\sim N^{-1},
\qquad
\mu_N\sim N^{-1}.
```

Thus the fixed-rate `O(N^2)` behavior is not universal.

### Extraction and dephasing scale together

For `alpha=beta=1`, `q_0` remains fixed:

```text
eta<q0:  mu_N ~ N^-1
eta=q0:  mu_N ~ (ln N)^2/N
eta>q0:  mu_N ~ N
```

The efficiency boundary survives but its power laws shift.

### Dephasing outruns fixed extraction

For `alpha=0`, `beta>0`:

```math
T_N\sim N,
\qquad
\mu_N\sim N^2.
```

---

# 6. Interpretation and claim boundary

The existence of large-`N` sectors controlled by collective versus local rates is already established broadly in Dicke/superradiance theory. The detector-specific object here is narrower:

```text
fixed conditional internal efficiency eta
+ minimum gate selected by that eta
+ continuous extensive local event generation
-> accepted local-event burden phase diagram.
```

Do not claim a new generic decoherence-scaling transition.

The theorem assumes a symmetric Markovian bright manifold, polynomial rate scalings, fixed per-site local event rate, and the noninteracting independent-particle stochastic lift. It does not determine which exponents are physically achievable in a real detector or the thermodynamic cost of achieving large positive `alpha`.

The locally detailed-balanced `kT ln(mathcal C)` result remains a separate supporting resource caveat.

## Manuscript consequence

A Rev. 2 paper should present the Rev. 1 fixed-rate theorem as the `alpha=beta=0` slice of this broader phase diagram. The central object is now the joint efficiency/rate-scaling classification, not the static `1/N` projection or the fixed-rate quadratic law alone.
