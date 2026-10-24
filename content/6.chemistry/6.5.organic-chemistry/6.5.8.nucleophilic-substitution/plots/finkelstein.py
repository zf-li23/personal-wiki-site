"""Finkelstein reaction (SN2). Iodide attacks C1 of 1-bromobutane from the side opposite to bromine;
the C-Br bonding pair leaves with bromide. In acetone NaI dissolves but NaBr precipitates, which
pulls the equilibrium to 1-iodobutane."""

from wikichem import Scheme

CHAIN = [(0.0, 0.0), (-0.5, 1.2), (0.4, 2.15), (-0.1, 3.35)]  # C1..C4, C1-Br along +x

s = Scheme()
i = s.molecule("[I-]", at=(-2.2, 0), lone_pairs=True)
rb = s.molecule("C(CCC)Br", coords=CHAIN + [(1.4, 0.0)], lone_pairs=[4])
s.curly(i.atom(0), rb.atom(0), bend=0.3)
s.curly(rb.bond(0, 4), rb.atom(4), bend=-0.8)
s.text((0.0, -1.1), "1-bromobutane", size=10)
s.arrow((2.6, 0.5), (4.2, 0.5), above="acetone")
s.molecule("C(CCC)I", coords=[(x + 5.6, y) for x, y in CHAIN] + [(7.0, 0.0)])
s.plus((8.1, 0.5))
s.text((9.6, 0.5), r"NaBr$\downarrow$")
s.draw()
