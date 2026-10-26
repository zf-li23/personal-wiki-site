"""First half of transamination by a PLP enzyme (aspartate aminotransferase type).
Top: the external aldimine (Schiff base of the substrate amino acid with PLP, formed by transimination from
the internal aldimine with the active-site Lys) loses the alpha-hydrogen to the Lys acting as a base; the
electron pair flows through the conjugated system into the protonated pyridine ring (electron sink), giving
the quinonoid intermediate. Reprotonation at C-4' gives the ketimine. Bottom: hydrolysis of the ketimine
releases the alpha-keto acid and pyridoxamine phosphate (PMP); the reverse sequence with alpha-ketoglutarate
gives glutamate and regenerates PLP (ping-pong). R = side chain; P = CH2OPO3(2-) at C-5."""

from wikichem import Scheme

s = Scheme()
lab = {4: "R", 15: "CH$_2$OPO$_3^{2-}$"}
y = 0.0
ald = s.molecule("[O-]C(=O)C(*)N=Cc1c(O)c(C)[nH+]cc1*", at=(0, y), labels=lab, show_h=[3], lone_pairs=[12])
s.curly(ald.bond(3, ald.mol.GetNumAtoms() - 1), ald.bond(3, 5), bend=0.6)
s.curly(ald.bond(5, 6), ald.bond(6, 7), bend=-0.6)
s.text((0, y - 3.1), "external aldimine", size=10)
ref = ald.coords[:16] - ald.coords[:16].mean(axis=0)
s.arrow((3.9, y), (5.3, y), above="Lys–NH$_2$", below="− H$^+$")
q = s.molecule("[O-]C(=O)C(*)=NC=C1C(O)=C(C)NC=C1*", at=(9.2, y), labels=lab, coords=ref)
s.text((9.2, y - 3.1), "quinonoid intermediate", size=10)
s.arrow((13.5, y), (15.1, y), above="Lys–NH$_3^+$", below="+ H$^+$, C-4′")
k = s.molecule("[O-]C(=O)C(*)=NCc1c(O)c(C)[nH+]cc1*", at=(19.3, y), labels=lab, coords=ref)
s.text((19.3, y - 3.1), "ketimine", size=10)

y = -6.4
s.molecule("[O-]C(=O)C(*)=NCc1c(O)c(C)[nH+]cc1*", at=(0, y), labels=lab, coords=ref)
s.plus((4.1, y))
s.text((5.0, y), "H$_2$O", size=12)
s.arrow((5.9, y), (7.3, y), kind="equilibrium")
s.molecule("[O-]C(=O)C(*)=O", at=(9.6, y), labels={4: "R"}, coords=ref[[0, 1, 2, 3, 4, 5]] - ref[[0, 1, 2, 3, 4, 5]].mean(axis=0))
s.text((9.6, y - 3.1), "α-keto acid", size=10)
s.plus((12.2, y))
s.molecule("NCc1c(O)c(C)[nH+]cc1*", at=(15.8, y), labels={10: "CH$_2$OPO$_3^{2-}$"}, coords=ref[5:16] - ref[5:16].mean(axis=0))
s.text((15.8, y - 3.1), "pyridoxamine phosphate (PMP)", size=10)
s.draw()
