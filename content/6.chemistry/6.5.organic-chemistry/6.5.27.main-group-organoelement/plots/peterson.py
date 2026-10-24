"""Peterson olefination under basic conditions. The alkoxide formed from an alpha-silyl carbanion
and a carbonyl compound attacks silicon intramolecularly; through a four-membered ring with
pentacoordinate silicon, the C-Si and C-O bonds break together on the same side (syn elimination),
giving the alkene and a silanolate. Under acid catalysis the beta-hydroxysilane eliminates anti
instead (an E2-like loss of water and the silyl group), so one diastereomer of the
beta-hydroxysilane can be taken to either alkene geometry."""

from wikichem import Scheme

s = Scheme()
yl = s.molecule("C[Si](C)(C)[CH-]CC", coords=[(-1.0, 1.0), (0, 1.0), (0, 2.0), (1.0, 1.0), (0, 0), (-0.87, -0.5), (-1.74, 0)], lone_pairs=[4])
k = s.molecule("O=CCC", coords=[(2.0, 1.0), (2.0, 0.0), (2.87, -0.5), (3.74, 0)], lone_pairs=[0])
s.curly(yl.atom(4), k.atom(1), bend=0.5)
s.curly(k.bond(0, 1), k.atom(0), bend=-0.7)
s.arrow((4.4, 0.5), (5.8, 0.5))
x = 7.8
ad = s.molecule("C[Si](C)(C)C(CC)C([O-])CC",
                coords=[(-1.0, 1.0), (0, 1.0), (0, 2.0), (-0.6, 1.8), (0, 0), (-0.87, -0.5), (-1.74, 0), (1.0, 0), (1.0, 1.0), (1.87, -0.5), (2.74, 0)],
                at=(x, 0), lone_pairs=[8])
s.curly(ad.atom(8), ad.atom(1), bend=0.6)
s.curly(ad.bond(1, 4), ad.bond(4, 7), bend=0.6)
s.curly(ad.bond(7, 8), ad.atom(8), bend=-0.6)
s.text((x + 0.5, -1.6), "syn elimination", size=12)
s.arrow((x + 3.4, 0.5), (x + 4.8, 0.5))
s.molecule("CCC=CCC", at=(x + 7.4, 0.5))
s.plus((x + 9.8, 0.5))
s.molecule("C[Si](C)(C)[O-]", at=(x + 11.2, 0.5))
s.draw()
