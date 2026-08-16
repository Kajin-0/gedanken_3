from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


src = Path("rev7_prapplied.tex")
figsrc = Path("rev7_figures.tex")
out = Path("rev8_prapplied.tex")
figout = Path("rev8_figures.tex")

s = src.read_text()
s = s.replace(r"\input{rev7_figures.tex}", r"\input{rev8_figures.tex}")
s = s.replace(
    r"\section{Production eight-band HgCdTe validation}",
    r"\section{Numerically converged eight-band HgCdTe validation}",
)

old_abstract = r"""In this BIA-neglecting validation, each thermally relevant selected parent shell is a single fixed-$\mathbf k$ $PT$ Kramers doublet, for which the velocity block is singular-value isotropic; $PT$ symmetry alone does not imply complete isotropy for general multidoublet blocks."""
new_abstract = r"""In the BIA-neglecting validation, each thermally relevant selected parent shell is a fixed-$\mathbf k$ $PT$ Kramers doublet with equal singular values. A separate symmetry-checked homogeneous $B_{8v}^{+}/B_{8v}^{-}/C_k$ inversion-asymmetry stress test splits the active exact shells to one dimension while retaining $\cS_a^{\rm act}=1$ and changes the full bound/reference ratio by less than $1\%$."""
s = replace_once(s, old_abstract, new_abstract, "abstract BIA robustness")

old_bia = r"""Real HgCdTe has zincblende BIA. More complete multiband models can include BIA terms~\cite{Cartoixa2003}, which can also lift the exact fixed-$\mathbf k$ doublet/quaternionic relation. We therefore claim complete shell isotropy only for the single-parent-doublet sectors actually present in this BIA-neglecting validation; the general population theorem itself does not rely on inversion symmetry."""
new_bia = r"""Real HgCdTe has zincblende BIA~\cite{Cartoixa2003}. To test whether the unity within-shell factor is merely an artifact of neglecting it, we repeated the hierarchy with the homogeneous bulk $B_{8v}^{+}$, $B_{8v}^{-}$, and complete eight-band $C_k$ couplings, using linearly interpolated HgTe/CdTe effective parameters from Ref.~\cite{Li2017HgTeBIA}. The added Hamiltonian reproduces the parent Kane phase convention, is Hermitian and spinful-time-reversal symmetric, vanishes at $\Gamma$, gives a $T$-odd analytic velocity, and agrees with a finite-difference Hamiltonian derivative. On a $120\times10\times16$ stress grid with an independently optimized ordinary capacity supremum, the active exact-shell blocks change from 20072 two-dimensional $PT$ doublets to 40452 one-dimensional BIA-split shells. Nevertheless every active block still has $\cS_a^{\rm act}=1$: for a nonzero block with a one-dimensional parent, rank and stable rank are both one. The selected-support splitting reaches $26.6$ meV, while the continuous capacity changes from $1.01764\times10^6$ to $1.02203\times10^6\,{\rm m/s}$ and the full bound/reference ratio changes from $0.11747$ to $0.11651$, a $0.82\%$ decrease. Independent grids give a change below $1\%$, the capacity supremum is multi-seed stable, and $\cS_a^{\rm act}=1$ is unchanged for clustering tolerances from $10^{-9}$ to $10^{-5}$ eV. This homogeneous stress test does not represent interface/atomistic inversion asymmetry and does not exclude exceptional multidimensional crystalline or accidental exact degeneracies; the general population theorem itself does not rely on inversion symmetry."""
s = replace_once(s, old_bia, new_bia, "full homogeneous BIA validation")

old_limit = r"""The exact HgCdTe shell isotropy is a property of the BIA-neglecting validation model."""
new_limit = r"""The BIA-neglecting production model and the separate homogeneous $B_{8v}^{+}/B_{8v}^{-}/C_k$ stress test both give $\cS_a^{\rm act}=1$ for their active exact shells, but the latter does not include interface/atomistic inversion asymmetry or exceptional multidimensional degeneracies."""
s = replace_once(s, old_limit, new_limit, "BIA limitation")

old_conclusion = r"""The absence of a further within-shell selectivity penalty follows because every thermally relevant selected parent shell in this validation is a single fixed-$\bm k$ $PT$ Kramers doublet; $PT$ symmetry is not asserted to make arbitrary multidoublet blocks fully isotropic, and real zincblende HgCdTe also contains BIA."""
new_conclusion = r"""The absence of a further within-shell selectivity penalty follows from the exact-shell dimensionality: the BIA-neglecting production model contains fixed-$\bm k$ $PT$ doublets with equal singular values, while the separate homogeneous $B_{8v}^{+}/B_{8v}^{-}/C_k$ stress test splits the sampled active parents to one-dimensional shells, for which $\cS_a^{\rm act}=1$ identically. That stress test changes the full bound/reference ratio by only $0.82\%$ but is not an atomistic or interface-BIA calculation."""
s = replace_once(s, old_conclusion, new_conclusion, "conclusion BIA robustness")

s = replace_once(
    s,
    r"\bibliography{rev4_unified}",
    r"\bibliography{rev4_unified,rev8_extra}",
    "Rev8 bibliography",
)

out.write_text(s)

f = figsrc.read_text()
f = f.replace(
    "and the single-parent-doublet sectors have no additional within-shell penalty in the BIA-neglecting validation.",
    "and the BIA-neglecting production sectors have no within-shell penalty. A separate homogeneous BIA stress test also gives a unity within-shell factor and shifts the full bound/reference ratio by less than $1\\%$.",
)
figout.write_text(f)

required = [
    r"\input{rev8_figures.tex}",
    "homogeneous $B_{8v}^{+}/B_{8v}^{-}/C_k$",
    "Li2017HgTeBIA",
    "40452 one-dimensional BIA-split shells",
    "26.6$ meV",
    "a $0.82\\%$ decrease",
    r"\bibliography{rev4_unified,rev8_extra}",
]
for token in required:
    if token not in s:
        raise RuntimeError(f"required Rev8 token missing: {token}")

if "BIA-neglecting validation model" in s:
    raise RuntimeError("obsolete Rev7 BIA limitation remains")

print(f"wrote {out} and {figout}")
