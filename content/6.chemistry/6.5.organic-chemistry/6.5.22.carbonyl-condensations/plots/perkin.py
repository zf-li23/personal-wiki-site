"""Intramolecular acyl transfer in the Perkin reaction. The alkoxide formed when the enolate of
acetic anhydride adds to benzaldehyde attacks the nearby acetyl carbonyl carbon, through a
six-membered cyclic tetrahedral intermediate; its collapse re-forms C=O and expels the carboxylate,
so the acetyl group has moved from the anhydride oxygen to the former aldehyde oxygen. E1cB loss of
acetate and hydrolysis then give (E)-cinnamic acid."""

from wikichem import Scheme

s = Scheme()
cyc = s.molecule("O1C(c2ccccc2)CC(=O)OC1([O-])C", at=(6.0, 0), lone_pairs=[13])
s.curly(cyc.atom(13), cyc.bond(12, 13), bend=0.7)
s.curly(cyc.bond(11, 12), cyc.atom(11), bend=0.7)
s.text((6.0, -3.0), "cyclic intermediate")
# same atom order: O(alkoxide), CH, phenyl x6, CH2, C, O, O(bridge), acetyl C, O, CH3
op = s.molecule("[O-]C(c1ccccc1)CC(=O)OC(=O)C", at=(0, 0), like=cyc, lone_pairs=[0])
s.curly(op.atom(0), op.atom(12), bend=0.5)
s.curly(op.bond(12, 13), op.atom(13), bend=-0.7)
s.text((0, -3.0), "alkoxide")
s.arrow((2.2, 0), (3.6, 0), kind="equilibrium")
s.arrow((8.4, 0), (9.8, 0), kind="equilibrium")
s.molecule("CC(=O)OC(c1ccccc1)CC(=O)[O-]", at=(12.4, 0))
s.text((12.4, -3.0), "acetyl transferred")
s.draw()
