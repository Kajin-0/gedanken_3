# Response to external hostile review of PRA Rev. 4

**Date:** 2026-08-14  
**Disposition:** MAJOR REVIEW ACCEPTED / CENTRAL MATHEMATICS RETAINED / PRIMARY ASYMPTOTIC OBSERVABLE REFORMULATED / REV. 5 OPEN

The external hostile review judged the central one-excitation dynamics, eigenvalues, Table-I exponents, bounded-coupling proof, and reverse-gate scaling to be algebraically sound, but identified one potentially blocking asymptotic self-consistency issue: fixed per-site generation rate `d` plus `N->infinity` can leave a literal low-density many-particle regime on slow branches.

That objection is accepted. Rev. 5 does **not** defend the old wording.

---

# 1. Main repair — replace finite-d asymptotic theorem by dilute susceptibility

The primary internally generated false-event observable is now

```math
\boxed{
\chi_N(\eta)
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d
=N\int_0^{T_N(\eta)}C_{loc,N}(u)du.
}
```

The minimum gate remains

```math
T_N(\eta)=\inf\{t:C_{S,N}(t)\ge\eta\}.
```

This order of limits removes the inconsistency between a fixed finite generation rate and a slow lifetime that itself grows with `N`.

For an unsaturable independent-particle Poisson lift,

```math
\mu_{loc,N}(\eta;d)=d\chi_N(\eta),
```

but this is now explicitly a secondary kinetic realization, not the definition of the asymptotic theorem.

The detailed Table-I exponents are therefore stated for `chi_N`, not for a universal finite-density count process.

---

# 2. Finite-d mapping is now conditional

Rev. 5 explicitly states that the finite-rate Poisson identity is physically appropriate only when:

```text
- generated excitations are genuinely linear/unsaturable; or
- the considered N range remains sufficiently dilute that occupancy,
  blocking, interactions, heating, and shared reset are negligible.
```

The phrase `extensive low-density kinetic limit` is no longer used as though it remained uniformly valid for fixed `d` on every `N->infinity` slow branch.

---

# 3. Stronger robustness result — maximal one-event-per-site saturation

To test the opposite extreme, Rev. 5 introduces a model in which each microscopic site can generate **at most one event during a gate**.

If the first-event density at one site is `d exp(-d s)`, the expected accepted count is

```math
\mu_{1,N}(T)
=N\int_0^T d e^{-ds}C_{loc,N}(T-s)ds.
```

For any strict slow-recycling operating point,

```math
\mu_{1,N}(T_N)
\ge
N(1-e^{-dT_N/2})C_{loc,N}(T_N/2).
```

On the dephasing-dominated slow branch,

```math
C_{loc,N}(T_N/2)\to1-e^{-x_\eta/2}>0.
```

On the balanced supercritical branch,

```math
C_{loc,N}(T_N/2)\to1-e^{-L_\eta/2}>0.
```

Under the bounded-coupling class `0<=alpha<=1`, `T_N` is either bounded below by a positive constant or diverges on every strict slow branch. Therefore

```math
\boxed{
\mu_{1,N}(T_N)=\Theta(N).
}
```

This is important:

```text
Detailed N^(2-alpha) powers:
    model-specific to the unsaturable independent-particle lift.

Strict slow-branch divergence:
    survives even maximal per-site saturation.
```

So the no-go is more robust than the original finite-d derivation implied.

---

# 4. Explicit Lindblad generator added

Rev. 4 jumped too quickly to the closed `(P,b)` equations. Rev. 5 now starts from an enlarged Hilbert space containing counted sink `|c>`:

```math
\dot\varrho
=\kappa_N\mathcal D[|c\rangle\langle B|]\varrho
+\gamma_N\sum_j\mathcal D[|j\rangle\langle j|]\varrho,
```

with

