"""The value of information for the decision of Example 37.3.1.

Binary condition (high or low quality), binary signal whose probability of matching the condition is q.
VI = expected payoff when deciding after the signal minus the payoff of the default action.
A: VI against the prior for three reliabilities. B: VI over prior and reliability, with the contour
VI = 0.2 (an attention cost).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
R = np.array([[10.0, 2.0], [5.0, 5.0]])  # rows: accept, reject; columns: high, low


def best(p):
    return np.maximum(R[0, 0] * p + R[0, 1] * (1 - p), R[1, 0] * p + R[1, 1] * (1 - p))


def vi(p, q):
    ps1 = q * p + (1 - q) * (1 - p)          # P(signal "high")
    post1 = q * p / ps1
    ps0 = 1 - ps1
    post0 = (1 - q) * p / ps0
    return ps1 * best(post1) + ps0 * best(post0) - best(p)


fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
p = np.linspace(0.001, 0.999, 400)
for q, tok in ((0.6, "neutral"), (0.75, "rna"), (0.9, "dna")):
    a.plot(p, vi(p, q), color=P.edge(tok), lw=1.7, label=f"reliability q = {q}")
a.axvline(3 / 8, color=P.edge("negative"), ls="--", lw=1.1)
a.text(3 / 8 + 0.02, 1.85, "red line", color=P.edge("negative"), fontsize=8)
a.set_xlabel("Prior probability of high quality, p")
a.set_ylabel("Value of information")
a.set_xlim(0, 1); a.set_ylim(0, 2.0)
a.legend(frameon=False, fontsize=8)
a.set_title("A", loc="left", fontweight="bold")

pp, qq = np.meshgrid(np.linspace(0.005, 0.995, 200), np.linspace(0.5, 0.995, 200))
z = vi(pp, qq)
im = b.pcolormesh(pp, qq, z, cmap="viridis", shading="auto", rasterized=True)
cs = b.contour(pp, qq, z, levels=[0.2], colors=[P.ink()], linewidths=1.2)
b.clabel(cs, fmt={0.2: "VI = 0.2"}, fontsize=7)
b.axvline(3 / 8, color=P.edge("negative"), ls="--", lw=1.0)
cb = fig.colorbar(im, ax=b, fraction=0.05, pad=0.03)
cb.set_label("Value of information", fontsize=8)
b.set_xlabel("Prior probability of high quality, p")
b.set_ylabel("Reliability q")
b.set_title("B", loc="left", fontweight="bold")
for sp in ("top", "right"):
    a.spines[sp].set_visible(False)
fig.tight_layout()
