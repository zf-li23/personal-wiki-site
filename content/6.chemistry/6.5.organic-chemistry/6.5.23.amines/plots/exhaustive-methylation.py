"""Ring opening of piperidine by exhaustive methylation and Hofmann elimination. Piperidine is
methylated twice to the N,N-dimethylpiperidinium ion and converted to the hydroxide (Ag2O). On
heating, hydroxide removes a beta hydrogen on C3 (anti-periplanar to the C-N bond), the C-H
electrons form the C=C bond and the ring C-N bond breaks: the ring opens to
N,N-dimethylpent-4-en-1-amine. A second methylation-elimination releases trimethylamine and
penta-1,4-diene."""

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
q = s.molecule("C[N+]1(C)CCCCC1", at=(0, 0), show_h=[4])
oh = s.molecule("[OH-]", at=(q.xy(4)[0] + 1.6, q.xy(4)[1] + 0.6), lone_pairs=True)
h = nearest_h(q, 4, oh.xy(0))
s.curly(oh.atom(0), h, bend=0.4)
s.curly((q.xy(4) + h.xy) / 2, q.bond(3, 4), bend=0.6)
s.curly(q.bond(1, 3), q.atom(1), bend=0.6)
s.text((0, -2.2), "N,N-dimethylpiperidinium")
s.arrow((3.0, 0), (4.4, 0), above="heat", below=r"$-$H$_2$O")
s.molecule("CN(C)CCCC=C", at=(7.0, 0))
s.arrow((9.6, 0), (11.4, 0), above=r"CH$_3$I; Ag$_2$O", below=r"heat, $-$Me$_3$N")
s.molecule("C=CCC=C", at=(13.0, 0))
s.draw()
