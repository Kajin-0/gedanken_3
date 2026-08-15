#!/usr/bin/env python3
"""Build the self-contained production TeX source for Experiment 13 Rev. 4.

The scientific source remains rev4_unified_prapplied.tex. This script performs
only production transformations:
  * select the Physical Review Applied REVTeX journal style and float handling;
  * enable T1 font encoding for bibliography diacritics;
  * load native TikZ figure definitions;
  * replace the five explicit figure placeholders by figure macros;
  * give the central population theorem full-width treatment without changing it;
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

# The central theorem was only ~14 pt too wide in a single APS column. Give the
# unchanged equation a full-width REVTeX widetext block so it remains the visual
# center of the manuscript instead of shrinking or abbreviating the formula.
main_eq = re.compile(
    r"(\\begin\{equation\}\s*\\boxed\{.*?\\label\{eq:main-theorem\}\s*\\end\{equation\})",
    re.DOTALL,
)
text, theorem_count = main_eq.subn(
    lambda m: "\\begin{widetext}\n" + m.group(1) + "\n\\end{widetext}",
    text,
    count=1,
)
if theorem_count != 1:
    raise RuntimeError(f"expected one main theorem display, wrapped {theorem_count}")

if "placeholder:" in text:
    raise RuntimeError("one or more figure placeholders remain in built source")

OUT.write_text(text, encoding="utf-8")
print(f"wrote {OUT.name}")
print(f"bytes: {OUT.stat().st_size}")
print("journal style: prapplied")
print("font encoding: T1")
print("main theorem: widetext")
for label in replacements:
    print(f"replaced {label}")
