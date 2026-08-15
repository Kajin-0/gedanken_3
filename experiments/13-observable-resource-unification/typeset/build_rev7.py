from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


src = Path("rev6_prapplied.tex")
figsrc = Path("rev6_figures.tex")
out = Path("rev7_prapplied.tex")
figout = Path("rev7_figures.tex")

s = src.read_text()
s = s.replace(r"\input{rev6_figures.tex}", r"\input{rev7_figures.tex}")
s = s.replace(
    "production-resolution second-order eight-band HgCdTe calculation",
    "numerically converged second-order eight-band HgCdTe calculation",
)

old_thermo = r"""Finite capacity at every finite $V$ is not sufficient if that capacity diverges with $V$. Under Eq.~\eqref{eq:thermo-cap}, the density form of the theorem survives the thermodynamic limit with $v_{\cB}^{\rm cap}$ replaced by $\bar v_{\cB}^{\rm cap}$; below we retain the shorter notation when the uniform bound is understood."""
new_thermo = r"""Finite capacity at every finite $V$ is not sufficient if that capacity diverges with $V$. Let $n_{\cB,V}^{\rm act}$ and $\cL_{\cB,V}$ denote the finite-volume intensive quantities in the active-population inequality. If both have thermodynamic limits, Eq.~\eqref{eq:thermo-cap} yields the same density inequality with $v_{\cB}^{\rm cap}$ replaced by $\bar v_{\cB}^{\rm cap}$. Without that convergence assumption, the finite-volume inequalities imply the weaker but fully general statement
\begin{equation}
\liminf_{j\to\infty} n_{\cB,V_j}^{\rm act}
\ge
\frac{\liminf_{j\to\infty}\cL_{\cB,V_j}}
{(\bar v_{\cB}^{\rm cap})^2},
\label{eq:thermo-liminf}
\end{equation}
for positive finite $\bar v_{\cB}^{\rm cap}$. Below we retain the shorter notation when the ordinary thermodynamic limits and uniform bound are understood."""
s = replace_once(s, old_thermo, new_thermo, "thermodynamic liminf qualifier")

old_ref = r"""and let $n_{\rm ref}$ be a reference electron-plus-hole population containing the selected active population $n_{\cB}^{\rm act}$. Then"""
new_ref = r"""and let $n_{\rm ref}$ be a reference electron-plus-hole population containing the selected active population $n_{\cB}^{\rm act}$. The resulting support-coverage factor $n_{\cB}^{\rm act}/n_{\rm ref}$ is therefore reference-domain dependent: unlike $\eta_F$, $c_a$, and $\cS_a^{\rm act}$, it is not determined by the selected optical map alone. Then"""
s = replace_once(s, old_ref, new_ref, "support-coverage reference qualifier")

old_carrier = r"""The carrier integral uses $|\bm k|\le2.0\,{\rm nm}^{-1}$ and the chemical potential is obtained by charge neutrality in the eight-band model. Because the second-order velocity matrix is finite-dimensional and bounded on this compact momentum domain, every selected projected-block norm is bounded by a volume-independent microscopic operator norm; the validation therefore satisfies Eq.~\eqref{eq:thermo-cap} within the stated bounded-domain model."""
new_carrier = r"""The carrier integral uses $|\bm k|\le2.0\,{\rm nm}^{-1}$ and the chemical potential is obtained by charge neutrality in the eight-band model. Increasing the carrier cutoff from $1.5$ to $2.0\,{\rm nm}^{-1}$ changes the cross-$\mu$ reference population by less than $1\%$, providing a direct convergence check on the denominator used in the support-coverage factor. Because the second-order velocity matrix is finite-dimensional and bounded on this compact momentum domain, every selected projected-block norm is bounded by a volume-independent microscopic operator norm; the validation therefore satisfies Eq.~\eqref{eq:thermo-cap} within the stated bounded-domain model."""
s = replace_once(s, old_carrier, new_carrier, "carrier-cutoff convergence")

old_dangle = r"""This relation supplies the spectral interpretation of task concentration. It does not replace the separate unknown-arrival transient construction, which equalizes eventual event-specific matched-filter SNR for one waveform and includes a correlated timing search."""
new_dangle = r"""This relation supplies the spectral interpretation of task concentration."""
s = replace_once(s, old_dangle, new_dangle, "remove dangling unknown-arrival sentence")

