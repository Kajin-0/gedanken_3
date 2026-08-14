"""Generate the Rev. 8 publication-quality mechanism/operating-definition figure.

The layout is intentionally sparse: no explanatory equation is placed on top of a flow line.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.0,
    "mathtext.fontset": "dejavusans",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.unicode_minus": False,
})

fig, ax = plt.subplots(figsize=(7.35, 2.95))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def box(x, y, w, h, lines, fs=8.7, lw=0.95, radius=0.012):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.007,rounding_size={radius}",
        linewidth=lw,
        edgecolor="black",
        facecolor="white",
    )
    ax.add_patch(p)
    if len(lines) == 1:
        ax.text(x+w/2, y+h/2, lines[0], ha="center", va="center",
                fontsize=fs, fontweight="semibold")
    else:
        ys = [y+h*0.64, y+h*0.32]
        for i, (t, yy) in enumerate(zip(lines, ys)):
            ax.text(x+w/2, yy, t, ha="center", va="center",
                    fontsize=fs if i else fs+0.2,
                    fontweight="semibold" if i == 0 else "normal")
    return p


def arr(x1, y1, x2, y2, lw=1.0, ls="solid", style="-|>", ms=7.5):
    a = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style,
        mutation_scale=ms,
        linewidth=lw,
        linestyle=ls,
        color="black",
        shrinkA=0,
        shrinkB=0,
    )
    ax.add_patch(a)
    return a


# Panel headers and divider.
ax.text(0.018, 0.955, "(a)", ha="left", va="top", fontsize=10, fontweight="bold")
ax.text(0.062, 0.955, "State flow", ha="left", va="top", fontsize=10, fontweight="semibold")
ax.plot([0.670, 0.670], [0.075, 0.91], lw=0.6, color="0.55")
ax.text(0.695, 0.955, "(b)", ha="left", va="top", fontsize=10, fontweight="bold")
ax.text(0.739, 0.955, "Operating definition", ha="left", va="top", fontsize=10, fontweight="semibold")

# State-flow panel.
box(0.035, 0.690, 0.135, 0.135, ["Signal", "photon"], fs=8.4)
box(0.300, 0.685, 0.195, 0.145, ["Bright state", r"$|B\rangle$"], fs=8.6)
box(0.570, 0.685, 0.070, 0.145, ["Counted", "sink"], fs=8.0)
box(0.035, 0.285, 0.135, 0.135, ["Local event", "one site"], fs=8.2)
box(0.300, 0.280, 0.195, 0.145, ["Dark subspace", r"$N-1$ directions"], fs=8.4)

arr(0.170, 0.758, 0.295, 0.758)
arr(0.500, 0.758, 0.565, 0.758)
ax.text(0.532, 0.805, r"$\kappa_N$", ha="center", va="center", fontsize=8.2)

sx, sy = 0.225, 0.3525
arr(0.170, sy, sx-0.008, sy)
ax.plot([sx], [sy], marker="o", ms=3.0, color="black")
arr(sx+0.006, sy, 0.295, 0.3525, lw=0.95)
arr(sx+0.006, sy+0.006, 0.295, 0.690, lw=0.95)
ax.text(0.245, 0.545, r"$1/N$", ha="right", va="center", fontsize=8.1)
ax.text(0.260, 0.395, r"$1-1/N$", ha="center", va="bottom", fontsize=8.0)

arr(0.520, 0.672, 0.520, 0.442, style="<->", lw=0.85, ls="dashed", ms=6.5)
ax.text(0.540, 0.585, "local dephasing", ha="left", va="center", fontsize=7.4)
ax.text(0.540, 0.535, r"$\gamma_N$", ha="left", va="center", fontsize=8.0)

box(0.300, 0.075, 0.310, 0.105,
    ["Emergent slow clock", r"$r_{-,N}^{-1}$  (eigenmode, not a jump)"],
    fs=7.6, lw=0.75)

# Operating-definition panel.
box(0.720, 0.700, 0.245, 0.125, [r"Target efficiency  $\eta$"], fs=8.5)
box(0.720, 0.445, 0.245, 0.125, [r"Minimum gate  $T_N(\eta)$"], fs=8.5)
box(0.720, 0.190, 0.245, 0.125, [r"Susceptibility  $\chi_N(\eta)$"], fs=8.5)
arr(0.8425, 0.695, 0.8425, 0.575, lw=0.9, ms=6.5)
arr(0.8425, 0.440, 0.8425, 0.320, lw=0.9, ms=6.5)

fig.subplots_adjust(left=0.006, right=0.994, top=0.99, bottom=0.01)
fig.savefig(OUT / "paper_rev8_fig1_mechanism.pdf", bbox_inches="tight", pad_inches=0.025)
fig.savefig(OUT / "paper_rev8_fig1_mechanism.png", dpi=320, bbox_inches="tight", pad_inches=0.025)
