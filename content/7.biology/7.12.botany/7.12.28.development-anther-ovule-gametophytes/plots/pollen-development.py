# Microsporogenesis and pollen. A: cytokinesis after meiosis of the pollen mother cell (callose wall):
# successive (a wall after meiosis I, dyad stage, isobilateral tetrad; common in monocots) and
# simultaneous (walls after meiosis II, tetrahedral tetrad; common in eudicots). B: development of the
# male gametophyte: free microspore with central nucleus; vacuolated microspore with the nucleus at the
# wall; asymmetric mitosis; two-celled pollen (generative cell inside the vegetative cell); three-celled
# pollen (two sperm cells). C: layers of the pollen wall in section. D: aperture types in polar view.
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle, Polygon, Arc
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 13.4)
CW = P.fill("carbohydrate")


def cellc(c, r, tok="cytoplasm", callose=False, lw=1.0, z=6):
    if callose:
        ax.add_patch(Circle(c, r + 0.16, facecolor=P.light("carbohydrate"), edgecolor=P.edge("carbohydrate"), lw=0.8, zorder=z - 1))
    ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z))


def nuc(c, r, tok="nucleus", z=8):
    ax.add_patch(Circle(c, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z))


bio.panel(ax, "A", (0.2, 13.2))
bio.label(ax, (6.6, 13.0), "Cytokinesis of the pollen mother cell", size="normal", bold=True)
for j, (name, y) in enumerate((("Successive", 10.6), ("Simultaneous", 7.4))):
    bio.label(ax, (0.3, y + 1.35), name, size="small", bold=True, ha="left")
    cellc((1.6, y), 1.0, callose=True)
    nuc((1.6, y), 0.38)
    bio.arrow(ax, (2.9, y), (3.7, y), kind="process", head=0.15)
    cellc((5.0, y), 1.0, callose=True)
    if j == 0:
        ax.plot([5.0, 5.0], [y - 1.0, y + 1.0], color=P.edge("carbohydrate"), lw=2.0, zorder=7)
        nuc((4.55, y), 0.26); nuc((5.45, y), 0.26)
        bio.label(ax, (5.0, y - 1.45), "dyad", size="tiny", color=P.muted())
    else:
        for dx, dy in ((-0.45, 0.4), (0.45, 0.4), (-0.45, -0.4), (0.45, -0.4)):
            nuc((5.0 + dx, y + dy), 0.2)
        bio.label(ax, (5.0, y - 1.45), "4 free nuclei", size="tiny", color=P.muted())
    bio.arrow(ax, (6.3, y), (7.1, y), kind="process", head=0.15)
    cellc((8.6, y), 1.15, callose=True)
    if j == 0:
        ax.plot([8.6, 8.6], [y - 1.15, y + 1.15], color=P.edge("carbohydrate"), lw=2.0, zorder=7)
        ax.plot([7.45, 8.6], [y, y], color=P.edge("carbohydrate"), lw=2.0, zorder=7)
        ax.plot([8.6, 9.75], [y + 0.0, y], color=P.edge("carbohydrate"), lw=2.0, zorder=7)
        for dx, dy in ((-0.55, 0.5), (0.55, 0.5), (-0.55, -0.5), (0.55, -0.5)):
            nuc((8.6 + dx, y + dy), 0.2)
        bio.label(ax, (8.6, y - 1.6), "isobilateral tetrad", size="tiny", color=P.muted())
    else:
        for a in (90, 210, 330):
            t = np.radians(a)
            ax.plot([8.6, 8.6 + 1.15 * np.cos(t)], [y, y + 1.15 * np.sin(t)], color=P.edge("carbohydrate"), lw=2.0, zorder=7)
        for a in (30, 150, 270):
            t = np.radians(a)
            nuc((8.6 + 0.6 * np.cos(t), y + 0.6 * np.sin(t)), 0.2)
        bio.label(ax, (8.6, y - 1.6), "tetrahedral tetrad", size="tiny", color=P.muted())
bio.label(ax, (5.0, 5.4), "outer ring: callose wall", size="tiny", color=P.muted())

bio.panel(ax, "B", (11.6, 13.2))
bio.label(ax, (20.6, 13.0), "Development of the male gametophyte", size="normal", bold=True)
xs = [13.0, 16.4, 19.8, 23.2, 26.8]
y = 10.2
names = ["Microspore", "Vacuolated microspore", "Asymmetric mitosis", "Two-celled pollen", "Three-celled pollen"]
for k, x in enumerate(xs):
    ax.add_patch(Circle((x, y), 1.35, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=2.2, zorder=5))
    ax.add_patch(Circle((x, y), 1.2, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=0.8, zorder=6))
    if k == 0:
        nuc((x, y), 0.38)
    elif k == 1:
        ax.add_patch(Circle((x + 0.25, y), 0.75, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.8, zorder=7))
        nuc((x - 0.85, y), 0.28)
    elif k == 2:
        ax.add_patch(Arc((x - 1.5, y), 1.8, 2.2, theta1=-55, theta2=55, color=P.edge("carbohydrate"), lw=1.8, zorder=8))
        nuc((x - 0.85, y), 0.2, tok="chromatin"); nuc((x - 0.2, y), 0.3)
    elif k == 3:
        ax.add_patch(Ellipse((x - 0.3, y + 0.15), 1.05, 0.42, angle=25, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"),
                             lw=0.9, zorder=8))
        nuc((x + 0.5, y - 0.35), 0.32)
    else:
        for dx, dy in ((-0.45, 0.35), (-0.1, -0.25)):
            ax.add_patch(Ellipse((x + dx, y + dy), 0.85, 0.3, angle=30, facecolor=P.fill("chromatin"),
                                 edgecolor=P.edge("chromatin"), lw=0.9, zorder=8))
        nuc((x + 0.6, y - 0.4), 0.3)
    bio.label(ax, (x, y - 1.8), names[k], size="tiny")
    if k < 4:
        bio.arrow(ax, (x + 1.45, y), (xs[k + 1] - 1.45, y), kind="process", head=0.15)
