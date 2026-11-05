# Ovule types in longitudinal section (funiculus, chalaza, nucellus with embryo sac, inner and outer
# integuments leaving the micropyle). Orthotropous: funiculus, chalaza and micropyle on one straight line.
# Anatropous: the body turned through 180 degrees, the micropyle next to the funiculus, which is fused to the
# outer integument along the raphe. Hemitropous: the body at right angles to the funiculus.
# Campylotropous: the body itself curved, bringing the micropyle near the funiculus. Circinotropous: a long
# funiculus coiled around the ovule.
import numpy as np
from matplotlib.patches import Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 6.6)
L, Wd = 2.6, 1.0   # ovule length (chalaza at y=0, micropyle at y=L) and half-width


def bend_map(pts, bend):
    """Bend local points (x across, y along the axis) around a circle of curvature `bend` (1/units)."""
    if abs(bend) < 1e-9:
        return pts
    R = 1.0 / bend
    th = pts[:, 1] / R
    r = R - pts[:, 0]
    return np.column_stack([R - r * np.cos(th), r * np.sin(th)])


def place(pts, origin, angle):
    t = np.radians(angle)
    rot = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    return pts @ rot.T + np.asarray(origin)


def ovule(origin, angle, bend=0.0):
    def T(p):
        return place(bend_map(np.asarray(p, float), bend), origin, angle)

    def stroke(pts, tok, lw):
        q = T(pts)
        ax.plot(q[:, 0], q[:, 1], color=P.fill(tok), lw=lw, solid_capstyle="round", zorder=6)
        ax.plot(q[:, 0], q[:, 1], color=P.edge(tok), lw=0.6, zorder=7)

    def blob(cx, cy, rx, ry, tok, z):
        t = np.linspace(0, 2 * np.pi, 80)
        q = T(np.column_stack([cx + rx * np.cos(t), cy + ry * np.sin(t)]))
        ax.add_patch(Polygon(q, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z))

    blob(0, 1.3, 0.6, 1.12, "ovule", 8)                 # nucellus
    blob(0, 1.75, 0.24, 0.52, "cytoplasm", 9)             # embryo sac
    # integuments: arcs of an ellipse open at the micropylar end (top)
    for r, tok, lw, gap in ((Wd * 0.98, "plant", 5.0, 0.16), (Wd * 0.78, "sepal", 4.0, 0.1)):
        s = np.linspace(np.pi / 2 + gap * 2.2, np.pi / 2 + 2 * np.pi - gap * 2.2, 120)
        pts = np.column_stack([r * np.cos(s), 1.3 + 1.42 * (r / Wd) * np.sin(s)])
        stroke(pts, tok, lw)
    return T


def funiculus(pts):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.fill("plant"), lw=7, solid_capstyle="round", zorder=5)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge("plant"), lw=0.7, zorder=5)


def mark(T, local, text, off):
    p = T([local])[0]
    bio.callout(ax, p, (p[0] + off[0], p[1] + off[1]), text, size="tiny")


bio.label(ax, (13.5, 6.35), "Ovule types", size="normal", bold=True)
xs = [2.6, 8.0, 13.4, 18.6, 23.8]
base = 1.2
# orthotropous
T = ovule((xs[0], base + 0.6), 0)
funiculus([(xs[0], base - 0.2), (xs[0], base + 0.55)])
mark(T, (0, 2.78), "Micropyle", (1.0, 0.6)); mark(T, (0, 0.1), "Chalaza", (1.3, -0.2)); mark(T, (0, 1.75), "Embryo sac", (-1.9, 1.4))
bio.callout(ax, (xs[0], base), (xs[0] - 1.6, base - 0.3), "Funiculus", size="tiny")
# anatropous: body inverted beside the funiculus
T = ovule((xs[1] + 0.25, base + 3.6), 180)
funiculus([(xs[1] - 0.85, base - 0.2), (xs[1] - 0.85, base + 3.2), (xs[1] - 0.2, base + 3.65)])
mark(T, (0, 2.78), "Micropyle", (0.9, -0.4)); bio.callout(ax, (xs[1] - 0.85, base + 2.0), (xs[1] - 2.1, base + 2.6), "Raphe", size="tiny")
# hemitropous: body at right angles
T = ovule((xs[2] - 1.3, base + 2.3), -90)
funiculus([(xs[2], base - 0.2), (xs[2], base + 1.35)])
mark(T, (0, 2.78), "Micropyle", (0.3, 0.9))
# campylotropous: curved body
T = ovule((xs[3] - 0.6, base + 0.6), -20, bend=0.55)
funiculus([(xs[3] - 0.6, base - 0.2), (xs[3] - 0.6, base + 0.55)])
mark(T, (0, 2.78), "Micropyle", (0.8, -0.8))
# circinotropous: long coiled funiculus
th = np.linspace(-np.pi / 2, 1.55 * np.pi, 80)
coil = np.column_stack([xs[4] + 1.55 * np.cos(th), base + 2.7 + 1.55 * np.sin(th)])
funiculus(np.vstack([[xs[4], base - 0.2], coil]))
T = ovule((xs[4] - 0.1, base + 1.5), 0)
for x, n in zip(xs, ["Orthotropous", "Anatropous", "Hemitropous", "Campylotropous", "Circinotropous"]):
    bio.label(ax, (x, 0.4), n, size="small", bold=True)
