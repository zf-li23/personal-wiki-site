# Structure of grass spikelets and florets (schematic). A: a many-flowered (wheat-type) spikelet in
# side view: two glumes at the base of the rachilla, florets alternating above, the uppermost sterile.
# B: one floret dissected: awned lemma, two-keeled palea, two lodicules, three versatile stamens and a
# pistil with two feathery stigmas. C: floral diagram of the floret: lemma abaxial (below), palea
# adaxial (above), two lodicules, three stamens, unilocular ovary. D: rice spikelet: two minute
# rudimentary glumes on the pedicel tip, two sterile lemmas and one fertile floret with six stamens.
import numpy as np
from matplotlib.patches import PathPatch, Ellipse, Circle
from matplotlib.path import Path
import wikibio as bio
from wikibio import plant
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(34, 13)


def boat(base, L, W, ang, token, z=5, awn=0.0, lw=1.1):
    a = np.radians(ang)
    u = np.array([np.cos(a), np.sin(a)])
    v = np.array([-u[1], u[0]])
    pts = [base + v * W * 0.15, base + u * L * 0.35 + v * W * 0.5, base + u * L * 0.8 + v * W * 0.3, base + u * L,
           base + u * L * 0.8 - v * W * 0.3, base + u * L * 0.35 - v * W * 0.5, base - v * W * 0.15]
    ax.add_patch(PathPatch(Path(smooth_closed(pts, n=80), closed=True), facecolor=P.fill(token), edgecolor=P.edge(token),
                           lw=lw, zorder=z))
    ax.plot(*np.array([base, base + u * L * 0.95]).T, color=P.edge(token), lw=0.6, zorder=z + 1)
    if awn:
        tip = base + u * L
        ax.plot(*np.array([tip, tip + u * awn]).T, color=P.edge(token), lw=1.0, zorder=z + 1)
    return base + u * L * 0.5


def anther(p, s=0.5, z=8):
    ax.add_patch(Ellipse(p, s * 0.45, s * 1.2, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9, zorder=z))


# ---- A: spikelet
bio.panel(ax, "A", (0.3, 12.7))
bio.label(ax, (4.2, 12.6), "Spikelet (side view)", size="title")
x0 = 4.2
ax.plot([x0, x0 + 0.15, x0 - 0.1, x0 + 0.1, x0 - 0.05, x0], [1.2, 3.0, 4.6, 6.2, 7.8, 9.2], color=P.edge("neutral"), lw=1.4, zorder=3)
g1 = boat(np.array([x0, 1.6]), 3.0, 1.1, 112, "bract", z=4)
g2 = boat(np.array([x0, 1.9]), 3.1, 1.1, 68, "bract", z=4)
fl = []
for k, (y, side) in enumerate([(2.8, -1), (4.3, 1), (5.8, -1), (7.3, 1)]):
    ang = 90 + side * 26
    fl.append(boat(np.array([x0, y]), 3.0 - 0.25 * k, 1.2, ang, "plant", z=5 + k, awn=1.8 - 0.3 * k))
boat(np.array([x0, 8.7]), 1.1, 0.5, 90, "neutral", z=10)
bio.callout(ax, g1, (0.6, 1.6), "First glume")
bio.callout(ax, g2, (8.0, 1.6), "Second glume")
bio.callout(ax, fl[0], (0.6, 5.2), "Floret (lemma)")
bio.callout(ax, (3.05, 9.85), (8.0, 11.6), "Awn")
bio.callout(ax, (x0, 9.3), (0.6, 10.2), "Sterile floret")
bio.callout(ax, (x0 + 0.12, 3.6), (8.0, 4.0), "Rachilla")

# ---- B: dissected floret
bio.panel(ax, "B", (9.8, 12.7))
bio.label(ax, (14.6, 12.6), "Floret, dissected", size="title")
lm = boat(np.array([11.2, 2.0]), 6.0, 1.9, 90, "plant", awn=3.0)
pa = boat(np.array([13.3, 2.0]), 5.2, 1.5, 90, "plant")
ax.plot([13.0, 13.05], [2.4, 6.9], color=P.edge("plant"), lw=1.0, zorder=7)
ax.plot([13.6, 13.55], [2.4, 6.9], color=P.edge("plant"), lw=1.0, zorder=7)
for dx in (-0.35, 0.35):
    ax.add_patch(Ellipse((15.4 + dx, 2.5), 0.5, 0.9, facecolor=P.light("tepal"), edgecolor=P.edge("tepal"), lw=0.9, zorder=6))
