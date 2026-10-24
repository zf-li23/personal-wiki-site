"""Amide formation with a carbodiimide (drawn with isopropyl groups, i.e. DIC, for compactness;
DCC carries cyclohexyl groups). The carboxylate adds to the central carbon of the protonated
carbodiimide and gives an O-acylisourea, an activated ester whose leaving group becomes a very
stable urea. The amine then attacks the acyl carbon (addition-elimination); the urea leaves."""

from wikichem import Scheme

s = Scheme()
y1, y2 = 0.0, -6.6  # the two rows
carb = s.molecule("CC(=O)[O-]", at=(-1.0, y1), lone_pairs=[3])
cdi = s.molecule("CC(C)N=C=[NH+]C(C)C", at=(3.1, y1 + 0.3))
s.curly(carb.atom(3), cdi.atom(4), bend=-0.3)
s.curly(cdi.bond(4, 5), cdi.atom(5), bend=-0.7)
s.text((3.1, y1 - 1.9), "protonated carbodiimide")
s.arrow((5.6, y1), (7.0, y1))
s.molecule("CC(=O)OC(=NC(C)C)NC(C)C", at=(9.6, y1), rotate=90)
s.text((9.6, y1 - 2.9), "O-acylisourea")

amine = s.molecule("CN", at=(-0.9, y2 + 2.1), lone_pairs=[1])
acyl = s.molecule("CC(=O)OC(=NC(C)C)NC(C)C", at=(2.2, y2), rotate=90, lone_pairs=[2])
s.curly(amine.atom(1), acyl.atom(1), bend=0.4)
s.curly(acyl.bond(1, 2), acyl.atom(2), bend=0.8)
s.arrow((4.4, y2), (6.0, y2), above="add.-elim.", below="proton transfers")
s.molecule("CNC(C)=O", at=(7.8, y2))
s.plus((9.3, y2))
s.molecule("CC(C)NC(=O)NC(C)C", at=(11.6, y2))
s.text((7.8, y2 - 1.8), "N-methylacetamide")
s.text((11.6, y2 - 1.8), "urea")
s.draw()
