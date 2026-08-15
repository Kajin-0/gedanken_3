# Post-Experiment-11 Theoretical Premise Screen 3 — 2026-08-14

**Scope:** analytical/theoretical only  
**Purpose:** preserve exact negative results and novelty collisions before opening Experiment 12.  
**Disposition:** **EIGHT ADDITIONAL CANDIDATES REJECTED / EXPERIMENT 12 NOT OPENED**

This file continues the post-Experiment-11 screening series.

---

## Candidate 18 — mobility-independent thermal diffusion blur during drift

### Premise

A faster carrier mobility appears to improve both transit time and spatial localization. Test whether the Einstein relation cancels that apparent double benefit.

For uniform drift field `E` across distance `d`,

```math
t_{tr}=\frac{d}{\mu E},
\qquad
D=\frac{\mu k_BT}{q}.
```

The diffusion-only transverse variance accumulated during collection is

```math
\boxed{
\sigma_\perp^2=2Dt_{tr}
=\frac{2k_BT\,d}{qE}.
}
```

Mobility cancels exactly.

### Interpretation

Increasing mobility shortens the drift time but increases the diffusion coefficient in the same proportion. At fixed `d`, `E`, and `T`, the thermal diffusion blur accumulated before collection is therefore not reduced by mobility.

### Prior-art collision

This is standard semiconductor charge-cloud physics. Modern detector transport work explicitly combines

```math
\sigma=\sqrt{2Dt}
```

with the Einstein relation `D=mu kT/q`, and earlier imaging-detector literature treats charge spread as a drift-field/depth problem rather than a mobility-independent new detector theorem.

### Disposition

```text
REJECT.
```

Retain the cancellation as a useful design identity.

---

## Candidate 19 — matched-absorptance carrier column for parabolic direct bands

### Premise

Ask whether making both electron and hole effective masses lighter necessarily lowers the thermal carrier column at fixed useful interband absorptance.

For nondegenerate 3-D parabolic bands,

```math
n_i\propto(m_em_h)^{3/4}e^{-E_g/(2k_BT)}.
```

For fixed interband momentum matrix element and fixed photon excess energy above the gap, the direct-transition absorption coefficient has the reduced-mass scaling

```math
\alpha\propto m_r^{3/2},
\qquad
m_r=\frac{m_em_h}{m_e+m_h}.
```

Matching optical depth requires `d~1/alpha`, so

```math
\boxed{
n_id
\propto
\frac{(m_em_h)^{3/4}}{m_r^{3/2}}
=
\left(
\frac{m_e}{m_h}+2+\frac{m_h}{m_e}
\right)^{3/4}.
}
```

The absolute mass scale cancels. The expression is minimized at

```math
\boxed{m_e=m_h.}
```

### Prior-art collision

The cancellation is a resolved effective-mass version of the long-established infrared-detector material criterion based on useful absorption relative to thermal generation, commonly written through `alpha/G_th` or closely related material figures of merit. The algebra is neat but not a sufficiently new principle.

### Disposition

```text
REJECT.
```

---

## Candidate 20 — photogating decouples DC dark current but not absorber GR noise

### Premise

Electrically isolate a narrow-gap absorber from a high-mobility readout channel. Absorber occupancy gates the channel, suppressing direct absorber DC dark current in the readout.

Minimal absorber number dynamics:

```math
\dot N=G_{th}+\delta G_{ph}-N/\tau.
```

Let readout current respond as `delta I=g delta N`.

For low frequency, useful signal is

```math
\delta I_{sig}\sim g\tau\,\delta G_{ph}.
```

For a simple birth-death absorber, GR number fluctuations give a low-frequency current-noise scale proportional to

```math
g^2G_{th}\tau^2.
```

Thus absorber-GR-limited SNR cancels both photogating gain `g` and lifetime `tau`.

### Interpretation

Separating the absorber from the conduction channel can decouple photocurrent from **DC dark current**, but does not automatically decouple useful signal from the absorber's underlying thermal generation-recombination fluctuations.

### Prior-art collision

Generation-recombination noise and photoconductive gain/lifetime cancellation are classical photoconductor theory. Hybrid QD/graphene photogating and recent MWIR nanohybrid work explicitly pursue photocurrent/dark-current decoupling. The surviving statement is ordinary GR-noise physics applied to that architecture.

### Disposition

```text
REJECT.
```

---

## Candidate 21 — high-v massive-Dirac transport versus Zener leakage

### Premise

Experiment 10 favored large Dirac/Kane velocity `v` for lowering matched thermal carrier column. Test whether high `v` also gives a speed advantage once band-to-band tunneling leakage is held fixed.

For the massive-Dirac edge,

```math
m_D=\Delta/v^2.
```

With a fixed momentum-relaxation time,

```math
\mu\sim q\tau_m v^2/\Delta.
```

A Landau-Zener / Dirac tunneling exponent has the scaling

