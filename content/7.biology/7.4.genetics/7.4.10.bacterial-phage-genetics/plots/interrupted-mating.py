# Interrupted mating (HfrH x F-): model recombinant frequencies against time, and entry time against map order
import numpy as np
import wikibio as bio
from wikibio import charts, transmission as T

fig, ax = bio.canvas(19, 7.6)
markers = [("azi", 9.0, "dna"), ("ton", 11.0, "enzyme"), ("lac", 18.0, "receptor"), ("gal", 25.0, "antibody")]
lam = 0.06
t = np.linspace(0, 60, 600)
a = charts.axes_at(ax, (1.4, 1.2, 8.0, 5.7))
for name, te, tok in markers:
    f = 100 * T.interrupted_mating(t, te, plateau=np.exp(lam * 7.0), lam=lam, rise=4.0)
    a.plot(t, f, color=charts.line(tok), lw=2)
    a.text(60.5, f[-1], name, color=charts.line(tok), fontsize=8, style="italic", va="center")
    a.axvline(te, color=charts.line(tok), lw=0.6, ls=":")
a.set_xlim(0, 60)
a.set_ylim(0, 100)
charts.style_axes(a, "time of interruption / min", "recombinants with donor allele / %")
charts.title(a, "A   time course of marker entry")

b = charts.axes_at(ax, (12.0, 1.2, 6.2, 5.7))
pos = [0, 2, 9, 16]  # minutes after azi on the map
b.plot([p + 9 for p in pos], [m[1] for m in markers], "-", color=charts.line("neutral"), lw=1)
for (name, te, tok), p in zip(markers, pos):
    b.plot([p + 9], [te], "o", color=charts.line(tok), ms=6)
    b.text(p + 9.8, te - 0.4, name, fontsize=8, style="italic", color=bio.P.ink(), va="top")
b.set_xlim(5, 30)
b.set_ylim(5, 30)
charts.style_axes(b, "map position / min", "entry time / min")
charts.title(b, "B   entry time = map position")
