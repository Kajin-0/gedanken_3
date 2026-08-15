# Experiment 13 — finite-transit Shockley–Ramo recycling observability

**Date:** 2026-08-15  
**Scope:** analytical/theoretical only  
**Status:** DERIVED / PHYSICAL BRIDGE BETWEEN INTERNAL RECYCLING AND ENDPOINT COUNTING / NOVELTY NOT ESTABLISHED

## 1. Purpose

The phenomenological interpolation

```math
y=a x+b j_e
```

already showed that occupancy-sensitive readout and ideal endpoint counting can expose radically different photon-recycling noise. The missing physical bridge is finite carrier transit: a real junction terminal can respond to carrier motion before the final extraction event.

This note derives that bridge directly from the Shockley–Ramo theorem.

The central result is stronger than the earlier `a,b` interpolation:

> an electron–hole pair that is created internally and later recombines internally at a common point produces **zero net induced charge** on every electrode but can produce a finite **AC Shockley–Ramo waveform**. A recycled lineage can therefore be invisible in the endpoint/DC limit while becoming visible at finite frequency through its transient weighting-field motion.

This is the mechanism required by the Poisson-lineage observability theorem.

---

## 2. General weighting-field identity

For electrode `k`, let the weighting potential be

```math
\phi_k(\mathbf r),
```

with the usual boundary conditions `phi_k=1` on electrode `k` and zero on the other electrodes, and define

```math
\mathbf E_{w,k}=-\nabla\phi_k.
```

For a point charge `q_c` following trajectory `r_c(t)`, the induced current is

```math
i_k^{(c)}(t)
=q_c\mathbf v_c(t)\cdot\mathbf E_{w,k}[\mathbf r_c(t)]
=-q_c\frac{d}{dt}\phi_k[\mathbf r_c(t)].
```

For an electron–hole pair,

```math
q_e=-e,
\qquad
q_h=+e,
```

so

```math
\boxed{
i_k(t)
=e\frac{d}{dt}
\left[
\phi_k(\mathbf r_e(t))-\phi_k(\mathbf r_h(t))
\right].
}
```

Define the weighting-potential separation

```math
\Delta\phi_k(t)
=\phi_k(\mathbf r_e(t))-\phi_k(\mathbf r_h(t)).
```

Then simply

```math
\boxed{i_k(t)=e\dot{\Delta\phi}_k(t).}
```

This identity is independent of the drift law, diffusion history, field uniformity, or device geometry, provided the ordinary Shockley–Ramo description applies.

---

## 3. Integrated induced charge: collection versus internal recombination

Integrating a pair trajectory from creation at `t=0` to termination at `t=t_f`,

```math
Q_k
=\int_0^{t_f}i_k(t)dt
=e[\Delta\phi_k(t_f)-\Delta\phi_k(0)].
```

If the electron and hole are created at the same point,

```math
\Delta\phi_k(0)=0.
```

### A. Internal recombination

If the pair later recombines at a common point `r_r`, then

```math
\mathbf r_e(t_f)=\mathbf r_h(t_f)=\mathbf r_r,
```

and therefore

```math
\Delta\phi_k(t_f)=0.
```

Hence

```math
\boxed{Q_k^{rec}=0}
```

for **every electrode**, regardless of how far the carriers separated before recombination.

The trajectory may have generated a sizable transient current, but its signed time integral vanishes.

### B. Complete collection

If a pair is fully collected at opposite contacts, then for a two-terminal detector read out at electrode `k`, the final weighting-potential separation is `+1` or `-1` according to the polarity convention. Therefore

```math
\boxed{|Q_k^{col}|=e.}
```

Thus internally recombining and finally collected pair segments are topologically different from the terminal point of view:

```text
internal creation -> internal recombination: zero net induced charge;
internal creation -> opposite-contact collection: one elementary-charge net signal.
```

---

## 4. Frequency-domain theorem for a recombining pair

Use the Fourier convention

```math
H_k(\omega)
=\int_0^{t_f}i_k(t)e^{-i\omega t}dt.
```

Since `i_k=e d(Delta phi_k)/dt`, integration by parts gives

```math
H_k(\omega)
=e\left[
\Delta\phi_k(t)e^{-i\omega t}
\right]_0^{t_f}
+i\omega e
\int_0^{t_f}
\Delta\phi_k(t)e^{-i\omega t}dt.
```

For an internally created and internally recombining pair both endpoint terms vanish exactly. Therefore

```math
\boxed{
H_k^{rec}(\omega)
=i\omega e
\int_0^{t_f}
\Delta\phi_k(t)e^{-i\omega t}dt.
}
```

