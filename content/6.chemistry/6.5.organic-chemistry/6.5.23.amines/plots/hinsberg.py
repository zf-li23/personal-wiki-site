"""The Hinsberg test with a primary amine. Top: the amine nitrogen attacks the sulfur of
benzenesulfonyl chloride and chloride leaves (substitution at sulfur); loss of a proton gives
N-butylbenzenesulfonamide. Bottom: the remaining N-H is acidic (pKa about 10) because the sulfonyl
group withdraws electrons, so hydroxide removes it and the sulfonamide dissolves in aqueous NaOH as
its sodium salt. A secondary amine gives a sulfonamide without N-H, which stays insoluble."""

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
am = s.molecule("CCCCN", at=(-3.2, y), lone_pairs=[4])
sc = s.molecule("O=S(=O)(Cl)c1ccccc1", at=(0.6, y), lone_pairs=[3])
s.curly(am.atom(4), sc.atom(1), bend=-0.4)
s.curly(sc.bond(1, 3), sc.atom(3), bend=0.6)
s.arrow((2.6, y), (4.0, y), below=r"$-$HCl")
s.molecule("CCCCNS(=O)(=O)c1ccccc1", at=(7.8, y))

y = -4.4
sa = s.molecule("CCCCNS(=O)(=O)c1ccccc1", at=(0, y), show_h=[4])
oh = s.molecule("[OH-]", at=(sa.xy(4)[0] - 0.4, sa.xy(4)[1] - 2.0), lone_pairs=True)
h = nearest_h(sa, 4, oh.xy(0))
s.curly(oh.atom(0), h, bend=-0.4)
s.curly((sa.xy(4) + h.xy) / 2, sa.atom(4), bend=-0.6)
s.arrow((3.0, y), (4.4, y), below=r"$-$H$_2$O")
s.molecule("CCCC[N-]S(=O)(=O)c1ccccc1", at=(8.2, y))
s.text((8.2, y - 1.9), "water-soluble anion")
s.draw()
