# Experiment 10 — Heavy-Hole Auger Rate Scaling and Joint Thermodynamic/Kinematic Bound

**Date:** 2026-08-14  
**Scope:** analytical/theoretical only  
**Disposition:** **OPEN-CCCH THRESHOLD PHASE SPACE DERIVED / NO INDEPENDENT HEAVY-HOLE-DOS DIVERGENCE / NEAR-CLOSURE SUPPRESSION DERIVED / EXACT-CLOSURE CARRIER-COLUMN LOWER BOUND DERIVED / NOVELTY NOT ESTABLISHED**

## 1. Question

The previous step added a heavy-hole-like spectator band to the active massive-Dirac electron/light-hole pair and proved the exact CCCH opening condition

```math
\rho\equiv\frac{M_{hh}v^2}{\Delta},
\qquad
\eta\equiv\frac{\delta_{hh}}{\Delta},
```

```math
\boxed{\rho\le\rho_c\equiv2(1+\eta)}
```

for exact finite-energy closure of the normal-momentum CCCH / Auger-1 channel.

This step asks two questions.

1. Once `rho > rho_c`, does the large heavy-hole density of states introduce a divergent rate prefactor that necessarily destroys the high-`v` design strategy?
2. If exact CCCH closure is required, what does the closure ceiling on `v` imply when combined with the already derived matched-absorptance law `Sigma_e=C/v^2`?

No empirical Auger coefficient is introduced.

---

## 2. Model and threshold geometry

Use

```math
\varepsilon(k)=\sqrt{\Delta^2+(\hbar vk)^2}
```

for the active conduction branch and

```math
E_{hh}(k)=\Delta+\delta_{hh}+\frac{\hbar^2k^2}{2M_{hh}}
```

for the heavy-hole excitation.

Dimensionless momenta are

```math
q=\frac{\hbar vk}{\Delta}.
```

On the open side, the threshold final state is collinear with

```math
q_1=q_2=x,
\qquad q_3=z,
```

and common dimensionless group velocity

```math
u=\frac{x}{\sqrt{1+x^2}}=\frac{z}{\rho}.
```

Thus

```math
x=\frac{u}{\sqrt{1-u^2}},
\qquad
z=\rho u,
```

and

```math
q_0=2x+z.
```

The threshold `u_th` is the unique solution of the equality derived in `THIRD_BAND_HEAVY_HOLE_AUGER_ESCAPE_STEP_2026-08-14.md`.

---

## 3. Six-dimensional constrained threshold Hessian

For a fixed initial hot electron, eliminate heavy-hole momentum through crystal-momentum conservation:

```math
\mathbf q_3=\mathbf q_0-\mathbf q_1-\mathbf q_2.
```

Define the dimensionless final energy

```math
f(\mathbf q_1,\mathbf q_2)
=e(q_1)+e(q_2)+h(q_3),
```

where

```math
e(q)=\sqrt{1+q^2},
\qquad
h(q)=1+\eta+\frac{q^2}{2\rho}.
```

At the threshold minimum, write local displacements of the two electron momenta as a six-vector `y`.

For a radial isotropic dispersion, the Dirac Hessian at momentum `x` has eigenvalues

```math
\boxed{
a_\parallel
=e''(x)
=(1+x^2)^{-3/2}
=(1-u^2)^{3/2},
}
```

and

```math
\boxed{
a_\perp
=\frac{e'(x)}{x}
=(1+x^2)^{-1/2}
=\sqrt{1-u^2}.
}
```

The heavy-hole curvature is isotropic:

```math
c_{hh}=1/\rho.
```

For each Cartesian direction `j`, the two-electron block of the constrained Hessian is therefore

```math
H_j=
\begin{pmatrix}
a_j+1/\rho & 1/\rho\\
1/\rho & a_j+1/\rho
\end{pmatrix}.
```

Its eigenvalues are

```math
a_j,
\qquad
a_j+2/\rho.
```

Hence the full six-dimensional determinant is exactly

```math
\boxed{
\det H
=
a_\parallel\left(a_\parallel+\frac{2}{\rho}\right)
\left[
a_\perp\left(a_\perp+\frac{2}{\rho}\right)
\right]^2.
}
```

For every finite open-side threshold this determinant is positive. Therefore the local threshold is a nondegenerate constrained quadratic minimum.

---

## 4. Fixed-hot-electron phase-space exponent

Let the hot-electron kinetic energy exceed threshold by

```math
\delta K=K-K_{th}^{hh}>0.
```

The increase in available final-state energy is not exactly `delta K` because the minimum final envelope itself moves with total momentum.

Let

```math
v_0^{(q)}=\frac{q_{th}}{\sqrt{1+q_{th}^2}}
```

be the dimensionless initial group velocity. The envelope slope is `u_th`, so

