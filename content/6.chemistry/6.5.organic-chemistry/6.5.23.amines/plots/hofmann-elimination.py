"""Hofmann elimination of butan-2-yltrimethylammonium hydroxide (E2), drawn with the H-C1-C2-N unit
antiperiplanar in the plane of the paper. Hydroxide removes a hydrogen of the terminal methyl group
(C1); the C-H bonding pair becomes the C1=C2 pi bond and trimethylamine leaves with the C-N bonding
pair. The major product is but-1-ene (Hofmann orientation)."""

from wikichem import Scheme

s = Scheme()
q = s.molecule(
    "[H:10][CH2:1][CH:2]([CH2:3][CH3:4])[N+:5](C)(C)C",
    coords=[(-0.7, 1.0), (-0.7, 0.0), (0.7, 0.0), (1.57, 0.5), (2.44, 0.0),
            (0.7, -1.0), (0.7, -2.0), (-0.17, -1.5), (1.57, -1.5)],
)
oh = s.molecule("[OH-:9]", at=(-2.4, 1.4), lone_pairs=True)
s.curly(oh.atom(9), q.atom(10), bend=-0.3)
s.curly(q.bond(10, 1), q.bond(1, 2), bend=0.5)
s.curly(q.bond(2, 5), q.atom(5), bend=-0.5)
s.arrow((3.2, 0), (4.6, 0), above="heat")
s.molecule("C=CCC", at=(6.1, 0))
s.plus((7.9, 0))
s.molecule("CN(C)C", at=(9.0, 0))
s.plus((10.2, 0))
s.molecule("O", at=(10.9, 0))
s.draw()
