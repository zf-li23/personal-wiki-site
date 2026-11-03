"""Taxonomic survivorship curves (Section 31.3.2). Durations of 2000 simulated genera: with a constant
extinction rate of 0.1 per Myr (blue) durations are exponential, so the number surviving to age t,
plotted on a logarithmic axis, falls on a straight line of slope -0.1 (Van Valen's law of constant
extinction). If extinction risk declines as a taxon ages (orange, a Weibull hazard with shape 0.6 and
the same mean duration), the curve is concave with a long tail of old survivors. The age of a genus
does not then predict its risk in the first case, but does in the second."""
import numpy as np
import matplotlib.pyplot as plt
from math import gamma
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(2)
n = 2000
d_const = rng.exponential(10.0, n)
k = 0.6
scale = 10.0 / gamma(1 + 1 / k)
d_dec = scale * rng.weibull(k, n)
t = np.linspace(0, 60, 241)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
for d, tok, lab in ((d_const, "dna", "constant extinction rate"), (d_dec, "rna", "rate declines with age")):
    surv = np.array([(d >= x).sum() for x in t])
    a.semilogy(t, np.maximum(surv, 0.8), color=charts.line(tok), lw=1.8, label=lab)
    # hazard estimated in 5-Myr intervals
    edges = np.arange(0, 45, 5.0)
    hz = []
    for e0, e1 in zip(edges[:-1], edges[1:]):
        at_risk = (d >= e0).sum()
        died = ((d >= e0) & (d < e1)).sum()
        hz.append(died / at_risk / 5.0 if at_risk > 20 else np.nan)
    b.plot((edges[:-1] + edges[1:]) / 2, hz, "o-", color=charts.line(tok), lw=1.5, ms=4)
a.set_ylim(0.8, 3000)
charts.style_axes(a, "age of taxon (Myr)", "genera surviving to this age")
charts.title(a, "A  Survivorship (log scale)")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
b.set_ylim(0, 0.25)
charts.style_axes(b, "age of taxon (Myr)", "extinction rate (per Myr)")
charts.title(b, "B  Estimated extinction rate by age")
