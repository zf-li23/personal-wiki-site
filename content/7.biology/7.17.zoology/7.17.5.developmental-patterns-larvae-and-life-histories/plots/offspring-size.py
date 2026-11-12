"""Two models of the trade-off between number and size of offspring (model curves, no data).
Panel A: the Smith-Fretwell (1974) model. Offspring survival f(x) = 1 - exp(-(x - x0)/a) for x > x0, with
a = x0 = 1; parental fitness W = (E/x) f(x) is maximal where the tangent from the origin touches f
(x* ~ 2.15 x0). Panel B: juveniles per unit energy for two larval strategies (Example 5.4.1 of the page):
small eggs (cost 1) whose larvae spend 30 days in the plankton, survival exp(-30 m), and eggs ten times
as costly whose larvae spend 5 days, survival exp(-5 m) / 10, against the larval mortality rate m.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 9.0)

# --- A: Smith-Fretwell
x0 = 1.0
f = lambda x: np.where(x > x0, 1 - np.exp(-(x - x0)), 0.0)
xs = brentq(lambda x: np.exp(x - 1) - (1 + x), 1.5, 3.0)
pa = quant.Plot(ax, (1.8, 1.6, 8.4, 6.0), xlim=(0, 5), ylim=(0, 1.1), xlabel="offspring size x (units of x$_0$)",
                ylabel="offspring survival f(x)", xticks=[0, 1, 2, 3, 4, 5], yticks=[0, 0.5, 1.0])
x = np.linspace(0, 5, 400)
pa.line(x, f(x), "dna", lw=2.0, text="f(x)", at=0.92, dy=-0.25)
slope = float(f(xs)) / xs
tx = np.linspace(0, 3.4, 60)
pa.line(tx, tx * slope, "negative", dashed=True, text="tangent from origin", at=0.35, dx=-0.3, dy=0.45, ha="right")
pa.points([xs], [float(f(xs))], "negative", r=0.12)
pa.vline(xs, token="muted", text="x* ≈ 2.15 x$_0$")
pa.vline(x0, token="muted", text="x$_0$")
bio.panel(ax, "A", (0.6, 8.6))
bio.label(ax, (6.0, 8.6), "Optimal offspring size", size="small", bold=True)

# --- B: planktotrophy versus lecithotrophy
m = np.linspace(0.0, 0.25, 300)
plank = np.exp(-30 * m)
leci = np.exp(-5 * m) / 10
mc = np.log(10) / 25
pb = quant.Plot(ax, (13.6, 1.6, 7.8, 6.0), xlim=(0, 0.25), ylim=(0.0005, 1.2), ylog=True,
                xlabel="larval mortality m / d$^{-1}$", ylabel="juveniles per unit energy",
                xticks=[0, 0.05, 0.1, 0.15, 0.2, 0.25],
                yticks=[(0.001, "0.001"), (0.01, "0.01"), (0.1, "0.1"), (1, "1")])
pb.line(m, plank, "dna", lw=2.0, text="small egg, 30 d", at=0.1, dy=0.25)
pb.line(m, leci, "rna", lw=2.0, text="large egg, 5 d", at=0.75, dy=0.3)
pb.vline(mc, token="muted", text="m = ln 10 / 25")
pb.points([mc], [np.exp(-30 * mc)], "ink", r=0.1)
bio.panel(ax, "B", (12.0, 8.6))
bio.label(ax, (17.5, 8.6), "Feeding versus nonfeeding larvae", size="small", bold=True)
