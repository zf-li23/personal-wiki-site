"""The mid-domain effect (Colwell and Hurtt 1994) as a null model, and its combination with a gradient.

A bounded domain [0, 1] (an elevational gradient from the valley floor to the summit, or a latitudinal
band between two coasts). A: 40 of 200 ranges placed at random: the two end points of each range are
independent uniform points of the domain. B: richness S(x) of 200 such species (steps, one realization;
grey band: central 90 % of 500 realizations) and the exact expectation S(x) = 2 N x (1 - x) (line); with
the same range sizes placed again at random within the domain (sizes kept, midpoints random where the
range fits; dashed) the peak is similar. C: an elevational gradient combining the mid-domain null model
with a monotonic decline of the regional pool with elevation (each species retained with probability
exp(-2.5 m), m its range midpoint), mean of 300 realizations (dotted line: the peak); the richness peak shifts below mid-elevation, as in Himalayan plants (Grytnes and Vetaas 2002).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(8)

N = 200
x = np.linspace(0, 1, 201)


def random_ranges(n):
    e = np.sort(rng.random((n, 2)), axis=1)
    return e[:, 0], e[:, 1]


def richness(lo, hi):
    return ((lo[:, None] <= x[None, :]) & (hi[:, None] >= x[None, :])).sum(0)


fig, ax = bio.canvas(31.0, 10.0)

lo, hi = random_ranges(N)
pa = C.axes_at(ax, (2.2, 1.6, 7.0, 6.8))
idx = np.argsort(lo[:40] + hi[:40])
for r, i in enumerate(idx):
    pa.plot([lo[i], hi[i]], [r, r], color=Q.line_color("dna"), lw=1.4, solid_capstyle="butt")
pa.set_xlim(0, 1)
pa.set_ylim(-1, 40)
pa.set_yticks([])
C.style_axes(pa, "position in the domain (0 = lower boundary)", "species (40 of 200)")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Ranges placed at random", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.4, 1.6, 7.0, 6.8))
sims = np.array([richness(*random_ranges(N)) for _ in range(500)])
pb.fill_between(x, np.percentile(sims, 5, 0), np.percentile(sims, 95, 0), color=P.muted(), alpha=0.2, lw=0)
pb.step(x, richness(lo, hi), where="mid", color=Q.line_color("dna"), lw=1.0, label="one realization")
pb.plot(x, 2 * N * x * (1 - x), color=Q.line_color("negative"), lw=1.8, label="expectation 2N x(1 − x)")
sizes = hi - lo
S2 = []
for _ in range(200):
    m = sizes / 2 + rng.random(N) * (1 - sizes)
    S2.append(richness(m - sizes / 2, m + sizes / 2))
S2 = np.mean(S2, axis=0)
pb.plot(x, S2, color=Q.line_color("protein"), lw=1.4, ls=(0, (4, 2)), label="range sizes kept, positions random")
pb.set_xlim(0, 1)
pb.set_ylim(0, 140)
C.style_axes(pb, "position in the domain", "species present")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.9, 9.6))
bio.label(ax, (12.4, 9.2), "A hump without any gradient", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.0, 6.8))


def keep_p(m):
    return np.exp(-2.5 * m)


res = []
for _ in range(300):
    l, h = random_ranges(N)
    mid = (l + h) / 2
    keep = rng.random(N) < keep_p(mid)
    res.append(richness(l[keep], h[keep]))
res = np.array(res)
pc.plot(x, res.mean(0), color=Q.line_color("plant"), lw=1.8, label="mid-domain × declining pool")
pc.axvline(x[np.argmax(res.mean(0))], color=Q.line_color("plant"), lw=0.8, ls=(0, (2, 2)))
pc.set_xlim(0, 1)
pc.set_ylim(0, 60)
C.style_axes(pc, "relative elevation (valley to summit)", "species present")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.1, 9.6))
bio.label(ax, (22.6, 9.2), "Null model plus a gradient", size="small", bold=True, ha="left")
