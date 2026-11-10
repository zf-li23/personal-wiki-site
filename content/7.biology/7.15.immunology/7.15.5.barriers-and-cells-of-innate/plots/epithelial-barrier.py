# The intestinal epithelial barrier: commensals and a pathogen in the outer mucus, dense inner mucus with
# antimicrobial peptides and secretory IgA, epithelial cells sealed by tight junctions, a Paneth cell at the
# crypt base, and lamina propria macrophages and dendritic cells below.
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import immuno

P = bio.P
rng = np.random.default_rng(2)
fig, ax = bio.canvas(22.0, 10.0)
y_ep = 3.6  # apical surface
ax.add_patch(Rectangle((0, y_ep), 22, 3.3, facecolor=P.light("lipid"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((0, y_ep), 22, 1.2, facecolor=P.fill("lipid"), edgecolor="none", zorder=0.5))
bio.label(ax, (21.8, 9.4), "Lumen", size="small", bold=True, ha="right")
bio.label(ax, (21.8, 6.5), "outer mucus (loose)", size="tiny", ha="right")
bio.label(ax, (21.8, 4.45), "inner mucus (dense)", size="tiny", ha="right")
bio.label(ax, (21.8, 0.4), "Lamina propria", size="small", bold=True, ha="right")
# epithelium
w = 1.5
for k in range(14):
    x0 = 0.25 + k * w
    tok = "neutral"
    if k == 4:
        tok = "carbohydrate"  # goblet cell
    ax.add_patch(FancyBboxPatch((x0, y_ep - 2.0), w - 0.08, 2.0, boxstyle="round,pad=0,rounding_size=0.15",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=3))
    ax.add_patch(Ellipse((x0 + w / 2 - 0.04, y_ep - 1.4), 0.6, 0.42, facecolor=P.fill("nucleus"),
                         edgecolor=P.edge("nucleus"), lw=0.6, zorder=4))
    # tight junction at the apical side of each lateral contact
    ax.add_patch(Rectangle((x0 + w - 0.13, y_ep - 0.32), 0.1, 0.3, facecolor=P.edge("positive"), edgecolor="none", zorder=5))
    for j in range(6):
        ax.plot([x0 + 0.15 + j * 0.22] * 2, [y_ep, y_ep + 0.13], color=P.edge(tok), lw=0.8, zorder=3)
bio.label(ax, (0.25 + 4.5 * w, y_ep - 2.4), "goblet cell", size="tiny")
bio.callout(ax, (0.25 + 2 * w - 0.08, y_ep - 0.17), (2.6, 2.2 - 1.6), "tight junction")
# mucus granules from goblet cell
for j in range(6):
    ax.add_patch(Circle((0.25 + 4.5 * w + rng.uniform(-0.4, 0.4), y_ep + 0.2 + j * 0.35), 0.12,
                        facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=0.4, zorder=5))
# antimicrobial peptides and IgA in inner mucus
for j in range(55):
    ax.add_patch(Circle((rng.uniform(0.3, 19.5), rng.uniform(y_ep + 0.2, y_ep + 1.1)), 0.05,
                        facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.2, zorder=6))
for j in range(8):
    bio.antibody(ax, (1.0 + j * 2.4, y_ep + 0.75), size=0.28, angle=rng.uniform(-30, 30), token="antibody",
                 light_token="protein")
# bacteria in outer mucus
for j in range(16):
    c = (rng.uniform(0.5, 19.8), rng.uniform(y_ep + 1.6, 9.6))
    ax.add_patch(Ellipse(c, 0.55, 0.25, angle=rng.uniform(0, 180), facecolor=P.fill("bacterium"),
                         edgecolor=P.edge("bacterium"), lw=0.6, zorder=6))
for c in ((9.0, 6.2), (14.5, 7.4)):
    ax.add_patch(Ellipse(c, 0.6, 0.28, angle=30, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.7, zorder=6))
bio.label(ax, (9.0, 6.65), "pathogen", size="tiny")
bio.label(ax, (6.0, 9.85), "commensals: colonization resistance", size="tiny", ha="left")
# Paneth cell drawn below a crypt opening
px = 0.25 + 10 * w
ax.add_patch(FancyBboxPatch((px, y_ep - 3.4), w - 0.08, 1.35, boxstyle="round,pad=0,rounding_size=0.15",
                            facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.9, zorder=3))
for j in range(7):
    ax.add_patch(Circle((px + 0.3 + (j % 4) * 0.3, y_ep - 2.6 + (j // 4) * 0.3), 0.1, facecolor=P.fill("drug"),
                        edgecolor=P.edge("drug"), lw=0.3, zorder=5))
bio.label(ax, (px + 0.7, y_ep - 3.75), "Paneth cell: α-defensins", size="tiny")
# lamina propria cells
immuno.immune_cell(ax, (5.0, 0.9), r=0.55, kind="dendritic", token="antibody", seed=3)
ax.plot([5.3, 5.6], [1.6, y_ep - 0.1], color=P.edge("antibody"), lw=1.6, zorder=6)
bio.label(ax, (5.0, 0.05), "dendritic cell (samples lumen)", size="tiny")
bio.shape(ax, bio.blob((9.5, 0.9), 0.9, 0.6, wobble=0.12, seed=9), token="neutral", zorder=4)
ax.add_patch(Circle((9.8, 1.0), 0.28, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.6, zorder=5))
bio.label(ax, (9.5, 0.05), "macrophage", size="tiny")
immuno.immune_cell(ax, (19.0, 1.0), r=0.5, kind="plasma", token="channel", seed=4)
bio.label(ax, (18.0, 0.05), "IgA plasma cell", size="tiny")
