"""Stork enamine alkylation. In the pyrrolidine enamine of cyclohexanone the nitrogen lone pair
pushes the C=C pi electrons, and the beta carbon attacks allyl bromide (SN2), giving an iminium
ion. Hydrolysis in dilute aqueous acid returns the carbonyl group and releases pyrrolidine,
giving 2-allylcyclohexanone."""

from wikichem import Scheme

s = Scheme()
en = s.molecule("C1=C(N2CCCC2)CCCC1", at=(0, 0), lone_pairs=[2])
ab = s.molecule("C=CCBr", at=(2.6, -1.8), lone_pairs=[3])
s.curly(en.atom(2), en.bond(1, 2), bend=-0.7)
s.curly(en.bond(0, 1), ab.atom(2), bend=-0.5)
s.curly(ab.bond(2, 3), ab.atom(3), bend=-0.7)
s.text((0, -3.0), "enamine")
s.arrow((4.0, 0), (5.4, 0), below=r"$-$Br$^-$")
s.molecule("C=CCC1CCCCC1=[N+]1CCCC1", at=(7.2, 0), rotate=180)
s.text((6.0, -2.6), "iminium ion")
s.arrow((10.2, 0), (11.8, 0), above=r"H$_3$O$^+$", below=r"$-$pyrrolidine")
s.molecule("C=CCC1CCCCC1=O", at=(13.6, 0), rotate=180)
s.draw()