```math
\boxed{
\gamma
=1-\frac{u_{th}}{v_0^{(q)}}>0
}
```

and the dimensionless energy available to local final-state motion is

```math
\epsilon
\simeq
\gamma\frac{\delta K}{\Delta}.
```

For six quadratic coordinates,

```math
\int d^6y\,
\delta\!\left(
\epsilon-\frac12y^THy
\right)
=
\frac{4\pi^3}{\sqrt{\det H}}\epsilon^2.
```

Therefore the pure CCCH energy-shell phase space obeys

```math
\boxed{
\Phi_{hh}^{(q)}(K)
\simeq
4\pi^3
\frac{\gamma^2}{\sqrt{\det H}}
\left(\frac{K-K_{th}^{hh}}{\Delta}\right)^2.
}
```

Thus the heavy-hole channel has the same **kinematic threshold exponent 2** as the earlier interior two-band reopening problem.

If the squared Coulomb/spinor matrix element behaves as

```math
|V_{eff}|^2\propto(K-K_{th})^\nu,
```

then

```math
\boxed{
\Gamma_{II}^{hh}\propto(K-K_{th}^{hh})^{2+\nu}.
}
```

As before, `nu` is microscopic and not universal. Kane-model prior art explicitly contains threshold overlap zeros.

---

## 5. Flat-heavy-hole limit: no independent DOS divergence

The dangerous intuition was

```text
M_hh -> infinity
-> heavy-hole DOS diverges
-> CCCH rate must diverge as a positive power of M_hh.
```

That conclusion is false for the threshold event-rate geometry.

For

```math
\rho\to\infty,
```

the threshold tends to

```math
K_{th}^{hh}\to E_g+\delta_{hh}.
```

At the constrained final-state minimum,

```math
u_{th}\to0,
\qquad
x\to0,
```

while the heavy hole carries the finite threshold momentum.

Therefore

```math
a_\parallel\to1,
\qquad
a_\perp\to1,
\qquad
1/\rho\to0,
```

so

```math
\boxed{\det H\to1.}
```

Also

```math
\boxed{\gamma\to1.}
```

Hence

```math
\boxed{
\frac{\gamma^2}{\sqrt{\det H}}\to1.
}
```

The normalized local phase-space coefficient remains finite rather than diverging as `M_hh^(3/2)`.

Interpretation:

```text
a flat heavy-hole band destroys the activation threshold,
but momentum conservation ties the local final-state variations to the two dispersive conduction electrons;
the threshold shell therefore does not acquire an independent infinite heavy-hole DOS factor.
```

This does not imply a small physical CCCH rate. Spinor overlap, exchange, screening, band degeneracy, and non-threshold parts of phase space remain material dependent.

---

## 6. Near the exact-closure boundary the phase-space prefactor also vanishes

Let

```math
\delta\rho=\rho-\rho_c>0,
\qquad
\rho_c=2(1+\eta).
```

The previous step gave the universal threshold divergence

```math
q_{th}\sim\frac{3}{\delta\rho},
```

and therefore

```math
K_{th}^{hh}/\Delta\sim\frac{3}{\delta\rho}.
```

Expanding the exact threshold geometry gives

```math
u_{th}
=1-\frac{2}{9}(\delta\rho)^2+o((\delta\rho)^2),
```

```math
v_0^{(q)}
=1-\frac{1}{18}(\delta\rho)^2+o((\delta\rho)^2),
```

so

```math
\boxed{
\gamma
\sim\frac{(\delta\rho)^2}{6}.
}
```

At the same time,

```math
a_\perp\sim\frac{2}{3}\delta\rho,
```

```math
a_\parallel\sim\frac{8}{27}(\delta\rho)^3.
```

Using `rho -> rho_c` in the finite heavy-hole-curvature factors,

```math
\boxed{
\det H
\sim
\frac{256}{243\rho_c^3}
(\delta\rho)^5.
}
```

Therefore

```math
\boxed{
\frac{\gamma^2}{\sqrt{\det H}}
\sim
\frac{\sqrt3\,\rho_c^{3/2}}{64}
(\delta\rho)^{3/2}.
}
```

So the phase-space prefactor **vanishes** as the exact-closure boundary is approached.

For a smooth threshold matrix element, the thermally integrated rate therefore has the near-closure schematic form

```math
\boxed{
G_{hh}^{area}
\propto
v^{-4}
(\delta\rho)^{3/2}
\exp\!\left[
-\frac{\Delta+3\Delta/\delta\rho}{k_BT}
\right]
}
```

in the weak-screening matched-absorptance limit, apart from dielectric, overlap, exchange, numerical, and optical-depth factors.

The exact closure boundary is therefore approached **nonperturbatively**: the threshold diverges exponentially in the thermal rate and the local phase-space coefficient simultaneously vanishes algebraically.

