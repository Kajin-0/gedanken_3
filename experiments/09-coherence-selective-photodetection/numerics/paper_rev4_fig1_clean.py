import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

out = Path('.')
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['svg.fonttype'] = 'none'

fig, ax = plt.subplots(figsize=(7.2, 3.15))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')


def box(x, y, w, h, text, fs=10.5):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle='round,pad=0.02,rounding_size=0.03',
        fill=False,
        linewidth=1.25,
    )
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs)
    return p


box(2.55, 2.45, 2.15, 0.72, 'bright state $|B\\rangle$')
box(2.55, 0.70, 2.15, 0.86, 'dark manifold\n$N-1$ directions', fs=10)
box(7.05, 2.45, 1.72, 0.72, 'counted sink')
box(6.60, 0.68, 2.65, 0.92, 'efficiency-selected gate\n$C_{S,N}(T_N)=\\eta$', fs=9.8)

ax.text(0.18, 3.18, 'signal photon', fontsize=10.5, ha='left', va='center')
ax.text(0.18, 2.78, r'$|B\rangle=N^{-1/2}\sum_j|j\rangle$', fontsize=10.2, ha='left', va='center')
ax.annotate('', xy=(2.55, 2.82), xytext=(1.85, 2.98), arrowprops=dict(arrowstyle='->', lw=1.35))

ax.text(0.18, 1.12, 'local internal event', fontsize=10.5, ha='left', va='center')
ax.text(0.18, 0.72, r'$|j\rangle$  (bright overlap $1/N$)', fontsize=10.0, ha='left', va='center')
ax.annotate('', xy=(2.55, 1.12), xytext=(1.85, 1.00), arrowprops=dict(arrowstyle='->', lw=1.35))

ax.annotate('', xy=(7.05, 2.81), xytext=(4.70, 2.81), arrowprops=dict(arrowstyle='->', lw=1.55))
ax.text(5.87, 3.03, r'bright extraction  $\kappa_N$', fontsize=10.2, ha='center')

ax.annotate('', xy=(3.42, 1.56), xytext=(3.42, 2.45), arrowprops=dict(arrowstyle='->', lw=1.35))
ax.text(2.98, 2.00, r'dephasing  $\gamma_N$', fontsize=9.6, ha='right', va='center')

ax.annotate('', xy=(4.08, 2.45), xytext=(4.08, 1.56), arrowprops=dict(arrowstyle='->', lw=1.25, linestyle='--'))
ax.text(4.30, 2.00, r'slow recycling  $r_{-,N}\sim \lambda_N/N$', fontsize=9.5, ha='left', va='center')

ax.text(7.92, 1.88, 'decision condition', fontsize=9.2, ha='center', va='center')
ax.text(5.72, 0.23, r'$\mu_{\mathrm{loc},N}=Nd\int_0^{T_N} C_{D,N}(u)\,du$', fontsize=10.0, ha='center')

fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.05)
for ext in ['pdf', 'png', 'svg']:
    kwargs = {'dpi': 300} if ext == 'png' else {}
    fig.savefig(out / f'paper_rev4_fig1_mechanism.{ext}', bbox_inches='tight', pad_inches=0.03, **kwargs)
plt.close(fig)
