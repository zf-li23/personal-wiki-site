"""The contact process: a lattice version of the Levins metapopulation model.

Each site of a 100 x 100 periodic square lattice is occupied or empty. An occupied site becomes empty at
rate 1; an empty site is colonized at rate lambda k / 4, where k is the number of its four nearest
neighbours that are occupied (offspring only reach adjacent sites). Simulated in small time steps
(dt = 0.1, each event with probability 1 - exp(-rate dt)), from full occupancy, to t = 300; occupancy
is averaged over t = 200-300.
A, B: snapshots for lambda = 1.9 (near the threshold: sparse clusters) and lambda = 3.
C: equilibrium occupancy against lambda. Mean-field (Levins) model p* = 1 - 1/lambda, threshold 1; pair
approximation p* = ((z - 1) lambda - z) / ((z - 1) lambda - 1) with z = 4, threshold 4/3; simulation
(points), whose threshold lies between 1.5 and 1.6, close to the critical value 1.65 of the
continuous-time contact process on the square lattice (the discrete time step lowers it slightly). Local dispersal clusters the occupied sites, so that colonists land on occupied
neighbours and the population needs a higher colonization rate to persist.
"""

import numpy as np
from matplotlib.colors import ListedColormap

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)
n, dt = 100, 0.1


def run(lam, T=300.0, tavg=200.0):
    s = np.ones((n, n), bool)
    pd = 1 - np.exp(-dt)
    acc = []
    for i in range(int(T / dt)):
        k = (np.roll(s, 1, 0).astype(int) + np.roll(s, -1, 0) + np.roll(s, 1, 1) + np.roll(s, -1, 1))
        pb = 1 - np.exp(-lam * dt * k / 4)
        r = rng.random((n, n))
        s = np.where(s, r > pd, r < pb)
        if i * dt >= tavg:
            acc.append(s.mean())
    return s, np.mean(acc)


fig, ax = bio.canvas(30.0, 11.0)
cmap = ListedColormap([P.surface(), P.fill("plant")])
for j, lam in enumerate((1.9, 3.0)):
    s, p = run(lam)
    x0 = 1.2 + 7.6 * j
    pa = C.axes_at(ax, (x0, 2.2, 6.8, 6.8))
    pa.imshow(s, cmap=cmap, interpolation="nearest", vmin=0, vmax=1)
    pa.set_xticks([])
    pa.set_yticks([])
    for sp in pa.spines.values():
        sp.set_color(P.muted())
    bio.panel(ax, "AB"[j], (x0 - 0.9, 10.7))
    bio.label(ax, (x0, 10.0), f"lambda = {lam}: occupancy {p:.2f}", size="small", bold=True, ha="left")

lams = np.array([1.2, 1.4, 1.55, 1.65, 1.75, 1.9, 2.2, 2.6, 3.0, 3.5, 4.0])
sim = np.array([run(l)[1] for l in lams])
ll = np.linspace(1.0, 4.0, 300)
z = 4
mf = 1 - 1 / ll
pa_ = ((z - 1) * ll - z) / ((z - 1) * ll - 1)
pc = C.axes_at(ax, (19.5, 2.2, 9.5, 6.8))
pc.plot(ll, np.maximum(mf, 0), color=Q.line_color("dna"), lw=1.6, label="mean field (Levins)")
pc.plot(ll, np.maximum(pa_, 0), color=Q.line_color("plant"), lw=1.6, ls=(0, (4, 2)), label="pair approximation")
pc.plot(lams, sim, "o", color=Q.line_color("negative"), ms=5, label="lattice simulation")
pc.set_xlim(1, 4)
pc.set_ylim(0, 0.8)
C.style_axes(pc, "colonization rate lambda (death rate 1)", "equilibrium occupancy")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (17.8, 10.7))
bio.label(ax, (19.5, 10.0), "Local dispersal raises the threshold", size="small", bold=True, ha="left")
