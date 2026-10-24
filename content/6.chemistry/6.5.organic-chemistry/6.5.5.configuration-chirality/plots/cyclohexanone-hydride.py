"""Stereoselectivity of hydride reduction of 4-tert-butylcyclohexanone. The tert-butyl group locks the
chair (equatorial). A small hydride donor (LiAlH4) approaches the carbonyl carbon mainly from the axial
direction (top face here), which puts H axial and OH equatorial: the trans alcohol (about 90%).
Approach from the equatorial direction (hindered by the C2/C6 hydrogens for large reagents, but favoured
by bulky L-Selectride, which cannot pass the axial H at C3/C5) gives the axial OH of the cis alcohol.
Chairs are projections of an ideal 3D chair; only the relevant hydrogens are drawn."""

import numpy as np
import matplotlib.pyplot as plt

CC, CH = 1.54, 1.0


def chair():
    h = 0.255
    r = np.sqrt(CC**2 - 4 * h**2)
    return np.array([[r * np.cos(np.pi / 3 * k), r * np.sin(np.pi / 3 * k), h if k % 2 == 0 else -h] for k in range(6)])


def subs(C):
    """For each ring carbon: (axial, equatorial) bond end points."""
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
        pair.sort(key=lambda q: -abs(q[2] - C[i][2]))
        out.append(pair)
    return out


def project(p, elev=18):
    e = np.radians(elev)
    return np.array([p[0], p[2] * np.cos(e) + p[1] * np.sin(e)])


C = chair()
S = subs(C)
fig, ax = plt.subplots(figsize=(10, 4.8))
ink = plt.rcParams["text.color"]


def ring(x0, y0):
    P = [project(c) + [x0, y0] for c in C]
    for i in range(6):
        ax.plot(*zip(P[i], P[(i + 1) % 6]), color=ink, lw=2, solid_capstyle="round")
    return P


def bond(P, i, k, text, x0, y0, stretch=1.0, dx=0.0):
    q = project(C[i] + stretch * (S[i][k] - C[i])) + [x0, y0]
    ax.plot(*zip(P[i], P[i] + 0.78 * (q - P[i])), color=ink, lw=1.6)
    ax.text(*(q + [dx, 0]), text, ha="center", va="center", fontsize=11)
    return q


def tbu(P, x0, y0):
    bond(P, 3, 1, "$t$-Bu", x0, y0, stretch=1.25, dx=-0.25)


# ketone: C1 = ring atom 0 (right tip, an "up" carbon)
x0, y0 = 0.0, 0.0
P = ring(x0, y0)
tbu(P, x0, y0)
mid = (project(S[0][0]) + project(S[0][1])) / 2 - project(C[0])
u = mid / np.linalg.norm(mid)
O = P[0] + 1.05 * u
for off in (-0.07, 0.07):
    n = np.array([-u[1], u[0]]) * off
    ax.plot(*zip(P[0] + n, P[0] + 0.8 * (O - P[0]) + n), color=ink, lw=1.6)
ax.text(*(O + 0.12 * u), "O", ha="center", va="center", fontsize=11)
ax.annotate("", xy=P[0] + [0.0, 0.22], xytext=P[0] + [-0.35, 1.75],
            arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.3, connectionstyle="arc3,rad=-0.25"))
ax.text(P[0][0] - 0.55, P[0][1] + 2.0, "axial attack", ha="center", fontsize=10)
ax.annotate("", xy=P[0] + [0.12, -0.18], xytext=P[0] + [1.3, -1.55],
            arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.3, connectionstyle="arc3,rad=-0.25"))
ax.text(P[0][0] + 0.2, P[0][1] - 1.95, "equatorial attack", ha="center", fontsize=10)
ax.text(x0 - 0.4, -2.9, "4-tert-butylcyclohexanone", ha="center", fontsize=10)

# products
for x0, y0, oh, title in ((7.6, 1.3, 1, "trans: OH equatorial (LiAlH$_4$: about 90%)"),
                          (7.6, -2.1, 0, "cis: OH axial (L-Selectride: major)")):
    P = ring(x0, y0)
    tbu(P, x0, y0)
    bond(P, 0, oh, "OH", x0, y0, dx=0.2 if oh else 0.0)
    bond(P, 0, 1 - oh, "H", x0, y0, dx=0.1 if not oh else 0.0)
    ax.text(x0 + 0.3, y0 - 1.15, title, ha="center", va="center", fontsize=10)
ax.annotate("", xy=(4.6, 1.2), xytext=(3.0, 0.5), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.2))
ax.annotate("", xy=(4.6, -1.8), xytext=(3.0, -0.8), arrowprops=dict(arrowstyle="-|>", color=ink, lw=1.2))
ax.set_aspect("equal")
ax.set_xlim(-2.8, 11.6)
ax.set_ylim(-3.4, 2.9)
ax.axis("off")
