"""Cleavage of ethers by hydroiodic acid. Top: anisole is protonated on oxygen and iodide attacks the
methyl carbon (SN2); the aryl-O bond is not broken, so the products are phenol and iodomethane.
Bottom: protonated tert-butyl methyl ether ionizes to the tert-butyl cation and methanol (SN1); the
cation is captured by iodide (2-iodo-2-methylpropane) or, without a good nucleophile, loses a proton
(E1) to give 2-methylpropene, which is how tert-butyl ethers are removed as protecting groups."""

from wikichem import Scheme

s = Scheme()
y = 0.0
an = s.molecule("C[OH+]c1ccccc1", at=(1.6, y))
i1 = s.molecule("[I-]", at=(-0.9, y + 0.9), lone_pairs=True)
s.curly(i1.atom(0), an.atom(0), bend=-0.4)
s.curly(an.bond(0, 1), an.atom(1), bend=-0.8)
s.text((1.4, y - 1.8), "protonated anisole")
s.arrow((3.6, y), (5.0, y), above=r"S$_{\mathrm{N}}$2")
s.molecule("Oc1ccccc1", at=(6.4, y))
s.plus((8.0, y))
s.molecule("CI", at=(8.9, y))

y = -4.4
te = s.molecule("CC(C)(C)[OH+]C", at=(0, y))
s.curly(te.bond(1, 4), te.atom(4), bend=0.8)
s.arrow((1.8, y), (3.2, y), below=r"$-$CH$_3$OH")
s.molecule("C[C+](C)C", at=(4.6, y))
s.arrow((6.0, y + 0.4), (8.4, y + 1.2), above=r"I$^-$ (S$_{\mathrm{N}}$1)")
s.molecule("CC(C)(C)I", at=(10.2, y + 1.3))
s.arrow((6.0, y - 0.4), (8.4, y - 1.2), below=r"$-$H$^+$ (E1)")
s.molecule("C=C(C)C", at=(10.2, y - 1.4))
s.draw()
