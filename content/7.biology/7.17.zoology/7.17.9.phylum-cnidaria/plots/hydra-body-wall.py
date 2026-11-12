"""The body wall of Hydra in longitudinal section (schematic, not to scale; outside at the top, gastrovascular
cavity at the bottom). Epidermis (ectoderm): epitheliomuscular cells whose basal processes run along the body
axis and form the longitudinal muscle layer; interstitial cells in nests between their bases; a cnidocyte with
its capsule and cnidocil; a sensory cell; a nerve cell at the base. Mesoglea: a thin acellular matrix.
Gastrodermis (endoderm): digestive (nutritive-muscular) cells with flagella and food vacuoles, whose basal
processes run around the body (circular muscle, cut across); gland cells with secretory granules; a mucous cell.
"""

import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 13.0)

ECT, END = "ectoderm", "endoderm"
y_mes0, y_mes1 = 5.6, 6.0          # mesoglea band
y_top = 10.2                       # outer surface of the epidermis
y_bot = 1.6                        # free surface of the gastrodermis


def cell(x0, x1, y0, y1, token, z=4):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.25",
                                facecolor=P.light(token), edgecolor=P.edge(token), lw=1.1, zorder=z))


def nucleus(c, r=0.42, ry=None):
    ax.add_patch(Ellipse(c, 2 * r, 2 * (ry or r * 0.8), facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                         lw=0.8, zorder=9))


# outside and cavity labels
bio.label(ax, (1.0, 12.3), "Outside (pond water)", size="small", color=P.muted(), ha="left")
bio.label(ax, (1.0, -0.3), "Gastrovascular cavity", size="small", color=P.muted(), ha="left")

# mesoglea
ax.add_patch(Polygon([(0.6, y_mes0), (22.0, y_mes0), (22.0, y_mes1), (0.6, y_mes1)], closed=True,
                     facecolor=P.fill("mesoglea"), edgecolor=P.edge("mesoglea"), lw=0.8, zorder=3))

# ---- epidermis: epitheliomuscular cells
xs = [0.6, 4.1, 7.6, 11.1, 14.6, 18.1, 22.0]
for i in range(len(xs) - 1):
    cell(xs[i] + 0.05, xs[i + 1] - 0.05, y_mes1 + 0.75, y_top, ECT)
    nucleus(((xs[i] + xs[i + 1]) / 2, 8.9))
    # basal muscle process: longitudinal, so it runs along the section
    ax.add_patch(FancyBboxPatch((xs[i] + 0.15, y_mes1 + 0.08), xs[i + 1] - xs[i] - 0.3, 0.42,
                                boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill("muscle"),
                                edgecolor=P.edge("muscle"), lw=0.9, zorder=6))
    ax.plot([(xs[i] + xs[i + 1]) / 2] * 2, [y_mes1 + 0.5, y_mes1 + 0.8], color=P.edge(ECT), lw=1.2, zorder=5)

# interstitial cells: a nest between two epitheliomuscular cells, near the base
for k, (cx, cy) in enumerate([(7.25, 7.3), (7.95, 7.4), (7.6, 7.95)]):
    ax.add_patch(Ellipse((cx, cy), 0.62, 0.56, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=10))
    ax.add_patch(Ellipse((cx, cy), 0.32, 0.28, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.5, zorder=11))

# cnidocyte with a capsule and cnidocil, wedged between cells 4 and 5
cx = 14.6
ax.add_patch(Polygon([(cx - 0.55, y_top - 0.05), (cx + 0.55, y_top - 0.05), (cx + 0.7, 8.0), (cx - 0.7, 8.0)],
                     closed=True, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=10))
ax.add_patch(Ellipse((cx, 9.15), 0.8, 1.45, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=1.1, zorder=11))
t = np.linspace(0, 5 * np.pi, 120)
ax.plot(cx + 0.22 * np.sin(t), 8.65 + 0.95 * t / t[-1], color=P.edge("highlight"), lw=0.7, zorder=12)
ax.plot([cx + 0.1, cx + 0.15], [y_top - 0.05, y_top + 0.7], color=P.ink(), lw=1.4, zorder=12)
nucleus((cx, 8.3), 0.28)

# sensory cell with an apical cilium, between cells 2 and 3
sx = 4.1
ax.add_patch(Polygon([(sx - 0.3, y_top - 0.05), (sx + 0.3, y_top - 0.05), (sx + 0.4, 7.4), (sx - 0.4, 7.4)], closed=True,
                     facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=1.0, zorder=10))
ax.plot([sx, sx + 0.25], [y_top - 0.05, y_top + 0.9], color=P.edge("neuron"), lw=1.2, zorder=12)
nucleus((sx, 8.1), 0.25)
ax.plot([sx, sx + 1.4], [7.4, 6.85], color=P.edge("neuron"), lw=1.2, zorder=12)

