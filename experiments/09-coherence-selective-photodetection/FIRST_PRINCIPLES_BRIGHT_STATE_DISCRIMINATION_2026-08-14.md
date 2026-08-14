# Experiment 09 — Coherence-Selective Photodetection from First Principles

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Status:** ACTIVE PROVISIONAL / FIRST THEOREM DERIVED / NOVELTY NOT ESTABLISHED

## 1. Minimal Gedanken experiment

Construct an excited-state manifold with orthonormal states

```math
|1\rangle,\ldots,|N\rangle
```

and one ground state `|g>`. Take the excited states to be exactly degenerate in the minimal model so that energy discrimination is impossible.

A photon in one accepted optical mode couples the ground state to one coherent bright superposition

```math
|B\rangle
=\sum_{j=1}^{N}\sqrt{w_j}e^{i\phi_j}|j\rangle,
\qquad
w_j\ge0,
\qquad
\sum_j w_j=1.
```

Conditioned on absorption of one photon, the material state is

```math
\rho_\gamma=|B\rangle\langle B|.
```

Now choose the dark-generation process adversarially so that it creates **exactly the same populations in every microscopic state**, but no phase coherence:

```math
\rho_D
=\sum_{j=1}^{N}w_j|j\rangle\langle j|.
```

Thus signal and dark event have identical energy, carrier number, and basis-state populations. The only difference is the off-diagonal coherence created by optical absorption.

The question is:

> Can an ideal detector extract the optically prepared coherent state while rejecting the population-identical incoherent dark state?

This premise deliberately removes ordinary energy, momentum-population, charge, and rate discrimination.

---

## 2. Population observables are exactly blind

For any observable diagonal in this microscopic basis,

```math
O=\sum_j o_j|j\rangle\langle j|,
```

one has

```math
\operatorname{Tr}(O\rho_\gamma)
=\operatorname{Tr}(O\rho_D)
=\sum_j o_jw_j.
```

Therefore no measurement that sees only the populations can distinguish the photon-created event from the dark event.

This is an exact state-level construction, not an SNR approximation.

---

## 3. Coherent bright-state projection

Consider the ideal yes/no readout

```math
\Pi_B=|B\rangle\langle B|.
```

The photon event is accepted with probability

```math
\boxed{\eta_\gamma=\operatorname{Tr}(\Pi_B\rho_\gamma)=1.}
```

The incoherent dark event is accepted with probability

```math
\boxed{
\epsilon_D
=\operatorname{Tr}(\Pi_B\rho_D)
=\sum_j w_j^2.
}
```

Define the effective coherence dimension

```math
\boxed{
N_{\rm eff}
=\frac{1}{\sum_j w_j^2}.
}
```

Then

```math
\boxed{\epsilon_D=1/N_{\rm eff}.}
```

For a uniform bright state,

```math
w_j=1/N,
```

so

```math
\boxed{
\eta_\gamma=1,
\qquad
\epsilon_D=1/N.
}
```

The **conditional** rejection factor is therefore exactly `N`.

A useful information-theoretic identity is

```math
N_{\rm eff}
=\frac1{\operatorname{Tr}(\rho_D^2)}
=e^{S_2(\rho_D)},
```

where `S_2` is the second Renyi entropy. In this deliberately matched-population Gedanken experiment, the ideal dark-rejection factor equals the effective Hilbert-space dimension occupied incoherently by the dark event.

---

## 4. Zero-signal-loss optimality theorem

Let `E` be any physically allowed yes/no POVM element,

```math
0\le E\le I,
```

and require perfect acceptance of the photon state:

```math
\operatorname{Tr}(E\rho_\gamma)=1.
```

Because the expectation value reaches the maximum allowed eigenvalue, `|B>` must be a unit-eigenvalue eigenvector of `E`. Hence

```math
E=\Pi_B+E_\perp,
\qquad
E_\perp\ge0.
```

Therefore

