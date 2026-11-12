# Anatomy of a freshwater planarian (Dugesia), dorsal view, schematic: A, digestive system; B, excretory
# (left half) and nervous systems; C, hermaphroditic reproductive system.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, Polygon

P = bio.P
fig, ax = bio.canvas(27, 12.8)
SX, SY, CY = 2.2, 5.0, 6.2
RIGHT = [(0, -1), (0.2, -0.9), (0.38, -0.6), (0.47, -0.2), (0.48, 0.3), (0.42, 0.58), (0.3, 0.68), (0.5, 0.78),
         (0.36, 0.86), (0.18, 0.95), (0, 1.0)]


def outline():
    pts = np.array(RIGHT + [(-x, y) for x, y in RIGHT[-2:0:-1]], float)
    return bio.smooth_closed(pts, n=400)


def T(cx, x, y):
    return cx + np.asarray(x) * SX, CY + np.asarray(y) * SY


def body(cx):
    o = outline()
    X, Y = T(cx, o[:, 0], o[:, 1])
    ax.add_patch(Polygon(np.c_[X, Y], closed=True, facecolor=P.mix(P.fill("animal"), P.surface(), 0.5),
                         edgecolor=P.edge("animal"), lw=1.1, zorder=3))
    for sx in (-1, 1):  # eyes
        x, y = T(cx, sx * 0.11, 0.84)
        ax.add_patch(Ellipse((x, y), 0.32, 0.22, facecolor=P.surface(), edgecolor=P.ink(), lw=0.8, zorder=9))
        ax.add_patch(Circle((x - sx * 0.04, y), 0.07, facecolor=P.ink(), edgecolor="none", zorder=10))


def line(cx, pts, color, lw, z=6):
    pts = np.asarray(pts, float)
    X, Y = T(cx, pts[:, 0], pts[:, 1])
    ax.plot(X, Y, color=color, lw=lw, solid_capstyle="round", zorder=z)


# ------------------------------------------------ A: gut
cx = 4.6
bio.panel(ax, "A", (0.3, 12.6))
body(cx)
G = P.fill("endoderm")
GE = P.edge("endoderm")
line(cx, [(0, 0.12), (0, 0.72)], GE, 7.5)
line(cx, [(0, 0.12), (0, 0.72)], G, 5.5, z=6.1)
for y in np.linspace(0.22, 0.66, 5):
    for sx in (-1, 1):
        line(cx, [(0, y), (sx * 0.2, y + 0.04), (sx * 0.3, y + 0.03)], GE, 4.5)
        line(cx, [(0, y), (sx * 0.2, y + 0.04), (sx * 0.3, y + 0.03)], G, 2.8, z=6.1)
for sx in (-1, 1):
    pp = [(0, 0.12), (sx * 0.2, 0.06), (sx * 0.22, -0.4), (sx * 0.14, -0.88)]
    line(cx, pp, GE, 7.0)
    line(cx, pp, G, 5.0, z=6.1)
    for y in np.linspace(-0.82, -0.02, 7):
        x0 = sx * (0.22 if y > -0.5 else 0.2)
        q = [(x0, y), (sx * 0.36, y - 0.03)]
        line(cx, q, GE, 4.0)
        line(cx, q, G, 2.4, z=6.1)
x, y = T(cx, 0, -0.06)
ax.add_patch(Ellipse((x, y), 0.95, 2.5, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.4), edgecolor=P.edge("neutral"), lw=0.8, zorder=7))
ax.add_patch(Ellipse((x, y), 0.55, 2.2, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.9, zorder=8))
mx, my = T(cx, 0, -0.32)
ax.add_patch(Circle((mx, my), 0.12, facecolor=P.surface(), edgecolor=P.ink(), lw=0.9, zorder=9))
bio.callout(ax, T(cx, 0, 0.5), (cx + 2.4, 11.0), "Anterior gut branch", size="small")
bio.callout(ax, (x + 0.25, y + 0.3), (cx + 2.4, 7.6), "Plicate pharynx\nin its pocket", size="small")
bio.callout(ax, (mx, my), (cx + 2.4, 4.0), "Mouth (ventral)", size="small")
bio.callout(ax, T(cx, -0.2, -0.6), (0.7, 2.2), "Posterior\nbranches", size="small")
bio.callout(ax, T(cx, -0.11, 0.84), (0.7, 11.3), "Eye", size="small")
bio.callout(ax, T(cx, -0.5, 0.78), (0.7, 10.0), "Auricle", size="small")

# ------------------------------------------------ B: excretory and nervous systems
cx = 13.4
bio.panel(ax, "B", (9.0, 12.6))
body(cx)
NE = P.edge("neuron")
for sx in (-1, 1):
    x, y = T(cx, sx * 0.09, 0.76)
    ax.add_patch(Ellipse((x, y), 0.7, 0.75, facecolor=P.fill("neuron"), edgecolor=NE, lw=0.9, zorder=8))
    line(cx, [(sx * 0.12, 0.72), (sx * 0.17, 0.3), (sx * 0.17, -0.5), (sx * 0.08, -0.95)], NE, 2.0, z=7)
for y in np.linspace(-0.85, 0.6, 13):
    line(cx, [(-0.17, y), (0.17, y)], NE, 0.9, z=7)
