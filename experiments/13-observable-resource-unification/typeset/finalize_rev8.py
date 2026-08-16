from pathlib import Path

p = Path("rev8_prapplied.tex")
s = p.read_text()
old = r"The selected-support splitting reaches $26.6$ meV;"
new = r"The adjacent-pair separation diagnostic over selected-support points reaches $26.6$ meV;"
count = s.count(old)
if count != 1:
    raise RuntimeError(f"expected exactly one BIA diagnostic phrase, found {count}")
s = s.replace(old, new, 1)
if "The selected-support splitting reaches" in s:
    raise RuntimeError("obsolete ambiguous splitting wording remains")
p.write_text(s)
print("tightened Rev8 BIA splitting diagnostic wording")
