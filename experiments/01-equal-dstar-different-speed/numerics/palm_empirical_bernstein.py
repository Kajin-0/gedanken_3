#!/usr/bin/env python3
"""Step-42 finite-sample concentration diagnostic for the occupation-Palm estimator.

The implemented Step-33 finite-grid contribution is

    Y = m_a S / L,

with L >= delta_t/2, hence

    0 <= Y <= B = 2 m_a / delta_t.

This script evaluates the Maurer-Pontil empirical-Bernstein radius from the
reported rough-endpoint mean/SE and compares it with duration-truncated support
bounds B0=m_a/L0.

The truncated sample-size projections use the current raw sample SD only as a
planning proxy; they are not certificates for a future truncated run.
"""

from __future__ import annotations

import argparse
import math
from statistics import NormalDist


ALPHA = 1.0e-6
RHO_FULL = 6.2407571
BETA = 0.90


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def qtail(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def empirical_bernstein_radius(
    *, sample_sd: float, support: float, n: int, failure_prob: float
) -> tuple[float, float, float]:
    """Maurer-Pontil one-sided empirical-Bernstein radius for [0,support]."""
    logterm = math.log(2.0 / failure_prob)
    variance_term = math.sqrt(2.0 * sample_sd * sample_sd * logterm / n)
    range_term = 7.0 * support * logterm / (3.0 * (n - 1))
    return variance_term + range_term, variance_term, range_term


def projected_n(
    *, sample_sd_proxy: float, support: float, failure_prob: float, target: float
) -> int:
    """Planning-only n using a fixed SD proxy."""
    n = 2
    while True:
        radius, _, _ = empirical_bernstein_radius(
            sample_sd=sample_sd_proxy,
            support=support,
            n=n,
            failure_prob=failure_prob,
        )
        if radius <= target:
            return n
        # accelerate search once n is large
        n += 1 if n < 10000 else 1000


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--Lambda", type=float, default=0.895)
    p.add_argument("--gap", type=float, default=0.15)
    p.add_argument("--grid-dt", type=float, default=0.001)
    p.add_argument("--n", type=int, default=50000)
    p.add_argument("--mean-alpha", type=float, default=0.98968)
    p.add_argument("--se-alpha", type=float, default=0.00429)
    p.add_argument("--failure", type=float, default=0.05)
    p.add_argument("--grid-allowance-alpha", type=float, default=0.002)
    p.add_argument("--L0", type=float, default=0.02)
    p.add_argument("--family-nodes", type=int, default=17)
    args = p.parse_args()

    z_beta = NormalDist().inv_cdf(BETA)
    u = RHO_FULL * math.sqrt(eta(args.X)) - z_beta
    a = u - args.gap
    qa = qtail(a)
    m_a = args.Lambda * qa

    mean = args.mean_alpha * ALPHA
    se_mean = args.se_alpha * ALPHA
    sample_sd = se_mean * math.sqrt(args.n)

    support = 2.0 * m_a / args.grid_dt
    radius, vterm, rterm = empirical_bernstein_radius(
        sample_sd=sample_sd,
        support=support,
        n=args.n,
        failure_prob=args.failure,
    )

    family_failure = args.failure / args.family_nodes
    family_radius, _, _ = empirical_bernstein_radius(
        sample_sd=sample_sd,
        support=support,
        n=args.n,
        failure_prob=family_failure,
    )

    margin = (1.0 - args.mean_alpha - args.grid_allowance_alpha) * ALPHA

    print("Step-42 raw occupation-Palm empirical Bernstein")
    print(f"u={u:.10f}  a={a:.10f}")
    print(f"Q(a)={qa:.12e}  m_a={m_a:.12e}")
    print(f"support B={support:.12e}")
    print(f"sample SD from quoted SE={sample_sd:.12e}")
    print(f"B/sample_SD={support/sample_sd:.3f}")
    print()
    print(f"variance term / alpha = {vterm/ALPHA:.8f}")
    print(f"range term / alpha    = {rterm/ALPHA:.8f}")
    print(f"total radius / alpha  = {radius/ALPHA:.8f}")
    print(f"upper mean / alpha    = {(mean+radius)/ALPHA:.8f}")
    print(
        f"familywise ({args.family_nodes} nodes) radius/alpha = "
        f"{family_radius/ALPHA:.8f}"
    )
    print(f"available endpoint margin/alpha = {margin/ALPHA:.8f}")

    logterm = math.log(2.0 / args.failure)
    range_only_n = math.ceil(
        1.0 + 7.0 * support * logterm / (3.0 * margin)
    )
    print(f"range-term-only required n ~= {range_only_n}")
    print(
        "projected total n with current SD as fixed planning proxy ~= "
        f"{projected_n(sample_sd_proxy=sample_sd, support=support, failure_prob=args.failure, target=margin)}"
    )

    B0 = m_a / args.L0
    tradius, tv, tr = empirical_bernstein_radius(
        sample_sd=sample_sd,
        support=B0,
        n=args.n,
        failure_prob=args.failure,
    )
    print("\nDuration-truncated planning diagnostic")
    print(f"L0={args.L0:g}  support B0={B0:.12e}  reduction={support/B0:.2f}x")
    print(f"range term / alpha at current n = {tr/ALPHA:.8f}")
    print(
        "total radius / alpha using raw SD only as proxy = "
        f"{tradius/ALPHA:.8f}"
    )
    print(
        "projected n with raw SD proxy = "
        f"{projected_n(sample_sd_proxy=sample_sd, support=B0, failure_prob=args.failure, target=margin)}"
    )

    print(
        "\nExact event decomposition for the proposed truncated estimator:\n"
        "    P_FA <= E[C_long] + P(C_short >= 1).\n"
        "The second term is not bounded by this helper; it is the next Gaussian "
        "short-time excursion problem."
    )


if __name__ == "__main__":
    main()
