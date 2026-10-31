"""Caspar-Klug construction of icosahedral shells (Theorem 7.5.2).

Top: on a hexagonal lattice of capsomer positions, the face of the icosadeltahedron is the
equilateral triangle spanned by the lattice vector (h, k) and its rotation by 60 degrees; its area
is T = h^2 + hk + k^2 times that of the smallest lattice triangle (T = 1). Pentamers sit at the
corners. Bottom: the lattice points inside every face of an icosahedron are mapped linearly onto
the face and projected onto a sphere, which gives the capsomer centres of the shell; the program
counts 12 pentamers and 10(T - 1) hexamers, 60T subunits in all.
"""

import itertools

import matplotlib.patches as mpatches
import numpy as np
import wikibio as bio

P = bio.P
FT = bio.core.FONT

A1 = np.array([1.0, 0.0])
A2 = np.array([0.5, np.sqrt(3) / 2])


def rot60(v):
    c, s = 0.5, np.sqrt(3) / 2
    return np.array([c * v[0] - s * v[1], s * v[0] + c * v[1]])


def icosahedron():
    g = (1 + np.sqrt(5)) / 2
    V = []
    for a, b in itertools.product((-1, 1), repeat=2):
        V += [(0, a, b * g), (a, b * g, 0), (b * g, 0, a)]
    V = np.array(V, float)
    V /= np.linalg.norm(V[0])
    F = []
    for i, j, k in itertools.combinations(range(12), 3):
        d = [np.linalg.norm(V[i] - V[j]), np.linalg.norm(V[j] - V[k]), np.linalg.norm(V[i] - V[k])]
        if max(d) < 1.1:
            # orient counterclockwise seen from outside
            if np.dot(np.cross(V[j] - V[i], V[k] - V[i]), V[i] + V[j] + V[k]) < 0:
                j, k = k, j
            F.append((i, j, k))
    return V, F


def capsomers(h, k):
    V, F = icosahedron()
    A = h * A1 + k * A2
    B = rot60(A)
    M = np.array([A, B]).T
    Minv = np.linalg.inv(M)
    n = h + k + 1
    pts = []
    for i in range(-n, 2 * n):
        for j in range(-n, 2 * n):
            p = i * A1 + j * A2
            l1, l2 = Minv @ p
            l0 = 1 - l1 - l2
            if min(l0, l1, l2) < -1e-9:
                continue
            for f in F:
                x = l0 * V[f[0]] + l1 * V[f[1]] + l2 * V[f[2]]
                pts.append(x / np.linalg.norm(x))
    pts = np.array(pts)
    uniq = []
    for p in pts:
        if not any(np.linalg.norm(p - q) < 1e-6 for q in uniq):
            uniq.append(p)
    uniq = np.array(uniq)
    is_penta = np.array([min(np.linalg.norm(p - v) for v in V) < 1e-6 for p in uniq])
    return uniq, is_penta


CASES = [(1, 0), (1, 1), (2, 0), (2, 1)]
fig, ax = bio.canvas(24.0, 13.6)
bio.panel(ax, "A", (0.1, 13.5))
for c, (h, k) in enumerate(CASES):
    T = h * h + h * k + k * k
    ox, oy, s = 1.6 + 5.9 * c, 8.6, 1.05
    # lattice
    for i in range(-2, 5):
        for j in range(-1, 5):
            p = i * A1 + j * A2
            q = np.array([ox, oy]) + s * p
            if ox - 1.0 < q[0] < ox + 3.7 and oy - 0.7 < q[1] < oy + 3.4:
                ax.add_patch(mpatches.RegularPolygon(q, 6, radius=0.3 * s, orientation=0,
                             facecolor=P.fill("virus"), edgecolor=P.edge("virus"), lw=0.6, zorder=3))
    A = h * A1 + k * A2
    B = rot60(A)
    tri = np.array([[0, 0], A, B, [0, 0]]) * s + [ox, oy]
    ax.fill(tri[:, 0], tri[:, 1], color=P.fill("highlight"), alpha=0.35, zorder=2, lw=0)
    ax.plot(tri[:, 0], tri[:, 1], color=P.edge("highlight"), lw=1.4, zorder=4)
    for v in tri[:3]:
        ax.add_patch(mpatches.RegularPolygon(v, 5, radius=0.33 * s, facecolor=P.fill("channel"),
                     edgecolor=P.edge("channel"), lw=0.8, zorder=5))
    # the (h, k) path: h steps along a1 then k along a2
    path = np.array([[0, 0], h * A1, h * A1 + k * A2]) * s + [ox, oy]
    ax.plot(path[:, 0], path[:, 1], color=P.ink(), lw=1.0, ls="--", zorder=6)
    bio.label(ax, (ox + 1.6, oy - 1.25), f"(h, k) = ({h}, {k})   T = {T}", size="small")

bio.panel(ax, "B", (0.1, 6.3))
light_dir = np.array([-0.4, 0.5, 0.77])
for c, (h, k) in enumerate(CASES):
    T = h * h + h * k + k * k
    pts, penta = capsomers(h, k)
    # rotate so that a fivefold axis points slightly away from the viewer
    th = 0.35
    Rx = np.array([[1, 0, 0], [0, np.cos(th), -np.sin(th)], [0, np.sin(th), np.cos(th)]])
    q = pts @ Rx.T
    cx, cy, R = 3.0 + 5.9 * c, 3.2, 2.1
    ax.add_patch(mpatches.Circle((cx, cy), R, facecolor=P.light("cytoplasm"), edgecolor=P.muted(),
                 lw=0.6, zorder=1))
    order = np.argsort(q[:, 2])
    rad = 0.40 * R * np.sqrt(4 * np.pi / (10 * T + 2))
    for idx in order:
        x, y, z = q[idx]
        if z < -0.05:
            continue
        tok = "channel" if penta[idx] else "virus"
        shade = 0.25 + 0.75 * max(0.0, float(np.dot([x, y, z], light_dir)))
        fc = P.mix(P.edge(tok), P.fill(tok), shade)
        ax.add_patch(mpatches.RegularPolygon((cx + R * x, cy + R * y), 5 if penta[idx] else 6,
                     radius=rad * (0.3 + 0.7 * z), facecolor=fc, edgecolor=P.edge(tok), lw=0.5, zorder=3 + z))
    npen, nhex = int(penta.sum()), int((~penta).sum())
    bio.label(ax, (cx, 0.55), f"T = {T}: {npen} pentamers + {nhex} hexamers = {5 * npen + 6 * nhex} subunits",
              size="tiny")
bio.label(ax, (21.0, 13.1), "pentamer", size="tiny", ha="left")
ax.add_patch(mpatches.RegularPolygon((20.6, 13.1), 5, radius=0.25, facecolor=P.fill("channel"),
             edgecolor=P.edge("channel"), lw=0.8))
bio.label(ax, (21.0, 12.4), "hexamer", size="tiny", ha="left")
ax.add_patch(mpatches.RegularPolygon((20.6, 12.4), 6, radius=0.25, facecolor=P.fill("virus"),
             edgecolor=P.edge("virus"), lw=0.8))
