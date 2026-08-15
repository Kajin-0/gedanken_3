# Progress Log — Experiment 10: Room-Temperature LWIR Material Admissibility

**Scope:** analytical/theoretical only.  
**Fixed target:** `T=300 K`, `lambda_c=10 um`, `Eg=0.123984 eV`, `Eg/kBT ~= 4.796`.

---

## 2026-08-14 — branch opened

Goal: derive from first principles the electronic-structure conditions for room-temperature LWIR intrinsic detector quality, rather than rank known materials.

Immediate novelty exclusions included `alpha/G_th`, generic detailed balance, generic Auger suppression, and Experiment-08 zero-gap Kane statistics.

---

## Matched finite-gap Dirac absorption/statistics

Derived

```math
n_c\propto v^{-3},
\qquad
\alpha_D\propto v^{-1},
```

so for controlled single-pass active-pair optical depth

```math
\Sigma_c=C/v^2
```

in the two-band neutral model.

Adding spectator hole states shifts intrinsic `mu>0`, increases active electron density and weakens active-pair absorption. Thus the rigorous multiband statement becomes

```math
\boxed{\Sigma_c\ge C/v^2.}
```

Standard witness:

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

---

## Microscopic velocity resource

A Wannier Hamiltonian gives

```math
\boxed{v\le V_{hop}}
```

and therefore the conditional single-pass bound `Sigma>=C/V_hop^2`.

Generic low-energy effective-mass sums, fixed-window optical f-sums and remote-band energy separation did not yield a universal upper `v`.

---

## Two-band direct-Auger sequence

Exact particle-hole-symmetric finite-gap massive-Dirac `eeh/hhe` direct Auger is closed.

Scalar particle-hole asymmetry reopens it with weak-asymmetry threshold

```math
\boxed{K_{th}\sim E_g\mathcal A_m^{-1/3}.}
```

At the fixed target, the scalar toy model needs about `A_m<=0.0848` for `K_th>=10 kBT`.

Near an interior threshold, pure kinematic phase space scales as `(K-K_th)^2`; microscopic overlap zeros can add powers.

In a minimal weak-screening model, matched-area direct Auger retains approximately `v^-4` algebraic suppression times the threshold activation.

Broad Dirac/symmetric Auger suppression is established prior art.

---

## Complete external radiative boundary

Corrected the founding comparison: useful front-side absorptance alone does not fix total thermal radiative exchange. Match the complete external mode-resolved optical boundary.

At equilibrium,

```math
\Phi_{abs}^{ext}=\Phi_{em}^{ext}=\Phi_0.
```

Internal radiative recombination is not invariant because photon recycling changes internal event count.

Ideal 10-um/300-K hemispherical step benchmark:

```text
Phi_0 = 4.89777e17 cm^-2 s^-1
q Phi_0 = 0.0784710 A/cm^2
```

Direct-Auger/radiative activation parity occurs at `K_th=Eg/2`.

---

## Heavy-hole third-band escape

For

```math
E_{hh}=\Delta+\delta_{hh}+p^2/(2M_{hh}),
```

proved exact finite-energy normal-momentum CCCH closure iff

```math
\boxed{M_{hh}v^2\le2(\Delta+\delta_{hh}).}
```

This was the first direct conflict with the high-`v` carrier-column lever.

The open heavy-hole threshold shell remains quadratic. In the flat-heavy-hole limit the normalized local threshold phase-space coefficient remains finite; the principal damage is threshold collapse rather than an independent universal `M_hh^(3/2)` threshold-DOS divergence.

Near exact closure the threshold diverges as `3Delta/(rho-rho_c)` and the local phase-space coefficient vanishes as `(rho-rho_c)^(3/2)`.

---

## General spectator-band theorem

For positive isotropic convex spectator excitation `E_s(p)`, define

```math
\boxed{v_s^{crit}=\inf_{p>0}E_s(p)/p.}
```

Exact finite-energy normal-momentum spectator-assisted CCCH closure is equivalent to

