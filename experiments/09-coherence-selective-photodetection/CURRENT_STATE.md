# Current State — Experiment 09: Coherence-Selective Photodetection

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** ACTIVE / FOUR CONNECTED EXACT RESULTS RETAINED / ONE-PORT ASSUMPTION REMOVED / PAPER-LEVEL NOVELTY AUDIT IS NOW THE NEXT GATE

## Minimal Gedanken premise

A photon-created event and a dark event are forced to have identical populations in an `N`-dimensional degenerate excitation manifold. The photon creates a coherent pure bright state

```math
|B\rangle=\sum_j\sqrt{w_j}e^{i\phi_j}|j\rangle,
```

while the dark process creates its completely dephased population-matched state

```math
\rho_D=\sum_jw_j|j\rangle\langle j|.
```

Thus energy, carrier number, and every observable diagonal in the microscopic basis are exactly unable to distinguish them. Only coherence differs.

Read in order:

1. `FIRST_PRINCIPLES_BRIGHT_STATE_DISCRIMINATION_2026-08-14.md`
2. `DEPHASING_EXTRACTION_AND_DETAILED_BALANCE_2026-08-14.md`
3. `CRITICAL_COUPLING_THERMAL_REVERSE_COST_2026-08-14.md`
4. `GENERAL_PASSIVE_EXTRACTION_AFFINITY_BOUND_2026-08-14.md`

---

## Result 1 — exact zero-signal-loss dark leakage

For the ideal coherent readout

```math
\Pi_B=|B\rangle\langle B|,
```

signal acceptance is

```math
\eta_\gamma=1,
```

while matched incoherent dark acceptance is

```math
\boxed{
\epsilon_D=\sum_jw_j^2=1/N_{eff},
\qquad
N_{eff}=1/\sum_jw_j^2.
}
```

Among all POVM elements constrained to accept the photon state with probability one, `Pi_B` minimizes dark acceptance.

For general dark-generation covariance

```math
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|,
```

and optical coupling vector `g`, the accepted internal dark-generation rate is

```math
\boxed{
\Gamma_D^B
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

For independent identical local dark channels, `D=dI`, so

```math
\boxed{\Gamma_D^B=d}
```

independent of the number of participating sites even though raw internal dark generation scales as `Nd`.

Thermal/background photons in the same accepted optical mode create the same bright state and are not rejected.

Generic state-verification mathematics is established; the detector specialization is the object of the current novelty audit.

---

## Result 2 — exact finite-time theorem under local dephasing

For uniform bright state, bright extraction rate `kappa`, and independent local pure-dephasing rate `gamma`, surviving excitation probability `P` and bright population `b` obey

```math
\dot P=-\kappa b,
```

```math
\dot b=-(\kappa+\gamma)b+(\gamma/N)P.
```

Hence

```math
\ddot P+(\kappa+\gamma)\dot P+(\kappa\gamma/N)P=0,
```

with exact rates

```math
r_\pm
=\frac{\kappa+\gamma
\pm\sqrt{(\kappa+\gamma)^2-4\kappa\gamma/N}}2.
```

For every `gamma>0`, both signal and initially dark excitations are eventually extracted:

```math
C_S(\infty)=C_D(\infty)=1.
```

Therefore coherence selectivity is a finite-decision-window resource, not permanent rejection.

For large `N`,

```math
\boxed{
r_-\simeq\frac{\kappa\gamma}{N(\kappa+\gamma)},
\qquad
\tau_{leak}\simeq N(1/\kappa+1/\gamma).
}
```

High fast-window photon collection requires `kappa >> gamma`.

---

## Result 3 — one-port critical-coupling result retained as a special case

For a one-port resonant model,

```math
\eta=4\Gamma\kappa/(\Gamma+\kappa)^2.
```

If collective optical coupling gives `Gamma=N gamma_o`, unit absorption requires `kappa=N gamma_o`.

For a thermally reversible counted extractor,

```math
\kappa_{rev}/\kappa=e^{-\Delta F/(kT)},
```

so keeping the reverse bright-aligned floor fixed gives

```math
\Delta F_{extra}=kT\ln N.
```

This result is now superseded in generality by Result 4 below, but remains a useful concrete realization.

---

## Result 4 — generalized passive-extraction affinity bound

For arbitrary parallel stationary counted channels `a` satisfying local detailed balance,

```math
\bar\kappa_a/\kappa_a=e^{-\beta\Delta F_a},
```

let

```math
K_\to=\sum_a\kappa_a,
\qquad
K_\leftarrow=\sum_a\bar\kappa_a.
```

With forward weights `p_a=\kappa_a/K_\to`, exactly

```math
\boxed{
\frac{K_\leftarrow}{K_\to}
=\sum_a p_a e^{-\beta\Delta F_a}
=e^{-\beta\Delta F_{eff}}.
}
```

Thus

```math
\boxed{
\Delta F_{eff}
=-kT\ln\left(\sum_a p_a e^{-\beta\Delta F_a}\right).
}
```

and

```math
\min_a\Delta F_a
\le\Delta F_{eff}
\le\sum_a p_a\Delta F_a
\le\max_a\Delta F_a.
```

So many passive pathways and affinity heterogeneity do not beat the best microscopic suppression; at fixed mean affinity, heterogeneity worsens reverse suppression.

If useful counted extraction is collectively enhanced by a factor

```math
K_\to(N)=\mathcal C(N)K_\to(1),
```

then holding the reverse bright-injection coefficient fixed requires

```math
\boxed{
\Delta F_{eff}(N)-\Delta F_{eff}(1)
\ge kT\ln\mathcal C(N).
}
```

The earlier `kT ln N` result is only the special case `mathcal C=N`.

Equivalent no-go form: if every microscopic channel has `Delta F_a<=Delta F_max`,

```math
\boxed{
K_\leftarrow
\ge K_\to e^{-\beta\Delta F_{max}}.
}
```

Therefore a collective increase of the forward counted rate necessarily appears in the reverse coefficient unless the available thermodynamic affinity grows.

### Hidden passive-state network

For an equilibrium detailed-balanced Markov network, Gibbs symmetrization makes the generator symmetric. Eliminating arbitrary hidden intermediate states by the quasistatic Schur complement preserves that symmetry and therefore preserves effective boundary detailed balance:

```math
\boxed{
\pi_iK_{i\to j}^{eff}
=\pi_jK_{j\to i}^{eff}.
}
```

Passive intermediate-state complexity therefore cannot create an equilibrium one-way counted transition.

---

# Combined scalability statement

The current detector-specific candidate can now be stated compactly:

```text
coherent optical excitation
+ incoherent local internal dark generation
-> bright projection prevents accepted internal dark rate from scaling with site number;

