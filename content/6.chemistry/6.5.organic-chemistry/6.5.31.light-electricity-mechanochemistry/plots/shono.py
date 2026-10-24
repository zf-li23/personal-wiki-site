"""Shono oxidation (anodic alpha-methoxylation) of methyl pyrrolidine-1-carboxylate in methanol.
The nitrogen lone pair loses one electron at the anode; the radical cation loses an alpha
proton, giving an alpha-amino radical, which is oxidized further (second electron) to the
N-acyliminium ion. Methanol adds to the iminium carbon and loses a proton, giving the
2-methoxy carbamate, a stable precursor of the N-acyliminium ion for Lewis-acid substitutions."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("COC(=O)N1CCCC1", at=(0.0, y))
s.arrow((2.4, y), (3.9, y), above=r"$-$e$^-$", below="anode")
s.molecule("COC(=O)[N+]1CCCC1", at=(6.6, y))
s.text((6.6, y - 2.4), "radical cation")
s.arrow((9.0, y), (10.5, y), above=r"$-$H$^+$")
s.molecule("COC(=O)N1CCC[CH]1", at=(13.2, y))
s.text((13.2, y - 2.4), "alpha-amino radical")
y2 = -5.2
s.arrow((-0.8, y2), (0.7, y2), above=r"$-$e$^-$")
im = s.molecule("COC(=O)[N+]1=CCCC1", at=(3.4, y2))
me = s.molecule("CO", at=(5.8, y2 + 1.8), lone_pairs=[1])
s.curly(me.atom(1), im.atom(5), bend=0.4)
s.curly(im.bond(4, 5), im.atom(4), bend=-0.6)
s.text((3.4, y2 - 2.4), "N-acyliminium ion")
s.arrow((6.6, y2), (8.2, y2), above=r"$-$H$^+$")
s.molecule("COC(=O)N1CCCC1OC", at=(11.0, y2))
s.text((11.0, y2 - 2.4), "2-methoxy carbamate")
s.draw()
