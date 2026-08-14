# Agent recovery entrypoint

Read `AGENTS.md` first.

## Global user constraint — ANALYTICAL / THEORETICAL RESEARCH ONLY

The user cannot perform real-life experiments. All active research must be analytical/theoretical.

Allowed active work:
- first-principles derivations;
- exact toy models;
- mathematical bounds/invariants/no-go theorems;
- numerical thought experiments;
- analytical comparison with published theory;
- adversarial prior-art/novelty audits.

Do not make fabrication, sample procurement, measurement pilots, instrument choice, anneal schedules, device processing, or physical experiments the next research step. Older experimental-feasibility files are archived history only.

## Experiment 08 — ZERO-GAP KANE STATISTICS — CLOSED BY DEFAULT AS NOVELTY PATH

Branch: `experiment-08-zero-gap-kane-statistics`

Read in this order:

1. `experiments/08-zero-gap-kane-statistics/00_NOVELTY_STOP_2026-08-14.md`
2. `experiments/08-zero-gap-kane-statistics/FIRST_PRINCIPLES_ZERO_GAP_2026-08-14.md`
3. `experiments/08-zero-gap-kane-statistics/DOS_MISMATCH_ASYMPTOTIC_2026-08-14.md`
4. `experiments/08-zero-gap-kane-statistics/numerics/zero_gap_kane_statistics.py`

### Controlling question

HgCdTe has Kane edge electron mass approximately `m_e*=E_g/(2v^2)`. Naively substituting this into a parabolic/nondegenerate intrinsic-carrier formula predicts `n_i -> 0` as `E_g -> 0+`, which is qualitatively wrong at the massless-Kane transition.

### Minimal reduced model

Positive-gap Kane electron/light-hole dispersions:

```math
E_c(p)=\frac{E_g}{2}+\sqrt{(E_g/2)^2+v^2p^2},
```

```math
E_{lh}(p)=\frac{E_g}{2}-\sqrt{(E_g/2)^2+v^2p^2}.
```

Retain finite heavy-hole curvature

```math
E_{hh}(p)=-p^2/(2m_{hh})
```

because the exactly flat heavy-hole continuum is singular for thermodynamic state counting.

### Exact zero-gap result

At `E_g=0`, define `eta=mu/(kT)` and

```math
\Lambda=(2m_{hh}v^2/kT)^{3/2}.
```

Charge neutrality is

```math
2[I_2(\eta)-I_2(-\eta)]
=\Lambda I_{1/2}(-\eta).
```

For representative HgCdTe scales `v=1.07e6 m/s`, `m_hh=0.5m0`, `T=77 K`, the reduced model gives approximately

```text
eta ~5.308
mu ~35.2 meV
n_i(E_g=0) ~5.70e15 cm^-3.
```

Hence, for fixed `T>0`,

```math
\boxed{\lim_{E_g\to0+}n_i^{Kane}=n_0(T)>0}
```

while the naive parabolic formula gives zero.

### Noncommuting-limit / validity result

The edge-parabolic mass `m_e*=E_g/(2v^2)` assumes occupied kinetic energies much smaller than `E_g`. Sending `E_g->0` at fixed `T` violates the expansion before the limit is reached.

The simplest parabolic/nondegenerate intrinsic-Fermi construction becomes self-inconsistent when its predicted Fermi level reaches the conduction edge:

```math
\frac{E_g^*}{kT}
=\frac32W\left(\frac{4m_{hh}v^2}{3kT}\right).
```

For the representative 77-K model this gives `E_g^*~48.7 meV`. This boundary applies only to the simple edge-parabolic/nondegenerate derivation, not to full Kane calculations or empirical fits already encoding nonparabolicity/degeneracy.

### Zero-gap low-temperature asymptotic

At low `T`,

```math
\eta^3e^\eta
\simeq3\sqrt{\pi/2}(m_{hh}v^2/kT)^{3/2},
```

so

