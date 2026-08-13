#!/usr/bin/env python3
"""Generate the three main figures for the Paper A Applied Optics draft.

The script intentionally does not draw a numerical T_G(L) crossover curve. The
paper proves crossover existence analytically, while the finite-scale witness is
a continuum one-sided feasibility bracket.

Outputs:
    paper_a_fig1_evidence.svg / .png
    paper_a_fig2_covariance.svg / .png
    paper_a_fig3_feasibility.svg / .png

The figures use both line/marker style and text labels so interpretation does not
rely on color alone.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"


def eta(x: np.ndarray) -> np.ndarray:
    return 1.0 - np.exp(-2.0 * x) * (1.0 + 2.0 * x + 2.0 * x * x)


def generate(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    # Figure 1: finite-time evidence accumulation.
    t = np.linspace(0.0, 20.0, 1000)
    fig = plt.figure(figsize=(7.2, 4.8))
    ax = fig.add_subplot(111)
    ax.plot(
        t,
        np.sqrt(np.maximum(eta(t), 0.0)),
        linewidth=2.0,
        label=r"fast: $\tau=\tau_f$",
    )
    ax.plot(
        t,
        np.sqrt(np.maximum(eta(t / 6.0), 0.0)),
        linewidth=2.0,
        linestyle="--",
        label=r"slow: $\tau=6\tau_f$",
    )
    ax.set_xlabel(r"Physical integration time $t/\tau_f$")
    ax.set_ylabel(r"Accumulated SNR fraction $\rho_{\tau,t}/\rho_0$")
    ax.set_xlim(0.0, 20.0)
    ax.set_ylim(0.0, 1.03)
    ax.legend(frameon=False)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "paper_a_fig1_evidence.svg")
    fig.savefig(output_dir / "paper_a_fig1_evidence.png", dpi=240)
    plt.close(fig)

    # Figure 2: same physical uncertainty, different timing-correlation scales.
    d = np.linspace(0.0, 10.0, 1000)
    fig = plt.figure(figsize=(7.2, 4.8))
    ax = fig.add_subplot(111)
    ax.plot(
        d,
        (1.0 + d) * np.exp(-d),
        linewidth=2.0,
        label=r"fast: $\tau=\tau_f$",
    )
    ax.plot(
        d,
        (1.0 + d / 6.0) * np.exp(-d / 6.0),
        linewidth=2.0,
        linestyle="--",
        label=r"slow: $\tau=6\tau_f$",
    )
    ax.axvline(
        9.0,
        linestyle=":",
        linewidth=1.6,
        label=r"common uncertainty $L=9\tau_f$",
    )
    ax.set_xlabel(r"Physical timing lag $|\Delta|/\tau_f$")
    ax.set_ylabel(r"Full-template timing covariance $R_\tau(\Delta)$")
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(0.0, 1.03)
    ax.legend(frameon=False)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "paper_a_fig2_covariance.svg")
    fig.savefig(output_dir / "paper_a_fig2_covariance.png", dpi=240)
    plt.close(fig)

    # Figure 3: controlling continuum feasibility bracket.
    alpha = 0.05
    slow_bound = 0.0336427995841
    fast_bound = 0.0624701020698

    fig = plt.figure(figsize=(6.8, 4.8))
    ax = fig.add_subplot(111)
    ax.axhline(
        alpha,
        linestyle="--",
        linewidth=1.6,
        label=r"required global PFA $\alpha=0.05$",
    )
    ax.scatter([0.0], [slow_bound], s=60, marker="o", zorder=3)
    ax.scatter([1.0], [fast_bound], s=60, marker="s", zorder=3)

    # Arrows point in the direction where the unknown exact PFA may lie.
    ax.annotate(
        "",
        xy=(0.0, 0.020),
        xytext=(0.0, slow_bound),
        arrowprops=dict(arrowstyle="->", linewidth=1.5),
    )
    ax.text(0.0, 0.0377, r"upper bound $0.0336428$", ha="center", va="bottom")

    ax.annotate(
        "",
        xy=(1.0, 0.076),
        xytext=(1.0, fast_bound),
        arrowprops=dict(arrowstyle="->", linewidth=1.5),
    )
    ax.text(1.0, 0.0583, r"lower bound $0.0624701$", ha="center", va="top")

    ax.set_xticks(
        [0.0, 1.0],
        [r"slow ($\ell_s=1.5$)", r"fast ($\ell_f=9$)"],
    )
    ax.set_ylabel("Global false-alarm probability")
    ax.set_ylim(0.0, 0.082)
    ax.set_xlim(-0.45, 1.45)
    ax.legend(frameon=False, loc="upper left")
    ax.grid(True, axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "paper_a_fig3_feasibility.svg")
    fig.savefig(output_dir / "paper_a_fig3_feasibility.png", dpi=240)
    plt.close(fig)


if __name__ == "__main__":
    generate(Path("."))