---

## 7. High-v dimensional scaling of the open CCCH rate

At fixed dimensionless `rho`, `eta`, and threshold geometry, the characteristic momentum scale is

```math
k_D=\frac{\Delta}{\hbar v}.
```

The equilibrium four-particle momentum measure with one momentum delta function and one energy delta function scales as

```math
k_D^9/\Delta\propto v^{-9}.
```

Thus before interaction momentum dependence,

```math
G_{hh}^{vol}\propto |V_{th}^{hh}|^2v^{-9}.
```

Matched absorptance gives `d ~ v`, so

```math
G_{hh}^{area}\propto |V_{th}^{hh}|^2v^{-8}.
```

For the same minimal statically screened Coulomb structure used earlier,

```math
V(Q)
=\frac{e^2}{\epsilon_0\epsilon_r(Q^2+\kappa^2)}S_{hh},
```

with threshold momentum transfer `Q_th ~ 1/v`, the weak-screening limit gives

```math
|V_{th}^{hh}|^2\propto v^4|S_{hh}|^2/\epsilon_r^2.
```

Hence

```math
\boxed{
G_{hh}^{area}
\propto
\mathcal P_{hh}(\rho,\eta)
\frac{|S_{hh}|^2}{\epsilon_r^2}
v^{-4}
\exp[-(\Delta+K_{th}^{hh})/(k_BT)]
}
```

up to thermal powers and exchange/screening corrections, where

```math
\boxed{
\mathcal P_{hh}(\rho,\eta)
\propto\frac{\gamma^2}{\sqrt{\det H}}
}
```

for the smooth-matrix threshold piece.

For fixed physical `M_hh` and `delta_hh`, increasing `v` increases `rho`; nevertheless

```math
\mathcal P_{hh}\to O(1)
```

in the flat-heavy-hole limit. There is no compensating positive power of `M_hh` that automatically cancels the high-`v` algebraic factor.

The real damage from a heavy spectator band is the collapse

```math
K_{th}^{hh}:\ \infty\to E_g+\delta_{hh},
```

not a universal divergent threshold DOS prefactor.

---

## 8. Stronger result: exact CCCH closure imposes a thermal-column lower bound

The matched-absorptance result is

```math
\boxed{
\Sigma_e=\frac{C(T,E_g,A,r,n_b)}{v^2}.
}
```

Exact finite-energy CCCH closure requires

```math
\boxed{
v^2\le\frac{2(\Delta+\delta_{hh})}{M_{hh}}.}
```

Combining the two gives immediately

```math
\boxed{
\Sigma_e
\ge
C(T,E_g,A,r,n_b)
\frac{M_{hh}}{2(\Delta+\delta_{hh})}.
}
```

Since `2Delta=E_g`, equivalently

```math
\boxed{
\Sigma_e
\ge
C\frac{M_{hh}}{E_g+2\delta_{hh}}.
}
```

This is a **direct thermodynamic/kinematic tradeoff**:

```text
making v large lowers the matched thermal carrier column,
but exact protection from a nearby heavy-hole Auger channel places an upper ceiling on v;
therefore the spectator-band mass and offset impose a lower floor on the carrier column.
```

This is stronger than merely saying that a heavy-hole band reopens Auger.

---

## 9. Combined microscopic-resource bound

The earlier lattice/Wannier result gave

```math
v\le V_{hop}.
```

Exact CCCH closure simultaneously gives

```math
v\le v_c^{hh}
=\sqrt{\frac{2(\Delta+\delta_{hh})}{M_{hh}}}.
```

Therefore an absorber satisfying both resources must obey

```math
\boxed{
v^2
\le
\min\!\left[
V_{hop}^2,
\frac{2(\Delta+\delta_{hh})}{M_{hh}}
\right].
}
```

Hence

```math
\boxed{
\Sigma_e
\ge
\max\!\left[
\frac{C}{V_{hop}^2},
C\frac{M_{hh}}{2(\Delta+\delta_{hh})}
\right].
}
```

This is the current strongest Experiment-10 exact-closure admissibility inequality.

It combines

```text
required optical depth;
finite-gap Dirac thermal statistics;
microscopic lattice velocity resource;
and the first extra-band Auger escape constraint.
```

Novelty is not established.

---

## 10. Numerical witness at 10 um / 300 K

For the existing matched-absorptance witness

```text
T = 300 K
lambda_c = 10 um
A = 0.90
r = 1.2
n_b = 3.5
```

```math
C=1.06668\times10^{29}\ \mathrm{m^{-2}(m/s)^2}.
```

For a touching spectator band (`delta_hh=0`), exact CCCH closure gives

```math
v_c=\sqrt{E_g/M_{hh}}.
```

Selected values are

