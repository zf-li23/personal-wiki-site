"""Hydrolytic deamination, the reaction of both classes of base editor.

Top: cytosine. The zinc-bound hydroxide of the deaminase attacks C-4 of the (N-3 protonated) ring; the
tetrahedral intermediate collapses, expelling ammonia, to give uracil, which pairs with adenine and is
replicated as thymine. Bottom: the same addition-elimination at C-6 of adenine gives hypoxanthine (inosine as
the nucleoside), which pairs with cytosine and is read as guanine. R = deoxyribose 5'-phosphate in the
chain. Both enzymes act only on single-stranded nucleic acid, which is what confines an editor to the window
of the R loop.
"""

from wikichem import Scheme

s = Scheme()
lab = {0: "R"}

# ---- cytosine -> uracil -------------------------------------------------------------------------
y = 0.0
cyt = s.molecule("*N1C(=O)N=C(N)C=C1", at=(0, y), labels=lab, lone_pairs=[4])
s.text((0, y - 2.9), "cytosine (single-stranded DNA)", size=10)
oh = s.molecule("[OH-]", at=(4.3, y + 1.5), lone_pairs=True)
s.label(oh.atom(0), "Zn$^{2+}$-bound", angle=90, dist=0.75, size=9)
s.curly(oh.atom(0), cyt.atom(5))
s.curly(cyt.bond(4, 5), cyt.atom(4))
s.arrow((5.6, y), (7.2, y), above="addition")
tet = s.molecule("*N1C(=O)NC(N)(O)C=C1", at=(10.2, y), labels=lab, lone_pairs=[7])
s.text((10.2, y - 2.9), "tetrahedral intermediate", size=10)
s.curly(tet.atom(7), tet.bond(5, 7))
s.curly(tet.bond(5, 6), tet.atom(6))
s.arrow((13.4, y), (15.0, y), above="elimination", below="− NH$_3$")
ura = s.molecule("*N1C(=O)NC(=O)C=C1", at=(18.0, y), labels=lab)
s.text((18.0, y - 2.9), "uracil: pairs with A, replicated as T", size=10)

# ---- adenine -> hypoxanthine --------------------------------------------------------------------
y = -6.8
ade = s.molecule("*n1cnc2c(N)ncnc12", at=(0, y), labels=lab, lone_pairs=[5])
s.text((0, y - 2.9), "adenine (single-stranded DNA)", size=10)
s.arrow((4.4, y), (6.8, y), above="H$_2$O, Zn$^{2+}$", below="− NH$_3$")
hyp = s.molecule("*n1cnc2c(=O)[nH]cnc12", at=(10.6, y), labels=lab)
s.text((10.6, y - 2.9), "hypoxanthine: pairs with C, read as G", size=10)
s.text((18.0, y + 0.4), "the same addition–elimination at C-6;", size=10)
s.text((18.0, y - 0.5), "no DNA glycosylase removes inosine,", size=10)
s.text((18.0, y - 1.4), "so no inhibitor is needed", size=10)
s.draw()
