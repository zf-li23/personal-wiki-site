# Epitopes and the hapten-carrier effect.
# A: one polypeptide drawn as a sequence bar and as a folded chain; a linear B-cell epitope is one contiguous
#    stretch, a conformational B-cell epitope joins two distant stretches that meet at the surface, a T-cell
#    epitope is a short stretch that may be buried and is shown to T cells only after processing.
# B: hapten-carrier effect: linked recognition of hapten (B cell) and carrier peptide (helper T cell).
import numpy as np
from matplotlib.patches import FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path
from scipy.interpolate import splev, splprep

import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(18.0, 8.6)

# --- A  one chain, three kinds of epitope -------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.4))
bio.label(ax, (4.6, 8.25), "Epitopes on one polypeptide", size="title", bold=True)

LIN = (0.36, 0.46)          # linear B-cell epitope: contiguous residues
CONF = ((0.08, 0.15), (0.80, 0.88))   # conformational epitope: two distant stretches
TCE = (0.55, 0.66)          # T-cell epitope (buried)
groups = [(LIN, "negative"), (CONF[0], "channel"), (CONF[1], "channel"), (TCE, "highlight")]


def tok_at(u):
    for (a, b), tok in groups:
        if a <= u <= b:
            return tok
    return None


# sequence bar
n = 30
x0, wbar = 0.7, 7.8
for i in range(n):
    u = (i + 0.5) / n
    tok = tok_at(u)
    ax.add_patch(FancyBboxPatch((x0 + i * wbar / n, 7.0), wbar / n * 0.9, 0.5, boxstyle="round,pad=0,rounding_size=0.05",
                                facecolor=P.fill(tok or "neutral") if tok else P.light("neutral"),
                                edgecolor=P.edge(tok or "neutral"), lw=0.6, zorder=5))
bio.label(ax, (x0, 7.75), "N", size="small", ha="left", color=P.muted())
bio.label(ax, (x0 + wbar, 7.75), "C", size="small", ha="right", color=P.muted())
bio.label(ax, (x0 + wbar / 2, 6.65), "primary sequence", size="tiny", color=P.muted())
bio.arrow(ax, (4.6, 6.4), (4.6, 5.8), kind="process")
bio.label(ax, (5.2, 6.1), "folding", size="tiny", ha="left", color=P.muted())

# folded chain: a smooth space curve through hand-placed control points
ctrl = np.array([
    (1.9, 1.7), (1.6, 2.7), (2.1, 3.6), (3.0, 4.2), (3.9, 3.9), (4.4, 3.0), (5.2, 2.2), (6.2, 2.1), (7.0, 2.8),
    (7.1, 3.8), (6.3, 4.5), (5.3, 4.4), (4.7, 3.7), (5.1, 3.0), (5.9, 3.2), (6.0, 3.9), (5.0, 4.9), (3.7, 5.0),
    (2.6, 4.6), (2.3, 3.7), (3.2, 3.3), (3.9, 2.6), (3.5, 1.7)])
tck, _ = splprep(ctrl.T, s=0, k=3)
uu = np.linspace(0, 1, 600)
cx, cy = splev(uu, tck)
glob = bio.blob((4.55, 3.4), 3.3, 2.5, wobble=0.04, seed=3, k=7)
ax.add_patch(PathPatch(Path(glob, closed=True), facecolor=P.light("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=2))
ax.plot(cx, cy, color=P.edge("neutral"), lw=2.0, zorder=4, solid_capstyle="round")
for (a, b), tok in groups:
    m = (uu >= a) & (uu <= b)
    ax.plot(cx[m], cy[m], color=P.edge(tok), lw=5.5, zorder=6, solid_capstyle="round")
    ax.plot(cx[m], cy[m], color=P.fill(tok), lw=3.8, zorder=7, solid_capstyle="round")

# legend
y0 = 0.4
for k, (tok, txt) in enumerate((("negative", "linear B-cell epitope"),
                                ("channel", "conformational B-cell epitope"),
                                ("highlight", "T-cell epitope"))):
    xx = (0.3, 3.3, 7.4)[k]
    ax.plot([xx, xx + 0.5], [y0, y0], color=P.fill(tok), lw=4, solid_capstyle="round", zorder=6)
    bio.label(ax, (xx + 0.65, y0), txt, size="tiny", ha="left")

# --- B  hapten-carrier effect ----------------------------------------------------------------------------------
bio.panel(ax, "B", (9.6, 8.4))
bio.label(ax, (14.0, 8.25), "Hapten-carrier effect", size="title", bold=True)
ym, yt = 2.8, 5.6
bio.box(ax, (13.8, 1.75), 7.6, 2.1, "neutral", None, radius=0.5)
bio.box(ax, (13.8, 6.9), 7.6, 1.8, "neutral", None, radius=0.5)
bio.label(ax, (13.8, 1.2), "hapten-specific B cell", size="small", color=P.on_fill())
bio.label(ax, (13.8, 7.35), "carrier-specific helper T cell (CD4)", size="small", color=P.on_fill())
# the BCR binds the hapten on the carrier
immuno.bcr(ax, 11.3, ym, up=1, size=1.0)
cp = bio.blob((11.25, 5.15), 0.75, 0.65, wobble=0.07, seed=5, k=7)
ax.add_patch(PathPatch(Path(cp, closed=True), facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.0, zorder=9))
bio.label(ax, (11.25, 5.25), "carrier", size="tiny", color=P.on_fill(), zorder=21)
ax.add_patch(Polygon([(10.72, 4.2), (10.87, 4.0), (11.02, 4.2), (10.87, 4.4)], closed=True, facecolor=P.fill("negative"),
                     edgecolor=P.edge("negative"), lw=0.8, zorder=11))
bio.callout(ax, (10.74, 4.2), (9.9, 4.7), "hapten", size="tiny")
# the processed carrier peptide on MHC II is recognised by the TCR of the helper T cell
immuno.mhc_ii(ax, 15.2, ym, up=1)
immuno.tcr(ax, 15.2, yt, up=-1, cd3=False)
bio.arrow(ax, (12.2, 5.0), (14.0, 4.25), kind="process", dashed=True, bend=-0.2)
bio.label(ax, (12.9, 5.55), "internalise,\nprocess", size="tiny", color=P.muted())
bio.label(ax, (13.3, 3.3), "peptide–MHC II", size="tiny", color=P.muted())
# CD40L-CD40 and cytokines return help to the B cell
bio.arrow(ax, (17.4, 5.6), (17.4, 2.9), kind="activation")
bio.label(ax, (17.1, 4.25), "CD40L → CD40, cytokines", size="tiny", rotation=90)
bio.label(ax, (13.8, 0.3), "help reaches the B cell that recognised the hapten", size="tiny", color=P.muted())
