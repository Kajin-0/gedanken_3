# Experiment 10 — Kane Velocity Freedom and Microscopic Resource Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **NO MATERIAL-INDEPENDENT UPPER BOUND FROM LOW-ENERGY k.p OR OPTICAL SUM RULE / CONDITIONAL LATTICE RESOURCE BOUND DERIVED / NOVELTY NOT ESTABLISHED**

## 1. Question answered in this step

The previous step established, inside the ideal intrinsic 3-D massive-Dirac family, that matched useful absorptance gives

```math
\Sigma_e=n_ed\propto v^{-2},
```

while ideal ballistic crossing time is independent of `v`.

The immediate question was therefore:

> Is the Dirac/Kane velocity `v` genuinely free, or do generic multiband `k.p`, oscillator-strength sum rules, or remote-band consistency impose a compensating upper bound?

The result of this step is two-part:

1. **generic low-energy `k.p` and the global optical f-sum do not give a useful material-independent upper bound on large `v`;**
2. **a microscopic lattice Hamiltonian with a bounded hopping-range resource does give a rigorous conditional upper bound on `v`, and therefore a lower bound on the matched thermal carrier column.**

No Auger process is introduced.

---

## 2. Kane velocity and Kane energy

For the simplified zinc-blende Kane model coupling the relevant `Gamma_6` and `Gamma_8` sectors, define the usual Kane energy

```math
E_P=\frac{2m_0P^2}{\hbar^2}.
```

With the conventional simplified Kane normalization, the cone velocity obeys

```math
\boxed{
v^2=\frac{E_P}{3m_0}.
}
```

Therefore the matched-absorptance result from the previous step can be written

```math
\boxed{
\Sigma_e\propto \frac{1}{E_P}.
}
```

So an improvement factor `Q` in matched thermal carrier column requires

```math
\frac{\Sigma_{e,ref}}{\Sigma_e}=Q
```

and hence

```math
\boxed{
E_P=Q E_{P,ref},
\qquad
v=\sqrt Q\,v_{ref}.
}
```

This is a useful resource interpretation: the column improvement is linear in Kane energy, not exponential.

For reference, accepted HgCdTe Kane-model values near the topological transition use approximately

```text
E_P ~ 18.8 eV
v ~ 1.07e6 m/s.
```

The exact relation gives the following scales:

```text
v = 5.0e5 m/s   -> E_P = 4.26 eV
v = 1.0e6 m/s   -> E_P = 17.06 eV
v = 1.07e6 m/s  -> E_P = 19.53 eV
v = 2.0e6 m/s   -> E_P = 68.23 eV
v = 3.0e6 m/s   -> E_P = 153.51 eV
```

These numbers are bookkeeping, not a claim that such large `E_P` values are chemically realizable.

---

## 3. Why the multiband effective-mass identity does not isolate an upper bound

For an ordinary periodic single-electron Hamiltonian, the `k.p` effective-mass theorem around a nondegenerate band edge has the structure

```math
\boxed{
\left(m_n^{-1}\right)_{ij}
=\frac{\delta_{ij}}{m_0}
+\frac{2}{m_0^2}
\sum_{m\ne n}
\frac{\langle n|p_i|m\rangle
      \langle m|p_j|n\rangle}
{E_n-E_m}.
}
```

For a conduction edge, bands below `n` and remote bands above `n` enter with opposite denominator signs. Therefore the contribution of the fundamental valence-conduction matrix element cannot be bounded from above merely from positivity of the observed effective mass.

Schematically,

```text
fundamental valence bands below conduction edge
    -> positive inverse-mass contribution;

remote conduction bands above conduction edge
    -> negative inverse-mass contribution.
```

Remote-band terms can compensate one another. Thus a measured or assumed finite effective mass is not by itself a positive oscillator-strength budget that produces a universal upper bound on the fundamental `P` or `E_P`.

This does **not** mean arbitrary `P` is available in a real crystal. It means the low-energy effective-mass identity alone is insufficient to prove otherwise.

---

## 4. Optical f-sum rule gives the wrong sign for an upper-v obstruction

The full longitudinal optical conductivity of an electron system obeys an integrated spectral-weight sum rule. The total sum is fixed by the microscopic electronic degrees of freedom, but it constrains the **integral over all frequencies**, not one low-energy interband sector in isolation.

For the massive-Dirac sector derived in the previous step,

```math
\sigma_1(\omega)
=\frac{N_De^2\omega}{12\pi\hbar v}
\Phi(\omega;E_g,T)
```

with dimensionless spectral factor `Phi`.

Integrate over any **fixed photon-energy window**

```math
\omega\in[\omega_1,\omega_2]
```

whose endpoints are independent of `v`. Then

```math
\boxed{
W_{12}
\equiv\int_{\omega_1}^{\omega_2}\sigma_1(\omega)d\omega
\propto v^{-1}.
}
```

Therefore increasing `v` consumes **less**, not more, optical spectral weight in the fixed LWIR/MWIR energy window.

Consequently a global positive f-sum constraint of the form

```math
W_{12}\le W_{total}
```

can at most obstruct **too-small** `v` for a specified low-energy model. It does not provide an upper bound on `v`.

