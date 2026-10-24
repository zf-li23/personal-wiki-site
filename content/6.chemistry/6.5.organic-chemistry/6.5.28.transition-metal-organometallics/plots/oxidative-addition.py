"""Oxidative addition to Vaska's complex trans-IrCl(CO)(PPh3)2 (16 e, Ir(I), d8).
Figure 1, concerted: H2 approaches the metal side-on; the H-H sigma electrons bond to iridium
while an iridium d pair goes into the H-H sigma* orbital, so both Ir-H bonds form at once and the
product is the cis dihydride (18 e, Ir(III)); the two hydrides are trans to Cl and to CO.
Figure 2, SN2-type: an iridium d pair attacks the methyl carbon of CH3I from the back, iodide
leaves (inversion at carbon if the carbon were stereogenic), and the iodide then binds in the
site trans to methyl. The octahedral products are drawn with one axis in perspective."""

exec(open("helpers.txt").read())

# ---- concerted addition of H2
s = Scheme()
c, lab = spokes("Ir", [(90, "PPh$_3$"), (270, "PPh$_3$"), (180, "Cl"), (0, "CO")])
ir = s.molecule("[Ir](*)(*)(*)*", coords=c, at=(0, 0), labels=lab)
hh = s.molecule("[H][H]", coords=[(1.3, 1.45), (2.15, 0.95)], at=(0, 0))
s.curly(hh.bond(0, 1), between(ir.atom(0), hh.atom(0), 0.5), bend=-0.5)
s.curly(ir.atom(0), hh.atom(1), bend=0.25)
s.text((0, -2.3), "16 e, Ir(I)", size=12)
s.arrow((3.0, 0), (4.6, 0))
x = 7.2
complex_at(s, "Ir", [(90, "PPh$_3$"), (270, "PPh$_3$"), (180, "Cl"), (0, "H"), (210, "OC", 0.2), (30, "H", 0.2)], at=(x, 0))
s.text((x, -2.3), "18 e, Ir(III)", size=12)
s.draw()

# ---- SN2-type addition of CH3I
s = Scheme()
ir = s.molecule("[Ir](*)(*)(*)*", coords=c, at=(0, 0), labels=lab)
mei = s.molecule("CI", coords=[(2.6, 0.0), (3.7, 0.0)], at=(0, 1.3), show_carbons=[0], lone_pairs=[1])
s.curly(ir.atom(0), mei.atom(0), bend=-0.5)
s.curly(mei.bond(0, 1), mei.atom(1), bend=-0.6)
s.arrow((4.6, 0), (6.0, 0))
x = 8.4
c2, lab2 = spokes("Ir", [(90, "PPh$_3$"), (270, "PPh$_3$"), (180, "Cl"), (0, "CO"), (30, "CH$_3$", 0.25)])
s.molecule("[Ir+](*)(*)(*)(*)*", coords=c2, at=(x, 0), labels=lab2)
s.text((x - 0.5, -2.3), "16 e, Ir(III)", size=12)
s.plus((x + 2.2, -0.9))
s.molecule("[I-]", at=(x + 2.9, -0.9))
s.arrow((x + 3.9, 0), (x + 5.3, 0))
x2 = x + 7.6
complex_at(s, "Ir", [(90, "PPh$_3$"), (270, "PPh$_3$"), (180, "Cl"), (0, "CO"), (30, "CH$_3$", 0.25), (210, "I", 0.2)], at=(x2, 0))
s.text((x2, -2.3), "18 e, Ir(III)", size=12)
s.draw()
