"""Key steps of the Hell-Volhard-Zelinsky reaction, with propanoic acid. PBr3 turns some of the acid
into the acyl bromide, which enolizes far more than the acid itself. The enol attacks Br2 (the
oxygen lone pair pushes, the C=C pi bond takes Br+), and loss of HBr gives 2-bromopropanoyl
bromide. Exchange with another molecule of acid gives the 2-bromo acid and regenerates the acyl
bromide, so a catalytic amount of phosphorus suffices."""

from wikichem import Scheme

s = Scheme()
y = -2.4  # caption line
s.molecule("CCC(=O)Br", at=(0, 0), rotate=120)
s.text((0, y), "propanoyl bromide")
s.arrow((1.6, 0), (3.0, 0), kind="equilibrium", above=r"H$^+$")
enol = s.molecule("C/C=C(/O)Br", at=(4.6, 0.3), lone_pairs=[3])
br2 = s.molecule("BrBr", at=(4.4, -1.5), lone_pairs=True)
s.curly(enol.atom(3), enol.bond(2, 3), bend=0.7)
s.curly(enol.bond(1, 2), br2.atom(0), bend=0.4)
s.curly(br2.bond(0, 1), br2.atom(1), bend=0.8)
s.text((4.6, y), "enol of the acyl bromide")
s.arrow((6.6, 0), (8.0, 0), above=r"$-\mathrm{Br}^-$")
s.molecule("CC(Br)C(=[OH+])Br", at=(9.6, 0))
s.arrow((11.2, 0), (12.6, 0), above=r"$-\mathrm{H}^+$")
s.molecule("CC(Br)C(=O)Br", at=(14.0, 0))
s.text((14.0, y), "2-bromopropanoyl bromide")
s.draw()