```math
\boxed{v\le v_s^{crit}.}
```

For multiple spectators,

```math
v_{spec}=\min_s v_s^{crit}.
```

This is mathematically Landau-like and equal-group-velocity threshold physics is classical.

Define

```math
v_{adm}=\min(V_{hop},v_{spec}).
```

The strongest conditional single-pass electronic theorem is

```math
\boxed{\Sigma_c\ge C/v_{adm}^2.}
```

Parabolic heavy-hole corollary:

```math
\boxed{
\Sigma_c\ge
\max[C/V_{hop}^2, C M_{hh}/(2(\Delta+\delta_{hh}))].
}
```

---

## Adversarial electronic novelty audit

Prior art directly covers nearly every constituent idea:

```text
alpha/G_th detector optimization;
small-gap band-structure Auger suppression;
HgCdTe heavy-hole CCCH;
equal-group-velocity impact-ionization thresholds;
Landau min[E/p] critical velocity;
Dirac/quasi-relativistic Auger suppression;
multiband IR detector optimization balancing absorption and Auger;
radiative detailed balance and photon recycling.
```

Focused search did not locate the exact carrier-sheet lower-bound composition, but a hostile reviewer can plausibly call it an elementary synthesis.

Two hard universality failures were identified:

```text
unbounded useful optical absorption by spectator bands;
arbitrary photonic path enhancement reducing physical absorber thickness.
```

---

## Resonant path enhancement versus finite response

One-port TCMT gives

```math
A(\omega)
=\frac{4\gamma_e\gamma_i}
{(\omega-\omega_0)^2+(\gamma_e+\gamma_i)^2}.
```

Define cavity field-envelope response time `tau_opt=1/(gamma_e+gamma_i)` and

```math
\boxed{g(A_0)=1-\sqrt{1-A_0}.}
```

On the over-coupled branch,

```math
\boxed{2\gamma_i\ge g(A_0)/\tau_{max}.}
```

Define optical sampling-rate resource

```math
\boxed{\Lambda_a=2\gamma_i/(\alpha_Dd).}
```

Then

```math
\boxed{
\Sigma_c\ge
\frac{B}{v_{adm}^2}
\frac{g(A_0)}{\Lambda_a\tau_{max}}.
}
```

TCMT does not upper-bound `Lambda_a`. Therefore finite temporal response alone does not restore a universal physical carrier-column floor.

In a simple one-optical-wavelength circulation at 10 um, a 1-ps optical response still permits roughly `100x` less active carrier column than the original 90%-absorbing single-pass bound.

---

## Final passive-photonics audit

Controlling file:

`FINAL_PHOTONIC_AUDIT_AND_DISPOSITION_2026-08-14.md`.

The missing photonic-resource space is already heavily occupied by established theory:

```text
Fano/Bode-Fano passive broadband matching constraints;
Rozanov thickness-bandwidth sum rules;
Miller slow-light delay bounds depending on footprint and dielectric contrast;
Yu-Raman-Fan nanophotonic light-trapping limits based on resonances/channels;
Miller et al. susceptibility-based per-volume absorption bounds;
mature resonant-cavity-enhanced photodetector efficiency/bandwidth engineering.
```

Thus arbitrary photonics necessarily introduces additional resources—susceptibility, footprint, channel count, accepted bandwidth, delay, port topology—and a pure electronic-structure universal carrier-column theorem cannot survive without them.

Mechanically composing those established optical bounds with the Experiment-10 electronic inequalities would yield engineering syntheses, not a sufficiently strong novelty case.

---

# FINAL DISPOSITION — 2026-08-14

```text
EXPERIMENT 10 CLOSED BY DEFAULT AS A NOVELTY / MANUSCRIPT PATH.
```

Retain the exact and conditional results for reuse.

Do not draft a manuscript from the current theorem package.

Do not continue by adding more known electronic mechanisms or established photonic resource bounds.

Reopen only for a genuinely non-compositional detector theorem/invariant.

## Next research action

Screen new purely theoretical photodetector Gedanken premises.