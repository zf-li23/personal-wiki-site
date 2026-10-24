"""Acid-catalysed hydrolysis of cyclohexene oxide. The protonated epoxide is attacked by water at one
ring carbon from the face opposite to the C-O bond (backside attack), the C-O bond breaks and the
ring strain is released; loss of a proton gives trans-cyclohexane-1,2-diol."""

from wikichem import Scheme

s = Scheme()
ep = s.molecule("C1CCC2[OH+]C2C1", at=(0, 0))
w = s.molecule("O", at=(-1.0, -2.2), explicit_h=True, lone_pairs=[0])
s.curly(w.atom(0), ep.atom(5), bend=-0.3)
s.curly(ep.bond(5, 4), ep.atom(4), bend=-0.7)
s.text((0, 1.9), "protonated epoxide")
s.arrow((2.2, 0), (3.6, 0), below=r"$-$H$^+$")
s.molecule("O[C@@H]1CCCC[C@H]1O", at=(5.4, 0))
s.text((5.4, -1.9), "trans-diol")
s.draw()
