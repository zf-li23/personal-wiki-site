"""Information in the honey bee waggle dance (schematic).

A: waggle-run duration = 1.0 s/km x distance (+ 0.1 s), with 8 % multiplicative noise per run.
B: angular scatter sigma(d) = 4 + 30 exp(-d / 0.4) degrees.
C: direction information per run, log2(360) - log2(sigma sqrt(2 pi e)) bits.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6))
a, b, c = axs
d = np.linspace(0.1, 4, 200)
dist = rng.uniform(0.1, 4, 120)
dur = (1.0 * dist + 0.1) * rng.normal(1, 0.08, dist.size)
a.scatter(dist, dur, s=8, color=P.light("dna"), edgecolor=P.edge("dna"), lw=0.4)
a.plot(d, 1.0 * d + 0.1, color=P.ink(), lw=1.5)
a.set_xlabel("Distance to food / km"); a.set_ylabel("Waggle-run duration / s")
sig = 4 + 30 * np.exp(-d / 0.4)
b.plot(d, sig, color=P.edge("rna"), lw=1.8)
b.set_xlabel("Distance to food / km"); b.set_ylabel("Directional scatter (s.d.) / deg")
bits = np.log2(360) - np.log2(sig * np.sqrt(2 * np.pi * np.e))
c.plot(d, bits, color=P.edge("positive"), lw=1.8, label="one run")
c.plot(d, bits + 0.5 * np.log2(4), color=P.edge("positive"), lw=1.2, ls="--", label="mean of 4 runs")
c.set_xlabel("Distance to food / km"); c.set_ylabel("Direction information / bit")
c.set_ylim(0, 6); c.legend(frameon=False, fontsize=8, loc="lower right")
for ax, t in zip(axs, "ABC"):
    ax.set_title(t, loc="left", fontweight="bold")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
