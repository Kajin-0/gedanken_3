from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


src = Path("rev5_prapplied.tex")
figsrc = Path("rev5_figures.tex")
out = Path("rev6_prapplied.tex")
figout = Path("rev6_figures.tex")

s = src.read_text()
s = s.replace(r"\input{rev5_figures.tex}", r"\input{rev6_figures.tex}")

# Stage-specific terminology: reserve observability for terminal-map null spaces.
s = s.replace(r"\tau_{\rm obs}^{\rm act}", r"\tau_{\rm bound}^{\rm act}")
s = s.replace("eq:shell-observable", "eq:shell-bound")

# The 0.3068 loss is introduced by the Fermi endpoint inequality; Kubo-Greenwood
# only provides the exact spectral representation.
s = s.replace("Fermi/Kubo asymmetry", "Fermi-statistical asymmetry")
s = s.replace("independent Fermi/Kubo step", "independent Fermi-statistical step")
s = s.replace("thermal/Fermi asymmetry", "Fermi-statistical asymmetry")
s = s.replace("from the Fermi/Kubo step", "from the Fermi-statistical step")
s = s.replace("selected active-population tightness", "selected active-population bound tightness")

capacity_anchor = (
    "The domain in Eq.~\\eqref{eq:capacity} is part of the theorem and cannot be enlarged "
    "after the response is known by adding unrelated high-coupling states.\n"
)
thermo = capacity_anchor + r"""

Equations up to this point are finite-system statements. Writing the capacity in a finite normalization volume as $v_{\cB,V}^{\rm cap}$, a nonzero macroscopic density floor requires uniform control along the thermodynamic sequence $V_j\to\infty$:
\begin{equation}
\boxed{
\bar v_{\cB}^{\rm cap}
\equiv
\limsup_{j\to\infty}v_{\cB,V_j}^{\rm cap}<\infty.}
\label{eq:thermo-cap}
\end{equation}
Finite capacity at every finite $V$ is not sufficient if that capacity diverges with $V$. Under Eq.~\eqref{eq:thermo-cap}, the density form of the theorem survives the thermodynamic limit with $v_{\cB}^{\rm cap}$ replaced by $\bar v_{\cB}^{\rm cap}$; below we retain the shorter notation when the uniform bound is understood.
"""
s = replace_once(s, capacity_anchor, thermo, "thermodynamic capacity insertion")

s = replace_once(
    s,
    "Equation~\\eqref{eq:main-theorem} is the principal physical theorem. It bounds equilibrium one-body endpoint population, not a recombination rate, dark current, or specific detectivity.",
    "Equation~\\eqref{eq:main-theorem} is the principal physical theorem. At finite $V$ it is an exact finite-system inequality; its macroscopic density interpretation additionally requires Eq.~\\eqref{eq:thermo-cap}. It bounds equilibrium one-body endpoint population, not a recombination rate, dark current, or specific detectivity.",
    "finite-system theorem qualification",
)

eta_old = r"""Define
\begin{equation}
\eta_F=\cL_{\cB}/\cR_{\cB}\le1.
\end{equation}
Then
"""
eta_new = r"""Define the Fermi-statistical factor
\begin{equation}
\eta_F=\cL_{\cB}/\cR_{\cB}\le1.
\end{equation}
The inequality in $\eta_F$ comes from the endpoint Fermi bound in Eq.~\eqref{eq:fermi}; Kubo--Greenwood is the exact spectral bookkeeping step in Eq.~\eqref{eq:kubo} and introduces no additional slack. Then
"""
s = replace_once(s, eta_old, eta_new, "Fermi-factor definition")
s = s.replace(r"\underbrace{\eta_F}_{\text{Fermi/Kubo}}", r"\underbrace{\eta_F}_{\text{Fermi factor}}")

