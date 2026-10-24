# The segmentation gene hierarchy of Drosophila (lateral views, anterior left; schematic positions in % egg
# length). Maternal gradients (Bicoid protein from the anterior pole, Nanos from the posterior) regulate the
# zygotic gap genes, expressed in broad overlapping domains; gap proteins position the seven stripes of each
# pair-rule gene (eve and ftz alternate); pair-rule proteins set up the 14 stripes of the segment-polarity
# genes engrailed and wingless at the parasegment boundaries (wg just anterior to en). Hox genes then give
# each segment its identity.
import numpy as np
import wikibio as bio
from wikibio import development as D

fig, ax = bio.canvas(19.0, 14.2)
P = bio.P
X, L, H = 12.6, 9.0, 1.9
rows = [12.0, 8.9, 5.8, 2.7]
tiers = [("Maternal effect", "protein gradients from localised mRNAs", "receptor"), ("Gap", "broad domains", "channel"),
         ("Pair-rule", "7 stripes", "positive"), ("Segment polarity", "14 stripes", "highlight")]

# left: the hierarchy
for k, ((name, sub, tok), y) in enumerate(zip(tiers, rows)):
    bio.box(ax, (3.1, y + 0.15), 4.4, 0.75, token=tok, text=name, size="normal")
    bio.label(ax, (3.1, y - 0.55), sub, size="small", color=P.muted())
    if k:
        bio.arrow(ax, (3.1, rows[k - 1] - 0.85), (3.1, y + 0.6), kind="activation")
bio.arrow(ax, (3.1, rows[-1] - 0.85), (3.1, 0.95), kind="activation")
bio.label(ax, (3.1, 0.6), "Hox genes: segment identity", size="small", bold=True)

genes = []
# maternal
e = D.FlyEmbryo(ax, (X, rows[0]), L, H)
e.gradients([(lambda f: np.exp(-f / 0.2), "receptor"), (lambda f: 0.8 * np.exp(-(1 - f) / 0.12), "metabolite")], floor=0.04)
genes.append([("bicoid", "receptor"), ("nanos", "metabolite")])
# gap
e = D.FlyEmbryo(ax, (X, rows[1]), L, H)
e.domain(0.0, 0.47, "channel")
e.domain(0.86, 0.95, "channel")
e.domain(0.42, 0.57, "positive")
e.domain(0.62, 0.77, "highlight")
e.domain(0.17, 0.3, "drug")
e.domain(0.79, 0.88, "drug")
genes.append([("hunchback", "channel"), ("Krüppel", "positive"), ("knirps", "highlight"), ("giant", "drug")])
# pair-rule
e = D.FlyEmbryo(ax, (X, rows[2]), L, H)
eve = 0.31 + 0.07 * np.arange(7)
e.stripes(eve, 0.03, "receptor")
e.stripes(eve + 0.035, 0.03, "na")
genes.append([("even-skipped", "receptor"), ("fushi tarazu", "na")])
# segment polarity
e = D.FlyEmbryo(ax, (X, rows[3]), L, H)
en = 0.31 - 0.015 + 0.035 * np.arange(14)
e.stripes(en - 0.011, 0.01, "positive")
e.stripes(en + 0.0, 0.012, "channel")
genes.append([("engrailed", "channel"), ("wingless", "positive")])

for (y, names) in zip(rows, genes):
    step = 2.3 if len(names) > 2 else 3.2
    xs = X + (np.arange(len(names)) - (len(names) - 1) / 2) * step
    for (g, tok), xx in zip(names, xs):
        ax.add_patch(bio.core.FancyBboxPatch((xx - 1.05, y - H / 2 - 0.58), 0.28, 0.24, boxstyle="round,pad=0,rounding_size=0.05",
                                             facecolor=P.edge(tok), edgecolor="none", zorder=12))
        bio.label(ax, (xx - 0.65, y - H / 2 - 0.46), g, size="small", italic=True, ha="left")

# axis below the last embryo
y0 = rows[-1] - H / 2 - 1.05
x0, x1 = X - L / 2, X + L / 2
ax.plot([x0, x1], [y0, y0], color=P.muted(), lw=0.8)
for f in (0, 0.25, 0.5, 0.75, 1.0):
    ax.plot([x0 + f * L] * 2, [y0, y0 - 0.1], color=P.muted(), lw=0.8)
    bio.label(ax, (x0 + f * L, y0 - 0.32), f"{int(f * 100)}", size="tiny", color=P.muted())
bio.label(ax, (X, y0 - 0.75), "position / % egg length (anterior → posterior)", size="small", color=P.muted())
bio.label(ax, (x0 - 0.2, rows[0] + H / 2 + 0.35), "anterior", size="small", ha="left", color=P.muted())
bio.label(ax, (x1 + 0.2, rows[0] + H / 2 + 0.35), "posterior", size="small", ha="right", color=P.muted())
