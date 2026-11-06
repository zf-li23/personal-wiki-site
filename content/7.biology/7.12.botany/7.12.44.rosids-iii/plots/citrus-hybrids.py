# Citrus fruit (hesperidium) in cross-section and the hybrid origins of cultivated citrus
# (after Wu et al. 2014, 2018, Nature). A: exocarp with oil glands, white spongy mesocarp,
# membranous endocarp forming segments filled with juice sacs, seeds on the central axis.
# B: four ancestral species and their hybrids.
import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, Wedge

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 13)

# ---------------- A: hesperidium cross-section
bio.panel(ax, "A", (0.3, 12.8))
c = np.array([6.2, 6.4])
R = 4.6
ax.add_patch(Circle(c, R, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.4, zorder=3))
ax.add_patch(Circle(c, R * 0.86, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.6, zorder=4))
n = 10
rng = np.random.default_rng(3)
for k in range(n):
    a0, a1 = 360 / n * k + 2.0, 360 / n * (k + 1) - 2.0
    ax.add_patch(Wedge(c, R * 0.74, 90 - a1, 90 - a0, width=R * 0.6, facecolor=P.fill("petal"),
                       edgecolor=P.edge("petal"), lw=1.0, zorder=5))
    # juice sacs: small ellipses inside the segment
    for j in range(9):
        rr = R * (0.24 + 0.46 * rng.random())
        aa = math.radians(a0 + 3 + (a1 - a0 - 6) * rng.random())
        p = c + rr * np.array([math.sin(aa), math.cos(aa)])
        ax.add_patch(Ellipse(p, 0.42, 0.2, angle=90 - math.degrees(aa), facecolor=P.light("petal"),
                             edgecolor=P.edge("petal"), lw=0.4, zorder=6))
    if k % 3 == 0:
        am = math.radians((a0 + a1) / 2)
        p = c + R * 0.2 * np.array([math.sin(am), math.cos(am)])
        ax.add_patch(Ellipse(p, 0.55, 0.32, angle=90 - math.degrees(am), facecolor=P.fill("ovule"),
                             edgecolor=P.edge("ovule"), lw=0.6, zorder=7))
ax.add_patch(Circle(c, R * 0.12, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.6, zorder=6))
# oil glands in the exocarp
for k in range(36):
    a = math.radians(k * 10 + 4)
    p = c + R * 0.93 * np.array([math.sin(a), math.cos(a)])
    ax.add_patch(Circle(p, 0.13, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.5, zorder=6))
bio.callout(ax, c + R * 0.93 * np.array([math.sin(math.radians(44)), math.cos(math.radians(44))]), (12.6, 12.0), "Exocarp with oil glands")
bio.callout(ax, c + R * 0.8 * np.array([0.98, 0.2]), (12.6, 9.6), "Mesocarp (albedo)")
bio.callout(ax, c + np.array([3.0, -1.6]), (12.6, 7.2), "Endocarp (segment wall)")
bio.callout(ax, c + np.array([1.6, -2.4]), (12.6, 4.8), "Juice sacs")
bio.callout(ax, c + np.array([0.74, -0.54]), (12.6, 2.4), "Seed (axile placentation)")
bio.callout(ax, c + np.array([0.0, 0.3]), (6.2, 0.6), "Central axis")

# ---------------- B: hybrid network
bio.panel(ax, "B", (16.2, 12.8))
anc = {"Pummelo": (18.6, 11.2), "Mandarin": (27.6, 11.2), "Citron": (18.6, 2.0), "Micrantha": (27.6, 2.0)}
sci = {"Pummelo": "C. maxima", "Mandarin": "C. reticulata", "Citron": "C. medica", "Micrantha": "C. micrantha"}
for k, xy in anc.items():
    bio.box(ax, xy, 3.6, 1.1, token="plant", text=k)
    bio.label(ax, (xy[0], xy[1] + (0.95 if xy[1] > 6 else -0.95)), sci[k], size="small", italic=True)
hyb = {"Sour orange": (23.2, 9.9), "Sweet orange": (26.8, 5.6), "Grapefruit": (19.8, 6.0),
       "Lemon": (22.6, 4.1), "Mexican lime": (26.4, 3.9)}
for k, xy in hyb.items():
    bio.box(ax, xy, 3.4, 0.95, token="highlight", text=k, size="small")
E = [("Pummelo", "Sour orange"), ("Mandarin", "Sour orange"), ("Pummelo", "Sweet orange"),
     ("Mandarin", "Sweet orange"), ("Pummelo", "Grapefruit"), ("Sweet orange", "Grapefruit"),
     ("Sour orange", "Lemon"), ("Citron", "Lemon"), ("Citron", "Mexican lime"), ("Micrantha", "Mexican lime")]
pos = {**anc, **hyb}
HALF = {k: (1.8, 0.55) for k in anc}
HALF.update({k: (1.7, 0.48) for k in hyb})


def edge_point(c, d, half, pad=0.12):
    """Point where the ray from box centre c towards d leaves the box (plus a small gap)."""
    c, d = np.asarray(c, float), np.asarray(d, float)
    v = d - c
    t = min((half[0] + pad) / abs(v[0]) if v[0] else 1e9, (half[1] + pad) / abs(v[1]) if v[1] else 1e9)
    return c + t * v


for a, b in E:
    bio.arrow(ax, edge_point(pos[a], pos[b], HALF[a]), edge_point(pos[b], pos[a], HALF[b]), kind="process",
              lw=1.0, color=P.muted(), zorder=5)
bio.arrow(ax, (28.9, 10.5), (28.2, 6.25), kind="process", bend=-0.4, shrink=0.2, lw=0.9, dashed=True, color=P.muted(), zorder=5)
bio.label(ax, (29.4, 9.0), "backcross", size="tiny", rotation=-70)
bio.label(ax, (23.1, 12.6), "Ancestral species (green) and hybrids (orange)", size="small")
