# Hg isotope crossover feasibility

**Date:** 2026-08-13

Use a thin HgCdTe epilayer and reversible saturated-Hg isotope anneals rather than separately grown isotope crystals.

Published lattice Hg self diffusion:
`D_Hg = 2e-4 exp[-1.1 eV/(kT)] cm^2/s`.
Published Hg-vacancy diffusion for Hg0.8Cd0.2Te:
`D_V = 2e-3 exp[-0.44 eV/(kT)] cm^2/s`.

At 250 C:
`D_Hg ~= 5.06e-15 cm^2/s`,
`D_V ~= 1.15e-7 cm^2/s`,
so `D_V/D_Hg ~= 2.3e7`.
Vacancy diffusion length in 1 h is ~288 um.

For an ideal constant-surface isotope step and semi-infinite lattice diffusion, a 96-h 250-C enriched-Hg anneal gives average isotope substitution of approximately:

`0.2 um layer -> 86.6%`
`0.3 um layer -> 80.2%`
`0.5 um layer -> 68.1%`
`1.0 um layer -> 45.0%`.

After an equal-duration reverse natural-Hg anneal, ideal residual enriched fraction is approximately:

`0.2 um -> 3.9%`
`0.3 um -> 5.7%`
`0.5 um -> 8.7%`.

Thus an A-B-A same-specimen test is plausible in a deliberately thin material sample:
`natural Hg -> 204Hg -> natural Hg`, with Raman and carrier lifetime after each step.

The key advantage is timescale separation: vacancies can equilibrate through the thin layer much faster than the isotope profile changes. Both anneals must nevertheless use matched Hg chemical potential and vacancy density must be checked independently.

For a 0.2-um layer the 86.6% exchange would convert the ideal Hg-only natural->204Hg HgTe-like phonon shift (~-0.325%) into about a -0.28% layer-average shift, roughly -0.40 cm^-1 for a 143 cm^-1 mode. This should be verified directly by Raman, not assumed.

Required controls: natural-Hg repeat-anneal control, Eg/cutoff after every anneal, Hall or other vacancy proxy, Raman mode frequency/linewidth, and SIMS on sacrificial sister pieces to verify isotope depth profiles.

This route only probes the Hg isotope axis. A positive reversible result would justify the much harder Cd/Te isotope-axis experiment; a null result at <~1% lifetime change would likely close Experiment 07 as a practical diagnostic.
