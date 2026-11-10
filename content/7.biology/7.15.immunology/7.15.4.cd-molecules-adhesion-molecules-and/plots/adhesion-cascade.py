# The leukocyte adhesion cascade: (1) selectin-mediated tethering and rolling, (2) chemokine-triggered
# inside-out activation of integrins, (3) firm adhesion of integrins to ICAM-1/VCAM-1, (4) crawling and
# transendothelial migration (diapedesis) into the tissue, then chemotaxis up a chemokine gradient.
import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(24.0, 10.0)
y_end = 4.2  # luminal surface of the endothelium

# lumen, endothelium and tissue
ax.add_patch(__import__("matplotlib").patches.Rectangle((0, y_end), 24, 5.8, facecolor=P.fill("blood") if False else P.light("extracellular"),
                                                       edgecolor="none", zorder=0))
bio.label(ax, (0.4, 9.5), "Blood vessel lumen", size="small", ha="left", bold=True)
bio.label(ax, (0.4, 0.4), "Tissue", size="small", ha="left", bold=True)
bio.arrow(ax, (3.6, 9.0), (6.6, 9.0), kind="process", head=0.2)
bio.label(ax, (5.1, 9.4), "flow", size="tiny")
for k in range(9):
    x0 = 0.1 + k * 2.65
    ax.add_patch(__import__("matplotlib").patches.FancyBboxPatch((x0, y_end - 0.75), 2.5, 0.75,
                 boxstyle="round,pad=0,rounding_size=0.3", facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"),
                 lw=1.0, zorder=3))
    ax.add_patch(__import__("matplotlib").patches.Ellipse((x0 + 1.25, y_end - 0.38), 1.0, 0.36,
                 facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.7, zorder=4))
bio.label(ax, (23.8, y_end - 1.05), "endothelium", size="tiny", ha="right", color=P.muted(), zorder=6)

def leuko(c, r=0.75, squash=1.0, seed=0, z=8):
    o = bio.blob(c, r * (2 - squash), r * squash, wobble=0.05, seed=seed, k=8)
    bio.shape(ax, o, token="neutral", zorder=z)
    ax.add_patch(Circle((c[0] + 0.1, c[1] + 0.05), r * 0.45 * squash ** 0.3, facecolor=P.fill("nucleus"),
                        edgecolor=P.edge("nucleus"), lw=0.8, zorder=z + 1))


# free-flowing leukocyte
leuko((1.6, 7.3), seed=1)
# 1 rolling: selectin tethers
c1 = (5.2, y_end + 0.82)
leuko(c1, seed=2)
for dx in (-0.45, 0.0, 0.45):
    ax.plot([c1[0] + dx, c1[0] + dx * 1.3], [y_end + 0.1, c1[1] - 0.7], color=P.edge("carbohydrate"), lw=1.6, zorder=7)
    ax.add_patch(Circle((c1[0] + dx, y_end + 0.12), 0.08, color=P.edge("receptor"), zorder=7))
bio.arrow(ax, (4.4, 6.3), (6.2, 6.3), kind="process", head=0.15, bend=-0.3)
# 2 activation by chemokine on the endothelial glycocalyx
c2 = (9.6, y_end + 0.78)
leuko(c2, seed=3)
for dx in (-1.1, -0.6, 0.6, 1.1, 1.6):
    immuno.cytokine(ax, (c2[0] + dx, y_end + 0.18), token="drug", r=0.11)
bio.arrow(ax, (c2[0] + 1.6, y_end + 0.35), (c2[0] + 0.5, c2[1] - 0.3), kind="activation", head=0.14, bend=0.2)
# 3 firm adhesion: extended integrins to ICAM-1
c3 = (14.0, y_end + 0.6)
leuko(c3, squash=0.8, seed=4)
for dx in (-0.8, -0.3, 0.2, 0.7):
    ax.plot([c3[0] + dx, c3[0] + dx], [y_end + 0.05, c3[1] - 0.5], color=P.edge("enzyme"), lw=2.2, zorder=7)
    ax.add_patch(Circle((c3[0] + dx, y_end + 0.06), 0.1, color=P.edge("protein"), zorder=7))
# 4 crawling and transmigration between two endothelial cells (junction at x = 18.65)
xj = 0.1 + 7 * 2.65 - 0.075
leuko((xj - 0.3, y_end + 0.35), r=0.62, squash=0.7, seed=5)
bio.shape(ax, bio.blob((xj, y_end - 0.4), 0.28, 0.6, wobble=0.03, seed=6, k=8), token="neutral", zorder=8)
leuko((xj + 0.25, y_end - 1.35), r=0.6, squash=0.75, seed=7)
# migrating cell in tissue up a gradient towards an infection focus
leuko((20.2, 1.6), r=0.65, seed=8)
for k in range(14):
    xx = 21.3 + (k % 5) * 0.45 + 0.2 * (k // 5)
    yy = 0.7 + (k // 5) * 0.55 + 0.1 * (k % 2)
    immuno.cytokine(ax, (xx, yy), token="drug", r=0.08)
bio.virus(ax, (23.0, 1.5), 0.3, kind="enveloped")
bio.arrow(ax, (19.0, 2.2), (19.9, 1.9), kind="process", head=0.14)

# step labels
for x, n, t1, t2 in ((5.2, "1", "Tethering and rolling", "selectins ↔ sLeX glycans"),
                     (9.6, "2", "Activation", "chemokine → GPCR →\nintegrin opens"),
                     (14.0, "3", "Firm adhesion", "LFA-1 / VLA-4 ↔\nICAM-1 / VCAM-1"),
                     (18.6, "4", "Diapedesis", "crawling, then exit\nbetween endothelial cells")):
    bio.label(ax, (x, 8.3), f"{n}  {t1}", size="small", bold=True)
    bio.label(ax, (x, 7.55), t2, size="tiny", va="top")
bio.label(ax, (21.7, 3.0), "chemotaxis up the\ngradient to the focus", size="tiny")
