"""Dynamic induction (polarization by an approaching reagent). As Br2 approaches the pi electrons of
ethene, the Br-Br bond is polarized: the near bromine becomes partly positive, the far one partly
negative. The pi electrons then attack the near bromine while the Br-Br bonding pair leaves as
bromide, giving a cyclic bromonium ion (details in the chapter on alkene additions)."""

from wikichem import Scheme

s = Scheme()
ene = s.molecule("C=C", at=(0, 0), rotate=90)
br2 = s.molecule("BrBr", at=(2.0, 0), lone_pairs=True)
s.label(br2.atom(0), r"$\delta^+$", angle=100, dist=0.75, size=10)
s.label(br2.atom(1), r"$\delta^-$", angle=80, dist=0.75, size=10)
s.curly(ene.bond(0, 1), br2.atom(0), bend=-0.5)
s.curly(br2.bond(0, 1), br2.atom(1), bend=-0.8)
s.arrow((3.8, 0), (5.2, 0))
s.molecule("C1C[Br+]1", at=(6.6, 0), rotate=90)
s.plus((8.0, 0))
s.molecule("[Br-]", at=(9.0, 0), lone_pairs=True)
s.text((6.6, -1.5), "bromonium ion", size=10)
s.draw()
