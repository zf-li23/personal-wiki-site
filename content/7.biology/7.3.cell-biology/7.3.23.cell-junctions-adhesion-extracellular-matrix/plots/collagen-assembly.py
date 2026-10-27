"""From polypeptide chains to collagen fibers (type I collagen; schematic, lengths not to scale except where stated).

A: every third residue of the helical domain is glycine (Gly-X-Y, X often proline, Y often hydroxyproline):
only glycine fits in the crowded centre of the triple helix formed by two alpha1(I) chains and one alpha2(I)
chain. B: the pathway. In the ER, prolines and lysines are hydroxylated (prolyl and lysyl hydroxylases,
which need ascorbate), some hydroxylysines are glycosylated, and three pro-alpha chains are aligned by
their C-propeptides and zip into procollagen; procollagen leaves the ER in enlarged COPII carriers, is
packaged in the Golgi and secreted; outside the cell procollagen proteinases remove both propeptides, the
resulting collagen molecules (300 nm x 1.5 nm) self-assemble into fibrils, and lysyl oxidase cross-links
them. C: the quarter-staggered packing: molecules 4.46 D long are separated by 0.54 D gaps and each row is
shifted by D = 67 nm; the gap zones (shaded) have four molecules per five and stain more heavily, giving the
banding of fibrils (D) seen by electron microscopy. Fibrils of 10-300 nm diameter are bundled into fibers (E).
"""

import numpy as np

import wikibio as bio
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(28.0, 13.4)

# A: sequence and helix
bio.panel(ax, "A", (0.1, 13.3))
seq = "G P O G A O G P R G E O G P O G"
xs = np.linspace(0.8, 9.4, 16)
for k, (x, ch) in enumerate(zip(xs, seq.split())):
    tokn = "highlight" if ch == "G" else (J.tok("collagen") if ch in "PO" else "neutral")
    bio.box(ax, (x, 12.1), 0.5, 0.5, tokn, text=ch, size="tiny", radius=0.12)
bio.label(ax, (5.1, 11.4), "Gly-X-Y repeats (G glycine, P proline, O hydroxyproline)", size="tiny", color=P.muted())
J.triple_helix(ax, (0.8, 10.2), (9.4, 10.2), width=0.42, tokens=("collagen", "collagen", "secondary"), shades=(0.0, 0.3, 0.0))
bio.label(ax, (10.0, 10.55), "α1(I)", size="tiny", ha="left")
bio.label(ax, (10.0, 10.2), "α1(I)", size="tiny", ha="left")
bio.label(ax, (10.0, 9.85), "α2(I)", size="tiny", ha="left")
bio.label(ax, (5.1, 9.45), "Triple helix, 1.5 nm wide", size="tiny", color=P.muted())

# B: biosynthesis pathway
bio.panel(ax, "B", (12.4, 13.3))
ax.add_patch(__import__("matplotlib").patches.FancyBboxPatch((12.8, 7.9), 7.4, 4.9, boxstyle="round,pad=0,rounding_size=0.5",
             facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=2.2, zorder=1))
bio.label(ax, (13.1, 12.5), "Fibroblast", size="small", ha="left", bold=True)
bio.er(ax, (14.6, 10.6), 2.4, 1.7, sheets=3)
bio.golgi(ax, (18.2, 10.9), 1.7, cisternae=4)
steps = [((14.6, 9.25), "ER: hydroxylation (vitamin C),\nglycosylation, triple helix"),
         ((18.2, 9.7), "Golgi:\npackaging")]
for xy, txt in steps:
    bio.label(ax, xy, txt, size="tiny")
# procollagen in ER and Golgi
for x0, y0 in ((13.9, 11.0), (17.6, 11.75)):
    J.triple_helix(ax, (x0, y0), (x0 + 1.3, y0), width=0.16, tokens=("collagen", "collagen", "secondary"), shades=(0, 0.3, 0))
    bio.molecule(ax, (x0 - 0.12, y0), "neutral", r=0.12)
    bio.molecule(ax, (x0 + 1.45, y0), "neutral", r=0.16)
bio.arrow(ax, (15.8, 11.0), (17.3, 11.6), kind="process", bend=-0.15)
bio.arrow(ax, (19.4, 11.6), (21.4, 11.6), kind="process")
bio.label(ax, (21.6, 12.45), "Secretion; propeptides cleaved", size="tiny", ha="left")
J.triple_helix(ax, (21.6, 11.6), (24.6, 11.6), width=0.16, tokens=("collagen", "collagen", "secondary"), shades=(0, 0.3, 0))
for x, r in ((21.3, 0.12), (25.0, 0.16)):
    bio.molecule(ax, (x, 10.9), "neutral", r=r)
bio.label(ax, (23.1, 10.9), "N- and C-propeptides", size="tiny", color=P.muted())
bio.label(ax, (25.0, 11.6), "Collagen molecule\n300 nm", size="tiny", ha="left")
bio.arrow(ax, (23.6, 10.5), (23.6, 9.0), kind="process")
bio.label(ax, (23.8, 9.75), "Self-assembly;\nlysyl oxidase cross-links", size="tiny", ha="left")
bio.label(ax, (16.5, 8.3), "Procollagen in enlarged COPII carriers", size="tiny", color=P.muted())

# C: quarter stagger
bio.panel(ax, "C", (0.1, 8.2))
D = 1.6
res = J.collagen_fibril(ax, (0.8, 4.4), 15.0, rows=5, D=D, row_h=0.42, width=0.22)
g0, g1 = res["gap"]
o0, o1 = res["overlap"]
y = 4.4 + 5 * 0.42 + 0.1
ax.annotate("", xy=(g0, y), xytext=(g0 + D, y), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.9, shrinkA=0, shrinkB=0))
bio.label(ax, (g0 + D / 2, y + 0.3), "D = 67 nm", size="tiny")
bio.label(ax, ((g0 + g1) / 2, 3.65), "gap", size="tiny", color=P.muted())
bio.label(ax, ((o0 + o1) / 2, 3.65), "overlap", size="tiny", color=P.muted())
bio.label(ax, (16.3, 5.3), "Quarter-staggered\nmolecules in a fibril", size="tiny", ha="left")

# D: banded fibril; E: fiber
bio.panel(ax, "D", (0.1, 3.0))
J.banded_fibril(ax, (0.8, 1.6), (15.8, 1.6), width=0.75, D=D)
bio.label(ax, (8.3, 0.55), "Collagen fibril (10–300 nm), banded with period D", size="tiny", color=P.muted())
bio.panel(ax, "E", (19.2, 7.0))
rng = np.random.default_rng(1)
for k in range(9):
    y0 = 2.2 + k * 0.42
    J.banded_fibril(ax, (19.8 + rng.uniform(0, 0.4), y0), (27.2 - rng.uniform(0, 0.4), y0 + 0.05), width=0.32, D=0.7)
bio.label(ax, (23.5, 1.5), "Collagen fiber: a bundle of fibrils (µm)", size="tiny", color=P.muted())