# nerve cell at the base of the epidermis, with processes along the mesoglea
nx = 18.9
ax.add_patch(Ellipse((nx, 6.95), 0.9, 0.6, facecolor=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=1.0, zorder=12))
ax.plot([nx - 3.0, nx - 0.45], [6.75, 6.9], color=P.edge("neuron"), lw=1.2, zorder=12)
ax.plot([nx + 0.45, nx + 2.9], [6.9, 6.7], color=P.edge("neuron"), lw=1.2, zorder=12)

# ---- gastrodermis: digestive (nutritive-muscular) cells
gs = [0.6, 4.6, 8.6, 12.0, 15.6, 19.0, 22.0]
for i in range(len(gs) - 1):
    x0, x1 = gs[i] + 0.05, gs[i + 1] - 0.05
    if i == 2:   # gland cell
        cell(x0, x1, y_bot, y_mes0 - 0.75, "enzyme")
        rng = np.random.default_rng(1)
        for _ in range(14):
            ax.add_patch(Ellipse((rng.uniform(x0 + 0.5, x1 - 0.5), rng.uniform(y_bot + 0.3, 3.3)), 0.32, 0.32,
                                 facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.5, zorder=8))
        nucleus(((x0 + x1) / 2, 4.1))
        continue
    if i == 4:   # mucous cell
        cell(x0, x1, y_bot, y_mes0 - 0.75, "carbohydrate")
        ax.add_patch(Ellipse(((x0 + x1) / 2, 2.6), 2.2, 1.6, facecolor=P.fill("carbohydrate"),
                             edgecolor=P.edge("carbohydrate"), lw=0.7, zorder=8))
        nucleus(((x0 + x1) / 2, 4.1))
        continue
    cell(x0, x1, y_bot, y_mes0 - 0.75, END)
    nucleus(((x0 + x1) / 2, 4.0))
    for fx in ((x0 + x1) / 2 - 0.7, (x0 + x1) / 2 + 0.7):
        ax.add_patch(Ellipse((fx, 2.6), 0.75, 0.6, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.6, zorder=8))
    tt = np.linspace(0, 1, 40)
    for fx in ((x0 + x1) / 2 - 0.3, (x0 + x1) / 2 + 0.35):
        ax.plot(fx + 0.15 * np.sin(tt * 9), y_bot - 0.9 * tt, color=P.edge(END), lw=0.9, zorder=8)
    # circular muscle processes, cut across
    for mx in np.linspace(x0 + 0.5, x1 - 0.5, 3):
        ax.add_patch(Ellipse((mx, y_mes0 - 0.32), 0.55, 0.42, facecolor=P.fill("muscle"), edgecolor=P.edge("muscle"),
                             lw=0.8, zorder=6))

# labels
bio.label(ax, (23.6, 8.3), "Epidermis\n(ectoderm)", size="normal", bold=True, color=P.edge(ECT))
bio.label(ax, (23.6, 5.8), "Mesoglea", size="normal", bold=True, color=P.muted())
bio.label(ax, (23.6, 3.4), "Gastrodermis\n(endoderm)", size="normal", bold=True, color=P.edge(END))

bio.callout(ax, (2.3, 8.9), (1.6, 11.5), "Epitheliomuscular cell", size="small")
bio.callout(ax, (sx + 0.2, y_top + 0.6), (5.8, 11.9), "Sensory cell", size="small")
bio.callout(ax, (7.95, 7.4), (9.2, 11.5), "Interstitial cells", size="small")
bio.callout(ax, (cx + 0.14, y_top + 0.6), (16.0, 11.9), "Cnidocil", size="small")
bio.callout(ax, (cx + 0.3, 9.3), (18.4, 11.5), "Cnidocyte with nematocyst", size="small")
bio.callout(ax, (nx + 0.2, 7.1), (21.0, 11.0), "Nerve cell", size="small")
bio.callout(ax, (12.0, y_mes1 + 0.3), (12.2, 7.3), "Longitudinal muscle process", size="small")
bio.callout(ax, (2.6 + 0.6, y_mes0 - 0.32), (1.0, 5.0), "Circular muscle process (cut across)", size="small")
bio.callout(ax, (6.6 - 0.7, 2.6), (6.2, 0.6), "Food vacuole", size="small")
bio.callout(ax, (10.3, 2.4), (11.0, 0.6), "Gland cell (enzymes)", size="small")
bio.callout(ax, (13.8 - 0.3, y_bot - 0.6), (14.6, 0.2), "Flagella", size="small")
bio.callout(ax, (17.3, 2.6), (17.9, 0.6), "Mucous cell", size="small")
bio.callout(ax, (20.5, 4.0), (21.6, 0.6), "Digestive cell", size="small")
