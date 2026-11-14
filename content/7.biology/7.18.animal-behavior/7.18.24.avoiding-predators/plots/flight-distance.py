# The economic model of escape (Ydenberg and Dill 1986; illustrative functions). As a predator approaches, the
# cost of staying, the expected loss from capture, rises: R(D) = r exp(-D / 10) for predator distance D (m).
# The cost of fleeing, the feeding or other opportunities lost by leaving now rather than later, falls as the
# predator comes closer because less is lost by leaving late: F(D) = f D. The prey should flee at the distance
# where the two costs are equal, the flight initiation distance. A: the base case (r = 1, f = 0.01) and the
# shifts caused by a more dangerous predator (r = 2: flee earlier) and by a richer food patch (f = 0.02:
# flee later). B: the predicted flight initiation distance as a function of the value of the food being
# given up, for a slow and a fast (more dangerous) predator.
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import quant

P = bio.P


def fid(r, f):
    return brentq(lambda d: r * np.exp(-d / 10) - f * d, 1e-6, 200)


fig, ax = bio.canvas(21.0, 9.8)
pa = quant.Plot(ax, (2.0, 1.8, 7.6, 6.4), (0, 60), (0, 1.05), xlabel="Distance to the approaching predator D / m",
                ylabel="Cost (fitness units)", xticks=[0, 20, 40, 60], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.6))
D = np.linspace(0, 60, 300)
pa.line(D, np.exp(-D / 10), "negative", lw=2.2)
pa.line(D, 2 * np.exp(-D / 10), "negative", lw=1.4, dashed=True)
pa.line(D, 0.01 * D, "dna", lw=2.2)
pa.line(D, 0.02 * D, "dna", lw=1.4, dashed=True)
for r, f, tok in ((1, 0.01, "ink"), (2, 0.01, "negative"), (1, 0.02, "dna")):
    d = fid(r, f)
    pa.points([d], [f * d], tok, r=0.12)
    pa.line([d, d], [0, f * d], tok, lw=0.8, dotted=True)
pa.text(3.5, 0.95, "cost of staying R(D)", ha="left", token="negative")
pa.text(11.5, 0.82, "faster predator", ha="left", token="negative")
pa.text(58, 0.5, "cost of fleeing F(D)", ha="right", token="dna")
pa.text(49, 0.72, "richer food", ha="left", token="dna")
pa.text(59, 0.06, "← predator approaches", ha="right", color=P.muted())

pb = quant.Plot(ax, (12.6, 1.8, 7.6, 6.4), (0.005, 0.05), (0, 40), xlabel="Value of the food given up f",
                ylabel="Flight initiation distance / m", xticks=[0.01, 0.02, 0.03, 0.04, 0.05], yticks=[0, 10, 20, 30, 40])
bio.panel(ax, "B", (10.8, 9.6))
fs = np.linspace(0.005, 0.05, 100)
pb.line(fs, [fid(1, f) for f in fs], "ink", lw=2.0)
pb.line(fs, [fid(2, f) for f in fs], "negative", lw=2.0, dashed=True)
pb.text(0.03, 17.5, "fast predator (r = 2)", ha="left", token="negative")
pb.text(0.03, 8.0, "slow predator (r = 1)", ha="left")
