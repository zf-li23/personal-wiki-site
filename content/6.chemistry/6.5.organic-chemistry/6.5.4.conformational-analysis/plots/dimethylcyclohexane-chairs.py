"""The two chairs of trans-1,2-, cis-1,2- and cis-1,3-dimethylcyclohexane (Example 4.6.1), drawn as
projections of an ideal chair. Each methyl keeps its side of the ring (up or down) on ring flip, while
axial (a) and equatorial (e) are exchanged. Numbers: strain counted in gauche butane units
(3.8 kJ/mol each; a CH3/CH3 1,3-diaxial contact counts about 15 kJ/mol)."""

import numpy as np
import matplotlib.pyplot as plt

CC, CH = 1.54, 1.0
ME = "#16a34a"
ink = plt.rcParams["text.color"]


def chair(sign):
    h = 0.255 * sign
    r = np.sqrt(CC**2 - 4 * h**2)
    return np.array([[r * np.cos(np.pi / 3 * k), r * np.sin(np.pi / 3 * k), h if k % 2 == 0 else -h] for k in range(6)])


def bonds(C):
    """For each carbon: dict up/down -> (end point, 'a' or 'e')."""
    out = []
    for i in range(6):
        u1, u2 = C[i - 1] - C[i], C[(i + 1) % 6] - C[i]
        u1, u2 = u1 / np.linalg.norm(u1), u2 / np.linalg.norm(u2)
        b = -(u1 + u2)
        b /= np.linalg.norm(b)
        p = np.cross(u1, u2)
        p /= np.linalg.norm(p)
        a = np.radians(54)
        pair = [C[i] + CH * (b * np.cos(a) + s * p * np.sin(a)) for s in (1, -1)]
        ax_i = int(np.argmax([abs(q[2] - C[i][2]) for q in pair]))
        kinds = ["a" if k == ax_i else "e" for k in range(2)]
        up = int(np.argmax([q[2] for q in pair]))
        out.append({"up": (pair[up], kinds[up]), "down": (pair[1 - up], kinds[1 - up])})
    return out


def project(p, elev=18):
    e = np.radians(elev)
    return np.array([p[0], p[2] * np.cos(e) + p[1] * np.sin(e)])


def draw(ax, sign, x0, y0, subs):
    C = chair(sign)
    B = bonds(C)
    P = [project(c) + [x0, y0] for c in C]
    for i in range(6):
        ax.plot(*zip(P[i], P[(i + 1) % 6]), color=ink, lw=2, solid_capstyle="round")
    kinds = []
    for i, side in subs:
        q, kind = B[i][side]
        q = project(q) + [x0, y0]
        ax.plot(*zip(P[i], q), color=ME, lw=2.6)
        ax.text(*(q + 0.42 * (q - P[i])), "CH$_3$", color=ME, ha="center", va="center", fontsize=10)
        kinds.append(kind)
    return ",".join(kinds)


rows = [
    ("trans-1,2", [(0, "up"), (1, "down")], {"e,e": "1 gauche: 3.8", "a,a": "4 gauche: 15.2"}),
    ("cis-1,2", [(0, "up"), (1, "up")], {"a,e": "3 gauche: 11.4", "e,a": "3 gauche: 11.4"}),
    ("cis-1,3", [(0, "up"), (2, "up")], {"e,e": "0", "a,a": "2 + CH$_3$/CH$_3$: about 23"}),
]
fig, ax = plt.subplots(figsize=(10, 9.8))
for r, (name, subs, energies) in enumerate(rows):
    y0 = -4.3 * r
    k1 = draw(ax, 1, 0, y0, subs)
    k2 = draw(ax, -1, 7.0, y0, subs)
    ax.annotate("", xy=(4.1, y0 + 0.2), xytext=(2.9, y0 + 0.2), arrowprops=dict(arrowstyle="<|-|>", color=ink, lw=1.2))
    ax.text(3.5, y0 + 0.5, "ring flip", ha="center", fontsize=9)
    ax.text(-3.4, y0, name, ha="center", va="center", fontsize=11)
    ax.text(0, y0 - 1.75, f"{k1}  ({energies[k1]})", ha="center", fontsize=10)
    ax.text(7.0, y0 - 1.75, f"{k2}  ({energies[k2]})", ha="center", fontsize=10)
ax.set_aspect("equal")
ax.set_xlim(-4.6, 9.6)
ax.set_ylim(-10.9, 1.9)
ax.axis("off")
