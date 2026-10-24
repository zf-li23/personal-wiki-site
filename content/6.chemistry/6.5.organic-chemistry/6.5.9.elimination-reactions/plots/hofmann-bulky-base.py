"""Regioselectivity of E2 of 2-bromo-2-methylbutane. Top: the small base ethoxide removes a hydrogen
from the inner CH2 group and gives mainly the more substituted alkene (Zaitsev product). Bottom: the
bulky tert-butoxide cannot reach the CH2 hydrogens easily and removes one of the more accessible,
more numerous methyl hydrogens, giving mainly the less substituted alkene (Hofmann product)."""

from wikichem import Scheme

s = Scheme()
for y, base, k, prod, name in ((0.0, "CC[O-]", 1, "CC=C(C)C", "Zaitsev, 70%"),
                               (-4.0, "CC(C)(C)[O-]", 3, "CCC(C)=C", "Hofmann, 72%")):
    sub = s.molecule("CCC(C)(C)Br", at=(2.6, y), show_h=[k], lone_pairs=[5])
    o = 2 if base == "CC[O-]" else 4
    b = s.molecule(base, at=(-0.4, y + 1.0), lone_pairs=[o])
    s.curly(b.atom(o), sub.h(k), bend=-0.4)
    hk = sub.mol.GetAtomWithIdx(k).GetNeighbors()
    h = [a.GetIdx() for a in hk if a.GetSymbol() == "H"][0]
    s.curly(sub.bond(k, h), sub.bond(k, 2), bend=-0.8)
    s.curly(sub.bond(2, 5), sub.atom(5), bend=0.7)
    s.arrow((4.8, y), (6.2, y))
    s.molecule(prod, at=(7.8, y))
    s.text((7.8, y - 1.4), name)
s.text((-0.4, -0.4), "ethoxide")
s.text((-0.4, -4.6), "tert-butoxide")
s.draw()
