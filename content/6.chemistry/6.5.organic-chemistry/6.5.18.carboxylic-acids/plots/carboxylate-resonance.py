"""The two equivalent resonance structures of the acetate ion. The lone pair on the negatively
charged oxygen forms a C=O pi bond while the original C=O pi pair moves onto the other oxygen; the
negative charge is shared equally by the two oxygens, and the two C-O bonds have the same length."""

from wikichem import Scheme

s = Scheme()
a = s.molecule("[CH3:1][C:2](=[O:3])[O-:4]", at=(0.0, 0.0), lone_pairs=[3, 4])
s.curly(a.atom(4), a.bond(2, 4), bend=-0.8)
s.curly(a.bond(2, 3), a.atom(3), bend=-0.8)
s.arrow((1.5, 0.0), (2.9, 0.0), kind="resonance")
s.molecule("[CH3:1][C:2]([O-:3])=[O:4]", at=(4.4, 0.0), like=a, lone_pairs=[3, 4])
s.draw()
