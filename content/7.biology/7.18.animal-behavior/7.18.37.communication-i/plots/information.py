"""Mutual information transmitted by a signal set of n equally likely alternatives with consistency q
(probability that the signal matches the condition; errors spread evenly over the other signals).

I = log2 n + q log2 q + (1 - q) log2((1 - q) / (n - 1)).
A: I in bits; B: I as a fraction of log2 n. The band marks consistencies of 0.3 to 0.8.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def info(n, q):
    q = np.asarray(q, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        t1 = np.where(q > 0, q * np.log2(q), 0.0)
        t2 = np.where(q < 1, (1 - q) * np.log2((1 - q) / (n - 1)), 0.0)
    return np.log2(n) + t1 + t2


fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8))
toks = {2: "rna", 3: "dna", 5: "positive"}
for n, tok in toks.items():
    q = np.linspace(1 / n, 1, 300)
    a.plot(q, info(n, q), color=P.edge(tok), lw=1.8, label=f"n = {n}")
    b.plot(q, info(n, q) / np.log2(n), color=P.edge(tok), lw=1.8, label=f"n = {n}")
    a.axvline(1 / n, color=P.edge(tok), ls=":", lw=0.9)
for ax in (a, b):
    ax.axvspan(0.3, 0.8, color=P.light("neutral"), alpha=0.5, lw=0)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Consistency q")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
a.text(0.55, 2.2, "typical animal\nsignal sets", ha="center", fontsize=8, color=P.muted())
a.set_ylabel("Mutual information / bit")
a.set_ylim(0, 2.45)
b.set_ylabel("Fraction of maximum information")
b.set_ylim(0, 1.02)
b.scatter([0.7], [info(5, 0.7) / np.log2(5)], color=P.ink(), s=20, zorder=5)
b.annotate(f"n = 5, q = 0.7: {info(5, 0.7) / np.log2(5):.2f}", (0.7, info(5, 0.7) / np.log2(5)), (0.33, 0.62),
           fontsize=8, arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A", loc="left", fontweight="bold")
b.set_title("B", loc="left", fontweight="bold")
fig.tight_layout()
