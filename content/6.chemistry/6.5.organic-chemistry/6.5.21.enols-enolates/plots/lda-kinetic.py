"""Kinetic deprotonation of 2-methylcyclohexanone by LDA at -78 C. Lithium coordinates to the
carbonyl oxygen; the amide nitrogen removes a proton from the less hindered C6, the C-H electrons
form the C=C bond and the C=O electrons move onto oxygen. The bulky base and the two accessible
hydrogens on C6 make this the faster pathway, giving the less substituted lithium enolate
(about 99 : 1); the step is irreversible because diisopropylamine (pKa 36) is far weaker an acid
than the ketone."""

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
# atoms: 0 CH3, 1 C2, 2 C3, 3 C4, 4 C5, 5 C6, 6 C1, 7 O
k = s.molecule("CC1CCCCC1=O", at=(0, 0), show_h=[5], lone_pairs=[7])
h = nearest_h(k, 5, (0.4, 2.6))
li = k.xy(7) + np.array([0.2, 1.4])
n = li + np.array([1.4, 0.6])
lda = s.molecule("[Li]N(*)*", coords=[tuple(li), tuple(n), tuple(n + [-0.5, 0.9]), tuple(n + [1.0, 0.5])],
                 labels={2: "$i$Pr", 3: "$i$Pr"}, lone_pairs=[1])
s.partial(k.atom(7), lda.atom(0))
s.curly(lda.atom(1), h, bend=-0.5)
s.curly((k.xy(5) + h.xy) / 2, k.bond(5, 6), bend=-0.6)
s.curly(k.bond(6, 7), k.atom(7), bend=0.7)
s.text((0, -2.0), "H removed from the less hindered C6")
s.arrow((2.4, 0.5), (4.4, 0.5), below="THF, $-$78 $^\\circ$C")
s.molecule("CC1CCCC=C1O[Li]", at=(7.2, 0.3))
s.text((7.2, -2.0), "kinetic enolate")
s.plus((9.2, 0.3))
s.molecule("CC(C)NC(C)C", at=(10.9, 0.3))
s.draw()