```text
M_hh/m0     v_c (m/s)       minimum Sigma_e for exact closure (cm^-2)
0.50        2.088e5          2.446e14
0.20        3.302e5          9.783e13
0.10        4.670e5          4.892e13
0.05        6.604e5          2.446e13
0.02        1.044e6          9.783e12
```

Thus a touching `0.5 m0` heavy-hole band forces a carrier-column floor about 23 times larger than the previous `v=1e6 m/s` witness (`~1.07e13 cm^-2`) if exact CCCH closure is demanded.

A touching spectator mass of order `0.02 m0` is required before the exact-closure ceiling permits `v` near `1e6 m/s`.

---

## 11. Prior-art boundary

The broad ingredients are established:

1. Classical direct-gap Auger theory already relates threshold behavior to carrier effective masses and energy/momentum conservation.
2. Bulk HgCdTe Auger-1/CCCH involving conduction electrons and a heavy hole is established and is a dominant fundamental channel in narrow-gap n-type material; see the review *Auger Recombination in Mercury Cadmium Telluride*, Semiconductors and Semimetals **18**, 121–155 (1981), DOI `10.1016/S0080-8784(08)62764-7`.
3. Gelmont, *Auger recombination in diamond-like narrow-gap semiconductors*, Phys. Lett. A **66**, 323–324 (1978), DOI `10.1016/0375-9601(78)90252-9`, shows that Kane overlap factors can vanish at threshold and alter the pre-exponential law.
4. Combescot & Combescot, Phys. Rev. B **37**, 8781 (1988), DOI `10.1103/PhysRevB.37.8781`, shows that band anisotropy/warping changes Auger pre-exponential temperature powers.
5. HgCdTe quantum-well work already engineers multiband dispersion to raise Auger thresholds and reach radiative-dominated regimes; see Alymov et al., ACS Photonics **7**, 98–104 (2020), DOI `10.1021/acsphotonics.9b01099`, and Morozov et al., ACS Photonics **8**, 3526–3535 (2021), DOI `10.1021/acsphotonics.1c01111`.

Therefore none of the following is a novelty claim:

```text
heavy-hole Auger channels;
threshold activation;
threshold overlap zeros;
multiband Auger engineering;
heavy-hole mass dependence of conventional Auger formulas.
```

A focused search did **not** establish prior art for the specific reduced-model combination

```math
\Sigma_e\ge C\,M_{hh}/[2(\Delta+\delta_{hh})]
```

obtained by composing the matched-absorptance high-`v` law with the exact three-band closure theorem. That absence is not sufficient to claim novelty.

Disposition:

```text
POSSIBLE JOINT ADMISSIBILITY THEOREM / NOVELTY NOT ESTABLISHED.
```

---

## 12. What has been established

```text
DERIVED:
    open CCCH has a six-dimensional nondegenerate threshold shell;

DERIVED:
    pure threshold phase space scales as (K-K_th)^2;

DERIVED:
    exact Hessian determinant and threshold-envelope factor gamma;

DERIVED:
    flat-heavy-hole limit has finite normalized threshold phase-space coefficient;

DERIVED:
    no universal M_hh^(3/2) rate divergence appears from local threshold DOS alone;

DERIVED:
    near exact closure, threshold coefficient ~ (rho-rho_c)^(3/2) while K_th ~ 1/(rho-rho_c);

DERIVED CONDITIONALLY:
    weak-screened matched-area CCCH rate retains v^-4 algebraic scaling times the heavy-hole threshold factor;

DERIVED:
    exact CCCH closure plus matched absorptance implies
    Sigma_e >= C M_hh/[2(Delta+delta_hh)];

DERIVED:
    combining lattice and spectator-band resources gives
    Sigma_e >= max[C/V_hop^2, C M_hh/(2(Delta+delta_hh))].
```

## 13. What is not established

```text
microscopic heavy-hole spinor/exchange factor;
dynamic screening;
an exact physical CCCH coefficient for real HgCdTe;
other spectator bands or split-off channels;
phonon-, disorder-, plasmon-, and Umklapp-assisted channels;
SRH or contact generation;
novelty of the joint bound;
full D* or SNR theorem.
```

---

## 14. Next question

The strongest surviving line is now the **joint admissibility theorem**, not another isolated rate prefactor.

Before adding further mechanisms, perform a dedicated prior-art audit of the composed structure

```text
matched complete optical boundary
+ matched absorptance
+ high-v carrier-column law
+ microscopic velocity resource
+ finite-k symmetry requirement
+ spectator-band CCCH closure
-> lower bound on carrier column / admissible band-structure region.
```

If that specific synthesis survives, compress Experiment 10 into theorem/corollary form and then attack the minimum additional channels needed to invalidate it. If it does not survive, close the branch rather than adding more phenomenology.