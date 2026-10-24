"""SN1-type tert-alkylation of a silyl enol ether (Reetz). TiCl4 abstracts chloride from tert-butyl
chloride to give the tert-butyl cation. The oxygen lone pair of the silyl enol ether pushes the C=C
electrons onto the cation, forming the C-C bond and a silyl oxocarbenium ion; chloride removes the
trimethylsilyl group from oxygen, giving 2-tert-butylcyclohexanone. An enolate could not do this by
SN2 at a tertiary carbon."""

from wikichem import Scheme

s = Scheme()
y = 0.0
se = s.molecule("C[Si](C)(C)OC1=CCCCC1", at=(0, y), lone_pairs=[4])
tb = s.molecule("C[C+](C)C", at=(2.8, y + 1.5))
s.curly(se.atom(4), se.bond(4, 5), bend=0.6)
s.curly(se.bond(5, 6), tb.atom(1), bend=-0.4)
s.text((2.8, y + 3.0), r"from $t$-BuCl + TiCl$_4$")
s.arrow((4.4, y), (5.8, y))
ox = s.molecule("C[Si](C)(C)[O+]=C1CCCCC1C(C)(C)C", at=(8.4, y))
cl = s.molecule("[Cl-]", at=(6.4, y + 2.0), lone_pairs=True)
s.curly(cl.atom(0), ox.atom(1), bend=-0.4)
s.curly(ox.bond(1, 4), ox.atom(4), bend=-0.6)
s.text((8.4, y - 2.4), "silyl oxocarbenium ion")
s.arrow((10.8, y), (12.2, y), below=r"$-$Me$_3$SiCl")
s.molecule("O=C1CCCCC1C(C)(C)C", at=(14.0, y))
s.draw()
