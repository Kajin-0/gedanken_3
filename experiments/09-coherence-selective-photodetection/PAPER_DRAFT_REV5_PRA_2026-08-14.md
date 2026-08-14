# Scalable internal false-count limits in a coherence-selective photodetector

**Target:** Physical Review A — Regular Article  
**Draft status:** Rev. 5 / major revision after external hostile review  
**Date:** 2026-08-14  
**Novelty status:** not established; no priority language authorized

## Abstract-level claim

A coherence-selective detector contains one optically bright excitation direction and a large internal dark manifold. Local dephasing reconnects those sectors. For each size `N`, choose the minimum gate `T_N(eta)` required to reach a prescribed conditional internal signal-collection efficiency.

The primary internally generated false-event observable is now the **dilute accepted-event susceptibility**

```math
\boxed{
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)du
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d.
}
```

This replaces the old fixed-`d`, `N->infinity` low-density formulation.

For

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
```

and bounded counted coupling per local state so `0<=alpha<=1`, define

```math
\eta_{sc}
=\sup\{\eta\in(0,1):\chi_N(\eta)=O(1)\}.
```

Then

```math
\boxed{
\eta_{sc}
=\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}}
```

`eta_sc` is a **bounded-response efficiency supremum**. `O(1)` means nondivergent with system size, not necessarily a small practical false-count probability.

Within the linear single-excitation resource class,

```math
\boxed{
\text{strict slow-recycling operation}
\Longrightarrow
\chi_N=\Omega(N).
}
```

The same slow-branch divergence survives a maximally saturating one-event-per-site model, where the accepted burden becomes `Theta(N)`.

---

# 1. Exact dynamical model

Bright state:

```math
|B\rangle=N^{-1/2}\sum_j|j\rangle.
```

Introduce counted sink `|c>` and local projectors

```math
P_j=|j\rangle\langle j|.
```

With

```math
\mathcal D[L]\rho
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
```

the enlarged Lindblad equation is

```math
\boxed{
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[P_j]\varrho.
}
```

Projecting back onto the surviving excitation manifold gives

```math
\dot\rho
=-\frac{\kappa_N}{2}\{\Pi_B,\rho\}
+\gamma_N\sum_j\mathcal D[P_j]\rho.
```

Define

```math
P=\operatorname{Tr}\rho,
\qquad
b=\langle B|\rho|B\rangle.
```

Exactly,

```math
\dot P=-\kappa_Nb,
```

because counted extraction removes trace, while

```math
\sum_j\langle B|P_j\rho P_j|B\rangle=P/N
```

and

```math
\frac12\sum_j\langle B|\{P_j,\rho\}|B\rangle=b.
```

Therefore

```math
\boxed{
\dot b
=-(\kappa_N+\gamma_N)b
+\frac{\gamma_N}{N}P.
}
```

and

```math
\boxed{
\ddot P
+(\kappa_N+\gamma_N)\dot P
+\frac{\kappa_N\gamma_N}{N}P=0.
}
```

The exact rates are

```math
r_{\pm,N}
=\frac{a_N\pm\sqrt{a_N^2-4\kappa_N\gamma_N/N}}2,
\qquad
a_N=\kappa_N+\gamma_N.
```

The slow eigenvalue is

```math
\boxed{
r_{-,N}
=\frac1N
\frac{\kappa_N\gamma_N}{\kappa_N+\gamma_N}
[1+O(N^{-1})].
}
```

This is an **emergent eigenmode**, not a primitive dark-to-bright jump.

For every `gamma_N>0`, both bright and local excitations are eventually counted. Coherence selectivity is therefore a finite-time resource.

---

# 2. Operational gate and dilute response

Photon-created state:

```math
b_0=1.
```

Uniform local internal event:

```math
b_0=1/N.
```

Let their collection kernels be

```math
C_{S,N}(t),
\qquad
C_{loc,N}(t).
```

Define the minimum gate

```math
\boxed{
T_N(\eta)
=\inf\{t:C_{S,N}(t)\ge\eta\}.
}
```

Then

```math
\boxed{
\chi_N(\eta)
=N\int_0^{T_N(\eta)}C_{loc,N}(u)du.
}
```

A finite-rate unsaturable independent-particle Poisson lift gives

```math
\mu_{loc,N}(\eta;d)=d\chi_N(\eta),
```

but only as a secondary kinetic realization.

For a practical dilute false-count budget `mu_*`, one can define

```math
\eta_{bud}(d,\mu_*)
=\sup\left\{\eta:
\limsup_{N\to\infty}d\chi_N(\eta)\le\mu_*
\right\},
```

when the linear-response mapping remains valid. Rev. 5 does not optimize this budgeted quantity.

---

# 3. Large-N scaling classification

```math
\boxed{
\begin{array}{c|c|c|c}
\text{rate sector} & \text{efficiency} & T_N & \chi_N\\
\hline
\alpha>\beta & \eta<1 & N^{-\alpha} & N^{-\alpha}\\
\alpha=\beta=s & \eta<q_0 & N^{-s} & N^{-s}\\
\alpha=\beta=s & \eta=q_0 & N^{-s}\ln N & N^{-s}(\ln N)^2\\
\alpha=\beta=s & \eta>q_0 & N^{1-s} & N^{2-s}\\
\alpha<\beta & \eta>0 & N^{1-\alpha} & N^{2-\alpha}
\end{array}}
```

where

```math
q_0=\frac{\kappa_0}{\kappa_0+\gamma_0}.
```

## Extraction dominated: alpha > beta

Let

```math
v=\kappa_Nt,
\qquad
x_\eta=-\ln(1-\eta).
```

Then

```math
C_{S,N}\to1-e^{-v},
```

```math
N C_{loc,N}\to1-e^{-v}.
```

Therefore

```math
T_N\sim\frac{x_\eta}{\kappa_0}N^{-\alpha},
```

```math
\boxed{
\chi_N\sim
\frac{x_\eta-\eta}{\kappa_0}N^{-\alpha}.
}
```

## Dephasing dominated: alpha < beta

Use

```math
z=\kappa_Nt/N.
```

After the fast transient,

```math
C_{S,N}\to1-e^{-z},
```

```math
C_{loc,N}\to1-e^{-z}.
```

Hence

```math
T_N\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha},
```

```math
\boxed{
\chi_N\sim
\frac{x_\eta-\eta}{\kappa_0}N^{2-\alpha}.
}
```

## Balanced: alpha=beta=s

Define

```math
A=\kappa_0+\gamma_0,
```

```math
q_0=\kappa_0/A,
```

```math
\lambda_0=\kappa_0\gamma_0/A.
```

On fast time `v=A N^s t`,

```math
C_{S,N}\to q_0(1-e^{-v}),
```

```math
N C_{loc,N}
\to q_0^2(1-e^{-v})+q_0(1-q_0)v.
```

For `eta<q_0`, with `x_eta=-ln(1-eta/q_0)`,

```math
T_N\sim\frac{x_\eta}{A}N^{-s},
```

```math
\chi_N\sim
\frac{N^{-s}}A
\left[
\frac{q_0(1-q_0)}2x_\eta^2
+q_0^2x_\eta-q_0\eta
\right].
```

For `eta>q_0`, on `t=N^(1-s)y`,

```math
C_{S,N}\to1-(1-q_0)e^{-\lambda_0y},
```

```math
C_{loc,N}\to1-e^{-\lambda_0y}.
```

Writing

```math
L_\eta=\ln\frac{1-q_0}{1-\eta},
```

```math
H_\eta=L_\eta-\frac{\eta-q_0}{1-q_0},
```

gives

```math
T_N\sim\frac{L_\eta}{\lambda_0}N^{1-s},
```

```math
\chi_N\sim\frac{H_\eta}{\lambda_0}N^{2-s}.
```

At the boundary `eta=q_0`, in the intermediate region `1<<v<<N`,

```math
q_0e^{-v}
\sim q_0(1-q_0)^2\frac vN.
```

Thus

```math
v e^v\sim\frac{N}{(1-q_0)^2},
```

so

```math
T_N=\Theta(N^{-s}\ln N),
```

```math
\boxed{
\chi_N=\Theta[N^{-s}(\ln N)^2].
}
```

---

# 4. Bounded microscopic coupling

For counted extraction matrix

```math
K=\sum_a|\ell_a\rangle\langle\ell_a|\ge0,
```

assume

```math
K_{jj}\le\kappa_{loc}
```

with `kappa_loc` independent of `N`.

Then

```math
\boxed{
\kappa(\psi)
\le\lambda_{max}(K)
\le\operatorname{Tr}K
\le N\kappa_{loc}.
}
```

Therefore

```math
\boxed{\alpha\le1}
```

within the **linear single-excitation resource class**.

This scope qualifier is part of the theorem, not merely a caveat after it.

---

# 5. Bounded-response efficiency supremum

Assume `0<=alpha<=1`.

```math
\boxed{
\eta_{sc}
=\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}}
```

Interpretation:

```text
alpha > beta:
    every fixed eta<1 has bounded dilute response;