out.write_text(s)

f = figsrc.read_text()

# Enlarge only the smallest annotations. The geometry and scientific content are unchanged.
f = f.replace(r"node[above,font=\scriptsize]{$M_{\rm opt}$}", r"node[above,font=\footnotesize]{$M_{\rm opt}$}")
f = f.replace(r"node[above,font=\scriptsize]{$M_{\rm dyn}$}", r"node[above,font=\footnotesize]{$M_{\rm dyn}$}")
f = f.replace(r"node[above,font=\scriptsize]{$M_{\rm ro}(\omega)$}", r"node[above,font=\footnotesize]{$M_{\rm ro}(\omega)$}")
f = f.replace(r"\node[font=\scriptsize,align=center] at (3.18,-1.05)", r"\node[font=\footnotesize,align=center] at (3.18,-1.05)")
f = f.replace(r"\node[font=\scriptsize,align=center] at (1.55,1.08)", r"\node[font=\footnotesize,align=center] at (1.55,1.08)")
f = f.replace(r"\node[font=\scriptsize,align=center] at (4.77,1.08)", r"\node[font=\footnotesize,align=center] at (4.77,1.08)")
f = f.replace(r"\node[font=\scriptsize,align=center] at (8.00,1.08)", r"\node[font=\footnotesize,align=center] at (8.00,1.08)")
f = f.replace(
    r"\node[font=\scriptsize,align=center] at (4.20,1.05) {four identifiable places where inverse population information can be lost};",
    r"\node[font=\footnotesize,align=center] at (4.20,1.05) {four distinct sources of bound looseness};",
)
for old, new in [
    (r"\node[anchor=east,font=\scriptsize] at (0,3.35)", r"\node[anchor=east,font=\footnotesize] at (0,3.35)"),
    (r"\node[anchor=east,font=\scriptsize] at (0,2.45)", r"\node[anchor=east,font=\footnotesize] at (0,2.45)"),
    (r"\node[anchor=east,font=\scriptsize] at (0,1.55)", r"\node[anchor=east,font=\footnotesize] at (0,1.55)"),
    (r"\node[anchor=east,font=\scriptsize] at (0,.65)", r"\node[anchor=east,font=\footnotesize] at (0,.65)"),
    (r"\node[anchor=west,font=\bfseries\scriptsize] at ({.30+\W*.66897},3.35)", r"\node[anchor=west,font=\bfseries\footnotesize] at ({.30+\W*.66897},3.35)"),
    (r"\node[anchor=west,font=\bfseries\scriptsize] at ({.30+\W*.30684},2.45)", r"\node[anchor=west,font=\bfseries\footnotesize] at ({.30+\W*.30684},2.45)"),
    (r"\node[anchor=west,font=\bfseries\scriptsize] at ({.30+\W*.57262},1.55)", r"\node[anchor=west,font=\bfseries\footnotesize] at ({.30+\W*.57262},1.55)"),
    (r"\node[font=\scriptsize,align=center] at (8.55,.58)", r"\node[font=\footnotesize,align=center] at (8.55,.58)"),
]:
    f = f.replace(old, new)
figout.write_text(f)

# Hard regression gates.
required = [
    r"\input{rev7_figures.tex}",
    "eq:thermo-cap",
    "eq:thermo-liminf",
    "reference-domain dependent",
    r"changes the cross-$\mu$ reference population by less than $1\%$",
    "numerically converged second-order eight-band HgCdTe calculation",
    r"\tau_{\rm bound}^{\rm act}",
    "Fermi-statistical factor",
]
for token in required:
    if token not in s:
        raise RuntimeError(f"required Rev7 token missing: {token}")

for token in [
    "unknown-arrival transient construction",
    "production-resolution second-order eight-band HgCdTe calculation",
    r"\tau_{\rm obs}^{\rm act}",
    "Fermi/Kubo",
]:
    if token in s or token in f:
        raise RuntimeError(f"obsolete token remains in Rev7: {token}")

if "four distinct sources of bound looseness" not in f:
    raise RuntimeError("Rev7 figure typography/annotation update missing")

print(f"wrote {out} and {figout}")
