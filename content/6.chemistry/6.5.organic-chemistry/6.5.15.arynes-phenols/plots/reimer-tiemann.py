"""Reimer-Tiemann reaction. Top: hydroxide deprotonates chloroform; the trichloromethyl anion loses
chloride (alpha elimination) to give singlet dichlorocarbene. Bottom: the ortho carbon of phenoxide
attacks the electron-poor carbene carbon (the oxygen lone pair pushes into the ring); proton
transfers restore the aromatic ring, and the CHCl2 group is hydrolysed in base to CHO
(salicylaldehyde after acidification)."""

exec(open("helpers.txt").read())

s = Scheme()
hcl3 = s.molecule("Cl[CH:1](Cl)Cl", at=(0, 0), show_h=[1])
h = hcl3.h(1)
oh = s.molecule("[OH-]", at=h.xy + (-1.6, 0.0), lone_pairs=True)
s.curly(oh.atom(0), h, bend=-0.5)
s.curly(bond_to(hcl3, 1, h), hcl3.atom(1), bend=-0.9)
s.arrow((2.4, 0), (3.6, 0), above=r"$-$H$_2$O")
an = s.molecule("[Cl:2][C-:1](Cl)Cl", at=(5.0, 0), lone_pairs=[1])
s.curly(an.bond(1, 2), an.atom(2), bend=0.7)
s.arrow((6.4, 0), (7.6, 0), above=r"$-$Cl$^-$")
s.molecule("Cl[C]Cl", at=(8.8, 0), singlet=[1])
s.text((8.8, -1.0), "dichlorocarbene", size=10)
s.draw()

s = Scheme()
ph = s.molecule("[O-:1][C:2]1=[CH:3][CH:4]=[CH:5][CH:6]=[CH:7]1", at=(0, 0), lone_pairs=[1], rotate=60)
out = ph.xy(3) - ring_centre(ph, [2, 3, 4, 5, 6, 7])
cb = s.molecule("Cl[C:8]Cl", at=ph.xy(3) + 2.0 * out / np.linalg.norm(out) + (0, 0.3), singlet=[8])
s.curly(ph.atom(1), ph.bond(1, 2), bend=-0.9)
s.curly(ph.bond(2, 3), cb.atom(8), bend=-0.4)
s.arrow((2.8, 0), (4.0, 0))
s.molecule("O=[C:2]1[CH:3]([C-](Cl)Cl)[CH:4]=[CH:5][CH:6]=[CH:7]1", at=(6.0, 0))
s.arrow((8.0, 0), (9.4, 0), above="H shifts")
s.molecule("[O-]c1ccccc1C(Cl)Cl", at=(11.4, 0))
s.arrow((13.4, 0), (14.8, 0), above=r"OH$^-$, H$_2$O", below=r"then H$^+$")
s.molecule("Oc1ccccc1C=O", at=(16.8, 0))
s.text((16.8, -1.9), "salicylaldehyde", size=10)
s.draw()
