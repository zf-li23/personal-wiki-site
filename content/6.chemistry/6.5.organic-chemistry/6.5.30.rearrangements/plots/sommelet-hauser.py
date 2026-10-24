"""Sommelet-Hauser rearrangement of benzyltrimethylammonium ion with sodium amide in liquid ammonia.
The benzylic ylide is formed fastest, but the reaction runs through the small equilibrium amount of
the methylide. Its carbanion attacks the ortho carbon of the ring while the ring pi bond shifts and the
benzylic C-N bond breaks: a concerted, thermally allowed [2,3]-sigmatropic shift through a five-membered
cyclic transition state. The dearomatized triene then tautomerizes back to the aromatic ring, giving
N,N-dimethyl-2-methylbenzylamine (the CH2 group has moved into the ortho position)."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
s.molecule("C[N+](C)(C)Cc1ccccc1", at=(0.0, y))
s.text((0.0, y - 2.6), "benzyltrimethylammonium")
s.arrow((2.8, y), (4.2, y), above=r"NaNH$_2$", below=r"NH$_3$(l)")
YLIDE = [(-1.73, 1.0), (-1.73, 0.0), (-2.7, 0.25), (-2.1, -0.95), (-0.87, -0.5),
         (0.0, 0.0), (0.0, 1.0), (0.87, 1.5), (1.73, 1.0), (1.73, 0.0), (0.87, -0.5)]
a = s.molecule("[CH2-][N+](C)(C)CC1=CC=CC=C1", coords=[(x + 7.0, y_ + y - 0.2) for x, y_ in YLIDE], lone_pairs=[0])
s.curly(a.atom(0), a.atom(6), bend=0.5)
s.curly(a.bond(5, 6), a.bond(4, 5), bend=0.6)
s.curly(a.bond(1, 4), a.atom(1), bend=-0.6)
s.text((7.0, y - 2.6), "methylide")
s.arrow((9.8, y), (11.2, y), above="[2,3]")
s.molecule("C=C1C=CC=CC1CN(C)C", at=(13.8, y))
s.text((13.8, y - 2.6), "triene")
s.arrow((16.4, y), (17.8, y), above="tautomerism")
s.molecule("Cc1ccccc1CN(C)C", at=(20.4, y))
s.text((20.4, y - 2.6), "ortho-methylbenzylamine")
s.draw()
