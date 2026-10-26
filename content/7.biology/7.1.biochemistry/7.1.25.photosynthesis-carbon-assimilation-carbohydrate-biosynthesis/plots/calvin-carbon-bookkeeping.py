"""Carbon bookkeeping in stage 3 of the Calvin cycle, and why the cycle is autocatalytic.

A: five triose phosphates (15 carbons; two dihydroxyacetone phosphate, DHAP, and three glyceraldehyde
3-phosphate, G3P) are rearranged into three pentose phosphates (15 carbons). Each dot is one carbon,
coloured by the triose phosphate it came from. Aldolase joins DHAP (carbons 1-3 of the product) to an
aldose (C3 or C4); FBPase and SBPase remove the 1-phosphate; transketolase moves carbons 1-2 of a
ketose (F6P, S7P) to G3P. Steps: (1) DHAP + G3P -> F1,6BP -> F6P; (2) F6P + G3P -> E4P + X5P;
(3) E4P + DHAP -> SBP -> S7P; (4) S7P + G3P -> R5P + X5P; R5P and two X5P become 3 Ru5P, which
phosphoribulokinase converts to 3 RuBP.
B: if a fraction f of the triose phosphate made is withdrawn, each round turns 3 RuBP into
6 (1 - f) triose phosphate, of which five sixths of the remainder rebuild RuBP: the RuBP pool is
multiplied by g = 6 (1 - f) / 5 per round. f = 1/6 is the steady state; smaller f lets the pool grow
(the induction period after a dark period); larger f drains it.
"""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(27.0, 12.6, scale=0.42)
SRC = {"a": "carbohydrate", "b": "dna", "c": "rna", "d": "lipid", "e": "atp"}


def mol(x, y, name, carbons, w=None):
    """A molecule box with its name above a row of carbon dots coloured by origin."""
    n = len(carbons)
    w = w or max(1.5, 0.36 * n + 0.5)
    ax.add_patch(FancyBboxPatch((x - w / 2, y - 0.55), w, 1.1, boxstyle="round,pad=0,rounding_size=0.18",
                                facecolor=P.surface(), edgecolor=P.muted(), lw=0.9, zorder=10))
    bio.label(ax, (x, y + 0.22), name, size="tiny", bold=True, zorder=12)
    x0 = x - 0.36 * (n - 1) / 2
    for k, s in enumerate(carbons):
        ax.add_patch(Circle((x0 + 0.36 * k, y - 0.22), 0.13, facecolor=P.fill(SRC[s]), edgecolor=P.edge(SRC[s]),
                            lw=0.8, zorder=12))
    return w


def step(x0, x1, y, text, side=None):
    bio.arrow(ax, (x0, y), (x1, y), kind="process", head=0.2)
    bio.label(ax, ((x0 + x1) / 2, y + 0.3), text, size="tiny", bold=True, color=P.edge("enzyme"))
    if side:
        bio.label(ax, ((x0 + x1) / 2, y - 0.3), side, size="tiny", color=P.muted())


def plus(x, y):
    bio.label(ax, (x, y), "+", size="normal")


bio.panel(ax, "A", (0.2, 12.4))
rows = [11.0, 8.6, 6.2, 3.8]
# (1) aldolase + FBPase
y = rows[0]
mol(1.4, y, "DHAP", "bbb"); plus(2.6, y); mol(3.8, y, "G3P", "aaa")
step(4.8, 6.8, y, "aldolase")
mol(8.3, y, "F1,6BP", "bbbaaa")
step(9.8, 11.6, y, "FBPase", "−Pᵢ")
mol(13.1, y, "F6P", "bbbaaa")
# (2) transketolase
y = rows[1]
mol(1.4, y, "F6P", "bbbaaa"); plus(2.85, y); mol(4.1, y, "G3P", "ccc")
step(5.1, 7.4, y, "transketolase", "C1–C2 of F6P → G3P")
mol(8.9, y, "E4P", "baaa"); plus(10.1, y); mol(11.4, y, "X5P", "bbccc")
# (3) aldolase + SBPase
y = rows[2]
mol(1.4, y, "E4P", "baaa"); plus(2.6, y); mol(3.8, y, "DHAP", "ddd")
step(4.8, 6.8, y, "aldolase")
mol(8.5, y, "SBP", "dddbaaa")
step(10.1, 11.9, y, "SBPase", "−Pᵢ")
mol(13.5, y, "S7P", "dddbaaa")
# (4) transketolase
y = rows[3]
mol(1.6, y, "S7P", "dddbaaa"); plus(3.2, y); mol(4.4, y, "G3P", "eee")
step(5.4, 7.7, y, "transketolase", "C1–C2 of S7P → G3P")
mol(9.2, y, "R5P", "dbaaa"); plus(10.5, y); mol(11.8, y, "X5P", "ddeee")
# final conversions
y = 1.3
mol(1.35, y, "R5P", "dbaaa"); plus(2.75, y); mol(4.15, y, "X5P", "bbccc"); plus(5.55, y); mol(6.95, y, "X5P", "ddeee")
step(8.25, 9.8, y, "isomerase,\nepimerase")
bio.box(ax, (11.1, y), 2.2, 1.1, "carbohydrate", text="3 Ru5P", size="small")
step(12.4, 14.0, y, "PRK", "3 ATP → 3 ADP")
bio.box(ax, (15.4, y), 2.2, 1.1, "carbohydrate", text="3 RuBP", size="small")
for k, (s, t) in enumerate((("a", "G3P 1"), ("b", "DHAP 1"), ("c", "G3P 2"), ("d", "DHAP 2"), ("e", "G3P 3"))):
    xx = 15.4
    yy = 11.4 - 0.55 * k
    ax.add_patch(Circle((xx, yy), 0.13, facecolor=P.fill(SRC[s]), edgecolor=P.edge(SRC[s]), lw=0.8, zorder=12))
    bio.label(ax, (xx + 0.3, yy), t, size="tiny", ha="left")
bio.label(ax, (15.25, 12.15), "carbon from", size="tiny", ha="left", color=P.muted())
bio.label(ax, (15.25, 8.0), "5 C₃ (15 C)\n→ 3 C₅ (15 C)", size="small", ha="left", bold=True)

# --- B: autocatalysis of the cycle --------------------------------------------------------------
bio.panel(ax, "B", (18.4, 12.4))
b = charts.axes_at(ax, (19.9, 2.0, 6.5, 9.4))
n = np.arange(0, 21)
for f, tok, lab in ((0.0, "positive", "f = 0"), (1 / 12, "dna", "f = 1/12"), (1 / 6, "neutral", "f = 1/6"),
                    (0.25, "negative", "f = 1/4")):
    g = 6 * (1 - f) / 5
    b.semilogy(n, g ** n, color=charts.line(tok), lw=2.0, marker="o", ms=2.5, label=lab)
b.set_xlim(0, 20)
b.set_ylim(0.05, 50)
charts.style_axes(b, "rounds of the cycle", "RuBP pool (relative)")
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left",
         title="fraction of triose\nphosphate withdrawn", title_fontsize=bio.core.FONT["tiny"])
b.get_legend().get_title().set_color(P.ink())