```math
\mathcal D[L]\rho
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

Projecting onto the surviving excitation manifold gives

```math
\dot\rho
=-\frac{\kappa_N}{2}\{\Pi_B,\rho\}
+\gamma_N\sum_j\mathcal D[|j\rangle\langle j|]\rho.
```

Then

```math
\dot P=-\kappa_N b,
```

and exactly

```math
\dot b=-(\kappa_N+\gamma_N)b+\frac{\gamma_N}{N}P.
```

This fixes the dephasing-rate convention, demonstrates complete positivity through the enlarged Lindblad evolution, and shows why the hierarchy closes.

---

# 5. Asymptotic proof expanded

Appendix B no longer says only that results `follow` from rescaled times. It now explicitly derives the leading signal and local-event kernels in each sector.

## Extraction dominated: alpha > beta

With `v=kappa_N t`,

```math
C_{S,N}\to1-e^{-v},
```

```math
N C_{loc,N}\to1-e^{-v}.
```

Hence

```math
T_N\sim\frac{x_\eta}{\kappa_0}N^{-\alpha},
```

```math
\chi_N\sim\frac{x_\eta-\eta}{\kappa_0}N^{-\alpha}.
```

## Dephasing dominated: alpha < beta

With `z=kappa_N t/N`,

```math
C_{S,N}\to1-e^{-z},
```

```math
C_{loc,N}\to1-e^{-z}.
```

Thus

```math
T_N\sim\frac{x_\eta}{\kappa_0}N^{1-\alpha},
```

```math
\chi_N\sim\frac{x_\eta-\eta}{\kappa_0}N^{2-\alpha}.
```

## Balanced fast branch

With `A=kappa_0+gamma_0`, `q_0=kappa_0/A`, and `v=A N^s t`,

```math
C_{S,N}\to q_0(1-e^{-v}),
```

while

```math
N C_{loc,N}
\to q_0^2(1-e^{-v})+q_0(1-q_0)v.
```

This yields the previously retained finite coefficient for `chi_N`.

## Balanced slow branch

On `t=N^(1-s)y`,

```math
C_{S,N}\to1-(1-q_0)e^{-\lambda_0 y},
```

```math
C_{loc,N}\to1-e^{-\lambda_0 y}.
```

This yields `T_N~N^(1-s)` and `chi_N~N^(2-s)`.

## Balanced boundary

In the boundary layer `1 << v << N`, the fast deficit and first slow correction satisfy

```math
q_0 e^{-v}
\sim q_0(1-q_0)^2\frac{v}{N}.
```

Therefore

```math
v e^v\sim\frac{N}{(1-q_0)^2},
```

so

```math
v=\Theta(\ln N),
```

```math
T_N=\Theta(N^{-s}\ln N),
```

and because the local kernel is asymptotically linear in `v`,

```math
\chi_N=\Theta[N^{-s}(\ln N)^2].
```

---

# 6. Efficiency language tightened

The quantity

```math
\eta_{sc}
=\sup\{\eta:\chi_N(\eta)=O(1)\}
```

is now called a **bounded-response efficiency supremum**, not an operational detector efficiency ceiling.

The paper states explicitly:

> `O(1)` means nondivergent with system size. It does not imply a small or acceptable false-count probability.

A budgeted quantity is introduced for interpretation:

```math
\eta_{bud}(d,\mu_*)
=\sup\left\{\eta:
\limsup_{N\to\infty}d\chi_N(\eta)\le\mu_*
\right\},
```

within the range where the linear-response mapping is physically valid.

The budgeted quantity is defined but not optimized in Rev. 5.

---

# 7. Balanced boundary precision

Rev. 5 now states explicitly:

```text
alpha=beta=s=0, eta=q0:
    q0 is a supremum but is NOT attained,
    because chi_N(q0)=Theta[(ln N)^2].

alpha=beta=s>0, eta=q0:
    the boundary itself is bounded because
    N^(-s)(ln N)^2 -> 0.
```

---

# 8. Bounded-coupling no-go scope moved into the statement itself

The boxed no-go now reads explicitly:

```text
within the linear single-excitation resource class,
strict slow-recycling operation
-> chi_N = Omega(N).
```

This prevents the `Omega(N)` result from being quoted as a universal bound on arbitrary nonlinear many-body detectors.

---

# 9. Figure corrections

Figure 1 was redrawn again:

```text
- local event visibly decomposes into bright weight 1/N and dark weight 1-1/N;
- gamma_N is shown as the primitive dephasing process;
- r_- is labeled `effective slow eigenmode`;
- the caption explicitly states that r_- is not a microscopic return jump;
- gate definition and susceptibility are placed in a separate decision strip.
```

Figure 2 now plots `chi_N`, not a finite-d count mean.

Figure 3 is explicitly called a **scaling classification diagram** and its y axis is `bounded-response efficiency supremum`.

---

# 10. Thermodynamic section demoted

The reversible-extraction result is no longer a coequal main-text theorem. The main text gives only a brief contextual statement and sends the derivation to an appendix.

Its claim remains conditional on an assumed effective local-detailed-balance model.

---

# 11. Current disposition

```text
External hostile review of Rev. 4: ACCEPTED
central one-body algebra: RETAIN
fixed-d low-density asymptotic wording: REMOVED
primary observable: chi_N
explicit Lindblad generator: ADDED
Table-I derivation: EXPANDED
one-shot saturation robustness: ADDED
bounded-response interpretation: CLARIFIED
balanced supremum subtlety: CLARIFIED
Fig. 1 microscopic/eigenmode ambiguity: FIXED
thermodynamic result: DEMOTED TO APPENDIX
```

The paper path remains active.

The next adversarial question after Rev. 5 is no longer the fixed-d consistency objection. The main remaining significance risk is whether a PRA referee demands robustness to bounded heterogeneity (nonuniform optical couplings/dephasing or finite-rank bright subspaces) before accepting a symmetric-model theorem.
