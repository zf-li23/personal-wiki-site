"""Second step of the thionyl chloride reaction, two stereochemical outcomes. Top (SNi, no base): the
C-O bond ionizes to a tight ion pair of the carbocation and the chlorosulfite anion; the anion
falls apart into SO2 and chloride on the same face, so chlorine takes the place of oxygen and the
configuration is retained. Bottom (with pyridine): free chloride attacks the chlorosulfite from the
back side (SN2) and the configuration is inverted."""

from wikichem import Scheme

R = r"C$_6$H$_{13}$"
s = Scheme()
EST = [(-0.87, -0.5), (0, 0), (0, 1), (0, 2), (-0.87, 2.5), (0.87, 2.5), (0.87, -0.5)]  # Me, C, O, S, O, Cl, R
y = 0.0
est = s.molecule("C[C@@H](OS(=O)Cl)*", coords=EST, at=(0, y), labels={6: R}, lone_pairs=[2])
s.curly(est.bond(1, 2), est.atom(2), bend=-0.8)
s.text((0, y - 1.4), "chlorosulfite")
s.arrow((2.0, y + 0.8), (3.4, y + 0.8))
cat = s.molecule("C[CH+]*", coords=[(-0.87, -0.5), (0, 0), (0.87, -0.5)], at=(5.2, y), labels={2: R})
an = s.molecule("[O-]S(=O)Cl", coords=[(-0.6, 1.5), (0.2, 2.1), (0.0, 3.1), (1.05, 1.45)], at=(5.2, y), lone_pairs=[0])
s.curly(an.atom(0), an.bond(0, 1), bend=-0.9)
s.curly(an.bond(1, 3), cat.atom(1), bend=-0.6)
s.text((5.2, y - 1.4), "tight ion pair")
s.arrow((7.2, y + 0.8), (8.6, y + 0.8), below=r"$-$SO$_2$")
s.molecule("C[C@@H](Cl)*", coords=[(-0.87, -0.5), (0, 0), (0, 1), (0.87, -0.5)], at=(10.2, y), labels={3: R})
s.text((10.2, y - 1.4), "retention")

y = -5.2
est2 = s.molecule("C[C@@H](OS(=O)Cl)*", coords=EST, at=(1.2, y), labels={6: R})
cl = s.molecule("[Cl-]", at=(1.2, y - 1.9), lone_pairs=True)
s.curly(cl.atom(0), est2.atom(1), bend=0.4)
s.curly(est2.bond(1, 2), est2.atom(2), bend=-0.8)
s.text((-0.9, y - 2.0), r"(pyH$^+$Cl$^-$)", size=10)
s.arrow((3.2, y + 0.8), (4.6, y + 0.8), above=r"S$_{\mathrm{N}}$2")
s.molecule("C[C@H](Cl)*", coords=[(-0.87, 0.5), (0, 0), (0, -1), (0.87, 0.5)], at=(6.4, y + 0.8), labels={3: R})
s.text((6.4, y - 1.4), "inversion")
s.text((9.4, y + 0.8), r"+  SO$_2$  +  Cl$^-$")
s.draw()
