"""SNAr by addition-elimination: methoxide and 1-fluoro-4-nitrobenzene. (1) Methoxide adds to the
carbon bearing fluorine (slow, rate-determining); the negative charge of the Meisenheimer complex is
delocalized onto C2, C4 and C6 and, through the para nitro group, onto oxygen (nitronate structure).
(2) Fluoride is expelled (fast) and the aromatic ring is restored."""

exec(open("helpers.txt").read())

RING = [1, 2, 3, 4, 5, 6]
MINUS = "−"
ARENE = "[C:1]1([F:7])[CH:2]=[CH:3][C:4]([N+](=O)[O-])=[CH:5][CH:6]=1"
M2 = "[C:1]1([F:7])(OC)[CH2:2][CH:3]=[C:4]([N+](=O)[O-])[CH:5]=[CH:6]1"
M4 = "[C:1]1([F:7])(OC)[CH:2]=[CH:3][CH:4]([N+](=O)[O-])[CH:5]=[CH:6]1"
MN = "[C:1]1([F:7])(OC)[CH:2]=[CH:3][C:4](=[N+]([O-])[O-])[CH:5]=[CH:6]1"
M6 = "[C:1]1([F:7])(OC)[CH:2]=[CH:3][C:4]([N+](=O)[O-])=[CH:5][CH2:6]1"

s = Scheme()
ar = s.molecule(ARENE, at=(0, 0), rotate=-90)
meo = s.molecule("C[O-]", at=ar.xy(1) + (1.6, 0.9), lone_pairs=True)
s.curly(meo.atom(1), ar.atom(1), bend=0.4)
s.curly(ar.bond(1, 6), ar.atom(6), bend=0.6)
s.arrow((2.2, 0), (3.4, 0), above="slow")
dx = 4.4
m2 = s.molecule(M2, at=(5.6, 0), rotate=90)
charge(s, m2, 2, RING, MINUS)
mols = [m2]
for i, smi in enumerate([M4, MN, M6], start=1):
    s.arrow((5.6 + dx * (i - 0.5) - 0.35, 0), (5.6 + dx * (i - 0.5) + 0.35, 0), kind="resonance")
    mols.append(s.molecule(smi, at=(5.6 + dx * i, 0), like=m2))
charge(s, mols[1], 4, RING, MINUS)
charge(s, mols[3], 6, RING, MINUS)
s.text((5.6 + 1.5 * dx, -3.3), "Meisenheimer complex", size=11)
s.draw()

s = Scheme()
m = s.molecule(M2, at=(0, 0), rotate=90)
v = ring_centre(m, RING) - m.xy(2)
minus = m.xy(2) + 0.42 * v / np.linalg.norm(v)
s.text(minus, MINUS)
s.curly(minus + (0.1, -0.15), m.bond(1, 2), bend=-1.4)
s.curly(m.bond(1, 7), m.atom(7), bend=0.6)
s.arrow((2.4, 0), (3.6, 0), above="fast")
s.molecule("COc1ccc(cc1)[N+](=O)[O-]", at=(5.6, 0), rotate=90)
s.plus((7.6, 0))
s.molecule("[F-]", at=(8.4, 0))
s.draw()
