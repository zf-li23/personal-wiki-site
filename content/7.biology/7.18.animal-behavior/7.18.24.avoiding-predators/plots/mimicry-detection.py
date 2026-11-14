# Batesian mimicry as a problem of signal detection for the predator (after Oaten, Pearce and Smyth 1975 and
# Sherratt 2002; illustrative parameters). The predator perceives an appearance x; noxious models give
# x ~ N(0, 1), palatable mimics x ~ N(d, 1), where d measures how imperfect the mimicry is. A proportion m of
# the prey with the pattern are mimics; eating a mimic gains B = 1, attacking a model costs C. Attacking every
# item with x > c maximizes the expected payoff when the likelihood ratio at the criterion equals
# (1 - m) C / (m B), which gives c* = d / 2 + ln[(1 - m) C / (m B)] / d. A: the two distributions with d = 1.5,
# m = 0.3 and C/B = 4; mimics attacked (blue) and models attacked by mistake (red) beyond the criterion.
# B: probability that a mimic is attacked as a function of the proportion of mimics, for good, moderate and
# poor mimics (d = 0.5, 1, 2): protection falls as mimics become common, and good mimics are protected even
# when fairly common. C: the same as a function of the noxiousness of the model (C/B), for m = 0.3: more noxious
# models make predators more cautious and protect more, and less perfect, mimics.
import numpy as np
from scipy.stats import norm

import wikibio as bio
import wikibehav as wb
from wikibio import quant

P = bio.P


def crit(d, m, k):
    return d / 2 + np.log((1 - m) * k / m) / d


def p_attack_mimic(d, m, k):
    return norm.sf(crit(d, m, k) - d)


fig, ax = bio.canvas(28.0, 9.8)

# ---- A ------------------------------------------------------------------------------------------------
d0, m0, k0 = 1.5, 0.3, 4.0
c0 = float(crit(d0, m0, k0))
pa = quant.Plot(ax, (1.6, 1.8, 7.4, 6.4), (-3.2, 5.0), (0, 0.5), xlabel="Appearance perceived by the predator x",
                ylabel="Probability density", xticks=[-2, 0, 2, 4], yticks=[0, 0.2, 0.4])
bio.panel(ax, "A", (0.2, 9.6))
H, F = wb.sdt_panel(pa, d=d0, xc=c0, labels=False)
pa.text(-3.0, 0.42, "noxious\nmodels", ha="left", color=P.muted())
pa.text(-3.0, 0.3, "palatable\nmimics", ha="left", token="dna")
pa.text(c0 - 0.1, 0.49, "attack if x > c*", ha="right", va="top")
pa.text(4.9, 0.47, f"mimics attacked {H:.2f}", ha="right", va="top", token="dna")
pa.text(4.9, 0.42, f"models attacked {F:.2f}", ha="right", va="top", token="negative")

# ---- B ------------------------------------------------------------------------------------------------
pb = quant.Plot(ax, (11.4, 1.8, 6.6, 6.4), (0, 1), (0, 1.02), xlabel="Proportion of mimics m",
                ylabel="Probability a mimic is attacked", xticks=[0, 0.25, 0.5, 0.75, 1], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (9.8, 9.6))
m = np.linspace(0.01, 0.99, 300)
for d, tok, lab, at in ((0.5, "positive", "good mimic, d = 0.5", 0.55), (1.0, "dna", "d = 1", 0.42),
                        (2.0, "rna", "poor mimic, d = 2", 0.18)):
    pb.line(m, p_attack_mimic(d, m, k0), tok, lw=2.0)
pb.legend([("good mimic, d = 0.5", "positive", "-"), ("d = 1", "dna", "-"), ("poor mimic, d = 2", "rna", "-")],
          at=(11.9, 7.9))
pb.text(0.98, 0.06, "C/B = 4", ha="right", color=P.muted())

# ---- C ------------------------------------------------------------------------------------------------
pc = quant.Plot(ax, (21.0, 1.8, 6.4, 6.4), (1, 50), (0, 1.02), xlog=True, xlabel="Noxiousness of the model C/B",
                ylabel="Probability a mimic is attacked", xticks=[(1, "1"), (3, "3"), (10, "10"), (30, "30")],
                yticks=[0, 0.5, 1])
bio.panel(ax, "C", (19.4, 9.6))
k = np.logspace(0, np.log10(50), 200)
for d, tok in ((0.5, "positive"), (1.0, "dna"), (2.0, "rna")):
    pc.line(k, p_attack_mimic(d, 0.3, k), tok, lw=2.0)
pc.text(48, 0.95, "m = 0.3", ha="right", va="top", color=P.muted())
