"""Benzylic radical bromination. Figure 1: the benzyl radical is delocalized: the single electron is
shared by the benzylic carbon and the ortho and para carbons (four resonance structures), which is why
the benzylic C-H bond is weak. Figure 2: the two propagation steps of the chain (fishhook arrows):
a bromine atom abstracts a benzylic hydrogen, and the benzyl radical abstracts a bromine atom from Br2
(kept at a low concentration by NBS), regenerating Br."""

exec(open("helpers.txt").read())

FORMS = ["[CH2:7][C:1]1=[CH:2][CH:3]=[CH:4][CH:5]=[CH:6]1",
         "[CH2:7]=[C:1]1[CH:2]=[CH:3][CH:4]=[CH:5][CH:6]1",
         "[CH2:7]=[C:1]1[CH:2]=[CH:3][CH:4][CH:5]=[CH:6]1",
         "[CH2:7]=[C:1]1[CH:2][CH:3]=[CH:4][CH:5]=[CH:6]1"]

s = Scheme()
first = s.molecule(FORMS[0], at=(0, 0), rotate=90)
for i, smi in enumerate(FORMS[1:], start=1):
    s.arrow((4.0 * i - 2.3, 0), (4.0 * i - 1.7, 0), kind="resonance")
    s.molecule(smi, at=(4.0 * i, 0), like=first)
s.text((6.0, -2.0), "benzyl radical: the odd electron on CH2, ortho and para carbons", size=10)
s.draw()

def facing(smiles, k, angle, **kw):
    """Rotation that points atom k of the molecule in direction ``angle`` from its centre."""
    m = Scheme().molecule(smiles, **kw)  # layout only
    v = m.xy(k) - np.mean(m.coords, axis=0)
    return angle - np.degrees(np.arctan2(v[1], v[0]))


s = Scheme()
t = s.molecule("[CH3:7]c1ccccc1", at=(0, 0), show_h=[7], rotate=facing("[CH3:7]c1ccccc1", 7, 0, show_h=[7]))
h = min((t.h(7, i) for i in range(3)), key=lambda p: -p.xy[0])
br = s.molecule("[Br]", at=h.xy + (1.6, 0))
mid = (h.xy + br.xy(0)) / 2
s.curly(br.atom(0), mid + (0, 0.05), bend=0.6, single=True)
s.curly(bond_to(t, 7, h), mid - (0, 0.05), bend=-0.6, single=True)
s.curly(bond_to(t, 7, h), t.atom(7), bend=0.8, single=True)
s.arrow((4.6, 0), (5.8, 0))
b = s.molecule("[CH2:7]c1ccccc1", at=(7.6, 0), rotate=facing("[CH2:7]c1ccccc1", 7, 0))
s.plus((9.6, 0))
s.text((10.4, 0), "HBr")

y = -4.2
b = s.molecule("[CH2:7]c1ccccc1", at=(0, y), rotate=facing("[CH2:7]c1ccccc1", 7, 0))
br2 = s.molecule("BrBr", at=b.xy(7) + (2.1, 0))
m = (b.xy(7) + br2.xy(0)) / 2
s.curly(b.atom(7), m + (0, 0.05), bend=0.6, single=True)
s.curly(br2.bond(0, 1), m - (0, 0.05), bend=-0.7, single=True)
s.curly(br2.bond(0, 1), br2.atom(1), bend=0.8, single=True)
s.arrow((5.0, y), (6.2, y))
s.molecule("Br[CH2:7]c1ccccc1", at=(8.2, y), rotate=facing("Br[CH2:7]c1ccccc1", 7, 0))
s.plus((10.8, y))
s.molecule("[Br]", at=(11.5, y))
s.draw()
