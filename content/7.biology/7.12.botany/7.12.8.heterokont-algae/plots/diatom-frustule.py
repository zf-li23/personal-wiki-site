"""Diatom frustule and the size cycle. A: pennate diatom in valve view (raphe, central and polar nodules,
pinnate striae). B: the same cell in girdle view (epitheca over hypotheca, girdle bands). C: centric diatom in
valve view (radial ornament). D: individual-based simulation of a diatom population. Each generation every
cell divides; the daughter that inherits the parental hypotheca is smaller by d = 0.4 um (with small random
variation); the population is resampled to a constant size N = 2000 (loss to sinking and grazing); cells
smaller than the critical size s_c = 35 um become sexual only in a short seasonal window (10 of every 150
generations, the environmental trigger), with probability p = 0.5 per generation, and are replaced by an initial cell (auxospore) of 56-62 um; cells below 22 um die. Line: mean diameter; band: 10-90 %
quantiles."""
import numpy as np
from matplotlib.patches import Ellipse, Circle, Rectangle, FancyBboxPatch
import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(32, 13)
D = "highlight"

# A valve view
bio.panel(ax, "A", (0.2, 12.8))
bio.label(ax, (2.8, 12.5), "Pennate, valve view", size="small", bold=True)
c = np.array([3.0, 6.4])
ax.add_patch(Ellipse(c, 2.2, 9.0, facecolor=P.light(D), edgecolor=P.edge(D), lw=1.4, zorder=4))
for y in np.linspace(c[1] - 4.0, c[1] + 4.0, 23):
    hw = 1.05 * np.sqrt(max(0, 1 - ((y - c[1]) / 4.5) ** 2))
    if abs(y - c[1]) < 0.5:
        continue
    for sg in (1, -1):
        ax.plot([c[0] + sg * 0.25, c[0] + sg * (hw - 0.08)], [y, y], color=P.edge(D), lw=0.8, zorder=5)
ax.plot([c[0], c[0]], [c[1] + 0.4, c[1] + 4.0], color=P.ink(), lw=1.3, zorder=6)
ax.plot([c[0], c[0]], [c[1] - 0.4, c[1] - 4.0], color=P.ink(), lw=1.3, zorder=6)
ax.add_patch(Ellipse(c, 0.5, 0.8, facecolor=P.fill(D), edgecolor=P.edge(D), lw=1.0, zorder=6))
for sg in (1, -1):
    ax.add_patch(Circle(c + np.array([0, sg * 4.15]), 0.16, facecolor=P.fill(D), edgecolor=P.edge(D), lw=1.0, zorder=6))
bio.callout(ax, (c[0], c[1] + 2.2), (5.6, 9.2), "raphe", size="tiny")
bio.callout(ax, tuple(c), (5.6, 6.4), "central nodule", size="tiny")
bio.callout(ax, (c[0], c[1] + 4.15), (5.6, 11.2), "polar nodule", size="tiny")
bio.callout(ax, (c[0] - 0.6, c[1] - 2.0), (0.6, 1.2), "striae", size="tiny")

# B girdle view
bio.panel(ax, "B", (7.6, 12.8))
bio.label(ax, (10.0, 12.5), "Girdle view", size="small", bold=True)
x0, y0 = 10.0, 6.4
ax.add_patch(FancyBboxPatch((x0 - 1.4, y0 - 4.5), 2.8, 9.0, boxstyle="round,pad=0,rounding_size=0.5",
                            facecolor=P.light(D), edgecolor=P.edge(D), lw=1.4, zorder=4))
ax.add_patch(Rectangle((x0 - 1.4, y0 - 4.3), 2.8, 8.6, facecolor="none", edgecolor="none"))
ax.plot([x0 - 0.15, x0 - 0.15], [y0 - 4.5, y0 + 4.5], color=P.edge(D), lw=1.2, zorder=5)
for xx in (x0 + 0.15, x0 + 0.45):
    ax.plot([xx, xx], [y0 - 4.3, y0 + 4.3], color=P.edge(D), lw=0.7, zorder=5, ls=(0, (3, 2)))
bio.label(ax, (x0 - 0.8, y0 + 5.0), "epitheca", size="tiny")
bio.label(ax, (x0 + 0.9, y0 + 5.0), "hypotheca", size="tiny")
bio.callout(ax, (x0 + 0.3, y0 - 2.0), (x0 + 2.0, y0 - 5.4), "girdle bands", size="tiny")

# C centric valve view
bio.panel(ax, "C", (12.8, 12.8))
bio.label(ax, (15.2, 12.5), "Centric, valve view", size="small", bold=True)
cc = np.array([15.2, 8.0])
ax.add_patch(Circle(cc, 2.2, facecolor=P.light(D), edgecolor=P.edge(D), lw=1.4, zorder=4))
for a in np.linspace(0, 2 * np.pi, 48, endpoint=False):
    u = np.array([np.cos(a), np.sin(a)])
    ax.plot(*np.c_[cc + 0.9 * u, cc + 2.05 * u], color=P.edge(D), lw=0.8, zorder=5)
ax.add_patch(Circle(cc, 0.8, facecolor=P.fill(D), edgecolor=P.edge(D), lw=0.8, zorder=5))
bio.label(ax, (15.2, 5.2), "radial striae, marginal ring", size="tiny", color=P.muted())

# D simulation
bio.panel(ax, "D", (18.4, 12.8))
N, d, sc, p, smin = 2000, 0.4, 35.0, 0.5, 22.0
s = rng.uniform(50, 60, N)
G = 700
mean, lo, hi = [], [], []
for g in range(G):
    small = s - d * (1 + 0.15 * rng.standard_normal(N))
    s = np.concatenate([s, small])
    s = s[s > smin]
    s = rng.choice(s, N, replace=len(s) < N)
    sex = (s < sc) & (rng.random(N) < p) & (g % 150 < 10)
    s[sex] = rng.uniform(56, 62, sex.sum())
    mean.append(s.mean()); lo.append(np.quantile(s, 0.1)); hi.append(np.quantile(s, 0.9))
gg = np.arange(G)
pl = quant.Plot(ax, (20.2, 2.2, 11.0, 8.8), xlim=(0, G), ylim=(20, 65), xlabel="generations",
                ylabel="cell diameter / µm", xticks=[0, 200, 400, 600], yticks=[20, 35, 50, 65])
pl.band(gg, np.array(lo), np.array(hi), token=D)
pl.line(gg, np.array(mean), token=D, lw=1.8)
pl.hline(sc, text="s_c (sexual size)", size="tiny")
bio.label(ax, (25.7, 12.4), "Population size cycle (model)", size="small", bold=True)
