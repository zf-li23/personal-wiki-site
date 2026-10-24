"""Tiffeneau-Demjanov ring expansion: 1-(aminomethyl)cyclohexan-1-ol and nitrous acid. Diazotization
of the primary amine gives an alkyldiazonium ion. As N2 leaves, a ring C-C bond migrates with its
electron pair to the CH2 carbon (no free primary carbocation is formed); the ring grows by one carbon
and the positive charge lands on the carbon bearing OH, where the oxygen lone pair stabilizes it.
Loss of the proton gives cycloheptanone."""

from wikichem import Scheme

s = Scheme()
y = 0.0
s.molecule("NCC1(O)CCCCC1", at=(0.0, y))
s.arrow((1.6, y), (3.2, y), above=r"NaNO$_2$", below=r"HOAc, H$_2$O")
d = s.molecule("N#[N+]CC1(O)CCCCC1", at=(6.3, y))
s.curly(d.bond(3, 5), d.atom(2), bend=-0.6)
s.curly(d.bond(1, 2), d.atom(1), bend=0.6)
s.text((6.3, y - 2.2), "alkyldiazonium ion")
s.arrow((8.5, y), (9.9, y), above=r"$-\,\mathrm{N_2}$")
c = s.molecule("O[C+]1CCCCCC1", at=(11.6, y), lone_pairs=[0])
s.curly(c.atom(0), c.bond(0, 1), bend=0.6)
s.text((11.6, y - 2.2), "ring-expanded cation")
s.arrow((13.4, y), (14.8, y), below=r"$-\,\mathrm{H^+}$")
s.molecule("O=C1CCCCCC1", at=(16.5, y))
s.text((16.5, y - 2.2), "cycloheptanone")
s.draw()
