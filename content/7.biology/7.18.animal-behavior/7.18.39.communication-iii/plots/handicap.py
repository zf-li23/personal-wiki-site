"""Costly signaling: benefit s (b = k = 1) and cost s^2 / (2 q) for q = 1 and q = 2.

A: benefit and cost curves. B: net payoffs s - s^2/(2q) with optima s* = q. C: payoffs at own optimum and
when the low-quality sender imitates the high-quality signal.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
s = np.linspace(0, 3.2, 300)
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6), gridspec_kw={"width_ratios": [1, 1, 0.75]})
a, b, c = axs
a.plot(s, s, color=P.ink(), lw=1.8, label="benefit")
for q, tok in ((1, "rna"), (2, "dna")):
    a.plot(s, s ** 2 / (2 * q), color=P.edge(tok), lw=1.8, label=f"cost, q = {q}")
    b.plot(s, s - s ** 2 / (2 * q), color=P.edge(tok), lw=1.8, label=f"q = {q}")
    b.scatter([q], [q / 2], color=P.edge(tok), zorder=5, s=25)
    b.vlines(q, -1.2, q / 2, color=P.edge(tok), ls=":", lw=1)
b.scatter([2], [0], facecolors="none", edgecolors=P.edge("rna"), s=40, zorder=6, lw=1.5)
b.annotate("q = 1 imitating\nthe q = 2 signal", (2, 0), (0.15, -0.95), fontsize=7.5,
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
a.set_xlabel("Signal level s"); a.set_ylabel("Benefit or cost")
a.set_ylim(0, 3.2); a.legend(frameon=False, fontsize=8)
b.set_xlabel("Signal level s"); b.set_ylabel("Net payoff")
b.set_ylim(-1.2, 1.3); b.axhline(0, color=P.muted(), lw=0.6)
b.legend(frameon=False, fontsize=8, loc="upper right")
labels = ["q = 1\nhonest", "q = 1\nimitating", "q = 2\nhonest"]
vals = [0.5, 0.0, 1.0]
cols = [P.fill("rna"), P.light("rna"), P.fill("dna")]
c.bar(range(3), vals, color=cols, edgecolor=[P.edge("rna"), P.edge("rna"), P.edge("dna")])
c.set_xticks(range(3)); c.set_xticklabels(labels, fontsize=8)
c.set_ylabel("Net payoff"); c.set_ylim(0, 1.2)
for ax, t in zip(axs, "ABC"):
    ax.set_title(t, loc="left", fontweight="bold")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