bio.callout(ax, (23.2 - 0.3, 10.35), (21.9, 12.2), "Generative cell", size="tiny")
bio.callout(ax, (23.7, 9.85), (24.6, 12.2), "Vegetative nucleus", size="tiny")
bio.callout(ax, (26.4, 10.5), (27.6, 12.2), "Sperm cells", size="tiny")
bio.callout(ax, (13.0 + 0.9, 11.1), (14.6, 12.2), "Exine", size="tiny")

bio.panel(ax, "C", (11.6, 6.6))
bio.label(ax, (15.6, 6.4), "Pollen wall in section", size="normal", bold=True)
x0, x1 = 12.2, 17.4
ax.add_patch(Rectangle((x0, 4.6), x1 - x0, 0.32, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.8, zorder=6))
for xx in np.arange(x0 + 0.2, x1, 0.42):
    ax.add_patch(Rectangle((xx, 3.75), 0.16, 0.85, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.6, zorder=6))
ax.add_patch(Rectangle((x0, 3.45), x1 - x0, 0.3, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=0.8, zorder=6))
ax.add_patch(Rectangle((x0, 3.1), x1 - x0, 0.35, facecolor=P.fill("atp"), edgecolor=P.edge("atp"), lw=0.8, zorder=6))
ax.add_patch(Rectangle((x0, 2.3), x1 - x0, 0.8, facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"), lw=0.8, zorder=6))
ax.plot([x0, x1], [2.25, 2.25], color=P.edge("membrane"), lw=2.0, zorder=7)
ax.add_patch(Rectangle((x0, 1.3), x1 - x0, 0.9, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=5))
for yy, t in ((4.76, "Tectum"), (4.15, "Columellae"), (3.6, "Foot layer"), (3.28, "Endexine"), (2.7, "Intine"),
              (2.25, "Plasma membrane"), (1.7, "Cytoplasm")):
    bio.label(ax, (x1 + 0.25, yy), t, size="tiny", ha="left")
ax.plot([x0 - 0.25] * 2, [3.8, 4.92], color=P.muted(), lw=0.9)
bio.label(ax, (x0 - 0.35, 4.35), "Sexine", size="tiny", ha="right")
ax.plot([x0 - 0.25] * 2, [3.1, 3.7], color=P.muted(), lw=0.9)
bio.label(ax, (x0 - 0.35, 3.4), "Nexine", size="tiny", ha="right")

bio.panel(ax, "D", (20.2, 6.6))
bio.label(ax, (25.2, 6.4), "Aperture types (polar view)", size="normal", bold=True)
types = ["Monosulcate", "Tricolpate", "Tricolporate", "Triporate", "Pantoporate", "Monoporate"]
for k, t in enumerate(types):
    x = 21.6 + 2.85 * (k % 3) + 0.0
    yy = 4.6 if k < 3 else 1.6
    R = 0.85
    if k == 0:
        ax.add_patch(Ellipse((x, yy), 2.0, 1.3, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.2, zorder=6))
        ax.add_patch(Ellipse((x, yy), 1.3, 0.22, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("anther"), lw=0.8, zorder=7))
    else:
        ax.add_patch(Circle((x, yy), R, facecolor=P.fill("anther"), edgecolor=P.edge("anther"), lw=1.2, zorder=6))
        if k in (1, 2, 3):
            for a in (90, 210, 330):
                tt = np.radians(a)
                px, py = x + R * np.cos(tt), yy + R * np.sin(tt)
                if k in (1, 2):
                    ax.add_patch(Ellipse((x + 0.72 * R * np.cos(tt), yy + 0.72 * R * np.sin(tt)), 0.55, 0.18, angle=a,
                                         facecolor=P.fill("cytoplasm"), edgecolor=P.edge("anther"), lw=0.8, zorder=7))
                if k in (2, 3):
                    ax.add_patch(Circle((x + 0.8 * R * np.cos(tt), yy + 0.8 * R * np.sin(tt)), 0.12, facecolor=P.edge("anther"),
                                        edgecolor="none", zorder=8))
        elif k == 4:
            for (dx, dy) in ((0, 0), (0.45, 0.3), (-0.45, 0.3), (0.45, -0.35), (-0.45, -0.35), (0, 0.6), (0, -0.6)):
                ax.add_patch(Circle((x + dx, yy + dy), 0.1, facecolor=P.edge("anther"), edgecolor="none", zorder=8))
        else:
            ax.add_patch(Circle((x, yy + 0.45), 0.16, facecolor=P.edge("anther"), edgecolor="none", zorder=8))
    bio.label(ax, (x, yy - 1.15), t, size="tiny")