```math
S_Z\sim\frac{\pi\Delta^2}{\hbar qEv}.
```

Holding an allowed tunneling exponent fixed therefore implies

```math
E_{max}\propto v^{-1}.
```

Experiment-10 matched absorptance gave

```math
d\propto v.
```

Hence

```math
\boxed{
t_{drift}\sim\frac{d}{\mu E_{max}}\propto v^0
}
```

when `tau_m` and the dimensionless leakage criterion are fixed.

### Prior-art collision

Narrow-gap HgCdTe/APD theory already treats the same small-effective-mass / high-mobility / band-to-band-tunneling conflict. The cancellation is a composition of established Kane transport and Zener-tunneling scalings rather than a new independent detector principle.

### Disposition

```text
REJECT.
```

---

## Candidate 22 — quantum geometry as absorption without DOS

### Premise

In a generic two-band Hamiltonian

```math
H(\mathbf k)=d_0(\mathbf k)I+\mathbf d(\mathbf k)\cdot\boldsymbol\sigma,
\qquad
\varepsilon=|\mathbf d|,
```

thermal DOS is controlled by dispersion while interband oscillator strength can reside in Bloch-state geometry.

The pointwise decomposition is

```math
\boxed{
|\partial_i\mathbf d|^2
=(\partial_i\varepsilon)^2+4\varepsilon^2g_{ii},
}
```

where `g_ii` is the band quantum metric.

This separates the microscopic `k`-derivative budget into an intraband-dispersion term and an interband-geometric term.

### Prior-art collision

Recent quantum-geometric optics work already establishes that the quantum metric controls linear optical oscillator strength/conductivity and can keep optical conductivity finite even when conventional joint-DOS intuition would predict suppression. The proposed `absorption without DOS` escape is therefore already active current literature.

### Disposition

```text
REJECT.
```

Do not open a detector branch around a 2025–2026 quantum-geometry effect whose essential optical consequence is already established.

---

## Candidate 23 — correlated / excitonic insulating absorber

### Premise

Use an insulating correlated ground state with a low-energy optical collective/excitonic excitation but strongly suppressed free thermal carriers.

### Prior-art collision

Excitonic-insulator infrared photodetection is already explicit theory and experiment. First-principles work proposes full-spectrum IR detection from doped excitonic insulators with reduced thermal disturbance, while room-temperature excitonic-insulator THz photodetection and interlayer-exciton detectors already exploit related correlated bound-state physics.

### Disposition

```text
REJECT.
```

---

## Candidate 24 — Coulomb charging blocks single-carrier leakage but not a neutral photo-pair

### Premise

Use a small island with charging energy `E_C`. Contact injection of a single carrier changes net charge and pays `E_C`, whereas optical creation of an electron-hole pair is globally neutral and may avoid the same charging penalty.

### First consequence

The architecture can indeed suppress **single-charge injection** relative to a neutral optical excitation. However intrinsic thermal electron-hole pair generation is also neutral, so the mechanism cannot remove the fundamental intrinsic pair-generation floor.

### Prior-art collision

Coulomb-blockade / single-electron-transistor photodetection, quantum-dot infrared photodetectors, and photoelectron-transistor concepts are longstanding. Coulomb blockade has explicitly been analyzed in quantum-dot photocurrent and single-photon devices.

### Disposition

```text
REJECT.
```

---

## Candidate 25 — simultaneous phonon/heat and charge readout

### Premise

A true photon absorption deposits energy and creates charge; some leakage events may create charge without the same local energy-deposition topology. Joint charge + phonon/heat detection might reject dark events.

### Prior-art collision

Simultaneous ionization and phonon readout is a mature semiconductor event-discrimination architecture in cryogenic detectors, including single-electron-hole-pair-sensitive devices. Moreover intrinsic thermal pair generation exchanges energy with the lattice and cannot generically be eliminated by an external-energy tag without modeling the bath itself.

### Disposition

```text
REJECT.
```

---

# Overall screen

```text
Candidate 18 — mobility-independent diffusion blur: REJECT
Candidate 19 — parabolic mass-scale cancellation: REJECT
Candidate 20 — photogating GR-noise no-go: REJECT
Candidate 21 — high-v / Zener speed cancellation: REJECT
Candidate 22 — quantum-geometry absorption without DOS: REJECT
Candidate 23 — excitonic-insulator detector: REJECT
Candidate 24 — Coulomb-charging optical neutrality: REJECT
Candidate 25 — dual phonon/charge event discrimination: REJECT
```

Experiment 12 remains unopened.

## Updated screening lesson

The search has now eliminated several superficially attractive ways to separate useful absorption from dark carriers. A surviving premise must do more than suppress contact leakage, move oscillator strength into a known degree of freedom, or exploit a standard conserved quantity. It should generate a photodetector-specific incompatibility or escape condition from at least two coupled microscopic constraints.
