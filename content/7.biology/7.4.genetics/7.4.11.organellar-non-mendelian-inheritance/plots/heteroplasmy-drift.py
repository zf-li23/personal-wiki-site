"""Heteroplasmy drift over several maternal generations (neutral Wright-Fisher sampling of N segregating units).
(A) Exact distribution of the mutant fraction h after t = 1, 2, 4 and 8 generations from h0 = 0.3, N = 20,
computed with the Wright-Fisher transition matrix; the bars at h = 0 and h = 1 are lineages that became
homoplasmic. (B) Variance of h against t: simulated lineages (points, 4000 per value) and
Var = h0 (1 - h0) [1 - (1 - 1/N)^t] (lines) for N = 5, 20 and 100. (C) Fate of lineages for N = 20:
probability of loss, of fixation of the mutant and of remaining heteroplasmic; fixation tends to h0."""

import numpy as np
from scipy.stats import binom

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
h0 = 0.3


def matrix(N):
    k = np.arange(N + 1)
    return np.array([binom.pmf(k, N, i / N) for i in k])


def evolve(N, t):
    M = matrix(N)
    v = np.zeros(N + 1)
    v[int(round(h0 * N))] = 1.0
    out = [v]
    for _ in range(t):
        v = v @ M
        out.append(v)
    return np.array(out)


fig, ax = bio.canvas(22.0, 7.6)

bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.6, 5.6))
N = 20
D = evolve(N, 8)
h = np.arange(N + 1) / N
w = 0.011
for off, (t, tok) in zip((-1.5, -0.5, 0.5, 1.5), ((1, "channel"), (2, "positive"), (4, "highlight"), (8, "negative"))):
    a.bar(h + off * w, D[t], width=w, color=charts.line(tok), label=f"t = {t}")
a.set_xlim(-0.04, 1.04)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "heteroplasmy h (N = 20, h0 = 0.3)", "probability")

bio.panel(ax, "B", (8.0, 7.5))
b = charts.axes_at(ax, (9.6, 1.3, 5.2, 5.6))
ts = np.arange(0, 41)
for N, tok in ((5, "negative"), (20, "positive"), (100, "channel")):
    b.plot(ts, h0 * (1 - h0) * (1 - (1 - 1 / N) ** ts), color=charts.line(tok), lw=1.6, label=f"N = {N}")
    hh = np.full(4000, h0)
    sim = [0.0]
    for _ in ts[1:]:
        hh = rng.binomial(N, hh) / N
        sim.append(hh.var())
    b.plot(ts[::4], np.array(sim)[::4], "o", color=charts.line(tok), ms=3)
b.axhline(h0 * (1 - h0), color=P.muted(), ls="--", lw=0.9)
b.text(40, h0 * (1 - h0) + 0.004, "h0(1 - h0)", fontsize=FT["tiny"], color=P.muted(), ha="right", va="bottom")
b.set_xlim(0, 40)
b.set_ylim(0, 0.24)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "maternal generations t", "Var(h)")

bio.panel(ax, "C", (15.6, 7.5))
c = charts.axes_at(ax, (17.2, 1.3, 4.6, 5.6))
D = evolve(20, 60)
t = np.arange(61)
c.plot(t, D[:, 0], color=charts.line("channel"), lw=1.7, label="lost (h = 0)")
c.plot(t, D[:, -1], color=charts.line("negative"), lw=1.7, label="fixed (h = 1)")
c.plot(t, 1 - D[:, 0] - D[:, -1], color=charts.line("neutral"), lw=1.7, label="heteroplasmic")
c.axhline(h0, color=P.muted(), ls=":", lw=0.9)
c.axhline(1 - h0, color=P.muted(), ls=":", lw=0.9)
c.set_xlim(0, 60)
c.set_ylim(0, 1)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(c, "maternal generations t (N = 20)", "fraction of lineages")
