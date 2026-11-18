"""Two mechanisms by which species richness raises productivity: sampling (selection) and complementarity.

A, sampling model (after Tilman, Lehman and Thomson 1997 and Huston 1997): a pool of 60 species with
monoculture yields M_i drawn from a lognormal distribution (median 200 g m^-2, log-sd 0.5). A mixture of S
species drawn at random is taken over by its best competitor, whose yield is that of its monoculture
(competitive exclusion: one species, one resource). If the best competitor is the most productive species
(dominance and yield perfectly correlated), the expected mixture yield is the expected maximum of S draws,
E[max] = integral of (1 - F(y)^S) dy (solid curve, computed numerically); points are means of 500 random
mixtures, bands the central 90 %. If competitive ability is unrelated to yield, the mixture yield is that of
a random species, and richness has no effect on the mean (grey).
B, complementarity model: a habitat varying continuously along a resource gradient x in [0, 1]. Species i
has an optimum u_i (uniform on [0, 1]) and yield density g_i(x) = exp(-(x - u_i)^2 / (2 w^2)), w = 0.12. In
monoculture species i yields integral g_i dx; in mixture, each point of the habitat is held by the species
that performs best there, so the mixture yields integral max_i g_i(x) dx. Curves: mean mixture yield, mean
yield of the best monoculture in the same mixture, and mean monoculture yield (500 random mixtures per S).
Mixture yield exceeds the best monoculture (transgressive overyielding) and saturates as the gradient fills.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(21)

pool = 60
M = 200 * np.exp(0.5 * rng.standard_normal(pool))
Ss = np.array([1, 2, 3, 4, 6, 8, 12, 16])
reps = 500

fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.4, 1.6, 11.0, 7.4))
mean_c, lo_c, hi_c, mean_u = [], [], [], []
for S in Ss:
    ys, yu = [], []
    for _ in range(reps):
        sub = rng.choice(pool, S, replace=False)
        ys.append(M[sub].max())
        yu.append(M[rng.choice(sub)])
    mean_c.append(np.mean(ys))
    lo_c.append(np.quantile(ys, 0.05))
    hi_c.append(np.quantile(ys, 0.95))
    mean_u.append(np.mean(yu))
grid = np.linspace(0, M.max() * 1.01, 4000)
F = np.searchsorted(np.sort(M), grid, side="right") / pool
sc = np.linspace(1, 16, 100)
emax = [np.trapezoid(1 - F ** s, grid) for s in sc]
c = Q.line_color("plant")
pa.fill_between(Ss, lo_c, hi_c, color=P.light("plant"), alpha=0.6, lw=0)
pa.plot(sc, emax, color=c, lw=1.6, label="dominant = most productive: E[max of S]")
pa.plot(Ss, mean_c, "o", color=c, ms=4)
pa.plot(Ss, mean_u, "s-", color=P.muted(), ms=4, lw=1.2, label="dominance unrelated to yield")
pa.axhline(M.max(), color=Q.line_color("negative"), lw=0.9, ls=(0, (4, 2)))
pa.text(16, M.max() + 12, "most productive species in the pool", ha="right", fontsize=FS["tiny"], color=Q.line_color("negative"))
pa.set_xlim(0.5, 16.5)
pa.set_ylim(0, M.max() * 1.15)
C.style_axes(pa, "species richness S", "mixture yield (g m⁻²)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.6, 10.6))
bio.label(ax, (2.4, 10.2), "Sampling (selection) effect", size="small", bold=True, ha="left")
bio.label(ax, (2.4, 9.5), "mixture never exceeds its best monoculture", size="tiny", ha="left")

x = np.linspace(0, 1, 801)
w = 0.12
mix, best, mono = [], [], []
for S in Ss:
    a, b_, m_ = [], [], []
    for _ in range(reps):
        u = rng.random(S)
        g = np.exp(-(x[None, :] - u[:, None]) ** 2 / (2 * w ** 2))
        ym = np.trapezoid(g, x, axis=1)
        a.append(np.trapezoid(g.max(0), x))
        b_.append(ym.max())
        m_.append(ym.mean())
    mix.append(np.mean(a))
    best.append(np.mean(b_))
    mono.append(np.mean(m_))
pb = C.axes_at(ax, (17.6, 1.6, 11.0, 7.4))
pb.plot(Ss, mix, "o-", color=Q.line_color("dna"), lw=1.6, ms=4, label="mixture")
pb.plot(Ss, best, "^-", color=Q.line_color("negative"), lw=1.3, ms=4, label="best monoculture in the mixture")
pb.plot(Ss, mono, "s-", color=P.muted(), lw=1.2, ms=4, label="mean monoculture")
pb.set_xlim(0.5, 16.5)
pb.set_ylim(0, 1.05)
C.style_axes(pb, "species richness S", "yield (habitat area = 1)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "B", (15.8, 10.6))
bio.label(ax, (17.6, 10.2), "Complementarity along a resource gradient", size="small", bold=True, ha="left")
bio.label(ax, (17.6, 9.5), "transgressive overyielding: mixture above its best monoculture", size="tiny", ha="left")