Consequences:

```math
\boxed{H_k^{rec}(0)=0,}
```

while generically

```math
H_k^{rec}(\omega)\ne0
```

for finite frequency.

If the first temporal moment exists,

```math
H_k^{rec}(\omega)
=i\omega e
\int_0^{t_f}\Delta\phi_k(t)dt
+O(\omega^2).
```

Thus an intermediate radiative-recombination segment is intrinsically **AC-only at low frequency** in the ideal Ramo description.

This statement does not assume a rectangular current pulse or a specific recombination trajectory.

---

## 5. Explicit planar collected-pair waveform

For a simple planar junction of thickness `L`, take the sensing electrode at `z=L` and return electrode at `z=0`, so

```math
\phi_w(z)=z/L.
```

Create an electron–hole pair at `z=z_0`. Let the electron drift toward `L` at constant speed `v_e` and the hole toward `0` at speed `v_h`.

Transit times are

```math
\tau_e=(L-z_0)/v_e,
\qquad
\tau_h=z_0/v_h.
```

With the sign convention chosen so the pair contributions add at the sensing terminal,

```math
i_e(t)=\frac{e v_e}{L}\,1_{0<t<\tau_e},
```

```math
i_h(t)=\frac{e v_h}{L}\,1_{0<t<\tau_h}.
```

The complete collected-pair Fourier waveform is

```math
\boxed{
H_{col}(\omega;z_0)
=\frac{e}{L}
\left[
\frac{v_e(1-e^{-i\omega\tau_e})}{i\omega}
+
\frac{v_h(1-e^{-i\omega\tau_h})}{i\omega}
\right].
}
```

Taking `omega -> 0`,

```math
H_{col}(0;z_0)
=\frac{e}{L}(v_e\tau_e+v_h\tau_h)
=e.
```

Thus the full finite-transit waveform continuously reduces to the one-electron endpoint charge at zero frequency.

At frequencies comparable to inverse transit times, however, the waveform retains depth and mobility information that a pure endpoint counter discards.

---

## 6. One photon-recycling lineage across two pixels

Now consider a complete conservative lineage:

```text
pair created in pixel A
-> carrier motion in A
-> radiative recombination in A
-> photon propagation/reabsorption
-> pair created in pixel B
-> carrier motion in B
-> final collection in B.
```

Let `T_AB` be the random delay between the start of the A-stage and creation of the B-stage.

Assume for clarity that the weighting fields are sufficiently localized that the A-stage is read primarily at terminal A and the B-stage at terminal B. The complete lineage vector is then

```math
\mathbf H_{A\to B}(\omega)
=
\begin{pmatrix}
H_A^{rec}(\omega)\\
e^{-i\omega T_{AB}}H_B^{col}(\omega)
\end{pmatrix}.
```

The lineage contribution to the terminal spectral matrix is the outer product

```math
\mathbf H_{A\to B}\mathbf H_{A\to B}^\dagger.
```

Its off-diagonal term is

```math
\boxed{
H_A^{rec}(\omega)
H_B^{col*}(\omega)
e^{+i\omega T_{AB}}.
}
```

Because

```math
H_A^{rec}(0)=0,
\qquad
H_B^{col}(0)=e,
```

the A-to-B conservative recycling contribution satisfies

```math
\boxed{S_{AB}^{A\to B}(0)=0}
```

but is generically nonzero at finite frequency.

Near zero frequency,

```math
S_{AB}^{A\to B}(\omega)=O(\omega)
```

at the complex cross-spectrum level unless ensemble symmetry cancels the linear term. In a fully symmetric equilibrium A<->B ensemble, conjugate directional contributions can cancel the odd/imaginary leading term, in which case the real symmetric cross-spectrum begins at higher order. The exact order is therefore symmetry/readout dependent; the zero-frequency cancellation is not.

---

## 7. Endpoint-counting limit recovered exactly

An ideal endpoint counter deliberately throws away all pre-collection Ramo motion and represents a lineage ending in B as only

```math
\mathbf H_{A\to B}^{end}(\omega)
=g_B(\omega)\mathbf e_B.
```

The A component is then identically zero at all frequencies:

```math
H_A^{end}(\omega)=0.
```

Therefore

```math
\boxed{S_{AB}^{end}(\omega)=0}
```

for every frequency, reproducing the Experiment-03 Poisson-output cancellation theorem.

The finite-transit Shockley–Ramo readout differs because the same lineage can leave an AC waveform at A before its final count appears at B.

---

## 8. Occupancy-sensitive limit and physical interpolation