This is the opposite of the initially suspected cancellation mechanism.

### Important cutoff distinction

If instead one integrates the Dirac model to a **fixed momentum cutoff** `k_c`, then the corresponding energy cutoff grows like

```math
\omega_c\sim vk_c,
```

and the integrated Dirac spectral weight can increase with `v`.

But a fixed-momentum cutoff is an additional ultraviolet assumption. The detector only requires the model to be accurate over a fixed **energy** range around the LWIR transition and the thermally occupied states. As `v` increases, the momentum radius needed to cover a fixed energy range decreases as `1/v`.

Therefore no detector-mandated fixed-`k` cutoff has yet been identified.

---

## 5. Kramers-Kronig dielectric loading also does not give an upper bound

The interband contribution to the static dielectric response is related to optical conductivity through Kramers-Kronig. Since the low-energy conductivity in a fixed energy interval scales as `1/v`, its corresponding low-energy dielectric spectral contribution also decreases rather than increases with increasing `v`.

Thus the obvious dielectric-loading argument does not restore a compensating upper-v penalty either.

This does not exclude a chemistry-specific correlation between large `E_P`, remote bands, and background dielectric constant. It only rules out a generic low-energy Kramers-Kronig cancellation.

---

## 6. Remote-band energy alone is not enough

Let the nearest omitted band lie an energy `Delta_R` outside the useful low-energy sector. The massive-Dirac model need only remain accurate through a detector-relevant maximum quasiparticle energy `E_req`, with

```math
E_req<Delta_R.
```

For a Dirac dispersion, the momentum required to reach that fixed energy is

```math
k_req
=\frac{\sqrt{E_req^2-\Delta^2}}{\hbar v}.
```

Hence

```math
\boxed{k_req\propto v^{-1}.}
```

Increasing `v` makes the required momentum-space neighborhood **smaller**.

So a finite remote-band separation in energy does not by itself upper-bound `v`. It only limits the maximum energy through which the reduced model can be trusted.

A velocity ceiling requires a more primitive microscopic resource controlling how rapidly the Bloch Hamiltonian itself can vary with crystal momentum.

---

## 7. Conditional microscopic lattice velocity bound

Now impose a genuine microscopic resource assumption.

Write a translationally invariant Wannier/tight-binding Hamiltonian as

```math
H(\mathbf k)
=\sum_{\mathbf R} H_{\mathbf R}e^{i\mathbf k\cdot\mathbf R},
```

where `H_R` is the hopping matrix between Wannier sectors separated by lattice vector `R`.

Within this lattice representation, the Bloch velocity operator along Cartesian direction `i` is

```math
\hat v_i(\mathbf k)
=\frac{1}{\hbar}\frac{\partial H}{\partial k_i}
=\frac{i}{\hbar}
\sum_{\mathbf R}R_iH_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}.
```

Take the operator norm. By the triangle inequality,

```math
\boxed{
\|\hat v_i(\mathbf k)\|
\le
\frac{1}{\hbar}
\sum_{\mathbf R}|R_i|\,\|H_{\mathbf R}\|
\equiv V_i^{hop}.
}
```

Every group-velocity expectation value and every interband velocity matrix element obeys

```math
|\langle u_m|\hat v_i|u_n\rangle|
\le \|\hat v_i\|
\le V_i^{hop}.
```

Therefore any isotropic Dirac/Kane velocity encoded by that microscopic lattice Hamiltonian satisfies the **conditional resource bound**

```math
\boxed{
v\le V_{hop},
}
```

where, for an isotropic scalar bound, one may take an appropriate maximum or rotationally invariant norm built from the `V_i^{hop}`.

### Interpretation

The required extra resource is not `E_g` or a scalar effective mass. It is a hopping-range-weighted Hamiltonian norm,

```math
\boxed{
\mathcal J_i
\equiv
\sum_{\mathbf R}|R_i|\,\|H_{\mathbf R}\|,
\qquad
V_i^{hop}=\mathcal J_i/\hbar.
}
```

Large `v` requires either

```text
larger hopping amplitudes;
longer-range hopping;
or both.
```

Without any bound on this ultraviolet lattice resource, the continuum massive-Dirac model has no useful material-independent upper bound on `v`.

---

## 8. Detector consequence — conditional lower bound on thermal carrier column

From the previous step, for matched single-pass absorptance at a chosen normalized photon energy,

```math
\Sigma_e=\frac{C(T,E_g,A,r,n_b)}{v^2},
```

where the prefactor `C` is independent of `v` and equivalent-species degeneracy in the ideal model.

Combining with

```math
v\le V_{hop}
```

gives

```math
\boxed{
\Sigma_e
\ge
\frac{C(T,E_g,A,r,n_b)}{V_{hop}^2}.
}
```

This is the first explicit **microscopic-resource-conditioned admissibility inequality** in Experiment 10.

For the clean optical model used previously,

```math
\Sigma_e
=
\frac{12\tau_0 n_b\epsilon_0c}{\pi}
\frac{(k_BT)^3F_2(\delta)}
{e^2\hbar^2\omega\Phi(r,\delta)}
\frac{1}{v^2},
```

