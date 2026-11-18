"""Lag phases and the spread of an invader.

A: occupied area after introduction, from a reaction-diffusion model with a strong Allee effect in two
dimensions (radially symmetric), u_t = D (u_rr + u_r / r) + r u (1 - u)(u - a), D = 0.05 km^2 per year,
r = 1 per year, a = 0.2, started from a small founding population of radius 1 km and density u0 = 0.5 (or a
denser 0.8). Occupied area = area where u > 0.5. With u0 = 0.5 the population first lingers near the Allee
threshold before the front forms. Logistic growth of a local population from 10^-4 of capacity is shown for
comparison of timescales (right axis): exponential growth looks like a lag on a linear scale. A detection
threshold of 10 km^2 is marked.
B: radius of the invaded range against time for diffusive spread (Fisher-KPP speed c = 2 sqrt(r D), radius
grows linearly) and for stratified dispersal (the same diffusion plus long-distance jumps founding new foci
at rate 0.01 per km of front per year at distances exponentially distributed with mean 30 km; simulated as
a set of growing circles; radius = sqrt(area / pi) of their union, estimated on a grid; mean of 20 runs, band:
central 80 %; at most 300 foci, grid of 5 km cells). New foci make spread accelerate.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(9)

D, r, a = 0.05, 1.0, 0.2
R, nr = 40.0, 400
dr = R / nr
rr = (np.arange(nr) + 0.5) * dr
dt = 0.2 * dr ** 2 / D


def allee(u0, T=60.0):
    u = np.where(rr < 1.0, u0, 0.0)
    ts, area = [], []
    t, k = 0.0, 0
    while t < T:
        up = np.append(u[1:], u[-1])
        um = np.insert(u[:-1], 0, u[0])
        lap = (up - 2 * u + um) / dr ** 2 + (up - um) / (2 * dr) / rr
        u = u + dt * (D * lap + r * u * (1 - u) * (u - a))
        t += dt
        k += 1
        if k % 20 == 0:
            ts.append(t)
            area.append(np.sum(2 * np.pi * rr * dr * (u > 0.5)))
    return np.array(ts), np.array(area)


fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.4, 1.6, 10.8, 7.4))
for u0, tok in ((0.8, "dna"), (0.5, "negative")):
    ts, ar = allee(u0)
    pa.plot(ts, ar, color=Q.line_color(tok), lw=1.6, label=f"Allee effect, founders at density {u0}")
pa.axhline(10, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(1, 11.5, "detection threshold", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0, 60)
pa.set_ylim(0, 90)
C.style_axes(pa, "years since introduction", "occupied area (km²)")
pa2 = pa.twinx()
tl = np.linspace(0, 60, 300)
pa2.plot(tl, 1 / (1 + (1e4 - 1) * np.exp(-0.5 * tl)), color=Q.line_color("plant"), lw=1.2, ls=(0, (4, 2)), label="local logistic growth, r = 0.5")
pa2.set_ylim(0, 1.05)
C.style_axes(pa2, None, "local density / capacity")
pa2.spines["right"].set_visible(True)
h1, l1 = pa.get_legend_handles_labels()
h2, l2 = pa2.get_legend_handles_labels()
pa.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.6, 10.6))
bio.label(ax, (2.4, 10.2), "Apparent and real lag phases", size="small", bold=True, ha="left")

c = 2 * np.sqrt(0.5 * 0.5)
T = 40
tt = np.arange(T + 1)
g = np.arange(-300, 301, 5.0)
X, Y = np.meshgrid(g, g)
runs = []
for _ in range(20):
    foci = [(0.0, 0.0, 0.0)]
    rad = []
    for t in tt:
        F = np.array(foci)
        rad_f = c * (t - F[:, 2])
        cover = np.zeros(X.shape, bool)
        for (x0, y0, _), rf in zip(F, rad_f):
            cover |= (X - x0) ** 2 + (Y - y0) ** 2 <= rf ** 2
        rad.append(np.sqrt(cover.sum() * 25.0 / np.pi))
        if len(foci) < 300:
            for (x0, y0, t0), rf in zip(F, rad_f):
                for _ in range(rng.poisson(0.01 * 2 * np.pi * rf)):
                    ang = rng.uniform(0, 2 * np.pi)
                    dist = rf + rng.exponential(30)
                    foci.append((x0 + dist * np.cos(ang), y0 + dist * np.sin(ang), t))
    runs.append(rad)
runs = np.array(runs)
pb = C.axes_at(ax, (17.6, 1.6, 10.8, 7.4))
pb.plot(tt, c * tt, color=Q.line_color("dna"), lw=1.6, label="diffusion only: radius = 2 sqrt(rD) t")
pb.fill_between(tt, np.quantile(runs, 0.1, 0), np.quantile(runs, 0.9, 0), color=P.light("negative"), lw=0, alpha=0.6)
pb.plot(tt, runs.mean(0), color=Q.line_color("negative"), lw=1.6, label="stratified dispersal (jumps found new foci)")
pb.set_xlim(0, T)
pb.set_ylim(0, 200)
C.style_axes(pb, "years since introduction", "radius of invaded range (km)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (15.8, 10.6))
bio.label(ax, (17.6, 10.2), "Linear versus accelerating spread", size="small", bold=True, ha="left")
bio.label(ax, (17.6, 9.5), "r = 0.5 per year, D = 0.5 km² per year", size="tiny", ha="left")
