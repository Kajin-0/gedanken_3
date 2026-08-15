# Physical Review B — Cover letter draft

**Manuscript:** `MANUSCRIPT_REV6_2026-08-14.md`  
**Proposed title:** **Thermal quasiparticle population bound from direct interband optical spectral weight**  
**Article type:** Regular Article  
**Status:** draft; author-owned declarations remain placeholders

---

Dear Editors of *Physical Review B*,

Please consider our manuscript, **“Thermal quasiparticle population bound from direct interband optical spectral weight,”** for publication as a Regular Article in *Physical Review B*.

The work addresses a general equilibrium question in semiconductor and condensed-matter optical response: if a direct interband system retains a specified amount of low-energy optical spectral weight, how small can the thermal population of the electronic states carrying that response be? Conventional infrared-detector and semiconductor-optics treatments normally answer related questions only after specifying a density of states, absorption model, recombination law, or carrier-generation mechanism.

For independent quasiparticles, we derive an exact finite-temperature inequality for transitions crossing the chemical potential. Combining the transitionwise Fermi-Dirac bound with Kubo-Greenwood response and a basis-invariant singular-value/rank constraint on the selected optical velocity blocks gives

```math
n_e+n_h
\ge
n_{e,\mathcal B}^{act}+n_{h,\mathcal B}^{act}
\ge
\frac{2}{\pi e^2(v_{\mathcal B}^{cap})^2}
\int_{\mathcal B}
\frac{\hbar\omega\,\sigma_1^{cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega.
```

The result is formulated for an arbitrary optical-frequency window and does not require a chosen density of states, parabolic dispersion, Dirac dispersion, equal band degeneracy, or translational invariance. Mirror-symmetric equal-mass parabolic bands provide an exact equality construction for the optically active population, while independent Dirac models provide nontrivial quantitative checks.

We believe the manuscript is appropriate for *Physical Review B* because the central result is a general statement about finite-temperature electronic occupations, optical conductivity, and semiconductor/condensed-matter band structure rather than a device-specific performance model. The manuscript also places the result explicitly relative to established phase-space-filling theory, optical sum rules, low-carrier semiconductor band engineering, and infrared detector material criteria.

The scope of the claim is intentionally limited. The paper does **not** claim a universal dark-current, thermal-generation-rate, detectivity, or finite-bandwidth-noise limit. Neutral excitons, phonon-assisted transitions, interacting many-body spectral functions, transport kinetics, and unconstrained photonic path enhancement require additional physics and are identified explicitly as escape routes or scope boundaries.

### Submission history

[AUTHOR TO COMPLETE: State whether this manuscript, or a substantially related manuscript, has previously been submitted to any Physical Review journal. If none, write: “This manuscript has not previously been submitted to a Physical Review journal.”]

[AUTHOR TO COMPLETE: State whether this is part of a joint submission. If not, write: “This is not a joint submission.”]

### Referees

[OPTIONAL — AUTHOR TO COMPLETE: Recommended referees, with institutional affiliations and email addresses if desired.]

[OPTIONAL — AUTHOR TO COMPLETE: Excluded referees and a concise reason, if any.]

### Author declarations

[AUTHOR TO COMPLETE: Confirm that all listed authors approve the submission and authorship order.]

[AUTHOR TO COMPLETE: Confirm that the manuscript is not under consideration elsewhere, if accurate.]

[AUTHOR TO COMPLETE: Identify any conflicts of interest, funding-related disclosure issues, or other matters that should be brought to the editors’ attention.]

Thank you for considering the manuscript.

Sincerely,

[CORRESPONDING AUTHOR NAME]  
[AFFILIATION]  
[EMAIL]  
[ORCID, optional]

---

## Claim-scope guardrail for future edits

Do not add any of the following to the cover letter without new evidence:

```text
“first” / “novel” / “unprecedented” priority claims;
universal photodetector limit;
universal dark-current floor;
universal D* bound;
universal finite-bandwidth noise bound;
claim that no prior conductivity-to-particle-count result exists.
```

The defensible significance statement is the **specific inverse thermal cross-mu spectral-weight/state-count theorem**, not novelty of its individual ingredients.