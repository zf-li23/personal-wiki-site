"""Ligand substitution. Figure 1 (dissociative): the 18-electron tetrahedral Ni(CO)4 loses one CO
in the slow step, giving 16-electron Ni(CO)3, which then binds the incoming ligand L.
Figure 2 (associative): the incoming Y- attacks a 16-electron square-planar Pt(II) complex from
above the plane, giving an 18-electron five-coordinate (trigonal-bipyramidal) intermediate in
which the leaving chloride, the entering Y and the trans ligand T share the trigonal plane;
chloride then leaves and Y ends up where chloride was (retention of geometry)."""

exec(open("helpers.txt").read())

# ---- dissociative: Ni(CO)4 -> Ni(CO)3 + CO -> Ni(CO)3L
s = Scheme()
c, lab = spokes("Ni", [(150, "OC"), (210, "OC"), (270, "CO")])
c.append((1.5, 0.0))          # the leaving carbonyl carbon, drawn as C#O
c.append((2.5, 0.0))
lab[5] = "O"  # O+ in the SMILES keeps RDKit valences; the label hides the formal charge
ni = s.molecule("[Ni](*)(*)(*)C#[O+]", coords=c, at=(0, 0), labels=lab, show_carbons=[4])
s.curly(ni.bond(0, 4), ni.atom(4), bend=0.9)
s.text((0.6, -2.2), "18 e", size=12)
s.arrow((3.0, 0), (4.6, 0), above="slow", below="$-$CO")
complex_at(s, "Ni", [(90, "CO"), (210, "OC"), (330, "CO")], at=(6.3, 0))
s.text((6.3, -2.2), "16 e", size=12)
s.arrow((8.0, 0), (9.6, 0), above="+ L", below="fast")
complex_at(s, "Ni", [(150, "OC"), (210, "OC"), (270, "CO"), (0, "L")], at=(11.2, 0))
s.text((11.2, -2.2), "18 e", size=12)
s.draw()

# ---- associative: square-planar Pt(II) + Y- -> five-coordinate -> product + Cl-
s = Scheme()
c, lab = spokes("Pt", [(90, "L"), (270, "L"), (180, "T")])
c.append((1.5, 0.0))
pt = s.molecule("[Pt](*)(*)(*)Cl", coords=c, at=(0, 0), labels=lab)
y = s.molecule("[Y-]", at=(1.3, 2.0))
s.curly(y.atom(0), pt.atom(0), bend=0.4)
s.text((0, -2.1), "16 e", size=12)
s.arrow((2.8, 0), (4.4, 0), above="slow")
x = 6.6
c, lab = spokes("Pt", [(90, "L"), (270, "L"), (180, "T"), (35, "Y")])
c.append((1.5 * math.cos(math.radians(-35)), 1.5 * math.sin(math.radians(-35))))
tbp = s.molecule("[Pt](*)(*)(*)(*)Cl", coords=c, at=(x, 0), labels=lab)
s.curly(tbp.bond(0, 5), tbp.atom(5), bend=-0.7)
s.text((x, -2.1), "18 e", size=12)
s.arrow((x + 2.0, 0), (x + 3.6, 0), above="fast", below="$-$Cl$^-$")
complex_at(s, "Pt", [(90, "L"), (270, "L"), (180, "T"), (0, "Y")], at=(x + 5.4, 0))
s.text((x + 5.4, -2.1), "16 e", size=12)
s.draw()
