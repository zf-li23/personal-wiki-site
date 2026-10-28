# Tetrad frequencies under the Haldane model and the accuracy of distance estimates from tetrads
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts, transmission as T

fig, ax = bio.canvas(19, 7.6)
d = np.linspace(0, 1.5, 300)
pd, npd, t = T.tetrad_freqs(d)
a = charts.axes_at(ax, (1.4, 1.2, 7.2, 5.7))
a.plot(d * 100, pd, color=charts.line("dna"), lw=2, label="PD")
a.plot(d * 100, t, color=charts.line("enzyme"), lw=2, label="T")
a.plot(d * 100, npd, color=charts.line("receptor"), lw=2, label="NPD")
a.plot(d * 100, T.mii_freq(d), color=charts.line("neutral"), lw=1.2, ls="--", label="MII (gene to centromere)")
a.axhline(2 / 3, color=charts.line("neutral"), lw=0.7, ls=":")
a.axhline(1 / 6, color=charts.line("neutral"), lw=0.7, ls=":")
a.text(150, 2 / 3 + 0.02, "2/3", ha="right", fontsize=7.5, color=bio.P.ink())
a.text(150, 1 / 6 + 0.02, "1/6", ha="right", fontsize=7.5, color=bio.P.ink())
a.set_xlim(0, 150)
a.set_ylim(0, 1.02)
charts.style_axes(a, "map distance d / cM", "frequency")
leg = a.legend(frameon=False, fontsize=7.5, loc="lower right", bbox_to_anchor=(1.0, 0.22))
for x in leg.get_texts():
    x.set_color(bio.P.ink())
charts.title(a, "A   tetrad types without interference")

b = charts.axes_at(ax, (11.0, 1.2, 7.2, 5.7))
dd = np.linspace(0.001, 1.0, 200)
pd, npd, t = T.tetrad_freqs(dd)
rf = npd + t / 2
perk = (t + 6 * npd) / 2


def invert(n):
    return brentq(lambda x: float(T.tetrad_freqs(x)[1]) - n, 1e-9, 20)


exact = np.array([invert(n) for n in npd])
b.plot(dd * 100, dd * 100, color=charts.line("neutral"), lw=1, ls=":")
b.plot(dd * 100, rf * 100, color=charts.line("receptor"), lw=2, label="NPD + T/2 (uncorrected)")
b.plot(dd * 100, perk * 100, color=charts.line("dna"), lw=2, label="Perkins")
b.plot(dd * 100, exact * 100, color=charts.line("enzyme"), lw=1.6, ls="--", label="exact (NPD inverted)")
b.set_xlim(0, 100)
b.set_ylim(0, 100)
charts.style_axes(b, "true distance / cM", "estimated distance / cM")
leg = b.legend(frameon=False, fontsize=7.5, loc="upper left")
for x in leg.get_texts():
    x.set_color(bio.P.ink())
charts.title(b, "B   distance estimates")
