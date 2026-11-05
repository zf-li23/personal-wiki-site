"""The three basic growth forms of lichens (schematic). A: crustose thallus on rock with apothecia.
B: foliose thallus with lobes, apothecia and soralia; side view with rhizines. C: fruticose lichens:
an erect Cladonia (cup-shaped podetia) and a pendent Usnea on a twig."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 12)
rng = np.random.default_rng(7)
TH, APO = "highlight", "chromatin"


def blob(c, r, k=11, wob=0.18, seed=0):
    return bio.blob(c, r, r * 0.85, wobble=wob, seed=seed, k=k)


# A crustose
bio.panel(ax, "A", (0.2, 11.8))
rock = np.array([[0.6, 1.4], [9.2, 1.0], [9.6, 8.6], [5.0, 9.6], [0.8, 8.8]])
ax.add_patch(Polygon(rock, closed=True, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=1.0, zorder=2))
for c, r, s in [((3.0, 5.6), 2.0, 1), ((6.6, 4.0), 1.6, 2), ((6.8, 7.2), 1.1, 3)]:
    bio.shape(ax, blob(c, r, seed=s), token=TH, zorder=4)
    for k in range(int(9 * r)):
        a = rng.uniform(0, 2 * np.pi); rr = rng.uniform(0, 0.75 * r)
        ax.add_patch(Circle((c[0] + rr * np.cos(a), c[1] + rr * np.sin(a)), 0.13, facecolor=P.fill(APO),
                            edgecolor=P.edge(APO), lw=0.4, zorder=5))
bio.callout(ax, (3.6, 6.4), (2.0, 10.6), "Thallus adheres to rock")
bio.callout(ax, (6.3, 4.2), (8.4, 10.6), "Apothecia")
bio.label(ax, (5.0, 0.4), "Crustose", size="small")

# B foliose
bio.panel(ax, "B", (10.4, 11.8))
cx, cy = 15.0, 7.4
ang = np.linspace(0, 2 * np.pi, 400)
r = 2.6 + 0.6 * np.abs(np.sin(4 * ang)) ** 0.6 + 0.15 * np.sin(23 * ang)
ax.add_patch(Polygon(np.c_[cx + r * np.cos(ang), cy + 0.8 * r * np.sin(ang)], closed=True, facecolor=P.fill("positive"),
                     edgecolor=P.edge("positive"), lw=1.0, zorder=4))
for k in range(8):
    a = k * np.pi / 4 + 0.2
    ax.plot([cx, cx + 2.4 * np.cos(a)], [cy, cy + 1.9 * np.sin(a)], color=P.edge("positive"), lw=0.6, zorder=5)
for xy in [(14.3, 7.9), (15.8, 6.8), (16.2, 8.3)]:
    ax.add_patch(Circle(xy, 0.3, facecolor=P.fill(APO), edgecolor=P.edge(APO), lw=0.6, zorder=6))
for xy in [(13.2, 6.5), (17.4, 7.6)]:
    for j in range(10):
        ax.add_patch(Circle((xy[0] + rng.normal(0, 0.15), xy[1] + rng.normal(0, 0.1)), 0.05, facecolor=P.light("positive"),
                            edgecolor=P.edge("positive"), lw=0.3, zorder=6))
bio.callout(ax, (16.2, 8.3), (16.8, 11.2), "Apothecium")
bio.callout(ax, (13.2, 6.5), (11.0, 10.8), "Soralium")
bio.callout(ax, (17.6, 5.6), (19.6, 4.6), "Lobe")
# side view
y0 = 2.2
ax.plot([11.2, 18.8], [y0 - 0.5, y0 - 0.5], color=P.edge("neutral"), lw=1.6, zorder=3)
xs = np.linspace(11.6, 18.4, 60)
ax.fill_between(xs, y0 + 0.1 * np.sin(xs * 3), y0 + 0.35 + 0.1 * np.sin(xs * 3), color=P.fill("positive"), zorder=4)
for x in np.linspace(12.0, 18.0, 9):
    ax.plot([x, x], [y0, y0 - 0.5], color=P.edge("bone"), lw=1.0, zorder=4)
bio.callout(ax, (15.0, y0 - 0.25), (16.6, 0.8), "Rhizines")
bio.label(ax, (15.0, 0.4), "Foliose", size="small")

# C fruticose
bio.panel(ax, "C", (20.4, 11.8))
gnd = 1.6
ax.plot([20.8, 24.6], [gnd, gnd], color=P.edge("neutral"), lw=1.6, zorder=3)
for x0, h in [(21.6, 4.6), (22.8, 5.8), (23.9, 4.0)]:
    stalk = np.array([[x0 - 0.14, gnd], [x0 - 0.12, gnd + h - 0.8], [x0 - 0.6, gnd + h], [x0 + 0.6, gnd + h],
                      [x0 + 0.12, gnd + h - 0.8], [x0 + 0.14, gnd]])
    ax.add_patch(Polygon(stalk, closed=True, facecolor=P.fill(TH), edgecolor=P.edge(TH), lw=0.9, zorder=5))
    for dx in (-0.5, 0.0, 0.5):
        ax.add_patch(Circle((x0 + dx, gnd + h + 0.12), 0.14, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.5, zorder=6))
for k in range(6):
    xs = 21.0 + 0.6 * k
    bio.shape(ax, blob((xs, gnd + 0.15), 0.3, seed=10 + k), token=TH, zorder=4)
bio.callout(ax, (22.8, gnd + 5.9), (24.0, 9.0), "Podetium with\napothecia")
bio.callout(ax, (21.0, gnd + 0.2), (21.0, 0.7), "Squamules")
bio.label(ax, (22.7, 0.2), "Cladonia", size="small", italic=True)
# Usnea hanging from a twig
ax.plot([25.2, 29.8], [10.6, 10.9], color=P.edge("bone"), lw=4.5, zorder=4, solid_capstyle="round")


def branch(p, ang, L, depth):
    q = p + L * np.array([np.cos(ang), np.sin(ang)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(TH), lw=1.4 if depth < 2 else 0.8, zorder=5, solid_capstyle="round")
    if depth < 4:
        for d in (-0.22, 0.18):
            branch(q, ang + d + rng.normal(0, 0.08), L * 0.72, depth + 1)


for x in (26.8, 27.8, 28.8):
    branch(np.array([x, 10.7]), -np.pi / 2 + rng.normal(0, 0.05), 1.9, 0)
bio.label(ax, (27.6, 2.6), "Usnea", size="small", italic=True)
bio.label(ax, (25.2, 0.2), "Fruticose", size="small")