EX = P.edge("vesicle")
for xo in (-0.34, -0.29):
    line(cx, [(xo, 0.62), (xo - 0.02, 0.0), (xo + 0.02, -0.85)], EX, 1.3, z=7.5)
for y in np.linspace(-0.75, 0.5, 9):
    line(cx, [(-0.31, y), (-0.42, y + 0.04)], EX, 0.8, z=7.5)
    x, yy = T(cx, -0.42, y + 0.04)
    ax.add_patch(Polygon([(x, yy), (x - 0.16, yy + 0.09), (x - 0.16, yy - 0.09)], facecolor=P.fill("vesicle"), edgecolor=EX, lw=0.6, zorder=8))
# inset: one flame cell
ix, iy = 9.9, 2.0
ax.add_patch(Circle((ix, iy), 1.0, facecolor=P.surface(), edgecolor=P.muted(), lw=0.8, zorder=11))
ax.add_patch(Polygon([(ix - 0.7, iy + 0.25), (ix + 0.1, iy + 0.12), (ix + 0.75, iy + 0.1), (ix + 0.75, iy - 0.1),
                      (ix + 0.1, iy - 0.12), (ix - 0.7, iy - 0.25)], facecolor=P.fill("vesicle"), edgecolor=EX, lw=0.8, zorder=12))
ax.add_patch(Circle((ix - 0.55, iy), 0.22, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=13))
for k in range(5):
    t = np.linspace(0, 1, 20)
    ax.plot(ix - 0.25 + 0.7 * t, iy - 0.06 + 0.03 * k + 0.03 * np.sin(t * 9 + k), color=P.ink(), lw=0.6, zorder=13)
ax.plot([T(cx, -0.42, 0.04)[0] - 0.2, ix + 0.6], [T(cx, -0.42, 0.04)[1], iy + 0.95], color=P.muted(), lw=0.6, zorder=10)
bio.label(ax, (ix, iy - 1.25), "Flame cell", size="small")
bio.callout(ax, T(cx, 0.09, 0.78), (cx + 2.6, 11.0), "Brain (cerebral ganglia)", size="small")
bio.callout(ax, T(cx, 0.17, 0.1), (cx + 2.6, 8.2), "Ventral nerve cord", size="small")
bio.callout(ax, T(cx, 0, -0.29), (cx + 2.6, 5.6), "Transverse commissure", size="small")
bio.callout(ax, T(cx, -0.335, 0.4), (9.4, 10.0), "Protonephridial\ncanals", size="small")

# ------------------------------------------------ C: reproductive system
cx = 22.6
bio.panel(ax, "C", (18.2, 12.6))
body(cx)
rng = np.random.default_rng(4)
for sx in (-1, 1):
    for y in np.linspace(-0.25, 0.6, 9):
        x, yy = T(cx, sx * (0.3 + rng.uniform(-0.03, 0.03)), y)
        ax.add_patch(Circle((x, yy), 0.17, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.6, zorder=8))
    for y in np.linspace(-0.66, 0.55, 14):
        x, yy = T(cx, sx * (0.37 + rng.uniform(-0.015, 0.015) - (0.06 if y < -0.5 else 0)), y)
        ax.add_patch(Circle((x, yy), 0.07, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.4, zorder=8))
    x, yy = T(cx, sx * 0.16, 0.64)
    ax.add_patch(Ellipse((x, yy), 0.42, 0.5, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=8))
    line(cx, [(sx * 0.16, 0.6), (sx * 0.2, 0.1), (sx * 0.06, -0.42)], P.edge("negative"), 1.1, z=7)   # oviducts
    line(cx, [(sx * 0.24, 0.55), (sx * 0.24, -0.1), (sx * 0.05, -0.38)], P.edge("dna"), 1.1, z=7)     # sperm ducts
x, y = T(cx, 0, -0.43)
ax.add_patch(Ellipse((x, y), 0.6, 0.8, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"), lw=0.9, zorder=9))
xb, yb = T(cx, 0, -0.58)
ax.add_patch(Ellipse((xb, yb), 0.5, 0.45, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.9, zorder=9))
gx, gy = T(cx, 0, -0.5)
ax.add_patch(Circle((gx + 0.42, gy), 0.08, facecolor=P.surface(), edgecolor=P.ink(), lw=0.8, zorder=10))
bio.callout(ax, T(cx, 0.16, 0.64), (cx + 2.5, 11.0), "Ovary", size="small")
bio.callout(ax, T(cx, 0.3, 0.3), (cx + 2.5, 9.2), "Testes", size="small")
bio.callout(ax, T(cx, 0.4, -0.2), (cx + 2.5, 7.0), "Vitellaria (yolk glands)", size="small")
bio.callout(ax, (x + 0.25, y), (cx + 2.5, 4.4), "Penis", size="small")
bio.callout(ax, (xb + 0.2, yb - 0.1), (cx + 2.5, 3.0), "Copulatory bursa", size="small")
bio.callout(ax, (gx + 0.42, gy), (cx + 2.5, 5.6), "Gonopore", size="small")
bio.callout(ax, T(cx, -0.235, -0.05), (18.5, 7.0), "Sperm duct", size="small")
bio.callout(ax, T(cx, -0.18, 0.4), (18.5, 9.0), "Oviduct", size="small")
