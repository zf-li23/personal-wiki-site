"""E2 of neomenthyl and menthyl chloride on the cyclohexane chair. Top: in neomenthyl chloride the
stable chair has the isopropyl and methyl groups equatorial and chlorine axial; both neighbouring
carbons carry an axial hydrogen anti to chlorine, so elimination is fast and gives mainly the more
substituted 3-menthene (about 3 : 1 over 2-menthene). Bottom: in menthyl chloride all three groups are
equatorial; the ring must flip to the all-axial chair, where only C6 has an axial hydrogen anti to
chlorine (the C2 hydrogen is now equatorial), so elimination is about 200 times slower and gives only
2-menthene."""

import math

import matplotlib.pyplot as plt
import numpy as np

from wikichem import Scheme

s = Scheme()
LINES = []
TILT = math.radians(18)
ROT = math.radians(15)


def project(p):
    x, y, z = p
    x, y = x * math.cos(ROT) - y * math.sin(ROT), x * math.sin(ROT) + y * math.cos(ROT)
    return np.array([1.15 * x, z * math.cos(TILT) + y * math.sin(TILT)])


def chair(c, subs, scale=1.6):
    """Ring atoms C1..C6; subs: {(atom, 'ax'|'eq'): label or '' for a plain line}. Returns 2D points."""
    c = np.asarray(c, float)
    r, h = 0.945, 0.163
    ring3 = [np.array([r * math.cos(math.radians(60 * i + 180)), r * math.sin(math.radians(60 * i + 180)), h * (1 if i % 2 else -1)])
             for i in range(6)]
    pts = [c + scale * project(p) for p in ring3]
    for i in range(6):
        LINES.append((pts[i], pts[(i + 1) % 6]))
    ends = {}
    for (k, kind), text in subs.items():
        p = ring3[k - 1]
        sign = 1 if p[2] > 0 else -1
        if kind == "ax":
            d = np.array([0, 0, sign * 1.0])
        else:
            d = np.array([p[0], p[1], -sign * 0.35])
            d = d / np.linalg.norm(d)
        q = c + scale * project(p + 0.8 * d)
        end = q
        if text:
            u = (q - pts[k - 1]) / np.linalg.norm(q - pts[k - 1])
            s.text(q + 0.25 * u, text)
            end = q - 0.05 * u
        LINES.append((pts[k - 1], end))
        ends[(k, kind)] = q
    for p in pts:
        s.text(p, "")
    return pts, ends


IPR = r"$i$-Pr"
# Top: neomenthyl chloride
y = 0.0
pts, e = chair((0, y), {(1, "ax"): "Cl", (2, "eq"): IPR, (2, "ax"): "H", (6, "ax"): "H", (5, "eq"): ""})
hb = e[(2, "ax")]
s.text(hb + np.array([1.2, 0.6]), r"EtO$^-$")
s.curly(hb + np.array([0.8, 0.6]), hb + np.array([0.15, 0.2]), bend=0.3)
s.curly((pts[1] + e[(2, "ax")]) / 2 + np.array([0.08, 0]), (pts[0] + pts[1]) / 2 + np.array([0.05, -0.05]), bend=0.8)
s.curly((pts[0] + e[(1, "ax")]) / 2 + np.array([0.1, 0]), e[(1, "ax")] + np.array([0.35, 0.15]), bend=-0.6)
s.text((0.3, y - 2.3), "neomenthyl chloride")
s.arrow((2.6, y), (4.0, y), above="fast")
s.molecule("CC1CCC(C(C)C)=CC1", at=(5.8, y))
s.text((5.8, y - 1.9), "3-menthene (75%)")
s.plus((7.8, y))
s.molecule("CC1C=CC(C(C)C)CC1", at=(9.8, y))
s.text((9.8, y - 1.9), "2-menthene (25%)")

# Bottom: menthyl chloride
y = -5.6
chair((0, y), {(1, "eq"): "Cl", (2, "eq"): IPR, (5, "eq"): ""})
s.text((0.3, y - 2.3), "menthyl chloride")
s.arrow((2.0, y), (3.2, y), kind="equilibrium", above="ring flip")
pts, e = chair((5.2, y), {(1, "ax"): "Cl", (2, "ax"): IPR, (6, "ax"): "H", (5, "ax"): ""})
hb = e[(6, "ax")]
s.text(hb + np.array([-1.3, 0.6]), r"EtO$^-$")
s.curly(hb + np.array([-0.9, 0.6]), hb + np.array([-0.15, 0.2]), bend=-0.3)
s.curly((pts[5] + e[(6, "ax")]) / 2 + np.array([0.08, 0]), (pts[5] + pts[0]) / 2 + np.array([0.0, -0.08]), bend=-0.8)
s.curly((pts[0] + e[(1, "ax")]) / 2 + np.array([-0.1, 0]), e[(1, "ax")] + np.array([-0.35, 0.15]), bend=0.6)
s.text((5.5, y - 2.3), "all-axial chair")
s.arrow((7.6, y), (9.0, y), above="slow")
s.molecule("CC1C=CC(C(C)C)CC1", at=(10.6, y))
s.text((10.6, y - 1.9), "2-menthene only")

fig, ax = s.draw()
ink = plt.rcParams["text.color"]
for a, b in LINES:
    ax.plot(*zip(a, b), color=ink, lw=1.4, solid_capstyle="round")
