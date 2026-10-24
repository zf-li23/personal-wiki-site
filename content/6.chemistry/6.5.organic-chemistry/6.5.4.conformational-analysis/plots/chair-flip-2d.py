"""Textbook chair drawings obtained by projecting the 3D chair, before and after the ring flip.
Axial bonds red, equatorial bonds blue; the methyl group on C1 moves from equatorial to axial.
The flipped chair is the mirror image of the first through its mean plane (z -> -z), which keeps
every atom's number but exchanges the axial and equatorial positions."""

import numpy as np
import matplotlib.pyplot as plt

CC, CH = 1.54, 1.0
AX, EQ, ME = "#dc2626", "#2563eb", "#16a34a"


def chair(sign):
    h = 0.255 * sign
    r = np.sqrt(CC**2 - 4 * h**2)
    return np.array([[r * np.cos(np.pi / 3 * k), r * np.sin(np.pi / 3 * k), h if k % 2 == 0 else -h] for k in range(6)])


def subs(C):
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
        pair.sort(key=lambda q: -abs(q[2] - C[i][2]))  # axial first
        out.append(pair)
    return out


def project(p, elev=18):
    e = np.radians(elev)
    return np.array([p[0], p[2] * np.cos(e) + p[1] * np.sin(e)])


def draw(ax, sign, x0, title):
    ink = plt.rcParams["text.color"]
    C = chair(sign)
    S = subs(C)
    P = [project(c) + [x0, 0] for c in C]
    for i in range(6):
        j = (i + 1) % 6
        ax.plot(*zip(P[i], P[j]), color=ink, lw=2.2, solid_capstyle="round")
    for i in range(6):
        for k, colour in ((0, AX), (1, EQ)):
            q = project(S[i][k]) + [x0, 0]
            me = i == 0 and ((k == 1) if sign > 0 else (k == 0))
            ax.plot(*zip(P[i], q), color=ME if me else colour, lw=3 if me else 1.4)
            if me:
                ax.text(*(q + (q - P[i]) * 0.45), "CH$_3$", color=ME, ha="center", va="center", fontsize=11)
        off = np.array([0.0, -0.32 if C[i][2] < 0 else 0.3])
        ax.text(*(P[i] + off * 0 + np.array([0.18, 0.0])), str(i + 1), fontsize=8, color="0.45")
    ax.text(x0, -2.1, title, ha="center", fontsize=10)


fig, ax = plt.subplots(figsize=(11, 3.6))
draw(ax, 1, 0, "CH$_3$ equatorial (about 95%)")
draw(ax, -1, 6.6, "CH$_3$ axial (about 5%)")
ink = plt.rcParams["text.color"]
for dy, (a, b) in ((1.0, (2.7, 3.9)), (0.8, (3.9, 2.7))):
    ax.annotate("", xy=(b, dy), xytext=(a, dy), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.2))
ax.text(3.3, 1.25, "ring flip", ha="center", fontsize=9)
ax.plot([], [], color=AX, label="axial")
ax.plot([], [], color=EQ, label="equatorial")
ax.legend(loc="upper center", ncol=2, frameon=False, fontsize=9)
ax.set_aspect("equal")
ax.set_xlim(-2.4, 9.0)
ax.set_ylim(-2.4, 2.2)
ax.axis("off")
