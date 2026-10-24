"""Base-catalysed aldol addition of acetaldehyde. Hydroxide removes an alpha proton (a small amount
of enolate forms); the enolate carbon attacks the carbonyl carbon of a second acetaldehyde and the
C=O pi electrons move onto oxygen; the alkoxide takes a proton from water, giving
3-hydroxybutanal and regenerating hydroxide. Every step is reversible."""

from wikichem import Scheme

s = Scheme()
s.molecule("CC=O", at=(-3.2, 0))
s.arrow((-2.2, 0), (-0.8, 0), kind="equilibrium", above=r"HO$^-$", below=r"$-$H$_2$O")
en = s.molecule("C=C[O-]", at=(0.8, 0.9), rotate=180, lone_pairs=[2])
ald = s.molecule("CC=O", at=(1.6, -1.9), rotate=200, lone_pairs=[2])
s.curly(en.atom(2), en.bond(1, 2), bend=0.7)
s.curly(en.bond(0, 1), ald.atom(1), bend=-0.6)
s.curly(ald.bond(1, 2), ald.atom(2), bend=0.7)
s.text((0.0, 2.2), "enolate")
s.arrow((2.8, 0), (4.2, 0), kind="equilibrium")
alk = s.molecule("CC([O-])CC=O", at=(5.8, 0), lone_pairs=[2])
w = s.molecule("[H]O[H]", coords=[(0.0, 0.0), (0.82, -0.57), (1.64, 0.0)], at=(4.6, -2.4), lone_pairs=[1])
s.curly(alk.atom(2), w.atom(0), bend=0.5)
s.curly(w.bond(0, 1), w.atom(1), bend=0.6)
s.arrow((7.6, 0), (9.0, 0), kind="equilibrium", below=r"$-$HO$^-$")
s.molecule("CC(O)CC=O", at=(10.6, 0))
s.text((10.6, -1.5), "3-hydroxybutanal")
s.draw()
