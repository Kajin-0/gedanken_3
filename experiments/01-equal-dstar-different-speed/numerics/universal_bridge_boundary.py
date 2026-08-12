#!/usr/bin/env python3
"""Step-31 Palm-anchored universal high-band boundary bridge.

This helper does not rerun the full finite-r Gaussian process.  It combines:

1. the Step-30/26 universal-crossover tangent boundary shape;
2. Step-22 exact/iterated Palm boundary anchors at kappa_f=60,100,200;
3. the Step-23 direct rough-endpoint boundary.

The finite-u discrepancy is represented by the deliberately minimal model

    delta(kappa) = delta_inf + A * kappa**(-p)

with A,p fitted to the three Palm anchors and delta_inf fixed by the direct
rough endpoint.  This is a numerical bridge, not a theorem for the exact
finite-alpha correction law.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import curve_fit


# Step-30/26 coupled tangent-shape values after inserting the universal F(mu)
# fast-channel bridge and the slow-channel large-mu correction.
KAPPA_TAN = np.array(
    [60, 80, 100, 130, 160, 200, 300, 500, 1000, 2000, 5000, 10000],
    dtype=float,
)
LAMBDA_TAN = np.array(
    [
        0.8825465245,
        0.8849669716,
        0.8860419953,
        0.8867459447,
        0.8870206766,
        0.8871482517,
        0.8871406922,
        0.8869320243,
        0.8866036617,
        0.8863302464,
        0.8860894279,
        0.8859547512,
    ],
    dtype=float,
)
LAMBDA_TAN_INF = 0.88564

# Step-22 Palm anchors.
KAPPA_PALM = np.array([60.0, 100.0, 200.0])
LAMBDA_PALM = np.array([0.9098, 0.9103, 0.9099])

# Step-23 central occupation-time rough endpoint.
LAMBDA_OCC_INF = 0.90513


def main() -> None:
    tangent = PchipInterpolator(np.log(KAPPA_TAN), LAMBDA_TAN)
    tan_at_palm = tangent(np.log(KAPPA_PALM))

    delta_inf = LAMBDA_OCC_INF - LAMBDA_TAN_INF

    def residual_model(kappa: np.ndarray, A: float, p: float) -> np.ndarray:
        return delta_inf + A * kappa ** (-p)

    target_residual = LAMBDA_PALM - tan_at_palm
    (A, p), _ = curve_fit(
        residual_model,
        KAPPA_PALM,
        target_residual,
        p0=(0.18, 0.8),
        maxfev=10000,
    )

    def bridge(kappa: np.ndarray | float) -> np.ndarray | float:
        k = np.asarray(kappa, dtype=float)
        return tangent(np.log(k)) + residual_model(k, A, p)

    dense = np.geomspace(60.0, 10000.0, 4000)
    values = np.asarray(bridge(dense))
    imax = int(np.argmax(values))

    after_100 = dense >= 100.0
    monotone_after_100 = bool(np.all(np.diff(values[after_100]) < 0.0))

    print(f"delta_inf: {delta_inf:.8f}")
    print(f"A: {A:.8f}")
    print(f"p: {p:.8f}")
    print(f"bridge maximum kappa_f: {dense[imax]:.6f}")
    print(f"bridge maximum Lambda: {values[imax]:.8f}")
    print(f"strictly decreasing on dense grid for kappa_f>=100: {monotone_after_100}")

    print("\nkappa_f      Lambda_bridge")
    for k in [60, 80, 100, 130, 160, 200, 250, 300, 400, 500, 750, 1000, 2000, 5000, 10000]:
        print(f"{k:8.1f}      {float(bridge(float(k))):.8f}")
    print(f"infinity      {LAMBDA_OCC_INF:.8f}")

    margin = LAMBDA_OCC_INF - 0.895
    conservative_margin = LAMBDA_OCC_INF - 0.004 - 0.895
    print(f"\ncentral rough-endpoint margin above Lambda=0.895: {margin:.8f}")
    print(
        "margin after subtracting the previously reported 0.004 endpoint "
        f"uncertainty: {conservative_margin:.8f}"
    )

    print(
        "\nNOTE: the fitted residual law is an empirical finite-u Palm/occupation "
        "bridge, not a proof of the exact correction law."
    )


if __name__ == "__main__":
    main()
