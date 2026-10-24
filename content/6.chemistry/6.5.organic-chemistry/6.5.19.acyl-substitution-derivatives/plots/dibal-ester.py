"""Partial reduction of an ester to an aldehyde with diisobutylaluminium hydride (DIBAL-H) at
-78 C. The Lewis-acidic aluminium binds the carbonyl oxygen and delivers its hydride to the carbonyl
carbon. At low temperature the aluminium hemiacetal (tetrahedral intermediate) does not expel
methoxide, so no aldehyde is present while hydride is still there; aqueous work-up then releases
the aldehyde."""

from wikichem import Scheme

s = Scheme()
y = -2.7  # caption line
ester = s.molecule("CCC(=O)OC", at=(0, 0), lone_pairs=[3])
dibal = s.molecule("CC(C)C[AlH]CC(C)C", at=(0.4, 2.6), show_h=[4])
s.curly(ester.atom(3), dibal.atom(4), bend=-0.4)
s.curly(dibal.bond(4, dibal.mol.GetNumAtoms() - 1), ester.atom(2), bend=0.5)
s.curly(ester.bond(2, 3), ester.atom(3), bend=-0.6)
s.text((0, y), "methyl propanoate")
s.arrow((2.2, 0), (3.6, 0), above=r"$-78\,^\circ$C")
s.molecule("CCC(OC)O[Al](CC(C)C)CC(C)C", at=(6.6, 0))
s.text((6.6, y), "aluminium hemiacetal")
s.arrow((9.3, 0), (10.7, 0), above=r"H$_3$O$^+$")
s.molecule("CCC=O", at=(12.4, 0))
s.text((12.4, y), "propanal")
s.draw()
