# Development of the Polygonum-type (monosporic, eight-nucleate) embryo sac; micropylar end at the top.
# The megasporocyte in the nucellus divides meiotically into a linear tetrad of megaspores; the three
# micropylar megaspores degenerate and the chalazal one enlarges (functional megaspore). Three free-nuclear
# mitoses give 2, 4 and 8 nuclei; one nucleus from each end moves to the centre (polar nuclei); cell walls
# then form: egg apparatus (egg and two synergids with the filiform apparatus) at the micropylar end, three
# antipodals at the chalazal end and the large central cell with two polar nuclei.
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 9.4)


def sac(c, w, h, tok="cytoplasm"):
    ax.add_patch(Ellipse(c, w, h, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=6))


def nuc(p, r=0.17, tok="nucleus", z=9):
    ax.add_patch(Circle(p, r, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z))


Y = 4.9
xs = [1.8, 5.0, 8.0, 11.2, 14.6, 18.2, 21.9, 26.2]
titles = ["Megasporocyte", "Linear tetrad", "Functional\nmegaspore", "2-nucleate", "4-nucleate", "8-nucleate",
          "Polar nuclei\nmigrate", "Mature embryo sac\n(7 cells, 8 nuclei)"]
for k, x in enumerate(xs):
    # nucellus background
    ax.add_patch(Ellipse((x, Y), 2.5 if k < 7 else 3.6, 6.4, facecolor=P.light("ovule"), edgecolor=P.edge("ovule"), lw=0.8,
                         zorder=4))
    bio.label(ax, (x, 0.7), titles[k], size="tiny")
bio.label(ax, (0.3, 8.9), "micropylar end", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.3, 1.55), "chalazal end", size="tiny", ha="left", color=P.muted())
# 1 megasporocyte
sac((xs[0], Y + 0.9), 1.1, 1.6); nuc((xs[0], Y + 0.9), 0.32)
# 2 linear tetrad
for i in range(4):
    yy = Y + 2.1 - 0.75 * i
    tok = "neutral" if i < 3 else "cytoplasm"
    ax.add_patch(Ellipse((xs[1], yy), 1.0, 0.7, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=6))
    nuc((xs[1], yy), 0.16, tok="neutral" if i < 3 else "nucleus")
bio.callout(ax, (xs[1] + 0.3, Y + 2.1), (xs[1] + 0.9, Y + 3.2), "degenerating", size="tiny")
# 3 functional megaspore
sac((xs[2], Y), 1.3, 2.6); nuc((xs[2], Y), 0.26)
for i in range(3):
    ax.add_patch(Ellipse((xs[2], Y + 1.7 + 0.32 * i), 0.5, 0.22, facecolor=P.light("neutral"), edgecolor=P.edge("neutral"), lw=0.6, zorder=6))
# free nuclear stages
for k, n in ((3, 2), (4, 4), (5, 8)):
    x = xs[k]
    sac((x, Y), 1.6, 4.0)
    ax.add_patch(Ellipse((x, Y), 1.0, 1.8, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.6, zorder=7))
    per = n // 2
    for end in (1, -1):
        for j in range(per):
            off = (j - (per - 1) / 2) * 0.38
            nuc((x + off, Y + end * (1.45 - 0.0 * abs(off))), 0.15)
# polar nuclei migrate
x = xs[6]
sac((x, Y), 1.7, 4.4)
ax.add_patch(Ellipse((x, Y), 1.0, 1.5, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=0.6, zorder=7))
for end in (1, -1):
    for off in (-0.4, 0.0, 0.4):
        nuc((x + off, Y + end * 1.6), 0.15)
    nuc((x + 0.12 * end, Y + end * 0.55), 0.15, tok="highlight")
    bio.arrow(ax, (x + 0.12 * end, Y + end * 1.35), (x + 0.12 * end, Y + end * 0.78), kind="process", head=0.12)
# mature embryo sac
x = xs[7]
ax.add_patch(Ellipse((x, Y), 2.2, 5.2, facecolor=P.fill("vacuole"), edgecolor=P.edge("cytoplasm"), lw=1.2, zorder=6))
for dx, tok, lab in ((-0.45, "receptor", "Synergid"), (0.45, "receptor", None)):
    ax.add_patch(Ellipse((x + dx, Y + 1.9), 0.62, 1.15, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=8))
    nuc((x + dx, Y + 2.15), 0.13)
    ax.plot([x + dx - 0.15, x + dx + 0.15], [Y + 2.45, Y + 2.45], color=P.edge(tok), lw=2.2, zorder=9)
ax.add_patch(Ellipse((x, Y + 1.35), 0.75, 1.15, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=1.0, zorder=9))
nuc((x, Y + 1.15), 0.16)
for dx, dy in ((-0.45, -1.95), (0.45, -1.95), (0.0, -2.25)):
    ax.add_patch(Ellipse((x + dx, Y + dy), 0.62, 0.55, facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"), lw=0.9,
                         zorder=8))
    nuc((x + dx, Y + dy), 0.11)
nuc((x - 0.16, Y + 0.2), 0.16, tok="highlight"); nuc((x + 0.16, Y + 0.2), 0.16, tok="highlight")
bio.callout(ax, (x + 0.55, Y + 2.0), (x + 2.0, Y + 3.3), "Synergids", size="tiny")
bio.callout(ax, (x + 0.55, Y + 2.47), (x + 2.0, Y + 2.7), "Filiform apparatus", size="tiny")
bio.callout(ax, (x + 0.2, Y + 1.15), (x + 2.0, Y + 1.6), "Egg cell", size="tiny")
bio.callout(ax, (x + 0.3, Y + 0.2), (x + 2.0, Y + 0.3), "Polar nuclei", size="tiny")
bio.callout(ax, (x + 0.8, Y - 0.6), (x + 2.0, Y - 0.9), "Central cell", size="tiny")
bio.callout(ax, (x + 0.55, Y - 2.0), (x + 2.0, Y - 2.1), "Antipodals", size="tiny")
for k in range(len(xs) - 1):
    bio.arrow(ax, (xs[k] + (1.25 if k < 7 else 1.6) + 0.05, 8.4), (xs[k + 1] - 1.25, 8.4), kind="process", head=0.12)
bio.label(ax, ((xs[0] + xs[1]) / 2, 8.75), "meiosis", size="tiny", color=P.muted())
bio.label(ax, ((xs[3] + xs[5]) / 2, 8.75), "three free-nuclear mitoses", size="tiny", color=P.muted())
bio.label(ax, ((xs[6] + xs[7]) / 2, 8.75), "cellularization", size="tiny", color=P.muted())
