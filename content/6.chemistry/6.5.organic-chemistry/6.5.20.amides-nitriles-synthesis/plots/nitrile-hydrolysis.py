"""Acid-catalysed hydrolysis of a nitrile (acetonitrile). The nitrile is protonated on nitrogen,
water adds to the electrophilic carbon, and loss of a proton gives the imidic acid, the enol-like
tautomer of the amide. Tautomerization gives acetamide, which under the same conditions is
hydrolysed further to acetic acid and ammonium."""

from wikichem import Scheme

s = Scheme()
y = -1.6  # caption line
w = s.molecule("O", at=(-1.2, 1.2), lone_pairs=True)
nit = s.molecule("CC#[NH+]", at=(0.2, 0))
s.curly(w.atom(0), nit.atom(1), bend=0.4)
s.curly(nit.bond(1, 2), nit.atom(2), bend=-0.7)
s.text((0.2, y), "protonated nitrile")
s.arrow((1.6, 0), (3.0, 0), below=r"$-\mathrm{H}^+$")
s.molecule("CC(O)=N", at=(4.3, 0))
s.text((4.3, y), "imidic acid")
s.arrow((6.4, 0), (8.0, 0), above="tautomerism")
s.molecule("CC(N)=O", at=(9.2, 0))
s.text((9.2, y), "acetamide")
s.arrow((10.5, 0), (12.1, 0), above=r"H$_3$O$^+$, heat")
s.molecule("CC(=O)O", at=(13.3, 0))
s.plus((14.4, 0))
s.molecule("[NH4+]", at=(15.3, 0))
s.draw()
