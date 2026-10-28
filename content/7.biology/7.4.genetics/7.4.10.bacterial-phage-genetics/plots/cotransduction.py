# Cotransduction frequency against distance: Wu's formula and a simulated experiment
import numpy as np
import wikibio as bio
from wikibio import charts, transmission as T

rng = np.random.default_rng(0)
fig, ax = bio.canvas(19, 7.6)


def simulate(d, L, n):
    """Selected marker at 0, unselected at d. Fragments of length L start uniformly so that they contain the
    selected marker; two crossovers fall uniformly in the fragment, one on each side of the selected marker."""
    hits = 0
    got = 0
    while got < n:
        s = rng.uniform(-L, 0)                 # fragment [s, s + L] contains 0
        left = rng.uniform(s, 0)
        right = rng.uniform(0, s + L)
        # require incorporation of the selected marker (always true here); count inheritance of the other
        got += 1
        if (d >= 0 and d < right) or (d < 0 and d > left):
            hits += 1
    return hits / n


a = charts.axes_at(ax, (1.4, 1.2, 7.4, 5.7))
for L, tok in ((2.0, "dna"), (1.0, "receptor")):
    dd = np.linspace(0, L, 200)
    a.plot(dd, T.wu_cotransduction(dd, L), color=charts.line(tok), lw=2, label=f"Wu, L = {L:g} min")
    pts = np.linspace(0.1, L * 0.9, 7)
    sim = [simulate(p, L, 300) for p in pts]
    a.plot(pts, sim, "o", color=charts.line(tok), ms=4)
a.set_xlim(0, 2.1)
a.set_ylim(0, 1.02)
charts.style_axes(a, "distance between markers d / min", "cotransduction frequency C")
leg = a.legend(frameon=False, fontsize=8)
for t in leg.get_texts():
    t.set_color(bio.P.ink())
charts.title(a, "A   cotransduction falls with distance")

b = charts.axes_at(ax, (11.2, 1.2, 7.0, 5.7))
C = np.linspace(0.001, 1, 300)
b.plot(C, 2 * (1 - C ** (1 / 3)), color=charts.line("dna"), lw=2)
b.plot([0.42, 0.42, 0], [0, 0.502, 0.502], color=charts.line("neutral"), lw=1, ls="--")
b.set_xlim(0, 1)
b.set_ylim(0, 2.05)
charts.style_axes(b, "cotransduction frequency C", "distance d / min (L = 2 min)")
charts.title(b, "B   d = L (1 - C^(1/3))")
