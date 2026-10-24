"""Acid-catalysed hydrolysis of an amide (acetamide). The amide is protonated on oxygen (not on
nitrogen, whose lone pair is delocalized into the carbonyl); water adds to the activated carbonyl
carbon. Proton transfer to nitrogen turns NH2 into NH3+, a good leaving group, which the hydroxyl
pushes out. Ammonia is then protonated (pKa of NH4+ 9.25), which makes the reaction irreversible
in acid."""

from wikichem import Scheme

s = Scheme()
y1, y2 = 0.0, -4.2  # the two rows
w = s.molecule("O", at=(-1.9, 0.9), lone_pairs=True)
am = s.molecule("CC(N)=[OH+]", at=(0, y1))
s.curly(w.atom(0), am.atom(1), bend=0.4)
s.curly(am.bond(1, 3), am.atom(3), bend=-0.7)
s.text((0, y1 - 1.7), "O-protonated acetamide")
s.arrow((1.6, y1), (3.0, y1), kind="equilibrium", above="slow")
s.molecule("CC(N)(O)[OH2+]", at=(4.5, y1))
s.arrow((6.0, y1), (7.4, y1), kind="equilibrium", above="proton", below="transfer")
s.molecule("CC(O)(O)[NH3+]", at=(8.9, y1))

ti = s.molecule("CC(O)(O)[NH3+]", at=(1.0, y2), lone_pairs=[2])
s.curly(ti.atom(2), ti.bond(1, 2), bend=0.7)
s.curly(ti.bond(1, 4), ti.atom(4), bend=-0.6)
s.arrow((2.6, y2), (4.0, y2), below=r"$-\mathrm{NH_3}$")
s.molecule("CC(O)=[OH+]", at=(5.0, y2))
s.arrow((6.6, y2), (8.0, y2), above=r"NH$_3$", below="fast")
s.molecule("CC(=O)O", at=(9.2, y2))
s.plus((10.4, y2))
s.molecule("[NH4+]", at=(11.3, y2))
s.text((10.2, y2 - 1.7), "acetic acid + ammonium")
s.draw()