# eq:shell-observable has already been renamed globally above, so the anchor here
# deliberately uses the Rev6 label while retaining the original Rev5 paragraph.
methods_old = r"""We evaluate Eqs.~\eqref{eq:shell-decomp}--\eqref{eq:shell-bound} in the second-order bulk eight-band Kane validation used for a 300-K, $10\,\mu$m-class HgCdTe absorber. The model follows the bulk constant-parameter limit of Novik \textit{et al.}~\cite{Novik2005}, uses the empirical gap relation of Laurenti \textit{et al.}~\cite{Laurenti1990}, and evaluates the physical velocity from the analytic Hamiltonian derivative. For the broad selected transition-energy window $E_g\le\Delta E\le0.5$ eV, the production quadrature gives the quantities summarized in Table~\ref{tab:hgcdte}.
"""
methods_new = r"""We evaluate Eqs.~\eqref{eq:shell-decomp}--\eqref{eq:shell-bound} in the second-order bulk eight-band Kane validation used for a 300-K, $10\,\mu$m-class HgCdTe absorber. The model follows the bulk constant-parameter limit of Novik \textit{et al.}~\cite{Novik2005}, uses the empirical gap relation of Laurenti \textit{et al.}~\cite{Laurenti1990}, and evaluates the physical velocity from the analytic Hamiltonian derivative. For $E_g=0.123984$ eV, the gap interpolation gives $x=0.17973$; the representative constant parameters are $\Delta=1.04945$ eV, $F=-0.01618$, $\gamma_1=3.6273$, $\gamma_2=0.3598$, $\gamma_3=1.0717$, and $E_P=18.8$ eV. The carrier integral uses $|\bm k|\le2.0\,{\rm nm}^{-1}$ and the chemical potential is obtained by charge neutrality in the eight-band model. Because the second-order velocity matrix is finite-dimensional and bounded on this compact momentum domain, every selected projected-block norm is bounded by a volume-independent microscopic operator norm; the validation therefore satisfies Eq.~\eqref{eq:thermo-cap} within the stated bounded-domain model.

The production optical integrals use 160 radial Gauss--Legendre nodes, 10 Gauss--Legendre nodes in $\cos\theta$, and 16 uniform azimuthal nodes; a $200\times12\times20$ grid supplies an independent support-population check. Exact twofold degeneracies are clustered at $10^{-7}$ eV, and the ordinary projected-block capacity supremum is searched directly in continuous $(k,\theta,\phi)$ rather than taken from the largest quadrature node. For the support diagnostics, a singular value is counted as nonzero when $s>10^{-6}\,{\rm m/s}$. On a reduced $40\times6\times8$ audit grid the broad-window active-support fraction is unchanged to printed precision as this threshold is swept from $10^{-9}$ through $10^{4}\,{\rm m/s}$; thus the support decomposition is numerically stable, while the central population lower bound is rank-threshold independent. Varying the degeneracy-clustering tolerance from $10^{-10}$ to $10^{-5}$ eV leaves the sampled capacity unchanged to the reported precision. For the broad selected transition-energy window $E_g\le\Delta E\le0.5$ eV, the production grid samples selected transitions through $|\bm k|=0.583\,{\rm nm}^{-1}$ and gives the quantities summarized in Table~\ref{tab:hgcdte}.
"""
s = replace_once(s, methods_old, methods_new, "HgCdTe reproducibility block")

limitations_old = "Important limitations are explicit. Equation~\\eqref{eq:main-theorem} requires a selected direct cross-$\\mu$ conductivity contribution and an independently justified finite capacity."
limitations_new = "Important limitations are explicit. Equation~\\eqref{eq:main-theorem} requires a selected direct cross-$\\mu$ conductivity contribution and an independently justified finite capacity; a nonzero macroscopic density floor further requires the uniform thermodynamic bound in Eq.~\\eqref{eq:thermo-cap}."
s = replace_once(s, limitations_old, limitations_new, "thermodynamic limitation")

out.write_text(s)

f = figsrc.read_text()
f = f.replace("Fermi/Kubo strength step", "Fermi inequality strength step")
f = f.replace("{Fermi + Kubo}", "{Kubo map + Fermi bound}")
f = f.replace(r"{Fermi/Kubo\\$\eta_F$}", r"{Fermi factor\\$\eta_F$}")
f = f.replace("Fermi/Kubo asymmetry", "Fermi-statistical asymmetry")
f = f.replace("at (0,2.45) {Fermi/Kubo};", "at (0,2.45) {Fermi factor};")
f = f.replace("the Fermi/Kubo and capacity factors", "the Fermi-statistical and capacity factors")
f = f.replace("active tightness: $0.1757$", "active bound tightness: $0.1757$")
figout.write_text(f)

# Hard regression gates.
checks_absent = [r"\tau_{\rm obs}^{\rm act}", "Fermi/Kubo", "eq:shell-observable"]
for token in checks_absent:
    if token in s or token in f:
        raise RuntimeError(f"obsolete Rev5 token remains: {token}")
checks_present = [
    r"\input{rev6_figures.tex}",
    "eq:thermo-cap",
    r"\tau_{\rm bound}^{\rm act}",
    "Fermi-statistical factor",
    "volume-independent microscopic operator norm",
    r"s>10^{-6}\,{\rm m/s}",
    r"160 radial Gauss--Legendre nodes",
    r"200\times12\times20",
    r"0.583\,{\rm nm}^{-1}",
]
for token in checks_present:
    if token not in s:
        raise RuntimeError(f"required Rev6 token missing: {token}")
if "Kubo map + Fermi bound" not in f:
    raise RuntimeError("Rev6 figure semantics were not applied")

print(f"wrote {out} and {figout}")
