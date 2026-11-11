"""Optimal coding under two constraints: a limited response range and a limited energy budget.

A, B (Laughlin 1981, schematic): natural contrasts c are distributed roughly as a Laplacian of
scale 0.25 (truncated to [-1, 1]); a noiseless neuron with outputs in [0, r_max] transmits the most
information when its response function is r_max times the cumulative distribution F(c). A: the
distribution (histogram of samples) and the optimal response function (the CDF) compared with a
linear response. B: histograms of responses for the two codes; the CDF code uses all response
levels equally (maximal entropy, here with 10 levels).
C (Levy and Baxter 1996): a binary neuron fires in a time bin with probability p; the information it
can transmit is at most the binary entropy h(p) bits, and the energy cost per bin is b + p, with
the resting cost b relative to the cost of a spike. Bits per unit energy h(p)/(b + p), for b = 1, 0.1,
0.01; the optimum moves to small p (sparse firing) when spikes are expensive relative to rest.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(4)
c = rng.laplace(0, 0.25, 40000)
c = c[np.abs(c) < 1]
cs = np.sort(c)
grid = np.linspace(-1, 1, 400)
F = np.searchsorted(cs, grid) / len(cs)

fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))
ax = axs[0]
ax.hist(c, bins=60, density=True, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.3,
        label="contrast distribution p(c)")
ax.set_xlabel("Contrast c")
ax.set_ylabel("Probability density")
a2 = ax.twinx()
a2.plot(grid, F, color=P.edge("dna"), lw=2, label="optimal response r/r$_{max}$ = F(c)")
a2.plot(grid, (grid + 1) / 2, color=P.edge("rna"), lw=1.5, ls="--", label="linear response")
a2.set_ylabel("Response r / r$_{max}$")
a2.set_ylim(0, 1.05)
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = a2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("A  Response function = cumulative distribution", loc="left", fontsize=10)

bx = axs[1]
lev = np.linspace(0, 1, 11)
r_opt = np.interp(c, grid, F)
r_lin = (c + 1) / 2
for r, col, lab, off in ((r_lin, P.edge("rna"), "linear code", -0.022), (r_opt, P.edge("dna"), "CDF code", 0.022)):
    h, _ = np.histogram(r, lev)
    p = h / h.sum()
    H = -(p[p > 0] * np.log2(p[p > 0])).sum()
    bx.bar(0.5 * (lev[1:] + lev[:-1]) + off, p, width=0.04, color=col, label=f"{lab}: H = {H:.2f} bits")
bx.set_ylim(0, 0.38)
bx.axhline(0.1, color=P.muted(), lw=0.8, ls=":")
bx.set_xlabel("Response level (10 bins)")
bx.set_ylabel("Fraction of time")
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Histogram equalization (max 3.32 bits)", loc="left", fontsize=10)

cx = axs[2]
p = np.logspace(-4, -0.0001, 400)
h = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
for b, col in ((1.0, P.edge("dna")), (0.1, P.edge("rna")), (0.01, P.edge("positive"))):
    eff = h / (b + p)
    cx.plot(p, eff / eff.max(), color=col, lw=1.8, label=f"rest/spike cost b = {b}")
    cx.plot(p[np.argmax(eff)], 1, "o", color=col, ms=5)
cx.set_xscale("log")
cx.set_xlabel("Firing probability per bin p")
cx.set_ylabel("Bits per unit energy (normalized)")
cx.legend(frameon=False, fontsize=8, loc="lower center")
cx.set_title("C  Energy efficiency favors sparse firing", loc="left", fontsize=10)
fig.tight_layout()
