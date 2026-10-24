"""Hydrolytic deamination of cytosine (1-methylcytosine as a model of the nucleoside). Top: with N3
protonated, water adds to C4 and the C4=N3 electrons move onto N3. Bottom: after proton transfers the
tetrahedral intermediate collapses; the oxygen lone pair re-forms a C=O bond and ammonia leaves,
giving uracil. In DNA this turns a C:G pair into U:G, which repair enzymes recognise because U does
not belong in DNA."""

from wikichem import Scheme

s = Scheme()
y = 0.0
c = s.molecule("CN1C=CC(N)=[NH+]C1=O", at=(0, y))
w = s.molecule("O", at=(c.xy(4)[0] + 1.6, c.xy(4)[1] + 0.8), lone_pairs=True)
s.curly(w.atom(0), c.atom(4), bend=0.4)
s.curly(c.bond(4, 6), c.atom(6), bend=0.6)
s.text((0, y - 2.4), "N3-protonated cytosine")
s.arrow((2.6, y), (4.0, y), above=r"$-$H$^+$")
s.molecule("CN1C=CC(N)(O)NC1=O", at=(6.0, y))

y = -5.0
t = s.molecule("CN1C=CC([NH3+])(O)NC1=O", at=(0, y), lone_pairs=[6])
s.curly(t.atom(6), t.bond(4, 6), bend=0.6)
s.curly(t.bond(4, 5), t.atom(5), bend=0.6)
s.arrow((2.6, y), (4.0, y), above=r"$-$NH$_3$", below=r"$-$H$^+$")
s.molecule("CN1C=CC(=O)NC1=O", at=(6.0, y))
s.text((6.0, y - 2.2), "uracil")
s.draw()
