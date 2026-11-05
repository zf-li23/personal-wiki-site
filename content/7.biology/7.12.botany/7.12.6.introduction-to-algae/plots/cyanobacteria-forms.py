"""Form and specialized cells of cyanobacteria (schematic, not to scale). A: Chroococcus, two hemispherical
cells flattened where they meet, with individual and colonial sheaths. B: Microcystis colony, cells in a
mucilaginous matrix (dark dots: gas vacuoles). C: Merismopedia, a flat plate of cells in groups of four.
D: Oscillatoria trichome breaking at dead cells (separation discs) into hormogonia. E: Nostoc, moniliform
trichomes in a common sheath, with heterocysts (larger, thick-walled, polar nodules) and akinetes.
F: Anabaena, no common sheath. G: Scytonema, paired false branches. H: Stigonema, true branching."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle, FancyBboxPatch
import wikibio as bio

P = bio.P
rng = np.random.default_rng(3)
fig, ax = bio.canvas(32, 15)
CY = "bacterium"
SH = "extracellular"


def c(xy, r, tok=CY, lw=1.0, z=5):
    ax.add_patch(Circle(xy, r, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=lw, zorder=z))


def hetero(xy, r):
    ax.add_patch(Circle(xy, r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(CY), lw=2.2, zorder=6))


def akinete(xy, rx, ry, ang=0):
    ax.add_patch(Ellipse(xy, 2 * rx, 2 * ry, angle=ang, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.6, zorder=6))


def head(x, y, L, t):
    bio.panel(ax, L, (x, y))
    bio.label(ax, (x + 0.6, y - 0.2), t, size="small", italic=True, ha="left", va="top")


# A Chroococcus
head(0.2, 14.8, "A", "Chroococcus")
ax.add_patch(Ellipse((3.6, 11.0), 4.2, 3.0, facecolor=P.fill(SH), edgecolor=P.muted(), lw=1.0, zorder=3))
for dx in (-0.62, 0.62):
    ax.add_patch(Ellipse((3.6 + dx * 1.15, 11.0), 1.9, 2.3, facecolor="none", edgecolor=P.muted(), lw=0.8, zorder=4))
    t = np.linspace(-np.pi / 2, np.pi / 2, 50)
    sgn = np.sign(dx)
    xs = 3.6 + sgn * 0.08 + sgn * 0.8 * np.cos(t)
    ys = 11.0 + 0.9 * np.sin(t)
    ax.fill(np.r_[xs, 3.6 + sgn * 0.08], np.r_[ys, 11.0 - 0.9], facecolor=P.light(CY), edgecolor=P.edge(CY), lw=1.1, zorder=5)
bio.label(ax, (3.6, 9.0), "individual and colonial sheaths", size="tiny", color=P.muted())

# B Microcystis
head(8.2, 14.8, "B", "Microcystis")
t = np.linspace(0, 2 * np.pi, 80)
rr = 1 + 0.18 * np.sin(3 * t + 1) + 0.1 * np.cos(5 * t)
ax.fill(11.6 + 2.3 * rr * np.cos(t), 11.0 + 1.7 * rr * np.sin(t), facecolor=P.fill(SH), edgecolor=P.muted(), lw=1.0, zorder=3)
for _ in range(90):
    r, a = np.sqrt(rng.random()) * 0.92, 2 * np.pi * rng.random()
    q = (11.6 + 2.1 * r * np.cos(a), 11.0 + 1.5 * r * np.sin(a))
    c(q, 0.13)
    ax.add_patch(Circle(q, 0.05, color=P.ink(), zorder=6))
bio.label(ax, (11.6, 9.0), "gas vacuoles (dark)", size="tiny", color=P.muted())

# C Merismopedia
head(16.2, 14.8, "C", "Merismopedia")
for i in range(4):
    for j in range(4):
        for di in (0, 1):
            for dj in (0, 1):
                c((17.4 + i * 1.05 + di * 0.4, 9.7 + j * 1.05 + dj * 0.4), 0.17)
bio.label(ax, (19.4, 9.0), "plate; cells in fours", size="tiny", color=P.muted())

# D Oscillatoria
head(24.2, 14.8, "D", "Oscillatoria")
x = 24.8
for k in range(20):
    tok = CY
    xx = x + k * 0.33
    if k in (7, 14):
        ax.add_patch(Rectangle((xx, 10.75), 0.3, 0.6, facecolor=P.fill("neutral"), edgecolor=P.muted(), lw=0.8, zorder=5))
        continue
    ax.add_patch(Rectangle((xx, 10.75), 0.3, 0.6, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=0.8, zorder=5))
bio.callout(ax, (x + 7 * 0.33 + 0.15, 10.75), (x + 1.4, 9.6), "dead cell (separation disc)", size="tiny")
bio.label(ax, (x + 1.15, 11.9), "hormogonium", size="tiny")
bio.label(ax, (x + 3.45, 11.9), "hormogonium", size="tiny")
bio.arrow(ax, (x + 4.8, 12.5), (x + 6.4, 12.5), kind="process", head=0.12)
bio.label(ax, (x + 5.6, 12.85), "gliding", size="tiny", color=P.muted())

# E Nostoc
head(0.2, 7.2, "E", "Nostoc")
ax.add_patch(Ellipse((3.8, 3.6), 6.6, 4.4, facecolor=P.fill(SH), edgecolor=P.muted(), lw=1.0, zorder=3))
for row, (y0, ph) in enumerate(((4.6, 0), (3.4, 1.2), (2.3, 2.4))):
    xs = np.arange(1.2, 6.5, 0.36)
    for k, xx in enumerate(xs):
        yy = y0 + 0.25 * np.sin(xx * 1.3 + ph)
        if (k + row * 3) % 9 == 4:
            hetero((xx, yy), 0.22)
        elif row == 2 and k in (2, 3):
            akinete((xx, yy), 0.24, 0.17)
        else:
            c((xx, yy), 0.16)
bio.callout(ax, (2.64, 4.48), (1.2, 6.2), "heterocyst", size="tiny")
bio.callout(ax, (2.0, 2.4), (0.9, 1.0), "akinete", size="tiny")
bio.label(ax, (5.6, 1.0), "common gelatinous sheath", size="tiny", color=P.muted())

# F Anabaena
head(8.2, 7.2, "F", "Anabaena")
xs = np.arange(8.8, 15.6, 0.38)
for k, xx in enumerate(xs):
    yy = 3.6 + 0.6 * np.sin(xx * 0.8)
    if k == 8:
        hetero((xx, yy), 0.23)
    elif k == 9:
        akinete((xx + 0.1, yy), 0.3, 0.19, ang=20)
    else:
        c((xx, yy), 0.17)
bio.label(ax, (12.0, 1.6), "no common sheath; akinete next\nto heterocyst (some species)", size="tiny", color=P.muted())

# G Scytonema: false branching
head(16.2, 7.2, "G", "Scytonema")
ax.plot([17.0, 19.3], [3.4, 3.4], color=P.muted(), lw=10, solid_capstyle="round", zorder=3, alpha=0.5)
for k, xx in enumerate(np.arange(17.0, 19.3, 0.32)):
    ax.add_patch(Rectangle((xx - 0.13, 3.25), 0.28, 0.3, facecolor=P.light(CY), edgecolor=P.edge(CY), lw=0.7, zorder=5))
for sgn in (1, -1):
    pts = [(19.3 + 0.32 * k * 0.8 + 0.1, 3.4 + sgn * (0.25 + 0.32 * k * 0.6)) for k in range(7)]
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=P.muted(), lw=10, solid_capstyle="round", zorder=3, alpha=0.5)
    for q in pts:
        ax.add_patch(Circle(q, 0.14, facecolor=P.light(CY), edgecolor=P.edge(CY), lw=0.7, zorder=5))
bio.label(ax, (19.6, 0.9), "two trichomes break out of the sheath\n(false branches)", size="tiny", color=P.muted())

# H Stigonema: true branching
head(24.2, 7.2, "H", "Stigonema")
main = [(25.2 + 0.0, 1.6 + 0.36 * k) for k in range(12)]
for q in main:
    for dx in (-0.15, 0.15):
        ax.add_patch(Rectangle((q[0] + dx - 0.15, q[1] - 0.15), 0.3, 0.3, facecolor=P.light(CY), edgecolor=P.edge(CY), lw=0.7, zorder=5))
for k0, sgn in ((4, 1), (8, 1)):
    q0 = main[k0]
    for k in range(1, 9):
        q = (q0[0] + 0.15 + 0.34 * k, q0[1] + 0.12 * k)
        ax.add_patch(Rectangle((q[0] - 0.15, q[1] - 0.15), 0.3, 0.3, facecolor=P.light(CY), edgecolor=P.edge(CY), lw=0.7, zorder=5))
bio.label(ax, (27.6, 0.9), "lateral division of a cell gives a true branch;\nmultiseriate main axis", size="tiny", color=P.muted())
