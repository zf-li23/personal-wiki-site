"""The symmetries available to assemblies of identical chiral subunits (Theorem 7.4.1).

Each group is generated numerically by closure from two rotation generators; every element is
applied to one asymmetric "subunit" (a large and a small sphere, so that its orientation can be
seen) and the result is drawn in orthographic projection, nearer subunits darker. One copy is
highlighted. Faint lines: edges of the tetrahedron, cube and icosahedron whose rotation groups are T, O and I.
The last panel is a helical array with 3.5 subunits per turn, the arrangement of an open-ended
polymer (axis vertical, viewed from the side).
"""

import numpy as np
import wikibio as bio
import matplotlib.patches as mpatches

P = bio.P
FT = bio.core.FONT


def rot(axis, angle):
    a = np.asarray(axis, float)
    a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * K @ K


def closure(gens):
    G = [np.eye(3)]
    frontier = [np.eye(3)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                m = h @ g
                if not any(np.allclose(m, x, atol=1e-8) for x in G):
                    G.append(m)
                    new.append(m)
        frontier = new
    return G


gr = (1 + np.sqrt(5)) / 2
GROUPS = [
    ("C$_5$", "cyclic, order 5", closure([rot([0, 0, 1], 2 * np.pi / 5)]), (0.2, 0.0)),
    ("D$_4$", "dihedral, order 8", closure([rot([0, 0, 1], np.pi / 2), rot([1, 0, 0], np.pi)]), (1.05, 0.3)),
    ("T", "tetrahedral, order 12", closure([rot([1, 1, 1], 2 * np.pi / 3), rot([0, 0, 1], np.pi)]), (0.5, 0.4)),
    ("O", "octahedral, order 24", closure([rot([1, 1, 1], 2 * np.pi / 3), rot([0, 0, 1], np.pi / 2)]), (0.45, 0.5)),
    ("I", "icosahedral, order 60", closure([rot([0, 1, gr], 2 * np.pi / 5), rot([1, 1, 1], 2 * np.pi / 3)]), (0.3, 0.25)),
]

fig, ax = bio.canvas(27.0, 7.6)
light = np.array([-0.4, 0.5, 0.77])
light /= np.linalg.norm(light)


def draw_units(cx, cy, scale, units, rb=0.30, highlight=0, tok="protein"):
    """units: list of (big centre, small centre) in 3D after the view rotation (z towards viewer)."""
    items = []
    for i, (b, sm) in enumerate(units):
        items.append((b[2], i, b, rb))
        items.append((sm[2], i, sm, 0.55 * rb))
    zs = np.array([it[0] for it in items])
    zmin, zmax = zs.min(), zs.max()
    for z, i, c, r in sorted(items, key=lambda t: t[0]):
        t = (z - zmin) / (zmax - zmin + 1e-9)
        tk = "highlight" if i == highlight else tok
        fc = P.mix(P.mix(P.fill(tk), P.surface(), 0.6), P.fill(tk), t)
        ax.add_patch(mpatches.Circle((cx + scale * c[0], cy + scale * c[1]), scale * r * (0.8 + 0.2 * t),
                                     facecolor=fc, edgecolor=P.edge(tk), lw=0.6, zorder=3 + t))


def polyhedron_edges(name):
    """Vertices and edges of the polyhedron whose rotation group is drawn (for a faint guide)."""
    if name == "T":
        V = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
    elif name == "O":
        V = np.array([[x, y, z] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)], float)
    else:
        V = []
        for a in (-1, 1):
            for b in (-1, 1):
                V += [(0, a, b * gr), (a, b * gr, 0), (b * gr, 0, a)]
        V = np.array(V, float)
    V /= np.linalg.norm(V[0])
    d = np.linalg.norm(V[:, None] - V[None], axis=-1)
    dmin = d[d > 1e-9].min()
    E = [(i, j) for i in range(len(V)) for j in range(i + 1, len(V)) if abs(d[i, j] - dmin) < 1e-6]
    return V, E


for j, (name, desc, G, view) in enumerate(GROUPS):
    V = rot([1, 0, 0], -view[1]) @ rot([0, 1, 0], view[0])
    N = len(G)
    cx = 2.6 + 4.6 * j
    if name[0] in "CD":
        rb = 0.30
        big = np.array([1.0, 0.0, 0.25 if name[0] == "C" else 0.45])
        small = big + np.array([0.22, 0.30, 0.18])
        scale = 1.35
    else:
        rb = 0.40 * np.sqrt(12 / N)
        big = np.array([0.20, 0.33, 0.92])
        big = big / np.linalg.norm(big) * 1.5
        tang = np.cross(big, [0, 0, 1.0])
        tang /= np.linalg.norm(tang)
        small = big * (1 + 0.5 * rb / 1.5) + 0.85 * rb * tang
        scale = 1.25
        PV, PE = polyhedron_edges(name[0])
        PV = (V @ (PV.T * 1.5)).T
        for a, b in PE:
            ax.plot(cx + scale * PV[[a, b], 0], 4.1 + scale * PV[[a, b], 1], color=P.muted(), lw=0.5,
                    ls="-", zorder=2.5, alpha=0.8)
    units = [(V @ g @ big, V @ g @ small) for g in G]
    draw_units(cx, 4.1, scale, units, rb=rb)
    bio.label(ax, (cx, 7.15), name, size="normal", bold=True)
    bio.label(ax, (cx, 0.75), desc, size="tiny", color=P.muted())
    assert N == {"C": 5, "D": 8, "T": 12, "O": 24, "I": 60}[name[0]]

# helical array viewed from the side: 3.5 subunits per turn
cx = 2.6 + 4.6 * 5
twist, rise, r = 2 * np.pi / 3.5, 0.40, 0.95
units = []
for k in range(13):
    th = k * twist
    y = (k - 6) * rise
    b = np.array([r * np.cos(th), y, r * np.sin(th)])
    th2 = th + 0.35
    sm = np.array([1.2 * r * np.cos(th2), y + 0.18, 1.2 * r * np.sin(th2)])
    units.append((b, sm))
draw_units(cx, 4.1, 1.0, units, rb=0.30, highlight=6, tok="enzyme")
ax.plot([cx, cx], [4.1 - 3.2, 4.1 + 3.2], color=P.muted(), lw=0.6, ls=":", zorder=2)
bio.label(ax, (cx, 7.15), "helical", size="normal", bold=True)
bio.label(ax, (cx, 0.75), "3.5 subunits per turn, open-ended", size="tiny", color=P.muted())
