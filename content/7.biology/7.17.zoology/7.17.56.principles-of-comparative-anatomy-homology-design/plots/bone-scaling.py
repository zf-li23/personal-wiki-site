# Model: three similarity rules for the scaling of a long bone with body mass M, relative to a 10 g animal
# (log-log axes). Geometric similarity: length l and diameter d both proportional to M^(1/3). Elastic similarity
# (McMahon 1973): l ~ M^(1/4), d ~ M^(3/8), so that d ~ l^(3/2). Static stress similarity: d ~ M^(1/2).
# (B) slenderness l/d under each rule. The line labelled "mammal femora" uses only the exponents reported by
# Alexander et al. (1979) for femur length (0.35) and diameter (0.36) across mammals; it is not a fit to data
# shown here. All curves are normalized to the same value at 10 g.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 9)
M = np.logspace(-2, 4, 200)  # kg
r = M / 0.01
p = quant.Plot(ax, (2.0, 1.5, 8.6, 6.4), xlim=(0.01, 10000), ylim=(1, 1e4), xlog=True, ylog=True,
               xlabel="body mass / kg", ylabel="relative bone dimension",
               xticks=[0.01, 1, 100, 10000], yticks=[1, 10, 100, 1000, 10000])
p.line(M, r ** (1 / 3), "dna")
p.line(M, r ** 0.25, "mrna")
p.line(M, r ** 0.375, "mrna", dashed=True)
p.line(M, r ** 0.5, "neutral", dotted=True)
for yy, s_, tok in ((3000, "static stress: d ~ M^1/2 (dotted)", "neutral"), (1300, "elastic: d ~ M^3/8 (dashed)", "mrna"),
                    (560, "geometric: l and d ~ M^1/3", "dna"), (240, "elastic: l ~ M^1/4", "mrna")):
    p.text(0.02, yy, s_, token=tok, ha="left")
bio.panel(ax, "A", (0.4, 8.6))

q = quant.Plot(ax, (14.0, 1.5, 8.6, 6.4), xlim=(0.01, 10000), ylim=(0.05, 2), xlog=True, ylog=True,
               xlabel="body mass / kg", ylabel="slenderness l / d (relative)",
               xticks=[0.01, 1, 100, 10000], yticks=[0.1, 0.5, 1, 2])
q.line(M, np.ones_like(M), "dna", text="geometric", at=0.05, dy=0.12)
q.line(M, r ** (0.25 - 0.375), "mrna", text="elastic", at=0.05, dy=-0.25)
q.line(M, r ** (0.35 - 0.36), "positive", dashed=True, text="mammal femora (exponents 0.35, 0.36)", at=0.35, dy=0.3)
bio.panel(ax, "B", (12.4, 8.6))
