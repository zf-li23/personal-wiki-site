"""The energy ledger of metabolism, assembled from the pathway cards of 7.1.18-7.1.28.

A: ATP yield per molecule of fuel (P/O = 2.5 for NADH, 1.5 for FADH2; glucose 30 or 32 depending
on the shuttle for cytosolic NADH; palmitate 7n - 6 = 106; beta-hydroxybutyrate = 2 acetyl-CoA
+ 1 NADH - 1 GTP for CoA transfer).
B: the same yields per carbon atom: reduced fatty acid carbon gives more than carbohydrate carbon.
C: costs of biosynthesis per molecule of product, as high-energy phosphates (ATP, GTP, UTP, CTP
equivalents) and as reduced carriers (NADH or NADPH), side by side.
"""

import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio.core import FONT

P = bio.P
fig, ax = bio.canvas(30, 11.5, scale=0.5)

# ---- A and B: yields -------------------------------------------------------------------------
fuels = [  # name, ATP (low, high), carbons
    ("Glucose → 2 lactate", (2, 2), 6),
    ("Glycogen residue → 2 lactate", (3, 3), 6),
    ("Pyruvate", (12.5, 12.5), 3),
    ("Acetyl-CoA", (10, 10), 2),
    ("Glucose (aerobic)", (30, 32), 6),
    ("β-Hydroxybutyrate", (21.5, 21.5), 4),
    ("Palmitate", (106, 106), 16),
]
names = [f[0] for f in fuels]
y = np.arange(len(fuels))[::-1]
colors = [charts.line("carbohydrate")] * 2 + [charts.line("metabolite")] * 2 + [charts.line("carbohydrate"),
                                                                              charts.line("lipid_head"),
                                                                              charts.line("lipid_head")]

a = charts.axes_at(ax, (6.2, 1.4, 7.4, 8.6))
for yi, (n, (lo, hi), c), col in zip(y, fuels, colors):
    a.barh(yi, hi, color=col, height=0.62, alpha=0.9)
    a.text(hi + 1.5, yi, f"{lo:g}–{hi:g}" if lo != hi else f"{hi:g}", va="center", fontsize=FONT["tiny"],
           color=P.ink())
a.set_yticks(y)
a.set_yticklabels(names)
a.set_xlim(0, 125)
charts.style_axes(a, "ATP per molecule")
charts.title(a, "A  Yield per molecule")

b = charts.axes_at(ax, (15.0, 1.4, 4.2, 8.6))
for yi, (n, (lo, hi), c), col in zip(y, fuels, colors):
    v = hi / c
    b.barh(yi, v, color=col, height=0.62, alpha=0.9)
    b.text(v + 0.15, yi, f"{v:.1f}", va="center", fontsize=FONT["tiny"], color=P.ink())
b.set_yticks(y)
b.set_yticklabels([])
b.set_xlim(0, 8)
charts.style_axes(b, "ATP per carbon")
charts.title(b, "B  Yield per carbon")

# ---- C: costs --------------------------------------------------------------------------------
costs = [  # product, high-energy phosphates, reduced carriers
    ("Glucose\n(from 2 pyruvate)", 6, 2),
    ("Glycogen residue\n(from glucose)", 2, 0),
    ("Triose P\n(from 3 CO₂)", 9, 6),
    ("Palmitate", 23, 14),
    ("Cholesterol", 18, 16),
    ("IMP", 6, 0),
    ("UMP", 4, 0),
    ("Urea", 4, 0),
]
c = charts.axes_at(ax, (21.4, 2.6, 8.2, 7.4))
x = np.arange(len(costs))
w = 0.38
c.bar(x - w / 2, [k[1] for k in costs], w, color=charts.line("atp"), label="ATP equivalents")
c.bar(x + w / 2, [k[2] for k in costs], w, color=charts.line("channel"), label="NAD(P)H")
for xi, (_, p, r) in zip(x, costs):
    c.text(xi - w / 2, p + 0.4, f"{p}", ha="center", fontsize=FONT["tiny"], color=P.ink())
    if r:
        c.text(xi + w / 2, r + 0.4, f"{r}", ha="center", fontsize=FONT["tiny"], color=P.ink())
c.set_xticks(x)
c.set_xticklabels([k[0] for k in costs], rotation=55, ha="right", fontsize=FONT["tiny"])
c.set_ylim(0, 26)
charts.style_axes(c, None, "per molecule of product")
charts.title(c, "C  Cost of biosynthesis")
leg = c.legend(frameon=False, fontsize=FONT["tiny"], loc="upper left")
for t in leg.get_texts():
    t.set_color(P.ink())
