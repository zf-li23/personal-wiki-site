"""The Volterra principle (Proposition 25.2.1).

A: Lotka-Volterra orbits (r = 1, a = 0.1, c = 0.5, m = 0.5) started at N = 25, P = 10, without
harvesting (h = 0) and with both species removed at the per capita rate h = 0.3. The cycle
averages (dots) move from (10, 10) to ((m + h)/(ca), (r - h)/a) = (16, 7): more prey, fewer predators.
B: percentage of selachians (sharks, skates and rays) in the fish landed at Fiume (Rijeka),
1914-1923, from the data of D'Ancona (1926) as tabulated by Braun (Differential Equations and
Their Applications). Fishing was greatly reduced during the First World War (shaded).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
r, a, c, m = 1.0, 0.1, 0.5, 0.5

fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.3))
ax = axes[0]
for h, col, lab in [(0.0, C.line("dna"), "no harvesting"), (0.3, C.line("negative"), "harvesting h = 0.3")]:
    f = lambda t, z: [(r - h) * z[0] - a * z[0] * z[1], c * a * z[0] * z[1] - (m + h) * z[1]]
    s = solve_ivp(f, [0, 40], [25, 10], max_step=0.02, rtol=1e-9, atol=1e-9)
    ax.plot(s.y[0], s.y[1], color=col, lw=1.3, label=lab)
    ax.plot((m + h) / (c * a), (r - h) / a, "o", color=col, ms=6)
ax.annotate("", xy=(16, 7), xytext=(10, 10), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.0))
ax.text(12.5, 10.6, "averages", fontsize=FS["tiny"], color=P.ink())
ax.legend(fontsize=FS["tiny"], frameon=False, loc="upper right")
C.style_axes(ax, "Prey density N", "Predator density P")
C.title(ax, "A  Harvesting shifts the cycle averages")

ax = axes[1]
years = np.arange(1914, 1924)
pct = np.array([11.9, 21.4, 22.1, 21.2, 36.4, 27.3, 16.0, 15.9, 14.8, 10.7])
ax.axvspan(1914.5, 1918.5, color=P.light("neutral"), lw=0)
ax.text(1916.5, 38, "war years:\nlittle fishing", ha="center", va="top", fontsize=FS["tiny"], color=P.on_fill())
ax.plot(years, pct, "-o", color=C.line("negative"), lw=1.3, ms=4)
ax.set_ylim(0, 40)
C.style_axes(ax, "Year", "Selachians in catch (%)")
C.title(ax, "B  Predatory fish at Fiume (D'Ancona 1926)")
fig.tight_layout()
