"""Randomized finite-dimensional stress tests for Experiment 12.

This is not a proof.  It is a bookkeeping/normalization check against arbitrary
asymmetric one-particle spectra, dense complex velocity matrices, and random
spectral windows.

The analytic theorem should imply ratio <= 1 in every trial.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(120814)


def fermi(E: np.ndarray, T: float) -> np.ndarray:
    return 1.0 / (np.exp(E / T) + 1.0)


def cross_trial(nv: int, nc: int, T: float) -> float:
    """Return theorem lower bound / exact thermal excitation count."""
    Ev = -RNG.uniform(0.02, 8.0, size=nv)
    Ec = RNG.uniform(0.02, 8.0, size=nc)

    # Dense complex crossing-transition velocity block.
    M = (RNG.normal(size=(nc, nv)) + 1j * RNG.normal(size=(nc, nv))) / math.sqrt(2.0)
    abs2 = np.abs(M) ** 2

    E = Ec[:, None] - Ev[None, :]
    fc = fermi(Ec, T)
    fv = fermi(Ev, T)
    hc = fc
    hv = 1.0 - fv
    D = fv[None, :] - fc[:, None]

    # Random nonempty energy window.
    emin = float(E.min())
    emax = float(E.max())
    a, b = sorted(RNG.uniform(emin, emax, size=2))
    if b - a < 1e-10:
        b = min(emax, a + 1e-6)
    mask = (E >= a) & (E <= b)
    if not np.any(mask):
        return 0.0

    selected = abs2 * mask
    row_strength = selected.sum(axis=1)
    col_strength = selected.sum(axis=0)
    vstar2 = max(float(row_strength.max()), float(col_strength.max()))
    if vstar2 == 0.0:
        return 0.0

    # The Kubo prefactor pi e^2/V cancels in the ratio.
    thermal_sum = np.sum(
        D[mask] * abs2[mask] / np.expm1(E[mask] / (2.0 * T))
    )
    lower_bound = 2.0 * thermal_sum / vstar2
    exact_count = float(fc.sum() + hv.sum())
    return lower_bound / exact_count


def all_transition_trial(n: int, T: float) -> float:
    """Return all-transition fallback lower bound / exact thermal excitation count."""
    energies = np.sort(RNG.uniform(-8.0, 8.0, size=n))
    # Avoid an exact state at mu=0 for cleaner zero-T reference bookkeeping.
    energies[np.abs(energies) < 1e-8] += 1e-4

    Vmat = (RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))) / math.sqrt(2.0)
    Vmat = np.triu(Vmat, 1)
    abs2 = np.abs(Vmat) ** 2

    f = fermi(energies, T)
    q = np.where(energies > 0.0, f, 1.0 - f)

    de = energies[None, :] - energies[:, None]
    positive = de > 0.0

    epos = de[positive]
    if epos.size == 0:
        return 0.0
    a, b = sorted(RNG.uniform(float(epos.min()), float(epos.max()), size=2))
    mask = positive & (de >= a) & (de <= b)
    if not np.any(mask):
        return 0.0

    # Vmat[i,j] is the matrix element from lower-energy i to higher-energy j.
    selected = abs2 * mask
    degree_out = selected.sum(axis=1)
    degree_in = selected.sum(axis=0)
    vstar2 = max(float(degree_out.max()), float(degree_in.max()))
    if vstar2 == 0.0:
        return 0.0

    fi = f[:, None]
    fj = f[None, :]
    D = fi - fj

    thermal_sum = np.sum(
        D[mask] * abs2[mask] / np.expm1(de[mask] / T)
    )
    lower_bound = 2.0 * thermal_sum / vstar2
    exact_count = float(q.sum())
    return lower_bound / exact_count


def main() -> None:
    max_cross = 0.0
    max_all = 0.0

    for _ in range(50_000):
        max_cross = max(
            max_cross,
            cross_trial(
                nv=int(RNG.integers(1, 10)),
                nc=int(RNG.integers(1, 10)),
                T=float(RNG.uniform(0.2, 3.0)),
            ),
        )
        max_all = max(
            max_all,
            all_transition_trial(
                n=int(RNG.integers(2, 14)),
                T=float(RNG.uniform(0.2, 3.0)),
            ),
        )

    print(f"max cross-mu theorem ratio = {max_cross:.12f}")
    print(f"max all-transition ratio   = {max_all:.12f}")

    assert max_cross <= 1.0 + 1e-12
    assert max_all <= 1.0 + 1e-12


if __name__ == "__main__":
    main()
