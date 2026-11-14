# Search images and apostatic selection (illustrative model). A: the proportion of prey morph 1 in a
# predator's diet as a function of its proportion in the environment. Without preference the two are equal
# (diagonal). A predator that forms a search image for the commoner morph overeats it (apostatic
# selection); a convenient form is diet = p^k / (p^k + (1 - p)^k) with k = 2. B: a population of three cryptic
# morphs, one of them (dark line) six times harder to detect than the others, hunted by predators whose risk of
# detecting a morph rises with its frequency (search image): each generation the survival of morph i is
# exp(-A d_i f_i), with detectability d = (1, 1, 1/6), frequency f_i and A = 1.5, and survivors are restored
# to the original population size. Starting from equal numbers, the most cryptic morph increases but does not
# take over: the population settles at 75 : 12.5 : 12.5 percent, where all morphs have equal risk, the outcome
# of Bond and Kamil's (1998) "virtual ecology" experiment with blue jays hunting digital moths.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(21.0, 9.8)

pa = quant.Plot(ax, (2.0, 1.8, 6.4, 6.4), (0, 1), (0, 1), xlabel="Proportion of morph 1 in the environment",
                ylabel="Proportion of morph 1 in the diet", xticks=[0, 0.5, 1], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.6))
p = np.linspace(0, 1, 200)
pa.line(p, p, "muted", lw=1.2, dashed=True)
pa.line(p, p ** 2 / (p ** 2 + (1 - p) ** 2), "rna", lw=2.2)
pa.text(0.62, 0.5, "no preference", ha="left", color=P.muted())
pa.text(0.5, 0.85, "apostatic: the commoner\nmorph is overeaten", ha="right", token="rna")
pa.text(0.97, 0.06, "rare morph protected\nbelow 0.5", ha="right", va="bottom", color=P.muted())

pb = quant.Plot(ax, (11.6, 1.8, 8.4, 6.4), (0, 50), (0, 1), xlabel="Generation", ylabel="Morph frequency",
                xticks=[0, 10, 20, 30, 40, 50], yticks=[0, 0.25, 0.5, 0.75, 1])
bio.panel(ax, "B", (10.0, 9.6))
d = np.array([1.0, 1.0, 1 / 6])
f = np.array([0.34, 1 / 3, 0.326])
f = f / f.sum()
hist = [f.copy()]
for _ in range(50):
    s = np.exp(-1.5 * d * f)
    f = f * s / np.sum(f * s)
    hist.append(f.copy())
hist = np.array(hist)
g = np.arange(51)
pb.line(g, hist[:, 2], "ink", lw=2.4)
pb.line(g, hist[:, 0], "dna", lw=1.8)
pb.line(g, hist[:, 1], "rna", lw=1.8, dashed=True)
pb.hline(0.75, text="0.75", side="right")
pb.hline(0.125, text="0.125", side="right")
pb.text(30, 0.82, "most cryptic morph", ha="left")
pb.text(30, 0.2, "two more conspicuous morphs", ha="left", color=P.muted())
