"""Reduced-order Maxwell-to-transport surrogate for the isochronous APD concept.

This is not a full Maxwell or TCAD simulation. It preserves the exact timing
variance decomposition while replacing the Maxwell absorption map by a
parameterized distributed-absorption coordinate U and the carrier transport by
constant-drift inverse-Gaussian first-passage statistics.

The script compares four controls:
  1. direct/unmapped depth-sensitive detector;
  2. forward depth-mapped isochronous detector;
  3. decorrelated traveling-wave control with identical optical/carrier marginals;
  4. reverse-illuminated anti-matched detector.

It also evaluates the 30% RMS-improvement avalanche-jitter budget and the
bias/velocity shift of the total-jitter minimum.
"""

from __future__ import annotations

import math
import numpy as np

SEED = 20260813
N = 1_000_000

# First realistic InGaAs/InP scale already used in the experiment notes.
d = 2.0e-6                # absorber depth [m]
v0 = 5.0e4                # design carrier drift speed [m/s]
vg = 7.5e7                # optical group velocity [m/s]
eta = 0.90                 # total useful distributed absorption
sigma_perp = 100e-9        # unresolved local absorption-depth RMS [m]
Pe0 = 100.0                # design carrier Peclet number
sigma_avalanche = 5e-12    # RMS avalanche-build-up placeholder [s]
sigma_electronics = 2e-12  # RMS electronics/threshold floor [s]
sigma_optical = 1e-12      # RMS optical pulse/dispersion floor [s]

T0 = d / v0
L = d * vg / v0
D0 = v0 * d / Pe0
b = -math.log(1.0 - eta)

# Truncated-exponential distributed-absorption moments for U=X/L in [0,1].
mean_u = 1.0 / b - 1.0 / (math.exp(b) - 1.0)
var_u = 1.0 / b**2 - math.exp(b) / (math.exp(b) - 1.0) ** 2
mean_remaining = 1.0 - mean_u

# Dimensionless design-point variance components in units of T0^2.
A = var_u
var_perp = (sigma_perp / d) ** 2
var_diff = 2.0 * mean_remaining / Pe0
var_av = (sigma_avalanche / T0) ** 2
var_e = (sigma_electronics / T0) ** 2
var_opt = (sigma_optical / T0) ** 2
floor = var_perp + var_diff + var_av + var_e + var_opt


def rms_ps(var_norm: float) -> float:
    return math.sqrt(var_norm) * T0 * 1e12


def analytic_summary() -> None:
    direct = floor + A
    forward = floor
    decorrelated = floor + 2.0 * A
    reverse = floor + 4.0 * A

    print("design")
    print(f"  T0_ps = {T0 * 1e12:.6f}")
    print(f"  L_mm = {L * 1e3:.6f}")
    print(f"  mean_u = {mean_u:.12f}")
    print(f"  var_u = {var_u:.12f}")
    print(f"  floor_norm = {floor:.12f}")
    print("analytic_rms_ps")
    print(f"  direct = {rms_ps(direct):.6f}")
    print(f"  forward = {rms_ps(forward):.6f}")
    print(f"  decorrelated = {rms_ps(decorrelated):.6f}")
    print(f"  reverse = {rms_ps(reverse):.6f}")
    print(f"  direct_to_forward_improvement = {1.0 - math.sqrt(forward/direct):.6%}")
    print(f"  decorrelated_to_forward_improvement = {1.0 - math.sqrt(forward/decorrelated):.6%}")


def sample_u(rng: np.random.Generator, n: int) -> np.ndarray:
    q = rng.random(n)
    return -np.log(1.0 - q * (1.0 - math.exp(-b))) / b


def first_passage(rng: np.random.Generator, u: np.ndarray) -> np.ndarray:
    ell = d * (1.0 - u)
    positive = ell > 0.0
    mu = np.maximum(ell / v0, 1e-18)
    shape = np.maximum(ell**2 / (2.0 * D0), 1e-24)
    t = rng.wald(mu, shape)
    t[~positive] = 0.0
    return t


