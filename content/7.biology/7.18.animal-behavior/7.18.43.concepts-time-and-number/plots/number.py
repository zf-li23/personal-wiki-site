# The approximate number system. A: discrimination of two numerosities n1 < n2 by an observer whose internal
# representation of a numerosity n is Gaussian with mean n and standard deviation w n (scalar variability,
# Weber fraction w = 0.25); the probability of choosing the larger set is Phi((n2 - n1) / (w sqrt(n1^2 + n2^2))).
# Plotted against the ratio n1 / n2 for small (n1 from 2 to 6) and large (n1 from 10 to 30) pairs, accuracy
# falls on a single curve: it depends on the ratio, not on the difference (as found in monkeys, birds, fish and
# human infants). B: tuning of "number neurons" of the prefrontal cortex of monkeys (after Nieder and Miller
# 2003): each neuron fires most for a preferred numerosity; plotted on a linear axis the tuning curves are
# asymmetric and broaden with the preferred number, on a logarithmic axis they are symmetric Gaussians of
# equal width (s.d. 0.12 in log10 units) - the compressed, logarithmic code of the Weber-Fechner law.
import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 9.4)
W = 0.25

pa = quant.Plot(ax, (2.0, 1.8, 7.6, 6.4), (0.3, 1.0), (0.4, 1.02), xlabel="Ratio n1 / n2 (smaller / larger)",
                ylabel="Proportion correct", xticks=[0.4, 0.6, 0.8, 1.0], yticks=[0.5, 0.75, 1.0])
bio.panel(ax, "A", (0.2, 9.2))
r = np.linspace(0.3, 1.0, 200)
pa.line(r, norm.cdf((1 - r) / (W * np.sqrt(1 + r ** 2))), "muted", lw=1.2, dashed=True)
pa.hline(0.5, text="chance", side="left")
for n1s, tok, hollow in (((10, 15, 20, 30), "dna", True), ((2, 3, 4, 5, 6), "rna", False)):
    for n1 in n1s:
        for n2 in range(n1 + 1, int(n1 / 0.3) + 1):
            if n1 / n2 < 0.3:
                continue
            pa.points([n1 / n2], [norm.cdf((n2 - n1) / (W * np.hypot(n1, n2)))], tok, r=0.1 if hollow else 0.06, hollow=hollow)
pa.legend([("small sets (2-6 vs more)", "rna", "-"), ("large sets (10-30 vs more)", "dna", "-")], at=(5.4, 7.6))

pb = quant.Plot(ax, (12.6, 1.8, 8.4, 6.4), (0, 1.0), (0, 1.05), xlabel="Numerosity (logarithmic axis)",
                ylabel="Firing rate (relative)", xticks=[(0, "1"), (np.log10(2), "2"), (np.log10(4), "4"),
                                                          (np.log10(8), "8"), (1.0, "10")], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.8, 9.2))
lx = np.linspace(0, 1.0, 300)
for k, (pref, tok) in enumerate(((1, "rna"), (2, "protein"), (3, "atp"), (4, "positive"), (5, "dna"))):
    pb.line(lx, np.exp(-0.5 * ((lx - np.log10(pref)) / 0.12) ** 2), tok, lw=1.8)
    pb.text(np.log10(pref), 1.04, str(pref), va="bottom", token=tok)
pb.text(0.98, 0.9, "preferred numerosity", ha="right", size="tiny", color=P.muted())
