"""The optimal parental investment per offspring (after Trivers 1972; Davies, Krebs and West 2012).

A: the benefit to an offspring of an investment x, B(x) = 1 - exp(-x), shows diminishing returns as its needs
are met; the cost to the parent, C(x) = k x^1.5 (resources withheld from current and future offspring), keeps
increasing. The parent's optimum maximizes B - C, where the slopes are equal, B'(x) = C'(x).
B: the optimum falls as the cost of investment rises, for example when the parent's prospects of future
reproduction (whose loss is the cost) are better. Dots: k = 0.15 and k = 0.4, shown in A.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
x = np.linspace(0, 5, 20001)


def opt(k):
    v = (1 - np.exp(-x)) - k * x ** 1.5
    return x[v.argmax()], v.max()


fig, ax = bio.canvas(30.0, 10.5)
pa = Ch.axes_at(ax, (2.6, 1.8, 10.8, 7.6))
pa.plot(x, 1 - np.exp(-x), color=P.ink(), lw=1.9)
pa.text(4.9, 1.02, "benefit $B$", fontsize=FS["tiny"], color=P.ink(), ha="right", va="bottom")
for k, tok in ((0.15, "dna"), (0.4, "rna")):
    pa.plot(x, k * x ** 1.5, color=Ch.line(tok), lw=1.5, ls=(0, (4, 2)))
    pa.plot(x, 1 - np.exp(-x) - k * x ** 1.5, color=Ch.line(tok), lw=1.8)
    xo, vo = opt(k)
    pa.plot([xo], [vo], "o", color=Ch.line(tok), ms=6)
    pa.axvline(xo, color=Ch.line(tok), lw=0.7, ls=(0, (1, 2)))
pa.text(3.3, 1.45, "cost $C$, high", fontsize=FS["tiny"], color=Ch.line("rna"))
pa.text(4.2, 0.95, "cost $C$, low", fontsize=FS["tiny"], color=Ch.line("dna"), ha="left", va="top")
pa.text(0.1, 0.62, "$B - C$", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 5)
pa.set_ylim(-0.4, 1.6)
Ch.style_axes(pa, "parental investment per offspring $x$", "fitness")
Ch.title(pa, "Diminishing benefits, increasing costs")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.6))
ks = np.linspace(0.05, 0.8, 120)
pb.plot(ks, [opt(k)[0] for k in ks], color=Ch.line("protein"), lw=1.9)
for k, tok in ((0.15, "dna"), (0.4, "rna")):
    pb.plot([k], [opt(k)[0]], "o", color=Ch.line(tok), ms=6)
pb.set_xlim(0, 0.8)
pb.set_ylim(0, 3.2)
Ch.style_axes(pb, "cost coefficient $k$ (value of future reproduction)", "optimal investment $x^*$")
Ch.title(pb, "Invest less when the future is worth more")
bio.panel(ax, "B", (16.0, 10.2))
