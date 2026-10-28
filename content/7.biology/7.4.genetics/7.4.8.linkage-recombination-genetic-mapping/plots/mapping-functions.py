# Haldane and Kosambi mapping functions and their inverses
import numpy as np
import wikibio as bio
from wikibio import charts, transmission as T

fig, ax = bio.canvas(18, 7.5)
d = np.linspace(0, 1.5, 400)
a1 = charts.axes_at(ax, (1.4, 1.2, 6.8, 5.6))
a1.plot(d * 100, np.minimum(d, 0.75), color=charts.line("neutral"), lw=1.3, ls="--", label="r = d")
a1.plot(d * 100, T.haldane(d), color=charts.line("dna"), lw=2, label="Haldane")
a1.plot(d * 100, T.kosambi(d), color=charts.line("receptor"), lw=2, label="Kosambi")
a1.axhline(0.5, color=charts.line("neutral"), lw=0.8, ls=":")
a1.set_xlim(0, 150)
a1.set_ylim(0, 0.6)
charts.style_axes(a1, "map distance d / cM", "recombination frequency r")
leg = a1.legend(frameon=False, fontsize=8, loc="lower right")
for t in leg.get_texts():
    t.set_color(bio.P.ink())
charts.title(a1, "A   r as a function of d")

r = np.linspace(0, 0.47, 400)
a2 = charts.axes_at(ax, (10.4, 1.2, 6.8, 5.6))
a2.plot(r, r * 100, color=charts.line("neutral"), lw=1.3, ls="--")
a2.plot(r, T.haldane_inv(r) * 100, color=charts.line("dna"), lw=2)
a2.plot(r, T.kosambi_inv(r) * 100, color=charts.line("receptor"), lw=2)
for rr in (0.3,):
    for f, tok in ((T.haldane_inv, "dna"), (T.kosambi_inv, "receptor")):
        a2.plot([rr], [f(rr) * 100], "o", color=charts.line(tok), ms=4)
a2.set_xlim(0, 0.5)
a2.set_ylim(0, 150)
charts.style_axes(a2, "recombination frequency r", "map distance d / cM")
charts.title(a2, "B   d as a function of r")
