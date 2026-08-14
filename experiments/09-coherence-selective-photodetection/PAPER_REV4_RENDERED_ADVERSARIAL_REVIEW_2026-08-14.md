# Final adversarial review — rendered Experiment 09 Rev. 4

**Date:** 2026-08-14  
**Target:** seven-page PRA-style rendered Rev. 4  
**Disposition:** **PASS FOR SCIENTIFIC/MANUSCRIPT FREEZE AT CURRENT INTERNAL REVIEW LEVEL / ONE MODEL-SCOPE DEFECT FOUND AND REPAIRED / NOVELTY NOT ESTABLISHED**

## 1. Review posture

This pass reviewed the actual two-column rendered manuscript rather than the derivation notes or Markdown source. It checked the scientific story as a skeptical Physical Review A referee would encounter it:

```text
closest prior art;
model definitions;
operational efficiency task;
rate-scaling theorem;
bounded-coupling resource assumption;
scalable-efficiency ceiling;
thermodynamic supporting result;
figure semantics;
claim boundaries.
```

No attempt was made to preserve a preferred theorem if the rendered paper exposed a stronger objection.

---

## 2. Substantive defect found — the phrase “low-density kinetic limit” was too broad

Rev. 4 originally described the independent-particle Poisson lift as an extensive low-density kinetic limit.

That wording is not uniformly defensible on a strict slow-recycling branch. There,

```math
T_N\sim N^{1-\alpha}
```

(or `N^{1-s}` on the balanced supercritical branch), so at fixed per-site event rate `d` the expected number of generation opportunities per site can itself grow with `N`.

Thus the exact slow-branch laws

```math
\mu_{loc,N}\sim N^{2-\alpha}
```

or

```math
\mu_{loc,N}\sim N^{2-s}
```

should be understood as properties of the explicit **linear independent-particle unlimited-event reference model**, not as universal many-body detector exponents.

This was a real claim-scope defect and was repaired in the rendered manuscript.

---

## 3. Adversarial saturation test

To test whether the paper's headline theorem depended on unlimited repeated generation at a microscopic site, the opposite limiting model was constructed:

```text
one microscopic site;
first dark event occurs at rate d;
after the first event, that site is completely saturated for the rest of the gate;
at most one accepted dark event per site.
```

The expected accepted dark count is

```math
\mu_{sat,N}(T)
=N\int_0^T d e^{-ds}C_{D,N}(T-s)\,ds.
```

It obeys

```math
\mu_{sat,N}(T)\le\mu_{Pois,N}(T),
```

so every fast-branch operating point that has bounded Poisson burden remains bounded under one-shot saturation.

For any **strict slow-recycling** operating point, restrict to sites generating during the first half of the gate:

```math
\boxed{
\mu_{sat,N}(T_N)
\ge
N(1-e^{-dT_N/2})C_{D,N}(T_N/2).
}
```

Under bounded local counted coupling, `alpha<=1`. On every strict slow branch:

- `T_N` either diverges or approaches a positive constant;
- `C_{D,N}(T_N/2)` approaches a positive constant.

Therefore

```math
\boxed{
\mu_{sat,N}(T_N)=\Omega(N).
}
```

Since the one-shot model also has `mu_sat,N<=N`, its strict slow-branch burden is `Theta(N)`.

This establishes that the **detailed superlinear Poisson exponents are model-specific, but the bounded/unbounded distinction defining the scalable-efficiency ceiling survives maximal one-shot site saturation.**

Full derivation:

`SATURATING_SITE_ROBUSTNESS_2026-08-14.md`.

---

## 4. Strengthened headline claim after repair

The manuscript may continue to use the independent-particle Poisson lift for exact coefficients and the detailed asymptotic table, provided it labels those powers as reference-model results.

The stronger detector statement is the robust one:

> With bounded counted coupling per microscopic state, any fixed operating point that strictly requires slow dark-manifold recycling has an accepted internal-dark burden that diverges at least linearly with the number of microscopic dark-generation sites, even in a maximally suppressive one-event-per-site saturation model.

The scalable internal-efficiency ceiling therefore survives:

```math
\boxed{
\eta_{sc}=
\begin{cases}
1,&\alpha>\beta,\\[4pt]
\dfrac{\kappa_0}{\kappa_0+\gamma_0},&\alpha=\beta,\\[10pt]
0,&\alpha<\beta,
\end{cases}}
```

