"""Topological defects of a two-dimensional director field n = (cos phi, sin phi), drawn as headless
segments (a nematic has no head or tail). Around a defect of charge k the director rotates by
2 pi k on any loop enclosing the core: phi = k atan2(y, x) + phi0. A: k = +1/2, the comet-shaped
defect, which self-propels along its head-tail axis in extensile active nematics. B: k = -1/2, the
three-fold defect, which has no preferred direction and moves only passively. C, D: k = +1 defects,
which in nematics usually split into two +1/2 defects: an aster (phi0 = 0) and a vortex
(phi0 = pi/2), the latter seen in confined bacteria and cell monolayers."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 4, figsize=(10.8, 2.9))
fig.subplots_adjust(wspace=0.12, left=0.02, right=0.98, bottom=0.04, top=0.86)
g = np.linspace(-1, 1, 15)
X, Y = np.meshgrid(g, g)
r = np.hypot(X, Y)
cases = [(0.5, 0.0, r"A  $k = +1/2$"), (-0.5, 0.0, r"B  $k = -1/2$"),
         (1.0, 0.0, r"C  $k = +1$, aster"), (1.0, np.pi / 2, r"D  $k = +1$, vortex")]
for ax, (k, p0, ttl) in zip(axs, cases):
    phi = k * np.arctan2(Y, X) + p0
    m = (r > 0.08) & (r < 1.05)
    h = 0.055
    segs = [[(x - h * np.cos(a), y - h * np.sin(a)), (x + h * np.cos(a), y + h * np.sin(a))]
            for x, y, a in zip(X[m], Y[m], phi[m])]
    ax.add_collection(LineCollection(segs, colors=charts.line("actin"), linewidths=1.6, capstyle="round"))
    ax.plot(0, 0, "o", color=charts.line("negative"), ms=5)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")
    charts.title(ax, ttl)
