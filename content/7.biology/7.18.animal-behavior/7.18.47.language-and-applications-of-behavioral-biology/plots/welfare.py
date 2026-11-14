# Assessing animal welfare. A: the Five Domains model (Mellor and Reid 1994; Mellor et al. 2020): four
# physical or functional domains (nutrition, physical environment, health, behavioral interactions)
# give rise to experiences in the fifth, the mental state, which is the welfare state of the animal.
# B: consumer demand (after Dawkins 1990; exponential demand equation of Hursh and Silberberg 2008):
# consumption Q of a resource as the price (lever presses per reward) increases,
# log10 Q = log10 Q0 + k (exp(-a Q0 C) - 1), with Q0 = 100, k = 2, and a = 0.00005 (an inelastic demand,
# as for food) or a = 0.0006 (an elastic demand). Illustrative curves, not data: a resource for which
# an animal keeps paying as the price rises is one whose lack is likely to impair welfare.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 10.0)
bio.panel(ax, "A", (0.3, 9.6))
doms = [("1 Nutrition", "food, water"), ("2 Physical\nenvironment", "space, shelter,\nthermal comfort"),
        ("3 Health", "injury, disease,\nfitness"), ("4 Behavioral\ninteractions", "with environment,\nother animals, humans")]
for k, (t, sub) in enumerate(doms):
    x = 1.6 + k * 2.75
    bio.box(ax, (x, 8.0), 2.5, 1.2, "dna", text=t, size="small")
    bio.label(ax, (x, 6.75), sub, size="tiny", color=P.muted())
    bio.arrow(ax, (x, 6.15), (5.75 + (x - 5.75) * 0.3, 4.75), kind="process", color=P.muted())
bio.box(ax, (5.75, 4.1), 6.0, 1.2, "positive", text="5 Mental state: affective experiences", size="small")
bio.label(ax, (5.75, 3.0), "negative (hunger, pain, fear, frustration, boredom)\nand positive (comfort, play, exploration, reward)",
          size="tiny", color=P.muted())
bio.arrow(ax, (5.75, 2.35), (5.75, 1.6), kind="process", color=P.muted())
bio.box(ax, (5.75, 1.1), 4.6, 0.8, "highlight", text="welfare state", size="small")

pb = quant.Plot(ax, (14.6, 1.9, 8.4, 6.6), (0, 2), (0, 2.1), xlabel="Price (lever presses per reward)",
                ylabel="Consumption (rewards per session)",
                xticks=[(0, "1"), (1, "10"), (2, "100")], yticks=[(0, "1"), (1, "10"), (2, "100")])
bio.panel(ax, "B", (13.0, 9.6))
lc = np.linspace(0, 2, 200)
C = 10 ** lc
for a, tok, txt, at, dy in ((0.00005, "dna", "inelastic demand (e.g. food)", 0.55, 0.3),
                            (0.0006, "rna", "elastic demand", 0.6, 0.0)):
    q = 2 + 2 * (np.exp(-a * 100 * C) - 1)
    pb.line(lc, q, tok, lw=2.0, text=txt, at=at, dy=dy, dx=0.35 if tok == "rna" else 0.08)
