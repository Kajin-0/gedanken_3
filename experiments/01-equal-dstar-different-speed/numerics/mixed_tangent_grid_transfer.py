#!/usr/bin/env python3
"""Step 48: paired finite-level transfer from the mixed rough tangent to alpha=1.

At the hard-window rough endpoint the finite-u tangent is

    W_chi(t) = sqrt(2) Z t - t^2
               + 2^(3/4) sqrt(chi) B(t)
               - sqrt(2) chi |t|.

A physical grid dt maps to tangent spacing

    Delta = u sqrt(b) dt / sqrt(2),

and the pure alpha=1 canonical spacing is

    delta = sqrt(2) chi Delta = a u^2 dt.

This helper estimates the generalized discrete Dieker-Yakir constants on
nested mixed-tangent grids Delta and Delta/sub using common Brownian paths,
then compares the paired ratio against the exact alpha=1 finite-grid ratio.

The default calculation uses three independent seeds x 3000 paths = 9000
paired paths and sub=128, matching Step 48. The resulting Monte Carlo interval
is not a distribution-free finite-sample theorem.
"""

from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.special import zeta


RHO_FULL = 6.2407571
BETA_DET = 0.90


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0*x)*(1.0 + 2.0*x + 2.0*x*x)


def rough_coefficients(x: float) -> tuple[float, float]:
    e = eta(x)
    a = 2.0*x*x*math.exp(-2.0*x)/e
    b = (1.0 + math.exp(-2.0*x)*(2.0*x*x - 2.0*x - 1.0))/e
    return a, b


def normal_ppf_09() -> float:
    # fixed standard-normal 90th percentile used throughout the experiment
    return 1.2815515655446004


def detector_threshold(x: float) -> float:
    return RHO_FULL*math.sqrt(eta(x)) - normal_ppf_09()


def nu_small_x(x: float) -> float:
    """Alpha=1 Gaussian overshoot function for the tiny x used here.

    The Step-47 expansion has errors far below the precision needed here for
    x < 0.002.
    """
    beta = -float(zeta(0.5, 1.0))/math.sqrt(2.0*math.pi)
    c3 = -float(zeta(-0.5, 1.0))/(24.0*math.sqrt(2.0*math.pi))
    c5 = float(zeta(-1.5, 1.0))/(640.0*math.sqrt(2.0*math.pi))
    log_nu = -beta*x + c3*x**3 + c5*x**5
    return math.exp(log_nu)


def dy_ratio(Wp: np.ndarray, Wn: np.ndarray, spacing: float) -> np.ndarray:
    b = Wp.shape[0]
    peak = np.maximum.reduce([Wp.max(axis=1), Wn.max(axis=1), np.zeros(b)])
    S = spacing*(
        np.exp(-peak)
        + np.exp(Wp-peak[:, None]).sum(axis=1)
        + np.exp(Wn-peak[:, None]).sum(axis=1)
    )
    return 1.0/S


