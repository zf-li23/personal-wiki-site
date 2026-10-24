"""Hock rearrangement in the cumene process. The protonated hydroperoxide loses water while the
phenyl group migrates from carbon to the electron-poor oxygen (concerted); the resulting oxocarbenium
ion adds water, and the hemiketal falls apart into phenol and acetone."""

exec(open("helpers.txt").read())

s = Scheme()
hp = s.molecule("C[C:1](C)([O:2][OH2+:3])[c:4]1ccccc1", at=(-1.4, 0), rotate=180)
s.curly(hp.bond(1, 4), hp.atom(2), bend=-0.8)
s.curly(hp.bond(2, 3), hp.atom(3), bend=-0.7)
s.arrow((2.4, 0), (3.6, 0), above=r"$-$H$_2$O")
s.molecule("CC(C)=[O+]c1ccccc1", at=(5.8, 0))
s.arrow((8.0, 0), (9.2, 0), above=r"H$_2$O", below=r"$-$H$^+$")
s.molecule("CC(C)(O)Oc1ccccc1", at=(11.4, 0))
s.arrow((14.0, 0), (15.2, 0), above=r"H$^+$")
s.molecule("Oc1ccccc1", at=(16.8, 0))
s.plus((18.3, 0))
s.molecule("CC(C)=O", at=(19.4, 0))
s.draw()
