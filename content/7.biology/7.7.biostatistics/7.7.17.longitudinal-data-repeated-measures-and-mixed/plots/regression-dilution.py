"""Regression dilution (simulation, seed 0). The outcome depends on a usual (long-term) level X with slope
1: Y = X + e. The exposure is measured once, W = X + U, with reliability ICC = var(X) / var(W).

A: 400 simulated people with reliability 0.5: the regression of Y on the true X (slope about 1) and on the
single measurement W (slope about 0.5). B: the estimated slope against the reliability of the measurement,
for 200 replicates at each reliability (points: means; line: the attenuation factor itself), and the
slope after dividing by the reliability estimated from a repeat measurement on 100 people.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
n = 400
x = rng.normal(0, 1, n)
w = x + rng.normal(0, 1, n)
yv = x + rng.normal(0, 0.8, n)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.87, wspace=0.25)
ax = axs[0]
ax.plot(w, yv, "o", ms=2.5, color=P.fill("neutral"), mec=charts.line("neutral"), mew=0.3, label="observed W")
xx = np.array([-4, 4])
for v, tok, lab in [(x, "dna", "on true X"), (w, "rna", "on one measurement W")]:
    b = np.polyfit(v, yv, 1)
    ax.plot(xx, b[1] + b[0] * xx, color=charts.line(tok), lw=2, label=f"slope {lab}: {b[0]:.2f}")
ax.set_xlim(-4, 4)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "exposure", "outcome Y")
charts.title(ax, "A  Reliability 0.5")
ax = axs[1]
rels = np.array([0.2, 0.35, 0.5, 0.65, 0.8, 0.95])
naive, corr = [], []
for r in rels:
    su = np.sqrt(1 / r - 1)
    bn, bc = [], []
    for _ in range(200):
        x = rng.normal(0, 1, n)
        w1 = x + rng.normal(0, su, n)
        y = x + rng.normal(0, 0.8, n)
        b = np.polyfit(w1, y, 1)[0]
        w2 = x[:100] + rng.normal(0, su, 100)
        lam = np.corrcoef(w1[:100], w2)[0, 1]
        bn.append(b)
        bc.append(b / lam)
    naive.append(np.mean(bn))
    corr.append(np.median(bc))
rr = np.linspace(0.1, 1, 50)
ax.plot(rr, rr, color=P.muted(), lw=1, label="attenuation factor = reliability")
ax.plot(rels, naive, "o", ms=5, color=charts.line("rna"), label="naive slope (mean)")
ax.plot(rels, corr, "s", ms=5, color=charts.line("dna"), label="corrected slope (median)")
ax.axhline(1, color=P.ink(), lw=0.8, ls="--")
ax.set_xlim(0.1, 1.02)
ax.set_ylim(0, 1.3)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "reliability of a single measurement (ICC)", "estimated slope (true = 1)")
charts.title(ax, "B  Attenuation and its correction")
