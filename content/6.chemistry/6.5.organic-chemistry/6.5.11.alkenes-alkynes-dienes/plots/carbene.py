"""Dichlorocarbene from chloroform (alpha-elimination) and its stereospecific addition to an alkene.
Hydroxide removes the acidic C-H proton; the trichloromethyl anion loses chloride from the same
carbon to give singlet :CCl2 (a lone pair in an sp2-like orbital and an empty p orbital). The
carbene adds to cis-2-butene in one step, so the cis geometry is kept in the cyclopropane."""

from wikichem import Scheme


s = Scheme()
hydroxide = s.molecule("[OH-]", at=(-1.6, 0.6), lone_pairs=True)
chcl3 = s.molecule("ClC(Cl)Cl", at=(0.8, 0), lone_pairs=False)
s.text(chcl3.xy(1) + (-0.45, 0.25), "H", size=11)
s.curly(hydroxide.atom(0), chcl3.xy(1) + (-0.45, 0.25), bend=-0.3)
s.curly(chcl3.xy(1) + (-0.25, 0.12), chcl3.atom(1), bend=0.9)
s.arrow((2.2, 0), (3.5, 0), above=r"$-\mathrm{H_2O}$")
anion = s.molecule("Cl[C-](Cl)Cl", at=(4.9, 0))
s.curly(anion.bond(1, 3), anion.atom(3), bend=0.5)
s.arrow((6.3, 0), (7.6, 0), above=r"$-\mathrm{Cl}^-$")
s.molecule("Cl[C]Cl", at=(8.8, 0.2), coords=[(-0.87, -0.5), (0, 0), (0.87, -0.5)], singlet=[1])

s.text((8.8, -1.0), "singlet dichlorocarbene")
s.draw()

s = Scheme()
s.molecule("C/C=C\\C", at=(0, 0))
s.text((1.5, 0), r"+ :CCl$_2$")
s.arrow((2.5, 0), (4.0, 0), above="one step")
s.molecule("C[C@H]1C(Cl)(Cl)[C@H]1C", at=(5.8, 0))
s.text((5.8, -1.9), "cis only (stereospecific)")
s.draw()
