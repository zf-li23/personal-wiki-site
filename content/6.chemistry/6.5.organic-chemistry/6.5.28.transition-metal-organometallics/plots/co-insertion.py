"""Migratory insertion of CO in CH3Mn(CO)5 (18 e). The methyl group migrates, with the electron
pair of the Mn-C bond, onto the carbon of the cis carbonyl; the acyl ligand occupies the old CO
site and a vacant site is left where the methyl was (16 e). An incoming ligand L then fills it.
The octahedra are drawn with one axis in perspective."""

exec(open("helpers.txt").read())

OTHERS = [(180, "OC"), (270, "CO"), (150, "OC", 0.2), (330, "CO", 0.2)]

s = Scheme()
c, lab = spokes("Mn", OTHERS)
c += [(1.3, 0.0), (0.0, 1.35), (0.0, 2.35)]
lab[7] = "O"  # O+ keeps RDKit valences for M-C#O; the label hides the charge
mn = s.molecule("[Mn](*)(*)(*)(*)(C)C#[O+]", coords=c, at=(0, 0), labels=lab, show_carbons=[5, 6])
s.curly(mn.bond(0, 5), mn.atom(6), bend=0.6)
s.text((0, -2.2), "18 e", size=12)
s.arrow((2.4, 0), (4.0, 0))
x = 6.0
c2, lab2 = spokes("Mn", OTHERS)
c2 += [(0.0, 1.3), (-0.95, 1.9), (0.95, 1.9)]
s.molecule("[Mn](*)(*)(*)(*)C(=O)C", coords=c2, at=(x, 0), labels=lab2, show_carbons=[7])
s.text((x + 1.25, 0), "vacant", size=10)
s.text((x, -2.2), "16 e", size=12)
s.arrow((x + 2.4, 0), (x + 4.0, 0), above="+ L")
x2 = x + 6.2
c3, lab3 = spokes("Mn", OTHERS + [(0, "L")])
c3 += [(0.0, 1.3), (-0.95, 1.9), (0.95, 1.9)]
s.molecule("[Mn](*)(*)(*)(*)(*)C(=O)C", coords=c3, at=(x2, 0), labels=lab3, show_carbons=[8])
s.text((x2, -2.2), "18 e", size=12)
s.draw()
