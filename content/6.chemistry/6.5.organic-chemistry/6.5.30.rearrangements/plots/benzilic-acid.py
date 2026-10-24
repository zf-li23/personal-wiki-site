"""Benzilic acid rearrangement. Hydroxide adds to one carbonyl group of benzil. In the tetrahedral
alkoxide, the oxygen lone pair re-forms C=O and pushes a phenyl group, with its electron pair, onto the
neighbouring carbonyl carbon; that C=O pi bond moves onto oxygen (a 1,2-shift to an electron-poor
carbonyl carbon, rate-determining). Fast proton transfer from the carboxylic acid to the alkoxide
gives the benzilate ion; acidification gives benzilic acid."""

from wikichem import Scheme

s = Scheme(scale=0.4)
y = 0.0
oh = s.molecule("[OH-]", at=(-0.4, y + 2.2), lone_pairs=True)
b = s.molecule("O=C(c1ccccc1)C(=O)c1ccccc1", at=(1.4, y), lone_pairs=[0])
s.curly(oh.atom(0), b.atom(1), bend=-0.4)
s.curly(b.bond(0, 1), b.atom(0), bend=0.6)
s.text((1.4, y - 4.0), "benzil")
s.arrow((4.0, y), (5.4, y))
t = s.molecule("[O-]C(O)(c1ccccc1)C(=O)c1ccccc1", at=(8.2, y), lone_pairs=[0])
s.curly(t.atom(0), t.bond(0, 1), bend=0.6)
s.curly(t.bond(1, 3), t.atom(9), bend=-0.6)
s.curly(t.bond(9, 10), t.atom(10), bend=0.6)
s.text((8.2, y - 4.0), "tetrahedral alkoxide")
s.arrow((11.0, y), (12.4, y), above="1,2-Ph shift", below="slow")
s.molecule("O=C(O)C([O-])(c1ccccc1)c1ccccc1", at=(14.8, y))
s.arrow((17.2, y), (18.6, y), below="H$^+$ transfer")
s.molecule("[O-]C(=O)C(O)(c1ccccc1)c1ccccc1", at=(21.0, y))
s.text((21.0, y - 4.0), "benzilate")
s.draw()
