"""Base-catalysed racemization of (S)-3-phenylbutan-2-one. Hydroxide removes the alpha proton on the
stereocentre; the C-H electrons become the C=C bond and the C=O electrons move onto oxygen, giving a
planar, achiral enolate. Water protonates the alpha carbon from either face with equal probability,
so the (S) and (R) ketones are formed in equal amounts and the optical activity decays."""

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
k = s.molecule("CC(=O)[C@@H](C)c1ccccc1", at=(0, 0), show_h=[3], lone_pairs=[2])
oh = s.molecule("[OH-]", at=(k.xy(3)[0] + 1.6, k.xy(3)[1] - 2.0), lone_pairs=True)
h = nearest_h(k, 3, oh.xy(0))
s.curly(oh.atom(0), h, bend=0.4)
s.curly((k.xy(3) + h.xy) / 2, k.bond(1, 3), bend=-0.6)
s.curly(k.bond(1, 2), k.atom(2), bend=-0.7)
s.text((0, -2.6), "(S)")
s.arrow((2.4, 0), (3.8, 0), kind="equilibrium", above=r"$-$H$_2$O", below=r"+H$_2$O")
s.molecule("CC([O-])=C(C)c1ccccc1", at=(6.2, 0))
s.text((6.2, -2.6), "planar enolate (achiral)")
s.arrow((8.6, 0), (10.0, 0), kind="equilibrium", above=r"+H$_2$O", below=r"$-$HO$^-$")
s.molecule("CC(=O)[C@H](C)c1ccccc1", at=(12.4, 0))
s.text((12.4, -2.6), "(R)")
s.text((6.2, 3.3), "protonation from either face: 1 : 1")
s.draw()
