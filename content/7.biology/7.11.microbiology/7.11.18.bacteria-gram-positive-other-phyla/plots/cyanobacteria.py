"""The five morphological subsections of cyanobacteria (schematic; after Rippka and colleagues 1979).
I: unicellular cells that divide by binary fission (Synechococcus, Prochlorococcus) or form colonies in a
common envelope (Gloeocapsa). II: cells that divide by multiple fission into many small baeocytes
(Pleurocapsa, Dermocarpa). III: filaments (trichomes) of undifferentiated cells (Oscillatoria, Limnospira).
IV: filaments with heterocysts, which fix nitrogen, and akinetes, resting cells (Anabaena, Nostoc).
V: filaments with true branching and heterocysts (Fischerella, Stigonema). Subsections I-III without
heterocysts are not natural groups; IV and V together form a clade."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 8.4)
V, H, A = "chloroplast", "highlight", "enzyme"


def cell(x, y, w, h, tok=V, wall=1.0, angle=0):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={min(w, h) * 0.35}",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=wall, zorder=8))


def heading(x, roman, genus):
    bio.label(ax, (x, 7.7), roman, size="title", bold=True)
    bio.label(ax, (x, 1.1), genus, size="small", italic=True)


# I
heading(2.4, "I", "Synechococcus, Gloeocapsa")
cell(1.4, 5.2, 0.6, 1.2)
cell(1.4, 3.6, 0.6, 1.2)
ax.add_patch(Ellipse((3.1, 4.4), 2.0, 2.4, facecolor=P.light("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=0.8,
                     zorder=6))
for dx, dy in [(-0.4, 0.5), (0.4, 0.5), (-0.4, -0.4), (0.4, -0.4)]:
    ax.add_patch(Circle((3.1 + dx, 4.4 + dy), 0.33, facecolor=P.fill(V), edgecolor=P.edge(V), lw=1.0, zorder=8))
bio.label(ax, (2.4, 2.1), "single cells, colonies", size="tiny", color=P.muted())
# II
heading(7.4, "II", "Pleurocapsa")
ax.add_patch(Circle((6.7, 4.4), 1.1, facecolor=P.light(V), edgecolor=P.edge(V), lw=1.3, zorder=7))
rng = np.random.default_rng(1)
for k in range(14):
    r, a = 0.75 * np.sqrt(rng.uniform()), rng.uniform(0, 2 * np.pi)
    ax.add_patch(Circle((6.7 + r * np.cos(a), 4.4 + r * np.sin(a)), 0.17, facecolor=P.fill(V), edgecolor=P.edge(V),
                        lw=0.6, zorder=8))
for dx, dy in [(1.5, 0.7), (1.8, 0.1), (1.6, -0.6)]:
    ax.add_patch(Circle((6.7 + dx, 4.4 + dy), 0.18, facecolor=P.fill(V), edgecolor=P.edge(V), lw=0.6, zorder=8))
bio.callout(ax, (8.5, 3.8), (8.8, 2.8), "released baeocytes", size="tiny")
bio.label(ax, (7.4, 2.1), "multiple fission", size="tiny", color=P.muted())
# III
heading(12.2, "III", "Oscillatoria")
for k in range(9):
    cell(10.3 + 0.42 * k, 4.4, 0.38, 0.95, wall=0.8)
bio.label(ax, (12.2, 2.1), "trichome, no heterocysts", size="tiny", color=P.muted())
# IV
heading(17.3, "IV", "Anabaena, Nostoc")
xs = 14.6
for k in range(11):
    if k == 5:
        ax.add_patch(Circle((xs + 0.33, 4.4), 0.38, facecolor=P.fill(H), edgecolor=P.edge(H), lw=2.0, zorder=8))
        for sgn in (-1, 1):
            ax.add_patch(Circle((xs + 0.33 + sgn * 0.3, 4.4), 0.07, color=P.edge(H), zorder=9))
        hx = xs + 0.33
        xs += 0.8
    elif k == 8:
        ax.add_patch(Ellipse((xs + 0.45, 4.4), 0.9, 0.62, facecolor=P.fill(A), edgecolor=P.edge(A), lw=1.6, zorder=8))
        ax_ = xs + 0.45
        xs += 0.95
    else:
        ax.add_patch(Circle((xs + 0.25, 4.4), 0.25, facecolor=P.fill(V), edgecolor=P.edge(V), lw=0.8, zorder=8))
        xs += 0.52
bio.callout(ax, (hx, 4.75), (hx - 0.6, 5.9), "heterocyst", size="tiny")
bio.callout(ax, (ax_, 4.7), (ax_ + 0.2, 5.9), "akinete", size="tiny")
bio.label(ax, (17.3, 2.1), "heterocysts, akinetes", size="tiny", color=P.muted())
# V
heading(23.2, "V", "Fischerella")
main = [(21.4 + 0.5 * k, 3.6) for k in range(8)]
for x, y in main:
    cell(x, y, 0.46, 0.6, wall=0.8)
for k in range(5):
    cell(23.0, 4.1 + 0.5 * k, 0.6, 0.46, wall=0.8)
for k in range(3):
    cell(21.9, 4.1 + 0.5 * k, 0.6, 0.46, wall=0.8)
ax.add_patch(Circle((24.9, 3.6), 0.3, facecolor=P.fill(H), edgecolor=P.edge(H), lw=2.0, zorder=9))
bio.callout(ax, (23.3, 6.1), (24.4, 6.6), "true branch", size="tiny")
bio.label(ax, (23.2, 2.1), "branched filaments", size="tiny", color=P.muted())
