"""Capacity of a combinatorial receptor code and decorrelation by lateral inhibition.

A: number of distinguishable codes with N receptor types if each odour is identified by
(i) the single most activated receptor (labelled line, N codes), (ii) which k receptors are
active (binomial coefficient C(N, k), k = 3 and 10), (iii) any on/off pattern (2^N).
Vertical lines: about 50 receptor genes (Drosophila), 350-400 (human), about 1100 (mouse).
B, C: 200 glomeruli ordered along one molecular feature (chemotopy, e.g. carbon-chain length);
an odour excites a Gaussian band of glomeruli (width 18). Lateral inhibition in the bulb
(periglomerular and granule cells) is modelled as subtracting a Gaussian-weighted average of the
surrounding activity (width 30, gain 1) and rectifying: y = max(x - K x, 0).
C: overlap (cosine similarity) between the patterns of two odours as a function of their separation.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gammaln

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)

fig, axs = plt.subplots(1, 3, figsize=(13, 4.1))
ax = axs[0]
N = np.arange(1, 1201)
ax.plot(N, np.log10(N), color=P.muted(), lw=2, label="labelled line: N")
for k, c in ((3, P.edge("dna")), (10, P.edge("rna"))):
    n = N[N >= k]
    lc = (gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)) / np.log(10)
    ax.plot(n, lc, color=c, lw=2, label=f"k = {k} active: C(N, k)")
ax.plot(N, N * np.log10(2), color=P.edge("enzyme"), lw=1.6, ls="--", label="any on/off pattern: 2$^N$")
for g, lab in ((50, "fly"), (380, "human"), (1100, "mouse")):
    ax.axvline(g, color=P.muted(), lw=0.6, ls=":")
    ax.text(g, 52, lab, fontsize=8, color=P.muted(), rotation=90, ha="right", va="top")
ax.set_ylim(0, 55)
ax.set_xlim(0, 1200)
ax.set_xlabel("Number of receptor types N")
ax.set_ylabel(r"log$_{10}$ (number of codes)")
ax.legend(frameon=False, fontsize=8, loc="center right")
ax.set_title("A  Combinatorial capacity", loc="left", fontsize=10)

G = 200
pos = np.arange(G)


def profile(mu, width=18.0):
    """Glomerular input for an odour at position mu on a chemical-feature axis."""
    return np.exp(-(pos - mu) ** 2 / (2 * width**2))


kern = np.exp(-(pos[:, None] - pos[None, :]) ** 2 / (2 * 30.0**2))
kern /= kern.sum(axis=1, keepdims=True)


def bulb(x, g=1.0):
    return np.clip(x - g * kern @ x, 0, None)


bx = axs[1]
a, b = profile(90), profile(110)
ya, yb = bulb(a), bulb(b)
bx.plot(pos, a, color=P.edge("dna"), lw=1.2, ls="--")
bx.plot(pos, b, color=P.edge("rna"), lw=1.2, ls="--")
bx.plot(pos, ya / ya.max(), color=P.edge("dna"), lw=2, label="odour 1 (output)")
bx.plot(pos, yb / yb.max(), color=P.edge("rna"), lw=2, label="odour 2 (output)")
bx.plot([], [], color=P.muted(), ls="--", label="glomerular input")
bx.set_xlabel("Glomeruli ordered by molecular feature (e.g. chain length)")
bx.set_ylabel("Activity (normalised)")
bx.set_xlim(20, 180)
bx.set_ylim(0, 1.1)
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Inhibition sharpens the patterns", loc="left", fontsize=10)

cx = axs[2]
d = np.arange(0, 81, 2)
def cos(u, v):
    return u @ v / np.sqrt((u @ u) * (v @ v))


rin = [cos(profile(100 - k / 2), profile(100 + k / 2)) for k in d]
rout = [cos(bulb(profile(100 - k / 2)), bulb(profile(100 + k / 2))) for k in d]
cx.plot(d, rin, color=P.muted(), lw=2, ls="--", label="glomerular input")
cx.plot(d, rout, color=P.edge("dna"), lw=2, label="bulb output")
cx.axvline(20, color=P.muted(), lw=0.6, ls=":")
cx.set_xlabel("Difference between the two odours (feature units)")
cx.set_ylabel("Pattern overlap (cosine similarity)")
cx.set_ylim(0, 1.02)
cx.legend(frameon=False, fontsize=8, loc="upper right")
cx.set_title("C  Similar odours are decorrelated", loc="left", fontsize=10)
fig.tight_layout()
