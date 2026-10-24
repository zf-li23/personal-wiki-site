"""SNAr of 2-chloropyridine with methoxide. Top: methoxide adds to C2 (slow); the negative charge of
the anionic intermediate is shared by N1, C3 and C5, and the structure with the charge on nitrogen is
the most important. Bottom: chloride is expelled (fast) and the aromatic ring is restored."""

from wikichem import Scheme

PY = "[Cl:7][C:2]1=[N:1][CH:6]=[CH:5][CH:4]=[CH:3]1"
N_ANION = "[Cl:7][C:2]1([O:8]C)[N-:1][CH:6]=[CH:5][CH:4]=[CH:3]1"
C3_ANION = "[Cl:7][C:2]1([O:8]C)[N:1]=[CH:6][CH:5]=[CH:4][CH-:3]1"
C5_ANION = "[Cl:7][C:2]1([O:8]C)[N:1]=[CH:6][CH-:5][CH:4]=[CH:3]1"
DX = 4.2

s = Scheme()
py = s.molecule(PY, at=(0, 0), rotate=-30)
meo = s.molecule("C[O-:9]", at=(py.xy(2)[0] - 0.6, py.xy(2)[1] + 2.0), lone_pairs=[9])
s.curly(meo.atom(9), py.atom(2), bend=0.3)
s.curly(py.bond(2, 1), py.atom(1), bend=0.9)
s.arrow((2.0, 0), (3.2, 0), above="slow")
first = s.molecule(N_ANION, at=(5.2, 0), lone_pairs=[1])
for i, smi in enumerate([C3_ANION, C5_ANION], start=1):
    x = 5.2 + DX * (i - 0.5)
    s.arrow((x - 0.35, 0), (x + 0.35, 0), kind="resonance")
    s.molecule(smi, at=(5.2 + DX * i, 0), like=first)
s.draw()

s = Scheme()
m = s.molecule(N_ANION, at=(0, 0), lone_pairs=[1])
s.curly(m.atom(1), m.bond(1, 2), bend=0.8)
s.curly(m.bond(2, 7), m.atom(7), bend=0.6)
s.arrow((2.2, 0), (3.4, 0), above="fast")
s.molecule("COc1ccccn1", at=(5.2, 0))
s.plus((7.0, 0))
s.molecule("[Cl-]", at=(7.8, 0))
s.draw()
