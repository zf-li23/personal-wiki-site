"""McLafferty rearrangement of the 4-octanone molecular ion (m/z 128). In a six-membered cyclic
arrangement the gamma hydrogen moves to the carbonyl oxygen and the alpha-beta bond breaks:
propene (42) leaves as a neutral molecule and the enol radical cation m/z 86 remains. The three
curved arrows show the formal electron-pair shifts (as in a retro-ene reaction); the charge and the
unpaired electron stay on the enol."""

import numpy as np
from wikichem import Scheme

s = Scheme(scale=0.5)

# Reactant ring: O, C, C(alpha), C(beta), C(gamma), H on a hexagon of side 1.4.
r = 1.4
ang = np.radians([150, 210, 270, 330, 30, 90])
P = dict(zip(["O", "C", "Ca", "Cb", "Cg", "H"], [r * np.array([np.cos(t), np.sin(t)]) for t in ang]))
right = np.array([1.9, 0.0])
coords = [
    P["O"], P["C"],
    P["C"] + (-1.21, -0.7), P["C"] + (-2.42, 0.0), P["C"] + (-3.63, -0.7),  # propyl
    P["Ca"], P["Cb"], P["Cg"], P["H"], P["Cg"] + right,
]
# O is written with its charge and unpaired electron (molecular ion); gamma carbon keeps its other H implicitly.
ion = s.molecule("[O+]=C(CCC)CCC([H])C", coords=coords, show_carbons=range(10))
s.text((0, -2.5), "4-octanone, $m/z$ 128", size=13)

# dashed H...O contact, stopping short of both labels
hp, op = ion.xy(8), ion.xy(0)
u = (op - hp) / np.linalg.norm(op - hp)
s.partial(hp + 0.3 * u, op - 0.3 * u)

# Electron-pair shifts: C=O pi -> O-H; C(gamma)-H -> C(beta)=C(gamma); C(alpha)-C(beta) -> C=C(alpha).
def at(point, dx, dy):
    return point.xy + (dx, dy)


s.curly(at(ion.bond(0, 1), 0.35, 0), at(ion.bond(0, 8), 0.1, -0.12), bend=0.45)
s.curly(at(ion.bond(7, 8), -0.12, -0.12), at(ion.bond(6, 7), -0.2, 0), bend=0.5)
s.curly(at(ion.bond(5, 6), -0.06, 0.14), at(ion.bond(1, 5), 0.1, 0.14), bend=-0.7)

s.arrow((3.6, 0), (5.2, 0))

# Products: enol radical cation (m/z 86) and propene (42).
x0 = 8.6
C = np.array([x0, 0.0])
s.molecule("C=C(O)CCC", coords=[C + (-1.4, 0), C, C + (0, 1.4), C + (1.21, -0.7), C + (2.42, 0), C + (3.63, -0.7)], show_carbons=range(6))
s.text(C + (-2.5, 0.3), "[", size=26)
s.text(C + (4.3, 0.3), r"]$^{+\bullet}$", size=13)
s.text((x0 + 0.6, -1.7), "$m/z$ 86", size=13)
s.plus((x0 + 7.0, 0))
s.molecule("C=CC", at=(x0 + 9.2, 0), show_carbons=[0, 1, 2])
s.text((x0 + 9.2, -1.5), "propene, 42", size=13)
s.draw()
