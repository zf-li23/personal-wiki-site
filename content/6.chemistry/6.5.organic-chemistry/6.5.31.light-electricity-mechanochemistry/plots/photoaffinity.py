"""Photoaffinity groups. Top: an aryl azide loses N2 on irradiation (drawn with the
iminodiazonium resonance form: the terminal nitrogen lone pair completes the N-N triple bond while
the Ar-N=N bond pair stays on the aryl nitrogen), giving a singlet aryl nitrene that inserts into a
nearby N-H or C-H bond (or first ring-expands to a ketenimine). Bottom: a 3-aryl-3-(trifluoromethyl)
diazirine loses N2 at about 350 nm to give a singlet carbene, which inserts into an X-H bond of the
binding protein, attaching the probe covalently."""

from wikichem import Scheme

s = Scheme()
y = 0.0
az = s.molecule("c1ccccc1[N-][N+]#N", at=(0.0, y), lone_pairs=[6])
s.curly(az.bond(6, 7), az.atom(7), bend=0.6)
s.text((0.0, y - 2.0), "aryl azide")
s.arrow((2.6, y), (4.0, y), above=r"$h\nu$", below=r"$-$N$_2$")
s.molecule("c1ccccc1[N]", at=(5.8, y), lone_pairs=[6], singlet=[6])
s.text((5.8, y - 2.0), "aryl nitrene")
s.arrow((7.6, y), (9.0, y), above="R-H", below="insertion")
s.molecule("c1ccccc1N*", at=(11.6, y), labels={7: "R"})
y2 = -4.6
dz = s.molecule("FC(F)(F)C1(c2ccccc2)N=N1", at=(0.0, y2))
s.curly(dz.bond(4, 11), dz.bond(11, 12), bend=0.6)
s.curly(dz.bond(4, 12), dz.atom(4), bend=-0.8)
s.text((0.0, y2 - 2.3), "aryl(trifluoromethyl)diazirine")
s.arrow((2.6, y2), (4.0, y2), above=r"$h\nu$ (350 nm)", below=r"$-$N$_2$")
s.molecule("FC(F)(F)[C]c1ccccc1", at=(6.8, y2), singlet=[4])
s.text((6.8, y2 - 2.3), "singlet carbene")
s.arrow((9.0, y2), (10.4, y2), above="R-H", below="insertion")
s.molecule("FC(F)(F)C(*)c1ccccc1", at=(12.6, y2), labels={5: "R"})
s.text((12.6, y2 - 2.3), "labelled protein")
s.draw()
