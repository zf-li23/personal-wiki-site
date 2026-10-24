"""Mechanism of the acid-catalysed (Fischer) esterification of acetic acid with methanol (AAc2).
Every step is reversible; read backwards, the same sequence is the acid-catalysed hydrolysis of
the ester. Top row: the carbonyl oxygen is protonated, methanol adds to the activated carbonyl
carbon. Bottom row: after proton transfer, water is a good leaving group; the remaining hydroxyl
pushes it out, and loss of the proton from the carbonyl oxygen gives the ester."""

from wikichem import Scheme

s = Scheme()
y1, y2 = 0.0, -4.2  # the two rows
s.molecule("CC(=O)O", at=(0, y1))
s.arrow((1.2, y1), (2.6, y1), kind="equilibrium", above=r"H$^+$")
prot = s.molecule("CC(O)=[OH+]", at=(3.9, y1), lone_pairs=[])
meoh = s.molecule("CO", at=(6.2, y1 + 0.6), lone_pairs=[1])
s.curly(meoh.atom(1), prot.atom(1), bend=0.4)
s.curly(prot.bond(1, 3), prot.atom(3), bend=-0.7)
s.arrow((7.4, y1), (8.8, y1), kind="equilibrium")
s.molecule("CC(O)(O)[OH+]C", at=(10.3, y1))
s.text((10.3, y1 - 1.6), "tetrahedral intermediate")

s.arrow((-0.4, y2), (1.0, y2), kind="equilibrium", above="proton", below="transfer")
ti = s.molecule("CC(O)([OH2+])OC", at=(2.8, y2), lone_pairs=[2])
s.curly(ti.atom(2), ti.bond(1, 2), bend=0.7)
s.curly(ti.bond(1, 3), ti.atom(3), bend=-0.6)
s.arrow((4.6, y2), (6.0, y2), kind="equilibrium", below=r"$-\mathrm{H_2O}$")
s.molecule("CC(OC)=[OH+]", at=(7.2, y2))
s.text((7.2, y2 - 1.6), "protonated ester")
s.arrow((8.4, y2), (9.8, y2), kind="equilibrium", above=r"$-\mathrm{H}^+$")
s.molecule("CC(=O)OC", at=(11.1, y2))
s.text((11.1, y2 - 1.6), "methyl acetate")
s.draw()