but

collectively enhanced stationary counted extraction
+ local detailed balance
-> bounded reverse bright dark floor requires extra affinity >= kT ln(mathcal C).
```

This gives a three-way scaling constraint:

```text
A. increasing collective useful extraction;
B. bounded thermodynamic affinity;
C. bounded thermally reversed bright dark floor.
```

All three cannot remain scale-independent within the theorem class.

At 77 K, `mathcal C=N` gives approximately

```text
N=10:    15.28 meV
N=100:   30.56 meV
N=1000:  45.84 meV
```

of additional effective affinity.

---

## Escape classes still outside the theorem

1. **Static nonreciprocity / broken microscopic time reversal.** Pairwise local detailed balance can fail even at thermal equilibrium in nonreciprocal many-body systems; global second-law/fluctuation constraints remain. This needs separate treatment if it is to be used as an escape.
2. **Time modulation / active gain / maintained nonequilibrium reservoirs / chemical bias.** These explicitly supply work or free energy and are outside the passive stationary theorem.
3. **Strongly non-Markovian transient storage.** May delay reverse injection rather than eliminate long-time return; not covered by the effective-rate bound.

Do not silently claim these are impossible.

---

## Prior-art status after the generalized theorem

Primary sources screened in this step establish the individual neighboring structures:

- local detailed balance and its coarse-graining behavior;
- quantum detailed balance/KMS thermalization;
- collectively enhanced reservoir-coupled currents/noise/entropy production;
- collective electronic transport in quantum infrared detectors;
- reciprocal and nonreciprocal thermal transport constraints.

No direct source found in the focused search states the complete detector-specific chain

```text
coherent bright-state projection suppresses local incoherent internal-dark scaling
+
collective counted-rate enhancement mathcal C
+
local detailed balance

-> extra effective affinity >= kT ln mathcal C for bounded reverse bright dark floor.
```

Absence of a hit is not proof of novelty.

---

## Current research decision

Experiment 09 has now accumulated enough connected analytical structure that continuing to add arbitrary device detail would be the wrong next move.

```text
minimal Gedanken premise: SHARP
static state-discrimination result: EXACT
finite-time dephasing result: EXACT IN REDUCED MODEL
one-port thermodynamic result: EXACT SPECIAL CASE
general parallel-channel affinity theorem: EXACT UNDER LDB
equilibrium hidden-state escape: CLOSED IN MARKOV REDUCTION
paper-level coherent story: PRESENT
novelty/significance: NOT YET ESTABLISHED
```

## Next gate

Perform a **paper-level closest-prior-art audit of the combined claim**, not another generic screen.

Specifically:

1. search for photodetector / quantum-sensor work that explicitly uses the coherence of the photon-created material excitation to reject incoherent internal dark-generation events with identical populations;
2. search for an existing theorem directly linking collective useful conversion enhancement to reverse detector noise/dark rate through a logarithmic thermodynamic-affinity cost;
3. test whether the combination is merely a transparent application of standard state discrimination + detailed balance or whether the detector-specific synthesis yields a genuinely nontrivial research contribution;
4. if no direct stronger result is found, begin manuscript architecture immediately and use a hostile referee-style review as the next research stress test rather than opening Experiment 10.
