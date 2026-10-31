# Counting subunits by photobleaching steps (simulation).
# A tetrameric membrane protein with each subunit fused to GFP; each GFP is fluorescent with probability
# p = 0.75 (incomplete maturation) and bleaches at a random exponential time (mean 15 s); each fluorescent
# GFP adds 300 photons per frame (100 ms) on a background of 200, with shot noise and 5 % extra noise.
# A: three example traces with 4, 3 and 2 steps. B: histogram of the number of steps in 300 spots with the
# binomial prediction Bin(4, 0.75) (renormalized over k >= 1, since dark spots are not seen) and, for
# comparison, the prediction for a trimer with the same p.
import matplotlib.pyplot as plt
import numpy as np
from math import comb

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n, p, tb = 4, 0.75, 15.0
t = np.arange(0, 60, 0.1)
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.0), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axs[0]
for k, (nf, off, tok) in enumerate(((4, 0, "dna"), (3, 1700, "rna"), (2, 3400, "protein"))):
    bt = np.sort(rng.exponential(tb, nf))
    lev = (t[:, None] < bt[None, :]).sum(1)
    mu = 200 + 300 * lev
    y = rng.poisson(mu) * (1 + rng.normal(0, 0.05, t.size))
    ax.plot(t, y + off, color=charts.line(tok), lw=0.7)
    ax.step(t, mu + off, color=P.ink(), lw=0.9, where="post")
    ax.text(58, off + 300, f"{nf} steps", fontsize=8, ha="right", color=P.ink())
ax.set_yticks([])
charts.style_axes(ax, "time / s", "photons per frame (offset)")
charts.title(ax, "A   Stepwise bleaching of single complexes")
ax = axs[1]
steps = rng.binomial(n, p, 400)
steps = steps[steps > 0][:300]
h = np.bincount(steps, minlength=5)[1:5] / steps.size
k = np.arange(1, 5)
ax.bar(k, h, width=0.6, color=P.fill("dna"), edgecolor=P.edge("dna"), label="observed (300 spots)")
for nn, tok, mk in ((4, "negative", "o"), (3, "protein", "s")):
    pk = np.array([comb(nn, int(j)) * p**j * (1 - p) ** (nn - j) if j <= nn else 0 for j in k])
    pk /= 1 - (1 - p) ** nn
    ax.plot(k, pk, mk + "-", color=charts.line(tok), lw=1.2, ms=5, label=f"Bin({nn}, {p}), k ≥ 1")
ax.set_xticks(k)
ax.set_ylim(0, 0.6)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "number of bleaching steps k", "fraction of spots")
charts.title(ax, "B   Binomial statistics give the stoichiometry")
fig.tight_layout()
