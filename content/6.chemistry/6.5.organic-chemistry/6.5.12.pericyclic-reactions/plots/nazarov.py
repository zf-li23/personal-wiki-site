"""Nazarov cyclization. A Lewis or Bronsted acid activates a divinyl ketone; the resulting
3-hydroxypentadienyl cation (4 pi electrons over five carbons) closes by a thermal conrotatory
4-electron electrocyclization to an oxyallyl cation; loss of a proton and tautomerization of the
enol give a cyclopent-2-enone."""

exec(open("fixedmol.txt").read())

p = ring(5, start=90)  # p[0] top, then counter-clockwise: upper left, lower left, lower right, upper right
s = Scheme()
s.molecule("C=CC(=O)C=C", at=(-0.4, 0.2), lone_pairs=[3])
s.arrow((1.3, 0.2), (2.5, 0.2), above=r"H$^+$")
# 3-hydroxypentadienyl cation drawn on an open pentagon: C1 lower left, C2 upper left, C3 top (OH), C4 upper right, C5 lower right
cat = fixed(s, "CC=C(O)C=C", [p[2], p[1], p[0], (0.0, 1.85), p[4], p[3]], at=(4.0, 0))
s.text(cat.xy(0) + (-0.38, 0.05), "+")
s.partial(cat.xy(0), cat.xy(5))
s.curly(cat.bond(4, 5), (cat.xy(0) + cat.xy(5)) / 2 + (0, -0.15), bend=-0.6)
s.text((4.0, -1.5), "pentadienyl cation")
s.arrow((5.4, 0.2), (6.8, 0.2), above="conrotatory", below=r"4$\pi$")
oxy = fixed(s, "C1C=C(O)CC1", [p[2], p[1], p[0], (0.0, 1.85), p[4], p[3]], at=(8.3, 0))
s.text(oxy.xy(4) + (0.42, 0.1), "+")
s.text((8.3, -1.5), "oxyallyl cation")
s.arrow((9.7, 0.2), (11.1, 0.2), above=r"$-$H$^+$", below="tautomerize")
s.molecule("O=C1C=CCC1", at=(12.6, 0.2))
s.text((12.6, -1.5), "cyclopentenone")
s.draw()
