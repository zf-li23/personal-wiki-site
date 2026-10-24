"""Role of zinc chloride in the Lucas reagent (concentrated HCl with ZnCl2), shown for butan-2-ol. The
Lewis acid ZnCl2 binds to the hydroxy oxygen; the weakened C-O bond ionizes to a secondary
carbocation and [ZnCl2(OH)]-, and chloride captures the cation. The insoluble 2-chlorobutane makes
the solution cloudy; tertiary alcohols react at once, secondary within minutes, primary hardly at all."""

from wikichem import Scheme

s = Scheme()
alc = s.molecule("CC(O)CC", at=(0, 0), lone_pairs=[2])
zn = s.molecule("Cl[Zn]Cl", at=(2.6, 1.2))
s.curly(alc.atom(2), zn.atom(1), bend=-0.4)
s.arrow((3.8, 0), (5.2, 0))
cx = s.molecule("CC([OH+][Zn-](Cl)Cl)CC", at=(7.0, 0))
s.curly(cx.bond(1, 2), cx.atom(2), bend=0.8)
s.arrow((9.0, 0), (10.4, 0), below=r"$-$[ZnCl$_2$OH]$^-$")
cat = s.molecule("C[CH+]CC", at=(11.6, 0))
cl = s.molecule("[Cl-]", at=(11.6, -1.8), lone_pairs=True)
s.curly(cl.atom(0), cat.atom(1), bend=0.4)
s.arrow((13.0, 0), (14.4, 0))
s.molecule("CC(Cl)CC", at=(15.6, 0))
s.draw()