under the stated bounded-resource assumptions.

This is more defensible than the pre-review interpretation.

---

## 5. Other technical checks

### Exact one-body dynamics

No defect found in

```math
\dot P=-\kappa_N b,
```

```math
\dot b=-(\kappa_N+\gamma_N)b+(\gamma_N/N)P,
```

or the resulting two-rate solution and `1/N` slow-recycling eigenvalue.

**PASS.**

### Rate-scaling classification

No contradiction found in the fast, balanced, or dephasing-dominated asymptotic sectors for the explicit independent-particle reference model.

**PASS WITH MODEL-SCOPE LABEL.**

### Bounded-local-coupling theorem

For positive extraction matrix `K`,

```math
\kappa_B\le\lambda_{max}(K)\le\operatorname{Tr}K\le N\kappa_{loc}
```

is correct and gives `alpha<=1` under the stated microscopic resource bound.

**PASS.**

### Gated reverse-injection law

The corrected branch-dependent result remains internally consistent:

```text
fast branch:          O(1)
balanced boundary:    O(log N)
strict slow branch:   O(N)
```

at fixed effective affinity. The older blanket gated `kT ln C` statement is not revived.

**PASS AS SUPPORTING RESULT.**

---

## 6. Prior-art disposition

The manuscript now correctly treats as established:

```text
coherent collective detector elements;
coherence/backaction detector optimization;
bright/dark manifolds;
dark-to-optically-active isolation as an ideal detector condition;
local-dephasing bright/dark transfer;
collective/decoherence large-N scaling regimes;
quantum-detector thermodynamic tradeoffs.
```

The closest detector comparator remains Young, Sarovar, and Leonard 2020. The closest scaling comparator remains Bassler, Lyne, and Cuerda 2026.

The surviving contribution is therefore narrow: a detector-operational efficiency-selected internal-dark scalability theorem plus bounded-resource no-go.

No direct stronger match has been found in the focused audit, but **novelty remains unestablished**.

---

## 7. Rendered-manuscript QA after the scientific repair

The corrected PDF remains seven pages in two-column REVTeX/PRA format.

Final post-repair checks:

```text
citations resolved: PASS
cross-references resolved: PASS
all 3 figures present: PASS
page-level visual QA: PASS
no clipping/overflow: PASS
PDF preflight: PASS
```

The only remaining REVTeX message is a benign deferred-float placement warning; all floats are visibly present and correctly placed.

Final corrected PDF SHA-256:

```text
cfd6a4c0faab9034d2c755276add6979161b3466af40be4f2aac7db5b249052a
```

Final corrected local LaTeX SHA-256:

```text
ad443bf05c8ab8fb84328da57986058251581929b96ac2a679a9915d968d0568
```

These hashes supersede the pre-saturation-repair hashes recorded in the earlier render-QA checkpoint.

---

## 8. Final internal referee disposition

```text
CORE ONE-BODY MATHEMATICS: PASS
OPERATIONAL DETECTOR TASK: PASS
INDEPENDENT-PARTICLE EXACT POWERS: PASS AS REFERENCE-MODEL RESULTS
LOW-DENSITY UNIVERSALITY LANGUAGE: FAILED AND REPAIRED
ONE-SHOT SATURATION ROBUSTNESS OF ETA_SC: PASS
BOUNDED-COUPLING NO-GO: PASS
GATED THERMODYNAMIC SUPPORTING RESULT: PASS
FIGURES/RENDER: PASS
PRIOR-ART HONESTY: PASS
NOVELTY: NOT ESTABLISHED
SIGNIFICANCE: PLAUSIBLE FOR A CONCISE PRA REGULAR ARTICLE
```

## 9. Recommended stopping point

**Freeze the theorem unless an external reviewer identifies a genuinely new scientific defect.**

The rational next work is submission production:

1. author name(s), affiliation(s), corresponding email;
2. final APS-required author declarations/data/code availability wording;
3. one last citation-network check immediately before submission, especially for the 2026 Bassler preprint;
4. package the REVTeX source, three figure files, and reproducibility scripts;
5. submit to Physical Review A if the author elects to proceed.

Do not open Experiment 10 merely to avoid submission-stage uncertainty.
