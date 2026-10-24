"""Acid- and base-catalysed enolization of acetone. Acid (top): the carbonyl oxygen is protonated
first, then water removes an alpha proton and the C-H electrons form the C=C bond. Base (bottom):
hydroxide removes the alpha proton first, giving the enolate, which is then protonated on oxygen by
water. Both routes make the same enol; their reverse steps take the enol back to the ketone."""

import numpy as np

from wikichem import Scheme


def nearest_h(mol, k, target):
    """The hydrogen drawn on atom k that lies closest to a target point."""
    best, d = None, 1e9
    for i in range(3):
        try:
            p = mol.h(k, i)
        except IndexError:
            break
        e = np.linalg.norm(p.xy - np.asarray(target, float))
        if e < d:
            best, d = p, e
    return best


s = Scheme()
# acid catalysis
y = 0.0
k = s.molecule("CC(=O)C", at=(0, y), lone_pairs=[2])
h3o = s.molecule("[H][OH2+]", coords=[(0.0, 0.0), (1.0, 0.0)], at=(2.0, y + 1.7))
s.curly(k.atom(2), h3o.atom(0), bend=-0.4)
s.curly(h3o.bond(0, 1), h3o.atom(1), bend=-0.8)
s.text((0.4, y - 1.7), "acid")
s.arrow((2.6, y), (3.8, y), kind="equilibrium")
p = s.molecule("CC(=[OH+])C", at=(5.4, y), show_h=[0])
w = s.molecule("O", at=(3.6, y - 1.8), lone_pairs=True)
h = nearest_h(p, 0, w.xy(0))
s.curly(w.atom(0), h, bend=0.4)
s.curly((p.xy(0) + h.xy) / 2, p.bond(0, 1), bend=0.7)
s.curly(p.bond(1, 2), p.atom(2), bend=0.7)
s.arrow((7.0, y), (8.2, y), kind="equilibrium", above=r"$-$H$_3$O$^+$")
s.molecule("C=C(O)C", at=(9.6, y))
s.text((9.6, y - 1.6), "enol")

# base catalysis
y = -4.6
k2 = s.molecule("CC(=O)C", at=(1.0, y), show_h=[0], lone_pairs=[2])
oh = s.molecule("[OH-]", at=(-1.2, y - 1.4), lone_pairs=True)
h = nearest_h(k2, 0, oh.xy(0))
s.curly(oh.atom(0), h, bend=-0.4)
s.curly((k2.xy(0) + h.xy) / 2, k2.bond(0, 1), bend=-0.7)
s.curly(k2.bond(1, 2), k2.atom(2), bend=-0.7)
s.text((0.4, y - 2.4), "base")
s.arrow((2.6, y), (3.8, y), kind="equilibrium", below=r"$-$H$_2$O")
e = s.molecule("C=C([O-])C", at=(5.2, y), lone_pairs=[2])
w2 = s.molecule("[H]O[H]", coords=[(0.0, 0.0), (0.82, -0.57), (1.64, 0.0)], at=(6.0, y + 1.2), lone_pairs=[1])
s.curly(e.atom(2), w2.atom(0), bend=-0.5)
s.curly(w2.bond(0, 1), w2.atom(1), bend=-0.6)
s.text((5.2, y - 1.6), "enolate")
s.arrow((8.2, y), (9.4, y), kind="equilibrium", above=r"$-$HO$^-$")
s.molecule("C=C(O)C", at=(10.8, y))
s.text((10.8, y - 1.6), "enol")
s.draw()
