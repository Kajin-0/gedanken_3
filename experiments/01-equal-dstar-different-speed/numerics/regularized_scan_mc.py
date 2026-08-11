"""Smooth finite-bandwidth correlated timing-scan prototype for Experiment 01.

This script implements the Step-15 Gaussian information-band regularization.
It does NOT use an independent-trials approximation.

Model
-----
Finite dimensionless template:
    h_x(v) = v exp(-v), 0 <= v <= x

Fourier transform:
    H_x(nu) = [1 - exp(-(1+i nu)x)(1+(1+i nu)x)]/(1+i nu)^2

Regularized noise-weighted timing spectrum:
    J_{x,kappa}(nu) = |H_x(nu)|^2 exp[-(nu/kappa)^2]

The Gaussian factor is an explicit high-frequency information/processing
penalty. It is a controlled smooth regularizer, not an invertible common
low-pass filter and not the exact brick-wall model from Step 14.

The normalized stationary Gaussian timing scan is synthesized periodically
from this spectrum using FFT filtering of white Gaussian samples. The period
is chosen much longer than the search interval and can be enlarged to check
wraparound sensitivity.

Rice / Euler-characteristic high-threshold approximation:
    alpha ~= Q(u) + ell * sigma_nu/(2 pi) * exp(-u^2/2)
where sigma_nu^2 is the second moment of the normalized J spectrum.

All quantities are dimensionless. No result from this script should be called
an exact continuous-time crossover unless grid, period, Monte Carlo tail, and
regularization sensitivity have all been checked.
"""

from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.stats import norm


def H_x(nu: np.ndarray | float, x: float):
    z = 1.0 + 1j * np.asarray(nu)
    return (1.0 - np.exp(-z * x) * (1.0 + z * x)) / z**2


def H_inf(nu: np.ndarray | float):
    z = 1.0 + 1j * np.asarray(nu)
    return 1.0 / z**2


def J_reg(nu: np.ndarray | float, x: float, kappa: float):
    return np.abs(H_x(nu, x)) ** 2 * np.exp(-(np.asarray(nu) / kappa) ** 2)


def _quad_even(fun, kappa: float) -> float:
    upper = max(10.0 * kappa, 50.0)
    val, _ = quad(fun, 0.0, upper, epsabs=1e-10, epsrel=1e-8, limit=300)
    return 2.0 * val


def moments(x: float, kappa: float) -> tuple[float, float]:
    i0 = _quad_even(lambda nu: float(J_reg(nu, x, kappa)), kappa)
    i2 = _quad_even(lambda nu: float(nu * nu * J_reg(nu, x, kappa)), kappa)
    return i0, i2


def eventual_energy(kappa: float) -> float:
    return _quad_even(
        lambda nu: float(np.abs(H_inf(nu)) ** 2 * math.exp(-(nu / kappa) ** 2)),
        kappa,
    )


def rho_fraction(x: float, kappa: float) -> float:
    i0, _ = moments(x, kappa)
    return math.sqrt(i0 / eventual_energy(kappa))


def sigma_nu(x: float, kappa: float) -> float:
    i0, i2 = moments(x, kappa)
    return math.sqrt(i2 / i0)


def rice_threshold(x: float, ell: float, alpha: float, kappa: float) -> float:
    sigma = sigma_nu(x, kappa)

    def equation(u: float) -> float:
        return (
            norm.sf(u)
            + ell * sigma / (2.0 * math.pi) * math.exp(-0.5 * u * u)
            - alpha
        )

    return brentq(equation, 0.0, 12.0)


def rice_detection_time(
    ell: float,
    rho0: float,
    alpha: float,
    beta: float,
    kappa: float,
    xmax: float = 30.0,
) -> float:
    target = norm.ppf(beta)

    def equation(x: float) -> float:
        return (
            rho0 * rho_fraction(x, kappa)
            - rice_threshold(x, ell, alpha, kappa)
            - target
        )

    if equation(xmax) < 0.0:
        return math.inf
    return brentq(equation, 1e-4, xmax)


def periodic_maxima(
    x: float,
    kappa: float,
    ell: float,
    delta: float,
    npaths: int,
    pad: float = 20.0,
    seed: int = 1,
    batch: int = 100,
) -> tuple[np.ndarray, float, int]:
    """Simulate grid-sampled maxima of the smooth correlated process.

    A periodic Gaussian process is synthesized with spectral eigenvalues
    proportional to J_reg. The period is at least 2*ell+2*pad. Increase pad
    to test wraparound sensitivity.
    """
    p_target = 2.0 * ell + 2.0 * pad
    nfft = 1
    while nfft * delta < p_target:
        nfft *= 2
    period = nfft * delta

    nu = 2.0 * math.pi * np.fft.fftfreq(nfft, d=delta)
    spectral = J_reg(nu, x, kappa)
    eigenvalues = spectral / spectral.mean()  # unit variance: mean(lambda)=1
    sqrt_eigenvalues = np.sqrt(eigenvalues)

    n_search = int(math.floor(ell / delta)) + 1
    rng = np.random.default_rng(seed)
    maxima = np.empty(npaths)

    done = 0
    while done < npaths:
        b = min(batch, npaths - done)
        white = rng.standard_normal((b, nfft))
        process = np.fft.ifft(
            np.fft.fft(white, axis=1) * sqrt_eigenvalues,
            axis=1,
        ).real
        maxima[done : done + b] = process[:, :n_search].max(axis=1)
        done += b

    return maxima, period, nfft


def bootstrap_quantile_ci(
    values: np.ndarray,
    q: float,
    reps: int = 200,
    seed: int = 123,
) -> tuple[float, float, float]:
    estimate = float(np.quantile(values, q))
    rng = np.random.default_rng(seed)
    boot = np.empty(reps)
    n = len(values)
    for i in range(reps):
        idx = rng.integers(0, n, size=n)
        boot[i] = np.quantile(values[idx], q)
    lo, hi = np.quantile(boot, [0.025, 0.975])
    return estimate, float(lo), float(hi)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--x", type=float, default=3.7839037723)
    p.add_argument("--kappa", type=float, default=8.0)
    p.add_argument("--ell", type=float, default=54.7488715432)
    p.add_argument("--alpha", type=float, default=0.01)
    p.add_argument("--delta", type=float, default=0.05)
    p.add_argument("--paths", type=int, default=15000)
    p.add_argument("--pad", type=float, default=20.0)
    p.add_argument("--seed", type=int, default=789)
    args = p.parse_args()

    maxima, period, nfft = periodic_maxima(
        args.x,
        args.kappa,
        args.ell,
        args.delta,
        args.paths,
        pad=args.pad,
        seed=args.seed,
    )
    q, lo, hi = bootstrap_quantile_ci(maxima, 1.0 - args.alpha)
    rice = rice_threshold(args.x, args.ell, args.alpha, args.kappa)

    print(f"period={period:.6g} nfft={nfft}")
    print(f"sigma_nu={sigma_nu(args.x, args.kappa):.8g}")
    print(f"MC threshold={q:.8g}  bootstrap95=[{lo:.8g}, {hi:.8g}]")
    print(f"Rice/EC threshold={rice:.8g}")


if __name__ == "__main__":
    main()
