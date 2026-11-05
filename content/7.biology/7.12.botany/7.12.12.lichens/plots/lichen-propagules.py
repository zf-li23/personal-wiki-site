"""Reproductive structures of lichens (schematic sections). A: soralium releasing soredia (photobiont
cells wrapped in hyphae, no cortex). B: isidia (corticate outgrowths with photobiont and hyphae).
C: lecanorine apothecium with a thalline margin containing photobiont cells."""
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 9)
rng = np.random.default_rng(3)
COR, ALG, MED = "bone", "positive", "lipid_tail"


def alga(xy, r=0.13):
    ax.add_patch(Circle(xy, r, facecolor=P.fill(ALG), edgecolor=P.edge(ALG), lw=0.5, zorder=8))


def thallus(x0, x1, y0=1.2, gap=None):
    # lower medulla band, algal layer, cortex (with an optional gap)
    ax.add_patch(Rectangle((x0, y0), x1 - x0, 2.15, facecolor=P.light(MED), edgecolor="none", zorder=3))
    for k in range(int((x1 - x0) * 6)):
        x = rng.uniform(x0, x1); y = rng.uniform(y0 + 0.1, y0 + 1.5)
        a = rng.uniform(0, np.pi)
        ax.plot([x, x + 0.3 * np.cos(a)], [y, y + 0.2 * np.sin(a)], color=P.edge(MED), lw=0.6, zorder=4)
    for k in range(int((x1 - x0) * 4)):
        x = rng.uniform(x0 + 0.1, x1 - 0.1)
        if gap and gap[0] < x < gap[1]:
            continue
        alga((x, y0 + 1.85 + rng.uniform(-0.1, 0.1)))
    segs = [(x0, x1)] if not gap else [(x0, gap[0]), (gap[1], x1)]
    for a, b in segs:
        ax.add_patch(Rectangle((a, y0 + 2.1), b - a, 0.45, facecolor=P.fill(COR), edgecolor=P.edge(COR), lw=0.8, zorder=6))
    return y0 + 2.55


# A soredia
bio.panel(ax, "A", (0.2, 8.8))
top = thallus(0.6, 8.6, gap=(3.6, 5.6))
for k in range(9):
    c = np.array([4.6 + rng.normal(0, 0.7), top + 0.3 + abs(rng.normal(0, 1.4)) + (0.2 if k < 3 else 1.2 * k / 9)])
    for j in range(3):
        alga(c + rng.normal(0, 0.1, 2), 0.1)
    t = np.linspace(0, 2 * np.pi, 40)
    ax.plot(c[0] + 0.3 * np.cos(t), c[1] + 0.26 * np.sin(t * 1.0 + 0.4), color=P.edge(MED), lw=0.7, zorder=9)
bio.callout(ax, (4.0, top + 1.5), (1.6, 7.6), "Soredia")
bio.callout(ax, (3.5, top - 0.2), (1.0, 6.0), "Soralium (cortex broken)")
bio.callout(ax, (7.0, top - 0.2), (7.6, 6.0), "Upper cortex")

# B isidia
bio.panel(ax, "B", (10.2, 8.8))
top = thallus(10.6, 18.6)
for x, h in [(12.2, 2.6), (13.8, 3.4), (15.4, 2.2), (17.0, 3.0)]:
    ax.add_patch(Polygon([[x - 0.35, top - 0.05], [x - 0.3, top + h], [x + 0.3, top + h], [x + 0.35, top - 0.05]], closed=True,
                         facecolor=P.light(MED), edgecolor="none", zorder=5))
    ax.add_patch(Circle((x, top + h), 0.3, facecolor=P.light(MED), edgecolor="none", zorder=5))
    xs = [x - 0.33, x - 0.3]; ax.plot([x - 0.33, x - 0.3], [top, top + h], color=P.edge(COR), lw=2.2, zorder=7)
    ax.plot([x + 0.33, x + 0.3], [top, top + h], color=P.edge(COR), lw=2.2, zorder=7)
    t = np.linspace(0, np.pi, 20); ax.plot(x + 0.3 * np.cos(t), top + h + 0.3 * np.sin(t), color=P.edge(COR), lw=2.2, zorder=7)
    for j in range(int(h * 2)):
        alga((x + rng.uniform(-0.12, 0.12), top + 0.4 + j * 0.45), 0.1)
bio.callout(ax, (13.8, top + 3.6), (15.6, 8.0), "Isidium (corticate)")
bio.callout(ax, (17.0, top + 1.0), (18.4, 6.4), "Photobiont inside")

# C lecanorine apothecium
bio.panel(ax, "C", (20.2, 8.8))
top = thallus(20.6, 29.6, gap=(22.6, 27.6))
a = plant.ascocarp(ax, (25.1, top + 0.6), 4.6, kind="apothecium")
for side in (-1, 1):
    xm = 25.1 + side * 2.55
    ax.add_patch(Polygon([[xm - 0.45, top - 0.4], [xm - 0.35, top + 1.3], [xm + 0.35, top + 1.3], [xm + 0.45, top - 0.4]],
                         closed=True, facecolor=P.fill(COR), edgecolor=P.edge(COR), lw=0.8, zorder=10))
    for j in range(4):
        alga((xm + rng.uniform(-0.15, 0.15), top + j * 0.35), 0.1)
if "hymenium" in a:
    bio.callout(ax, a["hymenium"], (23.0, 8.2), "Hymenium: asci and paraphyses")
bio.callout(ax, (27.65, top + 0.9), (28.8, 7.0), "Thalline margin\n(with photobiont)")
