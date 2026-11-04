"""Sporulation in Bacillus subtilis: morphology and the compartmentalized sigma-factor cascade.
A: the stages. A vegetative cell divides near one pole (asymmetric septum), the larger mother cell
engulfs the smaller forespore so that it lies within a double membrane, the cortex and the coat are
laid down, the core is dehydrated and filled with calcium dipicolinate, and the mother cell lyses.
B: the cascade. Spo0A is phosphorylated through a relay from several sensor kinases; sigma-F is freed
in the forespore by the SpoIIE-SpoIIAA-SpoIIAB partner switch, and from then on each compartment
activates the next factor in the other one (diagonal arrows), so gene expression follows morphology:
sigma-F -> (SpoIIR) sigma-E -> engulfment and the SpoIIIA-SpoIIQ channel -> sigma-G -> (SpoIVB)
sigma-K."""

from matplotlib.patches import Ellipse, FancyBboxPatch

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(26.0, 12.4)

# ---------------------------------------------------------------- A: morphology
bio.panel(ax, "A", (0.2, 12.2))
yc = 10.4
xs = [3.0, 8.0, 13.0, 18.0, 23.0]
names = ["vegetative cell", "asymmetric septum", "engulfment", "cortex and coat", "lysis: free spore"]
for k, (x, name) in enumerate(zip(xs, names)):
    if k < 4:
        M.bacillus(ax, (x, yc), 3.6, 1.2, gram="+")
    bio.label(ax, (x, yc - 1.25), name, size="tiny", color=P.muted())
    if k == 0:
        bio.shape(ax, bio.blob((x, yc), 0.9, 0.3, seed=1), token="dna", lw=0.8, zorder=10)
    elif k == 1:
        ax.plot([x + 1.0, x + 1.0], [yc - 0.55, yc + 0.55], color=P.edge("bacterium"), lw=2.2, zorder=12)
        bio.shape(ax, bio.blob((x - 0.5, yc), 0.7, 0.28, seed=2), token="dna", lw=0.8, zorder=10)
        bio.shape(ax, bio.blob((x + 1.35, yc), 0.22, 0.22, seed=3), token="dna", lw=0.8, zorder=10)
    elif k in (2, 3):
        ax.add_patch(Ellipse((x + 0.85, yc), 1.3, 0.85, facecolor=P.fill("cytoplasm"),
                             edgecolor=P.edge("bacterium"), lw=1.6, zorder=11))
        if k == 3:
            ax.add_patch(Ellipse((x + 0.85, yc), 1.75, 1.1, facecolor="none", edgecolor=P.edge("cell_wall"),
                                 lw=2.2, zorder=12))
        bio.shape(ax, bio.blob((x + 0.85, yc), 0.3, 0.22, seed=4), token="dna", lw=0.8, zorder=13)
        bio.shape(ax, bio.blob((x - 0.8, yc), 0.6, 0.26, seed=5), token="dna", lw=0.8, zorder=10)
    else:
        ax.add_patch(Ellipse((x, yc), 1.8, 1.1, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"),
                             lw=2.6, zorder=11))
        bio.shape(ax, bio.blob((x, yc), 0.32, 0.24, seed=6), token="dna", lw=0.8, zorder=12)
    if k < 4:
        bio.arrow(ax, (x + 2.0, yc), (xs[k + 1] - 2.0, yc), kind="process", lw=1.0, head=0.16)
bio.callout(ax, (xs[2] + 0.85, yc + 0.45), (xs[2] + 0.6, yc + 1.9), "forespore", size="tiny")
bio.callout(ax, (xs[2] - 1.2, yc + 0.5), (xs[2] - 2.0, yc + 1.9), "mother cell", size="tiny")

# ---------------------------------------------------------------- B: cascade
bio.panel(ax, "B", (0.2, 7.6))
lane = {"fs": 5.6, "mc": 2.2}
for key, y, name, tok in (("mc", lane["mc"], "Mother cell", "extracellular"),
                          ("fs", lane["fs"], "Forespore", "cytoplasm")):
    ax.add_patch(FancyBboxPatch((2.6, y - 1.0), 22.8, 2.0, boxstyle="round,pad=0,rounding_size=0.3",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.1, zorder=1))
    bio.label(ax, (2.4, y), name, size="tiny", color=P.muted(), ha="right")

bio.box(ax, (4.6, 7.0), 3.0, 0.8, token="positive", text="Spo0A~P", size="small", radius=0.25, zorder=10)
bio.label(ax, (4.6, 7.9), "phosphorelay from five sensor kinases\n(starvation, cell density, DNA damage)",
          size="tiny", color=P.muted())


def sig(x, y, text, note=None):
    bio.box(ax, (x, y), 2.2, 0.8, token="enzyme", text=text, size="small", radius=0.25, zorder=10)
    if note:
        bio.label(ax, (x, y - 0.75), note, size="tiny", color=P.muted())


sig(6.4, lane["fs"], "σᶠ", "partner switch:\nSpoIIE, SpoIIAA, SpoIIAB")
sig(11.4, lane["mc"], "σᴱ", "pro-σᴱ cut by SpoIIGA")
sig(16.4, lane["fs"], "σᴳ", "needs the\nSpoIIIA–SpoIIQ channel")
sig(21.4, lane["mc"], "σᴷ", "pro-σᴷ cut by SpoIVFB")
bio.arrow(ax, (5.3, 6.7), (6.1, 6.1), kind="activation", lw=1.2, head=0.2)
for a, b, text in (((7.5, 5.2), (10.4, 2.6), "SpoIIR"), ((12.5, 2.6), (15.4, 5.2), "engulfment"),
                   ((17.5, 5.2), (20.4, 2.6), "SpoIVB")):
    bio.arrow(ax, a, b, kind="activation", lw=1.2, head=0.2)
    bio.label(ax, ((a[0] + b[0]) / 2 + 0.9, (a[1] + b[1]) / 2), text, size="tiny", color=P.muted())
bio.label(ax, (7.9, lane["fs"] + 0.8), "small acid-soluble\nspore proteins", size="tiny", ha="left")
bio.label(ax, (17.9, lane["fs"] + 0.8), "dehydration,\nCa–dipicolinate", size="tiny", ha="left")
bio.label(ax, (12.9, lane["mc"] + 0.55), "engulfment, cortex", size="tiny", ha="left")
bio.label(ax, (22.9, lane["mc"] + 0.55), "coat, lysis", size="tiny", ha="left")
bio.arrow(ax, (4.6, 6.6), (4.6, 3.0), kind="activation", lw=1.0, head=0.18, dashed=True)
bio.label(ax, (4.6, 1.0), "early mother-cell genes", size="tiny", color=P.muted())
bio.label(ax, (14.0, 0.3), "time →", size="tiny", color=P.muted())
