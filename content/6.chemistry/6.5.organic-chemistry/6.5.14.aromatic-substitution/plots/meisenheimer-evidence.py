"""Meisenheimer's evidence (1902) for the addition intermediate of SNAr. 2,4,6-Trinitroanisole with
ethoxide (left) and 2,4,6-trinitrophenetole with methoxide (right) give the same red salt: the
Meisenheimer complex whose sp3 carbon carries both OCH3 and OC2H5 (drawn with the charge on the
para nitro group, the most important resonance structure)."""

exec(open("helpers.txt").read())

TNA = "C[O:7][C:1]1=[C:2]([N+](=O)[O-])[CH:3]=[C:4]([N+](=O)[O-])[CH:5]=[C:6]1[N+](=O)[O-]"
TNP = "CC[O:7][C:1]1=[C:2]([N+](=O)[O-])[CH:3]=[C:4]([N+](=O)[O-])[CH:5]=[C:6]1[N+](=O)[O-]"
MC = "COC1(OCC)C([N+](=O)[O-])=CC(=[N+]([O-])[O-])C=C1[N+](=O)[O-]"

RING = [1, 2, 3, 4, 5, 6]


def facing(smiles, k, angle):
    """Rotation that makes ring atom k point in direction ``angle`` (degrees) from the ring centre."""
    m = Scheme().molecule(smiles)  # layout only
    v = m.xy(k) - ring_centre(m, RING)
    return angle - np.degrees(np.arctan2(v[1], v[0]))


s = Scheme()
a = s.molecule(TNA, at=(0, 0), rotate=facing(TNA, 1, 0))
eto = s.molecule("CC[O-]", at=a.xy(1) + (2.2, 3.1), lone_pairs=True)
s.curly(eto.atom(2), a.atom(1), bend=0.4)
s.curly(a.bond(1, 6), a.atom(6), bend=-0.6)
s.arrow((3.4, 0), (4.8, 0), kind="equilibrium")
s.molecule(MC, at=(8.0, 0), rotate=90)
s.text((8.0, -3.6), "Meisenheimer complex (red salt)", size=11)
s.arrow((12.8, 0), (11.4, 0), kind="equilibrium")
b = s.molecule(TNP, at=(16.6, 0), rotate=facing(TNP, 1, 180))
meo = s.molecule("C[O-]", at=b.xy(1) + (-2.2, 3.1), lone_pairs=True)
s.curly(meo.atom(1), b.atom(1), bend=-0.4)
s.curly(b.bond(1, 6), b.atom(6), bend=0.6)
s.draw()
