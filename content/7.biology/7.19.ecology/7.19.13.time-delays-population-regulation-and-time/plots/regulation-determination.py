"""Regulation versus determination of abundance, and multiple equilibria.

A: per capita birth rate b(N) declining with density (density dependent, regulating) and per capita death
rate independent of density but set by physical conditions at three sites (d1 < d2 < d3). Each site has
a stable equilibrium where b = d: regulation is the same everywhere, but the level is determined by the
density-independent factor.
B: the spruce budworm model of Ludwig, Jones and Holling (1978) in dimensionless form,
du/dt = r u (1 - u/q) - u^2 / (1 + u^2): per capita growth r (1 - u/q) (lines, r = 0.55, three values of the
carrying capacity q, which grows with the foliage of the forest) against per capita predation by birds,
u / (1 + u^2) (curve: a type III functional response). Filled points are stable equilibria, open points
unstable ones. For q = 9 there are two stable states, an endemic level held by predators and an outbreak
level held by food, separated by an unstable threshold.
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = C.axes_at(ax, (2.5, 1.6, 10.5, 6.8))
N = np.linspace(0, 100, 300)
b = 0.9 - 0.008 * N
pa.plot(N, b, color=Q.line_color("positive"), lw=1.8)
pa.text(4, 0.86, "birth rate b(N)", fontsize=FS["tiny"], color=Q.line_color("positive"))
for k, (d, tok) in enumerate([(0.2, "dna"), (0.4, "protein"), (0.6, "negative")]):
    pa.axhline(d, color=Q.line_color(tok), lw=1.3)
    Ns = (0.9 - d) / 0.008
    pa.plot([Ns], [d], "o", ms=5, color=Q.line_color(tok))
    pa.plot([Ns, Ns], [0, d], color=Q.line_color(tok), lw=0.7, ls=(0, (2, 2)))
    pa.text(Ns + 1.5, 0.03, f"N{k + 1}*", fontsize=FS["tiny"], color=Q.line_color(tok))
    pa.text(99, d + 0.015, f"death rate d{k + 1}", fontsize=FS["tiny"], color=Q.line_color(tok), ha="right")
pa.set_xlim(0, 100)
pa.set_ylim(0, 1.0)
pa.set_xticks([])
pa.set_yticks([])
C.style_axes(pa, "population density N", "per capita rate")
bio.panel(ax, "A", (0.6, 9.6))
bio.label(ax, (2.5, 9.2), "Regulation and determination", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.5, 1.6, 11.5, 6.8))
r = 0.55
u = np.linspace(0.0, 15, 600)
pred = u / (1 + u ** 2)
pb.plot(u, pred, color=P.ink(), lw=1.8)
pb.text(1.1, 0.52, "predation u/(1+u^2)", fontsize=FS["tiny"], color=P.ink())
for q, tok in [(5, "dna"), (9, "protein"), (14, "negative")]:
    g = r * (1 - u / q)
    pb.plot(u, g, color=Q.line_color(tok), lw=1.3)
    pb.text(q + 0.15, 0.03, f"q = {q}", fontsize=FS["tiny"], color=Q.line_color(tok), ha="left")
    f = lambda x: r * (1 - x / q) - x / (1 + x ** 2)
    grid = np.linspace(0.01, q, 4000)
    sv = f(grid)
    for i in np.where(np.diff(np.sign(sv)))[0]:
        x = brentq(f, grid[i], grid[i + 1])
        stable = sv[i] > 0  # f decreases through the root
        pb.plot([x], [x / (1 + x ** 2)], "o", ms=5.5, mfc=Q.line_color(tok) if stable else "none",
                mec=Q.line_color(tok), mew=1.2)
pb.set_xlim(0, 15)
pb.set_ylim(0, 0.6)
C.style_axes(pb, "budworm density u", "per capita rate")
bio.panel(ax, "B", (16.0, 9.6))
bio.label(ax, (17.5, 9.2), "Multiple equilibria: spruce budworm", size="small", bold=True, ha="left")
