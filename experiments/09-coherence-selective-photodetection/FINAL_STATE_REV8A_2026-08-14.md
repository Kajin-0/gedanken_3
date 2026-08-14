# Final state pointer — Experiment 09 PRA Rev. 8a

**Date:** 2026-08-14

This file supersedes older recovery notes whenever they disagree with it.

## Active manuscript

**Scaling of internal false-event susceptibility in a coherence-selective photodetector**

Target: Physical Review A Regular Article.

## Primary observable

```math
\chi_N(\eta)=N\int_0^{T_N(\eta)}C_{loc,N}(u)\,du
=\lim_{d\to0}\frac{\mu_{loc,N}(\eta;d)}d.
```

For the dilute independent Poisson realization,

```math
\mu_N=d\chi_N,
```

and the correct false-alarm expansion is

```math
\boxed{
P_{FA}=1-e^{-d\chi_N}
=d\chi_N+O(d^2\chi_N^2).
}
```

Do **not** use the abbreviated `O(d^2)` remainder from older Rev. 8 recovery notes.

## Headline scaling result

For fixed `N`-independent exponents

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
\qquad
\kappa_0,\gamma_0>0,
```

and bounded microscopic counted coupling implying `alpha<=1`,

```math
\eta_{sc}=\begin{cases}
1,&\alpha>\beta,\\
\kappa_0/(\kappa_0+\gamma_0),&\alpha=\beta,\\
0,&\alpha<\beta.
\end{cases}
```

For any fixed target efficiency strictly in a slow-recycling sector,

```math
\chi_N=\Omega(N)
```

within the linear single-excitation resource class.

## Figure state

- Fig. 1: sparse two-panel Rev. 8 layout; do not add text back onto transition lines.
- Fig. 2 parameters: `kappa_0=10`, `gamma_0=1`, `q_0=10/11`; the `eta=.50` balanced-fast curve is strictly subcritical.
- Fig. 3: scaling-classification diagram unchanged.

## Current review disposition

Latest hostile re-review: **ready**, modulo the false-alarm remainder precision fix and actual author metadata at submission. The remainder fix is complete in Rev. 8a.

## Remaining work

1. Insert real author name, affiliation, corresponding email, and any required APS metadata.
2. Perform a final citation-network freshness check immediately before submission.
3. Prepare/finalize PRA submission declarations and cover letter.

Do not open Experiment 10 or add new theory unless a concrete external scientific blocker appears.

See `PAPER_REV8A_FINAL_PRECISION_PATCH_2026-08-14.md` for the production record and hashes.
