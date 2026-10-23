"""McLafferty rearrangement of the 4-octanone molecular ion (m/z 128). In a six-membered cyclic
arrangement the gamma hydrogen moves to the carbonyl oxygen and the alpha-beta bond breaks:
propene (42) leaves as a neutral molecule and the enol radical cation m/z 86 remains. The three
curved arrows show the formal electron-pair shifts (as in a retro-ene reaction); the charge and the
unpaired electron stay on the enol."""

import numpy as np
import matplotlib.pyplot as plt
from wikichem import Scheme

s = Scheme(scale=0.5)


def text(at, t, ha="center"):
    p = np.asarray(at, float)
    s.points.append(p)
    s.items.append(lambda ax: ax.text(*p, t, ha=ha, va="center", fontsize=13, color=plt.rcParams["text.color"]))


def bond(a, b, order=1, dotted=False, ca=0.3, cb=0.3):
    a, b = np.asarray(a, float), np.asarray(b, float)
    u = (b - a) / np.linalg.norm(b - a)
    n = np.array([-u[1], u[0]])
    p, q = a + ca * u, b - cb * u
    s.points.extend([p, q])

    def draw(ax):
        ink = plt.rcParams["text.color"]
        if dotted:
            ax.plot(*zip(p, q), color=ink, lw=1.3, ls=(0, (1, 2.5)))
        elif order == 2:
            for sgn in (-1, 1):
                ax.plot(*zip(p + sgn * 0.07 * n, q + sgn * 0.07 * n), color=ink, lw=1.4)
        else:
            ax.plot(*zip(p, q), color=ink, lw=1.4)

    s.items.append(draw)


def mid(a, b):
    return (np.asarray(a, float) + np.asarray(b, float)) / 2


# Reactant ring: O, C, C(alpha), C(beta), C(gamma), H on a hexagon of side 1.4.
r = 1.4
ang = np.radians([150, 210, 270, 330, 30, 90])
P = dict(zip(["O", "C", "Ca", "Cb", "Cg", "H"], [r * np.array([np.cos(t), np.sin(t)]) for t in ang]))
text(P["O"], "O")
text(P["O"] + np.array([-0.42, 0.25]), r"$^{+\bullet}$")
text(P["C"], "C")
text(P["Ca"], r"CH$_2$")
text(P["Cb"], r"CH$_2$")
text(P["Cg"], "CH")
text(P["H"], "H")
bond(P["O"], P["C"], order=2)
bond(P["C"], P["Ca"], cb=0.45)
bond(P["Ca"], P["Cb"], ca=0.5, cb=0.5)
bond(P["Cb"], P["Cg"], ca=0.35, cb=0.3)
bond(P["Cg"], P["H"], ca=0.35, cb=0.25)
bond(P["H"], P["O"], dotted=True, ca=0.25, cb=0.3)
text(P["C"] + np.array([-1.0, 0]), r"H$_3$CCH$_2$CH$_2$", ha="right")
bond(P["C"] + np.array([-1.0, 0]), P["C"], ca=0.05, cb=0.3)
text(P["Cg"] + np.array([1.2, 0]), r"CH$_3$", ha="left")
bond(P["Cg"], P["Cg"] + np.array([1.2, 0]), ca=0.4, cb=0.05)
text((0, -2.5), "4-octanone, $m/z$ 128")

# Electron-pair shifts: C=O pi -> O-H; C(gamma)-H -> C(beta)=C(gamma); C(alpha)-C(beta) -> C=C(alpha).
s.curly(mid(P["O"], P["C"]) + np.array([0.35, 0]), mid(P["O"], P["H"]) + np.array([0.1, -0.12]), bend=0.45)
s.curly(mid(P["Cg"], P["H"]) + np.array([-0.12, -0.12]), mid(P["Cb"], P["Cg"]) + np.array([-0.2, 0]), bend=0.5)
s.curly(mid(P["Ca"], P["Cb"]) + np.array([-0.06, 0.14]), mid(P["C"], P["Ca"]) + np.array([0.1, 0.14]), bend=-0.7)

s.arrow((3.6, 0), (5.2, 0))

# Products: enol radical cation (m/z 86) and propene (42).
x0 = 8.6
C = np.array([x0, 0.0])
O = C + np.array([0.0, 1.4])
text(C, "C")
text(O, "OH")
bond(C, O, ca=0.3, cb=0.32)
text(C + np.array([-0.9, 0]), r"H$_2$C", ha="right")
bond(C + np.array([-0.9, 0]), C, order=2, ca=0.05, cb=0.3)
text(C + np.array([0.9, 0]), r"CH$_2$CH$_2$CH$_3$", ha="left")
bond(C, C + np.array([0.9, 0]), ca=0.3, cb=0.05)
text(C + np.array([-1.8, 0]), "[", ha="center")
text(C + np.array([3.05, 0]), r"]$^{+\bullet}$", ha="left")
text((x0 + 0.5, -1.3), "$m/z$ 86")
s.plus((x0 + 4.9, 0))
text((x0 + 5.5, 0), r"H$_2$C=CH$-$CH$_3$", ha="left")
text((x0 + 7.2, -1.3), "propene, 42")
s.draw()