```math
\operatorname{Tr}(E\rho_D)
\ge
\operatorname{Tr}(\Pi_B\rho_D)
=\sum_jw_j^2.
```

Thus

```math
\boxed{
\epsilon_{D,\min}(\eta_\gamma=1)
=\sum_j w_j^2
=1/N_{\rm eff}.
}
```

The bright-state projector is not merely one possible readout. It is the optimal quantum measurement among all measurements that retain unit signal acceptance.

This is mathematically a specialization of established quantum-state-discrimination/state-verification theory; the generic measurement theorem is not claimed as new.

For the uniform case `rho_D=I_N/N`, the same projector is also the equal-prior Helstrom measurement. The minimum classification error is

```math
\boxed{P_e=1/(2N).}
```

---

## 5. Dephasing destroys exactly the resource being used

Apply uniform pure dephasing that leaves all populations fixed but multiplies every off-diagonal element by

```math
c(t)=e^{-t/T_2}.
```

Then

```math
\rho_\gamma(t)
=c(t)\rho_\gamma+[1-c(t)]\rho_D.
```

The same bright-state readout gives

```math
\boxed{
\eta_\gamma(t)
=\frac1{N_{\rm eff}}
+\left(1-\frac1{N_{\rm eff}}\right)e^{-t/T_2}.
}
```

while the matched incoherent dark state remains at

```math
\epsilon_D=1/N_{\rm eff}.
```

Hence the instantaneous signal/dark acceptance ratio is

```math
\boxed{
\mathcal G(t)
=1+(N_{\rm eff}-1)e^{-t/T_2}.
}
```

The entire advantage disappears continuously as coherence is lost.

To retain a target discrimination factor `G>1`, the coherent projection must occur by

```math
\boxed{
t\le T_2\ln\left(\frac{N_{\rm eff}-1}{G-1}\right).}
```

Example for `N_eff=100`:

```text
t=0       -> G=100
t=T2      -> G=37.42
t=2 T2    -> G=14.40
t=3 T2    -> G=5.93
```

Thus a large coherence dimension is useless if the readout acts only after full dephasing.

---

## 6. Critical correction: conditional rejection is not absolute 1/N dark-rate scaling

Suppose there are `N` independent, equivalent local dark-generation channels, each with physical event rate `d`:

```math
L_j=\sqrt d\,|j\rangle\langle g|.
```

The total raw dark-event rate is

```math
\Gamma_D^{raw}=Nd.
```

Conditioned on a dark event, the excited state is `I_N/N`, so the bright projection accepts only `1/N` of them. Therefore the **absolute accepted dark-event rate** is

```math
\boxed{
\Gamma_D^{B}=Nd\times\frac1N=d.
}
```

This is an essential correction:

```text
conditional dark leakage -> 1/N
number of local dark sources -> N
accepted absolute dark rate -> one local-channel rate
```

The coherent filter does not make the dark rate vanish as `N->infinity`. It prevents the accepted dark rate from growing with the number of independent local dark-generating degrees of freedom.

Meanwhile a common optical mode can couple coherently to all `N` constituents, so its squared collective coupling can scale as

```math
G_{opt}^2=\sum_j|g_j|^2.
```

For equivalent `g_j=g`, this is `N|g|^2`. Whether this produces a genuine detector-performance scaling advantage after optical sum rules, extraction thermodynamics, and passive-resource accounting is the next hard question; it is **not** assumed here.

---

## 7. General dark-generation covariance theorem

Do not assume dark generation is necessarily diagonal. Let independent bath jump channels have excitation vectors `l_alpha` in the excited manifold:

```math
L_\alpha
=|l_\alpha\rangle\langle g|.
```

Define the positive dark-generation matrix

```math
\boxed{
D=\sum_\alpha|l_\alpha\rangle\langle l_\alpha|.
}
```

Its trace is the total dark-generation rate from `|g>` in this reduced jump model:

```math
\Gamma_D^{raw}=\operatorname{Tr}D.
```

Let the optical coupling vector be `g` and

