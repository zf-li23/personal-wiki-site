"""Delocalization in the phthalimide anion. The negative charge on nitrogen can move onto either
carbonyl oxygen (the arrows lead to the second structure; the third, with the charge on the other
oxygen, is equivalent). Spreading the charge over two carbonyl groups makes the N-H of an imide about
as acidic as phenol."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("[O:1]=[C:2]1[N-:3][C:4](=[O:5])c2ccccc21", at=(0.0, 0.0), lone_pairs=[3])
s.curly(a.atom(3), a.bond(2, 3), bend=-0.7)
s.curly(a.bond(1, 2), a.atom(1), bend=-0.8)
s.arrow((2.0, 0.0), (3.3, 0.0), kind="resonance")
s.molecule("[O-:1][C:2]1=[N:3][C:4](=[O:5])c2ccccc21", at=(5.3, 0.0), like=a)
s.arrow((7.3, 0.0), (8.6, 0.0), kind="resonance")
s.molecule("[O:1]=[C:2]1[N:3]=[C:4]([O-:5])c2ccccc21", at=(10.6, 0.0), like=a)
s.draw()
