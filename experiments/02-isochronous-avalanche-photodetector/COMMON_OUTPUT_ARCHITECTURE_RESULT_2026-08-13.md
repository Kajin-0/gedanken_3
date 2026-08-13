# Common-output architecture result

**Date:** 2026-08-13  
**Status:** ARCHITECTURE NARROWING / TIMING-ONLY SEGMENTED BENCHMARK IDENTIFIED / NOVELTY NOT ESTABLISHED

## Equal timing budget

For the current surrogate, remove only the earlier `2 ps RMS` electronics term from the combined floor:

```math
F_{phys}=0.03228633258.
```

Using `T0=40 ps`, `D3=0.0089928`, `D4=0.0051232`, and the historical 30%-improvement target `8.8518 ps RMS`:

```text
N=3: no-readout RMS 8.1269 ps; maximum combined readout RMS 3.5082 ps
N=4: no-readout RMS 7.7366 ps; maximum combined readout RMS 4.3010 ps
continuous map: no-readout RMS 7.1874 ps; maximum combined readout RMS 5.1668 ps
```

Thus the N=3 common-output architecture has only about `3.51 ps RMS` total allowance for frontend, line dispersion, readout skew, pulse-shape distortion, etc. If `2 ps` is already spent in the frontend, only `2.88 ps RMS` remains for additional line/readout effects.

## Architecture comparison

### Lumped common output

Retains passive isochrony but places the full millimeter-scale junction capacitance at one node. With the earlier scale estimate `epsilon_r=13`, `w=1 um`, `Wd=2 um`, the capacitance is about `57.6 fF/mm`; 3 mm gives about `173 fF`. A 50-ohm RC time constant is about `8.63 ps`. This is **not** a jitter prediction, only a warning that a fixed 2-ps electronics assumption is not justified without a real frontend model.

### Electrically segmented and calibrated

From `READOUT_SIDE_INFORMATION_NO_GO_2026-08-13.md`, section identity allows per-section mean timestamp correction. The remaining deterministic spread is exactly the same within-section quantization term `D_N` as the passive N-step ladder.

Therefore on timing alone:

```text
segmented + calibrated is a tie or stronger comparator.
```

No claim of timing-only superiority over a calibrated segmented detector is allowed.

### Traveling-wave common output

Let near-end electrical propagation have velocity `ve`, optical group velocity `vg`, and `r=ve/vg`. Exact continuous mean matching requires

```math
L=L0 r/(1+r),
\qquad L0=3 mm.
```

The matched N-step forward residual remains `D_N`; electrical propagation can supply part of the required deterministic delay without intrinsically increasing the depth-quantization term.

For N=3:

```text
r=1   -> L=1.50 mm, 0.50-mm sections
r=1.5 -> L=1.80 mm, 0.60-mm sections
r=2   -> L=2.00 mm, 0.667-mm sections
r=4   -> L=2.40 mm, 0.80-mm sections
```

The 90%-absorption coefficient required over these lengths is only `ln(10)/L`, i.e. about `1.54`, `1.28`, `1.15`, and `0.96 per mm`, respectively.

## Direction-reversal correction

At fixed physical position, forward matching still gives

```math
dm_r/dx=-2/v_g,
```

independent of deterministic electrical delay.

However the integrated reverse span depends on the shortened matched length:

```math
\boxed{\Delta T_r=2T0\,ve/(ve+vg).}
```

Therefore the earlier `2T0` reverse-span result is only the optical-delay-dominated limit. The causal signature survives, but its magnitude decreases when electrical propagation supplies more of the forward compensation.

With the prior stochastic floor and N=3, reverse RMS is approximately:

```text
ve/vg=1   -> 12.06 ps
ve/vg=1.5 -> 13.62 ps
ve/vg=2   -> 14.73 ps
ve/vg=4   -> 17.06 ps
optical-only limit -> 20.72 ps
```

Forward remains about `8.37 ps` at exact N=3 matching under the same prior assumptions.

## Finite-ladder slope refinement

For fixed centroid depth levels, let

```math
k=L(1/vg+1/ve)/T0.
```

Then

```math
V_N(k)=k^2D_N+(k-1)^2(A-D_N).
```

Exact section-mean isochrony is `k=1`, but minimum deterministic RMS occurs at

```math
k_*=1-D_N/A.
```

For N=3, `k*=0.86198`; for N=4, `k*=0.92137`. This preserves the rule that the conditional-mean isochronous point and the minimum-total-RMS point need not coincide.

## Decision

```text
independent segmented SPADs as primary demonstration: REJECT
segmented/calibrated detector: REQUIRED CONTROL
lumped common-output APD: RETAINED BUT SECONDARY
continuous traveling-wave common-output APD: LEADING ARCHITECTURE
Geiger-mode traveling-wave SPAD: HIGH-RISK FOLLOW-ON
```

Next: determine whether the same timing decomposition can be demonstrated with a normalized **linear-mode APD impulse response**, avoiding Geiger quench/TDC complexity for the first physics test.