```math
|B\rangle=|g\rangle/\|g\|
```

(where here bold/vector `g` denotes the optical coupling vector, not the ground-state ket). The bright-selective accepted dark rate is exactly

```math
\boxed{
\Gamma_D^B
=\langle B|D|B\rangle
=\frac{g^\dagger Dg}{g^\dagger g}.
}
```

Hence coherence-selective dark rejection is fundamentally an **alignment problem in excitation Hilbert space**.

The exact bounds are

```math
\boxed{
\lambda_{min}(D)
\le\Gamma_D^B\le
\lambda_{max}(D).
}
```

Special cases:

```text
D = d I                  -> Gamma_D^B = d
D proportional |B><B|    -> no coherence-selective rejection
D|B> = 0                 -> perfect rejection of that dark bath
```

Therefore there is no universal `N` advantage. The advantage exists only when optical excitation is more coherent/collective than the relevant nonradiative dark-generation covariance.

This general form also protects the analysis against the known fact that incoherent reservoirs can generate excited-state coherences when their transition operators are correlated.

---

## 8. Radiative-background no-go

A thermal/background photon arriving in the **same accepted optical mode** couples through the same optical vector and prepares the same bright excitation as the desired photon.

Therefore an internal bright-state projector cannot distinguish

```text
desired photon from accepted optical mode
```

from

```text
thermal/background photon in that same optical mode.
```

Thus coherence-selective internal readout cannot beat the irreducible photon-background floor of the accepted optical modes. Its possible benefit is restricted to **nonradiative or differently correlated internal dark-generation channels**.

This prevents the Gedanken result from being misrepresented as a universal zero-dark-count detector.

---

## 9. Prior-art kill test — current status

The ingredients are individually established:

1. Quantum hypothesis testing / state verification already determines optimal measurements for discriminating pure and mixed quantum states.
2. Dicke bright/dark collective states and superradiant enhancement are established.
3. Coherent excitonic excitation can be converted into photocurrent in quantum-dot photodiodes.
4. Fully quantum photodetector theory already treats coherent optical excitation, incoherent internal transfer, amplification backaction, efficiency and dark counts.
5. Quantum infrared detectors driven by collective electronic polarizations with coherence-dependent extraction already exist theoretically and experimentally; this is the strongest device-level adjacent prior art.
6. Incoherent optical or thermal driving can itself generate Fano/noise-induced coherences, so `rho_D` need not be diagonal in a generic multilevel system.

The focused screen has **not yet located** a detector theorem formulated as

```text
optically prepared pure bright excitation
versus
population-identical incoherent internal dark generation
with
bright-selective extraction,
```

nor the exact accepted-dark-rate identity

```math
Gamma_D^B=g^\dagger Dg/(g^\dagger g)
```

used as an intrinsic dark-generation rejection criterion for photodetectors.

That absence is not proof of novelty. The mathematics is close to standard quantum-state discrimination and collective-state theory, and the 2023 collective quantum-infrared-detector literature is a serious adjacent risk.

Current label:

```text
Gedanken premise: SURVIVES FIRST SCREEN
first analytical consequence: ESTABLISHED HERE
mathematical ingredients: ESTABLISHED
photodetector-specific synthesis novelty: OPEN / NOT ESTABLISHED
paper drafting: PREMATURE
```

---

## 10. Single next theoretical question

Before extending the model, attack the strongest possible no-go:

> In a passive detector obeying microscopic reversibility / KMS detailed balance, does the same physics that permits coherent bright-state extraction necessarily introduce a thermally driven bright-aligned dark channel whose rate scales with the collective optical coupling, thereby erasing the apparent signal-to-internal-dark advantage?

If detailed balance forces such an aligned dark floor, Experiment 09 should close immediately.

If it does not, the next step is to derive the strongest resource-counted bound on

```math
\frac{\text{accepted optical coupling strength}}
{\text{accepted nonradiative dark-generation rate}}
```

for a local-bath / collective-optical-coupling model.
