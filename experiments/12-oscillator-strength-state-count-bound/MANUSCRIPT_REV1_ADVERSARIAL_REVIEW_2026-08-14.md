# Experiment 12 — Adversarial Review of MANUSCRIPT_REV1

**Date:** 2026-08-14  
**Reviewer posture:** hostile second-round referee  
**Disposition:** **PASS WITH MINOR REVISION — BASIS-INVARIANT BLOCKING DEFECT RESOLVED / CORE THEOREM DEFENSIBLE / NOVELTY REMAINS THE MAIN RISK**

## 1. Executive verdict

Rev1 successfully fixes the only blocking mathematical-presentation defect identified in Rev0. The optical resource is now defined using selected coupling operators inside exact degenerate energy eigenspaces, so arbitrary unitary rotations within a degenerate subspace no longer change the quoted material resource.

I do not find a counterexample to the corrected theorem. The pointwise Fermi inequality, Kubo normalization, degenerate-shell resource bound, parabolic equality family, and Dirac validation are mutually consistent.

Two minor revisions remain:

```text
1. a LaTeX notation typo writes `\nu_B` in a few boxed equations where the intended symbol is `u_B`;
2. the scope should state explicitly that the theorem constrains integrated optical spectral weight, not an arbitrarily narrow peak absorption amplitude.
```

After those corrections, the manuscript is technically defensible enough for a formal external-style review. The remaining dominant risk is novelty/significance, not correctness.

---

# 2. Degenerate-shell resource — PASS

For an upper degenerate eigenspace `P_epsilon_c`, Rev1 defines

```math
A_{\epsilon_c,B}
=P_{\epsilon_c}\hat v_iQ^-_{\epsilon_c,B}.
```

For any normalized `|c>` in that eigenspace,

```math
R_c(B)
=\langle c|A A^\dagger|c\rangle
\le\|A\|_{op}^2.
```

The analogous lower-shell statement also holds.

Defining `u_B^2` as the maximum of these shell operator norms therefore gives

```math
\mathcal R_B\le u_B^2(n_e+n_h)
```

independently of the basis chosen inside any exact degeneracy.

This is sharper than taking one spectral norm over states at different energies, because it maximizes only over genuine eigenbasis gauge freedom.

```text
PASS.
```

---

# 3. Notation regression — MINOR BUT MUST FIX

In several equations the intended resource `u_B` appears as

```math
\nu_B
```

because the LaTeX string was written `\nu` rather than `u`.

This is potentially confusing because Greek `nu` looks like an additional physical quantity.

All theorem statements should consistently use

```math
u_{\mathcal B}.
```

```text
MINOR REVISION REQUIRED.
```

---

# 4. Spectral-weight versus peak-absorption scope — MUST STATE EXPLICITLY

The theorem bounds a frequency **integral**:

```math
\int_B K_T(\hbar\omega)\sigma_1^{cross}(\omega)d\omega.
```

It does not prevent an arbitrarily narrow line from having a very high peak conductivity while its integrated spectral weight tends to zero.

Therefore the direct photodetector interpretation requires a nonzero useful optical bandwidth or an independently specified integrated oscillator strength.

This is not a loophole in the theorem; it is the meaning of the theorem. But if the manuscript simply says “strong absorption” without emphasizing spectral weight, a referee can accuse it of overstating detector relevance.

Add a sentence such as:

> The inequality constrains integrated cross-`mu` optical spectral weight; a peak-only requirement with vanishing useful bandwidth does not produce a finite population bound.

```text
MINOR SCOPE REVISION REQUIRED.
```

---

# 5. Pointwise Fermi lemma — PASS

No error found. Equality condition remains exact:

```math
E_c-\mu=\mu-E_v.
```

The half-transition-energy thermal factor is genuinely specific to crossing the chemical potential; same-side thermal transitions fall back to the weaker full-energy detailed-balance kernel.

```text
PASS.
```

---

# 6. Kubo normalization — PASS

The angular-frequency Kubo form in Rev1 is consistent. No missing factor of `hbar` found.

```text
PASS.
```

---

# 7. Parameter-free hierarchy — PASS AND SHOULD REMAIN CENTRAL

The strongest conceptual structure is

```math
\frac{2}{\pi e^2}
\int_B K_T\sigma_1^{cross}d\omega
\le
\mathcal R_B
\le
u_B^2(n_e+n_h).
```

The first inequality is exact Fermi/Kubo physics; the second explicitly identifies the microscopic optical resource.

This hierarchy is more persuasive than presenting only the final population bound.

```text
PASS.
```

---

# 8. Equal-mass parabolic saturation — PASS, WITH MODEL LABEL

The all-temperature equality is exact inside the stated ideal parabolic two-band model with constant one-to-one interband velocity matrix element.

A real semiconductor cannot maintain parabolic dispersion and a constant matrix element to arbitrarily high energy. The manuscript should continue to call this a model/equality construction rather than a literal full-band material.

This does not weaken its role as a mathematical saturation example.

```text
PASS.
```

---

# 9. Dirac references — CORRECTED

Rev1 now distinguishes the massless 3-D Dirac/Weyl comparator from the gapped-semimetal optical-response paper:

```text
Tabert, Carbotte & Nicol, PRB 93, 085426 (2016);
Tabert & Carbotte, PRB 93, 085442 (2016).
```

This is the appropriate adjacent literature for the validation family.

```text
PASS.
```

---

# 10. Static disorder / localization — PASS WITH NARROW CLAIM

Static one-body disorder is compatible with the exact-eigenstate proof. Localization does not evade the thermal population inequality.

The manuscript correctly refuses to infer dc dark current from that population.

```text
PASS.
```

---

# 11. Exciton counterexample — PASS AS SCOPE LIMIT

Neutral bound excitons remain a genuine escape from a free-quasiparticle population theorem.

Keeping this limitation in the main text is essential. It makes the theorem narrower but more credible.

```text
PASS.
```

---

# 12. Novelty audit — STILL HIGH RISK

The strongest rejection argument remains:

> Eq. (10) is elementary Pauli blocking, and the rest is just a norm bound plus Kubo.

No direct prior source has yet been located with the arbitrary-window inverse population inequality. But the proof's simplicity means “known but unstated” risk is substantial.

The paper is worth circulating/reviewing only because it has more than the one-line lemma:

```text
arbitrary dispersive multiband state reuse is handled;
degenerate-basis invariance is handled;
exact equality families are identified;
Dirac and parabolic tightness is quantified;
relation to f-sums and phase-space filling is explicit;
its detector scope is carefully bounded.
```

```text
CORRECTNESS RISK: LOW AFTER MINOR FIXES.
NOVELTY RISK: HIGH.
```

---

# 13. Overall second-round disposition

```text
ALGEBRA: PASS
KUBO NORMALIZATION: PASS
DEGENERACY/BASIS INVARIANCE: PASS
MULTIBAND STATE REUSE: PASS
PARABOLIC EQUALITY: PASS
DIRAC VALIDATION: PASS
DETECTOR OVERCLAIM: CONTROLLED
NOTATION: MINOR FIX
SPECTRAL-BANDWIDTH SCOPE: MINOR FIX
DIRECT PRIOR-ART COLLISION: NOT FOUND
NOVELTY SIGNIFICANCE: HIGH-RISK BUT PLAUSIBLE
```

## Recommendation

Create Rev2 with only the two minor corrections above and a short wording polish. Do **not** add new physics to make the paper look larger. After Rev2, the project has reached a defensible paper-draft stage; further work should be external-style manuscript review and priority verification, not theory inflation.
