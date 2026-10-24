"""Mukaiyama aldol reaction. TiCl4 coordinates to the oxygen of benzaldehyde and makes its carbonyl
carbon strongly electrophilic. The oxygen lone pair of the silyl enol ether of cyclohexanone pushes
the C=C electrons onto the aldehyde carbon (open transition state) and the C=O electrons move onto
the titanium-bound oxygen. Loss of the silyl group from the oxocarbenium ion and aqueous work-up
give the beta-hydroxy ketone."""

from wikichem import Scheme

s = Scheme()
se = s.molecule("C[Si](C)(C)OC1=CCCCC1", at=(0, 0), lone_pairs=[4])
c6 = se.xy(6)
ald = s.molecule("O=C*", coords=[(c6[0] + 2.2, c6[1] + 0.5), (c6[0] + 1.4, c6[1] + 1.1), (c6[0] + 1.5, c6[1] + 2.1)],
                 labels={2: "Ph"}, lone_pairs=[0])
ti = ald.xy(0) + (1.4, -0.2)
s.text(ti, r"TiCl$_4$")
s.partial(ald.atom(0), ti - (0.75, -0.1))
s.curly(se.atom(4), se.bond(4, 5), bend=-0.6)
s.curly(se.bond(5, 6), ald.atom(1), bend=-0.4)
s.curly(ald.bond(0, 1), ald.atom(0), bend=0.6)
s.text((0, -2.0), "silyl enol ether")
s.arrow((4.8, 0), (6.4, 0), above="C$-$C bond formation", below=r"then H$_2$O")
s.molecule("O=C1CCCCC1C(O)c1ccccc1", at=(9.0, 0))
s.text((9.0, -3.0), "beta-hydroxy ketone")
s.draw()