for k, dx in enumerate((-0.8, 0.0, 0.8)):
    xs = 17.0 + dx
    ax.plot([xs, xs + 0.1 * (k - 1)], [2.0, 6.0], color=P.edge("anther"), lw=0.9, zorder=6)
    anther((xs + 0.1 * (k - 1), 6.4))
ax.add_patch(Ellipse((19.4, 2.8), 0.9, 1.3, facecolor=P.fill("ovary"), edgecolor=P.edge("ovary"), lw=1.0, zorder=6))
for s in (-1, 1):
    base = np.array([19.4 + 0.2 * s, 3.4])
    for t in np.linspace(0, 1, 9):
        p = base + np.array([s * 0.9 * t, 2.2 * t])
        ax.plot([p[0], p[0] + s * 0.25], [p[1], p[1] + 0.15], color=P.edge("ovary"), lw=0.6, zorder=6)
    ax.plot([base[0], base[0] + s * 0.9], [base[1], base[1] + 2.2], color=P.edge("ovary"), lw=1.0, zorder=6)
bio.callout(ax, lm, (10.2, 9.8), "Lemma")
bio.callout(ax, (11.2, 8.4), (10.6, 11.4), "Awn")
bio.callout(ax, pa, (14.4, 9.6), "Palea (two keels)")
bio.callout(ax, (15.4, 2.9), (14.8, 0.6), "Lodicules")
bio.callout(ax, (17.1, 6.6), (17.8, 8.6), "Stamens (versatile)")
bio.callout(ax, (20.2, 5.0), (20.4, 7.4), "Feathery stigmas")
bio.callout(ax, (19.4, 2.4), (19.8, 0.6), "Ovary")

# ---- C: floral diagram
bio.panel(ax, "C", (21.8, 12.7))
bio.label(ax, (24.6, 12.6), "Floret diagram", size="title")
out = plant.floral_diagram(ax, (24.6, 8.2), 2.2, [
    dict(organ="tepal", n=1, phase=0, width=60, r=1.0, token="plant", keel=0.4),
    dict(organ="tepal", n=2, members=[dict(angle=150), dict(angle=210)], width=16, r=0.8, thickness=0.1),
    dict(organ="stamen", n=3, members=[dict(angle=a) for a in (180, 60, 300)], r=0.5),
    dict(organ="gynoecium", n=1, placentation="basal", ovules=1, size=0.22)], symmetry="bilateral")
bio.callout(ax, out["bract"], (27.6, 4.6), "Lemma")
bio.callout(ax, out["whorls"][0][0], (27.6, 11.4), "Palea")
bio.callout(ax, out["whorls"][1][1], (21.9, 5.0), "Lodicule")

# ---- D: rice
bio.panel(ax, "D", (28.2, 12.7))
bio.label(ax, (31.0, 12.6), r"$\it{Oryza}$ spikelet", size="title")
rx = 31.0
ax.plot([rx, rx], [1.0, 2.0], color=P.edge("neutral"), lw=1.4, zorder=3)
for s in (-1, 1):
    ax.add_patch(Ellipse((rx + 0.25 * s, 2.05), 0.3, 0.16, facecolor=P.fill("bract"), edgecolor=P.edge("bract"), lw=0.8, zorder=5))
boat(np.array([rx, 2.2]), 6.0, 2.2, 90, "plant", z=6)
for s in (-1, 1):
    boat(np.array([rx + 0.35 * s, 2.15]), 1.3, 0.45, 90 + 38 * s, "neutral", z=7)
for k, dx in enumerate(np.linspace(-1.0, 1.0, 6)):
    anther((rx + dx * 1.2, 8.8 + 0.25 * (k % 2)), s=0.5, z=9)
    ax.plot([rx + dx * 0.3, rx + dx * 1.2], [6.8, 8.4 + 0.25 * (k % 2)], color=P.edge("anther"), lw=0.7, zorder=8)
bio.callout(ax, (rx - 0.25, 2.05), (28.6, 1.2), "Rudimentary glumes")
bio.callout(ax, (rx + 0.55, 2.9), (32.8, 1.8), "Sterile lemmas")
bio.callout(ax, (rx + 0.6, 5.0), (32.6, 6.6), "Fertile floret")
bio.callout(ax, (rx + 1.2, 9.0), (32.6, 10.6), "6 stamens")
