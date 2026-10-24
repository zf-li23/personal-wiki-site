"""Ring expansion during dehydration of 1-cyclobutylethanol. Loss of water from the protonated alcohol
gives the secondary 1-cyclobutylethyl cation; a ring C-C bond migrates to the cationic carbon,
enlarging the strained four-membered ring to a five-membered ring (cyclopentyl cation, relief of
about 85 kJ/mol of ring strain); loss of a proton gives 1-methylcyclopentene."""

from wikichem import Scheme

s = Scheme()
ox = s.molecule("C[CH]([OH2+])C1CCC1", at=(0, 0))
s.curly(ox.bond(1, 2), ox.atom(2), bend=0.7)
s.arrow((1.9, 0), (3.3, 0), below=r"$-$H$_2$O")
cat = s.molecule("C[CH+]C1CCC1", at=(4.9, 0))
s.curly(cat.bond(2, 3), cat.atom(1), bend=-0.7)
s.arrow((6.6, 0), (8.0, 0), below="ring expansion")
cp = s.molecule("CC1([H])CCC[CH+]1", coords=[(-1.0, 0.0), (0, 0), (0.0, 1.0), (0.31, -0.95), (1.31, -0.95), (1.62, 0), (0.81, 0.59)], at=(9.2, 0.2))
w = s.molecule("O", at=(8.4, 2.0), explicit_h=True, lone_pairs=[0])
s.curly(w.atom(0), cp.atom(2), bend=-0.4)
s.curly(cp.bond(1, 2), cp.bond(1, 6), bend=-0.8)
s.arrow((11.6, 0), (13.0, 0), below=r"$-$H$_3$O$^+$")
s.molecule("CC1=CCCC1", at=(14.4, 0))
s.draw()
