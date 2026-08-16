from pathlib import Path

p = Path("rev8_prapplied.tex")
s = p.read_text()

old = r"The selected-support splitting reaches $26.6$ meV;"
new = r"The adjacent-pair separation diagnostic over selected-support points reaches $26.6$ meV;"
count = s.count(old)
if count != 1:
    raise RuntimeError(f"expected exactly one BIA diagnostic phrase, found {count}")
s = s.replace(old, new, 1)

old_params = r"using linearly interpolated HgTe/CdTe effective parameters from Ref.~\cite{Li2017HgTeBIA}."
new_params = r"using linearly interpolated HgTe/CdTe effective parameters from Ref.~\cite{Li2017HgTeBIA}: $B_{8v}^{+}=-20.26\,{\rm eV\,\AA^2}$, $B_{8v}^{-}=0.706\,{\rm eV\,\AA^2}$, and $C_k=-0.0654\,{\rm eV\,\AA}$ at the present composition."
count = s.count(old_params)
if count != 1:
    raise RuntimeError(f"expected exactly one BIA parameter-source phrase, found {count}")
s = s.replace(old_params, new_params, 1)

for obsolete in ["The selected-support splitting reaches", "using linearly interpolated HgTe/CdTe effective parameters from Ref.~\\cite{Li2017HgTeBIA}."]:
    if obsolete in s:
        raise RuntimeError(f"obsolete Rev8 wording remains: {obsolete}")

for required in [r"B_{8v}^{+}=-20.26", r"B_{8v}^{-}=0.706", r"C_k=-0.0654", "adjacent-pair separation diagnostic"]:
    if required not in s:
        raise RuntimeError(f"required finalized Rev8 token missing: {required}")

p.write_text(s)
print("finalized Rev8 BIA diagnostic wording and effective parameters")
