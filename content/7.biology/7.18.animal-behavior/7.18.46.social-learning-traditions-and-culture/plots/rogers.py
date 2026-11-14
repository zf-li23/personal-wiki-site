# Rogers' paradox (Rogers 1988) and its resolution by critical social learners (Enquist, Eriksson and
# Ghirlanda 2007). The environment changes each generation with probability u; behavior adapted to the
# current environment adds a benefit b to a baseline fitness w0. Individual learners always acquire the
# adaptive behavior at a cost c. Social learners copy a random adult of the previous generation at no cost;
# the copied behavior is adaptive if the model's behavior was adaptive and the environment has not changed.
# With a fraction p of social learners, the proportion of adaptive behavior at equilibrium is
# q = (1 - p) / (1 - p (1 - u)). Fitness: W_I = w0 + b - c, W_S = w0 + b (1 - u) q. Critical social learners
# copy and, if the copied behavior fails, learn individually: W_C = w0 + b - c (1 - (1 - u) q).
# Parameters: w0 = 1, b = 1, c = 0.3, u = 0.1. A: fitness against p in a population of individual and
# social learners. B: mean fitness at equilibrium against the cost of individual learning.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
w0, b, u = 1.0, 1.0, 0.1


def q_eq(p):
    return (1 - p) / (1 - p * (1 - u))


fig, ax = bio.canvas(22, 9.6)
pa = quant.Plot(ax, (2.0, 1.8, 7.8, 6.6), (0, 1), (1.0, 2.05), xlabel="Fraction of social learners p",
                ylabel="Fitness", xticks=[0, 0.25, 0.5, 0.75, 1.0], yticks=[1.0, 1.5, 2.0])
bio.panel(ax, "A", (0.2, 9.3))
c = 0.3
p = np.linspace(0, 0.999, 400)
q = q_eq(p)
WI = np.full_like(p, w0 + b - c)
WS = w0 + b * (1 - u) * q
Wm = p * WS + (1 - p) * WI
pa.line(p, WI, "dna", lw=2.0, text="individual learners", at=0.05, dy=-0.22)
pa.line(p, WS, "rna", lw=2.0, text="social learners", at=0.08, dy=0.1)
pa.line(p, Wm, "neutral", lw=1.6, dashed=True, text="population mean", at=0.33, dy=0.22)
ps = p[np.argmin(np.abs(WS - WI))]
pa.vline(ps, text=f"equilibrium p* = {ps:.2f}")
pa.points([ps], [w0 + b - c], "ink", r=0.11)

pb = quant.Plot(ax, (13.0, 1.8, 7.8, 6.6), (0, 0.6), (1.0, 2.05), xlabel="Cost of individual learning c",
                ylabel="Mean fitness at equilibrium", xticks=[0, 0.2, 0.4, 0.6], yticks=[1.0, 1.5, 2.0])
bio.panel(ax, "B", (11.2, 9.3))
cs = np.linspace(0, 0.6, 121)
pure = w0 + b - cs
mixed = pure.copy()  # Rogers: the mixed equilibrium has the same mean fitness as pure individual learning
crit = []
for cc in cs:
    # a population of critical learners: q = 1 (all end with adaptive behavior); copying succeeds with prob 1 - u
    crit.append(w0 + b - cc * u)
pb.line(cs, pure, "dna", lw=2.0)
pb.text(0.03, 1.3, "individual learners only, or mixed with", ha="left", token="dna")
pb.text(0.03, 1.24, "social learners at equilibrium (identical)", ha="left", token="rna")
pb.line(cs, mixed, "rna", lw=1.6, dashed=True, )
pb.line(cs, crit, "positive", lw=2.0, text="critical social learners", at=0.5, dy=0.1)