An occupancy-sensitive detector records residence of the excitation itself rather than only weighting-field motion or final extraction. A recycled lineage therefore naturally has finite waveform support in both A and B over its two residence intervals.

The three readout classes can now be ordered physically:

```text
occupancy readout:
    records internal residence directly;
    broad shared lineage support;
    recycling cross-spectrum visible.

finite-transit Shockley–Ramo junction readout:
    records charge motion during each residence;
    internally recombining stages have zero DC area but finite AC waveform;
    recycling can reappear in cross-spectrum at finite frequency.

ideal endpoint counter:
    retains only the final sink event;
    one lineage -> one terminal;
    recycling cross-spectrum exactly zero.
```

This is the desired physical interpolation. It is not controlled by an arbitrary phenomenological mixing coefficient; it is controlled by the weighting fields, carrier trajectories, recombination points, photon-transfer delays, and electronics.

---

## 9. Multi-electrode/general geometry form

For `m` electrodes and an arbitrary pair trajectory, define the vector of weighting-potential separations

```math
\Delta\boldsymbol\phi(t)
=
\begin{pmatrix}
\Delta\phi_1(t)\\
\vdots\\
\Delta\phi_m(t)
\end{pmatrix}.
```

For an internally recombining stage,

```math
\boxed{
\mathbf H^{rec}(\omega)
=i\omega e
\int
\Delta\boldsymbol\phi(t)e^{-i\omega t}dt.
}
```

For independent Poisson primary lineages, the terminal spectrum remains

```math
S_y(\omega)
=\sum_a\lambda_a
E[\mathbf H_a\mathbf H_a^\dagger].
```

Thus the complete finite-transit detector is still exactly a Gram geometry in the lineage-waveform Hilbert space.

The normalized terminal coherence obeys the ordinary Cauchy–Schwarz bound

```math
\boxed{
|S_{ij}(\omega)|^2
\le S_{ii}(\omega)S_{jj}(\omega).
}
```

Equality requires the weighted lineage-response vectors of terminals `i` and `j` to be linearly dependent at that frequency.

---

## 10. What is genuinely new here versus established Ramo theory

Do **not** claim the following as new:

- Shockley–Ramo current induction;
- weighting potentials or multi-electrode weighting fields;
- finite-transit photodiode impulse responses;
- application of Ramo/corpuscular methods to generation–recombination noise;
- Gram/cross-spectral coherence inequalities.

The candidate new detector-facing content is narrower:

1. apply the complete-lineage viewpoint specifically to **conservative photon recycling between photodetector pixels**;
2. show that an intermediate internally recombining pair stage is rigorously zero-area but finite-AC under Shockley–Ramo;
3. combine that fact with the Poisson-lineage outer-product theorem to obtain a clean frequency-dependent boundary between recycling that is hidden by endpoint counting and recycling that is exposed by finite-transit terminal motion;
4. embed this observability result in the same positive-operator geometry that also contains task ordering, coherent selectivity, and the Experiment-12 inverse population bound.

Novelty of this combined closure still requires a dedicated prior-art audit.

---

## 11. Immediate consequences worth testing next

### Consequence A — low-frequency null

For a lineage stage that both begins and ends as an internally neutral electron–hole pair,

```math
H^{rec}(0)=0.
```

Therefore passive recycling correlations exposed only through such intermediate Ramo stages must disappear in the strict zero-frequency limit even though they may be strong at finite frequency.

### Consequence B — characteristic frequency scale

The AC-only stage is controlled by carrier transit/separation and recombination times. Recycling visibility should therefore peak or turn over at frequencies comparable to inverse residence/transit times, not solely at the internal exchange rate `k` from the occupancy model.

### Consequence C — weighting-field engineering changes observability without changing recycling probability

Two devices can have the same internal photon-transfer matrix `p_ij` but different terminal recycling cross-spectra because their weighting-field overlaps and carrier trajectories differ.

This is a direct detector-specific example of the Experiment-13 thesis:

```text
same internal process + different measurement operator -> different measured physics.
```

---

## 12. Next step

Perform the dedicated prior-art kill test for the **combined** claim, with particular attention to:

- corpuscular/Ramo treatments of generation–recombination noise;
- photon-recycling noise in HgCdTe photodiodes;
- segmented-detector charge sharing and cross-spectra;
- task-based/Fisher information operator metrics;
- any prior paper that explicitly unifies detector task ordering, coherence discrimination, response/resource bounds, and terminal observability through one positive coupling operator.

Do not draft a unified manuscript until that audit is complete.
