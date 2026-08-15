#!/usr/bin/env python3
"""Build the self-contained production TeX source for Experiment 13 Rev. 4.

The scientific source remains rev4_unified_prapplied.tex. This script performs
only production transformations:
  * select the Physical Review Applied REVTeX journal style and float handling;
  * enable T1 font encoding and scalable Latin Modern for bibliography diacritics;
  * load native TikZ figure definitions;
  * replace the five explicit figure placeholders by figure macros;
  * format the central population theorem as an equivalent two-line column display;
  * emit rev4_unified_prapplied_built.tex for compilation.

It intentionally does not change scientific claims, algebra, numerical values,
reference content, or prose.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "rev4_unified_prapplied.tex"
OUT = HERE / "rev4_unified_prapplied_built.tex"

text = SRC.read_text(encoding="utf-8")

old_class = "\\documentclass[aps,twocolumn,superscriptaddress,longbibliography]{revtex4-2}"
new_class = "\\documentclass[aps,prapplied,twocolumn,superscriptaddress,longbibliography,floatfix]{revtex4-2}"
if old_class not in text:
    raise RuntimeError("REVTeX documentclass anchor not found")
text = text.replace(old_class, new_class, 1)

needle = "\\usepackage{graphicx}\n"
insert = (
    "\\usepackage[T1]{fontenc}\n"
    "\\usepackage{lmodern}\n"
    "\\usepackage{graphicx}\n"
    "\\usepackage{tikz}\n"
    "\\usetikzlibrary{arrows.meta,decorations.pathreplacing}\n"
)
if needle not in text:
    raise RuntimeError("graphicx package anchor not found")
text = text.replace(needle, insert, 1)

begin_doc = "\\begin{document}\n"
if begin_doc not in text:
    raise RuntimeError("begin{document} anchor not found")
text = text.replace(
    begin_doc,
    "\\input{rev4_figures.tex}\n\n" + begin_doc,
    1,
)

replacements = {
    "fig:stages": "\\RevFigStages",
    "fig:theorem-flow": "\\RevFigTheorem",
    "fig:geometry": "\\RevFigGeometry",
    "fig:hgcdte": "\\RevFigHgCdTe",
    "fig:recycling": "\\RevFigRecycling",
}

for label, macro in replacements.items():
    pattern = re.compile(
        r"\\begin\{figure\}\[t\].*?\\label\{" + re.escape(label) + r"\}\s*\\end\{figure\}",
        re.DOTALL,
    )
    text, count = pattern.subn(lambda _m, m=macro: m, text, count=1)
    if count != 1:
        raise RuntimeError(f"expected one placeholder for {label}, replaced {count}")

# Anchor on the unique theorem label rather than equation whitespace/content.
main_eq = re.compile(
    r"\\begin\{equation\}.*?\\label\{eq:main-theorem\}.*?\\end\{equation\}",
    re.DOTALL,
)
main_replacement = r"""\begin{equation}
\boxed{
\begin{aligned}
n_e+n_h
&\ge n_{e,\cB}^{\rm act}+n_{h,\cB}^{\rm act}\\
&\ge
\frac{2}{\pi e^2(v_{\cB}^{\rm cap})^2}
\int_{\cB}
\frac{\hbar\omega\,\sigma_1^{\rm cross}(\omega)}
{e^{\hbar\omega/(2k_BT)}-1}\,d\omega .
\end{aligned}}
\label{eq:main-theorem}
\end{equation}"""
text, theorem_count = main_eq.subn(lambda _m: main_replacement, text, count=1)
if theorem_count != 1:
    raise RuntimeError(f"expected one main theorem display, reformatted {theorem_count}")

if "placeholder:" in text:
    raise RuntimeError("one or more figure placeholders remain in built source")

OUT.write_text(text, encoding="utf-8")
print(f"wrote {OUT.name}")
print(f"bytes: {OUT.stat().st_size}")
print("journal style: prapplied")
print("font encoding: T1 + Latin Modern")
print("main theorem: two-line single-column display")
for label in replacements:
    print(f"replaced {label}")
