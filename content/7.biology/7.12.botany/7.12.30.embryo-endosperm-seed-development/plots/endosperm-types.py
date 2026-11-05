"""Three modes of endosperm development, embryo sacs in longitudinal section with the micropylar end on
the left (zygote or young embryo there). Top: nuclear endosperm (free nuclei along the wall around a
large central vacuole, then cellularization from the periphery). Middle: cellular endosperm (every
division followed by a wall). Bottom: helobial endosperm (the first division forms a transverse wall
separating a large micropylar chamber from a small chalazal chamber; free-nuclear divisions in both;
the micropylar chamber later becomes cellular).
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 13.0)
A, B = 2.7, 1.15  # half-axes of the embryo sac
rng = np.random.default_rng(4)


def sac(c):
    ax.add_patch(Ellipse(c, 2 * A, 2 * B, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.0, zorder=4))
    # zygote at the micropylar end
    ax.add_patch(Circle((c[0] - A + 0.35, c[1]), 0.22, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"),
                        lw=0.8, zorder=8))


def nuc(p, r=0.07):
    ax.add_patch(Circle(p, r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.5, zorder=9))


def vacuole(c, sx=0.78, sy=0.6):
    ax.add_patch(Ellipse(c, 2 * A * sx, 2 * B * sy, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.6,
                         zorder=5))


def wall(pts, lw=0.8):
    pts = np.asarray(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge("cell_wall"), lw=lw, zorder=7)


def rim(c, n, f=0.88, skip=0.0):
    """Points along the inner rim of the sac (avoiding the zygote end)."""
    t = np.linspace(0, 2 * np.pi, n, endpoint=False) + 0.1
    pts = np.c_[c[0] + A * f * np.cos(t), c[1] + B * f * np.sin(t)]
    return [p for p in pts if p[0] > c[0] - A + 0.75 + skip]


xs = [5.0, 12.4, 19.8]
rows = [(10.6, "Nuclear"), (6.4, "Cellular"), (2.2, "Helobial")]
for y, name in rows:
    bio.label(ax, (0.3, y + 1.7), name, size="title", ha="left")

# nuclear type
y = rows[0][0]
c = (xs[0], y)
sac(c)
vacuole(c)
for p in rim(c, 10):
    nuc(p)
c = (xs[1], y)
sac(c)
vacuole(c, 0.72, 0.55)
for p in rim(c, 34, 0.84):
    nuc(p, 0.06)
c = np.array((xs[2], y))
sac(c)
vacuole(c, 0.62, 0.42)
t = np.linspace(0, 2 * np.pi, 36, endpoint=False)
for k in range(36):
    a = c + np.array([A * 0.62 * np.cos(t[k]), B * 0.42 * np.sin(t[k])])
    b = c + np.array([A * np.cos(t[k]), B * np.sin(t[k])])
    if b[0] > c[0] - A + 0.7:
        wall([a, b], 0.6)
for p in rim(c, 36, 0.81):
    nuc(p, 0.05)
bio.label(ax, (xs[0], y - 1.55), "Free nuclei along the wall", size="small")
bio.label(ax, (xs[1], y - 1.55), "More free nuclei; central vacuole", size="small")
bio.label(ax, (xs[2], y - 1.55), "Cellularization from the periphery", size="small")

# cellular type
y = rows[1][0]
for i, nx in enumerate((2, 4, 7)):
    c = np.array((xs[i], y))
    sac(c)
    x0, x1 = c[0] - A + 0.7, c[0] + A
    edges = np.linspace(x0, x1, nx + 1)
    for e in edges[1:-1]:
        h = B * np.sqrt(max(0.0, 1 - ((e - c[0]) / A) ** 2))
        wall([(e, c[1] - h), (e, c[1] + h)])
    if i == 2:  # longitudinal walls as well
        for yy in (-0.4, 0.4):
            xx = np.linspace(x0, c[0] + A * 0.92, 30)
            wall(np.c_[xx, np.full_like(xx, c[1] + yy)], 0.6)
    for a, b in zip(edges[:-1], edges[1:]):
        m = 0.5 * (a + b)
        ys = [c[1]] if i < 2 else [c[1] - 0.7, c[1], c[1] + 0.7]
        for yy in ys:
            if abs(yy - c[1]) < B * np.sqrt(max(0.0, 1 - ((m - c[0]) / A) ** 2)) - 0.12:
                nuc((m, yy))
bio.label(ax, (xs[0], y - 1.55), "First division: a wall", size="small")
bio.label(ax, (xs[1], y - 1.55), "Each division with a wall", size="small")
bio.label(ax, (xs[2], y - 1.55), "Cellular throughout", size="small")

# helobial type
y = rows[2][0]
for i in range(3):
    c = np.array((xs[i], y))
    sac(c)
    xw = c[0] + A * 0.55
    h = B * np.sqrt(1 - 0.55 ** 2)
    wall([(xw, c[1] - h), (xw, c[1] + h)], 1.1)
    if i == 0:
        nuc((c[0] - 0.4, c[1]))
        nuc((xw + 0.55, c[1]))
    elif i == 1:
        vacuole((c[0] - 0.35, c[1]), 0.45, 0.5)
        for p in rim(c, 26, 0.84):
            if p[0] < xw - 0.1:
                nuc(p, 0.06)
        for p in [(xw + 0.45, c[1] + 0.25), (xw + 0.7, c[1] - 0.2), (xw + 0.4, c[1] - 0.3), (xw + 0.75, c[1] + 0.2)]:
            nuc(p, 0.06)
    else:
        x0 = c[0] - A + 0.7
        for e in np.linspace(x0, xw, 6)[1:-1]:
            hh = B * np.sqrt(max(0.0, 1 - ((e - c[0]) / A) ** 2))
            wall([(e, c[1] - hh), (e, c[1] + hh)], 0.6)
        xx = np.linspace(x0, xw, 20)
        wall(np.c_[xx, np.full_like(xx, c[1])], 0.6)
        for e in np.linspace(x0, xw, 6)[:-1] + (xw - x0) / 10:
            for yy in (c[1] - 0.45, c[1] + 0.45):
                nuc((e, yy), 0.06)
        for p in [(xw + 0.45, c[1] + 0.25), (xw + 0.7, c[1] - 0.2), (xw + 0.4, c[1] - 0.3), (xw + 0.75, c[1] + 0.2)]:
            nuc(p, 0.06)
bio.callout(ax, (xs[0] + A * 0.55, y + 0.6), (xs[0] + 2.2, y + 1.75), "Transverse wall")
bio.label(ax, (xs[0] - 0.6, y - 1.55), "Micropylar chamber", size="small")
bio.label(ax, (xs[0] + 2.1, y - 1.55), "Chalazal", size="small")
bio.label(ax, (xs[1], y - 1.55), "Free nuclei in both chambers", size="small")
bio.label(ax, (xs[2], y - 1.55), "Micropylar chamber cellular", size="small")
bio.callout(ax, (xs[0] - A + 0.35, rows[0][0] + 0.2), (xs[0] - A + 1.6, rows[0][0] + 1.75), "Zygote")
for x in xs[:-1]:
    bio.arrow(ax, (x + A + 0.25, 12.4), (x + 7.4 - A - 0.25, 12.4), kind="process", color=P.muted(), lw=0.9)
bio.label(ax, (xs[1], 12.75), "time after fertilization", size="small", color=P.muted())
