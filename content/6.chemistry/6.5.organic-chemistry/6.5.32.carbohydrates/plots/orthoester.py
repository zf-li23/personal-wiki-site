"""The orthoester side reaction of neighbouring-group participation in glycosylation (same model as
the acyloxonium figure: a pyranose ring with an acetoxy group on C2). The acceptor alcohol can
attack the central carbon of the bicyclic acyloxonium ion instead of C1; after loss of the proton
this gives a 1,2-orthoester. Under acid catalysis the orthoester reionizes to the acyloxonium ion,
which is then opened at C1 to give the desired 1,2-trans glycoside."""

from wikichem import Scheme

s = Scheme()
y = 0.0
ion = s.molecule("CC1=[O+][C@H]2OCCC[C@H]2O1", at=(0.0, y))
me = s.molecule("CO", at=(-1.2, y + 2.4), lone_pairs=True)
s.curly(me.atom(1), ion.atom(1), bend=0.4)
s.curly(ion.bond(1, 2), ion.atom(2), bend=0.6)
s.text((0.0, y - 2.2), "acyloxonium ion")
s.arrow((2.4, y), (3.8, y), above=r"$-$H$^+$")
s.molecule("COC1(C)O[C@H]2OCCC[C@H]2O1", at=(6.4, y))
s.text((6.4, y - 2.2), "1,2-orthoester")
s.arrow((8.8, y), (10.6, y), above=r"H$^+$ (cat.)", below="via the ion")
s.molecule("CO[C@@H]1OCCC[C@H]1OC(C)=O", at=(13.4, y))
s.text((13.4, y - 2.2), "1,2-trans glycoside")
s.draw()
