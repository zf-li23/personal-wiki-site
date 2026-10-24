"""Matteson homologation of a boronic ester (the chiral diol of the real reagents, such as
pinanediol, is drawn as ethylene glycol). Top: dichloromethyllithium adds to the empty p orbital of
boron, giving a borate ate complex. Bottom: the alkyl group on boron migrates to the CHCl2 carbon
with its bonding pair while chloride leaves from the back (a 1,2-metallate shift, promoted by
ZnCl2), giving an alpha-chloroboronic ester with one carbon more; the chiral diol decides which
chlorine leaves and so the configuration of the new stereocentre."""

from wikichem import Scheme

s = Scheme()
be = s.molecule("CCCB1OCCO1", at=(0, 0))
cl = s.molecule("Cl[CH-]Cl", coords=[(2.7, -1.0), (3.2, -0.13), (4.2, -0.13)], lone_pairs=[1])
s.curly(cl.atom(1), be.atom(3), bend=0.5)
s.arrow((5.0, 0), (6.4, 0))
s.text((5.7, -0.8), "$-100\\,^\\circ$C", size=11)
y = -4.2
ate = s.molecule("CCC[B-]1(C(Cl)Cl)OCCO1",
                 coords=[(-2.87, 0.5), (-2.0, 0), (-1.0, 0), (0, 0), (0.0, 1.0), (-0.6, 1.8), (0.9, 1.5),
                         (0.0, -1.0), (0.95, -1.31), (1.54, -0.5), (0.95, 0.31)],
                 at=(0, y))
s.curly(ate.bond(2, 3), ate.bond(3, 4), bend=-1.2)
s.curly(ate.bond(4, 6), ate.atom(6), bend=-0.6)
s.arrow((3.0, y), (4.4, y), above="ZnCl$_2$")
s.molecule("CCCC(Cl)B1OCCO1", at=(7.0, y))
s.plus((9.4, y))
s.molecule("[Cl-]", at=(10.2, y))
s.draw()
