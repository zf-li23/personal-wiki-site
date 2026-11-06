# Fruits of Sapindaceae s.l. A: Acer, a double samara (schizocarp of two winged mericarps).
# B: Dipteronia, each mericarp with a circular wing and the seed in the centre. C: Koelreuteria,
# an inflated, papery, three-valved capsule (one valve cut away to show the seeds). D: Litchi in
# section: warty pericarp, the fleshy white aril around the seed.
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 11)


def wing(base, angle, length, width, token="plant"):
    """A samara wing: a curved, rounded blade from ``base`` in direction ``angle`` (deg)."""
    t = np.linspace(0, np.pi, 50)
    u = np.r_[np.linspace(0, 1, 50), np.linspace(1, 0, 50)]
    v = np.r_[width * np.sin(t) ** 0.7 * (0.35 + 0.65 * np.linspace(0, 1, 50)),
              -0.25 * width * np.sin(t)[::-1] * np.linspace(1, 0, 50)]
    pts = np.c_[u * length, v]
    a = np.radians(angle)
    R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    bio.shape(ax, pts @ R.T + base, token=token, lw=1.0, zorder=5)
    for k in range(6):
        f = 0.15 + 0.13 * k
        q = np.array([[0.05 * length, 0], [f * length, 0.75 * width * f]]) @ R.T + base
        ax.plot(*q.T, color=P.edge(token), lw=0.5, zorder=6)


# A: Acer
bio.panel(ax, "A", (0.3, 10.8))
c = np.array([4.0, 4.4])
ax.plot([c[0], c[0]], [c[1] - 2.4, c[1]], color=P.edge("plant"), lw=1.6, zorder=4)
for s, ang in ((-1, 150), (1, 30)):
    wing(c + (s * 0.35, 0.1), ang, 4.0, 1.2)
    ax.add_patch(Ellipse(c + (s * 0.45, 0.05), 0.9, 0.7, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.9, zorder=7))
bio.label(ax, (4.0, 9.4), "Acer", italic=True, size="title")
bio.label(ax, (4.0, 8.6), "double samara", size="small")
bio.callout(ax, c + (0.45, 0.05), (6.6, 2.4), "Nutlet (seed)")
bio.callout(ax, c + (2.6, 1.9), (7.4, 7.2), "Wing")

# B: Dipteronia
bio.panel(ax, "B", (8.4, 10.8))
for s in (-1, 1):
    cc = np.array([12.0 + s * 1.3, 5.4])
    ax.add_patch(Circle(cc, 1.25, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0, zorder=5))
    ax.add_patch(Ellipse(cc, 0.6, 0.5, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.8, zorder=6))
ax.plot([12.0, 12.0], [2.6, 5.4], color=P.edge("plant"), lw=1.4, zorder=4)
bio.label(ax, (12.0, 9.4), "Dipteronia", italic=True, size="title")
bio.label(ax, (12.0, 8.6), "circular wings", size="small")

# C: Koelreuteria capsule
bio.panel(ax, "C", (15.6, 10.8))
c = np.array([19.6, 4.8])
th = np.linspace(0, 1, 60)
left = np.c_[c[0] - 2.2 * np.sin(np.pi * th) ** 0.9, c[1] - 2.6 + 5.4 * th]
right = np.c_[c[0] + 2.2 * np.sin(np.pi * th[::-1]) ** 0.9, c[1] - 2.6 + 5.4 * th[::-1]]
bio.shape(ax, np.vstack([left, right]), token="sepal", lw=1.1, zorder=4)
mid = np.c_[c[0] + 0.9 * np.sin(np.pi * th) ** 0.9, c[1] - 2.6 + 5.4 * th]
ax.plot(*mid.T, color=P.edge("sepal"), lw=0.9, zorder=5)
for k in range(5):
    f = 0.2 + 0.15 * k
    ax.plot([c[0] - 2.0 * np.sin(np.pi * f), c[0] + 0.8 * np.sin(np.pi * f)],
            [c[1] - 2.6 + 5.4 * f - 0.25, c[1] - 2.6 + 5.4 * f + 0.15], color=P.edge("sepal"), lw=0.4, zorder=5)
# cut-away window with seeds on the central axis
ax.add_patch(Ellipse(c + (1.3, -0.4), 1.4, 2.4, facecolor=P.light("sepal"), edgecolor=P.edge("sepal"), lw=0.8, zorder=6))
ax.plot([c[0] + 1.3, c[0] + 1.3], [c[1] - 1.5, c[1] + 0.7], color=P.edge("sepal"), lw=0.8, zorder=7)
for d in (-0.8, 0.0):
    ax.add_patch(Circle(c + (1.05, d), 0.24, facecolor=P.ink(), edgecolor=P.ink(), zorder=8))
ax.plot([c[0], c[0]], [c[1] - 3.4, c[1] - 2.6], color=P.edge("plant"), lw=1.6, zorder=3)
bio.label(ax, (19.6, 9.4), "Koelreuteria", italic=True, size="title")
bio.label(ax, (19.6, 8.6), "inflated capsule", size="small")
bio.callout(ax, c + (-1.2, 0.8), (16.2, 6.6), "Papery valve")
bio.callout(ax, c + (1.05, 0.0), (23.4, 6.2), "Seed")

# D: Litchi section
bio.panel(ax, "D", (24.2, 10.8))
c = np.array([28.0, 4.8])
ang = np.linspace(0, 2 * np.pi, 140)
r = 2.4 + 0.12 * np.cos(14 * ang)
bio.shape(ax, np.c_[c[0] + r * np.cos(ang), c[1] + 1.05 * r * np.sin(ang)], token="rna", lw=1.0, zorder=4)
ax.add_patch(Ellipse(c, 4.2, 4.5, facecolor=P.surface(), edgecolor=P.edge("rna"), lw=0.6, zorder=5))
ax.add_patch(Ellipse(c, 3.9, 4.2, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=6))
ax.add_patch(Ellipse(c + (0, -0.2), 1.6, 2.4, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.9, zorder=7))
ax.plot([c[0], c[0]], [c[1] - 2.5, c[1] - 3.3], color=P.edge("plant"), lw=1.6, zorder=3)
bio.label(ax, (28.0, 9.4), "Litchi", italic=True, size="title")
bio.label(ax, (28.0, 8.6), "drupe-like fruit with aril", size="small")
bio.callout(ax, c + (-2.35, 0.8), (24.6, 7.4), "Pericarp")
bio.callout(ax, c + (1.4, 0.9), (31.6, 7.4), "Aril")
bio.callout(ax, c + (0.5, -0.4), (31.6, 2.0), "Seed")
