"""Grobstein's experiments and the signals of reciprocal induction in the metanephros."""
from matplotlib.patches import Ellipse
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(26, 11)
P = bio.P
bio.panel(ax, "A", (0.2, 10.7))
cols = [(2.0, "Bud alone"), (6.0, "Mesenchyme alone"), (10.0, "Recombined")]
for x, t in cols:
    bio.label(ax, (x, 10.2), t, size="small", bold=True)
# bud alone: unbranched tube
M.tube(ax, [(2.0, 9.4), (2.0, 7.6)], 0.4, "ureteric", 5)
bio.label(ax, (2.0, 6.9), "no branching", size="tiny", color=P.muted())
# mesenchyme alone: dying cells
M.cells(ax, (6.0, 8.5), 1.0, 0.7, 25, "metanephric", 5, r=0.08, seed=2, faded=True)
bio.label(ax, (6.0, 6.9), "apoptosis", size="tiny", color=P.muted())
# recombined: branched + nephrons
ax.add_patch(Ellipse((10.0, 8.3), 3.2, 2.2, facecolor=P.light(M.tok("metanephric")), edgecolor=P.edge(M.tok("metanephric")), lw=0.8, zorder=4))
M.ureteric_tree(ax, (10.0, 9.5), -90, 3, 0.75, 6, width=0.07)
for (x, y) in ((8.9, 7.7), (11.1, 7.7), (9.6, 7.3), (10.5, 7.3)):
    ax.add_patch(Ellipse((x, y), 0.32, 0.22, facecolor=P.fill(M.tok("metanephric")), edgecolor=P.edge(M.tok("metanephric")), lw=0.6, zorder=7))
bio.label(ax, (10.0, 6.9), "branching + nephrons", size="tiny", color=P.muted())

bio.panel(ax, "B", (0.2, 5.6))
N = {"mm": (3.0, 3.0, "Metanephric mesenchyme\n(cap)", "carbohydrate", 4.2),
     "gdnf": (8.0, 4.4, "GDNF", "carbohydrate", 1.8), "ret": (12.6, 4.4, "RET / GFRa1", "channel", 2.6),
     "ub": (18.0, 3.0, "Ureteric bud\n(tip and stalk)", "channel", 3.8), "wnt11": (12.6, 2.9, "Wnt11", "dna2", 1.8),
     "surv": (8.0, 1.6, "FGF2/9, BMP7", "dna2", 2.6), "wnt9b": (12.6, 0.6, "Wnt9b", "dna2", 1.8),
     "met": (3.0, 0.75, "Wnt4: MET, nephron", "metabolite", 3.6), "ra": (22.8, 4.6, "RA (stroma)", "positive", 2.6),
     "inh": (22.8, 1.2, "Spry1, BMP4 (Gremlin1),\nSlit2-Robo2, Foxc1/2", "negative", 4.8)}
for k, (x, y, t, tok, w) in N.items():
    bio.box(ax, (x, y), w, 0.95 if "\n" not in t else 1.25, token=tok, text=t, size="small")
bio.arrow(ax, (5.1, 3.6), (7.1, 4.3), kind="process")
bio.arrow(ax, (8.9, 4.4), (11.3, 4.4), kind="activation")
bio.arrow(ax, (13.9, 4.2), (16.1, 3.4), kind="activation")
bio.label(ax, (15.3, 4.4), "budding, branching", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (16.1, 2.9), (13.5, 2.9), kind="process")
bio.arrow(ax, (11.7, 2.9), (5.1, 3.0), kind="activation")
bio.label(ax, (8.2, 3.25), "maintains GDNF", size="tiny", color=P.muted())
bio.arrow(ax, (16.1, 2.5), (9.3, 1.7), kind="process")
bio.arrow(ax, (6.7, 1.7), (4.6, 2.3), kind="activation")
bio.label(ax, (5.0, 1.55), "survival", size="tiny", color=P.muted())
bio.arrow(ax, (16.1, 2.2), (13.5, 0.7), kind="process")
bio.arrow(ax, (11.7, 0.65), (4.8, 0.75), kind="activation")
bio.arrow(ax, (21.5, 4.4), (14.0, 4.6), kind="activation", bend=0.15)
bio.arrow(ax, (20.4, 1.6), (19.6, 2.4), kind="inhibition")
