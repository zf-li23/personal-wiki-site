# Risk-sensitive foraging and the energy budget rule. A: a small bird must end the day with at least
# R = 8 energy units to survive the night (survival is a step function of reserves at dusk). From 7 units,
# the safe option (1 unit for certain) guarantees survival; from 6 units only the variable option
# (2 or 0 units, each with probability 1/2) gives any chance. The fitness function is convex below the
# requirement and concave above it. B: the z-score model (Stephens and Charnov 1982): daily intake X is
# normal with mean m and standard deviation s, and the bird survives if X >= R. P(survive) =
# Phi((m - R) / s) for a low-variance option (s = 1) and a high-variance option (s = 3) with the same mean:
# the variable option is better when the expected intake falls short of the requirement (risk-prone)
# and worse when it exceeds it (risk-averse). C: Jensen's inequality on an S-shaped (logistic)
# fitness function: averaging over outcomes (filled dot) beats the fitness of the mean (open dot) where it is convex.
import math

import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(28.0, 9.8)

# ---- A ------------------------------------------------------------------------------------------------
pa = quant.Plot(ax, (1.9, 1.8, 7.0, 6.4), (4.5, 11.5), (0, 1.15), xlabel="Reserves at dusk (energy units)",
                ylabel="Probability of surviving the night", xticks=[5, 6, 7, 8, 9, 10, 11], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.6))
pa.steps([4.5, 8, 11.5], [0, 1, 1], "ink", lw=2.2)
pa.vline(8, text="requirement R", top=True)
# outcomes of the two options from 6 and from 7 units
for x0, y, tok in ((6, 0.16, "rna"), (7, 0.52, "dna")):
    col = quant.line_color(tok)
    bio.arrow(ax, pa.xy(x0, y), pa.xy(x0 + 1, y), kind="process", color=col, lw=1.2, shrink=0.12)
    bio.arrow(ax, pa.xy(x0, y), pa.xy(x0 + 2, y), kind="process", color=col, lw=1.0, bend=-0.45, dashed=True, shrink=0.12)
    pa.points([x0], [y], tok, r=0.11)
    pa.points([x0 + 1, x0 + 2], [y, y], tok, r=0.08, hollow=True)
    pa.text(x0, y - 0.06, f"{x0}", va="top", token=tok)
pa.text(4.7, 0.95, "from 6: safe → 7, dies;\nvariable → 6 or 8,\nsurvives with P = 0.5", ha="left", va="top", token="rna")
pa.text(8.2, 0.85, "from 7: safe → 8,\nsurvives; variable\n→ 7 or 9, P = 0.5", ha="left", va="top", token="dna")

# ---- B ------------------------------------------------------------------------------------------------
Phi = np.vectorize(lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2))))
pb = quant.Plot(ax, (11.4, 1.8, 6.6, 6.4), (-5, 5), (0, 1.05), xlabel="Expected intake minus requirement, m − R",
                ylabel="Probability of survival", xticks=[-4, -2, 0, 2, 4], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (9.8, 9.6))
d = np.linspace(-5, 5, 300)
pb.line(d, Phi(d / 1.0), "dna", lw=2.2)
pb.line(d, Phi(d / 3.0), "rna", lw=2.2, dashed=True)
pb.vline(0)
pb.text(-4.8, 0.42, "risk-prone:\nvariable better", ha="left", va="top", color=P.muted())
pb.text(4.8, 0.62, "risk-averse:\nsafe better", ha="right", va="bottom", color=P.muted())
pb.legend([("low variance (s = 1)", "dna", "-"), ("high variance (s = 3)", "rna", "--")], at=(12.0, 7.9))

# ---- C: Jensen's inequality ---------------------------------------------------------------------------
pc = quant.Plot(ax, (21.0, 1.8, 6.4, 6.4), (0, 10), (0, 1.05), xlabel="Food obtained",
                ylabel="Fitness (probability of survival)", xticks=[0, 2, 4, 6, 8, 10], yticks=[0, 0.5, 1])
bio.panel(ax, "C", (19.4, 9.6))
x = np.linspace(0, 10, 300)
w = 1 / (1 + np.exp(-(x - 5) * 1.3))
pc.line(x, w, "ink", lw=2.0)
W = lambda v: 1 / (1 + np.exp(-(v - 5) * 1.3))  # noqa: E731
for (lo, hi), tok, lab in (((1.5, 4.5), "rna", "convex region:\nE[w] > w(E)"), ((5.5, 8.5), "dna", "concave region:\nE[w] < w(E)")):
    pc.line([lo, hi], [W(lo), W(hi)], tok, lw=1.2, dashed=True)
    m = (lo + hi) / 2
    pc.points([m], [(W(lo) + W(hi)) / 2], tok, r=0.11)
    pc.points([m], [W(m)], tok, r=0.11, hollow=True)
pc.text(0.3, 0.6, "convex: variance\nincreases mean fitness", ha="left", token="rna")
pc.text(9.8, 0.42, "concave: variance\ndecreases it", ha="right", token="dna")
