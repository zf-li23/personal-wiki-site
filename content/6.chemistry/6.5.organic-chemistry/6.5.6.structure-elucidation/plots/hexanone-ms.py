"""EI fragmentation of the 2-hexanone molecular ion (m/z 100), drawn with one-electron (fishhook) arrows.
Top: alpha cleavage. The unpaired electron on oxygen pairs with one electron of the C2-C3 bond, giving
the acylium ion CH3CO+ (m/z 43, base peak) and a butyl radical; cleaving the other alpha bond instead
loses CH3 and gives C4H9CO+ (m/z 85). Bottom: McLafferty rearrangement through a six-membered
arrangement. The gamma hydrogen moves to oxygen and the alpha-beta bond breaks: propene (42) leaves
and the enol radical cation m/z 58 remains (a distonic ion: charge on O, radical on CH2)."""

import numpy as np

from wikichem import Scheme

s = Scheme()

# alpha cleavage: atoms 0 C1, 1 C2, 2 O, 3 C3, 4 C4, 5 C5, 6 C6
y = 0.0
m = s.molecule("CC(=[O+])CCCC", at=(0, y))
s.curly(m.atom(2), m.bond(1, 2), bend=-0.9, single=True)
s.curly(m.bond(1, 3), m.bond(1, 2), bend=0.8, single=True)
s.curly(m.bond(1, 3), m.xy(3) + np.array([0.35, -0.75]), bend=-0.6, single=True)
s.text((0, y - 1.8), "2-hexanone, $m/z$ 100")
s.arrow((3.3, y), (4.7, y), above=r"$\alpha$ cleavage")
s.molecule("CC#[O+]", at=(6.0, y))
s.text((6.0, y - 1.8), "$m/z$ 43")
s.plus((7.5, y))
s.molecule("[CH2]CCC", at=(9.4, y), flip=True)
s.text((9.4, y - 1.8), "butyl radical")

# McLafferty: atoms 0 O, 1 C2, 2 C1, 3 C3 (alpha), 4 C4 (beta), 5 C5 (gamma), 6 H, 7 C6
y = -5.0
r = 1.0
ang = np.radians([150, 90, 30, -30, -90, -150])
P = [np.array([r * np.cos(t), r * np.sin(t) + y]) for t in ang]  # O, C2, C3, C4, C5, H around the ring
out = lambda p: p + 1.0 * (p - np.array([0, y])) / np.linalg.norm(p - np.array([0, y]))
coords = [P[0], P[1], out(P[1]), P[2], P[3], P[4], P[5], out(P[4])]
ion = s.molecule("[O+]=C(C)CCC([H])C", coords=coords)
s.partial(ion.xy(6) + np.array([0, 0.25]), ion.xy(0) - np.array([0, 0.25]))
mid = ion.bond(0, 6).xy + np.array([-0.08, 0])
s.curly(ion.atom(0), mid, bend=0.9, single=True)
s.curly(ion.bond(5, 6), mid, bend=-0.6, single=True)
s.curly(ion.bond(5, 6), ion.bond(4, 5), bend=0.7, single=True)
s.curly(ion.bond(3, 4), ion.bond(4, 5), bend=0.7, single=True)
s.text((0, y - 2.6), "2-hexanone, $m/z$ 100")
s.arrow((2.4, y), (3.8, y), above="McLafferty")
s.molecule("[CH2]C(C)=[OH+]", at=(5.4, y + 0.2))
s.text((5.4, y - 1.8), "$m/z$ 58")
s.plus((7.0, y))
s.molecule("C=CC", at=(8.4, y))
s.text((8.4, y - 1.8), "propene (42)")
s.draw()
