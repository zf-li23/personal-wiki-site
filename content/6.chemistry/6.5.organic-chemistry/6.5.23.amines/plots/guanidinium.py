"""Protonation of guanidine. The proton adds to the sp2 imine nitrogen; in the guanidinium ion the
positive charge is shared equally by all three nitrogens (three equivalent resonance structures,
interconverted by the curved arrows), which makes guanidine one of the strongest neutral organic
bases (pKa of the conjugate acid 13.6 in water). Amidines such as DBU are stabilised the same way
over two nitrogens."""

from wikichem import Scheme

s = Scheme()
g = s.molecule("N=C(N)N", at=(0, 0), lone_pairs=[0])
h = s.molecule("[H][OH2+]", coords=[(0, 0), (0.9, 0.0)], at=(g.xy(0)[0] + 1.4, g.xy(0)[1] + 0.9))
s.curly(g.atom(0), h.atom(0), bend=-0.4)
s.curly(h.bond(0, 1), h.atom(1), bend=-0.7)
s.text((0, -1.8), "guanidine")
s.arrow((2.4, 0), (3.6, 0), below=r"$-$H$_2$O")
a = s.molecule("[NH2+]=C(N)N", at=(5.6, 0), like=g, lone_pairs=[2])
s.curly(a.atom(2), a.bond(1, 2), bend=0.6)
s.curly(a.bond(0, 1), a.atom(0), bend=0.6)
s.arrow((6.8, 0), (8.0, 0), kind="resonance")
b = s.molecule("NC(=[NH2+])N", at=(9.4, 0), like=g, lone_pairs=[3])
s.curly(b.atom(3), b.bond(1, 3), bend=0.6)
s.curly(b.bond(1, 2), b.atom(2), bend=0.6)
s.arrow((10.8, 0), (12.0, 0), kind="resonance")
s.molecule("NC(N)=[NH2+]", at=(13.4, 0), like=g)
s.text((9.4, -1.8), "guanidinium ion: charge on all three N")
s.draw()