def monte_carlo() -> None:
    rng = np.random.default_rng(SEED)
    u = sample_u(rng, N)
    transit = first_passage(rng, u)
    local = rng.normal(0.0, sigma_perp / v0, N)
    common_sigma = math.sqrt(
        sigma_avalanche**2 + sigma_electronics**2 + sigma_optical**2
    )
    other = rng.normal(0.0, common_sigma, N)

    direct = transit + local + other
    forward = u * T0 + transit + local + other
    reverse = (1.0 - u) * T0 + transit + local + other

    # Keep the same optical and carrier marginals but destroy their correlation.
    u2 = sample_u(rng, N)
    transit2 = first_passage(rng, u2)
    local2 = rng.normal(0.0, sigma_perp / v0, N)
    other2 = rng.normal(0.0, common_sigma, N)
    decorrelated = u * T0 + transit2 + local2 + other2

    print("monte_carlo_rms_ps")
    for name, t in (
        ("direct", direct),
        ("forward", forward),
        ("decorrelated", decorrelated),
        ("reverse", reverse),
    ):
        print(f"  {name} = {np.std(t) * 1e12:.6f}")
    print(
        "  direct_to_forward_improvement = "
        f"{1.0 - np.std(forward) / np.std(direct):.6%}"
    )


def avalanche_budget(target_improvement: float = 0.30) -> None:
    k = (1.0 - target_improvement) ** 2
    floor_max = k / (1.0 - k) * A
    print(f"avalanche_budget_for_{target_improvement:.0%}_improvement")
    print("  Pe,avalanche_rms_max_ps")
    for Pe in (20, 30, 50, 75, 100, 150, 200, 300):
        non_av = var_perp + 2.0 * mean_remaining / Pe + var_e + var_opt
        remaining = floor_max - non_av
        av_ps = T0 * math.sqrt(remaining) * 1e12 if remaining > 0.0 else 0.0
        print(f"  {Pe},{av_ps:.6f}")


def velocity_optimum() -> None:
    # Hold D approximately fixed over a modest bias/velocity sweep. With
    # r=v/v0 and s=1/r, the forward normalized variance is
    # A(1-s)^2 + a s^2 + beta s^3 + c.
    a = var_perp
    beta = 2.0 * mean_remaining / Pe0
    c = var_av + var_e + var_opt

    disc = (A + a) ** 2 + 6.0 * A * beta
    s_star = (-(A + a) + math.sqrt(disc)) / (3.0 * beta)
    r_star = 1.0 / s_star

    def forward_var(r: float) -> float:
        return A * (1.0 - 1.0 / r) ** 2 + a / r**2 + beta / r**3 + c

    print("velocity_sweep")
    print("  assumption = D held fixed locally while v changes")
    print("  deterministic_match_r = 1.000000")
    print(f"  total_jitter_minimum_r = {r_star:.6f}")
    print(f"  rms_at_match_ps = {rms_ps(forward_var(1.0)):.6f}")
    print(f"  rms_at_total_min_ps = {rms_ps(forward_var(r_star)):.6f}")
    for r in (0.8, 0.9, 1.0, 1.1, 1.2, r_star, 1.4):
        print(f"  r={r:.6f},forward_rms_ps={rms_ps(forward_var(r)):.6f}")


def map_mismatch_tolerance() -> None:
    # q scales the designed optical-delay span relative to the exact match.
    # At design carrier velocity, V_f/T0^2 = floor + A(q-1)^2.
    print("map_mismatch_tolerance")
    for target in (0.20, 0.30, 0.40):
        k = (1.0 - target) ** 2
        rhs = (k * (floor + A) - floor) / A
        delta = math.sqrt(rhs) if rhs > 0.0 else 0.0
        print(f"  target={target:.0%},abs_q_minus_1_max={delta:.6f}")


if __name__ == "__main__":
    analytic_summary()
    monte_carlo()
    avalanche_budget()
    velocity_optimum()
    map_mismatch_tolerance()
