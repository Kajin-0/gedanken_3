#!/usr/bin/env python3
"""Discrete optical-depth ladder surrogate for Experiment 02.

This script evaluates the equal-longitudinal-section staircase approximation to
continuous transverse absorption-depth compensation.  It uses the same
90%-absorption and reduced-order residual floor as the current device surrogate.

No Maxwell or TCAD claim is made here.
"""

from math import exp, log, sqrt

B = log(10.0)              # 90% absorption over normalized length U in [0,1]
D_UM = 2.0                 # absorber depth
L_MM = 3.0                 # optical propagation length
T0_PS = 40.0               # d / v0
V0 = 5.0e4                 # m/s
VG = 7.5e7                 # m/s

# Existing combined residual floor from REDUCED_ORDER_DEVICE_SURROGATE_2026-08-13.md
F = 0.03478633258


def truncated_exponential_variance(width: float) -> float:
    """Variance of U within one interval of width `width` for exp(-B U)."""
    x = B * width
    return 1.0 / B**2 - width**2 * exp(x) / (exp(x) - 1.0) ** 2


def truncated_exponential_mean_offset(width: float) -> float:
    """Conditional mean offset from the left edge of an interval."""
    x = B * width
    return 1.0 / B - width / (exp(x) - 1.0)


def full_variance() -> float:
    return truncated_exponential_variance(1.0)


def ladder_stats(n: int) -> dict:
    h = 1.0 / n
    mu = truncated_exponential_mean_offset(h)
    q = [(j * h + mu) for j in range(n)]

    # Because q_j = E[U | section j], the forward quantization residual is
    # orthogonal to Q.  For equal-width sections its conditional variance is
    # the same in every section.
    d_n = truncated_exponential_variance(h)
    a = full_variance()

    # Exact centroid-quantizer identity: Var(U+Q) = 4 Var(U) - 3 Var(U-Q).
    reverse_det = 4.0 * a - 3.0 * d_n

    direct_rms = T0_PS * sqrt(F + a)
    forward_rms = T0_PS * sqrt(F + d_n)
    reverse_rms = T0_PS * sqrt(F + reverse_det)
    continuous_rms = T0_PS * sqrt(F)

    improvement = 1.0 - forward_rms / direct_rms
    continuous_improvement = 1.0 - continuous_rms / direct_rms
    retained = improvement / continuous_improvement

    return {
        "n": n,
        "h": h,
        "q": q,
        "depth_um": [D_UM * x for x in q],
        "section_length_mm": L_MM * h,
        "delay_increment_ps": T0_PS * h,
        "D_N": d_n,
        "direct_rms_ps": direct_rms,
        "forward_rms_ps": forward_rms,
        "reverse_rms_ps": reverse_rms,
        "improvement": improvement,
        "retained": retained,
    }


def systematic_error_budget_ps(n: int, target_improvement: float = 0.30) -> float:
    """Allowed weighted section-to-section mean timing RMS for a target gain.

    A common timing offset is irrelevant.  The returned value is the maximum
    weighted standard deviation of section mean timing errors after removal of
    their weighted mean.
    """
    a = full_variance()
    d_n = truncated_exponential_variance(1.0 / n)
    v_goal = (1.0 - target_improvement) ** 2 * (F + a)
    budget = v_goal - F - d_n
    return 0.0 if budget <= 0.0 else T0_PS * sqrt(budget)


def minimum_n(target_improvement: float) -> int:
    for n in range(1, 10000):
        if ladder_stats(n)["improvement"] >= target_improvement:
            return n
    raise RuntimeError("section search failed")


if __name__ == "__main__":
    a = full_variance()
    direct = T0_PS * sqrt(F + a)
    continuous = T0_PS * sqrt(F)

    print(f"Var(U) = {a:.12f}")
    print(f"direct RMS = {direct:.6f} ps")
    print(f"continuous matched RMS = {continuous:.6f} ps")
    print(f"continuous improvement = {(1-continuous/direct)*100:.4f}%")
    print()

    print(" N   D_N         forward_ps  improvement  retained_ideal  reverse_ps")
    for n in [1, 2, 3, 4, 5, 6, 8, 9, 12]:
        s = ladder_stats(n)
        print(
            f"{n:2d}  {s['D_N']:.9f}  {s['forward_rms_ps']:10.4f}  "
            f"{100*s['improvement']:10.3f}%  {100*s['retained']:12.3f}%  "
            f"{s['reverse_rms_ps']:10.4f}"
        )

    print()
    for target in [0.20, 0.30, 0.40]:
        print(f"minimum N for >= {100*target:.0f}% improvement: {minimum_n(target)}")

    print()
    for n in [3, 4, 6, 8]:
        s = ladder_stats(n)
        err_ps = systematic_error_budget_ps(n, 0.30)
        equiv_depth_nm = V0 * err_ps * 1e-12 * 1e9
        equiv_path_um = VG * err_ps * 1e-12 * 1e6
        print(f"N={n}")
        print(f"  section length = {s['section_length_mm']:.6f} mm")
        print(f"  optical delay increment = {s['delay_increment_ps']:.6f} ps")
        print("  depth centroids (um) = " + ", ".join(f"{z:.6f}" for z in s['depth_um']))
        print(f"  30% gate section-mean error budget = {err_ps:.6f} ps RMS")
        print(f"    pure depth equivalent = {equiv_depth_nm:.3f} nm RMS")
        print(f"    pure optical-path equivalent = {equiv_path_um:.3f} um RMS")
