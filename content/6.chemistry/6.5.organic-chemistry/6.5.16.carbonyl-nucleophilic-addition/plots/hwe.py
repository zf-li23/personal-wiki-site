"""Horner-Wadsworth-Emmons reaction of the anion of triethyl phosphonoacetate with benzaldehyde
(the two ethoxy groups on phosphorus and the phenyl group are written as labels). The carbanion
adds reversibly to the carbonyl carbon; the beta-oxido phosphonate closes onto phosphorus to give
the oxaphosphetane, and the ring collapses to the (E)-unsaturated ester and diethyl phosphate.
Because the addition is reversible, the diastereomer whose substituents end up trans, which closes
faster, carries most of the material through: hence the E selectivity."""

import numpy as np

from wikichem import Scheme

s = Scheme()


def labels(mol, centre, subs, text):
    """Write a group label at the ends of stand-in bonds."""
    for k in subs:
        u = mol.xy(k) - mol.xy(centre)
        u = u / np.linalg.norm(u)
        s.text(mol.xy(k) + 0.38 * u, text, size=13)


ESTER = [(1.5, -0.87), (1.0, -1.73), (2.5, -0.87), (3.0, -1.73), (4.0, -1.73)]
an = s.molecule("O=P(C)(C)[CH-]C(=O)OCC",
                coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (-0.87, -0.5), (1.0, 0)] + ESTER, lone_pairs=[4])
labels(an, 1, [2, 3], "EtO")
ald = s.molecule("O=CC", coords=[(0.0, 1.7), (1.0, 1.7), (1.5, 2.57)], lone_pairs=[0])
labels(ald, 1, [2], "Ph")
s.curly(an.atom(4), ald.atom(1), bend=0.5)
s.curly(ald.bond(0, 1), ald.atom(0), bend=0.8)
s.arrow((4.4, 0.4), (5.8, 0.4), kind="equilibrium")

x = 8.0
ad = s.molecule("O=P(C)(C)C(C(=O)OCC)C([O-])C",
                coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (-0.87, -0.5), (1.0, 0)] + ESTER
                + [(1.0, 1.1), (0.15, 1.45), (1.6, 1.95)], at=(x, 0), lone_pairs=[11])
labels(ad, 1, [2, 3], "EtO")
labels(ad, 10, [12], "Ph")
s.curly(ad.atom(11), ad.atom(1), bend=0.5)
s.curly(ad.bond(0, 1), ad.atom(0), bend=-0.8)

y = -5.0
ox = s.molecule("[O-]P1(C)(C)C(C(=O)OCC)C(C)O1",
                coords=[(0, -1.0), (0, 0), (-0.87, 0.5), (-0.87, -0.5), (1.0, 0)] + ESTER
                + [(1.0, 1.0), (1.6, 1.8), (0.0, 1.0)], at=(0, y))
labels(ox, 1, [2, 3], "EtO")
labels(ox, 10, [11], "Ph")
s.curly(ox.bond(1, 4), ox.bond(4, 10), bend=-0.6)
s.curly(ox.bond(10, 12), ox.bond(1, 12), bend=-0.6)
s.text((0.5, y - 2.6), "oxaphosphetane", size=13)
s.arrow((4.4, y + 0.3), (5.8, y + 0.3))
s.molecule("CCOC(=O)/C=C/c1ccccc1", at=(10.6, y + 0.3))
s.plus((14.9, y + 0.3))
s.molecule("[O-]P(=O)(OCC)OCC", at=(18.4, y + 0.3))
s.draw()
