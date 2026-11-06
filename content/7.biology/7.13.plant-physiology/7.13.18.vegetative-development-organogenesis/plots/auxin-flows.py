# Auxin flows and maxima at the two apical meristems (schematic, after Taiz et al. 6e, Figs 18.19 and 19.19;
# Blilou et al. 2005; Reinhardt et al. 2003). (A) Arabidopsis root tip, longitudinal: auxin arrives through
# the stele (PIN1), forms a maximum around the quiescent centre and columella, is redistributed laterally
# in the columella (PIN3, PIN4, PIN7), moves shootward in the lateral root cap and epidermis (AUX1, PIN2)
# and partly refluxes into the stele through the cortex: the "reverse fountain". (B) Shoot apex, side view:
# in the L1 layer PIN1 points towards a convergence point where the next primordium (I1) will form;
# existing primordia (P1, P2) act as sinks and drain auxin basipetally into the provascular strands.
import numpy as np
import wikibio as bio
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon

P = bio.P
fig, ax = bio.canvas(17, 10)
bio.panel(ax, "A", (0.1, 9.9))
bio.panel(ax, "B", (9.2, 9.9))
cx = 4.4
# root tissues: bands (half-widths) from the centre outwards
bands = [("stele", 0.75, "xylem"), ("pericycle", 0.95, "pericycle"), ("endodermis", 1.2, "endodermis"),
         ("cortex", 1.6, "cytoplasm"), ("epidermis", 1.95, "cell_wall"), ("lateral root cap", 2.3, "bract")]
y0, y1 = 3.0, 9.2
for name, hw, tok in reversed(bands):
    top = y1 if name != "lateral root cap" else 5.6
    bot = y0 - (0.0 if name != "lateral root cap" else 1.4)
    ax.add_patch(FancyBboxPatch((cx - hw, bot), 2 * hw, top - bot, boxstyle="round,pad=0,rounding_size=0.9",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=2))
# columella
ax.add_patch(Ellipse((cx, 2.3), 1.9, 1.5, facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"), lw=0.9, zorder=3))
# quiescent centre
ax.add_patch(FancyBboxPatch((cx - 0.45, 2.95), 0.9, 0.4, boxstyle="round,pad=0,rounding_size=0.1",
                            facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=5))
# auxin maximum (concentric tints)
for rr, al in ((1.15, 0.18), (0.8, 0.28), (0.45, 0.4)):
    ax.add_patch(Ellipse((cx, 2.75), 2 * rr, 1.7 * rr, facecolor=P.fill("negative"), edgecolor="none", alpha=al, zorder=6))
red = P.edge("negative")
bio.arrow(ax, (cx, 8.6), (cx, 3.6), kind="process", color=red, lw=2.2)
for s in (-1, 1):
    bio.arrow(ax, (cx + 0.25 * s, 2.3), (cx + 1.15 * s, 2.55), kind="process", color=red, lw=1.6, bend=0.15 * s)
    bio.arrow(ax, (cx + 2.1 * s, 2.9), (cx + 2.1 * s, 5.8), kind="process", color=red, lw=1.8)
    bio.arrow(ax, (cx + 1.78 * s, 6.1), (cx + 1.78 * s, 7.2), kind="process", color=red, lw=1.4)
    bio.arrow(ax, (cx + 1.6 * s, 7.6), (cx + 0.6 * s, 7.0), kind="process", color=red, lw=1.3, dashed=True)
lbl = [("Stele (PIN1: rootward)", (cx, 8.0), (7.6, 8.8)), ("Pericycle", (cx + 0.85, 6.5), (7.6, 7.9)),
       ("Endodermis", (cx + 1.08, 5.9), (7.6, 7.1)), ("Cortex: reflux", (cx + 1.4, 7.3), (7.6, 6.3)),
       ("Epidermis (PIN2, AUX1: shootward)", (cx + 1.78, 6.7), (7.6, 5.5)),
       ("Lateral root cap", (cx + 2.15, 4.4), (7.6, 4.6)), ("Quiescent centre", (cx + 0.4, 3.15), (7.6, 3.6)),
       ("Columella (PIN3, PIN4, PIN7)", (cx + 0.7, 2.1), (7.6, 2.6))]
for text, p, t in lbl:
    bio.callout(ax, p, t, text, size="tiny")
bio.label(ax, (cx, 0.5), "Auxin maximum (red) at the QC and columella", size="small")

# shoot apex
sx, sy = 13.1, 3.0
th = np.linspace(0, np.pi, 120)
dome = np.c_[sx + 2.6 * np.cos(th), sy + 2.0 * np.sin(th)]
bio.shape(ax, np.vstack([dome, [[sx - 2.6, sy - 2.2], [sx + 2.6, sy - 2.2]]]), token="cytoplasm", lw=1.0, zorder=2)
for (px, py, ang, size, name) in ((sx + 3.05, sy + 0.6, -35, 1.4, "P1"), (sx - 3.35, sy - 0.2, 40, 2.0, "P2")):
    ax.add_patch(Ellipse((px, py), size * 0.9, size * 1.6, angle=ang, facecolor=P.fill("plant"), edgecolor=P.edge("plant"),
                         lw=1.0, zorder=3))
    bio.label(ax, (px, py), name, size="small", color=P.on_fill(), zorder=8)
# L1 PIN1 arrows converging to I1
i1 = np.array([sx + 1.9, sy + 1.37])
ax.add_patch(Ellipse(i1, 0.75, 0.5, angle=-35, facecolor=P.fill("negative"), edgecolor="none", alpha=0.45, zorder=6))
for t0, t1 in ((1.55, 1.0), (0.9, 0.85), (0.35, 0.65)):
    if t0 > t1:
        pts = [np.array([sx + 2.75 * np.cos(t), sy + 2.12 * np.sin(t)]) for t in (t0, t1)]
    else:
        pts = [np.array([sx + 2.75 * np.cos(t), sy + 2.12 * np.sin(t)]) for t in (t0, t1)]
    bio.arrow(ax, pts[0], pts[1], kind="process", color=red, lw=1.6)
bio.arrow(ax, i1 + (-0.2, -0.3), (sx + 1.3, sy - 1.6), kind="process", color=red, lw=1.6, dashed=True)
bio.arrow(ax, (sx + 2.6, sy - 0.1), (sx + 1.9, sy - 1.8), kind="process", color=red, lw=1.8)
bio.arrow(ax, (sx - 2.6, sy - 0.4), (sx - 1.9, sy - 1.9), kind="process", color=red, lw=1.8)
bio.label(ax, (sx, sy + 0.8), "CZ", size="small")
bio.callout(ax, i1, (sx + 2.3, 7.6), "I1: auxin maximum\n(next primordium)", size="tiny")
bio.callout(ax, (sx + 0.8, sy + 2.0), (sx - 0.4, 6.9), "L1: PIN1 points to\nthe convergence point", size="tiny")
bio.callout(ax, (sx - 2.25, sy - 1.3), (sx - 2.25, 0.25), "Primordia drain auxin into provascular strands", size="tiny")
bio.label(ax, (sx, 9.5), "Shoot apex (side view)", size="small", bold=True)
bio.label(ax, (cx, 9.7), "Root tip (longitudinal)", size="small", bold=True)
