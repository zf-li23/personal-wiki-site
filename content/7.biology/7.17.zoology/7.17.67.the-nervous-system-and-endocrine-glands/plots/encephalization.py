# Brain size: (A) schematic allometry after Jerison 1973; (B) encephalization quotients of mammals, midpoints of
# the ranges in Roth & Dicke 2005, Trends Cogn. Sci. 9: 250-257, Table 1.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23, 9.2)
bio.panel(ax, "A", (0.3, 8.9))
p = quant.Plot(ax, (1.8, 1.4, 8.2, 6.8), xlim=(1e-3, 1e5), ylim=(1e-4, 1e4), xlog=True, ylog=True,
               xlabel="body mass / kg", ylabel="brain mass / g",
               xticks=[(1e-3, "0.001"), (1e-1, "0.1"), (10, "10"), (1e3, "1000"), (1e5, "1e5")],
               yticks=[(1e-4, "1e-4"), (1e-2, "0.01"), (1, "1"), (100, "100"), (1e4, "1e4")])
m = np.logspace(-3, 5, 50)
p.line(m, 0.12 * (m * 1000) ** (2 / 3), "neuron", text="mammals, birds", at=0.15, dy=0.35)
p.line(m, 0.012 * (m * 1000) ** (2 / 3), "plant", text="fishes, amphibians, reptiles", at=0.45, dy=-0.4)
for name, bm, br in (("human", 65, 1350), ("dolphin", 150, 1600), ("elephant", 5000, 4800)):
    q = p.xy(bm, br)
    ax.plot([q[0]], [q[1]], "o", ms=4, color=quant.line_color("neuron"), zorder=9)
    off = {"human": (0.15, -0.3, "left"), "dolphin": (-0.12, 0.3, "right"), "elephant": (-0.12, 0.3, "right")}[name]
    bio.label(ax, (q[0] + off[0], q[1] + off[1]), name, size="tiny", ha=off[2])
bio.label(ax, (6.0, 8.6), "schematic: slope 2/3, lines a factor of 10 apart", size="tiny", color=P.muted())

bio.panel(ax, "B", (11.8, 8.9))
data = [("human", 7.6), ("dolphin", 5.3), ("chimpanzee", 2.35), ("rhesus monkey", 2.1), ("whale", 1.8),
        ("elephant", 1.3), ("dog", 1.2), ("cat", 1.0), ("horse", 0.9), ("sheep", 0.8), ("mouse", 0.5),
        ("rat", 0.4), ("rabbit", 0.4)]
q = quant.Plot(ax, (15.6, 1.4, 6.8, 7.0), xlim=(0, 8), ylim=(0, len(data)), xlabel="encephalization quotient",
               xticks=[0, 2, 4, 6, 8], frame="l")
for i, (n, v) in enumerate(data):
    y = len(data) - i - 0.5
    x0, y0 = q.xy(0, y - 0.32)
    x1, y1 = q.xy(v, y + 0.32)
    ax.fill([x0, x1, x1, x0], [y0, y0, y1, y1], color=P.fill("neuron"), ec=P.edge("neuron"), lw=0.6, zorder=6)
    bio.label(ax, (x0 - 0.15, (y0 + y1) / 2), n, size="tiny", ha="right")
xa = q.xy(1, 0)[0]
ax.plot([xa, xa], [1.4, 8.4], color=P.muted(), lw=0.8, ls=(0, (3, 2)), zorder=7)
