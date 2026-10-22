"""Lewis structures with lone pairs and formal charges: H2O, NH3, NH4+, N2, CO2, CO, O3 and nitrate (one resonance form each)."""

from wikichem import Scheme

s = Scheme(scale=0.5)
# Top row: hydrogen compounds, hydrogens drawn as atoms.
s.molecule("O", at=(0, 4.2), lone_pairs=True, explicit_h=True)
s.text((0, 2.5), r"$\mathrm{H_2O}$")
s.molecule("N", at=(4.2, 4.2), lone_pairs=True, explicit_h=True)
s.text((4.2, 2.5), r"$\mathrm{NH_3}$")
s.molecule("[NH4+]", at=(8.4, 4.2), explicit_h=True)
s.text((8.4, 2.5), r"$\mathrm{NH_4^+}$")
s.molecule("C", at=(12.6, 4.2), explicit_h=True)
s.text((12.6, 2.5), r"$\mathrm{CH_4}$")
# Bottom row: multiple bonds and formal charges.
s.molecule("N#N", at=(0, 0), lone_pairs=True)
s.text((0, -1.7), r"$\mathrm{N_2}$")
s.molecule("O=C=O", at=(3.6, 0), lone_pairs=True)
s.text((3.6, -1.7), r"$\mathrm{CO_2}$")
s.molecule("[C-]#[O+]", at=(7.2, 0), lone_pairs=[0, 1])
s.text((7.2, -1.7), r"$\mathrm{CO}$")
s.molecule("[O-][O+]=O", at=(10.8, 0), lone_pairs=True)
s.text((10.8, -1.7), r"$\mathrm{O_3}$")
s.molecule("[O-][N+](=O)[O-]", at=(15.0, 0.2), lone_pairs=True)
s.text((15.0, -1.7), r"$\mathrm{NO_3^-}$")
s.draw()