alpha = beta:
    supremum is the fast branching fraction q0;

alpha < beta:
    no fixed positive eta has bounded dilute response.
```

Boundary precision:

```text
s=0, eta=q0:
    q0 is a supremum but NOT attained;
    chi_N ~ (ln N)^2 diverges.

s>0, eta=q0:
    q0 itself is bounded because
    N^(-s)(ln N)^2 -> 0.
```

---

# 6. Slow-branch no-go and saturation robustness

Within the linear single-excitation resource class,

```math
\boxed{
\text{strict slow recycling}
\Longrightarrow
\chi_N=\Omega(N).
}
```

Now impose the opposite of an unsaturable particle model: **one event maximum per site per gate**.

```math
\mu_{1,N}(T)
=N\int_0^T d e^{-ds}C_{loc,N}(T-s)ds.
```

Then

```math
\mu_{1,N}(T_N)
\ge
N(1-e^{-dT_N/2})C_{loc,N}(T_N/2).
```

For dephasing-dominated slow operation,

```math
C_{loc,N}(T_N/2)
\to1-e^{-x_\eta/2}>0.
```

For balanced supercritical slow operation,

```math
C_{loc,N}(T_N/2)
\to1-e^{-L_\eta/2}>0.
```

Therefore

```math
\boxed{
\mu_{1,N}(T_N)=\Theta(N).
}
```

So:

```text
Poisson independent-particle powers N^(2-alpha): MODEL-SPECIFIC.
Strict slow-branch divergence: ROBUST TO MAXIMAL PER-SITE SATURATION.
```

---

# 7. Supporting reversible-extraction result

The thermodynamic result is moved out of the main theorem and into an appendix.

Under the assumed effective local-detailed-balance model

```math
\bar\kappa_N
=\kappa_Ne^{-\Delta F_N/(kT)},
```

the efficiency-selected reverse contribution has fixed-affinity scaling

```text
fast branch:          O(1)
balanced boundary:    O(log N)
strict slow branch:   O(N)
```

This is supporting context and is explicitly not needed for the susceptibility theorem.

---

# 8. Figure / terminology changes

Rev. 5 reserves `dark manifold` for the coherent state-space sector and calls generated noise events `local internal events` or `false events`.

Symbols:

```text
rho_loc
C_loc,N
chi_N
```

replace the overloaded use of `rho_D`, `C_D`, and `dark` for both state-space and false-count concepts.

Figure 1 now:

```text
- separates local-event bright and dark weights;
- labels gamma_N as primitive local dephasing;
- labels r_- as an effective slow eigenmode;
- places the gate and chi_N definition in a distinct decision strip.
```

Figure 2 plots exact finite-`N` `chi_N` and calls itself a consistency illustration.

Figure 3 is a scaling classification diagram, not a continuous experimental phase curve.

---

# 9. Claim boundary

Established / adjacent:

```text
coherent collective detector architecture;
bright/dark state geometry;
local-dephasing mixing;
large-N collective/decoherence scaling;
quantum-detector thermodynamic tradeoffs.
```

The active claim is narrower:

> An efficiency-selected gate converts imperfect dark-state isolation into a size-dependent dilute internal-false-event susceptibility. Under bounded local counted coupling, strict slow-recycling operation has an unavoidable divergent internal response, while the bounded-response efficiency supremum is controlled by the relative scaling of extraction and dephasing.

Same-mode optical background and bright-aligned correlated internal baths remain outside the rejection theorem.

Novelty remains unestablished pending final external/citation-network audit.
