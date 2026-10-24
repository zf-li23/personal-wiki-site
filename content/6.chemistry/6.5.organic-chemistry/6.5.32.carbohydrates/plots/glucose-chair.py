"""alpha- and beta-D-glucopyranose in the 4C1 chair (C4 above and C1 below the mean plane of
the ring), drawn by projecting a 3D chair. The ring is laid out like the Haworth projection
(O5 at the back right, C1 at the right), and each substituent is placed by the Haworth rule:
the group that points up in the Haworth projection takes the position on the upper side of the
ring at that carbon, which is the axial position on an "up" carbon and the equatorial position
on a "down" carbon. In the beta anomer every large group (OH, CH2OH) is equatorial; in the alpha
anomer the anomeric OH (red) is axial. Hydrogens on C2-C5 are implicit."""

import numpy as np
import matplotlib.pyplot as plt

RED = "#dc2626"
CC, SUB = 1.6, 1.05
RING = ["O5", "C1", "C2", "C3", "C4", "C5"]
# Haworth (up, down) groups of D-glucopyranose; C1 depends on the anomer
HAWORTH = {"C2": ("H", "OH"), "C3": ("OH", "H"), "C4": ("H", "OH"), "C5": ("CH$_2$OH", "H")}


def chair():
    """Ring atoms in Haworth order, clockwise seen from above, O5 at the back right; z alternates."""
    h = 0.28
    r = np.sqrt(CC**2 - 4 * h**2)
    out = []
    for k in range(6):
        t = np.radians(60 - 60 * k)
        out.append(np.array([r * np.cos(t), r * np.sin(t), h if k % 2 == 0 else -h]))
    return out


def positions(C, i):
    """The two substituent positions on ring atom i (tetrahedral), sorted by height (upper first)."""
    u1, u2 = C[i - 1] - C[i], C[(i + 1) % 6] - C[i]
    u1, u2 = u1 / np.linalg.norm(u1), u2 / np.linalg.norm(u2)
    b = -(u1 + u2)
    b /= np.linalg.norm(b)
    p = np.cross(u1, u2)
    p /= np.linalg.norm(p)
    a = np.radians(54.75)
    pair = [C[i] + SUB * (b * np.cos(a) + s * p * np.sin(a)) for s in (1, -1)]
    return sorted(pair, key=lambda q: -q[2])


def project(p, x0):
    e = np.radians(20)
    return np.array([p[0] + x0, p[2] * np.cos(e) + p[1] * np.sin(e)])


def draw(ax, x0, anomer, title):
    ink = plt.rcParams["text.color"]
    C = chair()
    P = [project(c, x0) for c in C]
    for i in range(6):
        j = (i + 1) % 6
        a, b = P[i], P[j]
        if RING[i] == "O5" or RING[j] == "O5":  # stop short of the O label
            d = b - a
            if RING[i] == "O5":
                a = a + 0.18 * d / np.linalg.norm(d)
            else:
                b = b - 0.18 * d / np.linalg.norm(d)
        ax.plot(*zip(a, b), color=ink, lw=2.0, solid_capstyle="round")
    ax.text(*P[0], "O", ha="center", va="center", fontsize=12)
    groups = dict(HAWORTH)
    groups["C1"] = ("OH", "H") if anomer == "beta" else ("H", "OH")
    for i, name in enumerate(RING):
        if name == "O5":
            continue
        upper, lower = positions(C, i)
        for q, g in ((upper, groups[name][0]), (lower, groups[name][1])):
            if g == "H" and name != "C1":
                continue  # ring hydrogens are left implicit, as is usual for sugar chairs
            end = project(q, x0)
            col = RED if name == "C1" and g == "OH" else ink
            ax.plot(*zip(P[i], end), color=col, lw=1.2)
            lab = end + (end - P[i]) / np.linalg.norm(end - P[i]) * 0.3
            if g == "OH" and end[0] < P[i][0] - 0.2:
                g = "HO"
            ax.text(*lab, g, ha="center", va="center", fontsize=9.5 if g != "H" else 8.5, color=col)
        ax.text(*(P[i] + np.array([0.12, -0.2 if C[i][2] < 0 else 0.16])), name[1], fontsize=7, color="0.5")
    ax.text(x0, -2.1, title, ha="center", fontsize=10.5)


fig, ax = plt.subplots(figsize=(12, 3.9))
draw(ax, 0.0, "alpha", r"$\alpha$-D-glucopyranose: anomeric OH axial")
draw(ax, 6.6, "beta", r"$\beta$-D-glucopyranose: all OH and CH$_2$OH equatorial")
ax.set_aspect("equal")
ax.set_xlim(-2.8, 9.4)
ax.set_ylim(-2.4, 1.9)
ax.axis("off")
