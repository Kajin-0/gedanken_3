# Information-spectrum stop

**Date:** 2026-08-13
**Status:** EXPERIMENT 01 PUBLICATION PATH CLOSED UNLESS NEW DEVICE PHYSICS APPEARS

## Final reduction

For measured complex responsivity `R(f)` and output-noise PSD `S_n(f)`, define

```math
W(f)=\frac{|R(f)|^2}{S_n(f)}.
```

In consistent input-power units,

```math
W(f)=1/NEP^2(f).
```

For an optical event with spectrum `P(f)`,

```math
I_P(f)=|P(f)|^2W(f).
```

The quantities developed in Experiment 01 are standard consequences of this one spectrum:

```math
\rho_\infty^2=\int I_P(f)\,df,
```

```math
J_\theta=(2\pi)^2\int f^2I_P(f)\,df,
```

and

```math
C(\Delta)=
\frac{\int I_P(f)e^{i2\pi f\Delta}df}
{\int I_P(f)df}.
```

Thus eventual matched-filter SNR is its zeroth moment, timing Fisher information is its second moment, and unknown-arrival correlation is its normalized Fourier transform.

## Retained device result

For a single-pole photoconductor with GR noise plateau `S_GR,0` and white Johnson/readout floor `S_W`,

```math
\tau_{info}=\frac{\tau}{\sqrt{1+S_{GR,0}/S_W}}.
```

This is a useful engineering interpretation: the raw responsivity bandwidth and optimally whitened information bandwidth can differ strongly when GR noise shares the carrier-lifetime pole with the signal.

It is not a new optimum-filter principle.

## Publication disposition

```text
Paper A / Rev. 5: DO NOT SUBMIT as a full research article.
Original theorem: mathematically valid.
Pedagogical/device interpretation: useful.
Research novelty: not established.
```

Prior art already covers unknown-delay matched-filter acquisition, optimum timing with arbitrary stationary noise, sampled pulse processing, RMS/effective timing bandwidth, and photoconductor response/noise/bandwidth tradeoffs.

Do not resume this experiment by renaming `W(f)`, RMS bandwidth, or the timing-cell penalty as new metrics.

## End condition

Experiment 01 is considered scientifically closed unless a genuinely new microscopic detector-physics effect appears that cannot be reduced to the optimum-filter information spectrum above.

The natural next move is a new photodetector gedanken experiment with a device-physics premise, followed by a novelty audit early rather than after manuscript construction.