def one_seed(
    *,
    seed: int,
    paths: int,
    X: float,
    physical_dt: float,
    sub: int,
    T: float,
    batch: int,
) -> dict[str, np.ndarray | float]:
    a, bcoef = rough_coefficients(X)
    u = detector_threshold(X)
    chi = a*u/math.sqrt(bcoef)
    Delta = u*math.sqrt(bcoef)*physical_dt/math.sqrt(2.0)
    delta = a*u*u*physical_dt

    fine_dt = Delta/sub
    n = int(round(T/fine_dt))
    t = np.arange(1, n+1, dtype=float)*fine_dt

    sigma = 2.0**0.75*math.sqrt(chi)
    rough_drift = math.sqrt(2.0)*chi

    rng = np.random.default_rng(seed)
    coarse_rows: list[np.ndarray] = []
    fine_rows: list[np.ndarray] = []

    coarse_idx = np.arange(sub-1, n, sub)

    for start in range(0, paths, batch):
        bs = min(batch, paths-start)
        Z = rng.standard_normal(bs)

        Bp = np.cumsum(
            rng.standard_normal((bs, n))*math.sqrt(fine_dt), axis=1
        )
        Bn = np.cumsum(
            rng.standard_normal((bs, n))*math.sqrt(fine_dt), axis=1
        )

        common = -t*t - rough_drift*t
        Wp = math.sqrt(2.0)*Z[:, None]*t[None, :] + sigma*Bp + common[None, :]
        Wn = -math.sqrt(2.0)*Z[:, None]*t[None, :] + sigma*Bn + common[None, :]

        coarse_rows.append(dy_ratio(Wp[:, coarse_idx], Wn[:, coarse_idx], Delta))
        fine_rows.append(dy_ratio(Wp, Wn, fine_dt))

    coarse = np.concatenate(coarse_rows)
    fine = np.concatenate(fine_rows)

    H1_coarse = nu_small_x(math.sqrt(2.0*delta))
    H1_fine = nu_small_x(math.sqrt(2.0*delta/sub))
    pure_ratio = H1_coarse/H1_fine

    return {
        "coarse": coarse,
        "fine": fine,
        "u": u,
        "a": a,
        "b": bcoef,
        "chi": chi,
        "Delta": Delta,
        "delta": delta,
        "fine_dt": fine_dt,
        "H1_coarse": H1_coarse,
        "H1_fine": H1_fine,
        "pure_ratio": pure_ratio,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.16)
    p.add_argument("--physical-dt", type=float, default=.001)
    p.add_argument("--sub", type=int, default=128)
    p.add_argument("--T", type=float, default=4.0)
    p.add_argument("--paths-per-seed", type=int, default=3000)
    p.add_argument("--batch", type=int, default=20)
    p.add_argument("--seeds", default="777,778,779")
    args = p.parse_args()

    seeds = [int(s) for s in args.seeds.split(",") if s.strip()]
    rows = [
        one_seed(
            seed=s,
            paths=args.paths_per_seed,
            X=args.X,
            physical_dt=args.physical_dt,
            sub=args.sub,
            T=args.T,
            batch=args.batch,
        )
        for s in seeds
    ]

    coarse = np.concatenate([r["coarse"] for r in rows])
    fine = np.concatenate([r["fine"] for r in rows])
    n = len(coarse)

    coarse_mean = float(coarse.mean())
    fine_mean = float(fine.mean())
    mixed_ratio = coarse_mean/fine_mean
    mixed_loss = 1.0-mixed_ratio

    diff = fine-coarse
    mixed_loss_se = float(diff.std(ddof=1)/math.sqrt(n)/fine_mean)

    pure_ratio = float(rows[0]["pure_ratio"])
    pure_loss = 1.0-pure_ratio

    # Low-variance paired transfer statistic. Its expectation is
    # H_mix^coarse - pure_ratio * H_mix^fine.
    transfer_sample = coarse-pure_ratio*fine
    transfer_residual = mixed_ratio-pure_ratio
    transfer_se = float(
        transfer_sample.std(ddof=1)/math.sqrt(n)/fine_mean
    )

    r0 = rows[0]
    eps_par = float(r0["Delta"])**2/4.0

    print("Step-48 mixed-tangent finite-level transfer")
    print(f"paths={n} seeds={seeds} sub={args.sub} T={args.T:g}")
    print(f"u={float(r0['u']):.12f}")
    print(f"a_X={float(r0['a']):.12e}")
    print(f"b_X={float(r0['b']):.12f}")
    print(f"chi={float(r0['chi']):.12e}")
    print(f"Delta={float(r0['Delta']):.12e}")
    print(f"delta={float(r0['delta']):.12e}")
    print(f"parabolic cell bulge Delta^2/4={eps_par:.12e}")
    print()
    print(f"H_mix^Delta={coarse_mean:.12f}")
    print(f"H_mix^(Delta/sub)={fine_mean:.12f}")
    print(f"mixed coarse/fine ratio={mixed_ratio:.12f}")
    print(f"mixed coarse/fine loss={mixed_loss:.12e}")
    print(f"paired SE of mixed loss={mixed_loss_se:.12e}")
    print()
    print(f"H1^delta={float(r0['H1_coarse']):.12f}")
    print(f"H1^(delta/sub)={float(r0['H1_fine']):.12f}")
    print(f"pure coarse/fine ratio={pure_ratio:.12f}")
    print(f"pure coarse/fine loss={pure_loss:.12e}")
    print()
    print(f"transfer residual mixed_ratio-pure_ratio={transfer_residual:.12e}")
    print(f"paired SE transfer residual={transfer_se:.12e}")
    print(
        "approx normal 95% transfer interval=["
        f"{transfer_residual-1.96*transfer_se:.12e}, "
        f"{transfer_residual+1.96*transfer_se:.12e}]"
    )
    print(
        "NOTE: this interval is a paired Monte Carlo diagnostic, not a "
        "distribution-free finite-sample theorem."
    )


if __name__ == "__main__":
    main()
