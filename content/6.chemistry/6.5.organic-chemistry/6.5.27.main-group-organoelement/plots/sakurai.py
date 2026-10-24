"""Hosomi-Sakurai allylation of benzaldehyde. Top: the Lewis acid TiCl4 binds the carbonyl oxygen;
the terminal carbon of allyltrimethylsilane (the carbon remote from silicon) attacks the activated
carbonyl carbon. Bottom: the new carbocation is beta to silicon and is stabilised by
hyperconjugation with the C-Si bond, which lies parallel to the empty p orbital; a chloride (or
other nucleophile) attacks silicon and the C-Si electrons form the new C=C bond, so the double bond
moves (allyl transposition) and the homoallylic alkoxide is obtained."""

from wikichem import Scheme

s = Scheme()
al = s.molecule("C=CC[Si](C)(C)C", coords=[(0, 0), (-0.87, -0.5), (-1.74, 0), (-2.61, -0.5), (-2.61, -1.5), (-3.48, 0), (-2.61, 0.5)][:7])
ald = s.molecule("*[O+]=Cc1ccccc1",
                 coords=[(2.4, 2.6), (1.9, 1.73), (1.4, 0.87), (2.4, 0.87), (2.9, 0.0), (3.9, 0.0), (4.4, 0.87), (3.9, 1.73), (2.9, 1.73)][:9],
                 labels={0: "Cl$_4$Ti$^-$"})
s.curly(al.bond(0, 1), ald.atom(2), bend=-0.5)
s.curly(ald.bond(1, 2), ald.atom(1), bend=0.6)
s.arrow((6.0, 0.2), (6.0, -1.8))
y = -4.4
cat = s.molecule("C[Si](C)(C)C[CH+]CC(O*)c1ccccc1",
                 coords=[(-3.0, 1.2), (-2.0, 1.2), (-2.0, 2.2), (-2.6, 0.4), (-1.0, 1.2), (-0.5, 0.33), (0.5, 0.33), (1.0, -0.54),
                         (0.5, -1.4), (0.9, -2.3), (2.0, -0.54), (2.5, 0.33), (3.5, 0.33), (4.0, -0.54), (3.5, -1.4), (2.5, -1.4)],
                 at=(0, y), labels={9: "TiCl$_4^-$"})
s.orbital(cat.atom(5), angle=90, phase=0)
cl = s.molecule("[Cl-]", at=(-3.6, y + 2.6), lone_pairs=True)
s.curly(cl.atom(0), cat.atom(1), bend=0.4)
s.curly(cat.bond(1, 4), cat.bond(4, 5), bend=0.6)
s.arrow((5.0, y), (6.4, y), above="H$_2$O")
s.molecule("C=CCC(O)c1ccccc1", at=(10.4, y))
s.plus((13.2, y))
s.molecule("C[Si](C)(C)Cl", at=(14.6, y))
s.draw()