with

```math
\tau_0=-\ln(1-A),
```

```math
\delta=E_g/(2k_BT),
```

and

```math
\Phi(r,\delta)
=
\left(1+\frac{1}{2r^2}\right)
\sqrt{1-r^{-2}}
\tanh\left(\frac{r\delta}{2}\right).
```

Hence the resource-conditioned lower bound is obtained by replacing `v` with `V_hop` in the denominator.

For the previous numerical witness

```text
T = 300 K
lambda_c = 10 um
r = 1.2
A = 0.90
n_b = 3.5
```

one has

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

Thus

```text
V_hop = 1.0e6 m/s -> Sigma_e >= 1.067e13 cm^-2
V_hop = 2.0e6 m/s -> Sigma_e >= 2.667e12 cm^-2
V_hop = 3.0e6 m/s -> Sigma_e >= 1.185e12 cm^-2
```

These are model/resource bounds, not universal semiconductor constants.

---

## 9. Simple nearest-neighbor illustration

For a one-dimensional nearest-neighbor scale with lattice spacing `a` and hopping norm `t`, the generic operator bound reduces parametrically to

```math
V_{hop}\lesssim\frac{2at}{\hbar}
```

for the pair of `+/-a` neighbors.

Therefore reaching a target `v` requires roughly

```math
\boxed{
t\gtrsim\frac{\hbar v}{2a}.
}
```

For illustration only, taking

```text
a = 0.65 nm
```

gives

```text
v = 1.07e6 m/s -> t >= 0.54 eV
v = 2.00e6 m/s -> t >= 1.01 eV
v = 3.38e6 m/s -> t >= 1.71 eV
```

The numerical coefficient is model-dependent; the exact general result is the operator-norm inequality above.

---

## 10. Literature boundary checked in this step

Relevant established ingredients include:

- standard `k.p` effective-mass theory, in which momentum matrix elements and remote bands determine band-edge masses;
- Kane-band modeling and the Kane energy `E_P`;
- the experimentally observed approximately universal HgCdTe Kane velocity near `1.07e6 m/s` over a range of Cd content and temperature;
- optical-conductivity sum rules;
- the established inverse-velocity optical conductivity of 3-D Dirac systems;
- Wannier/tight-binding representations of Bloch Hamiltonians.

Primary references checked include:

```text
F. Teppe et al., Nature Communications 7, 12576 (2016),
DOI 10.1038/ncomms12576.

M. Orlita et al., Nature Physics 10, 233-238 (2014),
DOI 10.1038/nphys2857.

R. L. Bowers and G. D. Mahan, Physical Review 185, 1073 (1969),
DOI 10.1103/PhysRev.185.1073.

M. Jocić and N. Vukmirović, Physical Review B 102, 085121 (2020),
DOI 10.1103/PhysRevB.102.085121.

V. P. Gusynin, S. G. Sharapov, and J. P. Carbotte,
Physical Review B 75, 165407 (2007),
DOI 10.1103/PhysRevB.75.165407.
```

The general ingredients are not novel. No novelty claim is made for the operator-norm velocity inequality itself; it is essentially a direct consequence of the Bloch Hamiltonian derivative plus the triangle inequality.

The potentially useful synthesis is its insertion into the detector matched-absorptance result to produce a resource-conditioned lower bound on thermal carrier column.

Novelty remains **not established**.

---

## 11. What has actually been established

```text
DERIVED:
    Sigma_e ~ 1/E_P inside the simplified Kane normalization.

NEGATIVE RESULT:
    low-energy multiband effective-mass identities do not isolate a
    material-independent upper bound on the fundamental interband P.

NEGATIVE RESULT:
    the global optical f-sum does not upper-bound large v over a fixed
    detector-relevant photon-energy window; low-energy spectral weight
    decreases as 1/v.

NEGATIVE RESULT:
    fixed remote-band separation in energy alone does not upper-bound v.

DERIVED, CONDITIONAL:
    for a microscopic lattice Hamiltonian,
    v <= V_hop = hbar^-1 sum_R |R_i| ||H_R||.

DERIVED, CONDITIONAL:
    matched thermal carrier column obeys
    Sigma_e >= C/V_hop^2.
```

## 12. What is not established

```text
a material-independent numerical upper bound on v;
a chemistry-independent bound on hopping amplitudes or hopping range;
that the hopping-resource bound is tight for any real semiconductor;
that HgCdTe maximizes v or E_P;
that larger E_P improves actual detector D* once Auger and other intrinsic
processes are included;
novelty.
```

## 13. Single next question

The generic optical/DOS problem has now survived two obvious cancellation attacks. The next unavoidable intrinsic mechanism is Auger generation/recombination.

The next step should therefore ask:

> For the same finite-gap massive-Dirac family, how does the **kinematically allowed Auger phase space** depend on `v`, `E_g`, and any additional band asymmetry or remote-band parameter, and does increasing `v` preserve the matched-absorptance advantage or introduce a stronger nonradiative cost?

Do not insert an empirical Auger coefficient `C_A` as an independent parameter. Start from energy/momentum conservation and the simplest Coulomb matrix element structure.
