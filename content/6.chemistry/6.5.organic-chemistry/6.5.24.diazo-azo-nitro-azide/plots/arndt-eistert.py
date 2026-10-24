"""Formation of an alpha-diazo ketone, the first step of the Arndt-Eistert homologation. Top: the
nucleophilic carbon of diazomethane adds to the carbonyl carbon of benzoyl chloride; the tetrahedral
intermediate collapses and expels chloride. Bottom: the acyldiazonium-methyl ion is deprotonated (by
triethylamine, or by a second equivalent of diazomethane), giving 2-diazo-1-phenylethan-1-one, which
then undergoes the Wolff rearrangement."""

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
y = 0.0
ac = s.molecule("O=C(Cl)c1ccccc1", at=(0, y), lone_pairs=[0])
dm = s.molecule("[CH2-][N+]#N", at=(ac.xy(1)[0] + 0.2, ac.xy(1)[1] + 2.0), lone_pairs=[0])
s.curly(dm.atom(0), ac.atom(1), bend=0.4)
s.curly(ac.bond(0, 1), ac.atom(0), bend=0.6)
s.arrow((2.4, y), (3.8, y))
t = s.molecule("[O-]C(Cl)(C[N+]#N)c1ccccc1", at=(6.0, y), lone_pairs=[0])
s.curly(t.atom(0), t.bond(0, 1), bend=0.6)
s.curly(t.bond(1, 2), t.atom(2), bend=0.6)
s.text((6.0, y - 2.4), "tetrahedral intermediate")

y = -5.0
s.arrow((-2.6, y), (-1.2, y), below=r"$-$Cl$^-$")
k = s.molecule("O=C(C[N+]#N)c1ccccc1", at=(1.2, y), show_h=[2])
b = s.molecule("CCN(CC)CC", at=(k.xy(2)[0] + 0.6, k.xy(2)[1] - 2.8), lone_pairs=[2])
h = nearest_h(k, 2, b.xy(2))
s.curly(b.atom(2), h, bend=-0.4)
s.curly((k.xy(2) + h.xy) / 2, k.bond(2, 3), bend=-0.6)
s.curly(k.bond(3, 4), k.atom(4), bend=-0.6)
s.arrow((3.8, y), (5.2, y), below=r"$-$Et$_3$NH$^+$")
s.molecule("O=C(C=[N+]=[N-])c1ccccc1", at=(7.4, y))
s.text((7.4, y - 2.2), r"$\alpha$-diazo ketone")
s.draw()
