"""Amplification in the epinephrine cascade of a hepatocyte: an order-of-magnitude illustration.

Bars: the number of molecules activated (or, for cAMP and glucose 1-phosphate, produced)
at each stage for one occupied receptor; the gain of each step is written above the arrow between bars.
Assumed gains (illustrative, chosen within the ranges discussed in the text): one occupied receptor
activates about 100 Gs during its active lifetime; each Gs-alpha-GTP activates one adenylyl cyclase,
which makes about 100 cAMP during the life of the complex; four cAMP free two catalytic subunits of
PKA (a loss, factor 0.5); each PKA catalytic subunit phosphorylates about 10 phosphorylase kinase
molecules, each of which activates about 100 glycogen phosphorylase molecules, each releasing about
100 glucose 1-phosphate from glycogen. Overall gain about 5 x 10^8; the actual numbers depend on cell
type and conditions, and are given here only to show how the gains of successive catalytic steps multiply.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def sci(n):
    e = int(np.floor(np.log10(n) + 1e-9))
    m = n / 10**e
    if e < 2:
        return f"{n:g}"
    return (f"{m:g}×" if abs(m - 1) > 1e-9 else "") + "10" + str(e).translate(SUP)

fig, ax = bio.canvas(19.0, 8.6)
pa = charts.axes_at(ax, (1.8, 1.9, 16.6, 5.6))
stages = [("epinephrine-\nreceptor", 1, "receptor"), ("Gsα·GTP", 100, "positive"), ("adenylyl\ncyclase", 100, "enzyme"),
          ("cAMP", 1e4, "highlight"), ("PKA C", 5e3, "enzyme"), ("phosphorylase\nkinase", 5e4, "protein"),
          ("phosphorylase a", 5e6, "antibody"), ("glucose\n1-phosphate", 5e8, "carbohydrate")]
gains = ["×100", "×1", "×100", "×0.5", "×10", "×100", "×100"]
x = np.arange(len(stages))
for i, (name, n, tok) in enumerate(stages):
    pa.bar(i, n, 0.62, color=P.fill(tok), edgecolor=charts.line(tok), lw=1.0, log=True)
    pa.text(i, n * 1.6, sci(n),
            ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
for i, g in enumerate(gains):
    top = max(stages[i][1], stages[i + 1][1]) * 12
    pa.annotate("", xy=(i + 0.82, top), xytext=(i + 0.18, top),
                arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.9, shrinkA=0, shrinkB=0))
    pa.text(i + 0.5, top * 2.0, g, ha="center", fontsize=bio.core.FONT["small"], color=charts.line("negative") if g in ("×1", "×0.5") else P.ink(),
            weight="bold")
pa.set_yscale("log")
pa.set_ylim(0.5, 3e11)
pa.set_xlim(-0.6, len(stages) - 0.4)
pa.set_xticks(x, [s[0] for s in stages])
charts.style_axes(pa, None, "molecules (per occupied receptor)")
pa.tick_params(axis="x", labelsize=bio.core.FONT["tiny"])
charts.title(pa, "Gains multiply: overall about 5 × 10⁸ (illustrative values)")
