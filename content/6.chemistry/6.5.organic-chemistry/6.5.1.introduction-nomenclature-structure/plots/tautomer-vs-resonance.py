"""Tautomers versus resonance structures. Top: acetone and its enol (propen-2-ol) are two compounds
in equilibrium (equilibrium arrows); a hydrogen atom changes position. Bottom: the two resonance
structures of the enolate ion differ only in the placement of electrons (double-headed arrow); the
atoms do not move."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("CC(C)=O", at=(0, y), rotate=-90)
s.arrow((1.4, y), (2.8, y), kind="equilibrium")
s.molecule("C=C(C)O", at=(4.2, y), rotate=-90)
s.text((2.1, y - 1.6), "tautomers: H moves (two compounds)", size=10)

y = -3.6
e = s.molecule("[CH2-:1][C:2]([CH3:3])=[O:4]", at=(0, y), rotate=-90, lone_pairs=[1, 4])
s.curly(e.atom(1), e.bond(1, 2), bend=-0.7)
s.curly(e.bond(2, 4), e.atom(4), bend=-0.7)
s.arrow((1.6, y), (2.6, y), kind="resonance")
s.molecule("[CH2:1]=[C:2]([CH3:3])[O-:4]", at=(4.2, y), like=e, lone_pairs=[4])
s.text((2.1, y - 1.6), "resonance: only electrons move (one ion)", size=10)
s.draw()
