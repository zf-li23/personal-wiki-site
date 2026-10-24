"""Methyl esterification of a carboxylic acid with diazomethane. (1) The acid protonates the
nucleophilic carbon of diazomethane, giving a carboxylate / methyldiazonium ion pair. (2) The
carboxylate attacks the methyl carbon (SN2) and N2 leaves, giving the methyl ester."""

from wikichem import Scheme

s = Scheme()
acid = s.molecule("C[C:1](=O)[O:2][H:3]", at=(0, 0), coords=[(-1.3, -0.5), (-0.4, 0.0), (-0.4, 1.0), (0.47, -0.5), (1.3, 0.0)], lone_pairs=[2])
dm = s.molecule("[CH2-:4][N+:5]#[N:6]", at=(3.3, 0.0), coords=[(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)])
s.curly(dm.atom(4), acid.atom(3), bend=0.5)
s.curly(acid.bond(2, 3), acid.atom(2), bend=0.6)
s.arrow((5.0, 0), (6.4, 0))
car = s.molecule("C[C:1](=O)[O-:2]", at=(8.0, 0), coords=[(-1.3, -0.5), (-0.4, 0.0), (-0.4, 1.0), (0.47, -0.5)], lone_pairs=[2])
me = s.molecule("[CH3:4][N+:5]#[N:6]", at=(10.9, -0.5), coords=[(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)])
s.curly(car.atom(2), me.atom(4), bend=-0.4)
s.curly(me.bond(4, 5), me.atom(5), bend=-0.6)
s.arrow((12.6, 0), (14.0, 0))
s.molecule("CC(=O)OC", at=(15.6, 0))
s.plus((17.0, 0))
s.molecule("N#N", at=(17.9, 0))
s.draw()
