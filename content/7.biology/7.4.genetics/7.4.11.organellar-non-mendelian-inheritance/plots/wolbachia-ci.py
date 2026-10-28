"""Spread of a cytoplasmic-incompatibility (CI) inducing Wolbachia, discrete-generation model
p' = p (1 - sf)(1 - mu) / [1 - sf p - sh p (1 - p) - mu sh p^2 (1 - sf)],
with sf the fecundity cost to infected females, sh the CI strength (fraction of embryos from infected male x
uninfected female crosses that die) and mu the fraction of uninfected ova from infected mothers.
(A) Change per generation dp = p' - p against p for sh = 0.9: the unstable equilibrium (open circle) is the
invasion threshold, about sf/sh for perfect transmission. (B) Trajectories for sf = 0.1, sh = 0.9, mu = 0 from
initial frequencies below and above the threshold of 0.11."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def step(p, sf, sh, mu=0.0):
    return p * (1 - sf) * (1 - mu) / (1 - sf * p - sh * p * (1 - p) - mu * sh * p * p * (1 - sf))


fig, ax = bio.canvas(16.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.9, 1.3, 5.6, 5.6))
p = np.linspace(0, 1, 2001)
for sf, mu, tok in ((0.1, 0.0, "channel"), (0.2, 0.0, "negative"), (0.1, 0.03, "positive")):
    d = step(p, sf, 0.9, mu) - p
    a.plot(p, d, color=charts.line(tok), lw=1.7, label=f"sf = {sf}, mu = {mu}")
    s = np.sign(d)
    idx = np.where(s[1:-1] != s[2:])[0] + 1
    for i in idx:
        if 0.01 < p[i] < 0.9:
            a.plot(p[i], 0, "o", mfc=P.surface(), mec=charts.line(tok), ms=6, zorder=5)
a.axhline(0, color=P.muted(), lw=0.8)
a.set_xlim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "infection frequency p", "change per generation p' - p")

bio.panel(ax, "B", (8.3, 7.5))
b = charts.axes_at(ax, (10.1, 1.3, 5.6, 5.6))
g = np.arange(31)
for p0 in (0.05, 0.09, 0.105, 0.12, 0.15, 0.3):
    tr = [p0]
    for _ in g[1:]:
        tr.append(step(tr[-1], 0.1, 0.9))
    b.plot(g, tr, color=charts.line("channel" if p0 > 0.111 else "neutral"), lw=1.5)
b.axhline(0.1 / 0.9, color=P.muted(), ls="--", lw=0.9)
b.text(30, 0.13, "threshold sf/sh = 0.11", fontsize=FT["tiny"], color=P.muted(), ha="right", va="bottom")
b.set_xlim(0, 30)
b.set_ylim(0, 1.02)
charts.style_axes(b, "generations", "infection frequency p")
