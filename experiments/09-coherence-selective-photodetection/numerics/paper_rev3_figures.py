#!/usr/bin/env python3
"""Generate the three main theory figures for Experiment-09 Paper Rev. 3.

Outputs:
    paper_rev3_fig1_mechanism.svg/png
    paper_rev3_fig2_scaling.svg/png
    paper_rev3_fig3_ceiling.svg/png

The numerical curves use the exact finite-N one-body kernel plus the explicit
independent-particle count lift. Parameter values are dimensionless theory
illustrations, not material parameters or detector design recommendations.
"""

from __future__ import annotations

from pathlib import Path
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

plt.rcParams["svg.fonttype"] = "none"


def rates(N: int, kappa: float, gamma: float):
    a = kappa + gamma
    delta = math.sqrt(a * a - 4.0 * kappa * gamma / N)
    return 0.5 * (a - delta), 0.5 * (a + delta), delta


def collection(t: float, N: int, kappa: float, gamma: float, b0: float) -> float:
    rm, rp, delta = rates(N, kappa, gamma)
    A = (rp - kappa * b0) / delta
    B = (kappa * b0 - rm) / delta
    return 1.0 - A * math.exp(-rm * t) - B * math.exp(-rp * t)


def minimal_gate(N: int, kappa: float, gamma: float, eta: float) -> float:
    f = lambda t: collection(t, N, kappa, gamma, 1.0) - eta
    hi = 1.0 / (kappa + gamma)
    while f(hi) < 0.0:
        hi *= 2.0
    return float(brentq(f, 0.0, hi, xtol=1e-12, rtol=1e-11))


def exact_dark_mean(
    N: int,
    kappa0: float,
    gamma0: float,
    alpha: float,
    beta: float,
    d: float,
    eta: float,
):
    kappa = kappa0 * N**alpha
    gamma = gamma0 * N**beta
    T = minimal_gate(N, kappa, gamma, eta)
    integrand = lambda u: max(collection(u, N, kappa, gamma, 1.0 / N), 0.0)
    integral = quad(integrand, 0.0, T, epsabs=1e-11, epsrel=1e-9, limit=200)[0]
    return T, N * d * integral