```math
\eta\simeq3W\left[\frac13\left(3\sqrt{\pi/2}(m_{hh}v^2/kT)^{3/2}\right)^{1/3}\right],
```

and

```math
\boxed{n_0(T)\sim T^3[\ln(T_0/T)]^3}
```

up to Lambert-W / `ln ln` corrections.

The reduced chemical potential `eta=mu/kT` diverges while the absolute chemical potential `mu` tends to zero from the conduction side.

### Generic DOS-mismatch theorem

For zero-gap power-law DOS

```math
g_e(E)=AE^a,\qquad g_h(E)=BE^b,
```

if `a=b`, then `eta` tends to a constant and `n_i~T^(a+1)`.

If `a>b`,

```math
n_i\sim T^{a+1}[\ln(T_0/T)]^{a+1},
```

with the mirror result for `b>a`.

HgCdTe corresponds to `a=2` for the massless Kane cone and `b=1/2` for a finite-curvature heavy-hole reservoir.

### Practical comparison

The familiar Hansen-Schmit `n_i` fit has the wrong mathematical zero-gap limit but remains numerically close surprisingly deep into the narrow-gap regime at 77 K in the reduced comparison. Order-one disagreement appears only at gaps of a few meV, corresponding to hundreds of micrometers cutoff wavelength.

### Strong prior art / novelty stop

Classic and modern HgCdTe theory already treats Kane carrier statistics:
- Schmit 1970 calculated intrinsic carrier concentration from Kane-model charge neutrality;
- Nemirovsky/Finkman and Hansen/Schmit refined/fit it;
- later formulas include nonparabolicity and degeneracy;
- full-band work computes Fermi levels, `n_i`, absorption and recombination lifetimes;
- massless Kane fermions and the zero-gap transition are established.

Thus the Lambert-W asymptotic and explicit validity warning are useful theory notes, but the major carrier-statistics problem is not new.

```text
Experiment 08 zero-gap paradox: RESOLVED
Lambert-W asymptotic: RETAIN
DOS-mismatch theorem: RETAIN
parabolic self-consistency boundary: RETAIN
finite-heavy-hole thermodynamic regularization: RETAIN
major novelty: NOT ESTABLISHED
Experiment 08 publication frontier: CLOSED BY DEFAULT
paper drafting: DO NOT BEGIN
```

## Experiment 07 — CLOSED

Isotope-tuned HgCdTe SRH theory was closed after adversarial audit. Retain the isotope-control, broadening, one-phonon, Laplace/cumulant, mode-rank, bandgap/isotope, phonon-edge and defect-population identities documented on `experiment-07-isotope-srh`, but do not reopen without a genuinely new theoretical ingredient.

## Other closed paths

- Experiment 06: SRH two-carrier provenance architecture closed by direct prior art.
- Experiment 05: active-volume/bandwidth theorem failed under arbitrary lossless matching.
- Experiment 04: passive nonreciprocal sensitivity path closed by trace bound.
- Experiment 03: passive photon-recycling cross-noise contains the same linear exchange information as deterministic response.
- Experiment 02: migrating-depth APD dominated by fixed-depth waveguide comparator.
- Experiment 01: equal-D* acquisition/information-spectrum path closed by established optimum-filter theory.

## Candidate screen retained

`candidate-screens/MASS_ASYMMETRY_JDOS_BOUND_2026-08-14.md` contains an exact reduced-mass / DOS inequality, but practical band-structure co-optimization is already established, so do not open it as an experiment.

## Next research rule

Return to premise generation. For every new theory-only photodetector Gedanken experiment:

1. keep the premise physically minimal;
2. identify the strongest theorem or prior architecture first;
3. search primary literature before long derivations;
4. stop immediately if the result reduces to established detailed balance, fluctuation-dissipation, standard generation-recombination theory, optimum filtering, Shockley-Ramo, standard avalanche theory, or another stronger framework;
5. open a new experiment branch only if the premise survives that screen.

Preserve negative results. Do not manufacture novelty.
