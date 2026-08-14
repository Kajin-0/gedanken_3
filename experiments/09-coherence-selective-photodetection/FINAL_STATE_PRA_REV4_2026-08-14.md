# Final active state — Experiment 09 PRA Rev. 4

**Date:** 2026-08-14  
**Status:** **THEOREM/MANUSCRIPT FREEZE RECOMMENDED / FINAL RENDERED ADVERSARIAL REVIEW PASSES / NOVELTY NOT ESTABLISHED / SUBMISSION PRODUCTION IS THE NEXT PHASE**

This dated pointer supersedes earlier “next action = rendered review” language in recovery files.

## Active manuscript

> **Scalable internal-dark-count limits in a coherence-selective photodetector**

Target:

```text
Physical Review A — Regular Article
suggested section: A-3E Quantum Technologies
```

Read:

1. `PAPER_DRAFT_REV4_PRA_2026-08-14.md`
2. `PAPER_REV4_RENDERED_ADVERSARIAL_REVIEW_2026-08-14.md`
3. `SATURATING_SITE_ROBUSTNESS_2026-08-14.md`
4. `PAPER_REV4_PRA_RENDER_QA_2026-08-14.md`
5. `PAPER_REV4_REFERENCE_AUDIT_2026-08-14.md`
6. `SCALABLE_EFFICIENCY_CEILING_2026-08-14.md`
7. `RATE_SCALING_PHASE_DIAGRAM_2026-08-14.md`
8. `COLLECTIVE_EXTRACTION_RATE_BOUND_2026-08-14.md`
9. `GATED_REVERSE_INJECTION_PHASE_LAW_2026-08-14.md`.

## Headline theorem

For

```math
\kappa_N=\kappa_0N^\alpha,
\qquad
\gamma_N=\gamma_0N^\beta,
```

and bounded counted coupling per microscopic state, so `0<=alpha<=1`, define the supremum fixed conditional internal collection efficiency with bounded accepted local-dark burden:

```math
\eta_{sc}=\sup\{\eta\in(0,1):\mu_{loc,N}(\eta)=O(1)\}.
```

Then

```math
\boxed{
\eta_{sc}=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta.
\end{cases}}
```

Any operating point strictly requiring slow dark-manifold recycling has

```math
\boxed{\mu_{dark,N}=\Omega(N)}
```

under the bounded local-coupling resource.

## Important final modeling correction

The detailed power-law table

```text
N^{-alpha}, N^{-s}, N^{2-s}, N^{2-alpha}, etc.
```

is exact/asymptotic for the explicit **linear independent-particle unlimited-event Poisson reference model**.

Do not call those slow-branch powers universal many-body detector laws.

The headline ceiling/no-go is more robust. In the opposite maximally suppressive **one-event-per-site** saturation model,

```math
\mu_{sat,N}(T_N)
\ge
N(1-e^{-dT_N/2})C_{D,N}(T_N/2),
```

and every strict slow branch still has

```math
\mu_{sat,N}=\Omega(N).
```

Thus the bounded/unbounded efficiency classification survives site saturation even though the detailed divergent exponent changes (to `Theta(N)` in the one-shot reference).

## Corrected thermodynamic supporting result

For thermally reversible counted extraction at the same efficiency-selected gate, fixed affinity gives

```text
fast branch:          O(1) reverse burden
balanced boundary:    O(log N)
strict slow branch:   O(N)
```

The old blanket gated `kT ln(C)` statement is superseded.

## Rendered-paper status

The final corrected local PRA-style PDF is seven pages, two-column REVTeX, with three figures.

Final corrected PDF SHA-256:

```text
cfd6a4c0faab9034d2c755276add6979161b3466af40be4f2aac7db5b249052a
```

Final corrected local LaTeX SHA-256:

```text
ad443bf05c8ab8fb84328da57986058251581929b96ac2a679a9915d968d0568
```

Final internal checks:

```text
one-body mathematics: PASS
operational task definition: PASS
reference-model asymptotics: PASS WITH MODEL-SCOPE LABEL
saturation robustness of eta_sc: PASS
bounded-coupling no-go: PASS
gated reverse-injection law: PASS
citations/cross-references: PASS
figure QA: PASS
page-level PDF QA: PASS
novelty: NOT ESTABLISHED
significance: plausible for concise PRA Regular Article
```

## Closest prior-art boundary

The paper does not claim novelty for:

```text
coherent collective detector architectures;
bright/dark detector manifolds;
local-dephasing bright/dark transfer;
large-N collective/decoherence scaling regimes;
quantum-detector thermodynamic tradeoffs.
```

Young/Sarovar/Leonard 2020 remains the closest detector architecture; Bassler/Lyne/Cuerda 2026 remains the closest scaling-theory comparator.

Focused searches have not found the complete efficiency-selected internal-dark scalability theorem, but absence of a match is not proof of novelty.

## Next phase

**Freeze the theorem unless an external reviewer identifies a genuinely new defect.**

Do not open Experiment 10 merely to avoid submission uncertainty.

The remaining work is submission production:

1. author name(s), affiliation(s), corresponding email;
2. APS author declarations and final availability wording;
3. one last citation-network update immediately before submission, especially checking whether the 2026 Bassler preprint has journal metadata;
4. package the REVTeX source, final figure files, and numerical reproduction scripts;
5. submit to Physical Review A if the author elects to proceed.
