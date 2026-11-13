# Model: allometry of gas exchange across bird eggshells. (A) Water-vapour conductance of the shell
# G = 0.432 W^0.780 (mg per day per Torr; W = fresh egg mass in g; Ar et al. 1974) and incubation time
# I = 12.03 W^0.217 (days; Rahn & Ar 1974). (B) Fraction of the initial egg mass lost as water during
# incubation, M/W = G * dP * I / W with a vapour-pressure difference dP = 34 Torr between egg and nest air:
# because the exponents of G and I add to about 1, the predicted loss is nearly independent of egg size
# (about 18 %), close to the measured average of 15-18 %. Egg masses marked: hummingbird 0.5 g, chicken 60 g,
# ostrich 1500 g.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(23, 8.5)
W = np.logspace(np.log10(0.3), np.log10(2000), 200)
G = 0.432 * W ** 0.780
I = 12.03 * W ** 0.217
p = quant.Plot(ax, (1.8, 1.4, 8.4, 6.0), xlim=(0.3, 2000), ylim=(0.1, 1000), xlog=True, ylog=True,
               xlabel="fresh egg mass / g", ylabel="G / mg d-1 Torr-1;  I / d",
               xticks=[1, 10, 100, 1000], yticks=[0.1, 1, 10, 100, 1000])
p.line(W, G, "dna", text="shell conductance G", at=0.3, dy=-0.7)
p.line(W, I, "mrna", text="incubation time I", at=0.08, dy=0.25)
for w, name in ((0.5, "hummingbird"), (60, "chicken"), (1500, "ostrich")):  # noqa
    p.points([w], [0.432 * w ** 0.780], "dna")
    p.text(w * 1.25, 0.432 * w ** 0.780 / 2.4, name, ha="left")
bio.panel(ax, "A", (0.4, 8.1))

frac = 100 * G * 34 * I / (W * 1000)
q = quant.Plot(ax, (13.6, 1.4, 8.4, 6.0), xlim=(0.3, 2000), ylim=(0, 30), xlog=True,
               xlabel="fresh egg mass / g", ylabel="water lost during incubation / %",
               xticks=[1, 10, 100, 1000], yticks=[0, 10, 20, 30])
q.band(W, np.full_like(W, 15), np.full_like(W, 18), "highlight")
q.line(W, frac, "dna", text="predicted G x dP x I / W", at=0.35, dy=0.35)
q.text(1.0, 13.0, "measured range 15-18 %", ha="left")
bio.panel(ax, "B", (12.2, 8.1))
