#!/usr/bin/env python3
"""Step-43 short successful-cluster Gaussian bound.

A successful lower-level component shorter than L0 must contain two points
within lag <L0 whose values differ by the full amplitude gap Delta, with the
upper point already near the rare decision threshold u. A fine deterministic
time net plus a conservative short-lag correlation floor reduces this to a
union of discordant bivariate-Gaussian events.

The probability inequality is analytic conditional on the supplied numerical
covariance floor rho_star and local increment-metric envelope K_star.
"""

from __future__ import annotations

import math
from scipy.stats import norm


ALPHA = 1.0e-6
ELL = 0.895
U_LEVEL = 4.95898348
DELTA = 0.15
L0 = 0.02
H = 1.0e-5
GAMMA = 0.0025
RHO_STAR = 0.99980
K_STAR = 2.0e-4


def pair_upper(u: float, a: float, gamma: float, rho: float) -> tuple[float, float]:
    U = u - gamma
    A = a + gamma
    s = math.sqrt(1.0 - rho * rho)
    z = (A - rho * U) / s
    p = float(norm.sf(U) * norm.cdf(z))
    return p, z


def net_counts(ell: float, h: float, L0: float) -> tuple[int, int, int]:
    n_t = math.ceil(ell / h) + 1
    n_neighbor = 2 * math.ceil((L0 + 2.0 * h) / h) + 1
    return n_t, n_neighbor, n_t * n_neighbor


def log10_modulus_failure(
    *, ell: float, h: float, gamma: float, K: float
) -> float:
    n_t = math.ceil(ell / h) + 1
    m_h = math.sqrt(2.0 * K * h / math.pi)
    exponent = (gamma - m_h) ** 2 / (2.0 * K * h)
    return math.log10(2.0 * n_t) - exponent / math.log(10.0)


def main() -> None:
    a = U_LEVEL - DELTA
    pair, zcond = pair_upper(U_LEVEL, a, GAMMA, RHO_STAR)
    n_t, n_neighbor, n_pair = net_counts(ELL, H, L0)
    pair_union = n_pair * pair
    log_mod = log10_modulus_failure(
        ell=ELL,
        h=H,
        gamma=GAMMA,
        K=K_STAR,
    )

    print("Step-43 short-cluster oscillation envelope")
    print(f"u={U_LEVEL:.8f}")
    print(f"a={a:.8f}")
    print(f"Delta={DELTA:g}, L0={L0:g}, h={H:g}, gamma={GAMMA:g}")
    print(f"rho_star={RHO_STAR:.8f}, K_star={K_STAR:.3e}")
    print()
    print(f"N_time={n_t}")
    print(f"N_neighbor={n_neighbor}")
    print(f"N_pair<={n_pair}")
    print(f"conditional z={zcond:.8f}")
    print(f"pair probability upper={pair:.12e}")
    print(f"pair-union upper={pair_union:.12e}")
    print(f"pair-union / alpha={pair_union/ALPHA:.12e}")
    print(f"log10 modulus-failure upper={log_mod:.3f}")
    print()
    print(
        "Interpretation: the modulus term is negligible; the displayed pair-union "
        "bound is already a conservative upper envelope for P(C_short>=1), "
        "conditional on rho_star and K_star."
    )


if __name__ == "__main__":
    main()
