"""Conversion of a carboxylic acid into the acyl chloride with thionyl chloride. The acid first
attacks sulfur and loses HCl, giving an acyl chlorosulfite, in which the poor OH leaving group has
become a good one. Chloride adds to the carbonyl carbon; the tetrahedral intermediate collapses and
expels chlorosulfite, which falls apart into SO2 and chloride. The gases SO2 and HCl leave the
mixture and drive the reaction to completion."""

from wikichem import Scheme

s = Scheme()
y = -1.9  # caption line
cl = s.molecule("[Cl-]", at=(-0.6, 1.9), lone_pairs=True)
cs = s.molecule("CC(=O)OS(=O)Cl", at=(0, 0), lone_pairs=[2])
s.curly(cl.atom(0), cs.atom(1), bend=-0.4)
s.curly(cs.bond(1, 2), cs.atom(2), bend=-0.8)
s.text((0, y), "acyl chlorosulfite")
s.arrow((2.3, 0), (3.7, 0))
ti = s.molecule("CC([O-])(Cl)OS(=O)Cl", at=(5.9, 0), lone_pairs=[2])
s.curly(ti.atom(2), ti.bond(1, 2), bend=-0.7)
s.curly(ti.bond(1, 4), ti.atom(4), bend=0.6)
s.text((5.9, y), "tetrahedral intermediate")
s.arrow((8.2, 0), (9.6, 0))
s.molecule("CC(=O)Cl", at=(10.6, 0))
s.plus((11.9, 0))
s.molecule("O=S=O", coords=[(-0.8, -0.45), (0, 0), (0.8, -0.45)], at=(13.2, 0.1))
s.plus((14.5, 0))
s.molecule("[Cl-]", at=(15.3, 0))
s.text((13.2, y), r"SO$_2$")
s.text((10.6, y), "acetyl chloride")
s.draw()
