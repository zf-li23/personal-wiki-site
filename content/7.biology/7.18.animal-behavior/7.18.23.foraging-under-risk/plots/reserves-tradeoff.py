# An insurance model of energy reserves (after Lima 1986 and McNamara and Houston 1990; illustrative
# parameters). The energy needed to survive the night (or a spell of bad weather) is normal with mean 10
# and standard deviation s (arbitrary units). A bird carrying reserves y as body fat starves with
# probability 1 - Phi((y - 10) / s) and, independently, is killed by a predator with probability b y, because a heavier bird
# takes off and turns more slowly and must forage more. A: the two risks and their sum for s = 2 and
# b = 0.01; the optimal reserve y* minimizes the total and lies above the mean requirement.
# B: y* rises with the unpredictability of the requirement (s) and falls with the predation cost of mass
# (b), the predictions tested in great tits (Bednekoff and Krebs 1995; Gosler and coauthors 1995).
# C: storing the same energy as hidden food instead of fat: a cache adds no body mass (its cost here is
# 0.002 per unit, for the time and exposure spent caching), but only a fraction q = 0.75 of it is recovered
# (pilfering, forgetting, spoilage). The minimal total risk of each tactic is plotted against b:
# caching is the better insurance when carrying mass is dangerous.
import math

import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
Phi = np.vectorize(lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2))))
y = np.linspace(0, 25, 501)


def fat_risk(s, b):
    return 1 - Phi((y - 10) / s) * (1 - b * y)


def cache_risk(s, q=0.75, c=0.002):
    return 1 - Phi((q * y - 10) / s) * (1 - c * y)


fig, ax = bio.canvas(28.0, 9.8)

# ---- A ------------------------------------------------------------------------------------------------
pa = quant.Plot(ax, (1.9, 1.8, 7.0, 6.4), (0, 25), (0, 1.05), xlabel="Reserves carried y", ylabel="Risk of death",
                xticks=[0, 5, 10, 15, 20, 25], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.6))
st = 1 - Phi((y - 10) / 2.0)
pr = 0.01 * y
tot = 1 - (1 - st) * (1 - pr)
pa.line(y, st, "dna", lw=1.6, dashed=True)
pa.line(y, pr, "rna", lw=1.6, dashed=True)
pa.line(y, tot, "ink", lw=2.2)
i = int(np.argmin(tot))
pa.points([y[i]], [tot[i]], "ink", r=0.12)
pa.line([y[i], y[i]], [0, tot[i]], "ink", lw=0.8, dotted=True)
pa.text(y[i] + 0.5, tot[i] + 0.08, f"y* = {y[i]:.1f}", ha="left")
pa.text(3.5, 0.9, "starvation", ha="left", token="dna")
pa.text(24.5, 0.3, "predation", ha="right", token="rna")
pa.text(24.5, 0.48, "total", ha="right")

# ---- B ------------------------------------------------------------------------------------------------
pb = quant.Plot(ax, (11.4, 1.8, 6.8, 6.4), (0.5, 4), (8, 20), xlabel="Unpredictability of the requirement s",
                ylabel="Optimal reserve y*", xticks=[1, 2, 3, 4], yticks=[8, 12, 16, 20])
bio.panel(ax, "B", (9.8, 9.6))
ss = np.linspace(0.5, 4, 60)
for b, tok, lab in ((0.005, "dna", "low predation, b = 0.005"), (0.01, "ink", "b = 0.01"), (0.02, "rna", "high predation, b = 0.02")):
    opt = [y[np.argmin(fat_risk(s, b))] for s in ss]
    pb.line(ss, opt, tok, lw=2.0)
pb.legend([("b = 0.005", "dna", "-"), ("b = 0.01", "ink", "-"), ("b = 0.02", "rna", "-")], at=(12.0, 7.9))
pb.text(3.9, 9.0, "more variable → fatter;\nmore predators → leaner", ha="right", color=P.muted())

# ---- C ------------------------------------------------------------------------------------------------
pc = quant.Plot(ax, (21.0, 1.8, 6.4, 6.4), (0, 0.012), (0, 0.2), xlabel="Predation cost of mass b",
                ylabel="Minimal risk of death", xticks=[0, 0.004, 0.008, 0.012], yticks=[0, 0.1, 0.2])
bio.panel(ax, "C", (19.4, 9.6))
bs = np.linspace(0, 0.012, 61)
pc.line(bs, [fat_risk(2.0, b).min() for b in bs], "rna", lw=2.2)
pc.hline(cache_risk(2.0).min(), token="positive", dashed=False, lw=2.2)
pc.text(0.0115, 0.185, "store as fat", ha="right", va="top", token="rna")
pc.text(0.0118, cache_risk(2.0).min() - 0.012, "store as caches (q = 0.75)", ha="right", va="top", token="positive")