def save(fig, path: Path):
    fig.savefig(path.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(path.with_suffix(".png"), dpi=240, bbox_inches="tight")
    plt.close(fig)


def figure_1(output_dir: Path):
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    # Local-state manifold / bright mode.
    ax.text(0.45, 5.25, r"photon: coherent $|B\rangle=N^{-1/2}\sum_j|j\rangle$", fontsize=12)
    ax.annotate("", xy=(3.0, 4.25), xytext=(2.0, 4.95), arrowprops=dict(arrowstyle="->", lw=1.7))

    bright = plt.Rectangle((2.8, 3.55), 2.4, 1.15, fill=False, linewidth=1.8)
    ax.add_patch(bright)
    ax.text(4.0, 4.12, "bright counted sector", ha="center", va="center", fontsize=12)

    dark = plt.Rectangle((2.8, 1.15), 2.4, 1.25, fill=False, linewidth=1.8)
    ax.add_patch(dark)
    ax.text(4.0, 1.78, r"dark manifold ($N-1$ directions)", ha="center", va="center", fontsize=12)

    ax.text(0.45, 1.1, r"internal event: local $|j\rangle$", fontsize=12)
    ax.annotate("", xy=(2.8, 1.65), xytext=(1.95, 1.35), arrowprops=dict(arrowstyle="->", lw=1.7))
    ax.text(1.0, 2.0, r"direct bright overlap $1/N$", fontsize=10)

    # Dephasing and recycling.
    ax.annotate("", xy=(4.0, 2.4), xytext=(4.0, 3.55), arrowprops=dict(arrowstyle="->", lw=1.8))
    ax.text(4.15, 3.0, r"local dephasing $\gamma_N$", fontsize=11, va="center")

    ax.annotate("", xy=(4.8, 3.55), xytext=(4.8, 2.4), arrowprops=dict(arrowstyle="->", lw=1.5, linestyle="--"))
    ax.text(5.0, 2.95, r"slow return $r_-\sim\lambda_N/N$", fontsize=10, va="center")

    # Counted sink.
    sink = plt.Rectangle((7.2, 3.55), 1.8, 1.15, fill=False, linewidth=1.8)
    ax.add_patch(sink)
    ax.text(8.1, 4.12, "counted sink", ha="center", va="center", fontsize=12)
    ax.annotate("", xy=(7.2, 4.12), xytext=(5.2, 4.12), arrowprops=dict(arrowstyle="->", lw=2.0))
    ax.text(6.2, 4.38, r"$\kappa_N$", fontsize=12, ha="center")

    ax.text(6.35, 1.05, "gate closes when", fontsize=11, ha="center")
    ax.text(6.35, 0.65, r"$C_{S,N}(T_N)=\eta$", fontsize=12, ha="center")
    ax.text(6.35, 0.22, r"count burden: $\mu_N=Nd\int_0^{T_N}C_{D,N}(u)du$", fontsize=11, ha="center")

    ax.set_title("Coherence-selective detection: fast extraction versus slow dark-manifold recycling", fontsize=13)
    save(fig, output_dir / "paper_rev3_fig1_mechanism")


def figure_2(output_dir: Path):
    kappa0 = 10.0
    gamma0 = 1.0
    d = 1.0
    Ns = np.unique(np.round(np.logspace(1, 4, 24)).astype(int))

    cases = [
        ("extraction wins: $\alpha=1,\,\beta=0,\,\eta=.90$", 1.0, 0.0, 0.90, -1.0),
        ("balanced fast: $\alpha=\beta=0,\,\eta=.50$", 0.0, 0.0, 0.50, 0.0),
        ("balanced slow: $\alpha=\beta=0,\,\eta=.95$", 0.0, 0.0, 0.95, 2.0),
        ("balanced collective slow: $\alpha=\beta=1,\,\eta=.95$", 1.0, 1.0, 0.95, 1.0),
    ]

    fig, ax = plt.subplots(figsize=(7.4, 5.3))
    markers = ["o", "s", "^", "D"]

    for marker, (label, alpha, beta, eta, slope) in zip(markers, cases):
        values = []
        for N in Ns:
            _, mu = exact_dark_mean(N, kappa0, gamma0, alpha, beta, d, eta)
            values.append(mu)
        values = np.asarray(values)
        ax.loglog(Ns, values, marker=marker, markersize=4, linewidth=1.5, label=label)

        # Draw a local asymptotic slope guide normalized at the final exact point.
        Nguide = np.asarray([Ns[-5], Ns[-1]], dtype=float)
        guide = values[-1] * (Nguide / Ns[-1]) ** slope
        ax.loglog(Nguide, guide, linestyle="--", linewidth=1.2)
        ax.text(Nguide[0], guide[0] * 1.12, rf"slope ${slope:g}$", fontsize=9)

    ax.set_xlabel(r"coherently participating states $N$")
    ax.set_ylabel(r"accepted local-dark mean $\mu_{\mathrm{loc},N}$")
    ax.set_title("Exact finite-$N$ count burden approaches the predicted scaling classes")
    ax.grid(True, which="both", alpha=0.22)
    ax.legend(frameon=False, fontsize=9)
    save(fig, output_dir / "paper_rev3_fig2_scaling")


def figure_3(output_dir: Path):
    kappa0 = 10.0
    gamma0 = 1.0
    q0 = kappa0 / (kappa0 + gamma0)

    fig, ax = plt.subplots(figsize=(7.2, 4.9))
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(0.0, 1.0)

    # Use text/line structure rather than relying on color.
    ax.axvline(0.0, linewidth=1.6)
    ax.hlines(q0, -0.03, 0.03, linewidth=2.2)
    ax.plot([0.0], [q0], marker="o", markersize=7)

    ax.text(-0.5, 0.72, "dephasing scales faster", ha="center", fontsize=12)
    ax.text(-0.5, 0.57, r"$\eta_{\rm sc}=0$", ha="center", fontsize=13)
    ax.text(-0.5, 0.42, "no fixed positive efficiency\nkeeps local-dark burden bounded", ha="center", fontsize=10)

    ax.text(0.5, 0.72, "extraction scales faster", ha="center", fontsize=12)
    ax.text(0.5, 0.57, r"$\eta_{\rm sc}=1$", ha="center", fontsize=13)
    ax.text(0.5, 0.42, "every fixed $\eta<1$ can\nremain locally scalable", ha="center", fontsize=10)

    ax.annotate(
        r"balanced line: $\eta_{\rm sc}=q_0=\kappa_0/(\kappa_0+\gamma_0)$",
        xy=(0.0, q0),
        xytext=(-0.83, 0.91),
        arrowprops=dict(arrowstyle="->", linewidth=1.2),
        fontsize=10,
    )

    ax.set_xlabel(r"rate-scaling imbalance $\alpha-\beta$")
    ax.set_ylabel(r"scalable fixed internal efficiency $\eta_{\rm sc}$")
    ax.set_title("Scalable-efficiency ceiling under bounded per-site counted coupling")
    ax.set_xticks([-1, 0, 1], [r"$\alpha<\beta$", r"$\alpha=\beta$", r"$\alpha>\beta$"])
    ax.grid(True, axis="y", alpha=0.22)
    save(fig, output_dir / "paper_rev3_fig3_ceiling")


def generate(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    figure_1(output_dir)
    figure_2(output_dir)
    figure_3(output_dir)


if __name__ == "__main__":
    generate(Path("."))
