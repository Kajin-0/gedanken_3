#!/usr/bin/env python3
"""Step-23 occupation-time importance sampling for the kappa=infinity rough limit.

For the hard-window template

    h_x(t) = t exp(-t) 1_[0,x](t),

the infinite-information-band timing scan is continuous but nondifferentiable.
Upcrossing counts are therefore not a robust exact rare-event object.

Instead define the excursion occupation time

    V_u = integral_0^ell 1{z(t) > u} dt.

Choose T uniformly on [0,ell] and sample the stationary Gaussian path
conditional on z(T)>u. The resulting proposal satisfies

    dQ_occ/dP = V_u / [ell Q(u)],

hence exactly

    P(sup z > u) = ell Q(u) E_Qocc[1/V_u].

The implementation below approximates the continuous occupation integral on a
fine timing grid and synthesizes the stationary Gaussian process by FFT from
the exact unregularized template spectrum. It is a numerical validator for the
controlled thought experiment, not a literal electronics model.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.stats import norm


RHO_FULL_DEFAULT = 6.2407571
BETA_DEFAULT = 0.90
ALPHA_DEFAULT = 1e-6


def eta(x: float) -> float:
    return 1.0 - math.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def H_x(omega: np.ndarray, x: float) -> np.ndarray:
    z = 1.0 + 1j * omega
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / (z * z)


def available_threshold(
    x: float,
    rho_full: float = RHO_FULL_DEFAULT,
    beta: float = BETA_DEFAULT,
) -> float:
    rho = rho_full * math.sqrt(eta(x))
    return rho - float(norm.ppf(beta))


@dataclass
class PeriodicRoughModel:
    delta: float
    period: float
    sqrt_eig: np.ndarray
    covariance: np.ndarray


def build_periodic_model(
    x: float,
    delta: float,
    period_target: float = 16.0,
) -> PeriodicRoughModel:
    if x <= 0.0 or delta <= 0.0 or period_target <= 0.0:
        raise ValueError("x, delta, and period_target must be positive")

    n_target = int(math.ceil(period_target / delta))
    nfft = 1
    while nfft < n_target:
        nfft *= 2

    period = nfft * delta
    omega = 2.0 * math.pi * np.fft.fftfreq(nfft, d=delta)

    eig = np.abs(H_x(omega, x)) ** 2
    eig = eig / eig.mean()  # unit sampled variance

    sqrt_eig = np.sqrt(eig)
    covariance = np.fft.ifft(eig).real

    return PeriodicRoughModel(
        delta=delta,
        period=period,
        sqrt_eig=sqrt_eig,
        covariance=covariance,
    )


def occupation_false_alarm(
    *,
    x: float,
    ell: float,
    u: float,
    target_delta: float = 0.002,
    period_target: float = 16.0,
    n_paths: int = 10000,
    batch_size: int = 20,
    seed: int = 0,
) -> dict[str, float]:
    """Estimate P(sup_[0,ell] z > u) with occupation-time importance sampling."""
    if x <= 0.0 or ell <= 0.0 or target_delta <= 0.0:
        raise ValueError("x, ell, and target_delta must be positive")
    if n_paths <= 1 or batch_size <= 0:
        raise ValueError("n_paths must exceed one and batch_size must be positive")

    n_intervals = max(10, int(round(ell / target_delta)))
    delta = ell / n_intervals
    model = build_periodic_model(x, delta, period_target)

    nfft = len(model.sqrt_eig)
    offsets = np.arange(-n_intervals, n_intervals + 1)
    idx = offsets % nfft
    cov = model.covariance[idx]

    q_tail = float(norm.sf(u))
    rng = np.random.default_rng(seed)

    sum_w = 0.0
    sum_w2 = 0.0
    sum_occ = 0.0

    for start in range(0, n_paths, batch_size):
        b = min(batch_size, n_paths - start)

        white = rng.standard_normal((b, nfft))
        process = np.fft.ifft(
            np.fft.fft(white, axis=1) * model.sqrt_eig[None, :],
            axis=1,
        ).real

        # If Y ~ N(0,1) conditional on Y>u, then Q(Y)=U Q(u).
        y_cond = norm.isf(rng.random(b) * q_tail)

        # Condition the stationary Gaussian field at the selected point (index 0).
        local = (
            process[:, idx]
            + cov[None, :] * (y_cond - process[:, 0])[:, None]
        )

        # The selected exceedance time is uniform over the physical search interval.
        selected = rng.integers(0, n_intervals + 1, size=b)

        for j in range(b):
            m = int(selected[j])
            left = n_intervals - m
            segment = local[j, left : left + n_intervals + 1]

            indicator = (segment > u).astype(float)
            occupation = delta * (
                0.5 * indicator[0]
                + float(indicator[1:-1].sum())
                + 0.5 * indicator[-1]
            )

            # The conditioned selected point lies above u, so a zero occupation is
            # only a finite-grid pathology. Keep a conservative half-cell floor.
            if occupation <= 0.0:
                occupation = 0.5 * delta

            weight = ell * q_tail / occupation
            sum_w += weight
            sum_w2 += weight * weight
            sum_occ += occupation

    pfa = sum_w / n_paths
    variance = (sum_w2 - n_paths * pfa * pfa) / (n_paths - 1)
    pfa_se = math.sqrt(max(variance, 0.0) / n_paths)

    return {
        "false_alarm": pfa,
        "false_alarm_se": pfa_se,
        "false_alarm_over_alpha_default": pfa / ALPHA_DEFAULT,
        "mean_occupation": sum_occ / n_paths,
        "delta": delta,
        "period": model.period,
        "n_paths": float(n_paths),
    }


def evaluate_r2_boundary_candidate(
    *,
    X: float = 7.7528,
    Lambda: float = 0.90513,
    rho_full: float = RHO_FULL_DEFAULT,
    beta: float = BETA_DEFAULT,
    target_delta: float = 0.002,
    period_target: float = 16.0,
    n_paths: int = 10000,
    seed: int = 0,
) -> dict[str, dict[str, float]]:
    r = 2.0

    x_fast = X
    x_slow = X / r
    ell_fast = Lambda
    ell_slow = Lambda / r

    u_fast = available_threshold(x_fast, rho_full, beta)
    u_slow = available_threshold(x_slow, rho_full, beta)

    fast = occupation_false_alarm(
        x=x_fast,
        ell=ell_fast,
        u=u_fast,
        target_delta=target_delta,
        period_target=period_target,
        n_paths=n_paths,
        seed=seed,
    )
    slow = occupation_false_alarm(
        x=x_slow,
        ell=ell_slow,
        u=u_slow,
        target_delta=target_delta,
        period_target=period_target,
        n_paths=n_paths,
        seed=seed + 1,
    )

    fast["x"] = x_fast
    fast["ell"] = ell_fast
    fast["u_available"] = u_fast

    slow["x"] = x_slow
    slow["ell"] = ell_slow
    slow["u_available"] = u_slow

    return {"fast": fast, "slow": slow}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--X", type=float, default=7.7528)
    p.add_argument("--Lambda", type=float, default=0.90513)
    p.add_argument("--rho-full", type=float, default=RHO_FULL_DEFAULT)
    p.add_argument("--beta", type=float, default=BETA_DEFAULT)
    p.add_argument("--delta", type=float, default=0.002)
    p.add_argument("--period", type=float, default=16.0)
    p.add_argument("--paths", type=int, default=10000)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()

    result = evaluate_r2_boundary_candidate(
        X=args.X,
        Lambda=args.Lambda,
        rho_full=args.rho_full,
        beta=args.beta,
        target_delta=args.delta,
        period_target=args.period,
        n_paths=args.paths,
        seed=args.seed,
    )

    for detector, values in result.items():
        print(detector)
        for key, value in values.items():
            print(f"  {key}: {value}")
        print(
            f"  false_alarm_over_alpha: "
            f"{values['false_alarm'] / ALPHA_DEFAULT}"
        )


if __name__ == "__main__":
    main()
