"""Decisions with a red line (Example 37.3.1).

A: expected payoffs of accepting and rejecting a male against the probability p that he is of high quality
(accept: 10 if high, 2 if low; reject: 5 regardless); the lines cross at the red line p* = 3/8.
B: Bayesian updating of the female's estimate over successive songs of a high-quality and a low-quality male
(fast song with probability 0.8 if high, 0.3 if low), starting from the prior 0.3.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))

p = np.linspace(0, 1, 200)
acc = 10 * p + 2 * (1 - p)
rej = np.full_like(p, 5.0)
pstar = 3 / 8
a.plot(p, acc, color=P.edge("dna"), lw=1.6, label="accept")
a.plot(p, rej, color=P.muted(), lw=1.6, label="reject")
a.plot(p, np.maximum(acc, rej), color=P.ink(), lw=3.2, alpha=0.35, label="best action")
a.axvline(pstar, color=P.edge("negative"), ls="--", lw=1.2)
a.text(pstar + 0.02, 9.3, "red line p* = 0.375", color=P.edge("negative"), fontsize=8)
a.scatter([0.3], [5], color=P.edge("rna"), zorder=5, s=25)
a.annotate("prior 0.3", (0.3, 5), (0.08, 7.2), fontsize=8, color=P.edge("rna"),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
a.set_xlabel("Probability that the male is of high quality, p")
a.set_ylabel("Expected payoff")
a.set_xlim(0, 1); a.set_ylim(1.5, 10.5)
a.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.88))
a.set_title("A", loc="left", fontweight="bold")

rng = np.random.default_rng(3)
n = 12
for qual, ph, tok, lab in ((1, 0.8, "dna", "high-quality male"), (0, 0.3, "rna", "low-quality male")):
    for rep in range(4):
        post = [0.3]
        for k in range(n):
            fast = rng.random() < ph
            pr = post[-1]
            l1, l0 = (0.8, 0.3) if fast else (0.2, 0.7)
            post.append(l1 * pr / (l1 * pr + l0 * (1 - pr)))
        b.plot(range(n + 1), post, color=P.edge(tok), lw=1.3 if rep == 0 else 0.9,
               alpha=1.0 if rep == 0 else 0.55, marker="o", ms=2.5, label=lab if rep == 0 else None)
b.axhline(pstar, color=P.edge("negative"), ls="--", lw=1.2)
b.text(n - 0.2, pstar + 0.03, "red line", ha="right", color=P.edge("negative"), fontsize=8)
b.set_xlabel("Number of songs heard")
b.set_ylabel("Posterior probability of high quality")
b.set_xlim(0, n); b.set_ylim(0, 1)
b.legend(frameon=False, fontsize=8, loc="lower center", bbox_to_anchor=(0.55, 1.0), ncol=2)
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
