"""Dissolving-metal reduction of an internal alkyne (Na in liquid NH3). Electron transfer from Na
gives a radical anion that adopts the trans geometry (the two alkyl groups apart); NH3 protonates it
to a vinyl radical, a second electron gives a trans vinyl anion, and a second protonation gives the
(E)-alkene. Compare Lindlar hydrogenation, which delivers both H atoms to one face: (Z)-alkene."""

from wikichem import Scheme


s = Scheme(scale=0.4)
s.molecule("CC#CC", at=(0, 0))
s.arrow((1.6, 0), (2.9, 0), above=r"Na, $e^-$")
s.molecule("C/[C]=[C-]/C", at=(4.4, 0))
s.text((4.4, -1.4), "radical anion")
s.arrow((5.9, 0), (7.2, 0), above=r"NH$_3$", below=r"$-\mathrm{NH_2^-}$")
b = s.molecule("C/[C]=C/C", at=(8.7, 0), show_h=[2])
s.text((8.7, -1.4), "vinyl radical")
s.arrow((10.2, 0), (11.5, 0), above=r"Na, $e^-$")
c = s.molecule("C/[C-]=C/C", at=(13.0, 0), show_h=[2])
s.text((13.0, -1.4), "vinyl anion")
s.arrow((14.5, 0), (15.8, 0), above=r"NH$_3$")
s.molecule("C/C=C/C", at=(17.3, 0))
s.text((17.3, -1.4), "(E)-alkene")
s.draw()
