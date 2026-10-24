"""EI fragmentation of phenyl propanoate (m/z 150), the unknown of the worked example. Top: the
characteristic loss of a ketene from aryl esters. Through a four-membered arrangement (dashed contact)
a hydrogen on the alpha carbon moves to the ester oxygen while the acyl C-O bond breaks: methylketene (56) leaves and the phenol radical cation
m/z 94 (base peak) remains. Bottom: alpha cleavage of the acyl C-O bond gives the propanoyl cation
m/z 57 and a phenoxy radical."""

import numpy as np

from wikichem import Scheme

s = Scheme(scale=0.48)


def ring(p, d):
    """Hexagon coordinates for c1ccc(...)cc1 with atom 3 at p, the ring centre one bond further along d."""
    d = np.asarray(d, float) / np.linalg.norm(d)
    c = np.asarray(p, float) + d
    a0 = np.degrees(np.arctan2(-d[1], -d[0]))
    order = [3, 4, 5, 0, 1, 2]  # going round from atom 3
    xy = [None] * 6
    for k, i in enumerate(order):
        t = np.radians(a0 + 60 * k)
        xy[i] = c + np.array([np.cos(t), np.sin(t)])
    return xy


h = np.sqrt(3) / 2
# atoms: 0-5 phenyl (3 bears O), 6 O(ester), 7 C(acyl), 8 O(carbonyl), 9 C(alpha), 10 H, 11 CH3
y = 0.0
O6, C7, O8, C9, H10, C11 = (0, y), (-1.3, y), (-1.8, y + h), (-1.3, y - 1.3), (0, y - 1.3), (-2.17, y - 1.8)
coords = ring((h, y + 0.5), (h, 0.5)) + [O6, C7, O8, C9, H10, C11]
e = s.molecule("c1ccc(cc1)OC(=O)C([H])C", coords=coords)
s.partial(np.array(H10) + (0, 0.28), np.array(O6) - (0, 0.28))
s.text((-2.9, y + 0.1), "[", size=34)
s.text((3.4, y + 0.1), "]", size=34)
s.text((3.8, y + 1.0), r"$+\bullet$")
s.text((0.3, y - 2.4), "phenyl propanoate, $m/z$ 150")
s.arrow((4.3, y), (5.7, y), above="H shift")
x = 6.9
s.molecule("Oc1ccccc1", coords=[(x, y)] + ring((x + 1, y), (1, 0))[3:] + ring((x + 1, y), (1, 0))[:3], )
s.text((x - 0.6, y + 0.1), "[", size=34)
s.text((x + 3.4, y + 0.1), "]", size=34)
s.text((x + 3.8, y + 1.0), r"$+\bullet$")
s.text((x + 1.6, y - 2.4), "$m/z$ 94")
s.plus((x + 4.6, y))
x2 = x + 5.6
s.molecule("CC=C=O", coords=[(x2, y - 0.5), (x2 + h, y), (x2 + h + 1, y), (x2 + h + 2, y)], show_carbons=[2])
s.text((x2 + 1.3, y - 2.4), "methylketene (56)")

# alpha cleavage, from the ion with the charge and the unpaired electron on the carbonyl oxygen
y = -4.6
coords = ring((h, y + 0.5), (h, 0.5)) + [(0, y), (-1, y), (-1.5, y + h), (-1.5, y - h), (-2.5, y - h)]
a = s.molecule("c1ccc(cc1)OC(=[O+])CC", coords=coords)
s.curly(a.atom(8), a.bond(7, 8), bend=0.9, single=True)
s.curly(a.bond(6, 7), a.bond(7, 8), bend=-0.8, single=True)
s.curly(a.bond(6, 7), a.atom(6), bend=-0.8, single=True)
s.arrow((3.3, y), (4.7, y), above=r"$\alpha$ cleavage")
s.molecule("CCC#[O+]", coords=[(5.6, y - 0.5), (5.6 + h, y), (5.6 + 2 * h, y - 0.5), (5.6 + 3 * h, y - 1.0)], show_carbons=[2])
s.text((6.9, y - 2.0), "$m/z$ 57")
s.plus((9.0, y))
x = 9.8
s.molecule("[O]c1ccccc1", coords=[(x + 3, y)] + ring((x + 2, y), (-1, 0))[3:] + ring((x + 2, y), (-1, 0))[:3])
s.text((x + 1.5, y - 2.0), "phenoxy radical")
s.draw()
