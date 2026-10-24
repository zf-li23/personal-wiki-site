"""Acid-catalysed bromination of acetone, the step after the rate-determining enolization. The
oxygen lone pair of the enol pushes the C=C pi electrons onto bromine, which loses bromide; the
resulting protonated alpha-bromo ketone (an oxocarbenium ion) loses a proton to give bromoacetone."""

from wikichem import Scheme

s = Scheme()
s.molecule("CC(C)=O", at=(-3.4, 0))
s.arrow((-2.2, 0), (-0.9, 0), kind="equilibrium", above=r"H$^+$", below="slow")
enol = s.molecule("C=C(O)C", at=(0.8, 0.6), rotate=180, lone_pairs=[2])
br2 = s.molecule("BrBr", at=(-0.4, -1.5), lone_pairs=True)
s.curly(enol.atom(2), enol.bond(1, 2), bend=0.7)
s.curly(enol.bond(0, 1), br2.atom(0), bend=0.5)
s.curly(br2.bond(0, 1), br2.atom(1), bend=0.8)
s.text((1.9, -0.9), "enol")
s.arrow((2.6, 0), (4.0, 0), above="fast", below=r"$-$Br$^-$")
s.molecule("BrCC(C)=[OH+]", at=(5.6, 0))
s.arrow((7.2, 0), (8.6, 0), above=r"$-$H$^+$")
s.molecule("BrCC(C)=O", at=(10.2, 0))
s.text((10.2, -1.6), "bromoacetone")
s.draw()
